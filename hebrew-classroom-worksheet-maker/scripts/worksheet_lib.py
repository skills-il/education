#!/usr/bin/env python3
"""Shared helpers for the worksheet builder and checker. Standard library only, no network."""

import json
import os
import re
import sys
import unicodedata
from fractions import Fraction

LETTERS = set(chr(c) for c in range(0x05D0, 0x05EB))
FINAL_TO_BASE = {"ך": "כ", "ם": "מ", "ן": "נ", "ף": "פ", "ץ": "צ"}
DAGESH = "ּ"
SHEVA = "ְ"
HATAF_SEGOL = "ֱ"
HATAF_PATAH = "ֲ"
HATAF_QAMATS = "ֳ"
HIRIQ = "ִ"
TSERE = "ֵ"
SEGOL = "ֶ"
PATAH = "ַ"
QAMATS = "ָ"
HOLAM = "ֹ"
QUBUTS = "ֻ"
QATAN = "ׇ"
SHIN_DOT = "ׁ"
SIN_DOT = "ׂ"
VOWELS = set(chr(c) for c in range(0x05B0, 0x05BC)) | {QATAN}
POINTS = VOWELS | {DAGESH, "ֽ", "ֿ", SHIN_DOT, SIN_DOT}
WORD_RX = r"[֑-ׇֽֿׁׂׅׄא-ת]+"
VOWEL_NAMES = {
    "kamatz": QAMATS, "patah": PATAH, "hiriq": HIRIQ, "tsere": TSERE, "segol": SEGOL,
    "holam": HOLAM, "kubutz": QUBUTS, "sheva": SHEVA, "hataf-patah": HATAF_PATAH,
    "hataf-segol": HATAF_SEGOL, "hataf-kamatz": HATAF_QAMATS, "kamatz-katan": QATAN,
}
GRADES = ("gan", "1", "2", "3", "4", "5", "6")
MATH_GRADES = ("gan", "1", "2", "3")
_WORD_CHARS = "0-9A-Za-z\u0591-\u05BD\u05BF\u05C1\u05C2\u05C4\u05C5\u05C7\u05D0-\u05EA"
_SEPARATOR = rf"(?:[^{_WORD_CHARS}]|_)"
_OPERATORS = "+=×÷*/<>≤≥≠"
_DASHES = "\\-\u2010-\u2015\u2212\u05BE:"
MATH_IN_TEXT_RX = re.compile(
    rf"\d{_SEPARATOR}+\d|\d\s*[xX]\s*\d|[{_OPERATORS}]\s*[\d_]|[\d_]\s*[{_OPERATORS}]"
    rf"|_\s*[{_DASHES}]\s*\d|\d\s*[{_DASHES}]\s*_")
DIGIT_OR_OPERATOR_RX = re.compile(rf"\d|[{_OPERATORS}]")
BIDI_CONTROLS = dict.fromkeys(map(ord, "\u200e\u200f\u202a\u202b\u202c\u202d\u202e\u2066\u2067\u2068\u2069\u061c"), None)


def nfc(text):
    return unicodedata.normalize("NFC", text or "")


def _for_detection(text):
    return unicodedata.normalize("NFKC", str(text or "")).translate(BIDI_CONTROLS)


def has_math(text):
    """True for arithmetic, a comparison, or two numbers joined only by symbols or spaces.

    This also rejects clock times, dates and number ranges. Those print unreliably inside Hebrew.
    """
    return bool(MATH_IN_TEXT_RX.search(_for_detection(text)))


def has_digit_or_operator(text):
    return bool(DIGIT_OR_OPERATOR_RX.search(_for_detection(text)))


def printed_strings(data):
    """(where, text, is_story) for every string printed on the student or teacher page, except expr."""
    meta = data.get("meta", {})
    for field in ("title", "teacher_note", "niqqud_credit"):
        if meta.get(field):
            yield f"meta.{field}", str(meta[field]), False
    for section in data.get("sections", []):
        sid = section.get("id", "?")
        for field in ("title", "instruction"):
            if section.get(field):
                yield f"{sid}.{field}", str(section[field]), False
        for idx, line in enumerate(section.get("text", []) or []):
            yield f"{sid}.text[{idx}]", str(line), True
        for item in section.get("items", []) or []:
            iid = item.get("id", "?")
            for field in ("stem", "word", "prompt", "teacher_question", "rule"):
                if item.get(field):
                    yield f"{iid}.{field}", str(item[field]), False
            for option in item.get("options", []) or []:
                yield f"{iid}.option", str(option), False


def safe_path(base_dir, rel):
    """Resolve a path and refuse anything outside the worksheet folder."""
    base = os.path.realpath(base_dir)
    full = os.path.realpath(os.path.join(base, rel))
    if os.path.commonpath([base, full]) != base:
        sys.exit(f"ERROR: {rel} is outside the worksheet folder.")
    return full


def load_worksheet(path):
    try:
        with open(path, encoding="utf-8") as handle:
            data = json.load(handle)
    except (OSError, json.JSONDecodeError) as err:
        print(f"ERROR: cannot read {path}: {err}", file=sys.stderr)
        sys.exit(2)
    if not isinstance(data, dict) or not isinstance(data.get("meta"), dict) \
            or not isinstance(data.get("sections"), list):
        print("ERROR: the worksheet needs a meta object and a sections list.", file=sys.stderr)
        sys.exit(2)
    return data


def clusters(word):
    """Split a word into [letter, marks] pairs."""
    out = []
    for ch in nfc(word):
        if ch in LETTERS:
            out.append([ch, ""])
        elif ch in POINTS and out:
            out[-1][1] += ch
    return out


def hebrew_words(text):
    return [w for w in re.findall(WORD_RX, nfc(text)) if any(ch in LETTERS for ch in w)]


def letters_only(word):
    return "".join(ch for ch in nfc(word) if ch in LETTERS)


def is_pointed(word):
    return any(ch in VOWELS or ch in (DAGESH, SHIN_DOT, SIN_DOT) for ch in nfc(word))


def is_vowel_letter(cl, idx):
    """True for a vav or yod that only carries a vowel: shuruk, holam male, or yod after i or e."""
    letter, marks = cl[idx]
    vowels = [m for m in marks if m in VOWELS]
    if letter == "ו":
        return (DAGESH in marks and not vowels) or vowels == [HOLAM]
    if letter == "י" and not marks and idx > 0:
        return any(m in cl[idx - 1][1] for m in (HIRIQ, TSERE, SEGOL))
    return False


def word_vowels(word):
    """Vowel names in a word, with shuruk recognised on vav."""
    used = set()
    for letter, marks in clusters(word):
        vowels = [m for m in marks if m in VOWELS]
        if letter == "ו" and DAGESH in marks and not vowels:
            used.add("shuruk")
            continue
        for mark in vowels:
            used.update(name for name, value in VOWEL_NAMES.items() if value == mark)
    return used


def has_full_vowel(marks):
    return any(m in VOWELS and m != SHEVA for m in marks)


def follows_full_vowel(cl, idx):
    if idx == 0:
        return False
    letter, marks = cl[idx - 1]
    return has_full_vowel(marks) or is_vowel_letter(cl, idx - 1)


def unpointed_letters(word):
    """Letters inside a word that carry no vowel and are not excused.

    Excused: the last letter, a vowel letter, a letter right before a shuruk or holam male, a
    silent alef after a vowel (never a word-initial alef), and the silent yod of the suffix -av.
    """
    cl = clusters(word)
    missing = []
    for idx, (letter, marks) in enumerate(cl[:-1]):
        if any(m in VOWELS for m in marks) or is_vowel_letter(cl, idx):
            continue
        if letter == "א" and follows_full_vowel(cl, idx):
            continue
        if letter == "י" and not marks and idx == len(cl) - 2 and cl[-1][0] == "ו" and idx > 0 \
                and QAMATS in cl[idx - 1][1]:
            continue
        if cl[idx + 1][0] == "ו" and is_vowel_letter(cl, idx + 1):
            continue
        missing.append(letter)
    return missing


def _kept_gdt_dagesh(cl, idx):
    """A dagesh in gimel, dalet or tav that is not a doubling: not after a full vowel, or a final tav with sheva."""
    letter, marks = cl[idx]
    if letter not in "גדת":
        return False
    return not follows_full_vowel(cl, idx) or (idx == len(cl) - 1 and SHEVA in marks)


def grade1_form(word, keep_gdt=False):
    """Apply the grade 1 marks rule. It only removes marks.

    Remove every dagesh except in bet, kaf, pe and a shuruk. Remove the shin dot, except on a shin
    that also carries holam. The Ministry's outline names strong dagesh, mappiq and the shin dot.
    The rest is this skill's inference: the dagesh stays in bet, kaf and pe because it changes the
    sound there, goes from gimel, dalet and tav because it does not, and the dot stays with a holam
    so the holam is not read as a sin dot. With keep_gdt, for a class whose primer prints it,
    gimel, dalet and tav keep a dagesh unless it doubles the letter after a vowel. A final tav
    with sheva, as in the word for "you" (feminine), also keeps it.
    """
    cl = clusters(word)
    out = ""
    for idx, (letter, marks) in enumerate(cl):
        vowels = [m for m in marks if m in VOWELS]
        shuruk = letter == "ו" and not vowels
        kept_gdt = keep_gdt and _kept_gdt_dagesh(cl, idx)
        if DAGESH in marks and letter not in "בכפ" and not shuruk and not kept_gdt:
            marks = marks.replace(DAGESH, "")
        if HOLAM not in marks:
            marks = marks.replace(SHIN_DOT, "")
        out += letter + marks
    return nfc(out)


def gdt_forms(word):
    """(has a non-doubling dagesh in gimel, dalet or tav, lacks one where the standard form has it).

    Lacking it means at the start of a word, or after a closed syllable: a short vowel, then a
    letter with sheva. A few words have no dagesh there. List those in sight_words.
    """
    cl = clusters(word)
    present = any(DAGESH in m and _kept_gdt_dagesh(cl, i) for i, (_, m) in enumerate(cl))
    absent = False
    for idx, (letter, marks) in enumerate(cl):
        if letter not in "גדת" or DAGESH in marks:
            continue
        closed = idx >= 2 and SHEVA in cl[idx - 1][1] and any(v in cl[idx - 2][1] for v in (PATAH, HIRIQ, SEGOL, QUBUTS, QATAN))
        absent = absent or idx == 0 or closed
    return present, absent


def has_medial_bare_alef(word):
    cl = clusters(word)
    return any(letter == "א" and not marks for letter, marks in cl[1:-1])


QATAN_WORDS = {"כל", "צהריים", "צהרים", "צוהריים", "אזניים", "אזנים", "אוזניים", "אוזנים", "חכמה", "חוכמה",
               "תכנית", "תוכנית", "יפי", "יופי", "שרשים", "שורשים", "קרבן", "קורבן", "חפשי", "חופשי",
               "תכניות", "תוכניות"}
_PREFIX_LETTERS = "ובלשכהמ"


def _is_prefix_cluster(letter, marks):
    if letter not in _PREFIX_LETTERS or HOLAM in marks:
        return False
    return any(m in VOWELS for m in marks) or (letter == "ו" and DAGESH in marks)


def plain_qamats_qatan(word):
    """The listed word, if it is written with a plain qamats where a beginner would misread it."""
    cl = clusters(word)
    letters = "".join(c[0] for c in cl)
    for i in range(0, min(3, len(cl))):
        if letters[i:] in QATAN_WORDS and all(_is_prefix_cluster(c[0], c[1]) and not (c[0] == "מ" and TSERE in c[1]) for c in cl[:i]):
            return letters[i:] if QAMATS in cl[i][1] and QATAN not in cl[i][1] else None
    return None


def skeleton(word):
    """Pointed form without dagesh and shin or sin dots, used to tell homographs apart."""
    return nfc("".join(ch for ch in nfc(word) if ch not in (DAGESH, SHIN_DOT, SIN_DOT)))


class MathError(ValueError):
    pass


_INT = "(?:0|[1-9][0-9]*)"
_TERM = rf"(?:{_INT}|___)"
_BINARY_LEFT = re.compile(rf"({_TERM}) ([+\-×:]) ({_TERM}) = ({_TERM})")
_BINARY_RIGHT = re.compile(rf"({_TERM}) = ({_TERM}) ([+\-×:]) ({_TERM})")
_REMAINDER = re.compile(rf"({_INT}) : ({_INT}) = ({_TERM}) \+ \(({_TERM}) : ({_INT})\)")
_COMPARE = re.compile(rf"({_INT}) ___ ({_INT})")
GRAMMAR = "a + b = ___, ___ + b = c, a + ___ = c, c = a + ___ (with + - × :), a : b = ___ + (r : b), or a ___ b"


def _term(token):
    return None if token == "___" else int(token)


def parse_expr(expr):
    """Parse the one accepted grammar: plain integers, single spaces, exactly one ___ blank."""
    text = expr if isinstance(expr, str) else ""
    match = _COMPARE.fullmatch(text)
    if match:
        return {"kind": "compare", "a": int(match.group(1)), "b": int(match.group(2))}
    match = _REMAINDER.fullmatch(text)
    if match:
        a, b, q, r, b2 = int(match[1]), int(match[2]), _term(match[3]), _term(match[4]), int(match[5])
        if b != b2 or (q is None) == (r is None):
            raise MathError(f"use exactly one blank and one divisor. Accepted forms: {GRAMMAR}")
        return {"kind": "remainder", "a": a, "b": b, "q": q, "r": r}
    match = _BINARY_LEFT.fullmatch(text)
    if match:
        x, op, y, z = _term(match[1]), match[2], _term(match[3]), _term(match[4])
    else:
        match = _BINARY_RIGHT.fullmatch(text)
        if not match:
            raise MathError(f"not an accepted form. Accepted forms: {GRAMMAR}")
        z, x, op, y = _term(match[1]), _term(match[2]), match[3], _term(match[4])
    if [x, y, z].count(None) != 1:
        raise MathError(f"use exactly one ___ blank. Accepted forms: {GRAMMAR}")
    return {"kind": "binary", "x": x, "op": op, "y": y, "z": z}


def _exact(a, b):
    if b == 0:
        raise MathError("division by zero, or no single answer")
    if a % b:
        raise MathError("no whole-number answer. For a remainder use a : b = ___ + (r : b)")
    return a // b


def solve(parsed):
    """Return the one correct answer, or raise MathError."""
    kind = parsed["kind"]
    if kind == "compare":
        a, b = parsed["a"], parsed["b"]
        return "<" if a < b else ">" if a > b else "="
    if kind == "remainder":
        a, b = parsed["a"], parsed["b"]
        if b == 0:
            raise MathError("division by zero")
        right_q, right_r = divmod(a, b)
        if parsed["q"] not in (None, right_q) or parsed["r"] not in (None, right_r):
            raise MathError(f"correct is {a} : {b} = {right_q} + ({right_r} : {b})")
        return right_q if parsed["q"] is None else right_r
    x, op, y, z = parsed["x"], parsed["op"], parsed["y"], parsed["z"]
    if z is None:
        return x + y if op == "+" else x - y if op == "-" else x * y if op == "×" else _exact(x, y)
    if x is None:
        if op == "+":
            return z - y
        if op == "-":
            return z + y
        if y == 0:
            raise MathError("division by zero, or no single answer")
        return _exact(z, y) if op == "×" else z * y
    if op == "+":
        return z - x
    if op == "-":
        return x - z
    if op == "×":
        return _exact(z, x)
    result = _exact(x, z)
    if result == 0:
        raise MathError("division by zero")
    return result


def given_numbers(parsed):
    if parsed["kind"] == "compare":
        return [parsed["a"], parsed["b"]]
    if parsed["kind"] == "remainder":
        return [v for v in (parsed["a"], parsed["b"], parsed["q"], parsed["r"]) if v is not None]
    return [v for v in (parsed["x"], parsed["y"], parsed["z"]) if v is not None]


def counters_operands(expr):
    """Return (a, b) for the only expression that may carry counters: a + b = ___."""
    try:
        parsed = parse_expr(expr)
    except MathError:
        return None
    if parsed["kind"] == "binary" and parsed["op"] == "+" and parsed["z"] is None \
            and parsed["x"] is not None and parsed["y"] is not None and expr.endswith("= ___"):
        return parsed["x"], parsed["y"]
    return None


def checked_answer_problem(item):
    """Why this math item cannot be printed, or None."""
    try:
        right = solve(parse_expr(item.get("expr")))
    except MathError as err:
        return str(err)
    answer = item.get("answer")
    if isinstance(answer, bool) or answer != right or "answers" in item or "rule" in item:
        return "the answer is missing or wrong, or the item uses a removed field"
    return None


def iter_items(data):
    for section in data.get("sections", []):
        for item in section.get("items", []) or []:
            yield section, item
