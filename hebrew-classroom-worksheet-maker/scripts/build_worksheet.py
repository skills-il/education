#!/usr/bin/env python3
"""Turn a worksheet JSON into one print-ready, right-to-left A4 HTML file.

Student pages come first, then a separate teacher key generated from the same items, so the key
cannot drift from what is printed. Black and white only. Every math expression is an isolated
left-to-right run. No network and no external files.

Usage: python3 build_worksheet.py worksheet.json --out worksheet.html
"""

import argparse
import html
import os
import re
import sys
import tempfile

from pictures import PICTURES
from worksheet_lib import (checked_answer_problem, counters_operands, has_digit_or_operator, has_math, iter_items,
                           load_worksheet, printed_strings, safe_path)

FONT_PT = {"gan": 24, "1": 22, "2": 18, "3": 15, "4": 13, "5": 13, "6": 13}
CSS = """
@page { size: A4; margin: 14mm 16mm 14mm 16mm; }
* { box-sizing: border-box; }
html, body { margin: 0; background: #fff; color: #000; }
body { font-family: "Noto Sans Hebrew", "Arial Hebrew", Arial, sans-serif; font-size: var(--base); line-height: 1.55; }
.page { break-after: page; }
.page:last-child { break-after: auto; }
h1 { font-size: 1.45em; margin: 0 0 .15em; text-align: center; }
.fields { display: flex; justify-content: space-between; gap: 10mm; font-size: 12pt; margin-bottom: 4mm; }
.fields span { flex: 1; border-bottom: 1.2pt solid #000; padding-bottom: 1mm; }
.fields .code { flex: 0 0 auto; border: 0; }
section { border: 1.2pt solid #000; border-radius: 3mm; padding: 3mm 4mm; margin-bottom: 4mm; }
h2 { break-after: avoid; font-size: .82em; margin: 0 0 2mm; display: flex; flex-wrap: wrap; align-items: center; gap: 1mm 3mm; }
.num { display: inline-flex; width: 1.5em; height: 1.5em; align-items: center; justify-content: center; border: 1.2pt solid #000; border-radius: 999px; font-size: .85em; flex: none; }
.ins { font-weight: 400; }
.sec-reading p { margin: 0 0 1mm; font-size: 1.12em; line-height: 1.9; }
.q { display: flex; flex-wrap: wrap; align-items: center; gap: 3mm 5mm; margin-bottom: 2.5mm; break-inside: avoid; }
.stem { flex: 1 0 165mm; }
.opt { border: 1.2pt solid #000; border-radius: 6mm; padding: .5mm 5mm; min-width: 22mm; text-align: center; }
.blank { display: inline-block; min-width: 18mm; border-bottom: 1.4pt solid #000; height: 1em; vertical-align: baseline; }
.sec-match { break-inside: avoid; }
.match { display: grid; grid-template-columns: 1fr 34mm 1fr; align-items: center; row-gap: 2mm; }
.word { font-size: 1.1em; display: flex; align-items: center; justify-content: space-between; }
.dot { width: 3mm; height: 3mm; border-radius: 999px; background: #000; display: inline-block; flex: none; }
.picbox { display: flex; align-items: center; gap: 2mm; justify-content: flex-end; }
.pic { width: 21mm; height: 21mm; flex: none; }
.pic svg { display: block; width: inherit; height: inherit; }
.picnum { font-size: 12pt; font-weight: 700; border: 1.2pt solid #000; border-radius: 999px; width: 7mm; height: 7mm; display: inline-flex; align-items: center; justify-content: center; }
.math-row { display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 4mm; padding: 1mm 0; break-inside: avoid; }
bdi.math { direction: ltr; unicode-bidi: isolate; font-family: Arial, "Noto Sans Hebrew", sans-serif; font-size: 1.05em; white-space: nowrap; }
.prompt { flex: 1 0 165mm; }
.icon { display: inline-block; width: 1.05em; height: 1.05em; flex: none; }
.icon svg { display: block; width: inherit; height: inherit; }
.counters { direction: ltr; display: flex; align-items: center; gap: 1mm; flex-wrap: nowrap; }
.counters .pic { width: 8.5mm; height: 8.5mm; }
.counters b { margin: 0 1.5mm; font-size: 1em; }
.sec-first_letter .pic { width: 16mm; height: 16mm; }
.sheet { width: 178mm; font-size: inherit; }
.sheet > thead > tr > td, .sheet > tbody > tr > td { border: 0; padding: 0; }
.keybanner { border: 2pt solid #000; padding: 2mm 4mm; text-align: center; font-weight: 700; margin-bottom: 4mm; }
table { width: 178mm; border-collapse: collapse; font-size: 12pt; }
td, th { border: 1pt solid #000; padding: 1.2mm 2mm; text-align: right; vertical-align: top; }
.foot { font-size: 10pt; margin-top: 3mm; }
.aloud { border: 1.2pt solid #000; padding: 2mm 4mm; margin-bottom: 4mm; font-size: 13pt; }
.aloud h2 { font-size: 13pt; }
.aloud p { margin: 0 0 1mm; }
"""


def esc(text):
    return html.escape(str(text if text is not None else ""), quote=True)


def text_html(value):
    return esc(value)


def blanks_html(text):
    return re.sub(r"_{2,}", '<span class="blank"></span>', text_html(text))


def math_html(expr):
    return f'<bdi dir="ltr" class="math">{re.sub(r"_{2,}", chr(60) + "span class=" + chr(34) + "blank" + chr(34) + "></span>", esc(expr))}</bdi>'


def picture(name):
    pic = PICTURES.get(name)
    if not pic:
        sys.exit(f"ERROR: unknown picture {name!r}. Run the checker first.")
    return f'<span class="pic">{pic["svg"]}</span>'


ICON_STYLE = 'fill="none" stroke="#000" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"'
ICONS = {
    "reading": '<path d="M32 16c-6-5-16-6-24-4v38c8-2 18-1 24 4 6-5 16-6 24-4V12c-8-2-18-1-24 4z"/><path d="M32 16v38"/>',
    "mc": '<circle cx="32" cy="32" r="24"/>',
    "first_letter": '<circle cx="32" cy="32" r="24"/>',
    "match": '<circle cx="10" cy="14" r="5"/><circle cx="54" cy="50" r="5"/><path d="M15 18l34 28"/>',
    "math": '<path d="M12 52l4-14L44 10l10 10-28 28z"/><path d="M38 16l10 10"/>',
}


def icon(kind):
    body = ICONS.get(kind)
    return f'<span class="icon"><svg viewBox="0 0 64 64" aria-hidden="true"><g {ICON_STYLE}>{body}</g></svg></span>' if body else ""


def heading(number, section):
    title = text_html(section.get("title", ""))
    ins = text_html(section.get("instruction", ""))
    return (f'<h2><span class="num">{number}</span>{icon(section.get("type"))}<span>{title}</span>'
            + (f'<span class="ins">{ins}</span>' if ins else "") + "</h2>")


def rotated(items, seed=""):
    """Picture order for a matching task: every picture moves, and the shift varies by section."""
    if len(items) < 2:
        return list(items)
    shift = 1 + sum(ord(ch) for ch in str(seed)) % (len(items) - 1)
    return items[shift:] + items[:shift]


def picture_numbers(section):
    order = rotated(section.get("items", []), section.get("id", ""))
    return {item["id"]: idx + 1 for idx, item in enumerate(order)}, order


def render_section(number, section):
    kind = section.get("type")
    out = [f'<section class="sec-{esc(kind)}">', heading(number, section)]
    if kind == "reading":
        out += [f"<p>{text_html(line)}</p>" for line in section.get("text", [])]
    elif kind == "mc":
        for idx, item in enumerate(section.get("items", []), 1):
            options = "".join(f'<span class="opt">{text_html(o)}</span>' for o in item.get("options", []))
            out.append(f'<div class="q" data-item="{esc(item["id"])}"><span class="stem">{idx}. '
                       f'{blanks_html(item.get("stem", ""))}</span>{options}</div>')
    elif kind == "match":
        numbers, order = picture_numbers(section)
        out.append('<div class="match">')
        for left, right in zip(section.get("items", []), order):
            out.append(f'<div class="word" data-item="{esc(left["id"])}">{text_html(left["word"])}'
                       '<span class="dot"></span></div><div></div>'
                       f'<div class="picbox" data-pic="{esc(right["id"])}:{numbers[right["id"]]}">'
                       f'<span class="dot"></span>{picture(right["picture"])}'
                       f'<span class="picnum">{numbers[right["id"]]}</span></div>')
        out.append("</div>")
    elif kind == "math":
        for item in section.get("items", []):
            counters = ""
            if item.get("counters"):
                if counters_operands(item["expr"]) != tuple(item["counters"]) or sum(item["counters"]) > 10:
                    sys.exit(f"ERROR: {item['id']}: counters work only for a + b = ___ up to 10, and must match it.")
                groups = []
                for count in item["counters"]:
                    groups.append("".join(picture(item.get("picture", "dreidel")) for _ in range(int(count))))
                counters = '<span class="counters">' + "<b>+</b>".join(groups) + "</span>"
            prompt = f'<span class="prompt">{text_html(item["prompt"])}</span>' if item.get("prompt") else ""
            out.append(f'<div class="math-row" data-item="{esc(item["id"])}">{prompt}'
                       f'{math_html(item["expr"])}{counters}</div>')
    elif kind == "first_letter":
        for idx, item in enumerate(section.get("items", []), 1):
            cells = "".join(f'<span class="picbox" data-pic="{esc(item["id"])}:{n}">{picture(name)}'
                            f'<span class="picnum">{n}</span></span>'
                            for n, name in enumerate(item.get("picture_options", []), 1))
            out.append(f'<div class="q" data-item="{esc(item["id"])}"><span class="stem">{idx}. '
                       f'{esc(item.get("letter", ""))}</span>{cells}</div>')
    else:
        sys.exit(f"ERROR: section type {kind!r} is not supported by the builder.")
    out.append("</section>")
    return "".join(out)


def answer_text(section, item, numbers):
    kind = section.get("type")
    if kind == "match":
        num = numbers[section["id"]][item["id"]]
        return f'<span data-picref="{esc(item["id"])}:{num}">תמונה {num}</span>'
    if kind == "first_letter":
        num = item["picture_options"].index(item["answer"]) + 1
        return f'<span data-picref="{esc(item["id"])}:{num}">תמונה {num}</span>'
    if kind == "math":
        return f'<bdi dir="ltr" class="math">{esc(item["answer"])}</bdi>'
    return text_html(item.get("answer", ""))


def question_text(section, item):
    if section.get("type") == "math":
        return math_html(item["expr"])
    if section.get("type") == "match":
        return text_html(item.get("word", ""))
    if section.get("type") == "first_letter":
        return esc(item.get("letter", ""))
    if item.get("teacher_question"):
        number = section["items"].index(item) + 1
        return f'{number}. {text_html(item["teacher_question"])}'
    return blanks_html(item.get("stem", ""))


def render_read_aloud(section):
    lines = "".join(f"<p>{text_html(line)}</p>" for line in section.get("text", []))
    return f'<div class="aloud"><h2>{text_html(section.get("title", "קטע להקראה"))}</h2>{lines}</div>'


def render_key(data):
    meta = data["meta"]
    numbers = {}
    for section in data["sections"]:
        if section.get("type") == "match":
            numbers[section["id"]] = picture_numbers(section)[0]
    rows = []
    for section, item in iter_items(data):
        rows.append(f'<tr data-ref="{esc(item["id"])}"><td>{text_html(section.get("title", ""))}</td>'
                    f"<td>{question_text(section, item)}</td><td><b>{answer_text(section, item, numbers)}</b></td></tr>")
    note = text_html(meta.get("teacher_note", ""))
    credit = text_html(meta.get("niqqud_credit", ""))
    has_prompts = any(item.get("prompt") for _, item in iter_items(data))
    aloud = "".join(render_read_aloud(x) for x in data["sections"] if x.get("type") == "read_aloud")
    return ('<div class="page" data-part="teacher"><div class="keybanner">דף תשובות למורים, לא לצילום לתלמידים</div>'
            f'<h1>{text_html(meta.get("title", ""))}</h1>{aloud}'
            '<table><thead><tr><th>משימה</th><th>פריט</th><th>תשובה</th></tr></thead>'
            f'<tbody>{"".join(rows)}</tbody></table>'
            + (f'<p class="foot">{note}</p>' if note else "")
            + (f'<p class="foot">{credit}</p>' if credit else "")
            + ('<p class="foot"><b>לבדיקה שלכם:</b> קראו כל שאלה מילולית וודאו שהתרגיל שלה מתאים לה.</p>' if has_prompts else "")
            + '<p class="foot">הדף הוכן בעזרת בינה מלאכותית. זה לא אישור של משרד החינוך. '
            "לפני הצילום קראו את הדף ובדקו את הניקוד.</p></div>")


def split_pages(meta, sections):
    per_page = int(meta.get("sections_per_page") or 3)
    return [sections[i:i + per_page] for i in range(0, len(sections), per_page)] or [[]]


def build(data):
    meta = data["meta"]
    base = FONT_PT.get(str(meta.get("grade")), 15)
    base = int(meta.get("font_pt") or base)
    code = esc(meta.get("version_code", ""))
    fields = ('<div class="fields"><span>שם:</span><span>תאריך:</span>'
              + (f'<span class="code">{code}</span>' if code else "") + "</div>")
    student_sections = [x for x in data["sections"] if x.get("type") != "read_aloud"]
    for where, text, _ in printed_strings(data):
        if has_math(text):
            sys.exit(f"ERROR: {where}: arithmetic or a comparison can be printed only in a math section.")
    for section, item in iter_items(data):
        if section.get("type") == "math":
            problem = checked_answer_problem(item)
            if problem:
                sys.exit(f"ERROR: {item.get('id')}: {problem}")
        elif section.get("type") == "mc":
            mc_texts = [item.get("stem", ""), item.get("teacher_question", "")] + list(item.get("options", []) or [])
            if any(has_digit_or_operator(text) for text in mc_texts):
                sys.exit(f"ERROR: {item.get('id')}: multiple choice cannot hold digits or operators. Use a math section.")
    pages, number = [], 0
    for chunk in split_pages(meta, student_sections):
        body = []
        for section in chunk:
            number += 1
            body.append(render_section(number, section))
        title = f'<h1>{text_html(meta.get("title", ""))}</h1>' if not pages else ""
        pages.append(f'<div class="page" data-part="student">{title}<table class="sheet"><thead><tr><td>{fields}</td></tr></thead>'
                     f'<tbody><tr><td>{"".join(body)}</td></tr></tbody></table></div>')
    return (f'<!doctype html><html lang="he" dir="rtl"><head><meta charset="utf-8"><title>{esc(meta.get("title", ""))}</title>'
            f"<style>:root{{--base:{base}pt}}{CSS}</style></head><body>{''.join(pages)}{render_key(data)}</body></html>")


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("worksheet")
    parser.add_argument("--out", required=True, help="output file, inside the worksheet folder")
    args = parser.parse_args()
    data = load_worksheet(args.worksheet)
    base_dir = os.path.dirname(os.path.abspath(args.worksheet))
    out = safe_path(base_dir, args.out)
    content = build(data)
    descriptor, temporary = tempfile.mkstemp(dir=os.path.dirname(out), prefix=".worksheet-", suffix=".tmp")
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as handle:
            handle.write(content)
        os.chmod(temporary, 0o644)
        os.replace(temporary, out)
    except BaseException:
        if os.path.exists(temporary):
            os.unlink(temporary)
        raise
    print(f"wrote {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
