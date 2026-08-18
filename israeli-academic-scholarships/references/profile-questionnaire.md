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
6. **Did you serve in Sherut Leumi-Ezrachi or Sherut Leumi?** If yes, end-of-service date.
7. **Did you receive a service exemption?** (some tracks treat exempt civilians differently)

## Background

8. **Aliyah status** - born in Israel / oleh chadash within last 10 years / toshav chozer? If oleh, aliyah date and country of origin.
9. **Residence history** - where did you live for most of the 6 years before starting your degree? Specifically, were you in a national-priority-area yishuv for 5 of those 6 years?
10. **Household socioeconomic status** - single-parent / large family (4+ children) / working but below median income / first-generation in higher education / ultra-Orthodox / Arab-Israeli / Ethiopian-Israeli / Mizrahi / Bedouin / Druze / etc.

## Academic record

11. **Bagrut average** (numeric, e.g., 105 if extra credit, 95 otherwise)
12. **Psychometric / Yael score** (if took the test)
13. **First-year university GPA** (if continuing student)
14. **Academic distinctions** (any honors, prize lists, dean's list?)

## Special factors

15. **Are you a woman entering or pursuing STEM?** (HUJI free-tuition track, Weizmann pipeline)
16. **Are you on an Israeli national-team athletic roster?** (Mifal HaPais athlete track)
17. **Did you serve reserve duty during the current academic year?** (PEREACH miluim supplement)
18. **Are you currently a single parent?** (Rashi single-mother track, MilGo factor)

## Application willingness

19. **Are you willing to commit ~114 hours of tutoring per academic year** for the PEREACH grant? (140 hours for higher tier)
20. **Are you comfortable writing personal-statement essays** (foundation applications) or do you prefer auto-eligibility tracks only?

## Output

After collecting these, the skill should:

1. Build a profile vector
2. Run each scholarship's eligibility filter against the vector
3. Return the eligible scholarships ranked by deadline → grant size → effort
4. Surface stacking conflicts (especially MoD periphery exclusivity)
5. Generate a personalized application checklist with deadlines
