---
name: israeli-academic-scholarships
description: "Match an Israeli higher-education student to scholarships they qualify for, ranked by deadline and grant size. Covers PEREACH, MoD periphery, Mimadim LiLimudim (graduated 85% each year + final-year top-up, capped ~NIS 10,214/year, NOT flat 100%), Pikadon, Student Authority for olim, MilGo (4-tier), Rashi, ISEF, university merit, Adams Fellowship for PhDs in exact/math/life sciences only, Rothschild postdoc, PBC/MALAG, the Iron Swords (חרבות ברזל) reservist framework via CHE + MoD, statutory tracks for bereaved families / wounded soldiers, and evacuee (מפונים) scholarships. Use when a student asks מלגה, פר\"ח, מלגת פריפריה, פיקדון, מלגת אדמס, מלגת רוטשילד, מלגת מילואים, חרבות ברזל, or how to fund tuition. Prevents missed deadlines, over-budgeting Mimadim, and humanities PhDs wasting an Adams application. Do NOT use for K-12, Bituach Leumi welfare (israeli-bituach-leumi), loans, MFA inbound-student scholarships, yeshiva stipends, or general post-army benefits (israeli-miluim-manager)."
license: MIT
---

# Israeli Academic Scholarships

## Problem

Israeli higher-education students leave money on the table every year because Israel's scholarship landscape is fragmented across the Ministry of Defense, the Ministry of Education, the Council for Higher Education (המל"ג), Nefesh B'Nefesh, the Rashi Foundation, ISEF, individual universities, and dozens of smaller foundations, each with its own eligibility filters, branding, deadlines, and application portals. Since October 2023 the picture changed materially: an entire war-economy scholarship framework now sits on top of the historical landscape and is the single largest active funding pool, but it is invisible to users who only know the pre-war scholarship names. A typical Israeli student is eligible for 3-5 distinct scholarships but knows about 1, and most application windows cluster in May-September with hard cutoffs that forfeit the year's grant if missed.

## Instructions

### Step 1: Profile the user

Before recommending scholarships, gather the dimensions that determine eligibility. Don't ask one at a time, ask in a single batched intake.

| Dimension | Why it matters |
|---|---|
| Degree level (BA, MA, PhD, postdoc) | Different scholarships per level; doctoral fellowships are an entirely different category |
| Institution (university name, faculty) | MALAG-recognized vs MAHAT-recognized vs other; each university has its own merit scholarships |
| Year of study | Some scholarships only target incoming freshmen, others target second-year-and-above |
| Field of study (humanities/social sciences vs exact/life sciences/math) | Adams Fellowship excludes humanities; HUJI women-in-CS-or-math is field-gated |
| Military service status (discharged soldier, Sherut Leumi, exemption) | Unlocks Pikadon, Mimadim LiLimudim, MoD periphery scholarship |
| Combat profile / lochem status if served | Required for Mimadim LiLimudim and combat-track Iron Swords support |
| Reserve days served since Oct 2023 (total cumulative) | Iron Swords thresholds (8+ days, 50+ days, 100+ days) drive distinct grants and credit-unit exemptions |
| Aliyah status (oleh chadash; toshav chozer) and aliyah years | Unlocks Student Authority / Minhal HaStudentim |
| Residence history (priority-area yishuv 5 of 6 years before studies) | MoD periphery scholarship gate |
| Evacuated household status (פינוי 7.10.2023 from עוטף עזה / north) | Unlocks evacuee tracks (Heznek La'Atid, university emergency funds) |
| Bereaved-family / wounded-soldier status (יתום מערכות ישראל / נכה צה"ל) | Unlocks statutory tracks via Misrad HaBitachon Family & Commemoration Branch |
| Bagrut average + psychometric score | University merit scholarships, Adams |
| Household socioeconomic status | MilGo (Ministry of Education), Rashi, ISEF |
| Athletic status (national-team representative) | Mifal HaPais athlete track |

### Step 2: Run the universal-eligibility checks first

These three apply to almost every Israeli student:

| Scholarship | Universal? | What to check |
|---|---|---|
| PEREACH (פר"ח) | Yes for any undergraduate | Willing to commit ~114 hours (NIS 7,000) or 140 hours (NIS 10,000) of tutoring per academic year. תשפ"ז registration opens in September and runs first-come-first-served until ~November (NOT the May-September cluster of most other scholarships). |
| MilGo (MoE socioeconomic) | Yes for any BA / hand-engineer / mechina student | Socioeconomic score determines tier. תשפ"ז cycle: Tier A NIS 12,480 / Tier B NIS 10,000 / Tier C NIS 7,500 / Tier D NIS 5,000. Cycle opens December via the Milgapo platform. |
| University merit scholarship at admission | Yes for any incoming freshman | Bagrut + psychometric thresholds vary per institution; many are automatic at registration. The MALAG-set baseline tuition is NIS 12,017 for תשפ"ו, but actual tuition varies by program (humanities track is below 100%, medicine/law/MBA is above 100%, often NIS 14,500-16,000+). |

Surface PEREACH first if the user is undergraduate, but flag the timing exception: PEREACH opens later than other scholarships and seats fill first-come-first-served.

### Step 3: Run the post-service checks (if applicable)

If the user served in the IDF or Sherut Leumi:

| Track | Eligibility | What it pays |
|---|---|---|
| Pikadon Hayashi | Any discharged soldier or Sherut Leumi alum, within the post-discharge window (5 years for most; verify current window for active reservists/lone soldiers on hachvana.mod.gov.il, as windows have been extended in some tracks since Oct 2023) | Personal deposit (the user's own money), usable for tuition at MALAG-recognized institutions and for psychometric prep, mechina, vocational training, or ישיבה גבוהה |
| MoD periphery scholarship (אזורי עדיפות לאומית) | Lived in a national-priority-area yishuv 5 of 6 years before studies, AND within the post-discharge window: 5 years standard, extended to 10 years for active reservists and lone soldiers | Up to 100% of first-year BA tuition (cap ~NIS 11,653, תשפ"ה/2025; refreshes for תשפ"ז). Cannot stack with other periphery scholarships. |
| Mimadim LiLimudim | Combat-veteran cohort + special populations (a large annual cohort). Eligibility window: 5 years post-discharge (regular service), extended by 1 year (to 6) for bagrut completion / mechina / psychometric within those 5 years, by 2 years (to 7) for continuous career service of a year or more, and by 3 years (to 8) for both. תשפ"ו application: opens 3.11.2025, closes 31.7.2026, document upload by 31.8.2026. | NOT flat 100%. Graduated funding: up to 85% of university tuition in EACH year of study, with a top-up in the FINAL year of study bringing the total to 100% of tuition actually paid. Annual cap NIS 10,214.45 (less than the NIS 12,017 baseline). A first-year combat veteran will pay 15% of tuition out of pocket up front, recovered only at graduation. |
| Atid Foundation tracks | Combat veterans (foundation track, distinct from MoD) | Per-track grant; check current cycle |
| IMPACT! (FIDF) | Former combat / combat-support soldiers from low-income backgrounds | USD 4,000/year for up to 4 years; requires ~130 community-service hours/year plus two donor thank-you letters/year. The best-known privately-funded combat-veteran academic fellowship. |

The Pikadon comes first chronologically, direct the user to use their own deposit before tapping external scholarships, but stress the MoD periphery scholarship cannot stack with other periphery scholarships, and stress Mimadim's graduated model so the user budgets correctly for Year 1.

### Step 4: Run the Iron Swords reservist checks (if served reserve duty since 7.10.2023)

This is the single largest active funding pool in Israel today and the skill's #1 routing target for any user who served reserve duty since October 2023. The framework is set by the Council for Higher Education (CHE/המל"ג) for academic years תשפ"ה through תשפ"ז and is operated jointly with the MoD, covering tens of thousands of reservist students.

| Threshold | What it pays | Notes |
|---|---|---|
| 8+ cumulative reserve days since 7.10.2023 | One-time NIS 1,100 grant | Universal floor - every reservist who hits 8 days qualifies |
| Reservist parent of children under 14 | Additional one-time NIS 2,000 grant | Stacks on top of the NIS 1,100 |
| 50+ days reserve service under Order 8 | One-time tuition grant up to ~NIS 11,653 (combat array, 2025 cohort qualifying window 27.10.2024-30.9.2025) | Check che.org.il/war/ for the current cohort's amount and qualifying window |
| Combat-track reservists with extended service | Higher-tier tuition support up to full tuition | Subject to current CHE framework, direct the user to che.org.il/war/ for the active cohort terms |
| 61-99 reserve days | 8 credit-unit exemption (electives + general courses) | Academic accommodation, not money, but materially reduces course load |
| 100+ reserve days | 10 credit-unit exemption | Same |

Two stacking rules to surface up front:
- The Iron Swords scholarship and Mimadim LiLimudim **cannot** be received in the same academic year. Pick the higher payout for the user's profile.
- The Iron Swords NIS 1,100 + NIS 2,000 child supplement stacks with PEREACH miluim supplement, MilGo, and Pikadon. It does not foreclose other tracks.

Surface this step before Step 6 (olim) for any reservist user, regardless of pre-Oct-2023 status, because the Iron Swords floor (NIS 1,100) is unconditional and easy to claim.

### Step 5: Statutory tracks for bereaved families, wounded soldiers, and evacuees

Three distinct statutory pipelines, each with its own intake and not addressed elsewhere:

| Track | Eligibility | What it pays |
|---|---|---|
| יתומי מערכות ישראל (orphans of fallen soldiers) and bereaved siblings | Statutory under חוק משפחות חיילים שנספו במערכה | Tuition support and stipends via Misrad HaBitachon Family & Commemoration Branch (אגף משפחות, הנצחה ומורשת); separate budget line from Mimadim/Periphery |
| נכי צה"ל (wounded soldiers) | Statutory under חוק הנכים (תגמולים ושיקום) | Tuition + rehabilitation support via the Rehabilitation Branch (אגף השיקום); intake through the user's case manager, not via hachvana portal |
| Evacuee (מפונים) tracks | Residents of עוטף עזה / north (Kiryat Shmona, Metula, Shlomi, etc.) evacuated since 7.10.2023 who became students 2024-2026 | TAU emergency fund (~NIS 2,500/student), Heznek La'Atid (heznek.org), university-by-university emergency funds |

For bereaved/wounded users, do NOT route through hachvana.mod.gov.il; the entitlement is handled by their dedicated case manager at אגף משפחות or אגף השיקום. The skill's role is to surface that this lane exists and to route the user to the right office, not to enumerate the per-case grant amounts.

### Step 6: Run the olim checks (if applicable)

If the user made aliyah and meets the Student Authority eligibility:

| Track | Eligibility |
|---|---|
| Student Authority (Minhal HaStudentim) | Oleh Chadash for BA. Deadlines are FIXED RECURRING dates, not a per-year cycle: semester A new students by 10 November, continuing students by 1 October, semester B by 1 April, summer semester by 15 August, every year. (Do not apply the MoD Mimadim dates here.) |
| Repatriate "Masa Harhava" track | Enrolled within 3 years of aliyah; up to ~90% tuition discount |
| NBN-coordinated foundation referrals | Olim from North America/UK; NBN routes to Student Authority + ISEF + foundations |

**Mahar / Achi disambiguation:** users may ask about "Mahar" or "Achi" by name. The current 2026 NBN higher-education portal does not list these as standalone scholarship products, direct the user to the NBN higher-ed page rather than treating the names as live programs.

### Step 7: Run the foundation checks

Surface these to any user with strong academic record OR socioeconomic need OR periphery residence:

| Foundation | Track | Range |
|---|---|---|
| Rashi Foundation | Katzir + Rakia | Tuition scholarship plus a living stipend and personal mentoring; Rashi does not publish per-track amounts, so ask the foundation |
| Rashi Foundation | Single-mother track | Amount not published; apply through Rashi's Katzir program |
| ISEF (Israel Scholarship Education Foundation) | BA-to-PhD in Israel | 400-500 Edmond J. Safra scholarships a year on 20 campuses across Israel; multi-year mentorship + leadership program included |
| ISEF | International MD/PhD/postdoc | International Fellows program for doctoral and postdoctoral study abroad; cohort size varies by year |

ISEF specifically targets first-generation / underserved students with strong academic merit, a common match for periphery + Mizrahi/Sephardi profiles.

### Step 8: Graduate-level scholarships (if MA / PhD / postdoc)

| Scholarship | Stage | Terms |
|---|---|---|
| Adams Fellowship (Israel Academy of Sciences and Humanities) | 2nd-year PhDs in **exact sciences, mathematics, and life sciences only** (NOT humanities, NOT social sciences, despite the institution's name including "humanities") | Full tuition + NIS 100,000/year stipend + USD 3,000/year travel; 3 years base, extendable by up to 1 more (4 max) |
| Aharon Katzir Postdoctoral Fellowship (Israel Academy of Sciences) | Postdoctoral, humanities and social sciences focus (the natural complement to Adams for humanities/social-sciences PhDs) | Multi-year postdoc-abroad track via the Academy |
| PBC / MALAG outstanding-doctoral-from-periphery | PhDs from periphery yishuvim | Council for Higher Education direct track |
| Maof program (PBC / MALAG) | Outstanding young scientists from Arab community | Faculty-integration pipeline |
| Rothschild Fellowship (Yad Hanadiv) | Postdoc abroad after PhD from Israeli university | Supplementary funds with a USD 75,000/year ceiling on **other** external supplementary funds. Receiving more than USD 75k/year in other support makes you ineligible (it is a ceiling on other funding, not a cap on the Rothschild itself). |

The Adams Fellowship application window is unusual, it opens in October-November and closes in early January for the *following* academic year. Surface this even if the user's deadline radar is set on May-September. Critically: a humanities or social-sciences PhD asking about Adams should be redirected to Aharon Katzir or other field-appropriate fellowships, Adams will reject the application.

### Step 9: Specialized tracks

Surface only if the profile matches:

- **Women in CS/Math at HUJI** - free first-year tuition.
- **Weizmann promotes-women-in-science** - aggregates national doctoral + postdoctoral-abroad fellowships (about 10 doctoral seats per year).
- **Mifal HaPais athlete track** - for athletes on the Israeli national representative team.
- **University faculty-specific awards** - pattern only; instruct the user to check the target faculty's scholarships page after applying for institutional awards.
- **PEREACH miluim supplement** - for PEREACH recipients who served reserve duty during the academic year, additional grant on top of the base; stacks with the Iron Swords NIS 1,100 floor.

### Step 10: Rank by deadline and recommend an application order

Once the eligible set is identified, rank by:

1. Imminent deadlines (anything closing in the next 30 days first)
2. Grant size (larger grants first within the same deadline tier)
3. Effort required (low-friction applications like automatic university merit go before essay-heavy foundation applications)

Two timing exceptions to remember:
- **PEREACH** opens September and is first-come-first-served until ~November. It is NOT in the May-September cluster despite popular belief.
- **Adams Fellowship** opens October-November and closes early January for the *following* academic year, so if it's January and the user is a 2nd-year PhD targeting next October, this is the most imminent deadline.

Most other scholarships have annual deadlines clustered in May-September for the October academic year.

### Step 11: Surface the disqualifiers and stacking rules

A few rules cut across multiple tracks. Surface them before the user applies:

- The MoD periphery scholarship cannot be combined with other periphery scholarships. Pick one.
- The Iron Swords tuition support and Mimadim LiLimudim cannot be received in the same academic year. Pick the higher payout for the user's cohort.
- The Pikadon is the user's own money, using it doesn't disqualify them from anything else.
- The Rothschild Fellowship has a USD 75,000/year ceiling on **other** external supplementary funds; exceeding it disqualifies, it does not just reduce the Rothschild amount.
- Most foundation grants (Rashi, ISEF) require declaring all other received grants in the application; under-declaration risks revocation.
- Mimadim LiLimudim is graduated (up to 85% each year, top-up in the FINAL year, so a 4-year engineering or medicine degree carries the gap for 3 years). Don't budget Year 1 at full tuition or the user is short ~15% out of pocket.
- Adams Fellowship is restricted to exact sciences, math, and life sciences. Don't recommend it to humanities or social-sciences PhDs; route them to Aharon Katzir or field-specific tracks instead.
- PEREACH commitments (~114 or 140 tutoring hours) are real and audited. Don't recommend it to a student who can't realistically commit.

## Recommended MCP Servers

| MCP | Why it pairs with this skill | Install |
|---|---|---|
| `kolzchut` (All-Rights / כל-זכות) | Authoritative entitlements knowledge base; covers PEREACH miluim supplement, Pikadon usage rules, Student Authority benefits, Iron Swords reservist rights | `npx skills-il add skills-il/kolzchut --skill kolzchut` |

## Reference Links

| Source | URL | What to Check |
|---|---|---|
| PEREACH official site | https://www.perach.org.il/ | Current grant amounts, hours, eligibility, current-cycle dates |
| PEREACH on Milgapo (cycle dates) | https://milgapo.co.il/?milga=_perach | תשפ"ז cycle open/close dates (September-November, first-come-first-served) |
| MoD periphery scholarship | https://www.hachvana.mod.gov.il/MainEducation/HachvanaScholarship/Pages/Perypheria45.aspx | Yishuv eligibility list, current tuition cap |
| Mimadim LiLimudim | https://www.hachvana.mod.gov.il/MainEducation/HachvanaScholarship/Pages/UniformToStudies.aspx | Combat-veteran cohort terms, graduated funding model, application windows, current annual cap |
| Pikadon (deposit) eligible institutions | https://www.hachvana.mod.gov.il/GrantAndDeposit/DepositUpTo5/Pages/education.aspx | Eligible institutions list, current post-discharge window rules |
| Sherut Leumi-Ezrachi rights portal | https://www.hachvana.mod.gov.il/luemi11/Pages/default.aspx | Pikadon and periphery eligibility for Sherut Leumi alumni |
| CHE Iron Swords framework | https://che.org.il/war/ | Current cohort tuition support tiers for combat / rear-service reservists, credit-unit exemption thresholds |
| NBN scholarships portal | https://www.nbn.org.il/life-in-israel/education/higher-education/scholarships-and-loans-for-university-and-college-students/ | Current routing for olim |
| ISEF Foundation | https://www.iseffoundation.org/edmond-j-safra-scholarships/ | Application cycles, eligibility, current fellow count |
| Milgapo (MoE socioeconomic + Rashi) | https://milgapo.co.il/ | Current scholarship branding, MilGo tier amounts |
| Adams Fellowship | https://adams.academy.ac.il/fellowships/ | Doctoral fellowship terms, application window, **eligible fields** |
| Aharon Katzir Postdoctoral Fellowship (humanities/social sciences) | https://www.academy.ac.il/RichText/GeneralPage.aspx?nodeId=1250 | Postdoc-abroad track for humanities/social-sciences PhDs |
| Rothschild Fellowship | https://www.yadhanadiv.org.il/rothschild-fellows/ | Postdoctoral fellowship cutoff dates, USD 75,000 ceiling on other funding |
| PBC / MALAG scholarships | https://che.org.il/en/scholarships-grants-students-faculty/pbc-scholarship-program-for-outstanding-doctoral-students/ | Council for Higher Education direct tracks |
| Student Authority application | https://www.gov.il/en/service/apply-online-for-a-scholarship-from-the-student-authority | Olim scholarship application portal, current eligibility window |
| Heznek La'Atid (evacuees) | https://heznek.org/ | Evacuee tuition support fund |

## Gotchas

1. **Mimadim LiLimudim is NOT flat 100% tuition.** It is graduated: up to 85% of actual courses in Years 1-2, then a final-year top-up to 100%, with an annual cap (NIS 10,214.45 in תשפ"ו) that is below the MALAG baseline tuition (NIS 12,017). A combat-veteran user budgeting Year 1 at full tuition will be short ~15% out of pocket. Always state the model explicitly when recommending Mimadim.
2. **Adams Fellowship excludes humanities and social sciences.** Despite the institution name "Israel Academy of Sciences and Humanities," the Adams call covers exact sciences, mathematics, and life sciences only. A philosophy or sociology PhD applying will be rejected. Route humanities/social-sciences PhDs to the Aharon Katzir postdoc track or field-specific fellowships.
3. **Iron Swords scholarships and Mimadim LiLimudim are mutually exclusive in the same year.** A combat-veteran reservist must pick the higher payout for their cohort, not stack both. The Iron Swords NIS 1,100 floor and the NIS 2,000 child supplement DO stack with PEREACH, MilGo, and Pikadon, however.
4. **PEREACH timing is NOT May-September.** The תשפ"ז cycle opens in September and runs first-come-first-served until ~November. A student told to apply in May for PEREACH will find no portal open; one told to wait until November may find the cohort full.
5. **SHEFI is not a scholarship.** It's the Ministry of Education's Psychological Counseling Service. The current Ministry of Education socioeconomic scholarship is branded "MilGo" via the Milgapo platform, with 4 tiers: A NIS 12,480 / B NIS 10,000 / C NIS 7,500 / D NIS 5,000. Many older guides conflate the two, don't.
6. **Mahar and Achi are recognizable names but not active standalone scholarships in 2026.** Olim users who ask for them by name should be redirected to the NBN higher-education portal, which now routes through Student Authority + ISEF + foundations.
7. **MoD periphery scholarship is exclusive, it cannot stack with another periphery scholarship.** Choosing it forecloses on the alternative; pick the one with the higher payout for the user's profile.
8. **The Pikadon is not a scholarship.** It's the soldier's own deposit. Using it doesn't reduce eligibility for external scholarships, but it also doesn't increase trust score with foundation reviewers, present it as a complement, not a substitute.
9. **The Rothschild USD 75,000/year is a CEILING on OTHER funding, not a cap on the Rothschild itself.** A postdoc with another fellowship paying USD 80,000/year is disqualified from Rothschild entirely; one with USD 70,000 of other funding is eligible. Read the wording carefully when relaying to users.
10. **PEREACH commitments are audited.** A student who skips tutoring sessions loses the grant retroactively. Never recommend PEREACH to a student who can't credibly commit to ~114 or 140 tutoring hours per year.
11. **The Adams Fellowship deadline is in early January, not May-September.** The default mental model of Israeli scholarship deadlines (May-September cluster) does not apply to doctoral fellowships. Surface the calendar misalignment proactively.
12. **MK Israel Foundation is unverified.** A user may ask about it by name based on older guides. Do NOT confirm its existence, direct them to verify via the institution's financial aid office before relying on it.
13. **Bereaved-family / wounded-soldier tracks do NOT route through hachvana.mod.gov.il.** They are handled by the user's case manager at אגף משפחות (Family & Commemoration Branch) or אגף השיקום (Rehabilitation Branch). Pointing the user at hachvana for these tracks wastes their time.
14. **University tuition is NOT a flat NIS 12,017.** That is the MALAG-set baseline (תשפ"ו). Actual tuition varies by program: humanities tracks run below 100%, medicine / law / MBA run above 100% (often NIS 14,500-16,000+ per year). When estimating coverage gaps for the user, use their actual program tuition, not the baseline.

## Troubleshooting

### Issue: Student missed the May-September window for the upcoming academic year

Most major scholarship cycles are annual and the missed cohort is genuinely closed. Five fallbacks: (a) the Pikadon (if eligible) doesn't have a cycle, it can be used at any point in the post-discharge window; (b) PEREACH is the exception, its window opens in September and runs first-come-first-served through November, so a "missed" May-September student may still get PEREACH; (c) Iron Swords NIS 1,100 floor for 8+ days reserve has a longer eligibility window, verify on che.org.il/war/; (d) university merit scholarships sometimes have rolling deadlines for late-admit students; (e) some foundations open winter rounds for spring-semester start. Be honest about which scholarships are off the table for this year.

### Issue: Student is in a periphery yishuv but for fewer than 5 of 6 years

The MoD periphery scholarship is hard-gated on residence history. Without 5 of 6 years, this specific track is closed. Pivot to: (a) Rashi Foundation (also periphery-focused but with different eligibility logic), (b) PBC/MALAG outstanding-doctoral-from-periphery (for PhDs), (c) ISEF (which weighs periphery as a factor but doesn't require it), (d) Iron Swords reservist tracks if the user served reserve duty (no residence gate).

### Issue: Student is a humanities PhD and asks about Adams Fellowship

Adams does not cover humanities. Route them to: (a) Aharon Katzir Postdoctoral Fellowship (Israel Academy of Sciences) for postdocs in humanities/social sciences; (b) Alix de Rothschild Fellowship (Israel Academy of Sciences, distinct from Yad Hanadiv Rothschild) for humanities-leaning postdocs; (c) Yad Hanadiv Rothschild for postdocs abroad after Israeli PhD (does cover humanities); (d) PBC/MALAG outstanding-doctoral-from-periphery if eligible. Don't let them waste an application.

### Issue: Combat-veteran reservist is offered both Iron Swords and Mimadim LiLimudim

They cannot be received in the same academic year. Compute the per-year value of each for the user's cohort and pick the higher. For most full-time combat veterans starting a BA, Mimadim's 85%-of-tuition (capped NIS 10,214/year) sums to roughly NIS 30,000+ over the full degree, which usually beats the Iron Swords combat-track support, but verify the current Iron Swords cohort percentage on che.org.il/war/ before committing. The choice is made per academic year, so a user can switch between tracks across years if cohort terms change.

### Issue: Student wants to combine multiple scholarships beyond their actual cap

Some foundations cap stacked grant value to a percentage of tuition. Surface this honestly, the combined-cap rule is a frequent source of revocation. Always tell the user to declare all received grants in each application; foundations cross-check.

## Bundled Resources

- `references/domain-checklist.md` - coverage map for fact-check / future updates
- `references/scholarship-table.md` - quick-reference table of all major Israeli scholarships
- `references/profile-questionnaire.md` - structured intake questions for matching
- `scripts/match_scholarships.py` - reference implementation of the eligibility-filter logic
