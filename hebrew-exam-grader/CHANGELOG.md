# Changelog

## 1.0.0 (2026-10-27)

Initial release.

Built on the Ministry of Education's own conditions for AI-assisted marking, not on what a
general chatbot does by default:

- Anonymisation runs before any student text is read, and a named answer is refused, not graded.
  The Ministry's January 2026 guidelines ban identifiable student data in AI systems.
- Every grade is a suggestion with an empty teacher-approval column.
- Handwriting is transcribed verbatim (errors kept), confirmed by the teacher, and only then
  graded.
- Literature answers are scored on reasoning, with openness to readings other than the key, as
  the Ministry's model-answer file instructs.
- Answer keys are linked, never bundled.
- Testing accommodations: the teacher names, per code, criteria that are exempt (leave total and
  maximum) or adjusted (scored with the accommodation applied, printed on the row); never the
  reason. A spelling accommodation adjusts criteria that only contain spelling and never exempts
  them. Sourced to the Ministry's April 2025 accommodations document for the process only; a 2019
  document that split accommodations by committee was dropped as superseded.
- Draft first: with anonymised answers and an identifiable rubric, the first reply already
  contains the stated rubric, per-criterion draft scores with quotes, feedback and the sheet;
  setup questions come after the grades and lead to re-scoring only if something changes.
  Anonymisation is the only blocking check (plus transcription confirmation for handwriting), and
  the first batch's draft grades are the calibration sample.
- Teachers' own short codes (ח1, 07) are kept as they are.
- Literature: devices other than the key's are credited unless the question names specific ones.
- The Ministry's non-catalog clause is quoted in full and NOT presented as covering marking; the
  teacher is sent to a catalog tool or written school approval.
- The grade sheet is a draft on its own first line, carries the rubric status, is approved row by
  row, accepts only S01-style codes and fixed flag reasons, and rejects ID numbers, emails, phones
  and Latin full names anywhere in a record.
- 11282 is described as the paper repeat and external examinees take in place of the school-based
  30%; a task in the school-based component is an official school grade owned by the teacher.

Deliberately NOT asserted, because no primary source was found: an official public rubric for the
40-point writing chapter of bagrut 11282 or for a grade 10-12 language essay, the current year's
weights for the Hebrew school-based component, any accuracy figure for AI reading of Hebrew
handwriting, and any required calibration sample size. These are recorded in
`references/domain-checklist.md` under "Known gaps".
