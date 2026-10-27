#!/usr/bin/env python3
"""Turn per-criterion scores for an anonymised class into a DRAFT grade sheet CSV.

Input is a JSON file with a rubric and one record per student code:

    {
      "rubric": {"name": "grade 8 writing", "status": "practice", "scale_to": 100,
                 "criteria": [{"id": "syntax", "label": "תחביר", "max": 5}, ...]},
      "students": [
        {"code": "S01", "scores": {"syntax": 4, ...},
         "exempt": ["spelling"],
         "adjusted": [],
         "flags": ["position:alt_interpretation"],
         "batch": 1, "words": 312},
        ...
      ]
    }

Rules the script enforces (it exits 2 and names the record otherwise):
  * rubric.status is "practice" (a template or practice rubric) or "school"
    (the teacher's or school's own rubric). It is printed on the sheet.
  * codes are short: one capital Latin or Hebrew letter plus 1-3 ASCII digits
    (S01, ח1), or 2-3 ASCII digits (07). Nothing else is accepted, so a name or an ID number
    cannot be a code.
  * flags are "criterion:reason" with reason from a fixed list (see REASONS).
    Free text is not allowed anywhere in the sheet: a Hebrew name inside a
    sentence cannot be detected mechanically, so the sheet carries none.
  * every string value in a student record is scanned for a 9-digit number,
    an email address, a phone number, or a capitalised Latin first+last name.
  * a criterion listed in "exempt" must have no score. It is removed from both
    the total and the maximum, and the scaled grade is computed over what is left.
    A warning is printed when exemptions remove more than half of a code's maximum.
  * a criterion listed in "adjusted" is scored with an accommodation applied (for
    example, spelling errors not counted). It stays in the total and is printed on
    the row so the teacher can audit it. A criterion cannot be both.
  * scores must be finite numbers (not true/false, not NaN) within 0..max.
  * the rubric name and every criterion label are scanned for the same PII.

Output:
  * a CSV (UTF-8 with BOM, so Excel shows Hebrew) whose first line says the
    sheet is an unapproved draft, then the rubric name, status and date, then
    one row per student and a class-average row. The approval column is empty:
    the teacher fills it row by row.
  * a summary on stdout: weakest criteria, mean per batch (drift check), and a
    length-vs-score correlation when word counts are given for at least 10
    complete answers (length-bias check).

Standard library only. No network access.
"""

import argparse
import csv
import datetime
import json
import math
import re
import sys

CODE_RE = re.compile(r"(?:[A-Z\u05d0-\u05ea][0-9]{1,3}|[0-9]{2,3})")
FORBIDDEN_KEYS = {"name", "full_name", "student_name", "first_name", "last_name",
                  "id_number", "teudat_zehut", "tz", "email", "phone", "gender",
                  "diagnosis", "accommodation_reason"}
ALLOWED_KEYS = {"code", "scores", "exempt", "adjusted", "flags", "batch", "words"}
MIN_FOR_CORRELATION = 10
PII_PATTERNS = [
    (re.compile(r"(?<!\d)\d{9}(?!\d)"), "a 9-digit number (ID-like)"),
    (re.compile(r"(?<!\d)\d{8}-\d(?!\d)"), "an ID number with check digit"),
    (re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+"), "an email address"),
    (re.compile(r"(?<!\d)(?:\+972[-\s]?|0)(?:[23489]|5\d|7\d)[-\s]?\d{3}[-\s]?\d{4}(?!\d)"), "a phone number"),
    (re.compile(r"\b[A-Z][a-z]+\s+[A-Z][a-z]+\b"), "a Latin first and last name"),
]
REASONS = {
    "teacher_judgment": ("נדרש שיקול דעת", "needs teacher judgment"),
    "alt_interpretation": ("פרשנות חלופית", "alternative interpretation"),
    "between_bands": ("בין שתי רמות", "between two bands"),
    "transcription_unconfirmed": ("תמלול לא אושר", "transcription not confirmed"),
    "possible_ai_text": ("ייתכן טקסט מבינה מלאכותית", "possible AI-written text"),
    "off_topic": ("לא לעניין", "off topic"),
    "too_short": ("קצר מאוד", "very short"),
    "sensitive_content": ("תוכן רגיש, לטיפול המורה", "sensitive content, teacher to handle"),
}
STATUS = {"practice": ("מחוון תרגול, לא רשמי", "practice rubric, unofficial"),
          "school": ("מחוון של המורה או בית הספר", "teacher's or school's rubric")}

EXAMPLE = {
    "rubric": {
        "name": "grade 8 writing",
        "status": "practice",
        "scale_to": 100,
        "criteria": [
            {"id": "open_close", "label": "פתיחה וסיום", "max": 2},
            {"id": "position", "label": "עמדה וביסוס", "max": 7},
            {"id": "cohesion", "label": "לכידות", "max": 4},
            {"id": "audience", "label": "מודעות לנמען", "max": 2},
            {"id": "syntax", "label": "תחביר", "max": 5},
            {"id": "register", "label": "משלב ואוצר מילים", "max": 3},
            {"id": "spelling", "label": "כתיב", "max": 2},
        ],
    },
    "students": [
        {"code": "S01", "batch": 1, "words": 310,
         "scores": {"open_close": 2, "position": 5, "cohesion": 3, "audience": 2,
                    "syntax": 4, "register": 2, "spelling": 1}},
        {"code": "S02", "batch": 1, "words": 240,
         "scores": {"open_close": 1, "position": 3, "cohesion": 2, "audience": 1,
                    "syntax": 3, "register": 2, "spelling": 2},
         "flags": ["position:alt_interpretation"]},
        {"code": "S03", "batch": 2, "words": 355, "exempt": ["spelling"],
         "scores": {"open_close": 2, "position": 6, "cohesion": 4, "audience": 2,
                    "syntax": 5, "register": 3}},
        {"code": "S04", "batch": 2, "words": 290,
         "scores": {},
         "flags": ["all:transcription_unconfirmed"]},
    ],
}

HEADERS = {
    "he": {"code": "קוד", "total": "סה\"כ", "max": "מקסימום", "scaled": "ציון טיוטה",
           "exempt": "פטור", "adjusted": "מותאם", "flags": "לבדיקת המורה", "approved": "אישור המורה (שורה-שורה)",
           "avg": "ממוצע כיתתי",
           "banner": "טיוטה, לא אושר על ידי המורה. הצעת ציון שנוצרה בסיוע בינה מלאכותית. לאשר כל שורה בנפרד אחרי קריאת הנימוקים.",
           "rubric": "מחוון", "status": "סטטוס", "date": "תאריך"},
    "en": {"code": "code", "total": "total", "max": "max", "scaled": "draft_grade",
           "exempt": "exempt", "adjusted": "adjusted", "flags": "teacher_check", "approved": "teacher_approval_per_row",
           "avg": "class_average",
           "banner": "DRAFT, not approved by the teacher. AI-assisted grade suggestions. Approve each row separately after reading the reasons.",
           "rubric": "rubric", "status": "status", "date": "date"},
}


def fail(msg):
    print(f"error: {msg}", file=sys.stderr)
    sys.exit(2)


def scan_pii(where, value):
    if isinstance(value, dict):
        for k, v in value.items():
            scan_pii(where, k)
            scan_pii(where, v)
    elif isinstance(value, list):
        for v in value:
            scan_pii(where, v)
    elif isinstance(value, str):
        for pat, what in PII_PATTERNS:
            if pat.search(value):
                fail(f"{where}: a value contains {what}. Remove identifying data before building the sheet.")


def validate(data):
    rubric = data.get("rubric")
    students = data.get("students")
    if not isinstance(rubric, dict) or not isinstance(students, list):
        fail("input needs a 'rubric' object and a 'students' list")
    if rubric.get("status") not in STATUS:
        fail("rubric.status must be 'practice' or 'school'")
    scan_pii("rubric.name", rubric.get("name", ""))
    criteria = rubric.get("criteria") or []
    if not criteria:
        fail("rubric has no criteria")
    ids = [c.get("id") for c in criteria]
    if len(set(ids)) != len(ids) or not all(ids):
        fail("every criterion needs a unique 'id'")
    for c in criteria:
        scan_pii(f"criterion {c.get('id')!r}", [c.get("id", ""), c.get("label", "")])
        if not is_number(c.get("max")) or c["max"] <= 0:
            fail(f"criterion {c.get('id')!r} needs a positive 'max'")
    seen = set()
    for i, s in enumerate(students):
        where = f"students[{i}]"
        if not isinstance(s, dict):
            fail(f"{where} is not an object")
        bad = FORBIDDEN_KEYS & {k.lower() for k in s}
        if bad:
            fail(f"{where} has identifying field(s) {sorted(bad)}. Codes only; the key, gender and "
                 "accommodation reasons stay with the teacher.")
        extra = set(s) - ALLOWED_KEYS
        if extra:
            fail(f"{where} has unknown field(s) {sorted(extra)}. Allowed: {sorted(ALLOWED_KEYS)}")
        code = s.get("code")
        if not isinstance(code, str) or not CODE_RE.fullmatch(code):
            fail(f"{where}: code {code!r} is not a short code (a letter and 1-3 digits such as S01 or ח1, or 2-3 digits such as 07).")
        where = code
        scan_pii(where, s)
        if code in seen:
            fail(f"duplicate code {code!r}")
        seen.add(code)
        exempt = s.get("exempt") or []
        for cid in exempt:
            if cid not in ids:
                fail(f"{code}: exempt criterion {cid!r} is not in the rubric")
        if len(set(exempt)) == len(ids):
            fail(f"{code}: every criterion is exempt; nothing to grade")
        adjusted = s.get("adjusted") or []
        for cid in adjusted:
            if cid not in ids:
                fail(f"{code}: adjusted criterion {cid!r} is not in the rubric")
            if cid in exempt:
                fail(f"{code}: {cid} cannot be both exempt and adjusted")
        for cid, val in (s.get("scores") or {}).items():
            if cid not in ids:
                fail(f"{code}: score for unknown criterion {cid!r}")
            if cid in exempt:
                fail(f"{code}: {cid} is exempt and must not be scored")
            mx = next(c["max"] for c in criteria if c["id"] == cid)
            if not is_number(val):
                fail(f"{code}: {cid}={val!r} is not a finite number")
            if val < 0 or val > mx:
                fail(f"{code}: {cid}={val!r} is outside 0..{mx}")
        for f in s.get("flags") or []:
            if not isinstance(f, str) or f.count(":") != 1:
                fail(f"{code}: flag {f!r} must be 'criterion:reason'")
            cid, reason = f.split(":")
            if cid not in ids and cid != "all":
                fail(f"{code}: flag names unknown criterion {cid!r}")
            if reason not in REASONS:
                fail(f"{code}: flag reason {reason!r} not in {sorted(REASONS)}")
        for k in ("batch", "words"):
            if k in s and not (isinstance(s[k], int) and s[k] >= 0):
                fail(f"{code}: {k} must be a non-negative whole number")
    return rubric, criteria, students


def is_number(x):
    return isinstance(x, (int, float)) and not isinstance(x, bool) and math.isfinite(x)


def fmt(x):
    return str(int(x)) if float(x).is_integer() else f"{x:.1f}"


def pearson(xs, ys):
    n = len(xs)
    if n < 3:
        return None
    mx, my = sum(xs) / n, sum(ys) / n
    sx = math.sqrt(sum((x - mx) ** 2 for x in xs))
    sy = math.sqrt(sum((y - my) ** 2 for y in ys))
    if sx == 0 or sy == 0:
        return None
    return sum((x - mx) * (y - my) for x, y in zip(xs, ys)) / (sx * sy)


def build(data, lang):
    rubric, criteria, students = validate(data)
    h = HEADERS[lang]
    li = 0 if lang == "he" else 1
    scale_to = rubric.get("scale_to")
    preamble = [
        [h["banner"]],
        [h["rubric"], rubric.get("name", ""), h["status"], STATUS[rubric["status"]][li],
         h["date"], datetime.date.today().isoformat()],
    ]
    header = [h["code"]] + [c.get("label", c["id"]) for c in criteria] + [h["total"], h["max"]]
    if scale_to:
        header.append(h["scaled"])
    header += [h["exempt"], h["adjusted"], h["flags"], h["approved"]]
    label_of = {c["id"]: c.get("label", c["id"]) for c in criteria}
    full_max = sum(c["max"] for c in criteria)
    warnings = []

    rows, ratios_src, stats = [], {c["id"]: [] for c in criteria}, []
    for s in students:
        scores = s.get("scores") or {}
        exempt = set(s.get("exempt") or [])
        adjusted = set(s.get("adjusted") or [])
        flags = []
        for f in s.get("flags") or []:
            cid, reason = f.split(":")
            label = (("כל התשובה" if lang == "he" else "whole answer") if cid == "all"
                     else next(c.get("label", c["id"]) for c in criteria if c["id"] == cid))
            flags.append(f"{label}: {REASONS[reason][li]}")
        missing = [c["id"] for c in criteria if c["id"] not in scores and c["id"] not in exempt]
        if missing:
            flags.append(("חסר ציון: " if lang == "he" else "missing: ")
                         + ", ".join(c.get("label", c["id"]) for c in criteria if c["id"] in missing))
        row, total, max_total = [s["code"]], 0.0, 0.0
        for c in criteria:
            if c["id"] in exempt:
                row.append(h["exempt"])
                continue
            max_total += c["max"]
            v = scores.get(c["id"])
            row.append("" if v is None else fmt(v))
            if v is not None:
                total += v
                ratios_src[c["id"]].append(v)
        # An incomplete record gets no total: a partial sum would read as a low grade.
        row += ["" if missing else fmt(total), fmt(max_total)]
        if scale_to:
            scaled = None if missing else round(total / max_total * scale_to, 1)
            row.append("" if scaled is None else fmt(scaled))
        row += [", ".join(label_of[c] for c in sorted(exempt)),
                ", ".join(label_of[c] for c in sorted(adjusted)), "; ".join(flags), ""]
        if full_max - max_total > full_max / 2:
            warnings.append(f"{s['code']}: exemptions remove more than half of the maximum "
                            f"({fmt(full_max - max_total)} of {fmt(full_max)}); the grade rests on few criteria")
        rows.append(row)
        if not missing:
            stats.append((s.get("batch"), s.get("words"), total / max_total))

    avg_row = [h["avg"]]
    ratios = []
    for c in criteria:
        vals = ratios_src[c["id"]]
        if vals:
            a = sum(vals) / len(vals)
            avg_row.append(fmt(round(a, 1)))
            ratios.append((a / c["max"], c))
        else:
            avg_row.append("")
    avg_row += [""] * (len(header) - len(avg_row))
    return preamble, header, rows, avg_row, ratios, stats, warnings


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("input", nargs="?", help="scores JSON file")
    ap.add_argument("-o", "--output", default="grade_sheet.csv", help="CSV path (default grade_sheet.csv)")
    ap.add_argument("--lang", choices=["he", "en"], default="he", help="sheet language")
    ap.add_argument("--example", action="store_true", help="run on a built-in four-student example")
    ap.add_argument("--print-example-input", action="store_true", help="print the example input JSON and exit")
    args = ap.parse_args()

    if args.print_example_input:
        print(json.dumps(EXAMPLE, ensure_ascii=False, indent=2))
        return
    if args.example:
        data = EXAMPLE
    elif args.input:
        with open(args.input, encoding="utf-8") as f:
            data = json.load(f)
    else:
        ap.error("give an input JSON file, or --example")

    preamble, header, rows, avg_row, ratios, stats, warnings = build(data, args.lang)
    with open(args.output, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerows(preamble)
        w.writerow(header)
        w.writerows(rows)
        w.writerow(avg_row)

    flagged = sum(1 for r in rows if r[-2])
    print(f"wrote {args.output}: {len(rows)} students, {flagged} with items for teacher review")
    print("weakest criteria (class average as a share of the maximum):")
    for ratio, c in sorted(ratios, key=lambda t: t[0])[:3]:
        print(f"  {c.get('label', c['id'])}: {ratio:.2f}")
    batches = {}
    for b, _, r in stats:
        if b is not None:
            batches.setdefault(b, []).append(r)
    if len(batches) > 1:
        print("mean share of maximum per batch (a steady drift up or down suggests the standard moved):")
        for b in sorted(batches):
            print(f"  batch {b}: {sum(batches[b]) / len(batches[b]):.2f} (n={len(batches[b])})")
    for w in warnings:
        print("warning: " + w)
    pairs = [(wds, r) for _, wds, r in stats if wds is not None]
    corr = None
    if pairs and len(pairs) < MIN_FOR_CORRELATION:
        print(f"length vs score: too few answers to judge ({len(pairs)} with word counts, "
              f"need {MIN_FOR_CORRELATION})")
    elif pairs:
        corr = pearson([p[0] for p in pairs], [p[1] for p in pairs])
    if corr is not None:
        print(f"length vs score correlation: {corr:.2f} over {len(pairs)} answers")
        if abs(corr) >= 0.5:
            print("  strong link between length and score: re-check whether length is being rewarded")
    print("DRAFT: every grade is a suggestion until the teacher approves its row")


if __name__ == "__main__":
    main()
