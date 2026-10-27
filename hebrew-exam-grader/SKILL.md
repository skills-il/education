---
name: hebrew-exam-grader
description: "Helps an Israeli teacher grade a class set of Hebrew-language exams and essays against a points rubric. Anonymises students first, builds the rubric from the exam and answer key (templates for bagrut Hebrew practice, high-school and grade-8 writing, and literature bands), respects testing accommodations, scores each criterion with a quoted line from the answer, flags answers that need the teacher's judgment, drafts short Hebrew feedback, and outputs a draft class grade sheet plus a common-mistakes summary. Every grade stays a suggestion until the teacher approves it, as Ministry of Education guidance requires. Use when a teacher asks to check, mark or give feedback on class essays or exams, bdikat mivchanim, bdikat chiburim, a mechvan (rubric), or handwritten answers to transcribe and grade. Do NOT use for writing a student's essay, student exam preparation, appealing an official bagrut grade, or math exams checked by final answer."
license: MIT
---

# Hebrew Exam Grader for Teachers

## Problem

An Israeli teacher with thirty essays to mark faces the same trade-off every week: detailed,
fair feedback takes hours, and short feedback teaches nothing. The Ministry of Education now
trains teachers to use AI for exactly this, but with hard conditions that a generic chatbot
ignores by default: no identifiable student data, a rubric fixed in advance, a teacher who
approves every grade, and extra care with Hebrew handwriting. This skill runs the marking loop
inside those conditions and hands back a draft grade sheet the teacher checks line by line.

## Instructions

The skill is for the teacher only. Students never use it. Its output is a draft: a grade becomes a
grade only when the teacher approves it, and it is never an official bagrut grade.

**Draft first, questions after.** Anonymisation (Steps 1.3 and 1.4) is the ONLY check that stops
the work: if identifying data is present, stop, ask for the material again anonymised, and do not
grade. Otherwise, when the answers are there and a rubric can be identified (the teacher's own, or a
named or recognisable template such as the Ministry grade-8 writing rubric or the 11282 60/40
structure), grade in the SAME response:

1. State the rubric you applied at the top, before any score ("המחוון שהפעלתי: ..."), with its
   status (practice or school). That is the rubric, fixed for this class.
2. Give per-criterion scores with quotes, flags, feedback, and the draft sheet or CSV if asked, all
   labelled a draft pending the teacher's approval. If the teacher's message did not state
   accommodations, the draft line at the top AND the closing line say: "accommodations not yet
   applied: do not approve any row until you answer the accommodations question". Until
   accommodations are known, the draft feedback names no spelling or handwriting point.
3. Then, after the grades, ask only what the input did not answer, framed as "answer these and I
   will re-score if anything changes": approve or change the rubric, whether the task counts toward
   the school-based bagrut component, exempt or adjusted criteria per code, the singular feedback
   form per code, and which tool and account (with the information in Step 1.1).

If no rubric can be identified at all, pick the closest template, say so at the top, and still
grade as a labelled practice draft. If the rubric changes later, re-score every answer, never a
selection. On a first batch, these draft grades are the calibration sample (Step 6); say so.
One exception to grading in the same turn: photos of handwriting. There the first reply is the
verbatim transcription for the teacher to confirm (Step 5), and grading follows confirmation.

### Step 1: Safeguards first (before reading any student text)

These are the product, not a preamble. Run them at the start of every session.

1. **Tell the teacher what the Ministry says about the tool (information, not a gate).** The
   binding AI guidelines address non-catalog tools in one case only. The clause, in full:
   "ככל שייעשה שימוש על ידי מורה באופן עצמאי, לצורכי הכנת חומרי הוראה, בכלי שאינו כלול ברשימת
   הכלים המאושרים בקטלוג, יש להקפיד על איסור שיתוף מידע אישי ועל התנהלות לפי הכללים האתיים
   המופיעים בהנחיות אלה, ויש להימנע מהצגת כלי זה במסגרת הכיתה."
   Say plainly: the clause addresses preparing teaching materials. It does not address assessing
   student work, and nothing in the guidelines expressly provides for marking student work in a
   tool outside the Ministry's approved catalog. The safe route is a tool from the Ministry's
   catalog, or written approval from the school (principal or ICT coordinator) for this use. Do
   not tell the teacher their tool is approved or forbidden; that is the school's call. If the
   teacher has not said which tool or account they use, ask it among the questions after the
   grades; the answer does not change the steps that follow.
2. **Anonymise before anything is pasted.** The Ministry's AI guidelines (January 2026) forbid
   sharing personal, sensitive or identifiable information about students with AI systems, by
   text, images, audio or any file. The Ministry's training on AI marking says to anonymise names
   with initials or codes before uploading exam data. The teacher does this on their own computer:
   - Use short codes: a capital Latin or Hebrew letter and one to three digits, or two to three digits
     (S01, ח1, 07). If the teacher already uses codes like that, keep them as they are; do not
     re-map them. Not initials, not nicknames, not ID numbers. The list linking codes to names stays with the
     teacher, offline. Never ask for it, never accept it.
   - Remove identifying details inside the answers: names of the student, classmates or family,
     ID or phone numbers, addresses, the school's or a small town's name, a parent's workplace,
     health or welfare disclosures.
   - Keep every other attribute of a code offline too. Accommodation reasons and diagnoses never
     enter the chat; only the lists of exempt and adjusted criteria do (Step 4). Grammatical gender, if used
     at all, is asked only after scoring (Step 8).
3. **Before grading each batch, read it for identifying details yourself.** Look for personal
   names, 9-digit numbers, emails, phone numbers, addresses, school or town names, and health or
   welfare details. If you find one, stop the whole batch: do not repeat the detail, name the code
   and line where it appears, and ask for the batch again after anonymisation. Suggest deleting
   the conversation and any uploaded file.
4. **Photos need their own check.** The teacher, before uploading:
   - crops each page to the answer area only;
   - covers every examinee sticker and ID-number field (bagrut-style notebooks carry no name, but
     do carry stickers printed with the candidate's personal details), any name in a page header,
     class or section lines, and earlier grades;
   - checks the background for class lists or other students' sheets;
   - removes location data: take a screenshot of the photo and upload the screenshot, or turn off
     location in the camera.
   You then inspect every image for a name, a 9-digit number, a sticker or a barcode before
   transcribing. If one is visible, refuse that image and say why.
5. **Account, history, training, files.** Recommend an organisational (school) account and turning
   chat history off (both Ministry recommendations). Also: if the service has a setting that lets
   it use conversations to train models, turn it off, and delete uploaded photos and files from
   the service when the marking is done.
6. **The teacher approves every grade, row by row.** The Ministry's rule is not to approve grades or
   feedback automatically. The sheet is marked as a draft, and its approval column is filled by the
   teacher one row at a time after reading the reasons and quotes, never in bulk. Nothing is
   imported into the school grading system before every row is approved.
7. **Transparency without promoting the tool.** The Ministry asks teachers to explain to students
   when and how AI was used in checking or feedback. The binding clause above also says to avoid
   presenting a non-catalog tool in class. Reconcile them: students are told that AI assisted the
   checking and how the teacher reviewed it, without demonstrating or recommending the specific
   tool. How exactly to tell them is the school's decision.
8. **Disclosures of harm.** If an answer suggests that a student is being harmed (abuse, neglect,
   self-harm, violence at home), stop grading that answer and tell the teacher to involve the
   school counsellor (יועץ/ת) under the school's procedure. Penal Law section 368D(ב) (חוק העונשין,
   סעיף 368ד(ב)) lists "עובד חינוך" among professionals who, "שעקב עיסוקם במקצועם או בתפקידם היה
   להם יסוד סביר לחשוב כי נעברה עבירה בקטין או חסר ישע בידי אחראי עליו", must report "בהקדם
   האפשרי לעובד סוציאלי שמונה לפי חוק או למשטרה". The duty is the teacher's own: telling the
   counsellor is the school's route for doing it, normally in coordination, not a substitute for
   it. The teacher should get guidance from the counsellor or principal on how it applies.
   Never put the content in feedback, flags or the class summary. In the sheet use only the
   `sensitive_content` flag.

### Step 2: Choose the checking level, and ask what the task counts toward

The Ministry's training distinguishes a full in-depth check, a sample check, a submission-only
mark, and focused feedback. Ask which one this task needs. A practice worksheet does not need
per-criterion scoring; a term essay does.

Among the questions after the grades, ask the grade level and what the task counts toward:
formative, a term grade, or the school-based part of the bagrut. Per the Hebrew supervisor's circular for תשפ"ג (2022-2023), the
Hebrew bagrut grade combines a school-based assessment worth 30% with an external exam worth 70%,
and content from both programs is taught in grade 10. If the task feeds the school-based component,
the grade is an official school grade: the teacher alone decides it, and the school's and the
subject supervisor's current rules for that component govern assessment and documentation. Say so,
do not call the output "practice", and tell the teacher to check the current year's circular.

If the teacher asks for "the bagrut grade to enter", still compute the combined figure as a draft
practice score (for 11282: the comprehension points the teacher gives, out of 60, plus the essay
score out of 40, by simple addition), and say plainly that it is not an official bagrut grade and
that the teacher decides what is entered.

### Step 3: Build and freeze the rubric

Use what the teacher gave: their own or the school's rubric always wins, and a key or model answer
if they pasted one. Otherwise apply the template that matches the task from
`references/rubric-templates.md` and say which. Ask for a missing key only when an item truly cannot
be scored without it, and then grade everything else in the meantime:

| Template | When | Shape |
|---|---|---|
| A. 11282 practice paper | Practice on the Hebrew comprehension and writing paper | Reading comprehension 60, written expression 40, item weights read off the paper |
| B. 4 by 4 bands | Literature answers only | Four literature criteria, each scored 0-100 inside bands 0-39 / 40-59 / 60-79 / 80-100 |
| C. Grade 8 writing | Middle-school argumentative writing | 15 + 5 + 3 + 2 = 25 points, times 4 for 0-100 |
| D. Grades 10-12 language essay | High-school language essays with no school rubric | Five criteria from the Ministry's model prompt, 1-4 each, labelled practice |

Rules for the rubric:

- Every criterion has an id, a label, a maximum, and a description of full, partial and zero
  credit. Partial-credit rules come from the teacher, not from you.
- Every rubric has a status: `practice` (any template here) or `school` (the teacher's or school's
  own). The status is printed on the sheet.
- 11282 is the paper repeat and external examinees take in place of the school-based part; use its
  item weights as printed on that paper, never uniform or carried over from another sitting.
- A mock of 11281 (the 70% external exam general examinees sit): one criterion per printed item
  from that paper's weights, as in A, but do not reuse A's 60/40 split.
- No official public rubric for the 40-point 11282 writing chapter was found. Mark the essay on a
  separate sheet with C or D scaled to 40, labelled practice, and carry that score into A.
- C is a middle-school rubric. If a high-school teacher uses it, the rubric name says so.
- B is for literature. Its device and amar criteria do not fit a language essay; use D.
- Answer keys: link to the Ministry file, let the teacher paste only the items being marked, never
  reproduce a key into anything shared. Ministry solution files say not to copy or publish them
  without permission, and a corrected solution, when issued, is the binding one.
- State the rubric as a table at the top of the response, before any score, and grade with it as
  a draft. The teacher approves or changes it afterwards. Once stated, it does not drift between
  answers; if the teacher changes it, re-score every answer already scored, never a selection.

### Step 4: Accommodations, per code

Among the questions after the grades, ask the teacher which codes have approved testing
accommodations that affect how a criterion is marked, and re-score those codes when they answer.
Until they answer, the draft says "accommodations not yet applied: do not approve any row until you
answer the accommodations question", and no feedback names a spelling or handwriting point. Ask for the criteria only, never the diagnosis or the reason. Accommodations are decided per
student through the school's process: a Ministry accommodations document (April 2025, written for
the ICT subject, used here only for the general process) says requests
are discussed in a school committee and, where needed, a district accommodations committee or the
"מלקויות ללמידה" program, and that decisions rest first on the teachers' professional assessment,
supported by a diagnosis, not the other way round. It also tells schools to check the
learning-disabilities division's procedures circular every year. So never infer an accommodation
from anything in the text; the teacher tells you. New immigrants (עולים חדשים) may sit separate
questionnaires (the Hebrew circular lists one for new-immigrant repeat examinees), and the teacher
knows which apply.

Each accommodation becomes one of two entries per code:

- **Exempt**: the criterion is not marked at all for this code. It leaves both the total and the
  maximum, the grade is rescaled over the rest, and it is never mentioned as a weakness (`exempt`
  in the script). Use it only when a whole criterion measures what the accommodation removes, such
  as a separate spelling criterion (template C).
- **Adjusted**: the criterion is still marked, with the accommodation applied (`adjusted` in the
  script, printed on that row so the teacher can audit it). Example: an accommodation under which
  spelling errors are not counted. Where spelling sits inside another criterion (every comprehension
  item in A, the language criterion in D), mark that criterion as if the spelling were correct and
  judge register, vocabulary, grammar and punctuation as usual. Never exempt a whole criterion
  because of a spelling accommodation.
- A language (לשון) item that tests a spelling or morphology rule itself: ask the teacher, per item,
  whether the accommodation applies to it.
- Still transcribe verbatim, since the transcript must be faithful; the accommodation acts on the
  score, not on the transcript.
- Answers given by dictation or typed by someone else: the spelling and handwriting are not the
  student's. Mark spelling exempt or adjusted as the teacher says.
- If exempt criteria remove more than half of a code's maximum, the script warns: the grade then
  rests on few criteria, and the teacher should know.

### Step 5: Take in the answers

**Typed or scanned text:** batches of about five to ten anonymised answers, each headed by its
code, after the Step 1.3 check.

**Photos of handwriting:** transcribe first, grade later, never both in one pass.
1. Run the Step 1.4 image check.
2. Transcribe verbatim, including spelling, grammar and punctuation errors. A silently corrected
   word destroys the spelling and grammar criteria.
3. Mark every unclear word as `[?word]` and every unreadable span as `[unreadable]`.
4. Show the transcription to the teacher and wait for confirmation or corrections.
5. Grade only confirmed text. An unconfirmed answer gets no score.

The Ministry's training is blunt: AI still struggles to read Hebrew handwriting, any such use needs
teacher supervision, a result must not become a final grade without a teacher check, and handwriting
checking is better used for learning than for summative assessment. Pass that on.

### Step 6: Calibrate on a small sample

The first batch's draft grades are the calibration sample; say so when you deliver them. Ask the
teacher to compare them with their own reading (or their own marks, if they marked a few by hand)
before the next batch. Where you disagree, ask which reading of the rubric is right, write it into
the rubric as a clarification, and re-score the batch. This is general good practice rather than a
Ministry rule.

### Step 7: Score each answer, criterion by criterion

For every criterion of every answer, output:

| Field | Content |
|---|---|
| score | a number within the criterion's maximum, or `exempt` |
| reason | one short sentence tied to the rubric descriptor |
| evidence | a short verbatim quote from the answer that supports the score. For a missing element, write what is missing instead |
| flag | one reason from the fixed list (Step 9), or empty |

Rules from the Ministry's model prompt and model-answer guidance:

- Do not invent anything that is not in the answer. No quote, no credit claimed from it.
- Flag rather than guess: an interpretation that differs from the key but may be valid, an answer
  between two bands, an unconfirmed transcription, a passage that may be copied or AI-written, an
  off-topic or very short answer, or sensitive content (Step 1.8).
- Literature: the Ministry instructs bagrut literature examiners to be open to a different
  interpretation, provided it rests on the work and is properly reasoned. Score the reasoning, not
  the agreement with the key. (Applying the same openness to other open answers is general
  practice, not a Ministry rule.)
- Literature devices, derived from the same file, which presents its answers as possible ones
  ("בדגם שלהלן מוצעות תשובות אפשריות לשאלות שבמבחן"): unless the question itself names specific
  devices, credit any device correctly identified in the work, exemplified and tied to the reading,
  even when the key lists different ones.
- If the teacher's rubric says "anything that does not match the rubric gets 0", the teacher's
  rubric wins: score 0 by it, flag `alt_interpretation`, and put in the reason the score the
  openness principle would support (for example "לפי כלל הפתיחות: 3/5"). Add one sentence that the
  Ministry asks bagrut literature examiners to accept grounded, reasoned readings, and leave the
  decision to the teacher.
- Published model answers are short main-point answers, and the exam requires expansion beyond
  them. Never penalise an answer for saying more than the key, and never require its wording.
- Possible AI-written student text: you cannot detect it reliably. Flag it; never state that a
  student cheated. The Ministry asks teachers to adapt assessment to the fact that work may include
  AI-written parts.

General grading practice (not a Ministry rule), applied by default because the Ministry's
guidelines warn that AI produces bias and unfairness:

- Score against the descriptors, not against length. A long answer is not better because it is
  long, and a short one that meets the descriptor is not worse.
- Grade one criterion across all answers in a batch, then the next criterion, rather than one
  answer across all criteria. It keeps the standard steady.
- Shuffle the order of codes before scoring, so the same students are not always first or last.
- Start each batch from the frozen rubric only: a fresh session per batch where possible, or at
  least restate the rubric and do not compare a new answer with earlier ones.
- After all batches, blind re-check: re-score about one answer in ten, taken from the first and
  the last batch, without looking at the first score, and report every disagreement to the teacher.
- Give the script each answer's word count and batch number. It prints a length-vs-score
  correlation and a per-batch mean. A strong correlation or a drifting batch mean goes to the
  teacher as a warning.
- Do not penalise features of a non-native writer outside the language criteria. Content,
  organisation and reasoning are scored on content, organisation and reasoning.

### Step 8: Write the feedback (after every score is frozen)

Per student, in Hebrew, short:

- two strengths and two things to improve, each pointing at a specific place in the answer, never
  an exempt criterion;
- one closing sentence in the second person, encouraging and respectful (the Ministry's model
  prompt asks for this shape).

The draft feedback is in the plural. Among the questions after the grades, offer to switch it to
the singular form (masculine or feminine) per code; scores are already fixed by then, so gender can
never touch a score. Do not store the form in the sheet.

The teacher edits and adds personal comments before anything reaches a student. The Ministry's
practice page says to check and update the AI's feedback before passing it on.

### Step 9: Draft grade sheet and common mistakes

**Grade sheet.** The first line says it is an unapproved draft, the second gives the rubric name,
status and date. Then one row per code: each criterion score (or "exempt"), total, maximum, draft
grade if the rubric scales, exempt criteria, adjusted criteria ("מותאם"), flags, and an empty
per-row approval column.

Flags come from a fixed list, never free text, so no name or quote can leak into the sheet:
`teacher_judgment`, `alt_interpretation`, `between_bands`, `transcription_unconfirmed`,
`possible_ai_text`, `off_topic`, `too_short`, `sensitive_content`. Format: `criterion:reason`.

- Shell agents (Claude Code, Cursor, Codex, Windsurf, OpenCode, OpenClaw, Gemini CLI, Antigravity,
  Grok Build, Copilot, and Gemini Spark): write the scores as JSON (shape in the script's docstring, or
  `--print-example-input`) and run `python3 scripts/grade_sheet.py scores.json -o grade_sheet.csv`.
  The script refuses any code that is not exactly a short code (a capital Latin or Hebrew letter and
  1-3 digits, or 2-3 digits: S01, ח1, 07), any record with an identifying field
  (name, ID, gender, diagnosis and similar), any value in a student record, the rubric name or a
  criterion label containing a 9-digit number, an email, a phone number or a Latin first and last
  name, any flag outside the fixed list, a score that is not a finite number within its maximum,
  and a score on an exempt criterion. It cannot recognise a Hebrew name inside free text, which is why
  the sheet allows no free text. It writes UTF-8 with BOM so Excel shows Hebrew.
- Chat agents with no script access (Claude.ai, ChatGPT, Claude Desktop, Manus, Grok): build the
  same sheet yourself as a CSV code block, with the draft line on top, the exempt and adjusted
  criteria on each row, and a class-average row at the end. Add a column that shows the addition (for example `2+5+3+2+4+2+1=19`) so the teacher can
  audit it, leave the total empty for any record with a missing score, and tell the teacher to
  re-add each row in the spreadsheet with =SUM() before approving. If Hebrew shows as gibberish in
  Excel, import the file as UTF-8 or paste it into Google Sheets.

**Common-mistakes summary.** For the class as a whole:
- the criteria with the lowest class average relative to their maximum;
- recurring errors, each with how many answers showed it and one short example with any
  identifying detail removed;
- items most of the class got wrong (the Ministry's training names this as a key use of the data);
- one or two suggestions for what to reteach.

No codes in the summary unless the teacher asks, and nothing from a `sensitive_content` answer.

**Close with:** the list of flagged items, the blind re-check disagreements, the length and drift
warnings if any, and a reminder that every row is a draft until the teacher approves it. If the
accommodations question is still open: "accommodations not yet applied: do not approve any row until
you answer the accommodations question".

## Examples

### Example 1: Three grade-8 texts, codes already given, CSV requested
User says: "תבדוק לפי המחוון הרשמי של משרד החינוך למשימת כתיבה פנימית בכיתה ח', ותן לי CSV" with
three texts headed ח1, ח2, ח3.
Actions:
1. Step 1.3: no identifying details, so continue. Keep the codes ח1-ח3 as they are.
2. In the same response: "the rubric I applied" (template C, 25 points times 4, practice), then
   per-criterion scores with quotes and flags, plural feedback, and the CSV with a visible sum
   column, the draft line and an empty approval column. Say these grades are the calibration
   sample.
3. After the grades: approve or change the rubric, accommodations per code, singular form per
   code, tool and account.
Result: graded draft CSV in the first reply; the teacher's answers lead to re-scoring only where
something changed.

### Example 2: Photos of handwritten answers
User says: "Here are photos of 12 handwritten answers to the literature question, grade them."
Actions:
1. Inspect every image for a name, sticker, barcode or 9-digit number; refuse any that shows one.
2. Transcribe verbatim with `[?]` marks; wait for the teacher to confirm each transcription.
3. Grade only confirmed texts with template B, flagging alternative interpretations.
Result: confirmed transcriptions, scores with quotes, flags; unconfirmed answers stay unscored.

### Example 3: 11282 mock, "give me the bagrut grade to enter"
User says: comprehension already marked at 48, here is code 07's essay, give me the final bagrut
grade to enter.
Actions:
1. State the rubric applied to the essay: a practice rubric (C or D) scaled to 40, because no
   official public rubric for the 11282 writing chapter was found.
2. Score the essay out of 40 with quotes per criterion, note it is shorter than the roughly 300
   words the paper asks for if so, and add: 48 + essay = draft total out of 100.
3. Say plainly: a draft practice score, not an official bagrut grade; the teacher decides what is
   entered. Then ask whether the mock counts toward the school-based component.
Result: a draft essay score out of 40 and a combined draft total, both clearly not a bagrut grade.

## Recommended MCP Servers

None required. A filesystem MCP lets Claude Desktop save the CSV directly; without it, the teacher
copies the CSV block.

## Bundled Resources

### Scripts
- `scripts/grade_sheet.py`: builds the draft CSV grade sheet, class averages, per-batch means and a
  length-vs-score check from a scores JSON, with exemptions and anonymisation guards. Run:
  `python3 scripts/grade_sheet.py --help`, or `--example`.

### References
- `references/rubric-templates.md`: what a task counts toward, the four templates with JSON for the
  script, the band scoring rule, and accommodations. Consult in Steps 2 to 4.
- `references/domain-checklist.md`: what this skill must cover and what it deliberately does not.

## Gotchas

- **Agents grade first and ask about privacy later.** Step 1 runs before any answer is read, and a
  batch with an identifying detail is refused, not graded.
- **Agents read the non-catalog clause as permission.** It covers preparing teaching materials, not
  marking student work. Quote it in full and send the teacher to the catalog or the school.
- **Agents penalise accommodated students, or over-correct.** A spelling accommodation plus
  verbatim transcription becomes a spelling penalty unless it is applied before any row is
  approved, which is why an unanswered accommodations question blocks approval. The
  opposite error is exempting a whole criterion (a comprehension item, the language criterion)
  when only its spelling part is affected: that criterion is adjusted, not exempt.
- **Agents "fix" handwriting while transcribing**, so the spelling criterion rewards an error the
  student made. Transcribe verbatim, mark doubts, grade only confirmed text.
- **Agents treat the answer key as the only right answer.** Ministry literature guidance requires
  openness to other well-reasoned readings, and published keys are deliberately brief.
- **Agents call a suggestion a grade**, or a practice score a bagrut score, and a teacher approves a
  whole column at once. The sheet says draft on its first line and approval is per row.
- **Agents withhold grades waiting for setup answers.** A teacher who pasted anonymised answers
  and named a rubric gets the graded draft in the first reply; questions come after the grades.
- **Agents drift.** Earlier essays in the context anchor later ones. Shuffle, start each batch from
  the rubric only, re-check blind.

## Reference Links

| Source | URL | What to Check |
|---|---|---|
| Ministry AI guidelines, summary (January 2026) | https://meyda.education.gov.il/files/Pop/0files/lemida-metukshevet/AI/AI-Usage-Guidelines.pdf | Privacy ban, history off, human decision, assessment |
| Ministry AI guidelines, binding document | https://meyda.education.gov.il/files/Pop/0files/lemida-metukshevet/AI/Guidelines.pdf | The non-catalog clause and its limits |
| Ministry training: AI for checking work and feedback | https://meyda.education.gov.il/files/Pop/0files/lemida-metukshevet/bina_melachutit.pdf | Model prompt, handwriting, anonymisation, principles |
| Pedagogy portal: assessing writing with AI | https://pop.education.gov.il/teaching-tools/teaching-practices/search-teaching-practices/evaluating-writing-products-using-ai/ | 1-4 scale, review feedback before release |
| Hebrew supervisor's circular, תשפ"ג | https://meyda.education.gov.il/files/Mazkirut_Pedagogit/Ivrit/hozermafmar2022_2023.pdf | 30% school-based and 70% external parts, questionnaire codes |
| Hebrew 11282 paper, winter 2025 | https://meyda.education.gov.il/files/Pop/0files/ivrit_hinuch_leshoni/Chativa-Elyona/011282-K-01-25.pdf | Chapter and item weights, examinee stickers |
| Ministry accommodations document, April 2025 | https://meyda.education.gov.il/files/Pop/0files/tikshuv/hatamot.pdf | How accommodations are decided; check the annual circular |
| Penal Law, section 368D | https://he.wikisource.org/wiki/חוק_העונשין | Duty to report, education workers |

## Troubleshooting

### The teacher pasted answers with names or other identifying details
Cause: anonymisation was skipped or incomplete. Solution: stop the batch, do not repeat the detail,
name the code and line, ask for the batch again, suggest deleting the conversation and files.

### Scores swing between similar answers
Cause, usually: a rubric descriptor that can be read two ways, anchoring on earlier essays, or
batches too large. Solution: re-run calibration on the two answers, write the agreed reading into
the rubric, re-score the batch from a fresh context, criterion by criterion.

### Hebrew in the CSV shows as gibberish in Excel
Cause: Excel opened a UTF-8 file without a byte-order mark. `grade_sheet.py` writes one; a CSV
copied from chat may not. Solution: import as UTF-8 in Excel, or paste into Google Sheets.

### `grade_sheet.py` refuses the input
It exits with an error that names the record. Step 9 lists everything it refuses. Fix the input;
do not loosen the check.
