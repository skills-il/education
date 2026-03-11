---
name: israeli-academic-navigator
description: >-
  Guide users through Israel's higher education system, university admissions, scholarships,
  and student rights. Use when user asks about university admission requirements,
  sekher calculation, scholarship options (milgot), Perach tutoring program, student
  union (aguda) rights, comparing universities vs colleges (michlalot), or navigating
  the Council for Higher Education (CHE) system. Covers application timelines, financial
  aid, special accommodations for soldiers and olim, and institutional comparisons.
  Do NOT use for Bagrut exam preparation or psychometric test strategies.
license: MIT
compatibility: No network required. Works offline with reference data.
metadata:
  author: skills-il
  version: 1.0.0
  category: education
  tags:
    he:
    - אוניברסיטה
    - קבלה
    - מלגה
    - זכויות-סטודנטים
    - השכלה-גבוהה
    - ישראל
    en:
    - university
    - admission
    - scholarship
    - student-rights
    - higher-education
    - israel
  display_name:
    he: ניווט אקדמי ישראלי
    en: Israeli Academic Navigator
  display_description:
    he: מדריך לקבלה לאוניברסיטאות, מלגות וזכויות סטודנטים בישראל
    en: >-
      Guide users through Israel's higher education system, university admissions,
      scholarships, and student rights. Use when user asks about university admission
      requirements, sekher calculation, scholarship options (milgot), Perach tutoring
      program, student union (aguda) rights, comparing universities vs colleges (michlalot),
      or navigating the Council for Higher Education (CHE) system. Covers application
      timelines, financial aid, special accommodations for soldiers and olim, and
      institutional comparisons. Do NOT use for Bagrut exam preparation or psychometric
      test strategies.
  supported_agents:
  - claude-code
  - cursor
  - github-copilot
  - windsurf
  - opencode
  - codex
  - antigravity
---


# Israeli Academic Navigator

## Instructions

### Step 1: Israeli Higher Education Landscape
Israel's higher education system is overseen by the Council for Higher Education (CHE, Va'adat HaChinuch HaGavoha / Malag). Institutions fall into several categories:

| Institution Type | Hebrew | Count (approx.) | Degree Authority | Examples |
|-----------------|--------|-----------------|------------------|----------|
| Research Universities | אוניברסיטאות מחקר | 8 | BA, MA, PhD | Hebrew University, Technion, Tel Aviv University |
| Academic Colleges (Michlalot Akademi'ot) | מכללות אקדמיות | ~30 | BA, some MA | Ruppin, Sapir, Shenkar |
| Teacher Training Colleges (Michlalot LeChinuch) | מכללות לחינוך | ~20 | B.Ed, M.Ed | Levinsky, Oranim, Beit Berl |
| Open University (Ha'Universita HaPtucha) | האוניברסיטה הפתוחה | 1 | BA, MA | Open enrollment, distance learning |
| Private/International Institutions | מוסדות פרטיים/בינלאומיים | Several | Varies | IDC Herzliya (Reichman), Ono Academic College |

**The 8 research universities:**

| University | Hebrew | Location | Known For |
|-----------|--------|----------|-----------|
| Hebrew University of Jerusalem | האוניברסיטה העברית בירושלים | Jerusalem | Humanities, law, medicine, sciences |
| Technion (Israel Institute of Technology) | הטכניון | Haifa | Engineering, computer science, architecture |
| Tel Aviv University | אוניברסיטת תל אביב | Tel Aviv | Largest university, strong across fields |
| Weizmann Institute of Science | מכון ויצמן למדע | Rehovot | Graduate-only, natural sciences |
| Bar-Ilan University | אוניברסיטת בר אילן | Ramat Gan | Jewish studies, psychology, law |
| University of Haifa | אוניברסיטת חיפה | Haifa | Social sciences, marine sciences, education |
| Ben-Gurion University of the Negev | אוניברסיטת בן גוריון בנגב | Be'er Sheva | Engineering, health sciences, desert research |
| Ariel University | אוניברסיטת אריאל | Ariel | Engineering, health professions |

**Key differences: Universities vs. Colleges (Michlalot):**

| Factor | University | College (Michlala) |
|--------|-----------|-------------------|
| Research focus | High, publish-or-perish | Lower, teaching-focused |
| Class sizes | Larger lecture halls | Smaller, more personal |
| Degree offerings | BA, MA, PhD | BA, some MA |
| Admission difficulty | Generally higher | Generally more accessible |
| Tuition | Regulated by CHE | Regulated, may vary slightly |
| Prestige (perceived) | Higher in job market | Growing recognition |

### Step 2: Admission Requirements (Sekher Calculation)
Israeli university admission is based on a combined score called the Sekher (סכר), which weighs Bagrut and Psychometric results:

| Component | Description | Typical Weight |
|-----------|-------------|---------------|
| Bagrut Average (Memutza Bagrut Meshuklal) | Weighted matriculation average with bonuses | 40-60% |
| Psychometric Score (Tziun Psichometri) | PET score (200-800 scale) | 40-60% |
| Subject Bonuses (Bonusim) | Extra points for 5-unit and 4-unit subjects | Added to Bagrut average |

**Sample admission thresholds (approximate, vary by year):**

| Program | Hebrew | Typical Sekher Range | Notes |
|---------|--------|---------------------|-------|
| Medicine (Refu'a) | רפואה | Very high (top 1-2%) | Includes interview, morals exam |
| Law (Mishpatim) | משפטים | High (680+ PET, strong Bagrut) | Varies significantly by institution |
| Computer Science (Mada'ei HaMachshev) | מדעי המחשב | High | Math 5 units often required |
| Psychology (Psichologia) | פסיכולוגיה | High for BA, very high for clinical MA | Competitive field |
| Engineering (Handasa) | הנדסה | Moderate-high | Technion most selective |
| Business Administration (Minhal Asakim) | מנהל עסקים | Moderate | Widely available |
| Education (Chinuch) | חינוך | Moderate | College options more accessible |
| Social Work (Avoda Sotzialit) | עבודה סוציאלית | Moderate | Growing demand |

**Alternative admission paths:**

| Path | Hebrew | Who Qualifies | Notes |
|------|--------|--------------|-------|
| Mechina Pre-Academic Program | מכינה קדם אקדמית | Those without full Bagrut | 1-year preparatory program |
| Open University Transfer | העברה מהאוניברסיטה הפתוחה | Open University students | Accumulate credits, then transfer |
| Age-Based Admission (30+) | קבלה על בסיס גיל | Applicants over 30 | Some programs waive PET |
| Portfolio Admission | קבלה על בסיס תיק עבודות | Art, design, architecture programs | Portfolio review process |
| Army Service Credit | זיכוי שירות צבאי | IDF veterans | Bonus points at some institutions |

### Step 3: Application Process and Timelines
The academic year in Israel typically starts in October (semester alef) and ends in June-July:

| Phase | Hebrew | Timeline | Action Items |
|-------|--------|----------|--------------|
| Research programs | מחקר תוכניות | September-November | Review university catalogs, attend open days (yom patuach) |
| Registration opens | פתיחת הרשמה | November-January | Most universities open online registration |
| Application deadline | מועד אחרון להרשמה | February-April | Varies by institution (check each one) |
| Psychometric test | בחינה פסיכומטרית | April/July/Sept/Dec | Take PET if not yet done |
| Admission decisions | החלטות קבלה | April-July | Rolling admissions at some institutions |
| Confirmation deadline | מועד אישור | Varies | Confirm acceptance, pay deposit (pikdon) |
| Semester starts | תחילת סמסטר | October | Orientation (yom kiut / shvua klitatim) |

**Application requirements checklist:**

| Document | Hebrew | Notes |
|----------|--------|-------|
| Teudat Zehut (ID) | תעודת זהות | Copy required |
| Bagrut Certificate (Te'udat Bagrut) | תעודת בגרות | Official copy from school or MOE |
| Psychometric Score | ציון פסיכומטרי | Sent automatically from NITE |
| High school transcript | גיליון ציונים תיכון | If Bagrut not yet complete |
| Application fee | דמי הרשמה | Approximately 300-450 NIS per institution |
| Military service certificate (Shichrur) | תעודת שחרור | For IDF veterans |
| Passport photo | תמונת פספורט | Digital format for online applications |

### Step 4: Scholarships and Financial Aid
Israel offers various scholarship and financial aid options:

| Scholarship Type | Hebrew | Amount (approx.) | Eligibility |
|-----------------|--------|-----------------|-------------|
| Perach Tutoring | פר"ח | Tuition reduction (partial) | Students tutoring disadvantaged youth, 4 hrs/week |
| University Merit Scholarships (Milgot Mitztaynim) | מלגות מצטיינים | 5,000-full tuition | Based on academic achievement |
| Need-Based Grants (Milgot Al Basis Socio-Ekonomi) | מלגות סוציואקונומיות | Variable | Based on financial need |
| Field-Specific Scholarships | מלגות תחום ספציפי | Variable | STEM, periphery, teaching |
| Bituach Leumi Student Benefits | הטבות ביטוח לאומי לסטודנטים | Reduced NI payments | All full-time students |
| Government Tuition Assistance (Va'adot Siyua) | ועדות סיוע | Up to full tuition | Demonstrated financial hardship |
| IDF Atudot Program | עתודות | Full tuition + stipend | Pre-army commitment to specific fields |
| Olim (New Immigrant) Scholarships | מלגות עולים | Variable | Through Jewish Agency, ISEF, Absorption Ministry |

**Perach program details:**

| Aspect | Details |
|--------|---------|
| Commitment | 4 hours/week tutoring throughout academic year |
| Compensation | Partial tuition waiver (approximately 1/3 of annual tuition) |
| Who qualifies | Most undergraduate students |
| Registration | Through university Perach coordinator |
| Students tutored | Children from disadvantaged backgrounds |
| Additional benefits | Community service experience, teaching skills |

**Annual tuition reference (regulated by CHE):**

| Degree Level | Annual Tuition (approx.) | Notes |
|-------------|-------------------------|-------|
| Bachelor's (BA/BSc) | ~10,000-13,000 NIS | Regulated by CHE, updated annually |
| Master's (MA/MSc) | ~12,000-16,000 NIS | Some programs higher |
| MBA/Professional MA | ~30,000-80,000 NIS | Not fully regulated |
| PhD | Minimal or free | Often funded with stipend |
| College (Michlala) | ~10,000-15,000 NIS | Similar range to universities |

### Step 5: Student Rights and Accommodations
Israeli students have specific rights protected by law and institutional regulations:

| Right | Hebrew | Description |
|-------|--------|-------------|
| Student Union Membership (Aguda) | אגודת הסטודנטים | Automatic membership; union advocates for student interests |
| Academic Ombudsman (Netziv Kvilot Studentim) | נציב קבילות סטודנטים | Address academic grievances, grade disputes |
| Exam Accommodations (Hatkamot Bchinot) | התאמות בחינות | Extra time, separate room for documented disabilities |
| Army Reserve Accommodations (Hatkamot Miluim) | התאמות מילואים | Exam postponement, deadline extensions for reserve duty |
| Olim Accommodations | התאמות עולים | Extended exam time, dictionary use, Hebrew language support |
| Pregnancy/Parental Leave | חופשת הריון/הורות | Protected leave, exam postponement rights |
| Disability Services (Negishut) | נגישות | Physical and learning disability accommodations |
| Academic Appeal (Irur) | עירעור | Right to appeal grades and disciplinary decisions |

**Soldier (chayal meshuchrar) benefits:**

| Benefit | Details |
|---------|---------|
| Admission bonus points | Some institutions add points for meaningful service |
| Pikadon (Army Savings) | Funds saved during service, usable for tuition |
| ZAHAL Scholarship Program | Merit-based scholarships for veterans |
| Extended deadlines | Flexibility for recently discharged soldiers |
| Mechina programs | Preparatory programs designed for soldiers |
| Psychological support | Counseling services for transition to civilian life |

**Olim (new immigrant) benefits:**

| Benefit | Details |
|---------|---------|
| Hebrew Ulpan | Free intensive Hebrew courses (often on campus) |
| Exam accommodations | Extra time, dictionary use for several years |
| Absorption Ministry scholarships | Financial support for studies |
| ISEF Foundation grants | Scholarships for immigrant students |
| Reduced tuition | Some institutions offer discounts |
| Dedicated advisors | Olim academic advisors at most institutions |

### Step 6: Comparing Institutions
When comparing universities and colleges, consider these factors:

| Factor | What to Check | How to Find Information |
|--------|--------------|----------------------|
| Program quality | CHE quality assessments, rankings | CHE website, university publications |
| Employment outcomes (Hista'arut) | Graduate employment rates by field | CBS (Lishkat HaStatistika HaMerkazit) data |
| Campus location | Proximity to home, cost of living | University websites, student forums |
| Student life (Chayei Student) | Dormitories (me'onot), clubs, social life | Campus visits (yom patuach), student forums |
| Research opportunities | Lab access, faculty reputation | Faculty profiles, publication records |
| International programs | Exchange opportunities, English programs | International affairs office |
| Tuition and costs | Total cost including living expenses | University financial aid office |
| Dormitory availability (Me'onot) | Wait lists, pricing, distance students | Student services (sherut lastudent) |

**Cost of living comparison for students (monthly, approximate):**

| Expense | Tel Aviv | Jerusalem | Haifa | Be'er Sheva | Periphery |
|---------|----------|-----------|-------|-------------|-----------|
| Dormitory (Me'onot) | 2,500-4,000 NIS | 1,800-3,000 NIS | 1,500-2,500 NIS | 1,200-2,000 NIS | 1,000-1,800 NIS |
| Shared apartment (Shituf Dira) | 2,500-4,500 NIS | 2,000-3,500 NIS | 1,500-2,800 NIS | 1,200-2,200 NIS | 1,000-2,000 NIS |
| Food (Ochel) | 1,500-2,500 NIS | 1,200-2,000 NIS | 1,200-2,000 NIS | 1,000-1,800 NIS | 1,000-1,500 NIS |
| Transportation (Tachbura) | 200-400 NIS | 200-350 NIS | 150-300 NIS | 100-250 NIS | 100-250 NIS |
| Books/Materials (Sfarim) | 200-500 NIS | 200-500 NIS | 200-500 NIS | 200-500 NIS | 200-500 NIS |

## Examples

### Example 1: Choosing Between University and College
**Input:** "Should I go to Tel Aviv University or Ruppin College for a BA in Business?"
**Output:** Compare the two options: Tel Aviv University has higher prestige and research focus, larger campus with more social life, but higher admission threshold and higher cost of living in Tel Aviv. Ruppin College offers smaller classes, more personal attention, lower admission requirements, and significantly lower living costs in the Sharon region. Both are CHE-accredited and the degree is recognized for employment. Recommend visiting both on their yom patuach (open day) and checking graduate employment data from the CBS.

### Example 2: Scholarship Search for Low-Income Student
**Input:** "I'm from a low-income family, how do I pay for university?"
**Output:** Outline available options: (1) Apply for need-based scholarships (milgot socio-ekonomi'ot) through the university's financial aid office. (2) Register for Perach tutoring program for partial tuition waiver (about 1/3 of tuition for 4 hours/week). (3) Apply to the Va'adat Siyua (assistance committee) for hardship-based tuition reduction. (4) Check Bituach Leumi student benefits for reduced national insurance payments. (5) Explore field-specific scholarships if studying STEM or education. Provide application deadlines and contact information for the university's student services office (sherut lastudent).

### Example 3: Oleh Chadash University Admission
**Input:** "I made aliyah 2 years ago, what special accommodations do I get at university?"
**Output:** Explain oleh rights: extended exam time (typically 25-50% additional time depending on institution), permission to use a dictionary during exams, Hebrew language support through campus ulpan. Mention Absorption Ministry scholarships, ISEF Foundation grants, and dedicated olim academic advisors. Note that some institutions have specific olim tracks or preparatory programs. Advise contacting the university's olim coordinator (rakaz olim) early in the application process.

### Example 4: Application Timeline Planning
**Input:** "I'm finishing the army in August, when should I start applying to universities?"
**Output:** Map out the timeline: Start researching programs immediately (even before discharge). Most universities open registration November-January for the following October semester. Take the Psychometric in September or December (register 2-3 months ahead). Apply to multiple institutions by February-April deadlines. Use the pikadon (army savings) and explore ZAHAL veteran scholarships. Consider a pre-academic mechina program if Bagrut or PET scores need improvement. Contact university admissions offices about chayal meshuchrar benefits and bonus points.

## Bundled Resources

### References
- `references/universities-comparison.md` -- Detailed comparison of all major Israeli universities and colleges including location, strengths, tuition ranges, acceptance rates, and cost of living by city. Consult when a user needs to compare specific institutions or understand differences between universities and colleges.
- `references/scholarships-directory.md` -- Comprehensive directory of scholarships (milgot) available to Israeli students: Perach, university merit awards, need-based grants, olim scholarships, field-specific funding, and support for special populations. Consult when a user asks about financial aid options or how to pay for higher education.

### Scripts
- `scripts/tuition-estimator.py` -- Estimates annual tuition based on institution type, degree level, and student status. Run: `python scripts/tuition-estimator.py --institution university --degree bachelor --status citizen`

## Troubleshooting

### Error: "Sekher too low for desired program"
Cause: Combined Bagrut and Psychometric score does not meet the admission threshold.
Solution: Consider retaking the Psychometric (universities take highest score). Check if alternative admission paths exist (mechina, Open University transfer, age-based admission for 30+). Apply to the same program at a less selective institution. Explore whether the program is available at academic colleges with lower thresholds. Some programs offer conditional acceptance with a preparatory year.

### Error: "Cannot afford tuition and living expenses"
Cause: Financial barriers to higher education.
Solution: Apply for every available scholarship: need-based milgot, Perach program, field-specific grants, and Va'adat Siyua hardship assistance. Consider studying at a periphery institution where living costs are significantly lower. Check Bituach Leumi student benefits. Explore the Atudot program if still pre-army. Contact the university's student services (sherut lastudent) for emergency assistance options.

### Error: "Bagrut certificate incomplete or missing subjects"
Cause: Did not complete all required Bagrut exams or did not pass certain subjects.
Solution: Options include: complete missing exams through the external student (talmid eksterni) track via the Ministry of Education. Enroll in a pre-academic mechina program that can supplement missing subjects. Apply to the Open University, which does not require a full Bagrut for enrollment. Some colleges accept students without full Bagrut into specific preparatory tracks. Contact the university admissions office to ask about individual case review (bdika pratanit).
