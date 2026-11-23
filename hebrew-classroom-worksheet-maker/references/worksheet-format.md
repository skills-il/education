# Worksheet file format

One JSON file per version, in its own folder. The builder and the checker read the same file.

```json
{
  "meta": {
    "title": "חֲנֻכָּה",
    "grade": "1",
    "school_year": "תשפ\"ז",
    "allowed_letters": "אבלמרשתנד",
    "soft_letters": [],
    "sin_taught": false,
    "finals_taught": false,
    "gdt_dagesh": "drop",
    "allowed_vowels": ["kamatz", "patah", "hiriq"],
    "sight_words": [],
    "math_max": 10,
    "version_code": "",
    "sections_per_page": 3,
    "teacher_override": [],
    "niqqud_credit": "",
    "teacher_note": "Printed on the key page only. Never a student's name."
  },
  "sections": [
    {"id": "s0", "type": "read_aloud", "title": "סיפור להקראה", "text": ["..."]},
    {"id": "s1", "type": "reading", "title": "קִרְאוּ", "text": ["אַבָּא שָר."]},
    {"id": "s2", "type": "mc", "title": "הַקִיפוּ", "items": [
      {"id": "q1", "teacher_question": "מי הדליקה את הנר?", "options": ["אִמָא", "תָמָר"], "answer": "תָמָר"}]},
    {"id": "s3", "type": "first_letter", "title": "אוֹת רִאשוֹנָה", "items": [
      {"id": "f1", "letter": "נ", "picture_options": ["fish", "candle", "apple"], "answer": "candle"}]},
    {"id": "s4", "type": "math", "title": "פִּתְרוּ", "items": [
      {"id": "c1", "expr": "3 + 2 = ___", "answer": 5, "counters": [3, 2], "picture": "dreidel"},
      {"id": "c2", "expr": "10 = ___ + 4", "answer": 6},
      {"id": "c3", "expr": "8 - 3 = ___", "answer": 5}]}
  ]
}
```

## Fields

- `grade`: `gan`, `1` to `6`. Math sections are checked for `gan` to `3` only, and are an error above that.
- `allowed_letters`: required in grade 1. A bare ב, כ or פ means the **hard** sound (בּ כּ פּ). A bare ש means shin.
- `soft_letters`: the soft sounds learned, such as `["ב", "כ"]`.
- `sin_taught`, `finals_taught`: true only if the class learned them. Otherwise words with ש with a sin dot, or with final letters, are errors. You can also list single finals in `allowed_letters`, and a listed ך or ף counts as teaching that sound.
- `gdt_dagesh`: `drop` (the default rule) or `keep`, for a class whose primer prints the dagesh in ג ד ת. If it is not set and the sheet uses that dagesh consistently, you get a warning. Mixing both forms on one sheet is an error under every setting.
- `allowed_vowels`: kamatz, patah, hiriq, tsere, segol, holam, kubutz, shuruk, sheva, hataf-patah, hataf-segol, hataf-kamatz, kamatz-katan. A vav or yod that only carries a taught vowel does not need to be in the letter list.
- `sight_words`: words the teacher approved although they break the letter list.
- `math_max`: the highest number this class works with now. Required for gan math.
- `version_code`: a neutral shape: ● ■ ▲ ◆. Never a level, and not א ב ג, which read as a ranking.
- `teacher_override`: item ids of out-of-program exercises the teacher chose to keep. Their SCOPE error becomes a warning.
- `niqqud_credit`: a credit line printed on the key page, such as the Dicta credit.
- Section titles and instructions are read aloud in early grade 1, so the decodability check skips them. Their niqqud, gender and privacy checks still run.
- `source_text: true` with a required `source`: a verse or prayer in its original pointing. It skips the letter and grade 1 checks and always raises a warning.
- `quoted_work`: `{"title": "...", "creators": [{"role": "author", "death_year": 1900}]}`. It fails closed: every creator, including translators and co-authors, needs a death year, and all terms must have expired. Even then it is only a warning to confirm. The checker recognizes only a few known texts and **does not clear a text's copyright**.
- Optional top-level `key`: `[{"ref": "c1", "answer": 5}]` is a cross-check only. The printed key is always generated from the items.

## Section types

- `read_aloud`: a passage for the adult. Printed on the teacher page only, and not checked for decodability.
- `reading`: text the child reads.
- `mc`: `stem` is optional. `teacher_question` is printed in the key table, for a question the adult reads aloud. The stem, question and options cannot contain digits or operators. Arithmetic goes in a `math` section. A question that poses arithmetic in number words must be moved there by hand, since no check detects number words.
- `match`: `word` to `picture`. The word must be pointed and match the picture's pointed name.
- `first_letter`: `{"id", "letter", "picture_options": [...], "answer"}`. Exactly one picture must start with the letter.
- `math`: `expr`, `answer`, and optional `prompt` for a word problem. **One accepted grammar:** plain whole numbers (no commas, no leading zeros), single spaces, exactly one `___` blank. The forms are `a + b = ___`, `___ + b = c`, `a + ___ = c`, `c = a + ___`, `c = ___ + b`, `___ = a + b` (also with -, × and :), the remainder forms `a : b = ___ + (r : b)` and `a : b = q + (___ : b)`, and, from grade 2, the comparison `a ___ b` with answer `<`, `>` or `=`. Gan and grade 1 reject it as out of program. Complete equations, two blanks, chained operators, other blank styles, `answers` and `rule` are errors.
- A `prompt` writes its numbers as digits, which must match the exercise, and needs `prompt_read: true`, set only after someone read it against the exercise. The checker compares digits only, cannot judge the operation, and always warns. The key page prints a reminder.
- **Arithmetic or a comparison in any other printed field is an error**, including titles, notes and the read-aloud text. So are clock times, dates, number ranges, and two numbers joined only by symbols or spaces. Write those in words.
- Counters only for `a + b = ___`, matching the numbers, up to 10 in total.

Not built: exercises with several answers, number lines, vertical arithmetic, tracing or copying, free-writing lines. Write these by hand on the manual route, or leave them out.

## Pictures

`dreidel` (סְבִיבוֹן), `candle` (נֵר), `apple` (תַּפּוּחַ), `fish` (דָּג), `house` (בַּיִת), `sun` (שֶׁמֶשׁ), `tree` (עֵץ), `book` (סֵפֶר).

The set is small on purpose, and has no holiday-specific objects beyond the dreidel and candle. The name list cannot prove how a child will name a drawing, so look at each one. If a word has no clear picture, change the task.

## Check codes

| Code | Meaning |
|---|---|
| INTAKE | Grade, letters or vowels missing |
| LETTER, VOWEL | Outside what this class learned, including final letters, soft sounds and sin |
| G1_PROFILE, G1_GDT, G2_MATRES, UNPOINTED, ALEF, QATAN | Grade 1 to 3 niqqud rules. ALEF is a warning to confirm that a medial alef with no vowel is silent. QATAN flags a plain qamats on a listed word: an error for כל, a warning for the others |
| MATH_WRONG, MATH_PARSE | Recomputed answer differs or none exists, or not in the accepted grammar |
| MATH_OUTSIDE, MATH_GRADE | Arithmetic, comparison, time, date or range outside a math section, or math above grade 3 |
| NEGATIVE, NOTATION, SCOPE | Negative numbers, ÷ or old remainder form, above the grade or class range |
| COUNTERS | Counters that do not match or do not fit |
| KG_WRITING | Tracing or copying section |
| MC_ONE, MC_NUMERIC | Not exactly one correct option, or digits or operators in a multiple-choice item |
| WORD_PROBLEM | Digits missing or different from the exercise, or the question was not confirmed as read |
| KEY_ORPHAN, KEY_MISSING, KEY_WRONG, STALE | Key, student page and JSON disagree |
| PICTURE | Unknown picture, or a different word |
| PII | Identifier, roster, or a level or need label in any printed field except story text. It cannot recognize a person's name |
| EMOJI, PRINT, BIDI | Print safety and left-to-right math in the built page |
| COPYRIGHT, SOURCE | A few known protected texts, a work not confirmed as expired, or a source text with no source |
| GENDER | Singular or slash address in instructions |
