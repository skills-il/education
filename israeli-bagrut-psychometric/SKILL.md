---
name: israeli-bagrut-psychometric
description: Guide users through Israel's Bagrut matriculation exams and Psychometric entrance test (PET) system. Use when user asks about bagrut study units, psychometric scores, exam structure, university entrance requirements, sekher calculation, or study planning. Covers the Bagrut grading formula (70% exam + 30% magen), PET scoring (200-800), NITE registration, test dates, and strategies for maximizing combined admission scores (sekhem). Prevents confusion between the many overlapping terms and formulas in the Israeli higher-education admissions process. Do NOT use for university-specific admission thresholds, post-secondary academic advising, or non-Israeli education systems.
license: MIT
allowed-tools: Bash(python:*) Read
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
- **5-yedaot (5-unit) requirements** were partially relaxed for select subjects following pandemic-era and wartime adjustments. Some subjects now allow alternative magen pathways or project-based components in place of part of the external exam. Always verify per-subject rules on the Ministry of Education's current-year exam page (`https://edu.gov.il/mazkirut_pedagogit/BagrutExams`).
- **Oral and project components** count toward more subjects, not only languages. The 70/30 exam-to-magen split is the standard baseline (with a 2026 wartime 60/40 option, see the formula section), but the "exam" component is increasingly a portfolio of mini-exams + project work in subjects like history, civics, and computer science.
- **Wartime and emergency accommodations** introduced in 2023-24 (extended deadlines, oral substitutions for written exams, makeup sessions) carried into 2024-25 for students from evacuated communities or with reservist parents. Students should ask their school counselor whether they qualify.

When in doubt, treat the formula and unit numbers in this skill as the standard baseline and direct the student to the Ministry's current-year subject page for any subject-specific deviations.

#### Bagrut Grade Formula

Each subject's final Bagrut grade is calculated as:

| Component | Weight | Description |
|-----------|--------|-------------|
| External exam (בחינה חיצונית) | 70% | The national Bagrut exam |
| Magen grade (ציון מגן) | 30% | Teacher's assessment based on classwork, attendance, behavior |

**Final Subject Grade** = (Exam Score x 0.7) + (Magen Score x 0.3)

**Wartime accommodation (2026):** for cohorts affected by the war, the Ministry of Education allows a 60% exam / 40% magen split (instead of 70/30) when it raises the final grade, plus other flexible-Bagrut options. Check the current-year directive for which subjects and students qualify.

#### Study Units (יחידות לימוד)

Each subject is studied at a level measured in study units (1-5 units). More units = deeper study.

| Units | Level | Description |
|-------|-------|-------------|
| 1 unit | Basic | Minimal exposure |
| 3 units | Standard | Standard level for most subjects |
| 4 units | Extended | Above average depth |
| 5 units | Advanced | Highest level, required for competitive university programs |

**Minimum requirements for a Bagrut certificate:**
- Mandatory core subjects: Hebrew language and expression (lashon/hava'a), Hebrew Literature, Bible (Tanakh), History, Civics, English (3-5 units), Mathematics (3-5 units). Exact unit counts for the cores vary by education sector (state, state-religious, Arab, Druze) and year, so verify per-sector counts on the Ministry of Education site.
- Minimum total: 21 study units, including at least one subject at the 5-unit (moogbar) level
- Passing grade: 55 in each subject

#### Bonus Points for 5-Unit Subjects

Students who take subjects at 5-unit level receive bonus points on their Bagrut average. Bonuses are flat per subject (not tiered by score), but require a minimum grade of 60. Each university sets its own bonus amounts. Common values:

| Subject (5 units) | Typical Bonus |
|-------------------|--------------|
| Mathematics | +30 to +35 (Technion +30, Tel Aviv University +35) |
| Physics, Chemistry, Biology, Computer Science | +25 |
| English | +20 to +25 (4-unit English is typically +12.5) |
| History, Literature, Bible, other subjects | +20 |

**Important:** The bonus is a flat per-subject amount set by each university (it is NOT tiered by your score). It is awarded only if the subject grade is at least 60. The amount varies by university and subject: for example, the Technion awards +30 for 5-unit Math and +25 for the sciences, while Tel Aviv University awards +35 for 5-unit Math. Always check the target university's admissions page for its exact bonus table. The bonus is added to the subject grade when calculating the Bagrut weighted average.

Use `scripts/bagrut-calculator.py` to compute grades:

```bash
python scripts/bagrut-calculator.py --mode subject --exam 82 --magen 90
python scripts/bagrut-calculator.py --mode average --subjects "math:5:88,english:5:92,history:3:78,bible:3:80,hebrew:5:85,literature:3:76"
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

The Psychometric Entrance Test (מבחן פסיכומטרי, or "Psychometri") is administered by NITE (the National Institute for Testing and Evaluation, מרכז ארצי לבחינות ולהערכה, known in Hebrew as מאל"ב).

#### Test Structure

| Section | Content | Weight in Final Score |
|---------|---------|----------------------|
| Quantitative Reasoning (חשיבה כמותית) | Math, logic, data interpretation | 40% |
| Verbal Reasoning (חשיבה מילולית) | Reading comprehension, analogies, sentence completion | 40% |
| English (אנגלית) | Reading comprehension, vocabulary, sentence completion | 20% |

**Major change from the December 2026 session (winter, תשפ"ז):** English is removed from the psychometric test and assessed separately through NITE's standalone computerized English test (AMIRNET, part of NITE's AMIR English-test family), offered year-round. The psychometric general score becomes two-domain: Quantitative Reasoning and Verbal Reasoning only (within the verbal domain, the writing task counts for 25%). NITE has not yet published the weighting between the two remaining domains. The overall scale stays 200-800. Scores from the older three-domain format remain valid for their full 7 years. From this session the "combined Hebrew-English" version is also affected. Confirm the exact structure for your test date on the NITE site.

#### Scoring

- Scale: **200-800** (multiscale scoring)
- Mean score: approximately 530
- Standard deviation: approximately 100 (about 68% of test-takers score between 430 and 630)
- Each section also receives its own score on the 50-150 scale
- Scores are valid for university admission for **7 years** from the test date

#### Test Dates

NITE offers the PET **multiple times per year** (typically 4-6 administrations). Common months include January, April, July, September, October, and December, but the exact schedule changes annually. Test dates may also be postponed due to security situations or holidays. The 2026 cycle continues to follow this pattern, but specific dates are announced 6-9 months in advance and shift year-over-year.

Always check the official NITE website for the current year's schedule: `https://www.nite.org.il/test-dates-and-prices/`

#### Registration

1. Register online at the NITE website (`https://www.nite.org.il`)
2. Registration opens approximately 2-3 months before each test date
3. Fee: approximately 665 NIS as of 2026 (subject to annual NITE updates; always confirm on the test-dates-and-prices page above)
4. Test is offered in Hebrew, Arabic, Russian, French, Spanish, and combined Hebrew-English
5. Results are available on the NITE website within 45 days of the test
6. Late registration carries an additional surcharge; early-registration discounts may apply for some sittings

#### Available Languages

| Language | Notes |
|----------|-------|
| Hebrew | Standard version, most common |
| Arabic | For Arabic-speaking students |
| Russian | For Russian-speaking olim |
| French | For French-speaking olim |
| Spanish | For Spanish-speaking olim |
| Combined (Hebrew + English) | English verbal section replaces Hebrew verbal |

### Step 4: University Admission Score (Sekhem)

The sekhem (ציון סכם) is the combined score used by Israeli universities for admissions decisions. It merges the Bagrut average with the Psychometric score.

#### How Sekhem is Calculated

Each university uses its own weighting formula. Common patterns:

| University | Typical Bagrut Weight | Typical Psychometric Weight |
|------------|----------------------|----------------------------|
| Hebrew University | ~40% | ~60% |
| Tel Aviv University | ~40% | ~60% |
| Technion | ~40% | ~60% |
| Ben-Gurion University | ~40% | ~60% |
| Bar-Ilan University | ~40% | ~60% |
| University of Haifa | ~40% | ~60% |

**Note:** These are approximate general weights. Specific programs (medicine, law, engineering, computer science) often have different weights, additional requirements, or minimum score thresholds. Always check the specific program's admissions page.

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

Use `scripts/bagrut-calculator.py` to estimate the sekhem:

```bash
python scripts/bagrut-calculator.py --mode sekhem --bagrut-avg 95.5 --psychometric 680 --bagrut-weight 40 --psychometric-weight 60
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
| יחידות לימוד | Yechidot Limud | Study units (1-5 scale) |
| ממוצע בגרות | Memutza Bagrut | Bagrut GPA / weighted average |
| פסיכומטרי | Psychometri | Psychometric entrance test (PET) |
| מאל"ב (מרכז ארצי לבחינות ולהערכה) | MALAV / NITE | National Institute for Testing and Evaluation |
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
3. Run: `python scripts/bagrut-calculator.py --mode subject --exam 78 --magen 85`

Result: Final subject grade is 80.1. When calculating the Bagrut weighted average for university admission, this subject receives the university's flat bonus (e.g., 80.1 + 30 = 110.1 at the Technion). Check the target university's bonus table for the exact value.

### Example 2: Plan Psychometric Preparation

User says: "I'm taking the psychometric in July. My practice test scores are: Quantitative 130, Verbal 105, English 120. How should I prepare?"

Actions:
1. Convert section scores to identify weak areas. On the 50-150 scale, Verbal at 105 is the weakest section.
2. Calculate approximate composite using the pre-December-2026 three-section weights (Quantitative and Verbal 40% each, English 20%): approximately (130 x 0.4) + (105 x 0.4) + (120 x 0.2) = 52 + 42 + 24 = 118, which maps to roughly 620-640 on the 200-800 scale. For test dates from December 2026 onward, only the quantitative and verbal domains count, since English is scored separately; NITE has not yet published the new weighting between them.
3. Recommend focusing study time on Verbal Reasoning (biggest potential improvement) while maintaining Quantitative and English.
4. Suggest a 3-month preparation plan with emphasis on Hebrew reading comprehension and vocabulary.

Result: A targeted study plan prioritizing verbal reasoning improvement, with weekly practice schedule and specific resource recommendations.

### Example 3: Estimate University Admission Score

User says: "My Bagrut average is 98 and my psychometric is 720. Can I get into computer science at the Technion?"

Actions:
1. Calculate estimated sekhem using typical Technion CS weights: (98 x 0.4) + (720/800 x 100 x 0.6) = 39.2 + 54 = 93.2 (normalized score)
2. Note that Technion CS is highly competitive, typically requiring sekhem above 90-92
3. The user's score of 93.2 is competitive but not guaranteed
4. Run: `python scripts/bagrut-calculator.py --mode sekhem --bagrut-avg 98 --psychometric 720 --bagrut-weight 40 --psychometric-weight 60`

Result: Estimated sekhem of ~93.2. This is in the competitive range for Technion CS. Recommend checking the most recent admission cutoff on the Technion admissions website. If the user wants to improve their chances, retaking the psychometric (aiming for 740+) would be the most effective strategy since the Bagrut is already excellent.

## Bundled Resources

### Scripts
- `scripts/bagrut-calculator.py` - Calculate Bagrut subject grades, weighted averages with bonus points, and estimated sekhem scores. Run: `python scripts/bagrut-calculator.py --help`

### References
- `references/bagrut-subjects-and-units.md` - Complete list of Bagrut subjects with available unit levels, mandatory vs. elective status, and bonus point rules. Consult when helping students plan their subject selections.
- `references/university-admission-guide.md` - Overview of admission requirements and sekhem calculation methods for major Israeli universities. Consult when estimating admission chances or comparing programs.

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
| Ministry of Education - Bagrut | https://edu.gov.il/mazkirut_pedagogit/BagrutExams/Pages/bagrut-exams.aspx | Official bagrut exam schedule, subject weights, grading |
| NITE (Psychometric Entrance Test) | https://www.nite.org.il/en | Official psychometric test dates, registration, preparation materials |
| NITE - sample questions | https://www.nite.org.il/practice-tests/?lang=en | Practice psychometric tests with answer keys |
| NITE - two-domain psychometric (Dec 2026) | https://www.nite.org.il/two-domain-psychometric-test/general-information/?lang=en | The Dec-2026 reform: English split out, two-domain (Quant + Verbal) score |
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
