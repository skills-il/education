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

#### Bagrut Grade Formula

Each subject's final Bagrut grade is calculated as:

| Component | Weight | Description |
|-----------|--------|-------------|
| External exam (בחינה חיצונית) | 70% | The national Bagrut exam |
| Magen grade (ציון מגן) | 30% | Teacher's assessment based on classwork, attendance, behavior |

**Final Subject Grade** = (Exam Score x 0.7) + (Magen Score x 0.3)

#### Study Units (יחידות לימוד)

Each subject is studied at a level measured in study units (1-5 units). More units = deeper study.

| Units | Level | Description |
|-------|-------|-------------|
| 1 unit | Basic | Minimal exposure |
| 3 units | Standard | Standard level for most subjects |
| 4 units | Extended | Above average depth |
| 5 units | Advanced | Highest level, required for competitive university programs |

**Minimum requirements for a Bagrut certificate:**
- Mandatory subjects: Hebrew (5 units), English (3-5 units), Mathematics (3-5 units), History/Civics, Bible (Tanakh), Hebrew Literature
- Minimum total: 21 study units
- Passing grade: 55 in each subject

#### Bonus Points for 5-Unit Subjects

Students who take subjects at 5-unit level receive bonus points on their Bagrut average. Bonuses are flat per subject (not tiered by score), but require a minimum grade of 60. Each university sets its own bonus amounts. Common values:

| Subject (5 units) | Typical Bonus |
|-------------------|--------------|
| Mathematics | +25 to +35 |
| Physics, Chemistry, Biology, Computer Science | +20 to +25 |
| English | +12.5 to +20 |
| History, Literature, Bible, other subjects | +12.5 to +20 |

**Important:** These bonus amounts vary by university. For example, the Technion awards +30 for Math and Physics, while other universities may use different values. Always check the target university's admissions page for exact bonus tables. The bonus is added to the subject grade when calculating the Bagrut weighted average.

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
- New immigrants (olim chadashim) receive 15 bonus points on the magen of each subject (excluding English if from an English-speaking country)
- Students with learning disabilities may receive testing accommodations (extra time, oral exams)

### Step 3: Psychometric Entrance Test (PET)

The Psychometric Entrance Test (מבחן פסיכומטרי, or "Psychometri") is administered by NITE (the National Institute for Testing and Evaluation, מרכז ארצי לבחינות ולהערכה, known in Hebrew as מאל"ב).

#### Test Structure

| Section | Content | Weight in Final Score |
|---------|---------|----------------------|
| Quantitative Reasoning (חשיבה כמותית) | Math, logic, data interpretation | 40% |
| Verbal Reasoning (חשיבה מילולית) | Reading comprehension, analogies, sentence completion | 40% |
| English (אנגלית) | Reading comprehension, vocabulary, sentence completion | 20% |

#### Scoring

- Scale: **200-800** (multiscale scoring)
- Mean score: approximately 530
- Standard deviation: approximately 90
- Each section also receives its own score on the 50-150 scale
- Scores are valid for university admission for **7 years** from the test date

#### Test Dates

NITE offers the PET **multiple times per year** (typically 4-6 administrations). Common months include January, April, July, September, October, and December, but the exact schedule changes annually. Test dates may also be postponed due to security situations or holidays.

Always check the official NITE website for the current year's schedule: `https://www.nite.org.il/test-dates-and-prices/`

#### Registration

1. Register online at the NITE website (`https://www.nite.org.il`)
2. Registration opens approximately 2-3 months before each test date
3. Fee: 665 NIS as of 2026 (may change; check NITE for current fee)
4. Test is offered in Hebrew, Arabic, Russian, French, Spanish, and combined Hebrew-English
5. Results are available on the NITE website within 45 days of the test

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

### Step 5: Key Terms Reference

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
2. Since math is typically 5 units and the grade is above 60, bonus points apply. The exact bonus depends on the target university (typically +25 to +35 for 5-unit math).
3. Run: `python scripts/bagrut-calculator.py --mode subject --exam 78 --magen 85`

Result: Final subject grade is 80.1. When calculating the Bagrut weighted average for university admission, this subject receives a bonus (e.g., 80.1 + 25 = 105.1 at universities that award +25 for 5-unit math). Check the target university's bonus table for the exact value.

### Example 2: Plan Psychometric Preparation

User says: "I'm taking the psychometric in July. My practice test scores are: Quantitative 130, Verbal 105, English 120. How should I prepare?"

Actions:
1. Convert section scores to identify weak areas. On the 50-150 scale, Verbal at 105 is the weakest section.
2. Calculate approximate composite: Quantitative and Verbal are 40% each, English is 20%. The user's overall is approximately (130 x 0.4) + (105 x 0.4) + (120 x 0.2) = 52 + 42 + 24 = 118, which maps to roughly 620-640 on the 200-800 scale.
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
