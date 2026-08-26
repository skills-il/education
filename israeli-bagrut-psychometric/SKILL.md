---
name: israeli-bagrut-psychometric
description: Guide users through Israel's Bagrut matriculation exams and Psychometric entrance test (PET) system. Use when user asks about bagrut study units, psychometric scores, exam structure, university entrance requirements, sekher calculation, or study planning. Covers the Bagrut grading formula (70% exam + 30% magen), PET scoring (200-800), NITE registration, test dates, and strategies for maximizing combined admission scores (sekhem). Prevents confusion between the many overlapping terms and formulas in the Israeli higher-education admissions process. Do NOT use for university-specific admission thresholds, post-secondary academic advising, or non-Israeli education systems.
license: MIT
allowed-tools: Bash(python:*) Read
compatibility: Requires Claude Code or compatible AI coding agent
---


# Israeli Bagrut & Psychometric Guide

## Legal notice

This is a free informational tool operating through an AI model. It explains the Bagrut and psychometric rules and computes averages and grades from the figures you enter. Its output is an orientation estimate only. It is not an official grade, not an admission decision, and it does not determine entitlement to a Bagrut certificate, to accommodations, or to any benefit. The binding calculation belongs to the Ministry of Education, to NITE, and to the institution, and each institution computes a sekhem on its own formula, revised annually. An AI model can err or present an incorrect figure, so verify every date, amount and condition against the official source. This tool is not a substitute for advice that takes account of an individual's own circumstances and needs.


## Instructions

### Step 1: Identify the User's Goal

Work out which of four things the user needs: Bagrut planning (study units, subject requirements, magen), psychometric preparation (structure, scoring, registration, dates), university admissions (sekhem and requirements), or grade calculations (averages, subject grades, bonuses).

Ask before answering if it is unclear. A student choosing Bagrut subjects has very different needs from one estimating a sekhem for applications.

### Step 2: Bagrut (Matriculation) Exam System

The Bagrut (בגרות) is Israel's national matriculation exam system administered by the Ministry of Education. Students take exams during grades 10-12.

#### Where the Baseline Bends

Treat the formula and unit numbers here as the standard baseline and send the student to the Ministry's current-year subject document for deviations. Two are common: subjects assessed partly through alternative school-based assessment, where the school share can exceed 30%, and emergency accommodations for students from evacuated communities or with reservist parents. Both are set per subject and per year.

#### Bagrut Grade Formula

Each subject's final Bagrut grade is calculated as:

| Component | Weight | Description |
|-----------|--------|-------------|
| External exam (בחינה חיצונית) | 70% | The national Bagrut exam |
| Magen grade (ציון מגן) | 30% | Teacher's assessment based on classwork, attendance, behavior |

**Final Subject Grade** = (Exam Score x 0.7) + (Magen Score x 0.3)

**This formula does not apply to external examinees.** An extern has no school and therefore no magen: the externs regulations never use the word. Their subject grade is built from the weights of the questionnaires they sit (a single 100% paper in some subjects, 60/40 or 50/30/20 in others), so the exam carries the whole grade. For any post-army or self-study candidate this means they need a higher raw exam score to reach the same subject grade, and "protect your magen" is meaningless advice. In their favour: on a re-sit of the same questionnaire, the highest score achieved is the one that counts.

**70/30 is the majority rule, not a universal one.** Circular Hora'at Keva 0230 states that most subjects use 70/30 and that some publish a different split per subject; where alternative school-based assessment is heavy the school share can exceed 30%.

Do not assert a wartime "60% exam / 40% magen" option. A search of circulars 0230 and 0045 and the certificate-composition page found no support, and the page that once carried it no longer resolves. If a student was told about such a split, ask for the circular reference rather than confirming it.

#### Study Units (יחידות לימוד)

Each subject is studied at a level measured in study units (1-5 units). More units = deeper study.

Levels run 1 (minimal), 3 (standard for most subjects), 4 (extended) and 5 (advanced, required for competitive university programs).

**Minimum requirements for a Bagrut certificate:**
- Mandatory cores: Hebrew language and expression, Literature, Bible, History, Civics, English (3-5 units), Mathematics (3-5 units). Exact counts vary by sector and year; verify on the Ministry site.
- Minimum total: 21 study units, including at least one subject at the 5-unit (moogbar) level. **English at 5 units does not satisfy this requirement**: the Ministry excludes it, so the student needs another 5-unit subject.
- Passing grade: 55. See the compensation rule below for what happens when a grade falls short.
- Core units by sector: mamlachti 16, mamlachti-dati 20, atzmai/charedi 20, Arab 17, Druze 17.
- **Social involvement (מעורבות חברתית) is a condition of the certificate, not a grade.** A 180-hour programme across grades 10-12, recorded as a code from 1 to 4, not a mark. **Code 1 means no certificate at all**, however good the exam results.

#### Failing Grades and the Compensation Rule (כלל השיפוי)

Three separate reliefs, routinely confused:

- **One failing grade of 45-54** still leaves the student eligible, provided it is not in the mother-tongue subject (Hebrew for the Jewish sector, Arabic for the Arab and Druze sectors) and not in social involvement.
- **A grade of 01-04 is a chosem grade.** It forces a re-sit and is excluded from both the final subject grade and eligibility. Compensation cannot rescue it.
- **Compensation (kelal ha-shipuy) reaches lower.** A final grade of **05 to 44** in ONE subject only still yields a certificate, provided that grade is not in the mother tongue and the student's grades in two subjects at 3, 4 or 5 units reach a cumulative total:

| Unit combination | Required total of the two grades |
|---|---|
| 5 + 5 | 140 |
| 5 + 4 | 144 |
| 5 + 3 | 146 |
| 4 + 4 | 146 |
| 4 + 3 | 148 |
| 3 + 3 | 150 |

Check this first when a student believes one bad result cost them their certificate. It usually has not.

#### Bonus Points for 5-Unit Subjects

Students who take subjects at 5-unit level receive bonus points on their Bagrut average. Bonuses are flat per subject (not tiered by score) and require a minimum grade of 60 at every institution below. **There is no single national bonus table.** Quote the target university's own table, never a generic one:

Full verified tables are in `references/university-admission-guide.md`. Headline figures: 5-unit Mathematics is +30 at the Technion and +35 at TAU; 5-unit English is **+25 at both**; the Technion lifts Physics and Chemistry to +30 under a qualifying science/technology combination and counts Mathematics units double.

**Do not generalize a table across institutions.** The +12.5 for 4-unit English is a TAU figure; TAU does not name Computer Science in its +25 row, and awards nothing for a combination-of-subjects grade.

Universities also compute a **best (optimal) average**, dropping the subjects that pull it down. TAU's worked example moves from 97.81 to 108.39 by dropping three. The bundled calculator averages every subject, so treat its output as a floor.

Use `scripts/bagrut-calculator.py` to compute grades:

```bash
python scripts/bagrut-calculator.py --mode subject --exam 82 --magen 90
python scripts/bagrut-calculator.py --mode average --subjects "math:5:88,english:5:92,history:3:78,bible:3:80,hebrew:5:85,literature:3:76"
```

#### Magen Grade Details

The magen (מגן) grade is set by the school from in-class tests, assignments, attendance and participation, and the teacher's overall assessment.

**Special provisions:**
- New immigrants (olim chadashim) receive a points bonus on the standard written Hebrew-language Bagrut exam. **The level is set by the grade the student entered the Israeli school system in, not by their Hebrew proficiency** (circular Hora'at Keva 0045): level alef = arrived in grades 1-3, level bet = grades 4-8, level gimel = grades 9-12. The bonus is **+10 at level alef and +15 at levels bet and gimel**. Note that it runs counter to intuition, with the earliest arrivals receiving less. Separately, the external **English** written exam carries **+10 at all three levels**, except for students who came from countries where English is an official language.
- The bonus is added twice over: by the school to the annual grade, and automatically by the Exams Division to the exam grade. It applies only to regular Hebrew-language written papers, **not** to an oleh question paper, a bilingual paper, or an oral substitute, so the student picks one track. It also **does not apply to the 30% school-assessment component** or to alternative assessment.
- The benefit lasts 10 years from the date of aliyah or until age 23, whichever is later; Ethiopian immigrants are entitled for 12 years or until age 25, whichever is later. (Do not confuse the 10-year window with the separate 4-year continuous-absence rule that defines returning-resident status.)
- Students with learning disabilities may receive testing accommodations (extra time, oral exams) following a recognized diagnosis (see Step 5)

### Step 3: Psychometric Entrance Test (PET)

The Psychometric Entrance Test (מבחן פסיכומטרי, or "Psychometri") is administered by NITE (the National Institute for Testing and Evaluation, מרכז ארצי לבחינות ולהערכה, known in Hebrew as מאל"ב).

#### Test Structure

| Section | Content | Weight in Final Score |
|---------|---------|----------------------|
| Quantitative Reasoning (חשיבה כמותית) | Math, logic, data interpretation | 40% |
| Verbal Reasoning (חשיבה מילולית) | Reading comprehension, analogies, sentence completion | 40% |
| English (אנגלית) | Reading comprehension, vocabulary, sentence completion | 20% |

**Major change from the December 2026 session (winter, תשפ"ז):** English is removed from the psychometric test and assessed separately through NITE's standalone computerized English test (AMIRNET, part of NITE's AMIR English-test family). The psychometric general score becomes two-domain: Quantitative Reasoning and Verbal Reasoning only (within the verbal domain, the writing task counts for 25%).

**The weighting is published.** NITE states that in the two-domain general score the verbal and quantitative weights are **equal**. NITE also reports two emphasis scores alongside it: a quantitative-emphasis score weighting quantitative **three times** verbal, and a verbal-emphasis score weighting verbal three times quantitative. Faculties choose which of the three to use. (In the outgoing three-domain score, verbal and quantitative each carry double the weight of English, i.e. 40/40/20.)

The overall scale stays 200-800. Scores from the older three-domain format remain valid for their full 7 years.

#### What Happens to a Score Already Taken

The most common question from students holding a pre-December-2026 score.

- **NITE publishes a recomputed two-domain score for old sittings from October 2026**, in the personal area alongside the original.
- **At TAU**, from the תשפ"ח season as a **two-year pilot**: sat only the old format, you get the **higher** of the three-domain and recomputed two-domain scores; only the new format, the two-domain result; both, the highest of all three. Nobody is worse off for having sat the old exam there.
- **Do not assume other institutions match TAU.** Each decides independently and several had published nothing. Check the target institution before paying to re-sit.

#### Scoring

- General score **200-800**; each domain also scored **50-150**
- NITE states most departments require a score **close to the average, 550**, with only a few faculties such as medicine and law needing an exceptionally high one
- Scores are normed against all examinees since December 1983, so the session chosen does not affect the score
- Valid for admission **at least 7 years**. The period is set by the institutions, not NITE, so confirm with the target institution

Do not quote a standard deviation or percentile band: NITE publishes neither, and circulating figures are unsourceable.

#### Test Dates

The full published session table (dates, languages, registration-close and score-forecast dates) is in `references/university-admission-guide.md`. The published sessions are 2-3.9.2026, 4 and 6.12.2026, 18-19.4.2027 and 1.7.2027. Three things decide advice:

- **December 2026 is Hebrew and Arabic only**, on two non-consecutive days. A student needing Russian, French or the combined version cannot sit until April 2027.
- **The registration-close date is also the accommodations deadline, and NITE runs its own accommodations track.** A Ministry Bagrut accommodation does NOT carry over: NITE has a separate application ("bechina betnaim mutamim") and its own decision. A student assuming it transfers sits without extra time and cannot repair it, since the deadline passed months earlier and sessions run only a few times a year.
- NITE publishes a per-session score-forecast date, not a fixed turnaround, so never promise "results in 45 days". December 2026's forecast is 20.1.2027, 47 days out; check that against the target institution's registration deadline before recommending that session.

Sessions can be postponed for security or holiday reasons. Confirm against `https://www.nite.org.il/test-dates-and-prices/`.

#### Registration

1. Register online at the NITE website (`https://www.nite.org.il`)
2. **There are two fee tables and the reform makes the test cheaper**: standard registration is 665 NIS for the three-domain test through September 2026 and **495 NIS** for the two-domain test from December 2026. The late, same-day and date-change tiers move with it; the full table is in `references/university-admission-guide.md`. Quote the table matching the student's test date, not the one you remember. Late and same-day registration are not offered at every session, and changing the date is free while registration is still open.
3. NITE publishes a single registration-close date per session (see the table above), not an open date and a separate late-registration deadline. Do not state deadlines it has not published.
4. Test versions currently published are Hebrew, Arabic, Russian, French and combined Hebrew-English. **No currently published session offers a Spanish version**, so do not tell a student one exists.
5. Results: read the per-session score-forecast date from the test-dates table
6. No early-registration discount appears on NITE's fee tables, which list only registration and date-change items. Score reporting to institutions is done from the personal area

#### Available Languages

Hebrew (standard), Arabic, Russian, French, and a combined Hebrew-English version in which an English verbal section replaces the Hebrew one. Which of these is offered varies BY SESSION: December 2026 is Hebrew and Arabic only. No currently published session offers Spanish.

#### The Standalone English Test (AMIRNET)

From December 2026 this, not the psychometric, establishes a candidate's university English level. Full detail (scale, fee, equivalence to AMIR and AMIRAM, retake interval) is in `references/university-admission-guide.md`. Two points must be said out loud to anyone sitting from December 2026:

- **AMIRNET is a separate registration and a separate fee.** Sitting the two-domain psychometric leaves the candidate with NO English score and no university English placement until they book AMIRNET as its own test on its own date. A candidate who discovers this late cannot always fix it quickly: NITE requires at least 35 days between AMIRNET sittings.
- **NITE publishes no exemption (patur) threshold table.** Each institution decides what score exempts a student and at what level, and NITE warns that one institution's decision does not bind another. Never quote a universal patur cutoff.

### Step 4: University Admission Score (Sekhem)

The sekhem (ציון סכם) is the combined score used by Israeli universities for admissions decisions. It merges the Bagrut average with the Psychometric score.

#### How Sekhem is Calculated

**There is no national 40/60 split, and you should not state one.** Tel Aviv University says outright that its weighting formula changes from year to year and publishes a linear transformation rather than a percentage split; the Technion publishes formulas per faculty; the Hebrew University publishes no weighting numbers at all. The honest answer to "what is the formula?" is: per-institution, per-faculty, revised annually. Send the student to the target institution's own sekhem calculator and treat any number this skill produces as a rough orientation figure. Specific programmes (medicine, law, engineering, computer science) add their own thresholds on top. Detail in `references/university-admission-guide.md`.

#### Sekhem Optimization Strategy

On the Bagrut side: take 5-unit subjects that carry a bonus at the target institution, clear grade 60 in each (below it the bonus is zero, so a 59 and a 61 are far further apart than two points), and protect the magen, which is 30% of every subject grade for a school student. On the psychometric side, put preparation into the weakest domain, where the marginal point is cheapest. A weak first result is often recoverable by re-sitting, but do not tell a student that re-sitting is free or unlimited: NITE sets its own rules on repeat sittings, and whether an institution takes the best of several scores is that institution's policy, not a national rule. Check both before advising a re-sit.

#### Deciding Between the September 2026 and December 2026 Sittings

This is the live decision for anyone sitting in this window, and it turns on four things already established above.

1. **How strong is their English?** In the outgoing format English is 20% of the general score. From December it is worth nothing there. A candidate whose English is far stronger than their verbal and quantitative loses that lever by waiting; a candidate whose English is their weak spot gains by waiting.
2. **What language do they need?** December 2026 is Hebrew and Arabic only. A candidate needing Russian, French or the combined version cannot sit until April 2027, whatever they would prefer.
3. **When does the score have to be in hand?** The December session's scores are forecast for 20.1.2027. Check that date against the target institution's own registration deadlines before choosing it, since a score that arrives after the deadline is worth nothing that cycle and the next session is in April.
4. **Have they checked their institution's transition rule?** Only Tel Aviv University had published one at the time of writing, and it protects the candidate by taking the higher score. Do not assume another institution does the same.

Whichever they choose, from December onward AMIRNET is a separate registration and a separate fee.

Use `scripts/bagrut-calculator.py` to estimate the sekhem:

```bash
python scripts/bagrut-calculator.py --mode sekhem --bagrut-avg 95.5 --psychometric 680 --bagrut-weight 40 --psychometric-weight 60
```

### Step 5: Rights, Retakes, and Accommodations

Statutory rights administered by the Ministry, commonly needed and easy to miss. The full table is in `references/university-admission-guide.md`. The points that most often decide an outcome:

- **Moed bet is a summer mechanism only, and only in English, Mathematics and mother tongue.** Winter has none. In the תשפ"ז summer draft it falls on 5-8 July 2027. A student who fails a subject with no moed bet waits for a whole further session, which can push the certificate past graduation and disturb army-deferral planning, so say that consequence rather than just the rule.
- **Appeal windows differ by track**: 30 days from publication of the official grade for school students, 21 days for external examinees. The grade can go up, stay the same, or go **down**, so this is a real decision. An extern should request the scanned booklet immediately, no later than 10 days after publication, and then has up to 11 days from receiving it to file.
- **Learning-disability accommodations** need a recognised diagnosis and must be applied for through the school well before the exam. **A Ministry accommodation does not transfer to NITE**, which runs its own separate application (see Step 3).
- **Miluim accommodations are granted on application**, through an exceptions committee, scaled by service length and proximity to the exam. A student who does not apply gets nothing. If a psychometric session is missed because of a call-up, ask NITE about a date change rather than forfeiting the fee.
- **Deadlines for external examinees**: opening an examinee file runs 1 September to 20 November for winter and 1 February to 20 March for summer. These are the EXTERNS' windows; a school student registers through the school on its own timetable. Minimum age to sit is 16 years and 2 months. Approving an accommodation is not the same as arranging it: the regulations say a committee decision does not by itself secure implementation.
- **The 2026/27 (תשפ"ז) exam calendar is published in draft**, dated 12/07/2026 and expressly subject to change. Winter runs 27.12.2026 to 4.2.2027, summer 25.4.2027 to 9.7.2027. Read the subject date off the Ministry's current timetable rather than quoting it from here.

Always check the Ministry's student portal and Kol Zchut for current-year deadlines and forms.

### Step 6: Key Terms Reference

A bilingual glossary of the terms used on Ministry, NITE and university pages is in `references/bagrut-subjects-and-units.md`. Search official sites with the Hebrew term; the English one usually returns nothing.

## Examples

### Example 1: Calculate Bagrut Subject Grade

User says: "I got 78 on my math Bagrut exam and my magen is 85. What's my final grade?"

Actions:
1. Apply the formula: (78 x 0.7) + (85 x 0.3) = 54.6 + 25.5 = 80.1
2. Since math is typically 5 units and the grade is above 60, the flat bonus applies. The exact bonus depends on the target university (typically +30 at the Technion, +35 at Tel Aviv University for 5-unit math).
3. Run: `python scripts/bagrut-calculator.py --mode subject --exam 78 --magen 85`

Result: Final subject grade is 80.1. When calculating the Bagrut weighted average for university admission, this subject receives the university's flat bonus (e.g., 80.1 + 30 = 110.1 at the Technion). Check the target university's bonus table for the exact value.

### Example 2: Plan Psychometric Preparation

User says: "I'm taking the psychometric in July. My practice test scores are: Quantitative 130, Verbal 105, English 120. How should I prepare?"

Actions:
1. On the 50-150 domain scale, Verbal at 105 is the weak spot.
2. Compare the two formats, which is the decision this student actually faces. Outgoing three-domain weighting (verbal and quantitative each double English, i.e. 40/40/20): (130 x 0.4) + (105 x 0.4) + (120 x 0.2) = 118. From December 2026, English does not count and the two remaining domains are weighted **equally**: (130 + 105) / 2 = 117.5. For this student the formats are near-identical, so the choice turns on timing, not scoring. **Run this comparison every time**, because it flips: a student at English 140 and verbal 105 loses real ground by waiting, and a student with weak English gains. NITE publishes no conversion from domain scores to the 200-800 general score, so do not assert one.
3. Direct study to Verbal Reasoning, where the marginal point is cheapest.

Result: a targeted plan prioritising verbal reasoning, plus an explicit September-versus-December recommendation for this student's score profile.

### Example 3: Estimate University Admission Score

User says: "My Bagrut average is 98 and my psychometric is 720. Can I get into computer science at the Technion?"

Actions:
1. Do NOT produce a number and present it as an admission score. The Technion publishes formulas per faculty and no bagrut/psychometric percentage split, so any figure computed here is on an invented scale. The calculator now refuses to run sekhem mode unless the caller supplies weights explicitly, precisely so the assumption is visible.
2. Say that Technion CS is among the most competitive programmes in the country, and refuse to quote a cutoff: the Technion publishes none, and a number recalled from training data is unsourced.
3. Route the applicant to the Technion's own sekhem calculator for the specific faculty, and to its bonus table, noting that mathematics units count double there.

Result: no fabricated score. The applicant leaves with the right tool and the right question, rather than a number that feels authoritative and is not. If the user wants to improve their chances, retaking the psychometric (aiming for 740+) would be the most effective strategy since the Bagrut is already excellent.

## Bundled Resources

### Scripts
- `scripts/bagrut-calculator.py` - subject grades, weighted averages with per-institution bonuses (`--institution technion|tau`), and an admission-score estimate that requires explicit weights. `--help` for usage.

### References
- `references/bagrut-subjects-and-units.md` - subjects, unit levels, mandatory vs elective status, bonus rules, and the bilingual glossary.
- `references/university-admission-guide.md` - verified bonus tables, PET session and fee tables, AMIRNET, the full rights table, and the Dec-2026 transition.

## Gotchas

- The Israeli academic year runs October-July, so agents misplace exam scheduling and application deadlines.
- The PET scale is 200-800, not the SAT's 200-1600. Confusing them produces wildly wrong comparisons and admission estimates.
- Bonus points are flat per subject (not tiered by score), but vary by institution and there is no national table. Agents emit one universal figure. Concretely: 5-unit English is +25 at BOTH the Technion and TAU, not the "+20 for humanities" commonly assumed; 4-unit English at +12.5 is a TAU number and wrong elsewhere.
- Universities compute a **best (optimal) average** that drops weak subjects. An agent averaging every subject understates the applicant, sometimes by ten points or more.
- Each institution calculates the sekhem on its own formula, revised annually and often per faculty. An agent assuming a universal formula produces a confident wrong number. Route to the institution's calculator.
- Two psychometric fee tables are live at once, and the reform makes the test **cheaper**: 665 NIS through September 2026, 495 NIS from December 2026, with the whole ladder moving.
- NITE publishes no standard deviation, no percentile band and no fixed results turnaround. Agents state all three confidently; none is sourceable. NITE publishes an average of 550 and a per-session forecast date.
- From the December 2026 (winter תשפ"ז) session, English is removed from the psychometric and tested separately via NITE's computerized English test (AMIRNET), and the general score is based on the quantitative and verbal domains only, weighted **equally**. Agents trained on the older three-section (40/40/20) structure will describe the wrong test for students sitting from that date onward, and agents that say "the weighting has not been announced" are also out of date. Older three-domain scores remain valid for 7 years, and NITE publishes a recomputed two-domain score for them from October 2026.
- The Bagrut passing grade is 55; the minimum grade earning a university bonus is a separate threshold of 60. Agents conflate them.
- The new-immigrant Bagrut benefit lasts 10 years from aliyah (or until age 23, whichever is later; 12 years or until age 25 for Ethiopian immigrants). The 4-year figure belongs to returning-resident status, a different entitlement.
- The oleh bonus level is set by the **grade the student entered Israeli school in** (1-3, 4-8, 9-12), not by current Hebrew proficiency. Agents read "level alef/bet/gimel" as a language level and route a fluent late arrival to the wrong row. The values run counter to intuition too: earliest arrivals get +10, later arrivals +15.
- Moed bet exists only in summer and only for English, Mathematics and mother tongue. An agent offering a winter moed bet in Biology is inventing a sitting.
- External examinees have NO magen, so their exam carries 100% of the subject grade. An agent applying 70/30 to an extern, or telling them to protect their magen, is describing a mechanism they do not have.


## Reference Links

| Source | URL | What to Check |
|--------|-----|---------------|
| Ministry of Education - certificate composition | https://exams.education.gov.il/certificates/composition-of-certificate/ | The 70/30 exam-to-school split and how a subject grade is built |
| Ministry of Education - certificate eligibility | https://exams.education.gov.il/certificates/eligibility-for-matriculation-certificate/ | 21-unit minimum, the 5-unit requirement, failing grades, per-sector core units |
| Circular Hora'at Keva 0230 | https://apps.education.gov.il/Mankal/horaa.aspx?siduri=285 | Authoritative source for the 70/30 weighting and the subjects that deviate from it |
| Circular Hora'at Keva 0045 | https://apps.education.gov.il/Mankal/horaa.aspx?siduri=83 | New-immigrant levels, the point bonuses, and the duration rules |
| NITE (Psychometric Entrance Test) | https://www.nite.org.il/en | Test dates, registration, preparation materials |
| NITE - two-domain psychometric (Dec 2026) | https://www.nite.org.il/two-domain-psychometric-entrance-test/ | The Dec-2026 reform, and the two-domain fee table (495 NIS) |
| NITE - two-domain score calculation | https://www.nite.org.il/two-domain-psychometric-entrance-test/scores/calculation/ | The equal verbal/quantitative weighting and the two emphasis scores |
| NITE - AMIRNET | https://www.nite.org.il/other-tests/amirnet/ | The standalone English test: 50-150 scale, fee, equivalence to AMIR/AMIRAM |
| Technion - bonus coefficients | https://admissions.technion.ac.il/calculation-of-the-median-grade/ | The Technion's own 5-unit bonus table and the double-weighting of Mathematics |
| Tel Aviv University - computing the average | https://go.tau.ac.il/b.a_direct/how-to-calculate | TAU's bonus table, the best-average method, and the adaptation-score formula |
| Tel Aviv University - Dec 2026 psychometric change | https://go.tau.ac.il/he/psychometric-test | How TAU treats an existing three-domain score under the reform |
| Council for Higher Education | https://che.org.il/en/ | Accredited degree programs |
| Kol Zchut - bagrut rights | https://www.kolzchut.org.il/he/בחינות_בגרות | Retake rights, appeals, accommodations, foreign-diploma recognition |
| Externs regulations (PDF) | https://meyda.education.gov.il/files/Exams/TakanonExterni092025NEW.pdf | Extern registration windows, appeal window, questionnaire weights, chosem grades |

## Troubleshooting

### Error: "My calculated Bagrut average doesn't match my school's number"

Cause: schools and universities include different subjects and apply bonuses differently; universities also build a best average rather than a straight one.

Solution: check which subjects are in scope, check whether bonuses were applied, treat the official Ministry certificate as authoritative for the grades themselves, and expect each university to recalculate on its own formula.

### Error: "The sekhem I calculated doesn't match the university's calculator"

Cause: institutions use their own formulas, with subject bonuses, rounding rules and normalization that a simple weighted average cannot reproduce. TAU, for instance, applies a two-stage linear transformation that is revised annually.

Solution: use the institution's own calculator; treat this skill's number as orientation only; contact the admissions office for an exact figure.

### Error: "I sat the old psychometric. Is my score worthless now?"

Cause: the December 2026 reform removes English from the test, so a three-domain score no longer matches the new structure.

Solution: (1) Existing scores remain valid for their full validity period. (2) From October 2026 NITE shows a recomputed two-domain score for old sittings in the personal area, alongside the original. (3) At Tel Aviv University the higher of the two is used (and the highest of three if the student also re-sits), as a two-year pilot from the תשפ"ח season. (4) **Verified negative: this is not a universal rule.** Other institutions decide independently and several had published nothing, so do not tell the student every university will take the better score. Have them confirm with their target institution before paying to re-sit.

### Error: "I don't know my magen grade yet"

Cause: magen grades are finalized close to the exam date and are often unavailable during planning.

Solution: estimate from recent in-class test averages, run several scenarios to see the range, and keep improving classwork, since the magen is 30% of the final grade.
