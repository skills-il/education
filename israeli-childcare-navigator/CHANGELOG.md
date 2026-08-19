# Changelog

## 1.3.0 - 2026-08-19

Added the ma'on yom subsidy amounts. The skill previously stated eligibility
precisely and then said only that the subsidy "depends on income tier and family
size", so a working parent could not get a number out of it. All six published
תשפ"ו tables are now encoded in full in `references/maon-yom-tuition-tables.md`:
the four מעון tables (מלכ"ר and שאינו מלכ"ר, each in תקינה בסיסית and תקינה
מורחבת), the mishpachtonim table, and the extra-hour table, plus the income bands
and the grade-setting rules. Step 2 now instructs the agent to ask which operator
type and staffing standard the ma'on has, because the four tables differ by
hundreds of shekels a month.

Stated the school-year boundary. The tariff runs September to August, and the
תשפ"ז tables were not published as of 19 August 2026. Both facts are now in the
skill so the תשפ"ו figures cannot silently read as current.

Added the ma'on registration window (a roughly one-month national window in
February-March, not first-come-first-served, with acceptance committees between
March and June).

Corrected the income-tax credit-point table, which was wrong in every band. Points
run to age 18, not 12, and are keyed to the tax year in which the child reaches an
age: 2.5 / 4.5 / 3.5 / 2.5, then 2.0 for the mother and 1.0 for the father from age
6 to the year before 18, and 0.5 for the mother in the year of 18.

Enumerated the five disabled-child allowance levels instead of quoting a range,
and added the ventilator interaction at 235% (the supplement is paid but the base
drops to the 188% level), the two-caregiver supplement and its exclusions, the
50% uplift for two or more disabled children, and the institutional rates.

Added the 113 NIS child-allowance supplement for the third and fourth child paid
to a parent receiving a subsistence benefit.

Removed two cost ranges that their cited sources do not support: the 2,500-4,500
NIS psychodidactic assessment figure and the 300-700 / 500-1,200 / 6,000-12,000
NIS parent-payment figures. Both pages carry no shekel amounts at all. They are
replaced with what the sources do support, including the Ministry of Education's
annual maximum-price list for parent payments.

Created `references/domain-checklist.md`, which did not previously exist.

## 1.2.3 - 2026-08-11

Corrected the scope of the lower daycare-subsidy income floor: the 2,778 NIS
threshold applies to single parents AND parents of three children, not to single
parents alone. Verified against gov.il/he/pages/daycare-subsidie.
