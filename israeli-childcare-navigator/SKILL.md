---
name: israeli-childcare-navigator
description: "Navigate the Israeli childcare system from birth to age 12: daycare subsidies (ma'on yom), preschool registration (gan chova/trom-chova), Bituach Leumi child allowances, tza'haronim (after-school programs), and special education rights. Use when user asks about daycare, gan registration, child allowance, tza'haronim, special education committee (va'adat hashama), chinuch meyuchad, or any child-related benefit in Israel. Covers the full parent journey from infancy through elementary school. Do NOT use for Bituach Leumi contribution calculations or general NI benefits (use israeli-bituach-leumi), maternity leave (dmei leida), or Bagrut exams (use israeli-bagrut-psychometric)."
license: MIT
---

# Israeli Childcare Navigator

## Problem

Israeli parents face a fragmented system spanning multiple ministries and municipalities with different rules, deadlines, and eligibility criteria. Missing a gan registration window in February means losing your neighborhood placement. Applying late for daycare subsidies means paying full price for months. Parents of children with special needs must navigate the va'ada process with little guidance on their rights. This skill consolidates the entire childcare journey into one place, preventing costly mistakes and missed deadlines.

## Instructions

### Step 1: Identify the Parent's Situation

Determine which stage and need applies:

| Stage | Ages | Key Topics |
|-------|------|------------|
| Infancy | 0-3 | Daycare (ma'on/peuton) subsidies, child allowance, matapelet (nanny) options |
| Preschool | 3-5 | Gan registration (trom-trom-chova, trom-chova, gan chova), tza'haronim |
| Elementary | 6-12 | School registration, tza'haronim, special education, gifted programs |
| Cross-cutting | 0-18 | Child allowance (kiztavat yeladim), child savings plan (chisachon), special education |

### Step 1.5: After-Birth Registration Logistics

Before any benefits flow, several registration steps happen in the first few weeks. Cover these for any "I just had a baby" question:

1. **Birth registration**: most hospitals submit the registration directly to Misrad HaPnim (Ministry of Interior), but you must confirm and request the newborn's TZ (Israeli ID number). It's printed on the parent's TZ after the next update.
2. **Kupat cholim registration**: the newborn must be enrolled in a kupat cholim (HMO) within ~24 hours of hospital discharge to maintain coverage. Choose the kupa via Bituach Leumi (you can stay or switch from the parent's kupa) and notify the chosen HMO.
3. **Tipat Chalav (well-baby clinic)**: enroll the newborn in the local tipat chalav clinic for routine immunizations, growth monitoring, and developmental checkups in the first 6 years.
4. **Maternity grant (mae'nak leida)**: a one-time Bituach Leumi grant paid automatically when the hospital reports the birth. Amounts vary by birth order (highest for the first child). This is distinct from `dmei leida` (maternity-leave wages); the grant covers the equipment of the newborn (crib, layette).
5. **Child allowance kicks in automatically** after birth registration; see Step 5.

### Step 2: Daycare Subsidies (Ma'on Yom) -- Ages 0-3

Daycare subsidies are handled by the **Ministry of Labor, Social Affairs and Social Services** (Misrad HaAvoda), NOT the Ministry of Economy or Education.

**Eligibility criteria (both parents must meet at least one):**
- Working 24+ hours/week with minimum gross income of 3,333 NIS/month (couple) or 2,778 NIS/month (single parents and parents of three children)
- Enrolled in recognized studies 24+ hours/week (20 hours for single parents)
- Registered as unemployed with the Employment Service

**Registration is an annual window, not a rolling application.** Registration for a given
school year runs for about a month in mid-February to mid-March of the preceding calendar
year (for school year תשפ"ז it ran 15.02.2026 to 14.03.2026 and has closed). It is NOT
first-come-first-served within the window. Parents rank up to two recognized ma'onot;
where a ma'on is oversubscribed, acceptance committees between March and June apply the
Ministry's priority rules. Tell a parent asking outside the window when the next one opens
rather than sending them to an application they cannot submit.

**Application process:**
1. Verify the daycare is recognized by the Ministry (misrad haavoda registry)
2. Register via the Ministry's online service: https://www.gov.il/he/service/daycare-registration
3. Required documents: income verification, employment letter, identity documents
4. The Ministry assigns the family a **דרגה (grade)**, which sets the subsidy. See below.

**How much the subsidy is worth.** The state does not pay a percentage. It publishes a
tariff table per school year in which each grade has a fixed **parent share** and **state
share** in shekels. `references/maon-yom-tuition-tables.md` carries all six published
tables in full; consult it whenever a parent asks what they will actually pay.

**The tables govern a SCHOOL year (September to August), not a calendar year.** The
published tables are for **תשפ"ו (September 2025 to August 2026)**. As of August 2026 the
Ministry has **not yet published the תשפ"ז tables**. Always name the school year when
quoting a figure, and never present a תשפ"ו figure as governing תשפ"ז.

**There is no single ma'on table: there are four.** Which one applies depends on the
specific ma'on's operator type (מלכ"ר or שאינו מלכ"ר) and staffing standard (תקינה
בסיסית or תקינה מורחבת). At the 0-15-month band the full tariff ranges from 3,487 to
4,310 across the four, so guessing misstates the bill by hundreds of shekels a month.
**Ask the parent which operator type and staffing standard their ma'on has.** If they do
not know, tell them to ask the ma'on or call *2969, and give a range across the four
tables rather than one number. Mishpachtonim have a single table with no age dimension
(full tariff 2,819).

To orient a parent quickly, at the lowest grade (3) in a מלכ"ר תקינה בסיסית ma'on the
parent pays 1,159 of a 3,487 tariff for a 0-15-month place; at grade 10 the parent pays
2,438; at grades 11 and 12 there is no subsidy and the parent pays the full 3,487. Read
the actual cell from the reference file before quoting.

**Grades are set from per-capita income, with adjustments.** Per-capita income is the
parents' combined gross divided by household size (parents plus children up to 18); for a
single parent it is **half** their gross divided by (household size + 1). Two or more
enrolled children drop the grade by one; a grade-3 family with 2 enrolled children becomes
grade 14 and with 3 or more, grade 15. Some populations get a grade with no income test at
all (olim and returning residents, Otef Aza and Lebanon-border towns), and 60+ days of
miluim during 2024 drops the grade by one. Full rules and every income band are in the
reference file.

**Important notes:**
- New immigrants (olim) and returning residents receive grade 3 regardless of income
- Subsidy depends on space availability at recognized facilities
- Private (non-recognized) daycare centers do not qualify for subsidy
- A grade a parent believes is wrong can be corrected, and a mid-year change of
  circumstances must be reported to the Ministry

### Step 3: Preschool Registration (Gan) -- Ages 3-5

Municipal preschool registration is handled by the local **Education Department (Agaf Chinuch)**.

**Age categories (by Gregorian birth year, Jan 1 - Dec 31):**

| Level | Hebrew Name | Age | Compulsory |
|-------|-------------|-----|------------|
| Trom-Trom Chova | טרום-טרום חובה | Turning 3 | No (free since 2015-16 under Compulsory Education Law Amendment 9) |
| Trom-Chova | טרום חובה | Turning 4 | No (free since 2015-16 under Compulsory Education Law Amendment 9) |
| Gan Chova | גן חובה | Turning 5 | Yes (Compulsory Education Law) |

**Registration timeline:**
- **December:** Municipalities send registration information to parents
- **February-March:** Registration window (exact dates vary by municipality)
- Missing the window does NOT mean no placement, but you lose neighborhood priority

**Registration process:**
1. First-time registration requires in-person visit to Agaf Chinuch
2. Required documents: parents' ID copies showing child's name and address, proof of residency
3. Choose religious orientation: Mamlachti (secular), Dati (religious), Torani, Charedi
4. Pay parent payments (tashlumei horim) for enrichment, insurance and similar. These are set per municipality and school, not nationally. The Ministry of Education publishes an updated list each year of compulsory and optional services and the MAXIMUM price chargeable for each. Ask the municipality for its figure and check it against that year's ceiling rather than quoting a national number.

**Religious framework:** The municipality must honor your religious orientation choice but is not obligated to assign a specific gan.

### Step 4: Afternoon Programs (Tza'haronim)

Tza'haronim provide supervision after gan/school hours, typically until 16:00-17:00.

- Operated separately from the regular gan (different staff, separate registration)
- Additional tuition required (varies by municipality and provider)
- Some municipalities offer subsidized tza'haronim for eligible families
- Registration is usually done through the municipality or the specific gan

### Step 5: Child Allowance (Kiztavat Yeladim)

**Paid by Bituach Leumi to all Israeli residents with children under 18.**

Monthly amounts (2026):

| Children | Per Child | Total Example |
|----------|-----------|---------------|
| 1st child | 173 NIS | 173 NIS |
| 2nd child | 219 NIS | 392 NIS |
| 3rd child | 219 NIS | 611 NIS |
| 4th child | 219 NIS | 830 NIS |
| 5th+ child | 173 NIS | 1,003 NIS |

- Paid on the 20th of each month, automatically
- No application needed (starts automatically after birth registration)
- Amounts are CPI-adjusted each January, always confirm against the Bituach Leumi rates page for the current year
- **Supplement for a parent on a subsistence benefit.** A parent receiving havtachat hachnasa, mezonot, an old-age pension with income supplement, or a survivors' pension with income supplement receives an extra **113 NIS** for the **third and fourth** child. This is easy to miss and lands on exactly the lowest-income families.

**Child Savings Plan (Chisachon LeKol Yeled):**
- Bituach Leumi deposits 58 NIS/month per child into a savings plan
- Parents can opt to add another 58 NIS/month from the child allowance (total 116 NIS/month)
- Money is available to the child at age 18
- Parents choose between bank deposit or provident fund (kupat gemel) via the Bituach Leumi website
- One-time bonus of ~582 NIS added by Bituach Leumi if the child does not withdraw before age 21

### Step 5a: Disabled Child Allowance (Kiztavat Yeled Nechet)

If a child has a recognized disability (developmental, physical, sensory, or psychiatric), the family is entitled to a separate disabled child allowance, distinct from regular kiztavat yeladim.

- Amounts (from 01.01.2026): the allowance is a percentage of a full individual pension of 3,820 NIS. There are **five** entitlement levels, not a continuous range:

| Level | Monthly amount |
|-------|----------------|
| 50% | 1,943 NIS |
| 100% | 3,820 NIS |
| 112% | 4,501 NIS |
| 188% | 7,181 NIS |
| 235% | 9,126 NIS |

- A child with more than one qualifying medical condition is paid at the highest single qualifying level, not the sum.
- **Ventilator-dependent (monsham) supplement: 10,774 NIS/month.** For a child assessed at 100%, 112% or 188% it is paid on top of that level. For a child assessed at 235% the supplement is paid but the base drops to the 188% level (7,181 instead of 9,126). Do not tell a family at 235% they will receive 9,126 plus the supplement.
- **Two-caregiver supplement: 7,182 NIS/month**, where the Institute's physician has determined two carers are needed, a permit for two is held, and two are actually employed. It cannot be combined with the 235% level (the base is paid at 188% instead), and cannot be combined with the ventilator supplement.
- **Two or more disabled children in one family:** each child's allowance is increased by 50% of their own assessed level. A family with one child at 100% and one at 50% is paid at 150% and 75% respectively. This is paid automatically. It continues even if the second child's allowance is not actually being paid because the child is in a residential or foster placement, or because payment stopped only on reaching age 18.
- **Child in an institution:** 673 NIS/month at the 50% level, 1,347 NIS/month at 100% and above.
- Eligibility is determined by a medical committee (Bituach Leumi) and depends on the disability type and severity, NOT means-tested on parental income.
- Application: submit Bituach Leumi form 7821 with medical documentation. Initial decisions take 60-90 days.
- The allowance is paid alongside the standard child allowance and the child savings plan continues.
- For developmental-delay diagnoses surfaced via the Va'ada (Step 6), ask Bituach Leumi to assess eligibility for kiztavat yeled nechet as a separate track; the Va'ada itself does not trigger this benefit.
- Always confirm current 2026 amounts at the Bituach Leumi disabled-child page before quoting figures to a parent.

### Step 5b: Income Tax Credit Points (Nekudot Zikui) for Parents

Working parents receive additional tax credit points (nekudat zikui) per child. This is a tax benefit, not a direct payment, and reduces the parent's monthly income tax. The Israel Tax Authority sets the credit point at 2,904 NIS for the 2025 tax year, about 242 NIS/month, and the value is unchanged for 2026. Confirm the current year's value before quoting a shekel saving.

Credit points run to age 18, not to age 5 or 12, and the bands are keyed to the **tax year in which the child reaches an age**, not to the child's age on a given date.

| Tax year | Mother | Father |
|----------|--------|--------|
| Year of birth | 2.5 | 2.5 |
| Year after birth, through the year the child turns 2 | 4.5 | 4.5 |
| Year the child turns 3 | 3.5 | 3.5 |
| Years the child turns 4 and 5 | 2.5 | 2.5 |
| Year the child turns 6, through the year before the child turns 18 | 2.0 | 1.0 |
| Year the child turns 18 | 0.5 | none |

A single parent with the child in their custody receives one further credit point for being
a single-parent family, on top of the per-child points. A parent living apart who bears part
of the children's upkeep receives one point. Separate or divorced parents not running a
joint household are each entitled to the disabled-child points where those apply.

There are two additional child-linked credits worth flagging: two points per child who is
paralysed, blind, or has an intellectual-developmental disability, a severe attention and
concentration learning disability, or a serious illness causing developmental delay
(Ordinance s.45); and, alternatively, a 35% credit on institutional-maintenance costs above
12.5% of taxable income (s.44). A parent must choose one or the other per child, not both.

Always verify the current point allocation and the per-point shekel value via the Israel Tax Authority (`https://www.gov.il/he/departments/israel_tax_authority`) before quoting an exact monthly tax saving.

### Step 6: Special Education (Chinuch Meyuchad) -- Ages 3-18

Governed by the **Special Education Law 1988**, significantly reformed by **Amendment 11 (2018)**.

**The Va'adat Zakaut ve-Ipyun (Eligibility and Characterization Committee):**

Amendment 11 (2018) renamed the old "Va'adat Hashama" (placement committee) to "Va'adat Zakaut ve-Ipyun" (eligibility and characterization committee). The colloquial name "va'adat hashama" is still widely used.

This is an external government body (not school-based) that determines:
- Eligibility for special education services
- The service basket (sal sherutim) the child receives
- Support hour allocation (3-5 hours for mild needs, up to 21+ hours for profound needs)

**Key change in Amendment 11:** Parents now choose the educational framework (regular school with inclusion, special ed class in regular school, or special education school). The committee determines eligibility and service level, but the placement choice belongs to the parents.

**Committee composition:** Ministry of Education official with special education expertise (chair), psychologist, social worker, special education supervisor, and sometimes physicians or therapists.

**Process timeline:**
1. School-based intervention and identification (3-6 months)
2. Referral to Va'ada with documentation
3. Psychoeducational evaluation. A private assessment is expensive and the price varies widely by institute, region, and how many sessions the assessment runs to. Do not quote a figure. Many local authorities operate learning-disability assessment and support centres that reduce or cover the cost, so tell the parent to ask their local authority first.
4. Committee meeting (2-4 months after referral)
5. Decision issued (2-4 weeks post-meeting)
6. Service implementation (2-3 months)

**Placement continuum:**

| Level | Description | Support Hours |
|-------|-------------|---------------|
| Regular class with support | Mainstream class, pull-out services | 3-12 hours/week |
| Integration class (kita meshulevet) | Mixed abilities, co-taught | Varies |
| Special education class | Small group (6-12 students), within regular school | Full day |
| Specialized school (beit sefer meyuchad) | Comprehensive, therapy-integrated | Full day + therapies |

**Available services:** Speech therapy, occupational therapy, physical therapy, psychological services, assistive technology.

**Parental rights (strengthened by Amendment 11):**
- Right to choose the educational framework (regular, special ed class, or special school)
- Right to attend the committee meeting
- Right to bring an advocate or professional
- Right to file an objection (hashaga) to the regional committee, then to the national committee
- Right to request reevaluation annually

**Testing accommodations (for Bagrut and classroom tests):**
- Extended time (25-50%)
- Reader/scribe services
- Computer use
- Separate quiet room
- Oral exams (rare, requires special approval)

### Step 7: Gifted Programs (Mechunot LiMechonanim)

- Identification begins around grade 2-3 through school-administered tests
- Gifted programs are available in select schools (not all municipalities)
- The Ministry of Education's Division for Gifted and Outstanding Students manages the program
- Pull-out enrichment programs typically 1 day/week
- Full-time gifted classes exist in some cities (Tel Aviv, Jerusalem, Haifa)

### Step 8: Helpline and Government Information

When parents need to talk to a human or escalate, point them to these official entry points:

- **`*2969` (Ministry of Labor daycare hotline):** the dedicated hotline for ma'on yom subsidies, recognized-facility lookup, and ma'on application status. This is the number parents actually need for daycare subsidy questions.
- **`118` (Ministry of Welfare general hotline):** 24/7 multilingual hotline for general social services, family welfare, and child protection questions that fall outside the daycare-subsidy track.
- **`*6050` (Bituach Leumi):** for child allowance (kiztavat yeladim), Chisachon LeKol Yeled, and disabled child allowance (kiztavat nechut).
- **`105` (MAOR):** national child-protection online hotline for online harm and abuse reports.
- **Ministry of Welfare daycare portal:** `https://www.gov.il/he/service/daycare-registration` for subsidy eligibility, online applications, and the recognized facility lookup.
- **Kol Zchut (childcare entitlements portal):** `https://www.kolzchut.org.il/he/ילדים_ונוער` for plain-language summaries of every benefit, with appeal templates and recent updates.

## Examples

### Example 1: First-time Parent with Newborn
User says: "I just had a baby, what benefits and registrations should I know about?"
Actions:
1. Explain child allowance starts automatically after birth registration (173 NIS/month for first child)
2. Walk through after-birth registration logistics: confirm birth registration + newborn TZ, enroll in kupat cholim within 24h of discharge, enroll in tipat chalav, confirm mae'nak leida grant (Step 1.5)
3. Recommend choosing savings plan option (bank vs. kupat gemel) via Bituach Leumi website
4. If both parents work, guide through daycare subsidy application (Step 2)
4. Note the gan registration timeline (February-March when child turns 3)
Result: Parent has a clear timeline and action list from birth through preschool.

### Example 2: Gan Registration
User says: "How do I register my child for gan chova?"
Actions:
1. Determine child's age and birth year to confirm level (trom-trom-chova/trom-chova/gan chova)
2. Explain registration window (February-March) and that it's done at the municipal Agaf Chinuch
3. List required documents (IDs, proof of residency)
4. Explain religious orientation options (Mamlachti, Dati, Torani, Charedi)
5. Note that parent payments apply (capped annually by the Ministry of Education) and mention the tza'haron option
Result: Parent knows exactly when, where, and how to register.

### Example 3: Special Education Concerns
User says: "My child's teacher suggested we consider special education evaluation"
Actions:
1. Explain the Va'adat Hashama process and timeline
2. Clarify the placement continuum (inclusion in regular class is an option)
3. Note parental rights (attend meeting, bring advocate, appeal)
4. Advise on psychoeducational evaluation: private assessment is faster but costly, and the local authority may run a subsidised assessment centre
5. Emphasize: request in writing, keep copies of all documents
Result: Parent understands the process, their rights, and how to prepare.

## Bundled Resources

### References
- `references/childcare-timeline.md` -- Complete timeline of registrations, deadlines, and milestones from birth to age 12. Consult when creating a personalized plan for parents.
- `references/special-education-rights.md` -- Detailed guide to the Va'ada process, parental rights, appeal procedures, and available services. Consult when advising on special education.
- `references/maon-yom-tuition-tables.md` -- All six published תשפ"ו tuition and subsidy tables (four ma'on variants, mishpachtonim, extra hour), the income bands, and the grade-setting rules. Consult whenever a parent asks what daycare will actually cost them.
- `references/domain-checklist.md` -- Coverage contract for this domain: what the skill must cover, what is deliberately out of scope, and why.

## Reference Links

| Source | URL | What to Check |
|--------|-----|---------------|
| Ministry of Labor - Daycare Subsidy | https://www.gov.il/he/service/daycare-registration | Ma'on yom registration window, recognized facilities, online application |
| Ministry of Labor - Tuition Tables | https://www.gov.il/he/pages/tuition-daycare-and-supervised-nurseries?chapterindex=3 | Published tariff and subsidy tables per school year, and whether the next year's tables are out yet |
| Bituach Leumi - Child Allowance | https://www.btl.gov.il/benefits/children/Pages/default.aspx | Current monthly amounts, payment schedule, savings plan options |
| Bituach Leumi - Disabled Child Allowance | https://www.btl.gov.il/benefits/Disabled_Child/Pages/default.aspx | Eligibility, amounts, form 7821 |
| Israel Tax Authority - Credit Points | https://www.gov.il/he/departments/israel_tax_authority | Annual nekudat zikui value and per-child allocation |
| Ministry of Education - Preschool | https://www.gov.il/he/departments/ministry-of-education | Compulsory education ages, registration calendar, religious streams (navigate to preschool/early-childhood section) |
| Kol Zchut - Children and Youth | https://www.kolzchut.org.il/he/ילדים_ונוער | Plain-language entitlements, appeal templates, recent updates |
| Helpline *2969 (Ministry of Labor daycare hotline) | https://www.gov.il/he/service/daycare-registration | Direct hotline for ma'on yom subsidy and facility list |
| Helpline 118 (Ministry of Welfare general hotline) | https://www.gov.il/he/departments/molsa | Social services, family welfare, child protection |

## Gotchas

1. **Wrong ministry for daycare subsidies.** Agents often attribute daycare subsidies to the Ministry of Education or Ministry of Economy. The correct authority is the **Ministry of Labor, Social Affairs and Social Services** (Misrad HaAvoda). Getting this wrong sends parents to the wrong office.

2. **Gan registration is municipal, not national.** There is no single national registration system. Each municipality runs its own process with different dates, fees, and forms. Always ask which city the parent lives in before giving registration instructions.

3. **Child allowance amounts change annually.** The 2026 amounts (173/219 NIS per child) are CPI-adjusted each January. Do not use previous year's figures. Always specify the year when stating amounts.

4. **The committee was renamed in 2018.** Amendment 11 renamed "ועדת השמה" (Va'adat Hashama) to "ועדת זכאות ואפיון" (Va'adat Zakaut ve-Ipyun). Both names are used colloquially, but the legal name is the new one. Critically, Amendment 11 gave parents the right to choose the educational framework -- do not tell parents the committee decides placement. The committee decides eligibility and service basket; the parents choose where their child learns.

5. **Free education does not mean zero cost.** While gan tuition is covered from age 3 (under Amendment 9, since school year 2015-16), municipalities charge parent payments for enrichment, insurance, and the parent committee (vaad horim), and a tza'haron is charged separately on top. Agents should never tell parents "gan is completely free." Nor should they invent a shekel figure: parent payments are set locally within an annual Ministry of Education price ceiling, so the honest answer is to name the components and send the parent to the municipality for the amount.

6. **Major cities have moved gan registration online.** First-time municipal registration in Tel Aviv, Jerusalem, Haifa, Rishon LeZion, Petach Tikva and several others is digital-first since ~2023. In-person Agaf Chinuch visits are now exceptions for missing documents or special cases, not the default. Always ask which city; recommend the municipal portal first.

7. **The daycare tariff is a school-year table, and four tables exist.** Two failure modes compound here. First, quoting a תשפ"ו figure without saying so lets it read as current indefinitely; the תשפ"ז tables were still unpublished in August 2026. Second, there is no single ma'on rate: the operator type and staffing standard select one of four tables that differ by hundreds of shekels a month. Ask which ma'on, and name the school year.

8. **Ma'on registration closes.** Registration is a roughly one-month national window in February-March for the following school year, not a rolling application. An agent that tells a parent in June to "apply online" has sent them to a closed form.

9. **Disabled child allowance is a separate Bituach Leumi track.** If the Va'ada (Step 6) surfaces a developmental delay, parents must apply for kiztavat yeled nechet separately (Bituach Leumi form 7821). The Va'ada itself does not trigger this allowance. Missing this leaves up to thousands of shekels/month on the table for eligible families.

## Troubleshooting

### Problem: "Parent missed the gan registration window"
Cause: Registration was in February-March and parent didn't register on time.
Solution: Contact the municipal Agaf Chinuch directly. Missing the window does NOT mean no placement, but the municipality assigns you a gan without neighborhood priority. They must still honor your religious orientation choice.

### Problem: "Daycare subsidy application was rejected"
Cause: Common reasons include income below minimum threshold, daycare not on recognized list, or missing documentation.
Solution: Verify the daycare is on the Ministry of Labor's recognized facility list. Check income meets minimum (3,333 NIS/month for couples). New immigrants should mention oleh status for up to 2 years of automatic eligibility. Appeal through the Ministry.

### Problem: "Parent disagrees with Va'ada placement decision"
Cause: Va'ada placed child in more restrictive setting than parent wants, or denied services.
Solution: Parents have the right to appeal to the regional Va'ada, and then to the national Va'ada. The Integration Law (2002) gives weight to parental preference for inclusion. Recommend bringing a special education advocate to the appeal hearing.
