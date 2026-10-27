# Rubric templates

Four starting points. A, B and C are copied from Ministry of Education documents, cited in each
section. D is a practice rubric assembled from the Ministry's model prompt and its 1-4 scale. None
of them is the official marking scheme of a real bagrut sitting. The teacher adapts the template to
the exam in hand. The agent states the rubric it applied at the top of its response, before any
score, grades with it as a draft, and the teacher confirms or changes it afterwards (a change
re-scores every answer). Every template here goes on the
sheet with `"status": "practice"` unless the teacher says it is their own or the school's rubric
(`"school"`).

The JSON blocks are ready for `scripts/grade_sheet.py` (the `rubric` key). Chat-only agents use the
same structure as a table.

## First: what does this task count toward?

Ask before choosing a template. In the Hebrew (עברית: הבנה, הבעה ולשון) program described in the
Hebrew supervisor's circular for the תשפ"ג school year, the bagrut grade combines two parts:

| Part | Code | Weight | Who |
|---|---|---|---|
| School-based assessment (הערכה בית־ספרית) | 11283 (reporting code) | 30% | general examinees |
| External exam | 11281 | 70% (weighted with the annual magen grade) | general examinees |
| Questionnaire replacing the school-based part | 11282 | 30% | repeat examinees (נבחני משנה) and external examinees |

The 30% program covers comprehension and expression chapters plus selected chapters from one
language system (syntax or morphology), assessed by varied methods, and content from both programs
is taught during grade 10. So a grade-10 or grade-11 task may be part of the school-based 30%.

- If the task is formative or a term grade: proceed; the sheet is a draft for the teacher.
- If it counts toward the school-based bagrut component: the grade is an official school grade.
  The teacher alone decides it, and the school's and the subject supervisor's current rules for
  that component govern how it is assessed and documented. The tool may still help with feedback
  and consistency checks, but say this plainly and do not label its output "practice".
- The circular cited is for תשפ"ג (2022-2023). Weights and codes can change; tell the teacher to
  check the current year's circular.

Source: https://meyda.education.gov.il/files/Mazkirut_Pedagogit/Ivrit/hozermafmar2022_2023.pdf

## A. Practice on the 11282 paper (reading comprehension + written expression)

11282 is the paper repeat and external examinees take in place of the school-based 30%. Its
structure makes it a good practice paper for the comprehension and writing skills of the whole
program. Structure of the winter 2025 (תשפ"ה) paper:

| Chapter | What | Points |
|---|---|---|
| פרק ראשון | הבנת הנקרא, questions on two articles | 60 |
| פרק שני | הבעה בכתב, one argumentative article of about 300 words, one of two topics | 40 |
| Total | | 100 |

Each comprehension item prints its own weight beside it, for example "(5 נקודות)". Read the
weights off the paper you are marking. Never assume a uniform weight, and never carry weights from
one sitting to another.

Both chapters instruct "הקפידו על כתב ברור, על כתיב נכון, על כללי הדקדוק ועל פיסוק הגיוני", so
language accuracy is assessed in comprehension answers too. For a code with a spelling
accommodation, mark every item as if the spelling were correct and list the items under `adjusted`;
do not exempt the items. See "Accommodations" below.

Grammar (לשון: syntax or morphology) items, when an exam includes them, are marked one criterion
per item from the key, like comprehension items. This skill has no separate grammar template. For an
item that tests a spelling or morphology rule itself, ask the teacher whether a spelling
accommodation applies to it.

A mock of 11281, the 70% external questionnaire that general examinees sit
("נבחנים כלליים עברית :הבנה ,הבעה ולשון ,שאלון 70% 11281" in the circular's table), follows the
same method: one criterion per printed item, weights read off that paper. Do not reuse the 60/40
split above; it belongs to 11282.

How to build the rubric:

1. One criterion per comprehension item, `max` equal to the printed weight. For a multi-part item
   (א, ב) one criterion per part.
2. For each item, the acceptable answer points from the key the teacher has, plus partial-credit
   rules the teacher dictates.
3. The 40-point essay: no official public rubric for this chapter was located. If the teacher has
   none, mark the essay on a SEPARATE sheet with template C or D and `"scale_to": 40`, then enter
   the resulting essay score as the single `essay` criterion below. Both sheets carry
   `"status": "practice"`.

```json
{"name": "11282 practice", "status": "practice", "scale_to": 100, "criteria": [
  {"id": "q1", "label": "שאלה 1", "max": 4},
  {"id": "q2", "label": "שאלה 2", "max": 9},
  {"id": "essay", "label": "הבעה בכתב", "max": 40}
]}
```
(Abbreviated: list every item of the actual paper.)

Bagrut notebooks carry no name ("אין לכתוב שם בתוך המחברת משום שהבחינה נבדקת בעילום שם"), but
they DO carry examinee stickers printed with the candidate's personal details, and an ID-number
field ("מס' תעודת הזהות") on the cover. A photographed notebook is not anonymous until those are covered.

Source: https://meyda.education.gov.il/files/Pop/0files/ivrit_hinuch_leshoni/Chativa-Elyona/011282-K-01-25.pdf

## B. Four criteria by four bands (literature answer)

The Ministry rubric for an answer in the state-religious literature bagrut (ממ"ד). Each criterion
is placed in one of four bands, each with a written descriptor.

| Criterion | 0-40 | 40-60 | 60-80 | 80-100 |
|---|---|---|---|---|
| קשר בין שאלה לתשובה | no answer, or one component only | link unclear, a small part answered | partial link, most parts answered | clear link, all parts answered fully |
| ביסוס והנמקה של התשובה | claims wrong, work misrepresented | claims right but not grounded | grounded but not exhaustive | grounded and exhaustive |
| התייחסות לאמצעי עיצוב | no reference to devices | device named, no example, no link to the work | named and exemplified, no link described | named, exemplified, clear link to the work |
| רכיבי עמ"ר | student's view absent | view thin, loose link | view partial, partial link | reasoned view, clear grounded link |

(English glosses of the Hebrew cells. Paste the Hebrew original from the docx when marking.)

**How to score it, consistently:**

- Score each criterion directly on 0-100. First pick the band from the descriptors, then a number
  inside it. 0 is allowed (no answer).
- Boundary rule (a convention, because the docx bands share their end points): a score of exactly
  40, 60 or 80 belongs to the HIGHER band. So the bands are 0-39, 40-59, 60-79, 80-100.
- The docx states no weights between the four criteria. Equal weighting is an assumption: confirm
  it with the teacher, or take the teacher's weights.
- With equal weights the answer's grade is the average of the four, which is what the JSON below
  produces (max 100 each, total 400, `scale_to` 100).
- Do NOT mix this with a 1-4 scale. A 1-4 score scaled to 100 gives 25/50/75/100, which does not
  line up with these bands (a top-band answer scored 3 would land at 75, inside the 60-79 band).
  Use one or the other.

```json
{"name": "literature 4x4 bands", "status": "practice", "scale_to": 100, "criteria": [
  {"id": "link", "label": "קשר בין שאלה לתשובה", "max": 100},
  {"id": "grounding", "label": "ביסוס והנמקה", "max": 100},
  {"id": "devices", "label": "אמצעי עיצוב", "max": 100},
  {"id": "view", "label": "רכיבי עמ\"ר", "max": 100}
]}
```

B is a LITERATURE rubric. Its last two criteria (literary devices, the amar components) do not
apply to a language (לשון) essay. For a high-school language essay use D.

Literature answers have a rule that matters for AI marking. The Ministry's summer תשפ"ו
model-answer file for questionnaire 9181 says examiners must be open to the examinee's reading:
"הם רשאים לפרש את היצירות בדרך אחרת מזו שנלמדה בכיתה או מזו המוצעת כאן, ובלבד שהפירוש יסתמך
על היצירה והתשובה תהיה מנומקת כהלכה." And the published rubrics are short: "מחוונים אלו הם
תשובות בקצרה ובנקודות עיקריות. בבחינה התלמיד נדרש להרחבה ופירוט מעבר לכך."

Sources:
- https://meyda.education.gov.il/files/Mazkirut_Pedagogit/SifrutMmd/omermechvan.docx
- https://meyda.education.gov.il/files/Mazkirut_Pedagogit%5CSifrutMmd/TshuvonSummerTashpav.pdf
- https://pop.education.gov.il/tchumey_daat/literature-religious/high-school/pedagogy-literature-hemed/graduation-tests/

## C. Grade 8 writing task, 25 points times 4

The Ministry's analytic rubric for an internal Hebrew writing task in grade 8 (MIDDLE SCHOOL).

| Criterion | Sub-item | Points |
|---|---|---|
| איכות התוכן ואיכות מבנה הטקסט (0-15) | פתיחה וסיום | 0-2 |
| | עמדה מבוססת ומוצדקת (עמדה, ביסוס, הצדקה) | 0-7 |
| | לכידות וקישור | 0-4 |
| | עצמאות הטקסט ומודעות לנמען ולנסיבות השיח | 0-2 |
| התחביר | מבנה משפטים, התאם במין, במספר וביידוע, מילות יחס, פיסוק | 0-5 |
| משלב הלשון ואוצר המילים | | 0-3 |
| הכתיב | | 0-2 |
| Total | | 25 |

Final grade on 0-100: multiply the sum by 4. The form also asks for open feedback: strengths, and
what to strengthen. If a high-school teacher uses C, label it "middle-school rubric used as a
practice rubric for grade N" in the rubric name.

```json
{"name": "grade 8 writing", "status": "practice", "scale_to": 100, "criteria": [
  {"id": "open_close", "label": "פתיחה וסיום", "max": 2},
  {"id": "position", "label": "עמדה וביסוס", "max": 7},
  {"id": "cohesion", "label": "לכידות", "max": 4},
  {"id": "audience", "label": "מודעות לנמען", "max": 2},
  {"id": "syntax", "label": "תחביר", "max": 5},
  {"id": "register", "label": "משלב ואוצר מילים", "max": 3},
  {"id": "spelling", "label": "כתיב", "max": 2}
]}
```
With `scale_to: 100` the script multiplies 25 by 4, exactly as the form says. A student exempt from
spelling is graded out of 23 and rescaled.

Source: https://meyda.education.gov.il/files/Pop/0files/ivrit_habaah_lashon/chativat_bynaym/mivhanim-mesimot/mehvan-internal-writing-assignment.docx

## D. Grades 10-12 language essay (practice rubric)

There is no public Ministry rubric for a high-school language essay that this skill could find.
Prefer the teacher's or the school's own rubric (`"status": "school"`). If there is none, D is a
practice rubric built from two Ministry sources: the five criteria in the Ministry's model prompt
for AI-assisted checking ("הבנת המשימה, דיוק בתוכן, ארגון הרעיונות, יצירתיות, ניסוח ושפה") and the
1-4 per-criterion scale from the Ministry's teaching-practice page. Name it on the sheet as a
practice rubric.

| Criterion | 1 | 2 | 3 | 4 |
|---|---|---|---|---|
| הבנת המשימה | misses the task | partly answers it | answers it | answers it fully and precisely |
| דיוק בתוכן | mostly wrong or unsupported | mixed | accurate, thin support | accurate and well supported |
| ארגון הרעיונות | no visible structure | some order | clear structure | clear structure, smooth links |
| יצירתיות | none | a little | some original angle | a distinct, original angle |
| ניסוח ושפה | many errors that block meaning | frequent errors | few errors, suitable register | accurate, rich, register right |

The descriptors are this skill's wording, not the Ministry's: read them to the teacher and change
them to match the task. For a code with a spelling accommodation, the language criterion is
`adjusted`, not exempt: score it as if the spelling were correct and judge register, vocabulary,
grammar and punctuation as usual. Use 0 only for "no answer". With `scale_to: 100` a score of 15 of 20
becomes 75.

```json
{"name": "grade 10-12 language essay (practice)", "status": "practice", "scale_to": 100, "criteria": [
  {"id": "task", "label": "הבנת המשימה", "max": 4},
  {"id": "content", "label": "דיוק בתוכן", "max": 4},
  {"id": "organisation", "label": "ארגון הרעיונות", "max": 4},
  {"id": "creativity", "label": "יצירתיות", "max": 4},
  {"id": "language", "label": "ניסוח ושפה", "max": 4}
]}
```

Sources:
- https://meyda.education.gov.il/files/Pop/0files/lemida-metukshevet/bina_melachutit.pdf
- https://pop.education.gov.il/teaching-tools/teaching-practices/search-teaching-practices/evaluating-writing-products-using-ai/

## Accommodations (התאמות בדרכי היבחנות)

Accommodations are decided per student by the school's process, not by this skill. A Ministry
accommodations document dated April 2025 (ניסן תשפ"ה; written for the ICT subject) says:

- requests are discussed in a school committee and, where needed, a district accommodations
  committee or the "מלקויות ללמידה" program;
- decisions rest first on the professional assessment of the school's teachers, supported by a
  diagnosis and not the other way round;
- schools must check the learning-disabilities division's procedures circular every year;
- for that subject, accommodations that change presentation, response and content include playing
  the questionnaire aloud, typing answers on a computer, an adapted exam and an oral exam.

The specific accommodations differ by subject and year, so the skill names none as a rule. The
teacher reports, per code, which criteria are affected. Separate questionnaires exist for some
new-immigrant examinees (11272 in the Hebrew circular).

Two entries per code:
- `exempt`: a criterion not marked at all. It leaves both the total and the maximum, and the grade is
  rescaled over the rest. Only when a whole criterion measures what the accommodation removes (a
  separate spelling criterion, as in C). The script warns when exemptions remove more than half of a
  code's maximum.
- `adjusted`: a criterion still marked, with the accommodation applied, and printed on the row. For an
  accommodation under which spelling errors are not counted: every comprehension item in A and the
  language criterion in D are adjusted (scored as if spelling were correct), never exempt.

Rules:
- Ask only which criteria, never the diagnosis or the reason.
- Still transcribe verbatim; the accommodation acts on the score, not the transcript.
- Never list an exempt or adjusted aspect (for example spelling) as a point to improve in that
  student's feedback unless the teacher asks.
- Answers given by dictation or typed by someone else: spelling and handwriting are not the
  student's; mark spelling exempt or adjusted as the teacher says.
- A language item that tests a spelling or morphology rule itself: ask the teacher per item.

Sources:
- https://meyda.education.gov.il/files/Pop/0files/tikshuv/hatamot.pdf
- https://meyda.education.gov.il/files/Mazkirut_Pedagogit/Ivrit/hozermafmar2022_2023.pdf

## Answer keys: link, do not copy

Ministry solution files for bagrut carry the notice "אין להעתיק או לפרסם אלא ברשות משרד החינוך".
They also say a corrected solution, if published, is the binding one, and that publishing a
solution does not oblige examiners to accept a wrong answer. Point the teacher to the file, let the
teacher paste only the items being marked, and never reproduce a key into a file that gets shared.
Check for a corrected version before marking.

Example of such a file: https://meyda.education.gov.il/sheeloney_bagrut/Pitronot_bagrut/2021/8/pitron-035581-00-HEB.pdf
