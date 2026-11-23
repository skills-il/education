#!/usr/bin/env python3
"""Build a print-ready right-to-left A4 hunt kit (HTML) from a checked hunt.json.

No network access and no external packages. Refuses to build when check_hunt.py finds an error.
Open the HTML in Chrome or Edge, Print, Save as PDF. Print at 100 percent, in grayscale if you like.

  python3 build_kit.py hunt.json --out kit.html
  python3 build_kit.py hunt.json --out kit.html --font-file NotoSansHebrew.ttf

The output and any font file must sit in the same folder as hunt.json.
"""

import argparse
import base64
import datetime as dt
import html
import os
import sys

sys.dont_write_bytecode = True  # keep the skill folder free of build artifacts
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_hunt import PRIZES, ROOMS, hanukkah_containing, load, shabbat_status, validate  # noqa: E402

WEEKDAYS = ["שני", "שלישי", "רביעי", "חמישי", "שישי", "שבת", "ראשון"]
OCCASIONS = {"hanukkah": "חנוכה", "birthday": "יום הולדת", "purim": "פורים", "passover": "פסח", "tu_bishvat": "טו בשבט",
             "sukkot": "סוכות", "summer": "חופש גדול", "rainy_day": "יום בבית", "other": ""}
SIZES = {"gan": "24pt", "grade1": "23pt", "grade2": "20pt", "grade3": "17pt", "grade4-6": "15pt"}

# Plain line icons: black on white, so they survive grayscale printing. No emoji, no color.
S = 'fill="none" stroke="#111" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"'
ICONS = {
    "sofa": '<path d="M16 50V36a8 8 0 0 1 8-8h52a8 8 0 0 1 8 8v14"/><rect x="8" y="48" width="84" height="22" rx="7"/><path d="M20 70v9M80 70v9M50 30v18"/>',
    "bed": '<path d="M10 28v52M10 62h80v18"/><path d="M90 62V50a10 10 0 0 0-10-10H36v22"/><rect x="15" y="44" width="17" height="14" rx="4"/>',
    "table": '<path d="M8 34h84M18 34v46M82 34v46M18 52h64"/>',
    "chair": '<path d="M32 12v66M32 48h38v30M32 48V12h34v36"/>',
    "book": '<path d="M50 24c-9-7-24-8-38-5v58c14-3 29-2 38 5 9-7 24-8 38-5V19c-14-3-29-2-38 5zM50 24v58"/>',
    "teddy": '<circle cx="50" cy="34" r="18"/><circle cx="33" cy="18" r="7"/><circle cx="67" cy="18" r="7"/><ellipse cx="50" cy="70" rx="22" ry="20"/><circle cx="43" cy="31" r="2"/><circle cx="57" cy="31" r="2"/><path d="M46 40q4 4 8 0"/>',
    "basket": '<path d="M10 42h80l-8 40H18zM26 42c0-30 48-30 48 0M34 54v16M50 54v16M66 54v16"/>',
    "rug": '<rect x="16" y="26" width="68" height="48" rx="2"/><rect x="26" y="36" width="48" height="28"/><path d="M8 30h8M8 42h8M8 58h8M8 70h8M84 30h8M84 42h8M84 58h8M84 70h8"/>',
    "treasure": '<path d="M12 44c0-22 76-22 76 0v38H12zM12 44h76M44 40h12v14H44z"/>',
}


def e(s):
    return html.escape(str(s or ""), quote=True)


def icon(name, size=120):
    return f'<svg viewBox="0 0 100 100" width="{size}" height="{size}" {S} aria-hidden="true">{ICONS.get(name, "")}</svg>'


def safe_path(base_dir, rel):
    base = os.path.realpath(base_dir)
    full = os.path.realpath(os.path.join(base, rel))
    if os.path.commonpath([base, full]) != base:
        sys.exit(f"ERROR: {rel} is outside the hunt folder. Keep every file next to hunt.json.")
    return full


def nice_date(iso):
    d = dt.date.fromisoformat(iso)
    return f"יום {WEEKDAYS[d.weekday()]}, {d.day}.{d.month}.{d.year}"


def route(h):
    by_id = {s["id"]: s for s in h["stations"]}
    out, cur = [], h["start"]["next"]
    while cur:
        out.append(by_id[cur])
        cur = by_id[cur].get("next")
    return out


CSS = """
@page { size: A4; margin: 11mm; }
* { box-sizing: border-box; }
html, body { margin: 0; background: #fff; color: #111; }
body { font-family: FONTSTACK; font-size: 10.2pt; line-height: 1.32; direction: rtl; }
h1 { font-size: 21pt; margin: 0 0 1mm; line-height: 1.2; }
h2 { font-size: 12.5pt; margin: 2mm 0 .8mm; border-bottom: 1.6pt solid #111; padding-bottom: 1mm; }
p { margin: 0 0 2mm; }
ul { margin: 0 0 2mm; padding-inline-start: 5mm; }
li { margin-bottom: .7mm; }
section { break-after: page; }
section:last-of-type { break-after: auto; }
.lead { color: #333; font-size: 12pt; }
.box { border: 1.4pt solid #111; padding: 1.4mm 3.2mm; margin: 1.4mm 0; break-inside: avoid; }
.box h3 { margin: 0 0 .5mm; font-size: 11.5pt; }
.check li { list-style: none; position: relative; padding-inline-start: 6mm; }
.check { padding-inline-start: 0; }
.check li::before { content: ""; position: absolute; inset-inline-start: 0; top: 1mm; width: 3.4mm; height: 3.4mm; border: 1pt solid #111; }
table { width: 188mm; border-collapse: collapse; font-size: 10.5pt; }
th, td { border: 1pt solid #111; padding: 1.4mm 2mm; vertical-align: top; text-align: start; }
th { background: #e6e6e6; }
tr { break-inside: avoid; }
.phones { font-size: 12pt; font-weight: 700; }
.ltr { direction: ltr; unicode-bidi: isolate; display: inline-block; }
.cards { display: grid; grid-template-columns: 1fr 1fr; gap: 0; border-top: 1pt dashed #555; border-inline-start: 1pt dashed #555; }
.card { height: 84mm; padding: 5mm 6mm 4mm; border-bottom: 1pt dashed #555; border-inline-end: 1pt dashed #555;
        display: flex; flex-direction: column; break-inside: avoid; }
.card .top { display: flex; justify-content: space-between; align-items: baseline; font-size: 11pt; border-bottom: 1pt solid #111; padding-bottom: 1mm; }
.card .who { font-weight: 700; font-size: 14pt; }
.card .body { flex: 1; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; white-space: pre-line; line-height: 1.75; text-wrap: balance; }
.card .note { font-size: 9.5pt; color: #333; text-align: center; }
.cipher { font-size: 1.25em; letter-spacing: .18em; font-weight: 700; border: 1pt solid #111; padding: 1mm 3mm; margin-top: 2mm; }
.cuthint { font-size: 9.5pt; color: #333; margin-bottom: 1.5mm; }
.cert { height: 262mm; border: 3pt double #111; padding: 16mm 14mm; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center; break-after: page; }
.cert:last-child { break-after: auto; }
.cert .kicker { font-size: 18pt; }
.cert .name { font-size: 52pt; font-weight: 700; line-height: 1.25; margin: 6mm 0; }
.cert .line { font-size: 19pt; }
.cert .sign { margin-top: 26mm; font-size: 13pt; border-top: 1pt solid #111; padding-top: 2mm; min-width: 70mm; }
"""


def host_guide(h, rep, players, stops):
    occ = OCCASIONS.get(h["occasion"], "")
    sch = h["schedule"]
    d = dt.date.fromisoformat(sch["date"])
    on_shabbat = h["keeps_shabbat"] and bool(shabbat_status(sch))
    who = ", ".join(f"{p['name']} ({p['age']})" for p in players)
    others = [p for p in h["participants"] if p["role"] == "present"]  # by age only, no names of non-players
    guests = [p for p in h["participants"] if p.get("guest")]
    out = ["<section>", f"<h1>{e(h['title'])}</h1>",
           f'<p class="lead">מדריך למארחים. {e(occ)}{" · " if occ else ""}{e(nice_date(sch["date"]))}'
           + (f', {e(sch["start"])}' if sch.get("start") else "") + "</p>",
           f"<p><b>משחקים:</b> {e(who)}."
           + (f" <b>עוד ילדים בבית, בגילים:</b> {e(', '.join(str(p['age']) for p in others))}." if others else "")
           + f" <b>{len(stops)} תחנות.</b> הבדיקה נעשתה לפי הילד הצעיר ביותר בבית (גיל {e(rep.youngest)}).</p>"]
    out.append('<div class="box"><h3>מה נבדק ומה לא</h3><p>המקומות והפרסים נבחרו מתפריט קצר וסגור, והקובץ עבר בדיקה אוטומטית של סדר המסלול, '
               "רמת הקריאה והפנייה לכל ילד. סריקת הטקסט בכרטיסים חלקית ולא תתפוס כל מילה מסוכנת. "
               "היא לא ראתה את הבית שלכם, ולכן היא לא אומרת שהמשחק בטוח. "
               "<b>מבוגר עובר על המסלול לפני המשחק ונשאר עם הילדים עד הסוף.</b></p></div>")
    cut = "גוזרים את הכרטיסים לפני שבת ומניחים אותם לפי דף התשובות." if on_shabbat else "גוזרים את הכרטיסים לפי הקווים המקווקווים ומניחים אותם לפי דף התשובות."
    out.append('<h2>לפני שמתחילים</h2><ul class="check">'
               "<li>עוברים על המסלול ברגל, בגובה של הילד הצעיר. כל כרטיס נגיש בעמידה על הרצפה.</li>"
               "<li><b>קוראים כל כרטיס לפני שמחביאים אותו.</b> הבדיקה של הטקסט חלקית, ורק מבוגר יכול לוודא שכרטיס לא שולח ילד למקום מסוכן.</li>"
               "<li>אומרים לילדים מה מחוץ למשחק: מטבח, מרפסת, חלונות, מכשירי חשמל, ארונות, תנור ושירותים. לא נכנסים לתוך שום דבר.</li>"
               f"<li>{cut}</li>"
               "<li>מוודאים שאין שום דבר בדרך אל המרחב המוגן.</li>"
               "<li>שומרים את הפרסים רחוק מהישג יד עד הסוף. אוכלים רק בישיבה, אחרי המשחק.</li></ul>")
    rooms = {x["room_id"] for x in h["stations"]}
    candles_lit = 1 if h["candles"]["lit_during_hunt"] else 0
    if guests or len(rooms) > 1 or len(players) > 1:
        out.append('<div class="box"><h3>בזמן המשחק (נוהג מקובל)</h3><ul>'
                   + ("<li>סופרים את הילדים בהתחלה, בכל תחנה ובסוף.</li>" if guests or len(rooms) > 1 else "")
                   + ("<li>דלת הכניסה נשארת סגורה, ומבוגר פותח אותה לאורחים.</li>" if guests else "<li>דלת הכניסה נשארת סגורה.</li>")
                   + (f"<li>מבוגרים בבית בזמן המשחק: {e(h['adults_present'])}."
                      + (" כשאפשר, מבוגר אחד עם כל קבוצה קטנה." if h["adults_present"] - candles_lit > 1 else " המבוגר שעם הילדים נשאר קרוב לילד הצעיר ביותר.") + "</li>" if guests else "")
                   + ("<li>שומרים טלפון של ההורים של כל אורח.</li>" if guests else "")
                   + ("<li>הצעיר פותר ראשון. מי שסיים לא מגלה לאחרים, ועוזר בתפקיד של שומר הכרטיסים.</li>" if len(players) > 1 else "")
                   + "<li>ילד שהוצף יכול לעצור ולשבת ליד מבוגר.</li></ul></div>")
    candles = h["candles"]
    if candles["lit_during_hunt"]:
        names = ", ".join(ROOMS[x]["label"] for x in candles["room_ids"])
        out.append(f'<div class="box"><h3>נרות דולקים בזמן המשחק</h3><p>הנרות ב{e(names)}. אין שם תחנות. מבוגר אחד נשאר ליד הנרות כל הזמן, ומבוגר אחר נשאר עם הילדים.</p></div>')
    if h["format"] == "escape_room":
        out.append('<div class="box"><h3>חדר בריחה ביתי</h3><p>אף דלת לא ננעלת ואף ילד לא נשאר סגור בחדר. '
                   "ה\"מנעולים\" הם קופסאות או מעטפות עם קוד מדומה. אומרים לילדים שאפשר לצאת בכל רגע.</p></div>")
    space = h["home"].get("protected_space")
    target = f"אל: {h['home'].get('siren_place')}" if space == "none" else "למרחב המוגן"
    verb = "הולכים מיד" if space == "none" else "נכנסים מיד"
    out.append(f'<div class="box"><h3>אם יש אזעקה</h3><p>עוצרים את המשחק ו{verb} {e(target)}, עם כל הילדים. '
               "אם יש זמן ורק אם זה לא מעכב אתכם, מכבים בדרך כיריים, תנור, תנורי חימום ונרות. "
               "שם סופרים את הילדים. משאירים את אביזרי המשחק במקום.</p>"
               + ("<p>משפחה ששומרת שבת: לגבי כיבוי בשבת שואלים מראש את הרב של המשפחה.</p>" if h["keeps_shabbat"] else "")
               + "</div>")
    out.append('<div class="box"><h3>טלפונים לחירום</h3><p class="phones">מד"א <span class="ltr">101</span> · כבאות '
               '<span class="ltr">102</span> · המרכז הארצי למידע בהרעלות, רמב"ם <span class="ltr">04-7771900</span></p>'
               "<p>חשד לבליעת סוללה: פונים מיד לקבלת טיפול רפואי.</p></div>")
    nights = hanukkah_containing(d)
    if nights:
        a, z = nights[0], nights[-1]
        label = str(a.year) if a.year == z.year else f"{a.year}-{z.year}"
        line = f"נר ראשון ב-{a.day}.{a.month}.{a.year}, נר שמיני ב-{z.day}.{z.month}.{z.year}."
        if h["keeps_shabbat"]:
            fri = [f"{x.day}.{x.month}" for x in nights if x.weekday() == 4]
            sat = [f"{x.day}.{x.month}" for x in nights if x.weekday() == 5]
            if fri:
                line += f" <b>נרות של יום שישי ({', '.join(fri)})</b> מדליקים לפני השקיעה, לפני נרות שבת."
            if sat:
                line += f" במוצאי שבת ({', '.join(sat)}) מדליקים אחרי צאת השבת."
            if (z + dt.timedelta(days=1)).weekday() == 5:
                line += " במוצאי השבת שאחרי הנר השמיני כבר לא מדליקים."
        out.append(f"<h2>חנוכה {label}</h2><p>{line}</p>"
                   "<ul><li>אין תחנות בחדר עם נרות דולקים או בחלל פתוח אליו, ומבוגר נשאר ליד הנרות.</li>"
                   "<li>לא משחקים בזמן טיגון. אוכל מטוגן מתקרר לפני שמגישים.</li>"
                   "<li>ילדים עד גיל 9 מדליקים נרות רק בעזרת מבוגר. אוספים שיער ארוך ולובשים שרוולים צמודים.</li>"
                   "<li>מומלץ שיהיה בבית גלאי עשן.</li>"
                   + ("<li>מטבעות שוקולד: מבוגר מקלף ומשליך את העטיפה לפח.</li>" if "chocolate_coins" in h["treasure"]["prizes"] else "") + "</ul>")
    if on_shabbat:
        out.append('<div class="box"><h3>המשחק בשבת</h3><p>הכול מודפס, גזור ומונח לפני שבת. הילדים לא כותבים, לא גוזרים ולא מדביקים, '
                   "ואין טלפון, טיימר או פנס. כולם מקבלים אותו אוצר בסוף, בלי מנצח. המקור שלנו: פניני הלכה, שבת כד, ז, "
                   "שמדבר על ילדים שלא הגיעו לגיל מצוות ומחמיר יותר עם גדולים. יש בנושא דעות שונות, וההכרעה לגבי המשפחה שלכם היא של הרב שלכם.</p></div>")
    if guests:
        out.append('<div class="box"><h3>כשיש אורחים</h3><ul><li>לפני שבוחרים אוכל, שואלים כל הורה על אלרגיות ושומרים את האריזות עם הרכיבים.</li>'
                   "<li>לא מפרסמים תמונות של ילדים אחרים בלי הסכמה של ההורים שלהם.</li></ul></div>")
    credit = {"dicta_model": "ניקוד: מודל dictabert-large-char-menaked של דיקטה, ברישיון CC BY 4.0.",
              "nakdan_site": "ניקוד: הנקדן של דיקטה, ברישיון CC BY-NC-SA 4.0, לשימוש משפחתי בלבד."}.get(h.get("niqqud_route"))
    out.append('<h2>אחרי המשחק</h2><ul class="check"><li>אוספים כל כרטיס ופריט לפי הרשימה בדף התשובות, כדי שלא יישאר דבר לפעוט.</li>'
               "<li>התעודות נושאות שם פרטי בלבד. אם משתפים תמונה, בלי שם בית ספר, כתובת או תאריך לידה.</li></ul>"
               + (f'<p class="cuthint">{e(credit)}</p>' if credit else ""))
    out.append("</section>")
    return "".join(out)


def card_code(p, n):
    return f"{p['name']} {n}"


def answer_sheet(h, players, stops):
    rows = ['<section><h1>דף תשובות למארחים</h1><p class="lead">לא להראות לילדים. '
            "כל כרטיס מוביל למקום הבא, והמספר עליו אומר איפה להניח אותו.</p>"
            "<table><tr><th>שלב</th><th>איפה מניחים</th><th>מה מניחים</th><th>הפתרון של הכרטיסים</th><th>נאסף</th></tr>"]
    first = stops[0]["answer"]
    codes = "<br>".join(e(card_code(p, 1)) for p in players)
    rows.append(f"<tr><td>התחלה</td><td>נותנים ביד</td><td>{codes}</td><td>{e(first)}</td><td>&#9633;</td></tr>")
    for i, s in enumerate(stops, start=1):
        if s.get("treasure"):
            prizes = ", ".join(PRIZES[p]["label"] for p in h["treasure"]["prizes"])
            note = "<br><b>מניחים בפינה הרחוקה מהדלת, והדלת הכבדה מחוץ למשחק.</b>" if s["room_id"] == "mamad" else ""
            rows.append(f"<tr><td><b>אוצר</b></td><td>{e(s['room'])}: {e(s['spot'])}{note}</td><td>{e(prizes)}</td><td>סוף המסלול</td><td>&#9633;</td></tr>")
        else:
            codes = "<br>".join(e(card_code(p, i + 1)) for p in players)
            note = "<br><b>מניחים בפינה הרחוקה מהדלת, והדלת הכבדה מחוץ למשחק.</b>" if s["room_id"] == "mamad" else ""
            rows.append(f"<tr><td>תחנה {i}</td><td>{e(s['room'])}: {e(s['spot'])}{note}</td><td>{codes}</td><td>{e(stops[i]['answer'])}</td><td>&#9633;</td></tr>")
    rows.append("</table></section>")
    return "".join(rows)


def hint_ladder(h, players, stops):
    rows = ['<section><h1>סולם רמזים</h1><p class="lead">למארחים בלבד. ילד נתקע? מקריאים קודם את רמז 1, אחר כך את רמז 2. התשובה היא המוצא האחרון.</p>'
            "<table><thead><tr><th>כרטיס</th><th>רמז 1</th><th>רמז 2</th><th>התשובה ולמה</th></tr></thead><tbody>"]
    for p in players:
        seq = [h["start"]["clues"][p["id"]]] + [s["clues"][p["id"]] for s in stops if not s.get("treasure")]
        for n, c in enumerate(seq, start=1):
            rows.append(f"<tr><td>{e(card_code(p, n))}</td><td>{e(c['hints'][0])}</td><td>{e(c['hints'][1])}</td><td>{e(c['hints'][2])}</td></tr>")
    rows.append("</tbody></table></section>")
    return "".join(rows)


def card_html(p, n, clue, target):
    size = SIZES[p["reading_stage"]]
    mode = clue.get("mode", "read")
    inner = ""
    if mode == "picture":
        inner += icon(target["icon"], 130 if clue.get("text") else 190)
    if clue.get("text"):
        inner += f'<div style="font-size:{size}">{e(clue["text"])}</div>'
    if clue.get("puzzle"):
        inner += f'<div class="cipher">{e(clue["puzzle"]["cipher"])}</div>'
    note = {"adult_reads": "מבוגר מקריא בקול", "picture": "מה רואים בציור? לשם הולכים"}.get(mode, "")
    return (f'<div class="card"><div class="top"><span class="who">{e(p["name"])}</span><span>כרטיס {n}</span></div>'
            f'<div class="body">{inner}</div><div class="note">{e(note)}</div></div>')


def cards(h, players, stops):
    out = []
    for p in players:
        seq = [h["start"]["clues"][p["id"]]] + [s["clues"][p["id"]] for s in stops if not s.get("treasure")]
        out.append(f'<section><h2>כרטיסים של {e(p["name"])}</h2><p class="cuthint">גוזרים לאורך הקווים המקווקווים.</p><div class="cards">')
        out += [card_html(p, n, c, stops[n - 1]) for n, c in enumerate(seq, start=1)]
        out.append("</div></section>")
    return "".join(out)


def certificates(h, players):
    occ = OCCASIONS.get(h["occasion"], "")
    year = dt.date.fromisoformat(h["schedule"]["date"]).year
    no_sign = h["keeps_shabbat"] and bool(shabbat_status(h["schedule"]))
    out = ["<section>"]
    for p in players:
        out.append(f'<div class="cert">{icon("treasure", 170)}<div class="kicker">תעודת הצלחה</div><div class="name">{e(p["name"])}</div>'
                   f'<div class="line">על פתרון כל החידות במסע האוצר</div><div class="line">{e(occ)} {year}</div>'
                   + ('' if no_sign else '<div class="sign">חתימת המארחים</div>') + '</div>')
    out.append("</section>")
    return "".join(out)


def font_css(path, base):
    if not path:
        return "", '"Noto Sans Hebrew", "Arial Hebrew", Arial, "David", sans-serif'
    full = safe_path(base, path)
    with open(full, "rb") as f:
        data = base64.b64encode(f.read()).decode("ascii")
    return (f'@font-face {{ font-family: "HuntFont"; src: url(data:font/ttf;base64,{data}); }}',
            '"HuntFont", "Noto Sans Hebrew", Arial, sans-serif')


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("hunt")
    ap.add_argument("--out", default="kit.html")
    ap.add_argument("--font-file")
    a = ap.parse_args()
    base = os.path.dirname(os.path.realpath(a.hunt))
    out = safe_path(base, a.out)
    h = load(a.hunt)
    try:
        rep = validate(h)
    except (KeyError, TypeError, AttributeError, ValueError) as err:
        print(f"ERROR: the hunt file has the wrong shape ({type(err).__name__}: {err})", file=sys.stderr)
        return 2
    if rep.errors:
        print(f"REFUSED: {len(rep.errors)} error(s). Nothing was built. Fix them first:", file=sys.stderr)
        for x in rep.errors:
            print(f"- [{x['code']}] {x['where']}: {x['message']}", file=sys.stderr)
            if x["fix"]:
                print(f"    suggested alternative: {x['fix']}", file=sys.stderr)
        return 1
    h = rep.hunt
    players = [p for p in h["participants"] if p["role"] == "player"]
    stops = route(h)
    face, stack = font_css(a.font_file, base)
    doc = ('<!doctype html><html lang="he" dir="rtl"><head><meta charset="utf-8">'
           f"<title>{e(h['title'])}</title><style>{face}{CSS.replace('FONTSTACK', stack)}</style></head><body>"
           + host_guide(h, rep, players, stops) + answer_sheet(h, players, stops) + hint_ladder(h, players, stops)
           + cards(h, players, stops) + certificates(h, players) + "</body></html>")
    with open(out, "w", encoding="utf-8") as f:
        f.write(doc)
    print(f"built {out}: {len(players)} player(s), {len(stops)} stops, {len(rep.warnings)} warning(s)")
    for x in rep.warnings:
        print(f"- warning [{x['code']}] {x['where']}: {x['message']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
