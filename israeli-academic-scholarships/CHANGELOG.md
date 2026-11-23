# Changelog

## 1.4.0 - 2026-11-23

- Reservist benefits rebuilt from the IDF Reserve Aid Fund in `references/reservist-benefits.md`: grants by year and unit tier, places where official pages disagree, and credit relief.
- Corrected funding facts: Mimadim NIS 10,372.55 on a NIS 12,203 ceiling and its funded years, IMPACT USD 5,000, MilGo levels and aid caps, the cancelled MilGo and Mimadim offset, Adams second-year stage and fields, and PEREACH hours.
- Periphery tracks now state the state-budgeted institution limit and the yearly re-application for track 46. The Student Authority now states its age, timing and tariff limits.
- Humanities PhDs now route to the Alix de Rothschild Fellowship. Maskila and Rakia now point to the Welfare Ministry. Removed claims that could not be confirmed.
- The matcher now fails open: anything it cannot settle prints as CHECK instead of disappearing.

## 1.3.1 - 2026-11-23

- Corrective release. Removed the advice to pick the higher of Mimadim and the reservist grant. A student who holds or may still apply for Mimadim uses it first and does not cancel it. Anyone not entitled goes to the Reserve Aid Fund.
- Added the live dates near the top: Mimadim תשפ"ז is open 8.11.2026 to 31.8.2027, the 31.12.2026 last claim date for past-year reservist grants and early תשפ"ו private lessons, the תשפ"ו tuition-grant window to 30.6.2027, and the one-year claim rule for other entitlements from 1.1.2026.
- The script now prints that its list is not complete.

## 1.3.0 - 2026-08-19

- Added a Cycle-status box to both language files. Every Mimadim / MoD date in
  the skill was the תשפ"ו cycle, which closed 31.7.2026, and read as if it were
  live. The box states the check date, what has closed, and that תשפ"ז dates are
  NOT yet published for the MoD tracks, so the absence cannot read as an
  oversight.
- Surfaced the one window still open: document upload for already-accepted
  תשפ"ו Mimadim applicants runs to 31.8.2026.
- The Student Authority is explicitly NOT on the MoD cycle. Its deadlines are
  fixed recurring dates (1.10 and 10.11 next), as Step 6 always said.
- match_scholarships.py no longer manufactures false ineligibility: MilGo is
  open to any BA / mechina / hendesai student and the socioeconomic score
  selects the tier rather than gating entry. University merit and ISEF no
  longer require a bagrut average of 100.
- The tier helper returns the full ladder and states that the ministry computes
  the tier from a composite score whose band edges are not published, instead of
  quoting one shekel figure as a determination. Rashi amounts, which the
  foundation does not publish, are no longer emitted as figures.
- Mimadim funding corrected to up to 85% in EVERY year except the last, per the
  MoD page, replacing "Years 1-2" which understated the gap on 4 and 6-year
  degrees.
- Aligned the Mimadim document-upload deadline on 31.8.2026 (the official MoD
  date); references and the script had 30.8.2026.
- MoD periphery cap refreshed from ~NIS 11,653 (תשפ"ה/2025) to NIS 12,017
  (תשפ"ו/2026). The separate ~NIS 11,653 Order-8 reservist grant is unchanged.
- Added a legal notice and a description clause.

## 1.2.2 - 2026-08-11

Four corrections. Mimadim LiLimudim pays up to 85% in EACH year with the top-up in the final year, not '85% in years 1-2 with a year-3 top-up' (a 4-year degree carries the gap for 3 years). Its eligibility window extends to 8 years, not 6-7. Its document deadline is 31.8.26, not 30.8.2026. Most seriously, the Student Authority row carried the MoD Mimadim dates; its real deadlines are fixed recurring dates (10 Nov / 1 Oct / 1 Apr / 15 Aug).

