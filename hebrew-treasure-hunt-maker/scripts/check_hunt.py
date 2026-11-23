#!/usr/bin/env python3
"""Check a home treasure hunt (hunt.json) before anything is printed.

No network access and no external packages. Reads one JSON file and prints a report.

  python3 check_hunt.py hunt.json          human-readable report
  python3 check_hunt.py hunt.json --json   machine-readable report
  python3 check_hunt.py --dates 2026       Hanukkah nights for a civil year
  python3 check_hunt.py --menus            the room, spot and prize menus

Exit codes: 0 no errors (warnings may remain), 1 the hunt has errors, 2 the file could not be
checked. Exit 2 is never a pass.

Rooms, hiding spots and prizes are IDs from closed menus below. The menus are a design choice of
this skill, not taken from any source, and anything off a menu is refused. Card text is free
Hebrew, so its scan is ADVISORY: it catches some wording and misses other wording. An adult reads
every card before hiding it, walks the route first and stays present. The script has not seen the
home. The youngest child PRESENT (players, guests and toddlers) sets the level.
"""

import argparse
import copy
import datetime as dt
import json
import math
import os
import re
import sys
import unicodedata

sys.dont_write_bytecode = True  # keep the skill folder free of build artifacts
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from niqqud_tools import adapt_word, hebrew_words, is_vocalized, letters_only, second_person_gender  # noqa: E402

STAGES = ("gan", "grade1", "grade2", "grade3", "grade4-6")
MODES = ("read", "adult_reads", "picture")

# ---------------------------------------------------------------- closed menus (a design choice)
ROOMS = {
    "living": {"label": "הסלון", "answer": "סלון"},
    "dining": {"label": "פינת האוכל", "answer": "פינת אוכל"},
    "kids_room": {"label": "חדר הילדים", "answer": "חדר הילדים"},
    "kids_room_2": {"label": "חדר הילדים השני", "answer": "חדר הילדים השני"},
    "bedroom": {"label": "חדר השינה", "answer": "חדר השינה"},
    "study": {"label": "חדר העבודה", "answer": "חדר העבודה"},
    "mamad": {"label": "הממ\"ד", "answer": "ממ\"ד"},
}
SPOTS = {
    "sofa_cushion": {"label": "מתחת לכרית בספה", "answer": "ספה", "aliases": [], "icon": "sofa"},
    "rug": {"label": "על השטיח", "answer": "שטיח", "aliases": [], "icon": "rug"},
    "floor_corner": {"label": "על הרצפה בפינת החדר", "answer": "פינה", "aliases": [], "icon": None},
    "under_table": {"label": "מתחת לשולחן, על הרצפה", "answer": "שולחן", "aliases": [], "icon": "table"},
    "under_chair": {"label": "מתחת לכיסא, על הרצפה", "answer": "כיסא", "aliases": [], "icon": "chair"},
    "low_books": {"label": "על המדף התחתון של הספרים", "answer": "ספרים", "aliases": ["ספר"], "icon": "book"},
    "toy_basket": {"label": "בתוך סל צעצועים פתוח שעל הרצפה", "answer": "סל", "aliases": [], "icon": "basket"},
    "low_bed": {"label": "מתחת לשמיכה במיטה נמוכה", "answer": "מיטה", "aliases": [], "icon": "bed"},
    "big_toy": {"label": "ליד בובה גדולה על הרצפה", "answer": "בובה", "aliases": ["דובי"], "icon": "teddy"},
}
CONTAINERS = {"box": "בתוך קופסה פתוחה", "envelope": "בתוך מעטפה"}
# min_age is the youngest age present that may have the prize. mouth: also out under 5 for a child who
# still mouths objects (no answer counts as yes). food: out when anyone under 5 is present, the skill's own
# stricter choice. writing: not on Shabbat.
PRIZES = {
    "large_book": {"label": "ספר גדול", "min_age": 0},
    "big_soft_toy": {"label": "בובה רכה גדולה בלי חלקים קטנים", "min_age": 0},
    "certificate_only": {"label": "התעודה בלבד", "min_age": 0},
    "paper_crown": {"label": "כתר נייר", "min_age": 3, "mouth": True},
    "sticker_sheet": {"label": "דף מדבקות", "min_age": 3, "mouth": True, "writing": True},
    "coloring_book": {"label": "חוברת צביעה", "min_age": 3, "mouth": True, "writing": True},
    "big_dreidel": {"label": "סביבון גדול עם תו תקן", "min_age": 5},
    "biscuit": {"label": "ביסקוויט", "min_age": 5, "food": True},
    "pretzel": {"label": "בייגלה", "min_age": 5, "food": True},
    "wafer": {"label": "וופל", "min_age": 5, "food": True},
    "nut_free_chocolate": {"label": "שוקולד בלי אגוזים", "min_age": 5, "food": True},
    "chocolate_coins": {"label": "מטבעות שוקולד בלי אגוזים (מבוגר מקלף)", "min_age": 5, "food": True},
}
OPEN_PLAN = {"living", "dining"}  # one space around candles unless the parent confirms a wall

# Working defaults for a card a child reads alone. These are this skill's defaults, not official figures.
JUST_STARTED_WORDS = 8
MAX_AGE = 18  # participants are children
MAX_WORDS = {"grade1": 14, "grade2": 26, "grade3": 40, "grade4-6": 60}
MIN_POINTED = {"grade1": 1.0, "grade2": 0.8, "grade3": 0.3}

FINALS = str.maketrans("ךםןףץ", "כמנפצ")
FINAL_PAIRS = {"ך": "כ", "ם": "מ", "ן": "נ", "ף": "פ", "ץ": "צ"}
HEB = "א-ת"
PREFIX = "[ובלהמשכ]{0,2}"
SUFFIX = "(?:ים|ות|ה|ית|יות|י|ת)?"
SYNONYMS = [{"ממד", "מרחב מוגן", "חדר מוגן", "חדר ביטחון", "חדר בטחון", "mamad"}, {"ספה", "ספות", "sofa", "couch"},
            {"מיטה", "bed"}, {"שטיח", "rug", "carpet"}, {"כרית", "כריות", "pillow", "cushion"}, {"שולחן", "table"},
            {"ספר", "ספרים", "book", "books"}, {"סל", "basket"}, {"כיסא", "chair"}, {"בובה", "דובי", "doll", "teddy"}]
NOT_THE_ANSWER = {"מטה", "למטה", "מלמטה", "סיפור", "סיפורים", "סיפורי", "לספר", "סיפר", "סיפרה", "מספר", "מספרים",
                  "סופר", "ספור", "כורת", "שולח", "שולחת", "סלון", "בסלון", "לסלון", "הסלון", "מהסלון"}

# ---------------------------------------------------------------- advisory scan of card text
CARD_PLACES = [
    "מרפסת", "מירפסת", "חלון", "חלונות", "גג", "מעקה", "מקרר", "מקפיא", "מדיח", "מכונת כביסה", "מכונה", "כביסה", "מכבסים",
    "מייבש", "ארגז", "צידנית", "מזוודה", "ארון", "ארונות", "תנור", "כיריים", "קומקום", "מיחם", "פלטה", "מיקרוגל", "תרופה",
    "תרופות", "חומרי ניקוי", "אקונומיקה", "סכין", "סכינים", "מספריים", "אמבטיה", "שירותים", "אסלה", "מקלחת", "דלי", "כיור",
    "שקע", "מדרגות", "מעלית", "לובי", "מחסן", "מרתף", "מטבח", "בוידעם", "מגירה", "מאחורי הטלויזיה", "balcony", "window",
    "roof", "fridge", "oven", "stove", "washing machine", "bathroom", "toilet", "stairs", "kitchen",
]
CANDLE_WORDS = ["נר", "נרות", "חנוכיה", "חנוכית", "חנוכיות", "פמוט", "פמוטים", "אש", "להבה", "candle", "flame"]
TOWARD_WORDS = ["ליד", "אצל", "מתחת", "מאחורי", "חפשו", "חפש", "חפשי", "לכו", "לך", "לכי", "גשו", "גש", "גשי", "הביטו", "near", "beside"]


def verb_rx(forms):
    return f"(?<![{HEB}])[ו]?(?:{'|'.join(forms)})(?![{HEB}])"


DANGER_RX = [
    ("climbing", verb_rx(["טפס", "טפסי", "טפסו", "תטפס", "תטפסי", "תטפסו", "לטפס"])),
    ("tasting", verb_rx(["טעמי", "טעמו", "טעום", "תטעם", "תטעמי", "תטעמו", "לטעום"])),
    ("lighting", verb_rx(["הדלק", "הדליקי", "הדליקו", "תדליק", "תדליקי", "תדליקו", "להדליק"])),
    ("moving furniture", verb_rx(["הזז", "הזיזי", "הזיזו", "תזיז", "תזיזי", "תזיזו", "להזיז"])),
    ("burning or heating", verb_rx(["שרוף", "שרפי", "שרפו", "תשרוף", "תשרפי", "תשרפו", "לשרוף", "חמם", "חממי", "חממו", "לחמם"])),
    ("hiding", verb_rx(["התחבא", "התחבאי", "התחבאו", "תתחבא", "תתחבאי", "תתחבאו", "להתחבא"])),
    ("jumping", verb_rx(["קפוץ", "קפצי", "קפצו", "תקפוץ", "תקפצי", "תקפצו", "לקפוץ"])),
    ("getting inside", verb_rx(["היכנס", "היכנסי", "היכנסו", "הכנס", "הכנסי", "הכנסו", "כנס", "כנסי", "כנסו", "תיכנס", "תיכנסי",
                                "תיכנסו", "תכנס", "תכנסי", "תכנסו", "להיכנס", "להכנס"]) + r"\s+לתוך"),
    ("getting up on furniture", verb_rx(["עלה", "עלי", "עלו", "תעלה", "תעלי", "תעלו", "לעלות", "עמוד", "עמדי", "עמדו", "תעמוד",
                                         "תעמדי", "תעמדו", "לעמוד"]) + r"\s+על"),
    ("leaving the home", r"(?<![א-ת])(?:החוצה|מהדירה|מהבית)(?![א-ת])"),
    ("pulling or reaching", verb_rx(["משוך", "משכי", "משכו", "תמשוך", "תמשכי", "תמשכו", "למשוך", "הושט", "הושיטי", "הושיטו"])),
    ("something burning", verb_rx(["דולק", "דולקת", "דולקים", "דולקות", "שדולק", "שדולקת", "הדולק", "הדולקים", "הדולקת", "הדולקות"])),
    ("looking high up", r"(?<![א-ת])למעלה(?![א-ת])|(?<![א-ת])הכי גבוה(?![א-ת])"),
    ("climbing", r"\bclimb\b"), ("tasting", r"\btaste\b"), ("burning", r"\bburn\b"), ("lighting", r"\blight the\b"),
]
DOOR_SHUT_RX = verb_rx(["סגור", "סגרי", "סגרו", "תסגור", "תסגרי", "תסגרו", "לסגור"]) + r"\s+(?:את\s+)?ה?דלת"
LOCK_WORDS = ["לנעול", "ננעל", "ננעלת", "ננעלים", "נעולה", "נעולים", "נעול", "נעלו את", "דלת סגורה", "locked", "lock the", "shut the door"]
LOCK_NOUNS = ["מנעול", "מנעולים", "padlock", "lock"]
DARK_WORDS = ["חושך", "כבו את האור", "לכבות את האור", "in the dark", "lights off"]
SHABBAT_ACTIONS = ["כתבו", "כתבי", "כתוב", "לכתוב", "תכתוב", "תכתבי", "תכתבו", "רשמו", "רשמי", "רשום", "לרשום", "תרשום", "תרשמי",
                   "תרשמו", "סמנו", "סמני", "סמן", "לסמן", "תסמן", "תסמני", "תסמנו", "הקיפו", "הקיפי", "הקף", "להקיף", "תקיף", "תקיפי",
                   "תקיפו", "מחקו", "מחקי", "למחוק", "תמחק", "תמחקי", "תמחקו", "קרעו", "קרעי", "לקרוע", "תקרע", "תקרעי", "תקרעו",
                   "גזרו", "גזרי", "גזור", "לגזור", "תגזור", "תגזרי", "תגזרו", "הדביקו", "הדביקי", "הדבק", "להדביק", "תדביק", "תדביקי",
                   "תדביקו", "ציירו", "ציירי", "לצייר", "תצייר", "תציירי", "תציירו", "צבעו", "צבעי", "לצבוע", "תצבעי", "תצבעו",
                   "טיימר", "שעון עצר", "טלפון", "פלאפון", "סלולרי", "טאבלט", "רמקול", "פנס", "מצלמה", "כבו", "כבי", "write", "cut out",
                   "glue", "tape", "timer", "phone", "tablet", "speaker", "flashlight", "camera"]
OTHER_MASC = {"חפש", "בוא", "גש", "הסתכל", "רוץ", "תמצא", "תחפש", "תלך", "תראה", "תסתכל", "אתה", "תבוא", "תגש", "שים"}
OTHER_FEM = {"חפשי", "בואי", "גשי", "הסתכלי", "רוצי", "תמצאי", "תחפשי", "תלכי", "תראי", "תסתכלי", "תבואי", "תגשי", "שימי", "לכי"}
ATBASH = {a: b for a, b in zip("אבגדהוזחטיכלמנסעפצקרשת", "תשרקצפעסנמלכיטחזוהדגבא")}


def plain(s):
    """Lower-case text without niqqud or quotes, hyphens as spaces, doubled yod and vav collapsed."""
    s = unicodedata.normalize("NFC", s or "").lower()
    s = "".join(c for c in s if not "֑" <= c <= "ׇ" or c == "־")
    s = re.sub("[\"'׳״‘’“”`]", "", s)
    s = re.sub("[-־‐-―/]", " ", s)
    return s.replace("יי", "י").replace("וו", "ו")


def term_rx(term):
    t = plain(term)
    if not re.search(f"[{HEB}]", t):
        return rf"\b{re.escape(t)}(?:s|es)?\b"
    words = t.split()
    body = r"\s+ה?".join(re.escape(w) for w in words)  # definite construct: מכונת הכביסה
    tail = SUFFIX if len(words[-1]) >= 4 else ""
    if tail and body[-1] in FINAL_PAIRS:  # a final letter takes its regular form before an ending
        body = body[:-1] + f"[{body[-1]}{FINAL_PAIRS[body[-1]]}]"
    return f"(?<![{HEB}]){PREFIX}{body}{tail}(?![{HEB}])"


def find_terms(terms, text):
    t = plain(text)
    return [x for x in terms if re.search(term_rx(x), t)]


# ---------------------------------------------------------------- calendar
def hebrew_new_year(y):
    """Fixed day of 1 Tishri of Hebrew year y (arithmetic Hebrew calendar)."""
    def elapsed(yr):
        months = (235 * yr - 234) // 19
        parts = 12084 + 13753 * months
        day = 29 * months + parts // 25920
        return day + 1 if (3 * (day + 1)) % 7 < 3 else day
    a, b, c = elapsed(y - 1), elapsed(y), elapsed(y + 1)
    correction = 2 if c - b == 356 else 1 if b - a == 382 else 0
    return -1373427 + b + correction


def hanukkah_nights(civil_year):
    """Civil dates of the eight candle-lighting evenings of the Hanukkah that starts in civil_year."""
    hy = civil_year + 3761
    length = hebrew_new_year(hy + 1) - hebrew_new_year(hy)
    cheshvan = 30 if length % 10 == 5 else 29
    day25 = hebrew_new_year(hy) + 30 + cheshvan + 24
    return [dt.date.fromordinal(day25 - 1 + i) for i in range(8)]


def hanukkah_containing(d):
    """The eight lighting evenings of the Hanukkah that includes date d (through the eighth day), or None."""
    for y in (d.year, d.year - 1):
        nights = hanukkah_nights(y)
        if nights[0] <= d <= nights[-1] + dt.timedelta(days=1):
            return nights
    return None


def hanukkah_lines(civil_year):
    out = []
    for i, d in enumerate(hanukkah_nights(civil_year), start=1):
        w = d.weekday()
        note = "Friday: light before sundown, before Shabbat candles" if w == 4 else (
            "Saturday night: after nightfall" if w == 5 else "dusk")
        out.append(f"night {i}: {d.strftime('%a %d %b %Y')} ({note})")
    return out


def festival_days(civil_year):
    """Israeli Yom Tov days (daytime dates): Rosh Hashana, Yom Kippur, Sukkot, Shemini Atzeret, Pesach 1 and 7, Shavuot."""
    days = set()
    for hy in range(civil_year + 3759, civil_year + 3763):
        ny = hebrew_new_year(hy)
        days |= {ny, ny + 1, ny + 9, ny + 14, ny + 21, ny - 163, ny - 157, ny - 113}
    return {dt.date.fromordinal(x) for x in days}


def to_min(s):
    if not s:
        return None
    m = re.fullmatch(r"(\d{1,2}):(\d{2})", str(s))
    if not m or int(m.group(1)) > 23 or int(m.group(2)) > 59:
        raise ValueError(f"bad time {s!r}, expected HH:MM")
    return int(m.group(1)) * 60 + int(m.group(2))


def is_sacred(d):
    return d.weekday() == 5 or d in festival_days(d.year)


def shabbat_status(sch):
    """True if the hunt falls on Shabbat or Yom Tov, False if not, None when the times are not enough to tell."""
    if sch.get("yom_tov") is True:
        return True
    d = dt.date.fromisoformat(sch["date"])
    start, end = to_min(sch.get("start")), to_min(sch.get("end"))
    light, out = to_min(sch.get("candle_lighting")), to_min(sch.get("havdalah"))
    next_sacred = is_sacred(d + dt.timedelta(days=1))
    if is_sacred(d):
        if next_sacred:
            return True
        return not (start is not None and out is not None and start >= out)
    if next_sacred:
        if light is None or end is None:  # a missing end is never read as the start time
            return None
        return end > light
    return False


# ---------------------------------------------------------------- answers in riddles
def skel(word):
    """Spelling-blind form: no niqqud, no final forms, no alef, vav or yod, and a final he dropped."""
    out = plain(word).translate(FINALS).replace("ו", "").replace("י", "").replace("א", "")
    return " ".join(w[:-1] if len(w) > 2 and w.endswith("ה") else w for w in out.split())


def answer_forms(station):
    forms = {station.get("answer", "")} | set(station.get("aliases") or [])
    sk = {skel(f).strip() for f in forms if f}
    for group in SYNONYMS:
        gs = {skel(x) for x in group}
        if sk & gs:
            sk |= gs
    return {x for x in sk if x}


def contains_answer(text, forms):
    """The answer in any spelling the script knows: prefixes, plurals, inside a compound, reversed or spelled out."""
    raw = re.findall(rf"[{HEB}A-Za-z]+", plain(text))
    toks = [skel(t) for t in raw if t not in NOT_THE_ANSWER]
    singles, runs = "", []
    for t in toks:
        if len(t) == 1:
            singles += t
        else:
            if len(singles) > 1:
                runs.append(singles)
            singles = ""
    if len(singles) > 1:
        runs.append(singles)
    for f in forms:
        if " " in f:
            bare = [t[1:] if len(t) > 2 and t[0] in "הבלמ" else t for t in toks]
            if f" {f} " in f" {' '.join(toks)} " or f" {f} " in f" {' '.join(bare)} ":
                return f
            continue
        if any(f in r or f[::-1] in r for r in runs):
            return f
        for t in toks:
            if t == f[::-1] and len(f) > 2:
                return f
            if len(t) > len(f) and t.endswith(f) and len(f) >= 2 and not all(c in "בלהמשכ" for c in t[:-len(f)]):
                return f  # a compound ending in the answer, such as כדורסל for סל
            for cut in range(0, 3):
                if cut and not all(c in "בלהמשכ" for c in t[:cut]):
                    break
                stem = t[cut:]
                if stem == f or (stem.startswith(f) and stem[len(f):] in ("מ", "ת", "ה", "נ")):
                    return f
    return None


class Report:
    def __init__(self):
        self.errors, self.warnings, self.checks = [], [], []
        self.youngest, self.hunt = None, None

    def err(self, code, where, message, fix=""):
        self.errors.append({"code": code, "where": where, "message": message, "fix": fix})

    def warn(self, code, where, message, fix=""):
        self.warnings.append({"code": code, "where": where, "message": message, "fix": fix})


def valid_age(age):
    """Fail closed: a missing, non-numeric, boolean, NaN, infinite, negative or implausible age is not an age."""
    if isinstance(age, bool) or not isinstance(age, (int, float)):
        return False
    if isinstance(age, float) and not math.isfinite(age):  # isfinite overflows on a huge int, so floats only
        return False
    return 0 <= age <= MAX_AGE


def menu_text(menu):
    return ", ".join(f"{k} ({v['label']})" for k, v in menu.items())


def check_schema(h, r):
    for key in ("title", "occasion", "format", "keeps_shabbat", "younger_or_guests_asked", "host_is_adult", "adult_stays_present",
                "adults_present", "candles", "schedule", "home", "participants", "start", "stations", "treasure"):
        if key not in h:
            r.err("SCHEMA", key, f"required field {key} is missing",
                  "keeps_shabbat, adults_present, candles and younger_or_guests_asked come from asking the parent, never from a guess")
    if r.errors:
        return False
    if not isinstance(h["keeps_shabbat"], bool):
        r.err("SCHEMA", "keeps_shabbat", "must be true or false after asking the parent")
    if not isinstance(h["adults_present"], int) or isinstance(h["adults_present"], bool) or h["adults_present"] < 1:
        r.err("NO_ADULT", "adults_present", "state how many adults stay for the whole game (at least one)",
              "שואלים כמה מבוגרים יישארו לאורך כל המשחק")
    if h["younger_or_guests_asked"] is not True:
        r.err("GUESTS_NOT_ASKED", "younger_or_guests_asked", "ask whether guests or younger children will be present",
              "שואלים: יהיו בבית אורחים או ילדים צעירים יותר, גם אם לא משחקים?")
    if h["format"] not in ("treasure_hunt", "escape_room"):
        r.err("SCHEMA", "format", "must be treasure_hunt or escape_room")
    if not isinstance(h["candles"], dict) or not isinstance(h["candles"].get("lit_during_hunt"), bool):
        r.err("SCHEMA", "candles.lit_during_hunt", "on any date, ask whether candles will be lit in the home during the hunt",
              "שואלים: יהיו נרות דולקים בבית בזמן המשחק (שבת, חג, חנוכה)?")
    try:
        dt.date.fromisoformat(h["schedule"].get("date", ""))
        for k in ("start", "end", "candle_lighting", "havdalah"):
            to_min(h["schedule"].get(k))
        if h["schedule"].get("start") and h["schedule"].get("end") and to_min(h["schedule"]["end"]) <= to_min(h["schedule"]["start"]):
            r.err("TIME_ORDER", "schedule", "the end time must be after the start time; a hunt that crosses midnight is out of scope", "מתקנים את שעת הסיום, כך שתהיה אחרי ההתחלה ובאותו יום")
    except (ValueError, TypeError) as e:
        r.err("SCHEMA", "schedule", f"bad date or time: {e}")
    if not h["participants"]:
        r.err("SCHEMA", "participants", "at least one participant is required")
    ids = set()
    for p in h["participants"]:
        pid = p.get("id", "?")
        for key in ("id", "role"):
            if key not in p:
                r.err("SCHEMA", f"participant {pid}", f"missing {key}")
        if not isinstance(p.get("guest"), bool):
            r.err("SCHEMA", f"participant {pid}", "guest must be true or false: is this child from another family?",
                  "מסמנים לכל ילד אם הוא מהמשפחה או אורח")
        if p.get("id") in ids:
            r.err("SCHEMA", f"participant {pid}", "duplicate id")
        ids.add(p.get("id"))
        if not valid_age(p.get("age")):
            r.err("AGE_INVALID", f"participant {pid}", f"age must be a real number from 0 to {MAX_AGE}, so no youngest-child rule is skipped",
                  "שואלים את ההורה מה הגיל של הילד")
        if p.get("role") not in ("player", "present"):
            r.err("SCHEMA", f"participant {pid}", "role must be player or present")
        if p.get("role") == "present" and p.get("name"):
            r.err("NAME_NON_PLAYER", f"participant {pid}", "children who are not playing are listed by age only, with no name")
        if p.get("role") == "player":
            name = str(p.get("name", "")).strip()
            if not name:
                r.err("SCHEMA", f"participant {pid}", "a player needs a first name or nickname")
            if re.search(r"\d", name):
                r.err("PRIVACY", f"participant {pid}", "a name field must not hold digits or an identifier",
                      "משתמשים בשם פרטי או בכינוי בלבד")
            if len(name.split()) > 1:
                r.err("ONE_CHILD_PER_ROW", f"participant {pid}", "one first name or nickname per row, so a pair cannot hide a younger child's age",
                      "רושמים כל ילד בנפרד עם הגיל שלו, ומילה אחת בשם")
            if find_terms(["הקטנים", "הגדולים", "הילדים", "קבוצה", "צוות", "כולם", "team", "group", "kids"], name):
                r.err("ONE_CHILD_PER_ROW", f"participant {pid}", "list each child separately", "רושמים כל ילד בנפרד עם הגיל שלו")
            if p.get("address") not in ("m", "f", "plural"):
                r.err("GENDER_NOT_ASKED", f"participant {pid}", "address must be m, f or plural, taken from the parent; never infer it from a name")
            if p.get("reading_stage") not in STAGES:
                r.err("SCHEMA", f"participant {pid}", f"reading_stage must be one of {STAGES}")
    if not any(p.get("role") == "player" for p in h["participants"]):
        r.err("SCHEMA", "participants", "at least one player is required")
    if h.get("props"):
        r.err("OFF_MENU_PRIZE", "props", "free-form props are not accepted. A box or envelope is set with a station's container field",
              "מסירים את האביזר, או בוחרים קופסה או מעטפה בתחנה")
    for s in h["stations"]:
        sid = s.get("id", "?")
        if not s.get("id"):
            r.err("SCHEMA", f"station {sid}", "missing id")
        if any(k in s for k in ("room", "room_type", "spot", "height")):
            r.err("FREE_TEXT_PLACE", f"station {sid}", "places are menu IDs: use room_id and spot_id, not free text",
                  "בוחרים חדר ומקום מהתפריט")
        if s.get("room_id") not in ROOMS:
            r.err("OFF_MENU_ROOM", f"station {sid}", f"room_id must be one of: {menu_text(ROOMS)}",
                  "ממפים את החדר לחדר מהתפריט, או מוותרים על התחנה. מטבח, מרפסת, שירותים, מחסן ומסדרון לא בתפריט")
        if s.get("spot_id") not in SPOTS:
            r.err("OFF_MENU_SPOT", f"station {sid}", f"spot_id must be one of: {menu_text(SPOTS)}", "בוחרים מקום מהתפריט")
        if s.get("room_id") == "study" and s.get("spot_id") == "under_table":
            r.err("OFF_MENU_SPOT", f"station {sid}", "under the desk in the study is off the menu, because cables and power strips usually sit there",
                  "בוחרים מקום אחר בחדר העבודה, למשל על השטיח")
        if s.get("answer_from", "spot") not in ("spot", "room"):
            r.err("SCHEMA", f"station {sid}", "answer_from must be spot or room")
        if s.get("container") is not None and (s["container"] not in CONTAINERS or h["format"] != "escape_room"):
            r.err("OFF_MENU_SPOT", f"station {sid}", "container is box or envelope, in an escape room only", "מסירים את המיכל")
    prizes = h["treasure"].get("prizes")
    if not isinstance(prizes, list) or not prizes:
        r.err("OFF_MENU_PRIZE", "treasure.prizes", f"pick at least one prize ID: {menu_text(PRIZES)}", "בוחרים פרס מהתפריט")
    else:
        for pz in prizes:
            if not isinstance(pz, str) or pz not in PRIZES:
                r.err("OFF_MENU_PRIZE", f"prize {pz!r}", f"prizes are menu IDs: {menu_text(PRIZES)}", "בוחרים פרס מהתפריט")
    return not r.errors


def resolve(h, r):
    """Copy the hunt and fill each station's printed labels and answer from the menus."""
    out = copy.deepcopy(h)
    players = {p["id"]: p for p in out["participants"] if p["role"] == "player"}
    for s in out["stations"]:
        room, spot = ROOMS[s["room_id"]], SPOTS[s["spot_id"]]
        label = spot["label"]
        owner = s.get("owner_id")
        if owner is not None and owner not in players:
            r.err("SCHEMA", f"station {s['id']}", "owner_id must be a player id")
        elif owner is not None:
            label += f" של {players[owner]['name']}"
        if s["spot_id"] == "low_bed":
            if len(players) > 1 and owner is None:
                r.err("WHOSE_BED", f"station {s['id']}", "with more than one child, say whose bed (owner_id), so the clue has one answer",
                      "בוחרים של מי המיטה, והחידה אומרת את זה")
            if out["home"].get("bed_is_low") is not True:
                r.err("BED_NOT_CONFIRMED", f"station {s['id']}", "confirm this is a low bed and not a bunk (home.bed_is_low)",
                      "מאשרים שהמיטה נמוכה, או בוחרים מקום אחר")
        if s.get("container"):
            label = f"{CONTAINERS[s['container']]}, {label}"
        s["room"], s["spot"] = room["label"], label
        if s.get("answer_from") == "room":
            s["answer"], s["aliases"], s["icon"] = room["answer"], [], None
        else:
            s["answer"], s["aliases"], s["icon"] = spot["answer"], spot["aliases"], spot["icon"]
    return out


def check_people(h, r):
    r.checks.append("the youngest child present (guests and toddlers included) sets the level")
    if h["host_is_adult"] is not True or h["adult_stays_present"] is not True:
        r.err("NO_ADULT", "host", "an adult hosts and stays present for the whole hunt",
              "מבוגר נשאר בבית ועם הילדים לאורך כל המשחק, גם אם ילד גדול עוזר")
    players = [p for p in h["participants"] if p["role"] == "player"]
    if len(players) > 4:
        r.warn("MANY_PLAYERS", "participants", "this kit prints a card per child per step; with more than four players it gets long")
    youngest = min(p["age"] for p in h["participants"])
    rooms = {s["room_id"] for s in h["stations"]}
    free_adults = h["adults_present"] - (1 if h["candles"]["lit_during_hunt"] else 0)  # one adult stays with lit candles
    if free_adults < 1:
        r.err("NO_ADULT_FOR_CHILDREN", "adults_present", "with candles lit, one adult stays with them and no adult remains with the children",
              "משחקים לפני ההדלקה או אחרי שהנרות כבו, או מוסיפים מבוגר")
    elif any(p.get("guest") for p in h["participants"]) and youngest < 6 and free_adults < 2 and len(rooms) > 1:
        r.err("ADULT_RATIO", "adults_present", "guests, a child under 6 and one free adult across several rooms (common-practice rule of this skill; an adult staying with candles does not count)",
              "מוסיפים מבוגר או מקצרים את המשחק לחדר אחד, או משחקים כשהנרות לא דולקים")
    return youngest, players


def check_mamad(h, r):
    r.checks.append("the way to the protected space is confirmed clear")
    home = h["home"]
    space = home.get("protected_space")
    if space not in ("mamad", "mamak", "shelter", "stairwell", "none"):
        r.err("SCHEMA", "home.protected_space", "must be mamad, mamak, shelter, stairwell or none")
        return
    if space == "none":
        if not str(home.get("siren_place", "")).strip():
            r.err("SIREN_PLACE", "home", "with no protected space, ask where the family goes on a siren and record it in home.siren_place",
                  "שואלים לאן הולכים באזעקה, לפי הנחיות פיקוד העורף")
        return
    if home.get("protected_route_clear") is not True:
        r.err("MAMAD_BLOCKED", "home", "confirm that nothing in the game blocks the way to the protected space",
              "מפנים מהמעבר כיסאות, שקיות, שטיחים ואביזרי משחק, ומאשרים ב-protected_route_clear")
    if any(s["room_id"] == "mamad" for s in h["stations"]) and home.get("mamad_nothing_breakable") is not True:
        r.err("MAMAD_BREAKABLE", "home", "a mamad station must add nothing that can shatter or ignite",
              "משאירים בממ\"ד רק נייר ובד, ומאשרים ב-mamad_nothing_breakable")


def check_route(h, r):
    r.checks.append("route logic: each card leads to the next station's menu spot, no dead ends, no loops, treasure last")
    by_id, answers = {}, {}
    for s in h["stations"]:
        if s["id"] in by_id:
            r.err("ROUTE", f"station {s['id']}", "duplicate station id")
        by_id[s["id"]] = s
        key = skel(s["answer"])
        if key in answers:
            r.err("ROUTE", f"station {s['id']}", f"same answer as station {answers[key]}: children would be sent back", "בוחרים מקום אחר לתחנה")
        answers[key] = s["id"]
    treasures = [s for s in h["stations"] if s.get("treasure")]
    if len(treasures) != 1:
        r.err("ROUTE", "stations", f"expected exactly one treasure station, found {len(treasures)}")
    cur, seen = h["start"].get("next"), []
    while cur is not None:
        if cur in seen:
            r.err("ROUTE", f"station {cur}", "the route loops back to a station it already visited")
            break
        if cur not in by_id:
            r.err("ROUTE", f"station {cur}", "a clue points to a station that does not exist")
            break
        seen.append(cur)
        st = by_id[cur]
        if st.get("treasure"):
            if st.get("next"):
                r.err("ROUTE", f"station {cur}", "the treasure must be the end of the route")
            break
        if not st.get("next"):
            r.err("ROUTE", f"station {cur}", "dead end: this station has no next station and is not the treasure")
        cur = st.get("next")
    missing = [i for i in by_id if i not in seen]
    if missing:
        r.err("ROUTE", "stations", f"not reachable from the start: {', '.join(missing)}")
    return by_id


def word_list(text):
    return re.findall(rf"[֑-ׇ{HEB}]+", unicodedata.normalize("NFC", text or ""))


def check_reading(where, clue, p, target, r):
    stage = p["reading_stage"]
    mode = clue.get("mode", "read")
    if mode not in MODES:
        r.err("SCHEMA", where, f"mode must be one of {MODES}")
        return
    if mode == "picture" and not (target or {}).get("icon"):
        r.err("READING", where, "this destination has no picture on the menu: use adult_reads", "מחליפים לחידה שמבוגר מקריא")
    if stage == "gan":
        if mode == "read":
            r.err("READING", where, "a pre-reader must never need to read to progress",
                  "מחליפים לחידה שמבוגר מקריא (adult_reads) או לחידת תמונה (picture)")
        return
    if mode != "read":
        return
    words = [w for w in hebrew_words(clue.get("text", "")) if len(letters_only(w)) >= 2]
    if not words:
        r.err("READING", where, "the card has no Hebrew text")
        return
    limit = JUST_STARTED_WORDS if p.get("just_started") else MAX_WORDS[stage]
    if len(words) > limit:
        r.warn("READING", where, f"{len(words)} words is long for this reader (default limit {limit})", "מקצרים למשפט אחד או שניים")
    ratio = sum(1 for w in words if is_vocalized(w)) / len(words)
    need = 1.0 if clue.get("rhymed") and stage in ("grade2", "grade3") else MIN_POINTED.get(stage)
    if need is not None and ratio < need:
        bad = [w for w in words if not is_vocalized(w)][:5]
        r.err("NIQQUD_LEVEL", where, f"only {round(ratio * 100)} of 100 words carry niqqud for {stage}: {' '.join(bad)}",
              "מנקדים דרך דיקטה לפי references/niqqud-routes.md, לא ניקוד ידני של המודל")
    if stage == "grade1":
        nfc = lambda x: unicodedata.normalize("NFC", x)
        strong = [w for w in words if is_vocalized(w) and nfc(adapt_word(w, "grade1")) != nfc(w)]
        if strong:
            r.err("NIQQUD_GRADE1", where, "marks the grade 1 guideline drops (strong dagesh, mappiq, shin dot): " + " ".join(strong[:6]),
                  "מריצים: python3 scripts/niqqud_tools.py adapt --stage grade1")


def check_gender(where, text, p, r):
    want = p["address"]
    bad = []
    for w in word_list(text):
        g = second_person_gender(w) if is_vocalized(w) else None
        if g == "u" or (g and want != g):
            bad.append(w)
        core = letters_only(w)
        core = core[1:] if len(core) > 3 and core[0] == "ו" else core
        if not g:
            if core in OTHER_MASC and want != "m":
                bad.append(w)
            elif core in OTHER_FEM and want != "f":
                bad.append(w)
    if bad:
        label = {"m": "masculine", "f": "feminine", "plural": "plural"}[want]
        r.err("GENDER", where, f"form does not match {p['name']} ({label}): {' '.join(sorted(set(bad)))}",
              "מתקנים לפי טבלת הפנייה ב-references/reading-stages.md")


def check_puzzle(where, puzzle, answer, r):
    kind = puzzle.get("type")
    target = plain(answer).replace(" ", "").translate(FINALS)
    cipher = plain(puzzle.get("cipher", "")).replace(" ", "").translate(FINALS)
    if kind == "atbash":
        if "".join(ATBASH.get(c, c) for c in cipher) != target:
            r.err("PUZZLE", where, f"the atbash cipher does not decode to {answer}")
    elif kind == "scramble":
        if sorted(cipher) != sorted(target) or cipher == target:
            r.err("PUZZLE", where, f"the scramble is not a rearrangement of {answer}")
    else:
        r.err("PUZZLE", where, "puzzle type must be atbash or scramble")


def scan_card(where, clue, r):
    """Advisory scan. It flags some unsafe wording. A clean scan says nothing about wording it does not know."""
    hints = clue.get("hints") if isinstance(clue.get("hints"), list) else []
    all_text = " ".join([clue.get("text", "")] + [x for x in hints if isinstance(x, str)])
    flat = plain(all_text)
    places = find_terms(CARD_PLACES, all_text)
    if places:
        r.err("CARD_PLACE", where, f"the card or hint points to a place off the menu: {', '.join(places)}",
              "כותבים את החידה מחדש כך שתוביל רק למקום מהתפריט")
    for sentence in re.split(r"[.!?\n]+", all_text):
        if find_terms(CANDLE_WORDS, sentence) and find_terms(TOWARD_WORDS, sentence):
            r.err("CARD_CANDLES", where, "the card sends a child toward candles or fire", "אפשר להזכיר נר בסיפור, בלי לשלוח ילד אליו")
            break
    actions = sorted({label for label, rx in DANGER_RX if re.search(rx, flat)})
    if actions:
        r.err("DANGEROUS_ACTION", where, f"the wording asks for an unsafe action: {', '.join(actions)}",
              "כותבים בלי טיפוס, טעימה, הדלקה, קפיצה, התחבאות, יציאה מהבית או הזזת רהיטים")
    lock_flat = flat
    has_door = bool(find_terms(["דלת", "door"], flat))
    if clue.get("pretend_lock") and find_terms(["קופסה", "מעטפה", "box", "envelope"], flat) and not has_door:
        lock_flat = re.sub(rf"[{HEB}]*מנעול[{HEB}]*", " ", flat)
    locks = find_terms(LOCK_WORDS + LOCK_NOUNS, lock_flat)
    if re.search(DOOR_SHUT_RX, flat):
        locks.append("shutting a door")
    if locks:
        r.err("REAL_LOCK", where, f"nothing may lock or shut a child in: {', '.join(locks)}",
              "משתמשים בקופסה או במעטפה עם קוד מדומה, והדלתות נשארות פתוחות")
    if has_door and (find_terms(["ממד", "מרחב מוגן", "דלת כבדה"], flat)):
        r.err("MAMAD_DOOR", where, "the heavy protected-room door is never part of the game", "כותבים בלי הדלת")
    if find_terms(DARK_WORDS, all_text):
        r.err("DARKNESS", where, "no game in the dark", "משאירים אור דולק לכל אורך המשחק")


def check_clue(where, clue, target, p, r):
    if not isinstance(clue, dict):
        r.err("ROUTE", where, f"missing clue for {p['name']}")
        return
    if target is None:
        return
    if clue.get("answer") and skel(clue["answer"]).strip() not in answer_forms(target):
        r.err("ROUTE", where, f"the clue's answer ({clue['answer']}) is not the next station ({target['answer']})")
    forms = answer_forms(target)
    text = clue.get("text", "")
    if clue.get("mode") != "picture" and not text.strip():
        r.err("READING", where, "the clue has no text")
    if contains_answer(text, forms):
        r.err("ANSWER_IN_RIDDLE", where, f"the riddle prints its own answer ({target['answer']})",
              "כותבים את החידה מחדש בלי המילה, בלי שורש שלה ובלי לאיית אותה")
    hints = clue.get("hints")
    if not isinstance(hints, list) or len(hints) != 3 or not all(isinstance(x, str) and x.strip() for x in hints):
        r.err("HINTS", where, "needs exactly three hints: a nudge, a stronger hint, and the answer with why")
    else:
        for i in (0, 1):
            if contains_answer(hints[i], forms):
                r.err("HINTS", where, f"hint {i + 1} gives the answer away; only hint 3 may say it")
        if not contains_answer(hints[2], forms):
            r.err("HINTS", where, "hint 3 must state the answer and explain it")
    if clue.get("puzzle"):
        check_puzzle(where, clue["puzzle"], target["answer"], r)
    scan_card(where, clue, r)
    check_reading(where, clue, p, target, r)
    check_gender(where, " ".join([text] + (hints if isinstance(hints, list) else [])), p, r)


def check_clues(h, by_id, players, r):
    r.checks.append("riddles and early hints do not print the answer, in the spelling forms the script knows")
    r.checks.append("reading level and niqqud for each child; gender forms the script knows")
    r.checks.append("each child has a clue at every step, and every step has three hints")
    r.checks.append("advisory scan of card text: it catches some unsafe wording and misses other wording, so an adult reads every card")
    first = by_id.get(h["start"].get("next"))
    for p in players:
        check_clue(f"start clue for {p['name']}", (h["start"].get("clues") or {}).get(p["id"]), first, p, r)
    for s in h["stations"]:
        if s.get("treasure"):
            continue
        target = by_id.get(s.get("next"))
        for p in players:
            check_clue(f"station {s['id']} clue for {p['name']}", (s.get("clues") or {}).get(p["id"]), target, p, r)


def check_prizes(h, youngest, on_shabbat, r):
    r.checks.append("prizes come from a closed menu, with age limits for the youngest child present")
    mouths = h.get("still_mouths_objects") is not False  # no answer counts as yes
    foods = []
    for pid in h["treasure"]["prizes"]:
        pz = PRIZES[pid]
        if pz.get("food"):
            foods.append(pid)
            if youngest < 5:
                r.err("NO_FOOD_UNDER_5", f"prize {pid}", f"no food prizes when anyone under 5 is present, this skill's own stricter choice (youngest: {youngest})",
                      "בוחרים ספר גדול או בובה רכה גדולה בלי חלקים קטנים")
                continue
        elif youngest < pz["min_age"]:
            r.err("PRIZE_AGE", f"prize {pid}", f"not for a home with a child under {pz['min_age']} (youngest: {youngest})",
                  "בוחרים ספר גדול או בובה רכה גדולה בלי חלקים קטנים")
            continue
        if pz.get("mouth") and youngest < 5 and mouths:
            r.err("PRIZE_AGE", f"prize {pid}", f"a child of {youngest} who may still put things in the mouth is present",
                  "שואלים אם הילד עדיין מכניס דברים לפה, או בוחרים ספר גדול או בובה רכה גדולה בלי חלקים קטנים")
        if pz.get("writing") and on_shabbat:
            r.err("SHABBAT_ACTION", f"prize {pid}", "coloring or stickers mean writing or sticking on Shabbat or a festival", "בוחרים פרס אחר")
    if foods and any(p.get("guest") for p in h["participants"]) and h.get("allergies_asked") is not True:
        r.err("ALLERGIES", "treasure", "with guest children, ask each parent about allergies before choosing food prizes",
              "שואלים את ההורים של האורחים, או בוחרים אוצר בלי אוכל")
    if h["treasure"].get("eaten_during_hunt") or h.get("edible_clues"):
        r.err("EATING_MOVING", "treasure", "prizes are eaten sitting down after the hunt, never while moving",
              "מחלקים את האוכל רק בסוף, ליד השולחן")
    if on_shabbat and h["treasure"].get("competitive") and foods:
        r.err("SHABBAT_PRIZE", "treasure", "a real food prize won by competing is a problem in the cited source",
              "כולם מקבלים אותו אוצר בסוף, בלי מנצח, ושואלים את הרב של המשפחה במקרה של ספק")


def check_escape(h, r):
    r.checks.append("no real locks, no closed-in rooms, a free way out at all times")
    if h.get("doors_locked") or h.get("players_shut_in"):
        r.err("REAL_LOCK", "format", "no door is locked and no player is shut in a room",
              "הדלתות נשארות פתוחות. ה\"מנעולים\" הם קופסאות או מעטפות עם קוד מדומה")
    if h["format"] == "escape_room" and h.get("free_exit") is not True:
        r.err("REAL_LOCK", "format", "an escape room must state that players can leave at any moment (free_exit)",
              "אומרים לילדים שאפשר לצאת תמיד, ומסמנים free_exit")


def check_candles(h, r):
    r.checks.append("candles: on any date, no station in a room with lit candles or a space open to it")
    c = h["candles"]
    d = dt.date.fromisoformat(h["schedule"]["date"])
    nights = hanukkah_containing(d)
    if h["occasion"] == "hanukkah" and nights is None:
        first = hanukkah_nights(d.year)[0]
        r.err("HANUKKAH_DATE", "schedule.date", f"{d} is not during Hanukkah; in {d.year} the first candle is {first}")
    if nights is not None:
        if not isinstance(h.get("frying_during"), bool):
            r.err("SCHEMA", "frying_during", "the date is during Hanukkah: ask about frying, whatever the occasion", "שואלים: יהיה טיגון בזמן המשחק?")
        elif h["frying_during"]:
            r.err("FRYING", "frying_during", "no hunt while someone is frying", "מסיימים לטגן לפני שמתחילים, ומחכים שהאוכל יתקרר")
    sch = h["schedule"]
    light, end = to_min(sch.get("candle_lighting")), to_min(sch.get("end"))
    eve = h["keeps_shabbat"] and is_sacred(d + dt.timedelta(days=1))
    if eve and end is None:
        r.err("SHABBAT_TIME", "schedule.end", "on the eve of Shabbat or a festival, the hunt needs an end time",
              "שואלים מתי המשחק מסתיים, ומוסיפים end")
    if not c["lit_during_hunt"]:
        before_lighting = light is not None and end is not None and end <= light
        if eve and end is not None and not before_lighting:
            r.err("CANDLES_IMPLIED", "candles", "on the eve of Shabbat or a festival, candles count as lit for this family unless the hunt ends before candle lighting",
                  "מסמנים נרות דולקים ובאיזה חדר, או מסיימים את המשחק לפני ההדלקה")
        return
    if c.get("adult_stays") is not True:
        r.err("CANDLES_UNATTENDED", "candles", "while candles burn, an adult stays in that room",
              "משחקים לפני ההדלקה או אחרי שהנרות כבו, או שמבוגר נשאר ליד הנרות")
    rooms = c.get("room_ids")
    if not isinstance(rooms, list) or not rooms or any(x not in ROOMS for x in rooms):
        r.err("NEAR_CANDLES", "candles.room_ids", f"say which menu room holds the candles: {menu_text(ROOMS)}",
              "אם הנרות במטבח או בחדר שלא בתפריט, בוחרים את החדר הפתוח אליו")
        return
    zone = set(rooms)
    if zone & OPEN_PLAN and c.get("separated_by_wall") is not True:
        zone |= OPEN_PLAN
    for s in h["stations"]:
        if s["room_id"] in zone:
            r.err("NEAR_CANDLES", f"station {s['id']}", "this station is in the room with lit candles, or in a space open to it",
                  "מעבירים את התחנה לחדר אחר, או משחקים כשהנרות לא דולקים. סלון ופינת אוכל נחשבים חלל אחד אם אין קיר ביניהם")


def check_shabbat(h, r):
    """Returns True when the hunt is on Shabbat or Yom Tov for a family that keeps it."""
    if h["keeps_shabbat"] is not True:
        return False  # never impose these limits on a family that did not ask for them
    r.checks.append("Shabbat and Yom Tov planning limits, for a family that keeps them")
    sch = h["schedule"]
    status = shabbat_status(sch)
    d = dt.date.fromisoformat(sch["date"])
    if status is None:
        r.err("SHABBAT_TIME", "schedule", f"{d} is the eve of Shabbat or a festival: need end time and candle-lighting time to tell",
              "מוסיפים end ו-candle_lighting מ-Hebcal לעיר שלכם, ומסיימים לפני הכניסה")
        return False
    if d.weekday() == 5 and status is False:
        r.warn("SHABBAT_NIGHT", "schedule", "Saturday night: after nightfall. Families differ on Havdalah or candles first")
    if not status:
        return False
    if h.get("shabbat_mode") is not True:
        r.err("SHABBAT_MODE", "schedule", "the hunt falls on Shabbat or a festival: switch on shabbat_mode",
              "מדפיסים ומניחים הכול לפני הכניסה, ומסירים כתיבה, גזירה, הדבקה וחשמל מהמשחק")
    if h.get("prepared_before_shabbat") is not True:
        r.err("SHABBAT_PREP", "schedule", "everything is printed, cut and placed before Shabbat or the festival",
              "מסמנים prepared_before_shabbat אחרי שמכינים מראש")
    if any(p["role"] == "player" and p["age"] >= 12 for p in h["participants"]) and h.get("older_players_asked_rabbi") is not True:
        r.err("SHABBAT_OLDER", "participants", "the cited source's leniencies are for children below mitzvah age and it is stricter for older players",
              "לשחקנים מגיל 12 שואלים את הרב של המשפחה לפני שמשחקים, ומסמנים older_players_asked_rabbi")
    cards = [("start", c) for c in (h["start"].get("clues") or {}).values()]
    for s in h["stations"]:
        cards += [(f"station {s['id']}", c) for c in (s.get("clues") or {}).values()]
    for where, c in cards:
        if not isinstance(c, dict):
            continue
        found = find_terms(SHABBAT_ACTIONS, " ".join([c.get("text", "")] + list(c.get("hints") or [])))
        if found:
            r.err("SHABBAT_ACTION", where, f"on Shabbat the game avoids: {', '.join(found)}", "מחליפים בפעולה בלי כתיבה וחשמל, למשל פתרון בעל פה")
    return True


def validate(h):
    r = Report()
    if not check_schema(h, r):
        return r
    resolved = resolve(h, r)
    r.hunt = resolved
    youngest, players = check_people(resolved, r)
    r.youngest = youngest
    r.checks.insert(0, "rooms and hiding spots come from closed menus at floor or child height")
    check_mamad(resolved, r)
    by_id = check_route(resolved, r)
    check_clues(resolved, by_id, players, r)
    on_shabbat = check_shabbat(resolved, r)
    check_prizes(resolved, youngest, on_shabbat, r)
    check_escape(resolved, r)
    check_candles(resolved, r)
    return r


def load(path):
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except (OSError, ValueError) as e:
        print(f"ERROR: could not read {path}: {e}", file=sys.stderr)
        sys.exit(2)
    if not isinstance(data, dict):
        print("ERROR: hunt file must be a JSON object", file=sys.stderr)
        sys.exit(2)
    return data


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("hunt", nargs="?")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--dates", type=int, help="print the Hanukkah nights of this civil year")
    ap.add_argument("--menus", action="store_true", help="print the room, spot and prize menus")
    a = ap.parse_args()
    if a.dates:
        print("\n".join(hanukkah_lines(a.dates)))
        return 0
    if a.menus:
        for title, menu in (("ROOMS", ROOMS), ("SPOTS", SPOTS), ("PRIZES", PRIZES)):
            print(title)
            for k, v in menu.items():
                print(f"  {k}: {v['label']}")
        return 0
    if not a.hunt:
        ap.error("give a hunt.json file")
    h = load(a.hunt)
    try:
        r = validate(h)
    except (KeyError, TypeError, AttributeError, ValueError) as e:
        print(f"ERROR: the hunt file has the wrong shape ({type(e).__name__}: {e})", file=sys.stderr)
        return 2
    if a.json:
        print(json.dumps({"ok": not r.errors, "errors": r.errors, "warnings": r.warnings, "checks": r.checks},
                         ensure_ascii=False, indent=1))
    else:
        for title, rows in (("ERRORS", r.errors), ("WARNINGS", r.warnings)):
            print(f"{title}: {len(rows)}")
            for x in rows:
                print(f"- [{x['code']}] {x['where']}: {x['message']}")
                if x["fix"]:
                    print(f"    suggested alternative: {x['fix']}")
        print("CHECKED:")
        for c in r.checks:
            print(f"- {c}")
        print("NOT CHECKED: the real home, and any unsafe wording the card scan does not know. An adult reads every card, walks the route first and stays present.")
    return 1 if r.errors else 0


if __name__ == "__main__":
    sys.exit(main())
