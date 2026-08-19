# Domain coverage checklist: Israeli Childcare Navigator

Scope: the Israeli childcare and early-education system from birth to age 12, covering
daycare subsidies, preschool and school registration, National Insurance child benefits,
after-school programmes, and special-education rights.

Created 2026-08-19 (v1.3.0). This file is the anchor for the Expert Review gate and the
record of what is deliberately excluded. Re-litigate every "Out of scope" row each cycle.

## Must cover (core)

| Item | Why it is core | Status |
|---|---|---|
| Ma'on yom subsidy **amount** per grade, per age band, per operator type | A working parent's actual monthly bill. Stating eligibility without amounts leaves the central question unanswered. This was the v1.2.3 defect. | Covered: `references/maon-yom-tuition-tables.md`, all six tables |
| The **four** separate ma'on tables (מלכ"ר / שאינו מלכ"ר x תקינה בסיסית / מורחבת) | The 0-15 band ranges from a 3,487 tariff to a 4,310 tariff across the four tables. Collapsing them to one is a wrong answer, not a simplification. | Covered: Step 2 instructs the agent to ask; reference file carries all four |
| Mishpachtonim table (separate, no age dimension) | A distinct framework with its own tariff and its own table. | Covered: Table E |
| Extra-hour (שעה נוספת) subsidy table | The only hours-linked amount in the tariff system. | Covered: Table F |
| **School-year boundary** and which year the tables govern | The tariff runs Sept-Aug. Undated figures silently read as current forever. | Covered: Step 2 and the reference file header both name תשפ"ו and state that תשפ"ז is unpublished |
| Grade-setting rules: per-capita income formula, single-parent halving, sibling reduction, grades 14/15 | Without these a parent cannot find their own row. | Covered: reference file, "Grade-setting rules" |
| Income-test-free grades (olim, Otef Aza, Lebanon border) | Named entitlement categories an ordinary user falls into. | Covered: reference file |
| Miluim grade reduction (Swords of Iron) | Time-limited but live and widely applicable. | Covered: reference file |
| Ma'on subsidy **eligibility** (work/study hours, minimum income) | Gates access to everything above. | Covered: Step 2 |
| Ma'on **registration window** (annual, roughly mid-Feb to mid-March) | Registration is a closed annual window, not a rolling application. A parent told "apply online" in August will miss the year. | Covered: Step 2 |
| Child allowance amounts by birth position | The single most-asked figure in the domain. | Covered: Step 5 |
| Child allowance supplement for parents on a subsistence benefit | A named entitlement worth 113 NIS per child for the 3rd and 4th child, affecting exactly the lowest-income families. | Covered: Step 5 |
| Chisachon LeKol Yeled mechanics | Automatic, universal, and requires a parent decision. | Covered: Step 5 |
| Disabled-child allowance: **enumerated** entitlement levels, not a range | A parent at an intermediate severity level cannot read their amount off a range. | Covered: Step 5a, five levels plus supplements |
| Ventilator supplement and its interaction with the 235% level | The 235% case is a genuine trap: the supplement is paid but the base drops to 188%. | Covered: Step 5a |
| Two-caregiver supplement and its exclusions | Named entitlement with two mutual exclusions. | Covered: Step 5a |
| Multi-disabled-child 50% uplift | Automatic, materially large, and easy to miss. | Covered: Step 5a |
| Income-tax credit points per child, by age band, mother and father separately | Directly changes net monthly pay. The v1.2.3 table was wrong in every band. | Covered: Step 5b |
| Preschool levels, compulsory ages, registration timeline | Missing the window costs neighbourhood priority. | Covered: Step 3 |
| Special education: committee name and function post-Amendment 11, parental framework choice, objection route | Amendment 11 moved the placement decision to parents. Getting this wrong misstates a legal right. | Covered: Step 6, `references/special-education-rights.md` |
| After-birth registration logistics (birth registration, kupat cholim, tipat chalav, maternity grant) | The first-weeks checklist a new parent needs. | Covered: Step 1.5 |
| Official escalation channels (*2969, 118, *6050, 105) | Every workflow needs a human fallback. | Covered: Step 8 |

## Should cover (advanced)

| Item | Why | Status |
|---|---|---|
| Grade correction and mid-year change-of-circumstances procedure | Parents assigned a wrong grade have a real remedy. | Covered: reference file |
| Ministry grade simulator | Lets a parent estimate before applying. | Covered: reference file |
| Ma'on placement mechanics (two ranked choices, acceptance committees March-June, not first-come-first-served) | Corrects a common and costly misconception. | Covered: Step 2 |
| Tza'haron subsidy variation by municipality | Real cost driver. | Covered: Step 4 |
| Gifted-programme identification route | Narrow but frequently asked. | Covered: Step 7 |
| Testing accommodations | Follows from a special-education finding. | Covered: Step 6 |

## Out of scope (explicit)

| Item | Rationale (reviewed 2026-08-19) |
|---|---|
| תשפ"ז (2026-27) tuition tables | **Not published by the Ministry as of 2026-08-19.** This is an absence of source data, not an editorial choice. The skill states the absence explicitly so it cannot read as an oversight. Re-check on the next cycle: this is the highest-priority carry item. |
| Dmei leida (maternity-leave wages) | A distinct National Insurance benefit with its own eligibility and calculation. Named as an anti-trigger in the description. |
| General National Insurance contribution calculations | Handled by `israeli-bituach-leumi`. Named as an anti-trigger. |
| Bagrut and psychometric exams | Handled by `israeli-bagrut-psychometric`. Named as an anti-trigger. |
| Per-municipality gan fees, tza'haron prices, and registration dates | Set independently by ~250 local authorities and changed annually. No authoritative national table exists. The skill gives the national range and instructs the agent to ask which city and route to the municipal portal. Re-litigated 2026-08-19: still uncapturable, and a fabricated municipal figure would be worse than a routing instruction. |
| Exact per-severity special-education support-hour entitlements | The committee sets the service basket per child; the bands in the skill are labelled illustrative for this reason. Carried from the v1.2.1 cycle. Re-litigated 2026-08-19: still not published as a statutory table. |
| Statutory objection (hashaga) window in days | Not sourced to an authoritative text in this or the prior cycle. The skill points at the decision notice, which carries the operative deadline. Carried. |
| Institutional (מוסד) disabled-child rates beyond the two headline figures | Narrow population; the two published figures are stated and the skill routes to Bituach Leumi for the rest. |

## Authoritative sources

| Source | URL | Use for |
|---|---|---|
| Ministry of Labour, tuition tables | https://www.gov.il/he/pages/tuition-daycare-and-supervised-nurseries?chapterindex=3 | All six tariff and subsidy tables, published per school year |
| Ministry of Labour, ma'on registration | https://www.gov.il/he/service/daycare-registration | Registration window, placement mechanics |
| Kol Zchut, participation grades | https://www.kolzchut.org.il/he/דרגות_השתתפות_במימון_מעונות_יום_ומשפחתונים | Grade-setting rules, income-test-free categories |
| Bituach Leumi, child allowance amounts | https://www.btl.gov.il/benefits/children/Pages/שיעורי%20הקצבה.aspx | Per-child amounts, subsistence-benefit supplement |
| Bituach Leumi, disabled-child allowance amounts | https://www.btl.gov.il/benefits/Disabled_Child/Pages/שיעורי%20הגמלה.aspx | Five entitlement levels, supplements |
| Israel Tax Authority, "דע זכויותיך וחובותיך" | https://www.gov.il/he/pages/income-tax-guide-knowyourright | Credit points per child by age, credit-point value |
