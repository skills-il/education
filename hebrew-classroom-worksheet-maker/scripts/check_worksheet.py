#!/usr/bin/env python3
"""Check a worksheet JSON, and optionally its built HTML, before it is printed.

Exit codes: 0 no errors, 1 errors were found, 2 the check itself could not run.
A clean result means these rules passed. It does not mean the niqqud or the pedagogy are right,
it cannot recognize a person's name, and it does not clear a text's copyright.

Usage:
  python3 check_worksheet.py worksheet.json
  python3 check_worksheet.py worksheet.json --html worksheet.html
"""

import argparse
import datetime
import os
import re
import sys

from build_worksheet import build
from pictures import PICTURES
from worksheet_lib import (DAGESH, FINAL_TO_BASE, GRADES, HOLAM, MATH_GRADES, QUBUTS, SIN_DOT, VOWEL_NAMES,
                           MathError, clusters, counters_operands, gdt_forms, given_numbers, grade1_form,
                           has_digit_or_operator, has_math, has_medial_bare_alef, hebrew_words, is_pointed,
                           is_vowel_letter, iter_items, letters_only, load_worksheet, nfc, parse_expr,
                           plain_qamats_qatan, printed_strings, safe_path, skeleton, solve, unpointed_letters, word_vowels)

GRADE_MAX = {"1": 100, "2": 1000, "3": 10000}
G2_TABLES = {2, 4, 5, 10}
MAX_COUNTERS = 10
SINGULAR_IMPERATIVES = {
    "הקף", "הקיפי", "כתוב", "כתבי", "קרא", "קראי", "מצא", "מצאי", "חבר", "חברי", "מתח", "מתחי",
    "פתור", "פתרי", "סמן", "סמני", "ענה", "עני", "צבע", "צבעי", "השלם", "השלימי", "גזור", "גזרי",
}
AMBIGUOUS_PLURAL = {"מצאו", "כתבו", "קראו", "פתרו", "סמנו", "מתחו", "גזרו", "צבעו"}
NEED_TERMS = (
    "דיסלקציה", "דיסלקטי", "דיסלקטית", "דיסלקטים", "דיסקלקוליה", "הפרעת קשב", "הפרעות קשב", "לקות", "לקויות",
    "לקוי", "לקויה", "לקויים", "לקויי", "ליקויי", "קשיי למידה", "קשיים בלמידה", "מתקשה", "מתקשים", "מתקשות",
    "מצטיין", "מצטיינת", "מצטיינים", "מצטיינות", "חינוך מיוחד", "תלמידי שילוב", "ילדי שילוב", "כיתת שילוב",
    "ADHD", "dyslexia",
)
LEVEL_ADJECTIVES = "חלש|חלשה|חלשים|חלשות|חזק|חזקה|חזקים|חזקות|מתקדם|מתקדמת|מתקדמים|מתקדמות|מוגבר|מוגברת"
NOT_HEBREW_BEFORE = r"(?<![א-ת])"
NOT_HEBREW_AFTER = r"(?![א-ת])"
PREFIXES = "[ובכלמשה]{0,3}"
NEED_RX = re.compile(
    NOT_HEBREW_BEFORE + PREFIXES + "(?:" + "|".join(re.escape(t) for t in NEED_TERMS)
    + r"|ליקוי(?!\s+(?:חמה|לבנה)))" + NOT_HEBREW_AFTER, re.I)
LEVEL_RX = re.compile(
    NOT_HEBREW_BEFORE + "ל(?:חלשים|חלשות|חזקים|חזקות|מתקדמים|מתקדמות)" + NOT_HEBREW_AFTER + "|"
    + NOT_HEBREW_BEFORE + PREFIXES + r"(?:תלמיד\w*|ילד\w*|קבוצ\w*|גרס\w*|רמ[הת])\s+ה?(?:" + LEVEL_ADJECTIVES + ")"
    + NOT_HEBREW_AFTER + r"|\b(?:weak|strong)\s+(?:students?|pupils?|kids?|group|level)\b", re.I)
ROSTER_KEYS = {"students", "student", "student_name", "student_names", "roster", "class_list",
               "names", "pupil", "pupils", "diagnosis", "needs"}
KNOWN_PROTECTED = {"סביבון סוב סוב סוב": "Levin Kipnis, protected through 31.12.2060",
                   "חנוכה הוא חג טוב": "Levin Kipnis, protected through 31.12.2060"}
NEUTRAL_CODES = {"", "●", "■", "▲", "◆"}
EMOJI_RX = re.compile("[\U0001F000-\U0001FAFF☀-➿️]")
ID_RX = re.compile(r"(?<!\d)\d{9}(?!\d)")
PHONE_RX = re.compile(r"(?<!\d)0(?:5\d|[23489]|7\d)-?\d{3}-?\d{4}(?!\d)")
EMAIL_RX = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
OLD_REMAINDER_RX = re.compile(r"\d\s*\(\s*\d+\s*\)")
SLASH_GENDER_RX = re.compile(r"[א-ת֑-ׇ]/[תהי](?![א-ת])")
NO_MATRES = str.maketrans("", "", "וי")


class Report:
    def __init__(self, overrides=()):
        self.rows = []
        self.overrides = set(overrides or ())

    def error(self, code, where, message):
        if code == "SCOPE" and where in self.overrides:
            self.rows.append(("WARN", code, where, f"teacher chose to keep this: {message}"))
        else:
            self.rows.append(("ERROR", code, where, message))

    def warn(self, code, where, message):
        self.rows.append(("WARN", code, where, message))


def student_strings(section):
    """(where, text, kind) for each string a student sees."""
    if section.get("type") == "read_aloud":
        return
    sid = section.get("id", "?")
    if section.get("title"):
        yield f"{sid}.title", section["title"], "title"
    if section.get("instruction"):
        yield f"{sid}.instruction", section["instruction"], "instruction"
    for idx, line in enumerate(section.get("text", []) or []):
        yield f"{sid}.text[{idx}]", line, "read"
    for item in section.get("items", []) or []:
        iid = item.get("id", "?")
        for field in ("stem", "word", "prompt"):
            if item.get(field):
                yield f"{iid}.{field}", item[field], "read"
        for option in item.get("options", []) or []:
            if isinstance(option, str):
                yield f"{iid}.option", option, "read"


def check_intake(meta, report):
    grade = str(meta.get("grade", ""))
    if grade not in GRADES:
        report.error("INTAKE", "meta.grade", f"grade must be one of {', '.join(GRADES)}")
    if grade == "1" and not meta.get("allowed_letters"):
        report.error("INTAKE", "meta.allowed_letters",
                     "grade 1 needs the letters this class has learned. There is no national order.")
    if grade == "1" and not meta.get("allowed_vowels"):
        report.error("INTAKE", "meta.allowed_vowels",
                     "grade 1 needs the vowels this class has learned. There is no national order.")
    for name in meta.get("allowed_vowels") or []:
        if name not in VOWEL_NAMES and name != "shuruk":
            report.error("INTAKE", "meta.allowed_vowels", f"unknown vowel name {name!r}")
    if meta.get("gdt_dagesh") not in (None, "drop", "keep"):
        report.error("INTAKE", "meta.gdt_dagesh", "gdt_dagesh must be drop or keep")
    if not meta.get("school_year"):
        report.warn("INTAKE", "meta.school_year", "state the school year the content was checked for")


def letter_problem(cl, idx, meta):
    """Why this letter is outside the class's taught units, or None."""
    letter, marks = cl[idx]
    if is_vowel_letter(cl, idx):
        return None
    taught = set(nfc(meta.get("allowed_letters", "")))
    soft = set(meta.get("soft_letters") or [])
    base = FINAL_TO_BASE.get(letter, letter)
    if letter in FINAL_TO_BASE:
        if letter in taught:
            return None
        if not meta.get("finals_taught"):
            return f"final {letter} was not taught"
        if letter in "ךף" and base not in soft:
            return f"the soft sound of {base} was not taught"
        return None if base in taught or base in soft else f"letter {base} was not taught"
    if letter in "בכפ":
        if DAGESH in marks:
            return None if letter in taught else f"the hard sound of {letter} was not taught"
        return None if letter in soft else f"the soft sound of {letter} was not taught"
    if letter == "ש" and SIN_DOT in marks:
        return None if meta.get("sin_taught") else "sin was not taught"
    return None if letter in taught else f"letter {letter} was not taught"


def check_decodable(data, report):
    meta = data["meta"]
    if not meta.get("allowed_letters"):
        return
    vowels = set(meta.get("allowed_vowels") or [])
    sight = {letters_only(w) for w in meta.get("sight_words", [])}
    taught = set(nfc(meta["allowed_letters"])) | set(meta.get("soft_letters") or [])
    for section in data["sections"]:
        if section.get("type") == "first_letter":
            for item in section.get("items", []):
                target = letters_only(item.get("letter", ""))
                base = FINAL_TO_BASE.get(target, target)
                if base and base not in taught:
                    report.error("LETTER", item.get("id", "?"), f"first-letter target {base} was not taught")
                pic = PICTURES.get(item.get("answer"))
                if pic:
                    problem = letter_problem(clusters(pic["names"][0]), 0, meta)
                    if problem:
                        report.error("LETTER", item.get("id", "?"), f"answer picture {pic['names'][0]}: {problem}")
        if section.get("source_text"):
            continue
        for where, text, kind in student_strings(section):
            if kind != "read":
                continue
            for word in hebrew_words(text):
                if letters_only(word) in sight:
                    continue
                cl = clusters(word)
                problems = {letter_problem(cl, i, meta) for i in range(len(cl))} - {None}
                for problem in sorted(problems):
                    report.error("LETTER", where, f"{word}: {problem}")
                if vowels:
                    bad = sorted(word_vowels(word) - vowels)
                    if bad:
                        report.error("VOWEL", where, f"{word}: vowel not taught: {', '.join(bad)}")


def defective_vowel(word):
    """A qubuts, or a holam on a letter other than vav: the sound has no vowel letter."""
    cl = clusters(word)
    for idx, (letter, marks) in enumerate(cl):
        if QUBUTS in marks:
            return True
        next_is_vav = idx + 1 < len(cl) and cl[idx + 1][0] == "ו"
        if HOLAM in marks and letter != "ו" and not next_is_vav:
            return True
    return False


def check_niqqud_profile(data, report):
    grade = str(data["meta"].get("grade", ""))
    if grade not in ("1", "2", "3"):
        return
    mode = data["meta"].get("gdt_dagesh")
    with_dagesh, without_dagesh = [], []
    sight = {letters_only(w) for w in data["meta"].get("sight_words", [])}
    for section in data["sections"]:
        if section.get("source_text"):
            continue
        for where, text, kind in student_strings(section):
            for word in hebrew_words(text):
                long_word = len(letters_only(word)) >= 2
                if grade == "3":
                    if kind == "read" and section.get("type") == "reading" and long_word and not is_pointed(word):
                        report.warn("UNPOINTED", where, f"{word}: grade 3 stories and poems are fully pointed")
                    continue
                if long_word and not is_pointed(word):
                    if grade == "1":
                        report.error("UNPOINTED", where, f"{word}: grade 1 text is pointed")
                    elif kind == "read":
                        report.warn("UNPOINTED", where, f"{word}: grade 2 reading text is usually pointed")
                    continue
                if grade == "2" and kind == "read" and defective_vowel(word):
                    report.warn("G2_MATRES", where, f"{word}: grade 2 prefers a vowel letter with the niqqud")
                if grade == "1":
                    expected = grade1_form(word, keep_gdt=mode != "drop")
                    if expected != nfc(word):
                        report.error("G1_PROFILE", where, f"{word}: grade 1 form is {expected}")
                    if letters_only(word) not in sight:
                        present, absent = gdt_forms(word)
                        if present:
                            with_dagesh.append(word)
                        if absent:
                            without_dagesh.append(word)
                    qatan_word = None if letters_only(word) in sight else plain_qamats_qatan(word)
                    if qatan_word == "כל":
                        report.error("QATAN", where, f"{word}: with a plain qamats a child reads kal. Use ׇ or another word")
                    elif qatan_word:
                        report.warn("QATAN", where, f"{word}: if this qamats is read as o, use ׇ or another word")
                    if kind == "read" and has_medial_bare_alef(word):
                        report.warn("ALEF", where, f"{word}: confirm this alef is silent and hides no untaught vowel")
                    missing = unpointed_letters(word)
                    if missing:
                        report.error("UNPOINTED", where,
                                     f"{word}: no vowel on {' '.join(missing)}, so it can hide an untaught vowel")


    if with_dagesh and without_dagesh:
        report.error("G1_GDT", "sheet", f"mixed dagesh in ג ד ת: {with_dagesh[0]} and {without_dagesh[0]}. Use one form.")
    elif mode == "keep" and without_dagesh:
        report.error("G1_GDT", "sheet", f"gdt_dagesh is keep, but {without_dagesh[0]} has no dagesh")
    elif mode is None and with_dagesh:
        report.warn("G1_GDT", "sheet", f"{with_dagesh[0]}: this skill drops the dagesh in ג ד ת by default. "
                    "If the class primer prints it, set gdt_dagesh to keep. Otherwise remove it.")


def scope_values(iid, expr, values, operators, meta, report):
    grade = str(meta.get("grade", ""))
    top = max(values or [0])
    ceiling = int(meta.get("math_max") or 0)
    if ceiling and top > ceiling:
        report.error("SCOPE", iid, f"{expr}: above this class's range of {ceiling}")
    if grade in GRADE_MAX and top > GRADE_MAX[grade]:
        report.error("SCOPE", iid, f"{expr}: above the grade {grade} number range")
    if grade == "1":
        if operators & {"×", ":"}:
            report.error("SCOPE", iid, f"{expr}: no multiplication or division in the new grade 1 program")
        if any(v > 20 and v % 10 for v in values):
            report.error("SCOPE", iid, f"{expr}: grade 1 works to 20, and in whole tens to 100")
    if grade == "gan" and operators & {"×", ":"}:
        report.error("SCOPE", iid, f"{expr}: multiplication and division are not used in this route for gan")


def check_counters(item, report):
    if not item.get("counters"):
        return
    iid, expr = item["id"], item["expr"]
    operands = counters_operands(expr)
    if not operands:
        report.error("COUNTERS", iid, f"{expr}: counters are only for a + b = ___")
        return
    if list(operands) != list(item["counters"]):
        report.error("COUNTERS", iid, f"{expr}: counters {item['counters']} do not match the exercise")
    if sum(operands) > MAX_COUNTERS:
        report.error("COUNTERS", iid, f"{expr}: at most {MAX_COUNTERS} counters fit on the line")
    if item.get("picture", "dreidel") not in PICTURES:
        report.error("PICTURE", iid, f"unknown picture {item.get('picture')!r}")


def check_word_problem(item, parsed, report):
    prompt = item.get("prompt")
    if not prompt:
        return
    iid = item.get("id", "?")
    in_prompt = sorted(int(n) for n in re.findall(r"(?<![א-ת\d])\d+", prompt))
    in_expr = sorted(given_numbers(parsed))
    if not in_prompt:
        report.error("WORD_PROBLEM", iid, "write the question's numbers as digits, so they can be compared with the exercise")
    elif in_prompt != in_expr:
        report.error("WORD_PROBLEM", iid, f"the numbers in the question {in_prompt} differ from the exercise {in_expr}")
    if item.get("prompt_read") is True:
        report.warn("WORD_PROBLEM", iid, "the script compares digits only and cannot tell whether the operation fits the story. A person must read it.")
    else:
        report.error("WORD_PROBLEM", iid, "read the question, confirm the exercise fits it, then set prompt_read to true")


def check_math_item(item, meta, report):
    iid, expr = item.get("id", "?"), item.get("expr", "")
    grade = str(meta.get("grade", ""))
    if grade not in MATH_GRADES:
        report.error("MATH_GRADE", iid, "automatic math checks cover gan to grade 3 only")
        return
    if grade == "gan" and not meta.get("math_max"):
        report.error("SCOPE", iid, "state the range this gan works with in math_max")
    if "answers" in item or "rule" in item:
        report.error("MATH_PARSE", iid, "an item has exactly one blank and one answer. answers and rule are not supported")
        return
    if isinstance(expr, str) and ("÷" in expr or "/" in expr or "*" in expr):
        report.error("NOTATION", iid, f"{expr}: use × and a colon, never ÷, / or *")
        return
    if isinstance(expr, str) and OLD_REMAINDER_RX.search(expr):
        report.error("NOTATION", iid, f"{expr}: old remainder form. Write 13 : 4 = ___ + (1 : 4)")
        return
    try:
        parsed = parse_expr(expr)
    except MathError as err:
        report.error("MATH_PARSE", iid, f"{expr}: {err}")
        return
    check_counters(item, report)
    check_word_problem(item, parsed, report)
    try:
        right = solve(parsed)
    except MathError as err:
        report.error("MATH_WRONG", iid, f"{expr}: {err}")
        return
    if "answer" not in item:
        report.error("MATH_WRONG", iid, f"{expr}: no answer given")
        return
    answer = item["answer"]
    if parsed["kind"] == "compare":
        if answer != right:
            report.error("MATH_WRONG", iid, f"{expr}: the answer is {right}")
        if grade in ("gan", "1"):
            report.error("SCOPE", iid, f"{expr}: the grade 1 program compares numbers without math signs, so this form is not used in gan or grade 1")
        scope_values(iid, expr, given_numbers(parsed), set(), meta, report)
        return
    if isinstance(answer, bool) or not isinstance(answer, int):
        report.error("MATH_WRONG", iid, f"{expr}: answers must be whole numbers")
        return
    if answer != right:
        report.error("MATH_WRONG", iid, f"{expr}: answer {answer} is wrong, it is {right}")
    if right < 0:
        report.error("NEGATIVE", iid, f"{expr}: negative numbers are outside gan to grade 3")
        return
    values = given_numbers(parsed) + [right]
    if parsed["kind"] == "remainder":
        if grade != "3":
            report.error("SCOPE", iid, f"{expr}: division with remainder is taught in grade 3")
        if parsed["b"] > 9:
            report.error("SCOPE", iid, f"{expr}: the grade 3 program uses a one-digit divisor")
        if parsed["a"] // parsed["b"] > 10:
            report.error("SCOPE", iid, f"{expr}: the grade 3 program keeps division with remainder within the 10 by 10 table")
        scope_values(iid, expr, values, {":"}, meta, report)
        return
    operators = {parsed["op"]}
    scope_values(iid, expr, values, operators, meta, report)
    if grade == "2" and "×" in operators and not set(given_numbers(parsed)) & G2_TABLES:
        report.warn("SCOPE", iid, f"{expr}: grade 2 targets multiples of 2, 4, 5 and 10")


def check_math_outside(data, report):
    for where, text, _ in printed_strings(data):
        if has_math(text):
            report.error("MATH_OUTSIDE", where, f"{text}: arithmetic and comparisons belong only in a math section")
    for section in data["sections"]:
        for item in section.get("items", []) or []:
            if section.get("type") != "math" and item.get("expr"):
                report.error("MATH_OUTSIDE", item.get("id", "?"), "expr is allowed only in a math section")


def check_picture_word(item, iid, report):
    pic = PICTURES.get(item.get("picture"))
    word = item.get("word", "")
    if not pic:
        report.error("PICTURE", iid, f"unknown picture {item.get('picture')!r}")
    elif not is_pointed(word):
        report.error("PICTURE", iid, f"{word}: point a word that goes with a picture")
    elif skeleton(word) not in {skeleton(name) for name in pic["names"]}:
        report.error("PICTURE", iid, f"{word}: this picture is {' / '.join(pic['names'])}")


def check_first_letter(item, iid, report):
    target = letters_only(item.get("letter", ""))
    target = FINAL_TO_BASE.get(target, target)
    options = item.get("picture_options") or []
    hits = []
    for option in options:
        pic = PICTURES.get(option)
        if not pic:
            report.error("PICTURE", iid, f"unknown picture {option!r}")
            continue
        if any(letters_only(name)[0] == target for name in pic["names"]):
            hits.append(option)
    if item.get("answer") not in options or hits != [item.get("answer")]:
        report.error("MC_ONE", iid, f"exactly one picture must start with {target}, found {hits}")


def check_items(data, report):
    meta = data["meta"]
    grade = str(meta.get("grade", ""))
    seen = set()
    for section in data["sections"]:
        kind = section.get("type")
        if kind == "gematria" and grade in ("gan", "1", "2"):
            report.error("SCOPE", section.get("id", "?"), "letter values appear in the grade 3 program")
        if kind == "trace":
            report.error("KG_WRITING", section.get("id", "?"),
                         "copying and tracing are not built. Use a sound game or matching.")
    for section, item in iter_items(data):
        iid = item.get("id")
        if not iid:
            report.error("ITEM", section.get("id", "?"), "every item needs an id")
            continue
        if iid in seen:
            report.error("ITEM", iid, "duplicate item id")
        seen.add(iid)
        kind = section.get("type")
        if kind == "math":
            check_math_item(item, meta, report)
        elif kind == "mc":
            options = item.get("options") or []
            correct = [o for o in options if o == item.get("answer")]
            if len(correct) != 1 or len(set(options)) != len(options):
                report.error("MC_ONE", iid, f"needs exactly one correct option, found {len(correct)}"
                             + (" and duplicates" if len(set(options)) != len(options) else ""))
            if len(options) < 2:
                report.error("MC_ONE", iid, "needs at least two options")
            fields = [item.get("stem", ""), item.get("teacher_question", "")] + [str(o) for o in options]
            if any(has_digit_or_operator(field) for field in fields):
                report.error("MC_NUMERIC", iid, "multiple choice cannot hold digits or operators. Arithmetic belongs in a math section")
        elif kind == "match":
            check_picture_word(item, iid, report)
        elif kind == "first_letter":
            check_first_letter(item, iid, report)
    for section in data["sections"]:
        if section.get("type") == "match":
            pics = [i.get("picture") for i in section.get("items", [])]
            if len(set(pics)) != len(pics):
                report.error("PICTURE", section.get("id", "?"), "the same picture appears twice")
    return seen


def check_key(data, seen, report):
    key = data.get("key")
    if key is None:
        return
    by_id = {item.get("id"): (section, item) for section, item in iter_items(data)}
    refs = set()
    for entry in key:
        ref = entry.get("ref")
        refs.add(ref)
        if ref not in seen:
            report.error("KEY_ORPHAN", str(ref), "key entry points to an item not printed on the student page")
            continue
        _, item = by_id[ref]
        expected = item.get("answers", item.get("answer", item.get("picture")))
        if "answer" in entry and entry["answer"] != expected:
            report.error("KEY_WRONG", ref, f"key says {entry['answer']}, item says {expected}")
    for iid in seen - refs:
        report.error("KEY_MISSING", iid, "printed item has no key entry")


def walk(node, path=""):
    if isinstance(node, dict):
        for key, value in node.items():
            child = f"{path}.{key}" if path else key
            if key.lower() in ROSTER_KEYS:
                yield child, None
            yield from walk(value, child)
    elif isinstance(node, list):
        for idx, value in enumerate(node):
            yield from walk(value, f"{path}[{idx}]")
    elif isinstance(node, str):
        yield path, node


def plain_text(value):
    without_marks = "".join(ch for ch in nfc(value) if not "֑" <= ch <= "ׇ")
    return re.sub(r"\s+", " ", re.sub(r"[^\w\s]", " ", without_marks)).strip()


def check_quoted_works(data, report):
    current = datetime.date.today().year
    for section in data["sections"]:
        sid = section.get("id", "?")
        if section.get("source_text"):
            if not str(section.get("source", "")).strip():
                report.error("SOURCE", sid, "source_text needs a source, such as the book and chapter or the prayer")
            else:
                report.warn("SOURCE", sid, f"{section['source']}: not checked for decodability or grade marks. "
                            "Confirm this is a verse or prayer and not a protected poem, and compare it with a trusted edition.")
        work = section.get("quoted_work")
        if work is None:
            continue
        creators = work.get("creators") if isinstance(work, dict) else None
        if not creators or any(not isinstance(c, dict) or isinstance(c.get("death_year"), bool)
                                or not isinstance(c.get("death_year"), int) for c in creators):
            report.error("COPYRIGHT", sid, "cannot confirm: list every creator, including translators "
                         "and co-authors, with a death year. Otherwise do not print it.")
            continue
        last = max(c["death_year"] for c in creators)
        if last + 70 >= current:
            report.error("COPYRIGHT", sid, f"{work.get('title', 'work')}: protected through 31.12.{last + 70}. "
                         "Name it, do not print it.")
        else:
            report.warn("COPYRIGHT", sid, "the listed dates have expired. This does not clear the text, "
                        "so confirm the creators and the edition.")


def check_privacy_and_text(data, report):
    code = str(data["meta"].get("version_code", ""))
    if code not in NEUTRAL_CODES:
        report.error("PII", "meta.version_code", f"{code}: use a neutral shape: ● ■ ▲ ◆")
    for path, value in walk(data):
        if value is None:
            report.error("PII", path, "no student names, lists or needs in the worksheet file")
            continue
        if path.endswith(".expr") or path.endswith(".allowed_letters") or path.endswith(".school_year"):
            continue
        if ID_RX.search(value) or PHONE_RX.search(value) or EMAIL_RX.search(value):
            report.error("PII", path, "looks like an ID number, phone or email")
        if EMOJI_RX.search(value):
            report.error("EMOJI", path, "emoji depend on the device and photocopy badly")
        squeezed = plain_text(value).translate(NO_MATRES)
        for opening, owner in KNOWN_PROTECTED.items():
            if opening.translate(NO_MATRES) in squeezed:
                report.error("COPYRIGHT", path, f"known protected song text ({owner}). Name it, do not print it.")
    for where, text, is_story in printed_strings(data):
        if is_story:
            continue
        plain = "".join(ch for ch in nfc(text) if not "\u0591" <= ch <= "\u05C7")
        found = NEED_RX.search(plain) or LEVEL_RX.search(plain)
        if found:
            report.error("PII", where, f"a label about a student's level or needs: {found.group(0)}")
    check_quoted_works(data, report)


def check_gender(data, report):
    for section in data["sections"]:
        for where, text, kind in student_strings(section):
            if kind != "instruction":
                continue
            if SLASH_GENDER_RX.search(nfc(text)):
                report.error("GENDER", where, f"{text}: no slash forms, use the plural")
            for word in hebrew_words(text):
                plain = letters_only(word)
                if plain in SINGULAR_IMPERATIVES:
                    report.error("GENDER", where, f"{word}: use the plural imperative")
                if plain in AMBIGUOUS_PLURAL and not is_pointed(word):
                    report.warn("GENDER", where, f"{word}: reads as past tense too, add helper niqqud")


def check_html(path, data, report):
    try:
        with open(path, encoding="utf-8") as handle:
            html_text = handle.read()
    except OSError as err:
        print(f"ERROR: cannot read {path}: {err}", file=sys.stderr)
        sys.exit(2)
    try:
        if build(data) != html_text:
            report.error("STALE", "html", "the page does not match the JSON. Rebuild it, and do not edit it by hand.")
    except SystemExit as err:
        report.error("STALE", "html", f"the page cannot be rebuilt from the JSON: {err}")
    if "size: A4" not in html_text:
        report.error("PRINT", "html", "no A4 page rule")
    if 'dir="rtl"' not in html_text:
        report.error("PRINT", "html", "the page is not right to left")
    if EMOJI_RX.search(html_text):
        report.error("EMOJI", "html", "emoji in the page")
    for color in re.findall(r"#[0-9a-fA-F]{3,8}\b", html_text):
        if color.lower() not in ("#000", "#000000", "#fff", "#ffffff"):
            report.error("PRINT", "html", f"color {color}: black and white only")
    student, _, teacher = html_text.partition('data-part="teacher"')
    if not teacher:
        report.error("KEY_ORPHAN", "html", "no separate teacher key")
    printed = set(re.findall(r'data-item="([^"]+)"', student))
    for ref in re.findall(r'data-ref="([^"]+)"', teacher):
        if ref not in printed:
            report.error("KEY_ORPHAN", ref, "the key refers to an item not printed on the student page")
    student_pics = set(re.findall(r'data-pic="([^"]+)"', student))
    for ref in re.findall(r'data-picref="([^"]+)"', teacher):
        if ref not in student_pics:
            report.error("KEY_ORPHAN", ref, "the key names a picture number not printed on the student page")
    body = html_text.split("</style>")[-1]
    outside = re.sub(r'<bdi dir="ltr" class="math">.*?</bdi>', " ", body, flags=re.S)
    outside = re.sub(r"<svg.*?</svg>", " ", outside, flags=re.S)
    if any(has_math(node) for node in re.split(r"<[^>]+>", outside)):
        report.error("BIDI", "html", "math on the page is outside a left-to-right run")
    for section, item in iter_items(data):
        if section.get("type") == "math":
            block = re.search(rf'data-item="{re.escape(item.get("id", ""))}".*?</bdi>', student, re.S)
            if not block or 'dir="ltr"' not in block.group(0):
                report.error("BIDI", item.get("id", "?"), "math is not isolated as a left-to-right run")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("worksheet")
    parser.add_argument("--html", help="the built page, in the same folder as the worksheet")
    args = parser.parse_args()
    data = load_worksheet(args.worksheet)
    report = Report(data["meta"].get("teacher_override"))
    check_intake(data["meta"], report)
    check_decodable(data, report)
    check_niqqud_profile(data, report)
    check_math_outside(data, report)
    seen = check_items(data, report)
    check_key(data, seen, report)
    check_privacy_and_text(data, report)
    check_gender(data, report)
    if args.html:
        base = os.path.dirname(os.path.abspath(args.worksheet))
        check_html(safe_path(base, args.html), data, report)
    for level, code, where, message in report.rows:
        print(f"{level} {code} [{where}] {message}")
    errors = sum(1 for row in report.rows if row[0] == "ERROR")
    warnings = len(report.rows) - errors
    print(f"SUMMARY: {errors} error(s), {warnings} warning(s). "
          + ("Fix the errors before printing." if errors else
             "Rules passed. A person still reads the niqqud, the pictures, the rendered math, "
             "and confirms that no student name appears."))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
