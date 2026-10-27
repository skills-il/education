# Domain Coverage Checklist: hebrew-exam-grader

Generated: 2026-10-27. Aggregator sweep: the Ministry of Education pedagogy portal
(pop.education.gov.il, teaching-practice and subject pages) and the Ministry file server
(meyda.education.gov.il: AI policy, teacher-training summaries, bagrut papers, rubrics, model
answers). NITE and the Council for Higher Education were swept for scope only: neither governs
how a school teacher marks a class exam, so they appear under "Out of scope".

Every row below that states a rule, a weight or a band is backed by an entry in `evidence.json`.
Rows marked (structural) describe how to reason and carry no figure.

## Must cover (core)

- [ ] Anonymise before anything is pasted or photographed. Names become codes, the name key stays
  with the teacher, identifying details inside the text are removed. Source: Ministry AI summary
  guidelines (January 2026) ban sharing identifiable student data with AI systems by any channel;
  the Ministry training summary on AI marking says to anonymise names with initials or codes before uploading
  exam data. Why core: this is the Ministry's own hard rule, and grades are the most sensitive case.
- [ ] Tool approval. The binding guidelines' non-catalog clause is limited to a teacher using a
  non-catalog tool "לצורכי הכנת חומרי הוראה", keeps the ban on personal information, and says to
  avoid presenting the tool in class. It does NOT cover marking student work. The skill states this
  as information in its single setup message (it does not gate grading on it), quotes the clause in
  full, and points to a catalog tool or written school approval. Why core: a teacher marking in a personal chatbot must not leave believing it is
  Ministry-sanctioned.
- [ ] Anonymisation enforced, not only advised: short codes (S01, ח1, 07; the teacher's own kept as they are), the agent reads each batch
  for identifying details and refuses it, the script whitelists codes, allows only fixed flag
  reasons, and scans every value for ID numbers, emails, phones and Latin full names. Attributes of a
  code (gender, accommodations) stay offline except the exempt- and adjusted-criteria lists.
- [ ] Photo identifiers: bagrut-style notebooks carry no name but do carry examinee stickers with
  personal details and an ID-number field (11282 paper). Crop, cover stickers and headers, check the
  background, strip location data; the agent refuses an image showing a name, ID, sticker or barcode.
- [ ] Testing accommodations (התאמות בדרכי היבחנות): ask per code which criteria are exempt or
  adjusted, never the reason. Exempt criteria leave total and maximum; adjusted criteria are scored
  with the accommodation applied and printed on the row. A spelling accommodation adjusts (never
  exempts) criteria that only contain spelling. Verbatim transcription never feeds a penalty the
  accommodation removes. Under draft-first, when the teacher's message does not state
  accommodations, the draft line and the closing line say "accommodations not yet applied: do not
  approve any row until you answer the accommodations question", and draft feedback names no
  spelling or handwriting point until they are known. Source: Ministry accommodations document, April 2025 (school committee,
  district committee or the מל"ל program; teachers' assessment first, supported by a diagnosis;
  check the annual procedures circular). The specific accommodations vary by subject and year, so
  none is stated as a rule.
- [ ] What the task counts toward. Hebrew bagrut per the תשפ"ג supervisor circular: school-based
  assessment 30% (reporting code 11283) plus external 11281 at 70%; 11282 is the 30% paper for repeat
  and external examinees; grade 10 teaches content of both programs. A task in the school-based
  component is an official school grade owned by the teacher. Why core: "never official" is wrong
  for that case.
- [ ] Disclosures of harm: stop grading the answer, involve the school counsellor, Penal Law section
  368D(ב) duty to report on education workers; never in feedback or summaries.
- [ ] Teacher approves every grade and every feedback text. Source: "לא לאשר ציונים או משובים באופן
  אוטומטי" and the human-in-the-loop rule. Why core: without it the tool issues grades.
- [ ] Rubric defined in advance and fixed across the class: stated at the top of the response
  before any score, applied to every answer, and a change re-scores everyone. Source: "להגדיר מראש
  קריטריונים".
- [ ] Draft first: with anonymised answers and an identifiable rubric, grade in the same response
  as a labelled draft, then ask the open setup questions; anonymisation is the only blocking check
  (handwriting adds the transcription confirmation before scores). The first batch's draft grades
  are the calibration sample. A request for "the bagrut grade to enter" gets a combined draft
  practice score (for 11282: comprehension out of 60 plus essay out of 40), stated as not an
  official grade (structural).
- [ ] Per-criterion score, a short reason, a quoted evidence span, and a "needs teacher judgment"
  flag. Source: the Ministry model prompt ("אל תמציא מידע שאינו מופיע בעבודה, וסמן מקומות שבהם
  נדרש שיקול דעת של המורה").
- [ ] Feedback: two strengths, two improvements, second person, encouraging and respectful.
  Source: the same model prompt. The teacher adds personal comments before release (POP page).
- [ ] Handwriting: transcribe, teacher confirms the transcription, only then grade; never a final
  grade without a teacher check; prefer formative use. Source: Ministry training summary on AI marking.
- [ ] 11282 practice paper structure: chapter one reading comprehension 60 points, chapter two
  written expression 40 points, essay of about 300 words, item weights printed on the paper.
  Source: the winter 2025 paper.
- [ ] Grade-8 analytic rubric in full: content and structure 0-15 (opening/closing 0-2, position
  0-7, cohesion 0-4, audience 0-2), syntax 0-5, register and vocabulary 0-3, spelling 0-2, total
  25, times 4 for 0-100. Source: Ministry docx rubric. All sub-items enumerated (Step C.1).
- [ ] 4 x 4 band rubric: the Ministry literature rubric's four criteria and four bands
  (0-40, 40-60, 60-80, 80-100), each criterion scored 0-100 inside its band with an explicit
  boundary convention; not mixed with a 1-4 scale; weights not stated in the docx, so confirmed
  with the teacher. Source: Ministry docx rubric.
- [ ] Grade 10-12 language essay: no public Ministry rubric found; practice rubric D from the
  Ministry model-prompt criteria and the POP 1-4 scale, labelled practice.
- [ ] Draft status on the sheet itself: first-line draft banner, rubric name and status, per-row
  approval, never bulk-approved or imported before approval.
- [ ] Bias controls: criterion-across-batch by default, shuffled order, fresh context per batch,
  blind re-check of about one answer in ten, length-vs-score and per-batch drift checks (general
  practice, operationalising the Ministry's bias warning).
- [ ] Openness to alternative interpretations in literature answers, provided they rest on the
  text and are reasoned. Source: summer תשפ"ו model-answer file, questionnaire 9181.
- [ ] Published rubrics are short main-point answers; the examinee is expected to expand.
  Source: the literature graduation-tests page. Why core: an AI matching against the key
  penalises the expansion the exam requires.
- [ ] Answer keys: link, never bundle. Ministry solution files carry "אין להעתיק או לפרסם אלא
  ברשות משרד החינוך"; a corrected solution supersedes the original.
- [ ] Never present the output as an official bagrut grade (structural).
- [ ] Tell students AI assisted the checking. Source: "שקיפות" principle.
- [ ] Organisational account and chat history off. Source: both Ministry documents.
- [ ] Class grade sheet plus a common-mistakes summary. Source: the training summary endorses
  finding questions most of the class got wrong.

## Should cover (advanced / edge cases)

- [ ] Checking levels: full, sample, submission-only, focused feedback (training summary). Lets
  the teacher choose the depth per task.
- [ ] Student work may contain AI-written parts (Ministry assessment clause). The skill must not
  act as an AI-text detector; it can only flag passages for the teacher.
- [ ] Hebrew second-person feedback is gendered (structural). Ask the singular form per code only
  after all scores are frozen; plural as fallback; never infer gender; never stored in the sheet.
- [ ] Verbatim transcription including spelling errors, or the spelling criterion is meaningless
  (structural).
- [ ] Calibration on a hand-graded sample before trusting the batch (structural, general
  practice; no Israeli source mandates a sample size, so the skill states none as a rule).
- [ ] Data settings: model-training off where the service offers it, delete uploaded files.
- [ ] Hebrew CSV opening as gibberish in Excel unless written with a UTF-8 BOM (structural,
  technical).
- [ ] Ministry bias and hallucination warnings, applied to grading (AI summary guidelines).

## Out of scope (explicit, with rationale)

- Student use of the tool (age bands, parental consent). The skill is teacher-only; students never
  touch it. Those rules govern student use.
- Writing an essay or answers for a student. A student asking the tool to write a bagrut essay is
  the opposite of this skill.
- Appealing an official bagrut grade (ערעור). Official bagrut marking belongs to the Ministry's
  examiners; this skill marks practice and school exams.
- Psychometric (NITE) and higher-education marking (CHE). Different institutions and rules. Student
  preparation for those exams belongs to `israeli-bagrut-psychometric`.
- Math and sciences checked by final answer. The rubric approach here is for written Hebrew
  answers; final-answer keys need no language model.
- AI-text detection. No reliable detector is claimed; the skill flags, the teacher decides.

## Authoritative sources

- https://meyda.education.gov.il/files/Pop/0files/lemida-metukshevet/AI/AI-Usage-Guidelines.pdf
  (privacy, history off, human decision, assessment clause; update date)
- https://meyda.education.gov.il/files/Pop/0files/lemida-metukshevet/AI/Guidelines.pdf (binding
  full guidelines; the non-catalog clause and its limits)
- https://meyda.education.gov.il/files/Mazkirut_Pedagogit/Ivrit/hozermafmar2022_2023.pdf (Hebrew
  supervisor circular: 30/70 split, questionnaire codes)
- https://meyda.education.gov.il/files/Pop/0files/tikshuv/hatamot.pdf (accommodations process,
  April 2025)
- https://he.wikisource.org/wiki/חוק_העונשין (section 368D duty to report)
- https://meyda.education.gov.il/files/Pop/0files/lemida-metukshevet/bina_melachutit.pdf (model
  prompt, handwriting, anonymisation, organisational account, transparency)
- https://pop.education.gov.il/teaching-tools/teaching-practices/search-teaching-practices/evaluating-writing-products-using-ai/
  (1-4 scale, review before release, no identifying details)
- https://meyda.education.gov.il/files/Pop/0files/ivrit_hinuch_leshoni/Chativa-Elyona/011282-K-01-25.pdf
  (bagrut 11282 structure)
- https://meyda.education.gov.il/files/Pop/0files/ivrit_habaah_lashon/chativat_bynaym/mivhanim-mesimot/mehvan-internal-writing-assignment.docx
  (grade-8 rubric)
- https://meyda.education.gov.il/files/Mazkirut_Pedagogit/SifrutMmd/omermechvan.docx (4 x 4 bands)
- https://meyda.education.gov.il/files/Mazkirut_Pedagogit%5CSifrutMmd/TshuvonSummerTashpav.pdf
  (openness to interpretation)
- https://pop.education.gov.il/tchumey_daat/literature-religious/high-school/pedagogy-literature-hemed/graduation-tests/
  (published rubrics are short)
- https://meyda.education.gov.il/sheeloney_bagrut/Pitronot_bagrut/2021/8/pitron-035581-00-HEB.pdf
  (no-copy notice, corrected solution binds)

## Known gaps (do not invent)

- No single public index of all bagrut answer keys was found; the folder root returns an error
  page. Keys are reached from each subject's page or by questionnaire number.
- No official Ministry rubric for the 40-point writing chapter of 11282 was located. The skill
  must not present the grade-8 or 4 x 4 rubric as the bagrut writing rubric.
- No public Ministry rubric for a grade 10-12 language essay was located; D is a labelled practice
  rubric.
- The 30/70 weights and codes come from the תשפ"ג circular; the current year's circular was not
  located. The skill tells the teacher to check it.
- No current accommodations document for the Hebrew subject was found. The April 2025 document used
  is for ICT; it supports only the general process. An older (2019) literature document that split
  accommodations by committee was dropped as superseded. The skill names no specific accommodation
  as a rule and asks the teacher which criteria are affected.
- A barcode on the examinee sticker was not confirmed from a primary source; the skill says
  "stickers with personal details" and asks the agent to refuse a visible barcode anyway.
- No benchmark of AI accuracy on Hebrew student handwriting was found. State the Ministry's
  caution, not a number.
