---
name: israeli-bagrut-psychometric
description: Guide users through Israel's Bagrut matriculation exams and Psychometric entrance test (PET) system. Use when user asks about bagrut study units, psychometric scores, exam structure, university entrance requirements, sekher calculation, or study planning. Covers the Bagrut grading formula (70% exam + 30% magen), PET scoring (200-800), NITE registration, test dates, and strategies for maximizing combined admission scores (sekhem). Prevents confusion between the many overlapping terms and formulas in the Israeli higher-education admissions process. Do NOT use for university-specific admission thresholds, post-secondary academic advising, or non-Israeli education systems.
license: MIT
allowed-tools: Bash(python3:*) Read
compatibility: Requires Claude Code or compatible AI coding agent
---


# Israeli Bagrut & Psychometric Guide

## Instructions

### Step 1: Identify the User's Goal

Determine what the user needs help with:

1. **Bagrut planning** - understanding study units, subject requirements, magen grades
2. **Psychometric preparation** - exam structure, scoring, registration, test dates
3. **University admissions** - calculating sekhem (combined admission score), understanding requirements
4. **Grade calculations** - computing Bagrut average (sekher), subject grades, bonus points

Ask clarifying questions if the goal is unclear. A student planning their Bagrut subjects has very different needs from one calculating their sekhem for university applications.

### Step 2: Bagrut (Matriculation) Exam System

The Bagrut (בגרות) is Israel's national matriculation exam system administered by the Ministry of Education. Students take exams during grades 10-12.

#### Recent Reform (2024-25)

The Bagrut underwent significant changes during the 2024-25 school year (תשפ"ה). Key shifts students should be aware of:

- **English Bagrut "matzav 2"** continues as the standard format, with the modular structure (oral, listening, reading, writing) replacing the older single-exam approach. Students assemble units across grades 10-12.
- **5-yedaot (5-unit) requirements** were partially relaxed for select subjects following pandemic-era and wartime adjustments. Some subjects now allow alternative magen pathways or project-based components in place of part of the external exam. Always verify per-subject rules on the Ministry of Education's current-year exam page (`https://exams.education.gov.il/certificates/eligibility-for-matriculation-certificate/`).
- **Oral and project components** count toward more subjects, not only languages. The 70/30 exam-to-magen split remains the Ministry's stated standard (a 2026 wartime accommodation package may shift it in the student's favour, see the formula section). Do NOT tell a student the exam component has become "a portfolio of mini-exams and project work": the Ministry's certificate-composition page still frames the structure around the תשע"ז framework and states 70/30 flatly, and no primary source was found for a structural move to portfolio assessment. The 2026 flexibility is a wartime accommodation, not a reform of the system.
- **Wartime and emergency accommodations** introduced in 2023-24 (extended deadlines, oral substitutions for written exams, makeup sessions) carried into 2024-25 for students from evacuated communities or with reservist parents. Students should ask their school counselor whether they qualify.

When in doubt, treat the formula and unit numbers in this skill as the standard baseline and direct the student to the Ministry's current-year subject page for any subject-specific deviations.

#### Bagrut Grade Formula

Each subject's final Bagrut grade is calculated as:

| Component | Weight | Description |
|-----------|--------|-------------|
| External exam (בחינה חיצונית) | 70% | The national Bagrut exam |
| Magen grade (ציון מגן) | 30% | Teacher's assessment based on classwork, attendance, behavior |

**Final Subject Grade** = (Exam Score x 0.7) + (Magen Score x 0.3)

**Wartime accommodation (2026):** a relief package exists for cohorts affected by the war, and it has several operative parts.

The package is reported to shift the exam-to-magen ratio, and to carry regional grade uplifts, an internal-for-external substitution in some humanities subjects, and a lowered minimum in at least one subject.

**This skill states no figure for any of them, deliberately.** The Ministry's page could not be reached on any route tried, so every specific number previously carried here was removed rather than repeated unsourced. Never quote a ratio, an uplift, a substituted subject or a lowered pass mark from memory. Tell the student the package exists and send them to the current-year directive or the school counsellor to confirm the entitlement and its direction. Telling a student they qualify for a relief they do not have is the worst outcome available here.

#### Study Units (יחידות לימוד)

Each subject is studied at a level measured in study units. The Ministry's range across subjects is **2 to 5 units**, not 1 to 5; one unit is roughly 90 hours of study and 5 units is at least 450.

| Units | Level | Description |
|-------|-------|-------------|
| 2 units | Basic | Minimum level at which a subject is offered |
| 3 units | Standard | Standard level for most subjects |
| 4 units | Extended | Above average depth |
| 5 units | Advanced (מוגבר) | Highest level, required for competitive university programs |

**Minimum requirements for a Bagrut certificate:**
- Mandatory cores. **In state education they total 16 units**: Tanakh 2, Literature 2, History 2, Hebrew 2, Civics 2, Mathematics 3, English 3. That is what makes the 21 make sense: 16 plus a 5-unit moogbar is exactly 21, so the moogbar is a floor, not a preference. Other sectors differ (state-religious 20, Arab 17, Druze 17, Haredi 20); verify per sector on the Ministry page.
- Minimum total: 21 study units, including at least one subject at the 5-unit (מוגבר) level. **A 5-unit English does NOT satisfy the one-moogbar requirement**, which is the single most common planning error: a student who takes English at 5 and everything else at 3 or 4 is not eligible.
- **A cap, not just a floor.** At most **3 subjects at 5 units**, excluding English and Mathematics. "Take as many 5-unit subjects as you can for the bonus" is not executable advice.
- **Internal subjects (מקצועות פנימיים) are a condition of eligibility**, assessed by the school rather than by external exam, and they are where eligibility is quietly lost: two general-education subjects at 30 hours each; מבוא למדעים at 90 hours, waived for two 5-unit sciences; physical education; and **מעורבות חברתית**, where code 1 means no certificate at all whatever the exam results.
- Passing grade is 55, but a certificate is **not** lost to a single failure. See below.

#### Failing grades, and the compensation rule (כלל השיפוי)

Two separate reliefs, routinely confused:

- **One failing grade of 45-54** still leaves the student eligible, provided the failure is not in the mother-tongue subject (Hebrew for the Jewish sector, Arabic for the Arab and Druze sectors) and not in מעורבות חברתית.
- **A grade of 01-04 is a "ציון חסם".** It forces a re-sit and is excluded from the final subject grade and from eligibility. Compensation cannot rescue it.
- **כלל השיפוי (compensation)** reaches lower. A final grade between **05 and 44** in ONE subject only still yields a certificate, provided that grade is not in the mother-tongue subject, and provided the student's grades in two subjects at 3, 4 or 5 units reach the cumulative total for that unit combination:

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

Students who take subjects at 5-unit level receive bonus points on their Bagrut average. Bonuses are flat per subject (not tiered by score), but require a minimum grade of 60. Each university sets its own bonus amounts. Common values:

**A 4-unit bonus exists.** Do not tell a 4-unit student there is none; that is wrong at every institution checked.

| Subject | Units | Technion | Tel Aviv University |
|---|---|---|---|
| Mathematics | 5 | +30 | +35 |
| Physics, Chemistry | 5 | +25, or **+30** in the science bundle below | +25 |
| Biology | 5 | +25 | +25 |
| English, Literature, Bible, History, Arabic | 5 | **+25** | **+25** |
| Recognised technology subjects | 5 | +25, dropping to +20 inside the science bundle | see the eligible list |
| Other bonus-eligible subjects | 5 | +20 | +20 |
| Mathematics, English | 4 | not published in the Technion table | **+12.5** |
| Other bonus-eligible subjects | 4 | not published in the Technion table | **+10** |

Only "other subjects" is +20 at the Technion; English and the humanities named above are +25 there, the same as at TAU. The Technion's published table has **no 4-unit row**, so do not state a Technion 4-unit figure. TAU's table applies its values to an exam **or a recognised גמר paper** at the same unit level.

**The Technion science bundle.** With 5-unit mathematics plus two 5-unit sciences (or one science and one recognised technology subject), physics and chemistry pay **+30** instead of +25. Biology stays at 25 and technology subjects drop to 20 inside the bundle. Mathematics is also double-weighted in the Technion's average for most programmes.

A subject must be on the institution's bonus-eligible list; a bonus applied to an ineligible subject silently inflates the whole average.

**Important:** The bonus is a flat per-subject amount set by each university (it is NOT tiered by your score). It is awarded only if the subject grade is at least 60. The amount varies by university and subject: for example, the Technion awards +30 for 5-unit Math and +25 for the sciences, while Tel Aviv University awards +35 for 5-unit Math. Always check the target university's admissions page for its exact bonus table. The bonus is added to the subject grade when calculating the Bagrut weighted average.

Use `scripts/bagrut-calculator.py` to compute grades:

```bash
python3 scripts/bagrut-calculator.py --mode subject --exam 82 --magen 90
python3 scripts/bagrut-calculator.py --mode average --subjects "math:5:88,english:5:92,history:5:78,bible:3:80,literature:3:76"
```

#### Magen Grade Details

The magen (מגן) grade is determined by the school and considers:
- In-class test scores throughout the year
- Homework and assignments
- Attendance and participation
- Teacher's overall assessment

**Special provisions:**
- New immigrants (olim chadashim) receive a Hebrew-proficiency-based bonus when sitting the standard Hebrew written Bagrut exam: +10 points at basic Hebrew level (alef) or +15 points at levels bet/gimel. The bonus is not added on top of an adapted oleh question paper, a bilingual exam, or an oral substitute, so a student chooses one accommodation track. The benefit lasts 10 years from the date of aliyah or until age 23, whichever is later; Ethiopian immigrants are entitled for 12 years or until age 25, whichever is later. (Do not confuse the 10-year window with the separate 4-year continuous-absence rule that defines returning-resident status.)
- Students with learning disabilities may receive testing accommodations (extra time, oral exams) following a recognized diagnosis (see Step 5)

### Step 3: Psychometric Entrance Test (PET)

The Psychometric Entrance Test (מבחן פסיכומטרי, or "Psychometri") is administered by NITE (the National Institute for Testing and Evaluation, מרכז ארצי לבחינות ולהערכה, known in Hebrew as מאל"ו).

#### Test Structure

Which structure applies depends on the sitting. **From the December 2026 sitting the test is two-domain**; sittings up to and including September 2026 are three-domain.

**Three-domain PET** (to September 2026): 9 sections, a writing task of 30 to 35 minutes depending on test language plus 8 multiple-choice sections of exactly 20 minutes. Only 6 MC sections are scored; two are unidentifiable pilot sections.

**Two-domain PET** (from December 2026): 6 sections, the writing task plus 5 MC sections of which 4 are scored. About two and a half hours.

There is no single "weight in the final score": NITE reports several general scores computed from different weightings of the same domains.

| Score | Three-domain weighting | Two-domain weighting (from Dec 2026) |
|---|---|---|
| Multi-domain (רב-תחומי), the general score | Verbal 40%, Quantitative 40%, English 20% (verbal and quantitative each carry double English's weight) | **Quantitative 50%, Verbal 50%** |
| Quantitative emphasis (דגש כמותי) | Quantitative carries three times each other score (60/20/20) | Not applicable, ask NITE for the current set |
| Verbal emphasis (דגש מילולי) | Verbal carries three times each other score (60/20/20) | Not applicable, ask NITE for the current set |

Faculties choose which they use, so a candidate's "psychometric score" is not one number. Engineering and exact sciences typically read the quantitative-emphasis score, humanities and law the verbal-emphasis one.

**Major change from the December 2026 session (winter, תשפ"ז):** English is removed from the psychometric test and assessed separately through NITE's standalone computerized English test (AMIRNET, part of NITE's AMIR English-test family), offered year-round. The psychometric general score becomes two-domain: Quantitative Reasoning and Verbal Reasoning only. **NITE has published the weighting: quantitative 50 percent and verbal 50 percent.** Within the verbal domain the writing task counts for 25 percent and the two closed MC sections for 75 percent. The overall scale stays 200-800 and each domain is reported on 50-150. Scores from the older three-domain format remain valid for their full 7 years. From this session the "combined Hebrew-English" version is also affected. Confirm the exact structure for your test date on the NITE site.

#### Scoring

- Scale: **200-800** (multiscale scoring)
- Mean score: **550**. NITE states that most departments require a score close to the mean, and that only a small number, such as medicine and law, require an exceptionally high one
- Standard deviation: commonly cited as about 100, but **this figure appears on no NITE page found**. Present it as a rule of thumb if at all, never as a published statistic, and do not derive score bands from it
- Each section also receives its own score on the 50-150 scale
- Scores are valid for university admission for **at least 7 years** from the test date, old three-domain and new two-domain formats alike

#### Test Dates

NITE publishes a **closing date**, not an opening date, and the accommodations-request deadline is the SAME date. Sittings verified on the NITE calendar:

| Sitting | Dates | Languages | Registration closes | Format |
|---|---|---|---|---|
| Autumn 2026 | 2-3.9.2026 | Hebrew, Arabic | 8.7.2026 (closed) | Three-domain, the last one |
| Winter 2026 | 4 and 6.12.2026 | Hebrew, Arabic | **14.10.2026** | **First two-domain** |
| Spring 2027 | 18-19.4.2027 | Hebrew, Arabic, combined-English, Russian, French | 10.2.2027 | Two-domain |
| Summer 2027 | 1.7.2027 | Hebrew, Arabic, combined-English, Russian, French | 13.5.2027 | Two-domain |

Dates shift and can be postponed, so always re-check `https://www.nite.org.il/test-dates-and-prices/`. Re-verify this table each cycle; it is the first thing here that goes stale.

#### Registration

1. Register online at the NITE website (`https://www.nite.org.il`)
2. Work backwards from the **closing** date for the sitting, not from an opening date. The accommodations request is due on the same day, so a student needing accommodations has no extra time
3. Fee: **665 NIS** for the September 2026 sitting. NITE had not published the fee for the December 2026, April 2027 or July 2027 sittings at the time of writing, so quote 665 as the September figure and send the student to the price page rather than presenting it as the standing fee
4. The test is offered in **five languages: Hebrew, Arabic, Russian, French, and the combined-English version.** Not every language is offered at every sitting, and the non-Hebrew, non-Arabic versions run in only some test regions
5. Score-reporting is on a published forecast date per sitting (September 2026 to 18.10.2026; December 2026 to 20.1.2027), not a rolling 45 days
6. Late registration, cancellation and date changes each carry their own surcharge or forfeit, on a schedule that depends how close to the closing date you are. The figures are in `references/nite-tests-and-procedures.md`

#### Available Languages

There are **five** test languages. Spanish is NOT one, and telling a Spanish-speaking oleh he can sit in Spanish is a live error: Spanish appears only as a glossary-translation language inside the combined-English booklet, and as a language the writing task may be written in there.

Hebrew and Arabic run at every sitting. Russian and French do not, and run only in some regions. The combined-English version is for native English speakers and for anyone whose Hebrew or English beats the other test languages: it is presented in English and Hebrew, glosses harder words into eight further languages, and its booklet is laid out left to right.

The writing task must be in the language of the test. In the combined-English version it may be in any of that version's languages; an essay in another language is disqualified and scored lowest.

**YAEL comes free with a non-Hebrew sitting.** A candidate sitting in any language other than Hebrew, the combined-English version included, may sit the YAEL Hebrew-knowledge test straight afterwards at no extra charge (accommodated candidates get YAELNET instead). The YAEL score is never part of the psychometric score and is reported separately.

### Step 4: University Admission Score (Sekhem)

The sekhem (ציון סכם) is the combined score used by Israeli universities for admissions decisions. It merges the Bagrut average with the Psychometric score.

#### How Sekhem is Calculated

**Do not present the sekhem as a 40/60 blend of the two.** That table used to appear here for all six universities and no institution's published formula was found to support it. Real formulas are affine transformations with their own coefficients and caps, not percentage weights, so a 40/60 estimate can be off by a wide margin and cannot be compared across institutions.

Two verified examples of how different they actually are:

- **Tel Aviv University** publishes a ציון התאמה of the form `((9.62 x adapted bagrut average - 349.9) + PET) x 0.52 - 43.10`, with the bagrut average **capped at 117**. There is no 40/60 anywhere in it, and the cap means bonus points stop helping past a point.
- **Hebrew University** computes an **optimal** average, selecting the elective subjects that improve the result rather than averaging everything the student sat.

So: never quote a cross-university weighting, never present a sekhem on a 0-100 scale as though institutions produce one, and send the student to the target institution's own calculator. The Ministry of Education does not publish a sekhem; each institution does.

**Exemptions and the new English test:** Many universities exempt older applicants (commonly age 27-30+) and holders of a prior academic degree from the psychometric, admitting on the Bagrut alone. Faculties may also use a domain-weighted psychometric score (favoring quantitative or verbal) rather than the general score. From December 2026, the separate AMIRNET English score (not the psychometric) determines a student's university English placement and exemption level (patur). Confirm the rules with each institution.

#### Sekhem Optimization Strategy

To maximize the sekhem:

1. **Bagrut optimization:**
   - Take as many 5-unit subjects as possible for bonus points
   - Focus on magen grades (they are 30% of each subject grade)
   - Score above 60 in 5-unit subjects to qualify for bonus points

2. **Psychometric optimization:**
   - Can retake the PET multiple times (universities use the best score)
   - Invest in preparation courses (typically 3-6 months of study)
   - Focus on weakest section for maximum score improvement

3. **Combined strategy:**
   - If Bagrut average is high but psychometric is low, retake the PET
   - If psychometric is high but Bagrut is lower, explore programs that weight psychometric more heavily
   - Some programs accept psychometric-only track for exceptional scores (typically 700+)

Use `scripts/bagrut-calculator.py` for the **bagrut average**, which is a real computation. Its `sekhem` mode is an illustrative blend only, and the script itself says so in its output; do not present that number to a user as an admission score.

```bash
python3 scripts/bagrut-calculator.py --mode average --subjects "math:5:88,english:5:92,history:5:78,bible:3:80,literature:3:76"
```

### Step 5: Rights, Retakes, and Accommodations

Beyond grades and scores, students have a layer of statutory rights administered by the Ministry of Education. These are commonly needed and easy to miss.

| Right | Details |
|-------|---------|
| Retake / grade improvement (moed bet, mo'ed meyuchad) | A student can re-sit a Bagrut exam to improve a grade; the higher grade counts. Special sessions exist for students who missed an exam for an approved reason (illness, bereavement, reserve duty). Improvement re-sits are available even after finishing school (as an external examinee). |
| Appeal a school (magen) grade | A student may appeal the summary school grade (irur al tziun beit-sifri mesakem) through the school and district, within the published window. |
| Appeal / exam-integrity review | Separate procedures exist if a student is suspected of an exam-integrity violation, with a right to a hearing. |
| Learning-disability accommodations | Students with a recognized diagnosis (ikui lemida) can receive accommodations: extra time, separate room, oral exam, reader/scribe, spelling leniency. Funding support for the diagnosis itself may be available. Apply through the school well before the exam. |
| Reserve-duty (miluim) accommodations | A special exceptions committee sets accommodations (extended deadlines, special sessions, magen adjustments) for students or those whose parents served, scaled by service length and proximity to the exam. War-period frameworks expand these. |
| New-immigrant / returning-resident adaptations | Beyond the Hebrew-level bonus, olim get adapted exam papers, extra time, and dictionary use for a defined period (see Step 2). |

When advising a student, always check the Ministry of Education student portal and Kol Zchut for the current-year deadlines and forms, since these accommodations are time-bound.

### Step 6: Key Terms Reference

| Hebrew Term | Transliteration | English |
|-------------|----------------|---------|
| בגרות | Bagrut | Matriculation exams |
| ציון מגן | Tziun Magen | School-based grade (teacher assessment) |
| יחידות לימוד | Yechidot Limud | Study units (2 to 5 across subjects) |
| ממוצע בגרות | Memutza Bagrut | Bagrut GPA / weighted average |
| פסיכומטרי | Psychometri | Psychometric entrance test (PET) |
| מאל"ו (מרכז ארצי לבחינות ולהערכה) | MALAV / NITE | National Institute for Testing and Evaluation |
| ציון סכם | Tziun Sekhem | Combined admission score |
| חשיבה כמותית | Chashiva Kamutit | Quantitative reasoning |
| חשיבה מילולית | Chashiva Milolit | Verbal reasoning |
| נקודות בונוס | Nekudot Bonus | Bonus points (for 5-unit subjects) |
| תעודת בגרות | Te'udat Bagrut | Bagrut certificate |
| עולה חדש/חדשה | Oleh/Olah Chadash/Chadasha | New immigrant |

## Examples

### Example 1: Calculate Bagrut Subject Grade

User says: "I got 78 on my math Bagrut exam and my magen is 85. What's my final grade?"

Actions:
1. Apply the formula: (78 x 0.7) + (85 x 0.3) = 54.6 + 25.5 = 80.1
2. Since math is typically 5 units and the grade is above 60, the flat bonus applies. The exact bonus depends on the target university (typically +30 at the Technion, +35 at Tel Aviv University for 5-unit math).
3. Run: `python3 scripts/bagrut-calculator.py --mode subject --exam 78 --magen 85`

Result: Final subject grade is 80.1. When calculating the Bagrut weighted average for university admission, this subject receives the university's flat bonus (e.g., 80.1 + 30 = 110.1 at the Technion). Check the target university's bonus table for the exact value.

### Example 2: Plan Psychometric Preparation

User says: "I'm taking the psychometric in July. My practice test scores are: Quantitative 130, Verbal 105, English 120. How should I prepare?"

Actions:
1. Convert section scores to identify weak areas. On the 50-150 scale, Verbal at 105 is the weakest section.
2. Calculate approximate composite using the pre-December-2026 three-section weights (Quantitative and Verbal 40% each, English 20%): approximately (130 x 0.4) + (105 x 0.4) + (120 x 0.2) = 52 + 42 + 24 = 118. Treat this as a RELATIVE diagnostic only: it identifies the weakest domain, and it does NOT convert to the 200-800 scale, because the multiscale transform is not a linear reweighting of section scores. Only NITE's own score report gives the general score. For test dates from December 2026 onward only the quantitative and verbal domains count, since English is scored separately, and NITE weights them **50/50**, so the same worked example becomes (130 x 0.5) + (105 x 0.5).
3. Recommend focusing study time on Verbal Reasoning (biggest potential improvement) while maintaining Quantitative and English.
4. Suggest a 3-month preparation plan with emphasis on Hebrew reading comprehension and vocabulary.

Result: A targeted study plan prioritizing verbal reasoning improvement, with weekly practice schedule and specific resource recommendations.

### Example 3: Estimate University Admission Score

User says: "My Bagrut average is 98 and my psychometric is 720. Can I get into computer science at the Technion?"

Actions:
1. **Do not compute a 0-100 sekhem and compare it to a cut-off.** The Technion does not publish one, and a number invented here would look authoritative and mean nothing.
2. Rebuild the inputs first: the Technion computes an OPTIMAL bagrut average with its own bonus table, so "98" is almost certainly not the figure it will use. Recompute with the table above.
3. Send the user to the Technion's own sekhem formula and quick-calculation table on its admissions site, and to its published cut-off for the specific programme. That is the only number that answers the question asked.
4. Say plainly what is and is not knowable: a 720 is a strong score, computer science is among the most competitive programmes, and whether it clears this year's cut-off is a fact the Technion publishes and this skill does not hold.

Result: the user leaves with a correctly-constructed bagrut average, the institution's own calculator, and a realistic read, rather than a fabricated composite. If they want to improve their position, a higher psychometric is the faster lever when the bagrut is already strong.

## Bundled Resources

### Scripts
- `scripts/bagrut-calculator.py` - Calculate Bagrut subject grades and weighted averages with bonus points. Run: `python3 scripts/bagrut-calculator.py --help`

### References
- `references/bagrut-subjects-and-units.md` - Complete list of Bagrut subjects with available unit levels, mandatory vs. elective status, and bonus point rules. Consult when helping students plan their subject selections.
- `references/university-admission-guide.md` - Overview of admission requirements and sekhem calculation methods for major Israeli universities. Consult when estimating admission chances or comparing programs.
- `references/nite-tests-and-procedures.md` - Retake rules, the accommodations deadline, answer-sheet re-checks, the full fee and cancellation schedule, and the rest of the NITE test family (מו"ר, מרק"ם, מתא"ם, יע"ל, אמירנט). **Read this before answering anything about deadlines, fees, retakes, or which test a student actually needs.**

## Gotchas

- The Israeli academic year runs October-July, not September-June (US) or September-July (UK). Agents may give incorrect advice about exam scheduling, application deadlines, and academic calendar planning.
- The Psychometric Entrance Test (PET) scoring scale is 200-800, not 200-1600 like the US SAT. Agents may confuse the two scales, leading to wildly inaccurate score comparisons or admission estimates.
- Bagrut bonus points for 5-unit subjects are flat per subject (not tiered by score range), but the amount varies by university and subject. Agents may invent a tiered bonus system or use a single universal value. Always direct users to check their target university's specific bonus table.
- Each Israeli university calculates the sekhem (admission score) using its own proprietary formula. Agents that assume a universal formula will produce inaccurate admission estimates. Always direct users to the specific university's calculator.
- The Psychometric test fee, NITE registration dates, and section weights are updated periodically. Agents using stale data from their training corpus may provide outdated registration information or incorrect scoring breakdowns.
- From the December 2026 (winter תשפ"ז) session, English is removed from the psychometric and tested separately via NITE's computerized English test (AMIRNET), and the general score is based on the quantitative and verbal domains only. Agents trained on the older three-section (40/40/20) structure will describe the wrong test for students sitting from that date onward. Older three-domain scores remain valid for 7 years.
- The Bagrut passing grade is 55, not 56 or 60. The minimum grade to earn a university 5-unit bonus is a separate threshold (around 60). Agents conflate these two numbers.
- The new-immigrant Bagrut benefit lasts 10 years from aliyah (or until age 23, whichever is later; 12 years or until age 25 for Ethiopian immigrants), and the bonus is +10 or +15 by Hebrew level, not a flat +15. The 4-year figure belongs to returning-resident status, a different entitlement.


## Reference Links

| Source | URL | What to Check |
|--------|-----|---------------|
| Ministry of Education, exams portal | https://exams.education.gov.il/certificates/eligibility-for-matriculation-certificate/ | Eligibility conditions, the 5-unit cap, internal subjects, failing grades and the compensation thresholds |
| NITE (Psychometric Entrance Test) | https://www.nite.org.il/en | Official psychometric test dates, registration, preparation materials |
| NITE - sample questions | https://www.nite.org.il/practice-tests/?lang=en | Practice psychometric tests with answer keys |
| NITE - two-domain psychometric (Dec 2026) | https://www.nite.org.il/two-domain-psychometric-entrance-test/faqs/?lang=en | The Dec-2026 reform: English split out, two-domain (Quant + Verbal) score |
| Council for Higher Education | https://che.org.il/en/ | University admission thresholds, accredited degree programs |
| Kol Zchut - bagrut rights | https://www.kolzchut.org.il/he/בחינות_בגרות | Retake rights, grade appeals, accommodations, recognition of foreign diplomas |
| Ministry of Education - olim accommodations | https://www.kolzchut.org.il/he/התאמות_בבחינות_הבגרות_לתלמידים_עולים | New-immigrant exam adaptations and Hebrew-level bonus |

## Troubleshooting

### Error: "My calculated Bagrut average doesn't match my school's number"

Cause: Schools may use slightly different rounding methods, or include/exclude certain subjects. Also, bonus points for 5-unit subjects are sometimes counted differently by schools vs. universities.

Solution: (1) Verify which subjects are included in the calculation. (2) Check whether bonus points have been applied. (3) Use the official Ministry of Education Bagrut certificate as the authoritative source. (4) For university admissions, each university recalculates the average using their own formula.

### Error: "The sekhem I calculated doesn't match the university's calculator"

Cause: Each university uses proprietary formulas that may include adjustments beyond simple weighted averages, such as bonuses for certain subjects, different rounding rules, or normalization methods.

Solution: (1) Use the specific university's online admission calculator if available. (2) The sekhem calculated by this skill is an estimate based on common weighting patterns. (3) For exact figures, contact the university's admissions office directly.

### Error: "I don't know my magen grade yet"

Cause: Magen grades are finalized by teachers close to the exam date and may not be available during early planning.

Solution: (1) Use recent test averages as an estimate for the magen. (2) Calculate scenarios with different magen grades to understand the range of outcomes. (3) Focus on improving in-class performance to maximize the magen, as it is 30% of the final grade.
