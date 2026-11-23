#!/usr/bin/env python3
"""Check and adapt vocalized (menukad) Hebrew story text for a children's book.

No network access and no external packages. Two subcommands:

  check  Compare the vocalized text with the plain text you sent to the vocalizer
         and list every word the parent should look at: words whose letters
         changed, words left without niqqud, the child's name, second-person
         forms that do not match the child's gender, and malformed marks.

  adapt  Apply a reading-stage profile from the Ministry of Education guideline
         for vocalizing primary-school texts:
           grade1  drop the strong dagesh (kept in bet, kaf and pe, where it changes
                   the sound), drop the mappiq, drop the shin dot (kept on a shin
                   that carries holam, so it cannot be read as sin)
           grade2  keep the vowel letters (matres lectionis) next to the niqqud
           full    standard niqqud (default model output)

  inventory  For a child who reads alone: list words that use letters or vowel
             signs the child has not learned yet, long words, and qamats qatan.

Examples:
  python3 niqqud_tools.py check --plain story.txt --vocalized story_menukad.txt \\
      --gender f --name "נועה"
  python3 niqqud_tools.py adapt --stage grade1 --in story_menukad.txt --out story_grade1.txt
  python3 niqqud_tools.py inventory --in story_grade1.txt --letters "אבגדהוזחטילמנסעפצקרשת" \
      --vowels kamatz,patah,hiriq,holam,shuruk --max-syllables 3

Input files are UTF-8 text, one page per paragraph (blank line between pages).
"""

import argparse
import difflib
import re
import sys
import unicodedata

LETTERS = set(chr(c) for c in range(0x05D0, 0x05EB))
BGDKPT = set("בגדכךפףת")
SOUND_DAGESH = set("בכךפף")  # dagesh changes the sound only in these (b/v, k/kh, p/f)
FINAL_FORMS = set("ךםןףץ")
DAGESH = "ּ"
SHEVA = "ְ"
QAMATS = "ָ"
PATAH = "ַ"
HIRIQ = "ִ"
SHIN_DOT = "ׁ"
HOLAM = "\u05B9"
QUBUTS = "\u05BB"
QATAN = "\u05C7"
SIN_DOT = "ׂ"
VOWELS = set(chr(c) for c in range(0x05B0, 0x05BC)) | {"ׇ"}
POINTS = VOWELS | {DAGESH, "ֽ", "ֿ", SHIN_DOT, SIN_DOT}
CANTILLATION = set(chr(c) for c in range(0x0591, 0x05B0))
MATRES_MARK = "*"  # the Dicta model marks kept vowel letters with '*' when asked
PREFIXES = "ובלשכהמ"
WORD_RX = r"[\u0591-\u05BD\u05BF\u05C1\u05C2\u05C4\u05C5\u05C7\u05D0-\u05EA*]+"  # no maqaf, paseq, sof pasuq

# Feminine second-person singular forms (after one-letter prefixes are removed).
FEM_WORDS = {"לָךְ", "בָּךְ", "שֶׁלָּךְ", "אוֹתָךְ", "אִתָּךְ", "עִמָּךְ", "מִמֵּךְ", "אַתְּ", "בִּשְׁבִילֵךְ",
             "שְׁמֵךְ", "אִמֵּךְ", "עַצְמֵךְ", "כָּמוֹךְ", "אֶצְלֵךְ", "לְבַדֵּךְ", "אָבִיךְ", "אָחִיךְ",
             "אֲחוֹתֵךְ", "חֲבֵרָתֵךְ", "בֵּיתֵךְ", "חַדְרֵךְ", "רָאִית", "עָשִׂית", "קָנִית", "בָּנִית",
             "שָׁתִית", "הָיִית", "רָצִית", "בָּכִית", "מָצָאת", "בָּאת", "קָרָאת", "יָצָאת", "נִסִּית",
             "חִכִּית", "עָלִית", "שָׂחִית", "קַמְתְּ", "שַׂמְתְּ", "רַצְתְּ"}
MASC_WORDS = {"אַתָּה"}
# Imperatives match only bare or after ו: with ל/ב/מ they are other words (לָקוּם, בָּרְאִי).
FEM_IMPERATIVES = {"לְכִי", "בּוֹאִי", "רְאִי", "שְׁבִי", "קוּמִי", "תִּרְאִי"}
MASC_IMPERATIVES = {"לֵךְ", "בּוֹא", "רְאֵה", "שֵׁב", "קוּם"}
NOT_SECOND_PERSON = {"כָּךְ"}  # "kakh" (so, like this) ends like a feminine suffix
# Unvocalized, these letters can be "you" for either gender: list them for reading aloud.
NOT_AMBIGUOUS = {"כך", "דרך", "מלך", "חושך", "חשך", "תוך", "איך", "ארוך", "ארך", "צריך", "הולך", "ילך",
                 "תלך", "נלך", "אלך", "הלך", "ברוך", "מחייך", "מברך", "חייך", "סמוך", "רך", "פך", "ענק"}


def nfc(s):
    return unicodedata.normalize("NFC", s)


FEM_WORDS = {nfc(w) for w in FEM_WORDS}
MASC_WORDS = {nfc(w) for w in MASC_WORDS}
FEM_IMPERATIVES = {nfc(w) for w in FEM_IMPERATIVES}
MASC_IMPERATIVES = {nfc(w) for w in MASC_IMPERATIVES}
# Words a beginner misreads when the vocalizer writes a plain qamats for a qamats qatan.
QATAN_WORDS = {"כל", "צהריים", "צהרים", "צוהריים", "אזניים", "אזנים", "אוזניים", "אוזנים", "חכמה", "חוכמה",
               "תכנית", "תוכנית", "יפי", "יופי", "שרשים", "שורשים", "קרבן", "קורבן", "חפשי", "חופשי",
               "תכניות", "תוכניות"}
NOT_SECOND_PERSON = {nfc(w) for w in NOT_SECOND_PERSON}


def letters_only(word):
    """Base letters of a word: marks, cantillation and '*' removed."""
    return "".join(ch for ch in word if ch in LETTERS)


def clusters(word):
    """Split a word into (letter, marks) pairs. Marks before any letter are orphans."""
    out, orphans = [], []
    for ch in word:
        if ch in LETTERS:
            out.append([ch, ""])
        elif ch in POINTS or ch in CANTILLATION:
            if out:
                out[-1][1] += ch
            else:
                orphans.append(ch)
        elif ch == MATRES_MARK and out:
            out[-1][1] += ch
    return out, orphans


def hebrew_words(text):
    return [w for w in re.findall(WORD_RX, text) if any(ch in LETTERS for ch in w)]


def is_vocalized(word):
    return any(ch in VOWELS or ch in (DAGESH, SHIN_DOT, SIN_DOT) for ch in word)


def is_prefix_cluster(letter, marks):
    """A one-letter prefix (ו ב ל ש כ ה מ) always carries a vowel; וּ counts. A bare letter
    or a holam vav (the וֹ of הוֹלֵךְ) is part of the word, not a prefix."""
    if letter not in PREFIXES or HOLAM in marks:
        return False
    return any(m in VOWELS for m in marks) or (letter == "ו" and DAGESH in marks)


def strip_prefixes(word):
    """Yield the word and versions with leading one-letter prefixes removed."""
    yield word
    cl, _ = clusters(word)
    for i in range(1, min(3, len(cl))):
        if all(is_prefix_cluster(c[0], c[1]) for c in cl[:i]):
            yield "".join(c[0] + c[1] for c in cl[i:])


def skeleton(word):
    """Comparison form that survives the grade 1 profile and website spelling: dagesh, mappiq,
    shin and sin dots removed, and a bare yod or vav inside the word (a vowel letter the website
    kept, as in נִיסִּית) dropped. The word lists go through the same function."""
    cl, _ = clusters(nfc(word.replace(MATRES_MARK, "")))
    out = []
    for i, (letter, marks) in enumerate(cl):
        if letter in "וי" and not marks and 0 < i < len(cl) - 1:
            continue
        out.append(letter + "".join(m for m in marks if m not in (DAGESH, SHIN_DOT, SIN_DOT)))
    return nfc("".join(out))


SK_FEM = {skeleton(w) for w in FEM_WORDS}
SK_MASC = {skeleton(w) for w in MASC_WORDS}
SK_FEM_IMP = {skeleton(w) for w in FEM_IMPERATIVES}
SK_MASC_IMP = {skeleton(w) for w in MASC_IMPERATIVES}
SK_NOT = {skeleton(w) for w in NOT_SECOND_PERSON}


def second_person_gender(word):
    """Return 'm', 'f', 'u' (mixed, undecidable) or None for a vocalized word."""
    w = nfc(word.replace(MATRES_MARK, ""))
    for k, core in enumerate(strip_prefixes(w)):
        sk = skeleton(core)
        if sk in SK_NOT:
            return None
        if sk in SK_FEM:
            return "f"
        if sk in SK_MASC:
            return "m"
        bare_or_vav = k == 0 or letters_only(w)[0] == "ו" and len(letters_only(w)) - len(letters_only(core)) == 1
        if bare_or_vav and sk in SK_FEM_IMP:
            return "f"
        if bare_or_vav and sk in SK_MASC_IMP:
            return "m"
    cl, _ = clusters(w)
    if not cl:
        return None
    last_letter, last_marks = cl[-1]
    if last_letter == "ך":
        if QAMATS in last_marks:
            return "m"  # -kha: לְךָ, שֶׁלְּךָ, אוֹתְךָ, אֵלֶיךָ
        if len(cl) >= 3 and cl[-2][0] == "י" and HIRIQ in cl[-2][1] and PATAH in cl[-3][1]:
            return "f"  # -ayikh: אֵלַיִךְ, עָלַיִךְ
        if len(cl) >= 2 and SHEVA in last_marks and SHEVA in cl[-2][1]:
            return "u"  # לְךְ, שֶׁלְּךְ: neither לְךָ nor לָךְ, the vocalizer could not decide
    if last_letter == "ת" and len(cl) >= 2:
        if QAMATS in last_marks:
            return "m"  # past tense -ta: הִצְלַחְתָּ, רָאִיתָ
        if SHEVA in last_marks:
            return "f"  # past tense -t: הִצְלַחְתְּ, אַתְּ
    return None


def ambiguous_plain(plain_letters):
    """Unvocalized word that could be "you"/"your" of either gender: ending in ך, or a
    past-tense form ending in את / ית (מצאת, ראית, הבאת), which a vocalizer may leave unmarked.
    At most one prefix letter is set aside, so בשבילך is never cut down to ילך."""
    cores = [plain_letters]
    if len(plain_letters) > 3 and plain_letters[0] in PREFIXES:
        cores.append(plain_letters[1:])
    if plain_letters.endswith(("את", "ית")):
        return not any(c in ("את", "ואת") for c in cores) and len(plain_letters) >= 3
    if not plain_letters.endswith("ך"):
        return False
    return not any(c in NOT_AMBIGUOUS for c in cores)


def is_qatan_candidate(cl):
    """A known qamats-qatan word (כל, חכמה...) written with a plain qamats."""
    letters = "".join(c[0] for c in cl)
    for i in range(0, min(3, len(cl))):
        if letters[i:] in QATAN_WORDS and all(is_prefix_cluster(c[0], c[1]) for c in cl[:i]):
            return QAMATS in cl[i][1] and "\u05C7" not in cl[i][1]
    return False


def is_name(plain_letters, name_letters):
    """The plain word is the name, optionally with one or two prefix letters (ו, ל, ש...)."""
    for n in name_letters:
        if not n or not plain_letters.endswith(n):
            continue
        head = plain_letters[: len(plain_letters) - len(n)]
        if len(head) <= 2 and all(c in PREFIXES for c in head):
            return True
    return False


def read_pages(path):
    with open(path, encoding="utf-8") as f:
        text = nfc(f.read())
    return [p.strip() for p in re.split(r"\n\s*\n", text) if p.strip()]


def matres_only_change(plain_letters, voc_letters):
    """True when the vocalized word equals the plain word minus some vav/yod letters."""
    if len(voc_letters) >= len(plain_letters):
        return False
    it = iter(plain_letters)
    removed = []
    for ch in voc_letters:
        for p in it:
            if p == ch:
                break
            removed.append(p)
        else:
            return False
    removed.extend(it)
    return all(r in "וי" for r in removed)


def cmd_check(args):
    plain_pages = read_pages(args.plain)
    voc_pages = read_pages(args.vocalized)
    name_letters = {letters_only(nfc(n)) for n in (args.name or [])}
    report = {"changed": [], "matres": [], "unvocalized": [], "names": [], "gender": [],
              "second_person": [], "malformed": [], "no_shin_dot": [], "ambiguous": [], "qatan": []}
    if len(plain_pages) != len(voc_pages):
        print(f"WARNING: {len(plain_pages)} pages in the plain text, {len(voc_pages)} in the "
              "vocalized text. Compare page by page by hand.", file=sys.stderr)

    for pno, (ptxt, vtxt) in enumerate(zip(plain_pages, voc_pages), start=1):
        pw, vw = hebrew_words(ptxt), hebrew_words(vtxt)
        pl = [letters_only(w) for w in pw]
        vl_full = [letters_only(w) for w in vw]
        sm = difflib.SequenceMatcher(a=pl, b=[letters_only(w.replace(MATRES_MARK, "")) for w in vw],
                                     autojunk=False)
        aligned = []
        for tag, i1, i2, j1, j2 in sm.get_opcodes():
            pairs = list(zip(range(i1, i2), range(j1, j2)))
            aligned.extend(pairs)
            if tag == "equal":
                continue
            for i, j in pairs:
                if matres_only_change(pl[i], vl_full[j]):
                    report["matres"].append((pno, pw[i], vw[j]))
                else:
                    report["changed"].append((pno, pw[i], vw[j]))
            for i in range(i1 + len(pairs), i2):
                report["changed"].append((pno, pw[i], "(missing)"))
            for j in range(j1 + len(pairs), j2):
                report["changed"].append((pno, "(added)", vw[j]))

        for i, j in aligned:
            if is_name(pl[i], name_letters):
                report["names"].append((pno, pw[i], vw[j]))
            if ambiguous_plain(pl[i]) and not second_person_gender(vw[j].replace(MATRES_MARK, "")):
                report["ambiguous"].append((pno, vw[j]))

        for w in vw:
            core = w.replace(MATRES_MARK, "")
            cl, orphans = clusters(core)
            if orphans:
                report["malformed"].append((pno, w, "mark with no letter before it"))
            for k, (letter, marks) in enumerate(cl):
                vowels = [m for m in marks if m in VOWELS]
                if len(vowels) > 1:
                    report["malformed"].append((pno, w, f"two vowels on {letter}"))
                if (letter == "ו" and not marks and 0 < k < len(cl) - 1 and cl[k + 1][0] != "ו"
                        and cl[k - 1][0] != "ו" and any(m in VOWELS and m != SHEVA for m in cl[k - 1][1])):
                    report["malformed"].append((pno, w, "bare vav beside a vowel (as in נֹועָה, יָופִי, אׇוזְנַיִם); "
                                                        "run adapt, it writes נוֹעָה / יוֹפִי / אוֹזְנַיִם"))
                if letter == "ש" and is_vocalized(core) and SHIN_DOT not in marks and SIN_DOT not in marks:
                    report["no_shin_dot"].append((pno, w))
            if len(letters_only(core)) >= 2 and not is_vocalized(core):
                report["unvocalized"].append((pno, w))
            if is_qatan_candidate(cl):
                report["qatan"].append((pno, w))
            g = second_person_gender(core)
            if g:
                report["second_person"].append((pno, w, g))
                if g == "u" or (args.gender and g != args.gender):
                    report["gender"].append((pno, w, g))

    def section(title, rows, fmt):
        print(f"\n## {title} ({len(rows)})")
        for r in rows:
            print("- " + fmt(r))

    print("# Niqqud check report")
    section("CHANGED: letters differ from what you sent, check the word", report["changed"],
            lambda r: f"page {r[0]}: sent {r[1]} , got {r[2]}")
    section("GENDER: second-person form that does not match the child (or speaks to someone else: check who)", report["gender"],
            lambda r: f"page {r[0]}: {r[1]} reads as " + {"m": "masculine", "f": "feminine",
                                                             "u": "neither (mixed vowels), fix by hand"}[r[2]])
    section("NAME: confirm the child's name is vocalized and spelled the way you say it", report["names"],
            lambda r: f"page {r[0]}: sent {r[1]} , got {r[2]}")
    section("UNVOCALIZED: word came back without niqqud", report["unvocalized"],
            lambda r: f"page {r[0]}: {r[1]}")
    section("MALFORMED marks", report["malformed"], lambda r: f"page {r[0]}: {r[1]} ({r[2]})")
    section("SHIN WITHOUT DOT (fine for a grade 1 profile, otherwise check)", report["no_shin_dot"],
            lambda r: f"page {r[0]}: {r[1]}")
    section("QAMATS QATAN written as a plain qamats (a beginner reads 'a', the word says 'o'): "
            "use ׇ or another word in a first reader", report["qatan"], lambda r: f"page {r[0]}: {r[1]}")
    section("VOWEL LETTERS REMOVED (vav/yod dropped, normal for standard niqqud)", report["matres"],
            lambda r: f"page {r[0]}: {r[1]} , {r[2]}")
    section("All second-person forms found (read each one aloud)", report["second_person"],
            lambda r: f"page {r[0]}: {r[1]} ({r[2]})")
    section("COULD BE 'YOU' (ends in ך, את or ית; gender not visible to this script): read aloud", report["ambiguous"],
            lambda r: f"page {r[0]}: {r[1]}")
    blocking = len(report["changed"]) + len(report["gender"]) + len(report["malformed"])
    print(f"\nSUMMARY: {blocking} item(s) to fix, {len(report['names'])} name occurrence(s) to confirm.")
    return 1 if blocking else 0


def follows_full_vowel(cl, idx):
    """True when the letter before idx carries a full vowel: a vowel sign other than sheva,
    a shuruk, a holam male, or a bare vowel letter (yod/vav) after a vowel (תּוּתִּים, כִּיתָּה)."""
    j = idx - 1
    while j >= 0 and MATRES_MARK in cl[j][1]:
        j -= 1  # a starred vowel letter is dropped: look at the letter before it
    if j < 0:
        return False
    letter, marks = cl[j]
    if any(m in VOWELS and m != SHEVA for m in marks):
        return True
    if letter == "ו" and DAGESH in marks:
        return True
    if letter in "וי" and not marks and j > 0:
        return any(m in VOWELS and m != SHEVA for m in cl[j - 1][1])
    return False


def adapt_word(word, stage):
    cl, orphans = clusters(word)
    out = "".join(orphans)
    if stage == "grade2":
        # Keep the vowel letters the model marked with '*', and move the vowel onto
        # them: holam + vav* becomes holam male (נוֹעָה), qubuts + vav* becomes
        # shuruk (בּוּבָּה), as in the Ministry's grade 2 examples.
        for i, (letter, marks) in enumerate(cl):
            if MATRES_MARK not in marks:
                continue
            if i > 0 and cl[i - 1][0] == letter:
                continue  # doubled consonant yod/vav of unvocalized spelling (שמיים): drop it below
            cl[i][1] = marks.replace(MATRES_MARK, "")
            if letter == "ו" and i > 0:
                prev = cl[i - 1][1]
                o = next((m for m in (HOLAM, QATAN) if m in prev), None)
                if o:  # holam or qamats qatan + vav*: holam male (נוֹעָה, אוֹזְנַיִם)
                    cl[i - 1][1] = prev.replace(o, "")
                    cl[i][1] += HOLAM
                elif QUBUTS in prev:
                    cl[i - 1][1] = prev.replace(QUBUTS, "")
                    cl[i][1] += DAGESH
    # The Nakdan website keeps the vowel letters you typed but leaves them bare beside the
    # vowel (נֹועָה, הַבֻּובָּה). In every profile, move the vowel onto the vav.
    # A bare vav inside the word after a qamats (qatan or plain) is the "o" of a word like
    # יופי or אוזניים: the website writes אָוזְנַיִם, which a beginner reads "avznayim".
    for i, (letter, marks) in enumerate(cl):
        if letter == "ו" and not marks and i > 0:
            if cl[i - 1][0] == "ו" or (i + 1 < len(cl) and cl[i + 1][0] == "ו"):
                continue  # doubled consonant vav of full spelling (צוואר, אווז, מצווה): not a vowel letter
            prev = cl[i - 1][1]
            medial = i < len(cl) - 1
            o = (next((m for m in (HOLAM, QATAN, "\u05B3") if m in prev), None)
                 or (QAMATS if medial and QAMATS in prev else None))
            if o:
                cl[i - 1][1] = prev.replace(o, "")
                cl[i][1] = HOLAM
            elif QUBUTS in prev:
                cl[i - 1][1] = prev.replace(QUBUTS, "")
                cl[i][1] = DAGESH
    for idx, (letter, marks) in enumerate(cl):
        if MATRES_MARK in marks:
            continue  # standard niqqud: drop the vowel letter the model marked
        if stage == "grade1":
            vowels = [m for m in marks if m in VOWELS]
            is_last = idx == len(cl) - 1
            if DAGESH in marks:
                shuruk = letter == "ו" and not vowels
                mappiq = letter == "ה" and is_last
                # In gimel, dalet and tav the dagesh no longer changes the sound; drop it
                # where it is strong (after a full vowel inside the word), keep it word-initially.
                prev_full_vowel = follows_full_vowel(cl, idx)
                strong_gdt = letter in "גדת" and prev_full_vowel
                if mappiq or strong_gdt or (letter not in BGDKPT and not shuruk):
                    marks = marks.replace(DAGESH, "")
            if HOLAM not in marks:
                marks = marks.replace(SHIN_DOT, "")  # שֹׁ keeps its dot, or the holam reads as a sin dot
        out += letter + marks
    return out


def restore_vowel_letters(plain_word_letters, voc_word):
    """Put back the vav / yod the parent typed that the vocalizer dropped (נֹעָה + נועה ->
    נֹועָה, which adapt then writes as נוֹעָה). Only vav and yod are restored."""
    cl, orphans = clusters(voc_word)
    out, i = [], 0
    for letter, marks in cl:
        while i < len(plain_word_letters) and plain_word_letters[i] != letter and plain_word_letters[i] in "וי":
            if not (out and out[-1][0] == plain_word_letters[i]):  # doubled consonant (שמיים): not a vowel letter
                out.append([plain_word_letters[i], ""])
            i += 1
        out.append([letter, marks])
        if i < len(plain_word_letters) and plain_word_letters[i] == letter:
            i += 1
    return "".join(orphans) + "".join(l + m for l, m in out)


def restore_from_plain(text, plain_text):
    """Page by page, align vocalized words with the parent's words and restore dropped
    vowel letters in words whose only change is a missing vav / yod."""
    voc_parts = re.split(r"(\n\s*\n)", text)
    plain_pages = [p for p in re.split(r"\n\s*\n", nfc(plain_text)) if p.strip()]
    page = 0
    for k, part in enumerate(voc_parts):
        if not part.strip() or re.fullmatch(r"\n\s*\n", part):
            continue
        if page >= len(plain_pages):
            break
        pw = [letters_only(w) for w in hebrew_words(plain_pages[page])]
        matches = list(re.finditer(WORD_RX, part))
        vw = [m.group(0) for m in matches]
        key = lambda x: x.replace("ו", "").replace("י", "")
        sm = difflib.SequenceMatcher(a=[key(x) for x in pw],
                                     b=[key(letters_only(w.replace(MATRES_MARK, ""))) for w in vw], autojunk=False)
        repl = {}
        for tag, i1, i2, j1, j2 in sm.get_opcodes():
            if tag != "equal":
                continue
            for i, j in zip(range(i1, i2), range(j1, j2)):
                vl = letters_only(vw[j].replace(MATRES_MARK, ""))
                if MATRES_MARK not in vw[j] and matres_only_change(pw[i], vl):
                    repl[j] = restore_vowel_letters(pw[i], vw[j])
        out, last = [], 0
        for j, m in enumerate(matches):
            out.append(part[last:m.start()])
            out.append(repl.get(j, m.group(0)))
            last = m.end()
        out.append(part[last:])
        voc_parts[k] = "".join(out)
        page += 1
    return "".join(voc_parts)


def cmd_adapt(args):
    with open(args.inp, encoding="utf-8") as f:
        text = nfc(f.read())
    if args.plain:
        if args.stage != "grade2":
            sys.exit("ERROR: --plain restores vowel letters for the grade2 profile only.")
        with open(args.plain, encoding="utf-8") as f:
            text = nfc(restore_from_plain(text, f.read()))
    result = re.sub(WORD_RX, lambda m: adapt_word(m.group(0), args.stage), text)
    result = nfc(result)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(result)
        print(f"wrote {args.out} (stage {args.stage})")
    else:
        sys.stdout.write(result)
    return 0



VOWEL_NAMES = {
    "kamatz": "\u05B8", "patah": "\u05B7", "hiriq": "\u05B4", "tsere": "\u05B5", "segol": "\u05B6",
    "holam": "\u05B9", "kubutz": "\u05BB", "sheva": "\u05B0", "hataf-patah": "\u05B2",
    "hataf-segol": "\u05B1", "hataf-kamatz": "\u05B3", "kamatz-katan": "\u05C7",
}
FINAL_TO_BASE = {"ך": "כ", "ם": "מ", "ן": "נ", "ף": "פ", "ץ": "צ"}


def word_vowels(cl):
    """Vowel names used in a word, with shuruk and holam male recognised on vav."""
    used = set()
    for letter, marks in cl:
        vowels = [m for m in marks if m in VOWELS]
        if letter == "ו" and DAGESH in marks and not vowels:
            used.add("shuruk")
            continue
        for m in vowels:
            used.update(k for k, v in VOWEL_NAMES.items() if v == m)
    return used


def letter_tokens(spec):
    """Parse --letters: plain letters, or letters with a dagesh / shin dot / sin dot when the child
    learned the two sounds separately (בּ and ב, כּ and כ, פּ and פ, שׁ and שׂ)."""
    toks, cur = set(), ""
    for ch in nfc(spec or ""):
        if ch in LETTERS:
            if cur:
                toks.add(cur)
            cur = ch
        elif ch in (DAGESH, SHIN_DOT, SIN_DOT) and cur:
            cur += ch
    if cur:
        toks.add(cur)
    return toks


def letter_known(letter, marks, toks, strict_finals):
    base = letter if strict_finals else FINAL_TO_BASE.get(letter, letter)
    variants = {t for t in toks if t[0] == base and len(t) > 1}
    if letter == "ש" and variants:
        # a dotless ש is a shin (the grade 1 profile drops the shin dot, never the sin dot)
        dot = SIN_DOT if SIN_DOT in marks else SHIN_DOT
        return (base + dot) in toks
    if base in "בכפ" and variants:
        return (base + DAGESH in toks) if DAGESH in marks else base in toks
    return base in toks or any(t[0] == base for t in toks)


def cmd_inventory(args):
    toks = letter_tokens(args.letters)
    known_vowels = {v.strip() for v in (args.vowels or "").split(",") if v.strip()}
    unknown = [k for k in known_vowels if k not in VOWEL_NAMES and k != "shuruk"]
    if unknown:
        sys.exit(f"ERROR: unknown vowel name(s) {unknown}. Use: {', '.join(list(VOWEL_NAMES) + ['shuruk'])}")
    pages = read_pages(args.inp)
    sight = {letters_only(nfc(x.strip())) for x in (args.sight or "").split(",") if x.strip()}
    issues = 0
    print("# Reading inventory")
    for pno, text in enumerate(pages, start=1):
        rows = []
        for w in hebrew_words(text):
            cl, _ = clusters(w.replace(MATRES_MARK, ""))
            notes = []
            if is_name(letters_only(w), sight):
                continue
            if args.letters:
                bad = sorted({c[0] + "".join(m for m in c[1] if m in (DAGESH, SHIN_DOT, SIN_DOT) and c[0] in "בכפש")
                              for c in cl if not letter_known(c[0], c[1], toks, args.strict_finals)})
                if bad:
                    notes.append("letters not learned yet: " + " ".join(bad))
            if known_vowels:
                bad_v = sorted(word_vowels(cl) - known_vowels)
                if bad_v:
                    notes.append("vowels not learned yet: " + ", ".join(bad_v))
            if any("\u05C7" in c[1] for c in cl):
                notes.append("qamats qatan (read as o, a beginner reads a): swap the word or teach it")
            syll = sum(1 for c in cl if any(m in VOWELS and m != SHEVA for m in c[1])
                       or (c[0] == "ו" and DAGESH in c[1]))
            if syll > args.max_syllables:
                notes.append(f"{syll} syllables")
            if notes:
                rows.append(f"- {w}: " + "; ".join(notes))
        sentences = [x for x in re.split(r"[.!?]", text) if x.strip()]
        avg = sum(len(x.split()) for x in sentences) / max(1, len(sentences))
        print(f"\n## Page {pno} ({len(text.split())} words, {avg:.1f} words per sentence)")
        print("\n".join(rows) if rows else "- nothing to change")
        issues += len(rows)
    print(f"\nSUMMARY: {issues} word(s) to reconsider for a child reading alone.")
    return 1 if issues else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("check", help="word-by-word check of vocalized text")
    c.add_argument("--plain", required=True, help="the text you sent to the vocalizer")
    c.add_argument("--vocalized", required=True, help="the text that came back")
    c.add_argument("--gender", choices=["m", "f"], help="the child's grammatical gender")
    c.add_argument("--name", action="append", help="the child's first name (repeat for each named character)")
    a = sub.add_parser("adapt", help="apply a reading-stage profile")
    a.add_argument("--stage", required=True, choices=["grade1", "grade2", "full"])
    a.add_argument("--in", dest="inp", required=True)
    a.add_argument("--out")
    a.add_argument("--plain", help="grade2 only: the text you sent to the vocalizer; vowel letters (vav, yod) "
                   "it dropped are put back from it, so the model's default output can be used")
    v = sub.add_parser("inventory", help="decodability check for a child reading alone")
    v.add_argument("--in", dest="inp", required=True)
    v.add_argument("--letters", help="letters the child already reads, e.g. אבגדהו; write בּ / ב, כּ / כ, "
                   "פּ / פ, שׁ / שׂ separately when the child learned them as separate sounds")
    v.add_argument("--strict-finals", action="store_true", help="final forms count only if listed")
    v.add_argument("--vowels", help="vowel names the child knows: " + ", ".join(list(VOWEL_NAMES) + ["shuruk"]))
    v.add_argument("--max-syllables", type=int, default=3)
    v.add_argument("--sight", help="comma-separated words the parent approved as sight words (the "
                   "child's name, the theme word); they are not flagged")
    args = ap.parse_args()
    return {"check": cmd_check, "adapt": cmd_adapt, "inventory": cmd_inventory}[args.cmd](args)


if __name__ == "__main__":
    sys.exit(main())
