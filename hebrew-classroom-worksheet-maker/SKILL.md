---
name: hebrew-classroom-worksheet-maker
description: "Make a printable Hebrew worksheet for kindergarten and primary school, or a math sheet from kindergarten to grade 3: an A4 file ready to photocopy, with a separate answer key. Asks what the class has learned, writes only with the letters and vowels the children know, fits niqqud to the grade using published Ministry of Education guidance, and recomputes every answer before sending. Use when a teacher, ganenet or parent asks for a daf avoda, a Hebrew or math worksheet, a short ungraded practice quiz, a holiday sheet, or versions of a sheet for one class. Prevents untaught letters, wrong answers in the key, reversed math and content beyond the grade's program. Do NOT use for writing a personalized story book (use hebrew-kids-story-maker), treasure hunts (use hebrew-treasure-hunt-maker), grading student work (use hebrew-exam-grader), graded or formal exams, math for grades 4 to 6, or diagnosing learning difficulties."
license: MIT
---

# Hebrew Classroom Worksheet Maker

## Problem

Teachers and parents spend evenings building Hebrew worksheets, and a general AI answer often looks fine but fails in class: words with letters the children have not learned, niqqud that ignores the grade, a math exercise that flips inside the Hebrew line, or content from a program the grade no longer follows. This skill makes an A4 sheet with a separate key, and checks the sheet before it reaches the copier.

## Instructions

### Ground rules

- **This skill serves the adult preparing the material.** Never direct young students to use the assistant.
- **No student data.** Never ask for names, needs, diagnoses or a class list. If someone pastes them, do not repeat them, and continue without them. Print a blank name field. When you make versions for one class, **every** version, including the regular one, looks the same and carries a neutral shape (● ■ ▲), never a level, a name or "easier". The teacher keeps the mapping. A note to the teacher never repeats a student's name or diagnosis, even when the request included them: write "the version you asked for", not "the version for [name]".
- **No diagnosis.** Do not infer or suggest a learning difficulty from a child's work or from a request. If asked, say that a worksheet cannot show this, and refer the person to the school's educational counselor, an educational psychologist or the family doctor.
- **Original text by default.** Never print a protected song, poem or textbook page, even with words removed and even for class use. Name the work, let the teacher use the class's licensed copy, and offer an original rhyme instead. Never say a use "is fair use". See `references/rights-and-privacy.md`.

### Step 1: One short question round

Ask once, in the user's language, only what is missing:

1. **Grade** (gan, or א to ו).
2. **Grade 1 and gan: what has the class learned?** Never assume an order, since it varies between reading methods. Ask in one compact list: letters, final letters (ם ן ץ ף ך), the two sounds of ב כ פ (hard, soft or both), sin (שׂ), and vowels.
3. **Where is the class in the year**, and for math, up to which number.
4. **Stream, only when it changes the content** (a holiday, a religious text, images).

If the request already answers these, go straight to the work. If a detail is missing and you must proceed, take the narrower reading: a listed ב כ פ means the hard sound only, a listed ש means shin only, and final letters are not taught.

Hebrew as a second language (Arab and Druze schools, ulpan) does not follow this grade table. Ask for the learners' level and say that the grade rules do not apply.

### Step 2: Apply the rules for this grade

Full wording and sources are in `references/grade-rules.md`.

| Grade | Niqqud | Math in תשפ"ז |
|---|---|---|
| Gan | Sound games, matching, circling. No copying or tracing sheets | The range the teacher states |
| א | Heavy, with the marks rule in Step 4 | New program: to 20, whole tens to 100. No × or : |
| ב | Heavy, vowel letters kept, partial toward year end | New program: to 1,000, multiples of 2, 4, 5, 10 |
| ג | Stories full. Instructions partial or none | New program: to 10,000, full table, remainder with a one-digit divisor |
| ד-ו | Sparse: rare words, terms, names, homographs | Not covered. These grades follow the 2006 program, and this skill has no checked math rules for it |

For math in grades 4 to 6, say this plainly. If the teacher still wants a sheet, ask for the exact topic and range, recompute every answer, and do not claim it fits the program.

Verses and prayers keep their original full pointing at every grade.

**When a request goes beyond the grade's current program** (for example multiplication in grade 1, or division with remainder in grade 2):

1. Keep the sheet inside the program by default.
2. Tell the teacher why in one line.
3. Replace those items with an in-program challenge for students ready for more: a missing addend, the equals sign on the left, or a word problem.
4. Leave the decision with the teacher. If they say to keep the original items after hearing this, add them, and list them in `teacher_override` on the script route.

### Step 3: Write the content

- **Check first whether the taught letters can carry a real story.** With few letters they usually cannot. Do not force disconnected sentences and call them a story. Use this route and tell the teacher why in one line:
  1. A short **read-aloud passage** on the topic, for the adult, on the teacher page.
  2. **Decodable word and short phrase tasks** for the child, built only from taught units.
  3. Comprehension where **the adult reads the question and the child circles a decodable word**.
- If the letters do carry a story, write one connected piece on the requested topic.
- **Decodable means every word**, with its real spelling and pointing: נֶשֶׁר has segol and דֹּב has holam, so neither fits a class that learned only qamats, patah and hiriq.
- **Instructions** use the plural imperative (הַקִיפוּ, כִּתְבוּ), with niqqud, since plural imperative and past tense look alike. Early grade 1 instructions are read aloud, so add a simple icon.
- **Questions must not give the answer away by grammar.** "מי שר?" with אִמָא and אַבָּא as options is answered by the verb alone. Use options of the same gender.
- **Arithmetic belongs in math sections only.** Never put arithmetic, a comparison, a count or a number in a multiple-choice item, including numbers written as words. Do not print clock times, dates or number ranges on the sheet. Write them in words, or leave them out. In a hand-made page keep every expression, including `<`, `>` and subtraction, inside a left-to-right element.
- **Pictures** must have one obvious Hebrew name. Check the first letter in Hebrew, not in English. If no decodable word has a clear picture, use a first-sound task or leave pictures out, and say so.

### Step 4: Niqqud

Prefer Dicta's Nakdan, following `references/niqqud-routes.md`, and tell the teacher which route was used.

**Grade 1 marks rule. Apply it to every word the same way:**

1. Remove every dagesh, except in **ב, כ, פ** and a **shuruk** (וּ). So: אִמָא, דָן, תָמָר, הַמַיִם, and also אַבָּא, סִפּוּר. If the class primer prints the dagesh in ג ד ת, keep it there at the start of a word and after a sheva (דָּן, תָּמָר), and use that form across the whole sheet. A dagesh that doubles a letter after a vowel is still removed. The final ת of אַתְּ is not a doubling, so in this setting it stays.
2. Remove the shin dot, except on a shin that also carries holam (שֹׁ). So: שָלוֹם, שָר.
3. Keep the sin dot (שׂ) and every vowel. Never add or change a vowel.

The Ministry's text says to omit strong dagesh and mappiq and not to point the right shin. The rest is this skill's inference. The dagesh stays in ב כ פ because it changes the sound there. It goes from ג ד ת by default because in modern Hebrew it does not change the sound. The dot stays on שֹׁ so the holam is not read as a sin dot.

### Step 5: Mandatory pass before sending, on every host

Do these five passes on the finished sheet, including on hosts with no code tool. Fix what you find, then pass again over what you changed.

1. **Decodability (grade 1 and gan).** Go word by word through everything the child reads: the text, options, matching words and word problems. For each letter, check it against the taught list, including final letters, the hard or soft sound of ב כ פ, and sin. For each vowel, check it against the taught vowels. A vav or yod that only carries a taught vowel is fine. Replace any word that fails. Never change its niqqud to make it pass.
2. **Grade 1 marks.** Apply Step 4 to every word, including titles and instructions. Every letter except the last must carry a vowel, unless it is a vowel letter, a silent alef after a vowel (as in רִאשוֹן, never an alef that opens a word), or comes right before וּ or וֹ.
3. **Recompute every answer** from the exercise as printed, one at a time. Through grade 3: whole numbers, nothing negative, even in a middle step. Remainder: `a : b = q + (r : b)` with r smaller than b. Each exercise has exactly one blank and one answer. Multiple choice has exactly one correct option and no arithmetic: if a question poses arithmetic, even in number words (שְׁלוֹשָׁה נֵרוֹת וְעוֹד שְׁנַיִם), move it to a math item. No check detects number words, so this pass is the only guard. Every key line points to something printed on the student page. **Read every word problem**: its numbers and its operation must fit the story. No script can check the operation.
4. **Program scope.** Compare every exercise with the Step 2 table. Grade 1 has no × or :, and works to 20 and in whole tens to 100. Notation is × and a colon, never ÷, and never the old form `7 (3)`. Grade 3 remainder stays within the 10 by 10 table.
5. **Privacy.** Read the reply and the sheet for any student name, diagnosis or level. Every version carries only a neutral shape.

### Step 6: Build and check, on hosts that run Python

Write `worksheet.json` in its own folder (format in `references/worksheet-format.md`), then:

```bash
python3 scripts/build_worksheet.py worksheet.json --out worksheet.html
python3 scripts/check_worksheet.py worksheet.json --html worksheet.html
```

The checker exits 1 on any error. Fix every error and run it again. Warnings need a decision. Math is printed only in one exact form: one exercise, one `___` blank, plain whole numbers (no commas), single spaces. Accepted: `a + b = ___`, `___ + b = c`, `a + ___ = c`, `c = a + ___`, `c = ___ + b`, `___ = a + b` (also with -, × and :), the remainder forms `a : b = ___ + (r : b)` and `a : b = q + (___ : b)`, and, from grade 2, the comparison `a ___ b` with the answer `<`, `>` or `=`. The grade 1 program compares numbers "ללא סימון מתמטי", so gan and grade 1 sheets do not use this form. Complete equations, several blanks, other blank styles and anything else are errors. Multiple choice cannot hold digits or operators. A word problem writes its numbers as digits. After you read it and confirm its exercise fits, set `prompt_read` to true. The checker compares the digits only, and the key page prints a reminder for the teacher to read it.

Hosts without a code tool skip this step, write the sheet in the reply or as HTML using `references/manual-route.md`, and **never say a script ran**.

### Step 7: Render and look

Where the host can make a PDF, print the HTML to A4, convert pages to images, and look at each page in grayscale:

- Each math expression reads in the same order as in the file, especially when the equals sign is on the left.
- Niqqud marks sit on the right letters and are not clipped.
- Every picture is recognizable, and its number is printed. Counters show the right number.
- The key's numbers match the student page.

### Step 8: Deliver

Give one PDF, or the HTML or text on hosts that cannot make a PDF: student pages first, then the key page. Say in plain words:

- what was checked and how (by the script, or by hand with no script), and for which school year (תשפ"ז);
- what still needs a person: reading the niqqud, reading each word problem against its exercise, and **confirming that no student's name appears**, since no check can recognize a name;
- any choice you made for the teacher, such as a read-aloud route, items kept in program, or dropping the dagesh in ג ד ת (one line, so a class whose primer prints it can ask to keep it);
- for a school teacher, one line: check whether this AI tool is on the Ministry's approved list.

The key page states that the sheet was prepared with AI. Do not claim Ministry approval or a guarantee of curriculum alignment.

## Examples

### Example 1: Grade 1 Hanukkah sheet, few letters

User says: "אני מורה בכיתה א. צריכה דף לחנוכה. הכיתה למדה קמץ, פתח, חיריק ואת האותיות א ב ל מ ר ש ת נ ד. קטע קריאה, 3 שאלות, התאמת מילה לתמונה, חיבור עד 10 עם סביבונים, ודף תשובות."

Actions: these letters have no word for the holiday, a candle or a dreidel, and no natural story. Put a short Hanukkah story on the teacher page to read aloud. Give the child short decodable lines (אַבָּא בָּא. אַבָּא שָר. אַבָּא אָמַר: שִיר!), three questions the adult reads while the child circles a word (תָמָר or אִמָא), a first-sound picture task in place of word-to-picture matching, and addition to 10 including `10 = 6 + ___`.

Result: a student sheet and a key page with the passage and questions. The reply explains the read-aloud choice in one line and asks whether final letters were taught.

### Example 2: A request beyond the grade

User says: "דף חשבון לכיתה א עם חיבור וחיסור עד 20, ותוסיפו כמה תרגילי כפל לילדים החזקים."

Actions: keep addition and subtraction to 20. Say in one line that multiplication is not in the current grade 1 program. For students ready for more, add missing-addend items and equations with the equals sign on the left. Ask whether the teacher still wants the multiplication items.

Result: an in-program sheet, with the final decision left to the teacher.

### Example 3: Grade 3 division with remainder

User says: "דף חילוק עם שארית לכיתה ג, 10 תרגילים."

Actions: use one-digit divisors. Print each exercise as `13 : 4 = ___ + (1 : 4)` or `13 : 4 = 3 + (___ : 4)`, never in the older bracket form. Recompute each quotient and remainder.

Result: one page with a key.

### Example 4: Kindergarten letter activity

User says: "אני גננת, רוצה דף להעתקת האות מ."

Actions: explain in one line that the Ministry's kindergarten chapter does not recommend formal writing practice, and offer a first-sound circling game with clear pictures instead.

Result: a sound-matching sheet.

## Bundled Resources

### Scripts

- `scripts/build_worksheet.py`: turns the worksheet JSON into a right-to-left, black-and-white A4 HTML with student pages and a key. It refuses arithmetic outside a math section. Run: `python3 scripts/build_worksheet.py worksheet.json --out worksheet.html`
- `scripts/check_worksheet.py`: reports decodability, grade marks, recomputed math for gan to grade 3 in one strict exercise format (not whether a word problem's operation fits its story), multiple choice, key references, notation, scope, level labels and identifiers, plural address, a few known protected texts, and print safety. It cannot recognize a person's name and does not clear copyright. Run: `python3 scripts/check_worksheet.py worksheet.json --html worksheet.html`
- `scripts/worksheet_lib.py`, `scripts/pictures.py`: shared helpers and a small black line picture set. Imported by the two scripts above.

The scripts need only Python, with no packages and no network.

### References

- `references/grade-rules.md`: niqqud, reading stages and math rules by grade, with the Ministry's wording and what is inference. Consult before writing a sheet.
- `references/worksheet-format.md`: the JSON format, picture names, check codes and what is not built. Consult when writing `worksheet.json`.
- `references/niqqud-routes.md`: how to get niqqud from Dicta and its terms. Consult at Step 4.
- `references/rights-and-privacy.md`: copyright, student privacy and AI-tool rules. Consult when a song, poem, image or student detail comes up.
- `references/manual-route.md`: a print template for hosts that cannot run scripts.

## Gotchas

- Agents assume a standard order of Hebrew letters and vowels. There is none, so use the class's own list, including final letters and the two sounds of ב כ פ.
- Agents force a "story" out of a few letters. The result is a list of unrelated sentences. Use a read-aloud passage with decodable tasks.
- Agents apply the grade 1 niqqud unevenly, removing a dagesh in one word and keeping it in the next. Apply the rule in Step 4 to every word.
- Agents add what the teacher asked even when it is outside the grade's program. Keep the sheet in program by default, explain in one line, and let the teacher decide.
- Agents recall the older 2006 math program. In תשפ"ז grades 1-3 are on the new program, and only grades 4-6 remain on 2006.
- Agents write remainders as `7 (3)`. The new grade 3 program flags that form as misleading.
- Agents treat holiday songs as free and cite section 29 for copying. Section 29 covers performance only. The words of "סביבון סוב סוב סוב" are protected through 31.12.2060.
- Agents use color emoji for pictures. They differ between devices and turn to gray blobs on a photocopier.

## Reference Links

| Source | URL | What to Check |
|---|---|---|
| Ministry niqqud outline | https://meyda.education.gov.il/files/Mazkirut_Pedagogit/HebrewPrimary/learning-teaching/books/nikod.pdf | Niqqud by grade |
| Language curriculum, K-2, 2026 | https://meyda.education.gov.il/files/Pop/0files/ivrit_hinuch_leshoni/Yesodi/tohnit-limudim-safa.pdf | Reading stages, no fixed vowel order |
| Math supervisor circular, תשפ"ז | https://meyda.education.gov.il/files/Mazkirut_Pedagogit/math/primary-school/math2025/mafmar_yesodi_tashpaz.pdf | Which grades are on the new program |
| New math program, grade 1 | https://meyda.education.gov.il/files/Mazkirut_Pedagogit/math/primary-school/math2023/Newprogramgrade1.pdf | Grade 1 scope |
| New math program, grade 3 | https://meyda.education.gov.il/files/Mazkirut_Pedagogit/math/primary-school/math2023/Newprogramgrade3.pdf | Remainder notation |
| Ministry AI guidance | https://meyda.education.gov.il/files/Pop/0files/lemida-metukshevet/AI/AI-Usage-Guidelines.pdf | Student data, approved tools |
| Copyright Law (unofficial consolidation) | https://he.wikisource.org/wiki/חוק_זכות_יוצרים | Sections 19, 29, 38, 43 |

## Troubleshooting

### Error: LETTER or VOWEL on a word that looks fine

Cause: the word uses a final letter, a soft ב כ פ, sin or a vowel outside the class's list. Solution: replace the word. Do not change its niqqud to make it pass.

### Error: G1_PROFILE or UNPOINTED

Cause: the word does not follow the grade 1 marks rule, or a letter has no vowel. Solution: use the form the checker prints, or complete the pointing.

### Error: MATH_OUTSIDE

Cause: arithmetic, a comparison, a clock time, a date, a number range, or two numbers joined only by symbols, outside a math section. Solution: move arithmetic to a `math` section, and write anything else in words.

### Error: MC_NUMERIC

Cause: a multiple-choice stem, question or option holds a digit or an operator. Solution: move the question to a `math` section with `expr` and `answer`.

### Error: WORD_PROBLEM

Cause: the digits in the question differ from the exercise, the numbers are written as words, or nobody confirmed the question was read. Solution: write the numbers as matching digits, read the story against the exercise, then set `prompt_read` to true.

### Warning or error: G1_GDT

Cause: the sheet has the dagesh in ג ד ת, or mixes both forms. Solution: remove it, or set `gdt_dagesh` to `keep` if the class primer prints it, and use one form on the whole sheet. Mixed forms are an error under every setting. If a word correctly has no dagesh after a closed syllable, list it in `sight_words`.

### Error: MATH_GRADE

Cause: a math section in grades 4 to 6, which this checker does not cover. Solution: tell the teacher, and follow the note in Step 2.

### Error: MATH_PARSE

Cause: the exercise is not in the one accepted form, for example a complete equation, two blanks, a comma in a number or another blank style. Solution: rewrite it with one `___` blank, as in Step 6.

### Error: STALE or KEY_ORPHAN

Cause: the page does not match the JSON, or the key points to something not printed. Solution: rebuild from the JSON rather than editing the HTML by hand.

### Math looks reversed in a hand-made page

Cause: the expression is outside a left-to-right element. Solution: keep each expression inside `<bdi dir="ltr" class="math">`, then look at the page again.

### Niqqud shows as boxes or shifted marks

Cause: the font on that device lacks Hebrew points. Solution: select a Hebrew font with niqqud support, such as Noto Sans Hebrew, then print again.
