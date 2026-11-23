# Profile Questionnaire - Scholarship Matching

Structured intake the skill should run before recommending. Ask in a single batched prompt rather than one-at-a-time.

## Core profile

1. **Degree level** - BA / MA / PhD / postdoc?
2. **Institution** - which university or college? (HUJI / TAU / Technion / BIU / BGU / OpenU / Reichman / Ariel / college / מכינה / הנדסאי)
3. **Year of study** - incoming freshman / second-year / completing / graduate-level?
4. **Faculty / field** - CS / Math / Engineering / Medicine / Humanities / Social Sciences / Other?

## Service status

5. **Did you serve in the IDF?** If yes:
   - Combat profile? (lochem yes/no)
   - Length of service? (sherut chova months + miluim days)
   - Discharge date? (anchors the 5-year Pikadon window)
   - Discharge certificate type? (gold honorable discharge matters for Mimadim)
6. **Did you serve in Sherut Leumi-Ezrachi or Sherut Leumi?** If yes, end-of-service date.
7. **Did you receive a service exemption?** (some tracks treat exempt civilians differently)

## Background

8. **Aliyah status** - born in Israel / oleh / toshav chozer? If oleh: date status was received, age at the start of studies, and country of origin (Student Authority age and 36-month limits).
9. **Residence history** - where did you live for most of the 6 years before starting your degree? Specifically, were you in a national-priority-area yishuv for 5 of those 6 years?
9a. **Did you complete a pre-academic mechina funded by the MoD fund?** If yes, when did it start? (periphery track 46)
10. **Household socioeconomic status** - single-parent / large family (4+ children) / working but below median income / first-generation in higher education / ultra-Orthodox / Arab-Israeli / Ethiopian-Israeli / Mizrahi / Bedouin / Druze / etc.

## Academic record

11. **Bagrut average** (numeric, e.g., 105 if extra credit, 95 otherwise)
12. **Psychometric / Yael score** (if took the test)
13. **First-year university GPA** (if continuing student)
14. **Academic distinctions** (any honors, prize lists, dean's list?)

## Special factors

15. **Are you a woman entering or pursuing STEM?** (Weizmann pipeline)
16. **Are you on an Israeli national-team athletic roster?** (Mifal HaPais athlete track)
17. **Reserve duty since 7.10.2023:** days in each academic year (תשפ"ד, תשפ"ה, תשפ"ו, תשפ"ז), your unit's activity tier (מדרג), and any child under 14? (reservist tuition grants, PEREACH supplement)
17a. **Was your household evacuated since 7.10.2023?** (evacuee tracks)
17b. **Are you a bereaved family member or a recognized wounded veteran?** (statutory tracks through your case manager)
18. **Are you a parent?** (ask the Welfare Ministry about Maskila; MilGo factor)

## Application willingness

19. **Are you willing to commit about 114 hours of tutoring per academic year** for the PEREACH grant? (130 hours on the enhanced track, in some cities)
20. **Are you comfortable writing personal-statement essays** (foundation applications) or do you prefer tracks with no essay?

## Output

After collecting these, the skill should:

1. Build a profile vector
2. Compare each scholarship's published criteria with the vector, marking anything unsettled as "check"
3. Return the possible matches ranked by deadline → grant size → effort
4. Surface stacking conflicts (MoD periphery exclusivity, Mimadim before the reservist tuition grant)
5. Generate a personalized application checklist with deadlines
