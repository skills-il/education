#!/usr/bin/env python3
"""Israeli special education committee deadlines, from a decision date.

Pure date arithmetic. No network access, so it runs on every host including sandboxed ones.

The periods encoded here are statutory and stable: 21 days to file an objection at both stages,
21 days for the deciding body to answer, and 14 days for the parents to notify their choice of
setting. The annual cycle dates (referral by 31 March, choice changes until 25 June) come from
the standing Ministry circular and recur every year; confirm them against the current circular.

Entitlement is counted in SCHOOL YEARS, not from the decision date: a decision in the spring cycle
takes effect the following September, and a renewal must be referred by 31 March of the last
school year the entitlement covers.

The day of receipt is not counted (Interpretation Law s.10(a)). A period whose last day is a
statutory rest day carries to the next day (s.10(c)). This script flags Saturdays only; it does
not know the Jewish holiday calendar, so check holidays yourself.

Usage:
  python3 deadline_calc.py --decision-date 2026-05-20 --from committee
  python3 deadline_calc.py --decision-date 2026-05-20 --from committee --has-choice --one-year
  python3 deadline_calc.py --decision-date 2023-05-22 --from committee
  python3 deadline_calc.py --decision-date 2026-05-20 --from team
  python3 deadline_calc.py --decision-date 2027-05-05 --has-choice --off-cycle
  python3 deadline_calc.py --example
"""

import argparse
import sys
from datetime import date, timedelta

OBJECTION_DAYS = 21       # s.13(a) and s.20e(a)
BODY_DECIDES_DAYS = 21    # s.13(c) and s.20e(b)
CHOICE_DAYS = 14          # s.7(b)(2)
POSITION_DAYS = 14        # s.7(b)(4)(b), from the committee's receipt of the parents' choice
DISCLOSURE_DAYS = 14      # s.9(b)(3), documents due BEFORE the hearing
PROTOCOL_DAYS = 14        # s.9(c)(2)
ENTITLEMENT_YEARS = 3     # s.10(a) re-hearing once every three years
CHOICE_CHANGE_UNTIL = (6, 25)   # circular 3.6.1(f): parents may change the setting type until 25 June
REFERRAL_BY = (3, 31)           # circular 3.6.1(a): referral until 31 March
# Wartime extension law 2023, s.1(a): decisions given in school years 2020/21 to 2022/23
# (identified here by the calendar year in which the school year ENDS).
WARTIME_SY_ENDS = (2021, 2022, 2023)

WEEKDAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

BODY = {
    "committee": ("ועדת זכאות ואפיון", "ועדת השגה"),
    "team": ("the school multidisciplinary team", "ועדת זכאות ואפיון"),
}


def parse_date(s, flag):
    try:
        y, m, d = (int(x) for x in s.split("-"))
        return date(y, m, d)
    except ValueError:
        sys.exit("%s: expected a real date as YYYY-MM-DD, got %r" % (flag, s))


def fmt(d, statutory=True):
    """ISO date and weekday; for a statutory period, a Saturday warning."""
    s = "%s (%s)" % (d.isoformat(), WEEKDAYS[d.weekday()])
    if statutory and d.weekday() == 5:
        s += "  [Saturday: s.10(c) of the Interpretation Law carries it to Sunday; do not plan on it]"
    return s


def school_year_end(d):
    """Calendar year in which the school year containing d ends (Sep-Aug convention)."""
    return d.year + 1 if d.month >= 9 else d.year


def sy_label(end_year):
    return "%d/%02d" % (end_year - 1, end_year % 100)


def first_year_end(decision_date, same_year):
    """End-year of the first school year the entitlement covers."""
    sy_end = school_year_end(decision_date)
    if same_year and decision_date.month not in (7, 8):
        return sy_end
    # Spring cycle, or an off-cycle decision in July/August implemented in the year about to start.
    return sy_end + 1


def is_off_cycle(decision_date, same_year, off_cycle=False):
    """Hearings run from early November to 31 May, continuation hearings to 15 July."""
    return off_cycle or same_year or decision_date.month in (9, 10)


def anniversary_passed(d):
    """First day on which a full year has passed since d (the start day is not counted)."""
    try:
        anniv = d.replace(year=d.year + 1)
    except ValueError:            # 29 February
        anniv = date(d.year + 1, 2, 28)
    return anniv + timedelta(days=1)


def renewal_lines(decision_date, years, same_year, today):
    first = first_year_end(decision_date, same_year)
    last = first + years - 1
    referral = date(last, *REFERRAL_BY)
    span = sy_label(first) if years == 1 else "%s to %s" % (sy_label(first), sy_label(last))
    out = ["  Covers school year%s %s (%d year%s)."
           % ("" if years == 1 else "s", span, years, "" if years == 1 else "s"),
           "  Renewal must be REFERRED by: %s  (circular date, file earlier if it falls on a weekend)"
           % fmt(referral, statutory=False)]
    if referral < today:
        out.append("  That date is already past (today %s)." % today.isoformat())
    return out


def report(decision_date, source, has_choice=False, hearing_date=None, one_year=False,
           same_year=False, today=None, off_cycle=False):
    today = today or date.today()
    out = []
    decided_by, appeal_to = BODY[source]
    out.append("Decision from: %s" % decided_by)
    out.append("Decision received: %s" % fmt(decision_date, statutory=False))
    out.append("")

    out.append("Objection (השגה)")
    deadline = decision_date + timedelta(days=OBJECTION_DAYS)
    out.append("  File with %s by: %s  (%d days, the day of receipt not counted)"
               % (appeal_to, fmt(deadline), OBJECTION_DAYS))
    filed = deadline + timedelta(days=1) if deadline.weekday() == 5 else deadline
    out.append("  They must decide by: %s if filed on the last day  (%d days from filing)"
               % (fmt(filed + timedelta(days=BODY_DECIDES_DAYS), statutory=False), BODY_DECIDES_DAYS))
    out.append("  Treat this filing date as HARD. The recorded-reasons extension in the statute applies")
    out.append("  to the body's own time to ANSWER, not to your time to file.")
    out.append("  Jewish holidays are NOT checked by this tool; a deadline on a statutory holiday also")
    out.append("  carries to the next day, but file before it.")
    if source == "committee":
        out.append("  The circular counts from receipt of BOTH the protocol and the reasoned decision.")
        out.append("  If the protocol arrived later, the clock may start later; use that only as an")
        out.append("  argument if you are already late. Who may file: student, parent, public organisation.")
    else:
        out.append("  The circular counts from receipt of the team's protocol AND written decision.")
        out.append("  Who may file against a TEAM decision: the student or a parent. If the contact details")
        out.append("  fail, the circular lets you file in a sealed envelope at the school, the מתי\"א or the")
        out.append("  local authority. No member of the team may sit on the committee hearing it.")

    if source == "committee":
        out.append("")
        out.append("Choice of setting type")
        if has_choice:
            cd = decision_date + timedelta(days=CHOICE_DAYS)
            out.append("  Notify the committee by: %s  (%d days)" % (fmt(cd), CHOICE_DAYS))
            out.append("  Miss it and the committee may decide the setting itself, giving priority")
            out.append("  to integration in a regular school.")
            change = date(school_year_end(decision_date), *CHOICE_CHANGE_UNTIL)
            if is_off_cycle(decision_date, same_year, off_cycle):
                out.append("  Off-cycle committee: you may CHANGE the chosen setting type only within 14 days")
                out.append("  of the day you deliver your choice, so at the latest: %s"
                           % fmt(cd + timedelta(days=CHOICE_DAYS), statutory=False))
            elif decision_date > change:
                out.append("  The 25 June change date for this cycle has passed: no change of setting type is")
                out.append("  possible after your notice, so decide before you notify.")
            else:
                out.append("  You may CHANGE the chosen setting type until: %s  (circular date)"
                           % fmt(change, statutory=False))
                if change < cd:
                    out.append("  That is before your notice deadline: notify by 25 June if you may want to change.")
                out.append("  If this was an off-cycle committee (ועדה חריגה), 25 June does not apply: change")
                out.append("  only within 14 days of delivering your choice. Re-run with --off-cycle.")
            out.append("")
            out.append("  If the committee moves to override your choice: you get an opportunity to state")
            out.append("  your position within %d days of the committee receiving your choice, the"
                       % POSITION_DAYS)
            out.append("  circular adds a second hearing, and the override needs the approval of the head")
            out.append("  of the special education division or the deputy. It is itself appealable.")
        else:
            out.append("  Not applicable, or not yet established. Whether a choice exists depends on")
            out.append("  the disability AND the function level. Check the choice table before")
            out.append("  telling a parent they may choose; several combinations carry no choice.")

        out.append("")
        out.append("Entitlement and renewal (counted in school years)")
        sy_end = school_year_end(decision_date)
        if one_year:
            out.append("  Suspected intellectual developmental disability: valid for ONE year only.")
            out.extend(renewal_lines(decision_date, 1, same_year, today))
            out.append("  An UPDATED admissible document is required for the renewal.")
            if sy_end in WARTIME_SY_ENDS:
                out.append("  Decided in a wartime-extension year: how the 2023 law applies to a one-year")
                out.append("  decision was not established. Ask the Ministry; all such dates have passed.")
        elif sy_end in WARTIME_SY_ENDS:
            out.append("  Decided in school year %s: the wartime extension law (2023) adds a fourth"
                       % sy_label(sy_end))
            out.append("  school year, and the head of the institution is exempt from the re-hearing.")
            out.extend(renewal_lines(decision_date, 4, same_year, today))
            if first_year_end(decision_date, same_year) in (2023, 2024):
                out.append("  EXCEPTION: no extension if three years have passed since the previous decision")
                out.append("  and next school year the child moves stage (compulsory kindergarten to primary,")
                out.append("  primary to middle or upper, middle to upper). In that case:")
                out.extend(renewal_lines(decision_date, ENTITLEMENT_YEARS, same_year, today))
        else:
            out.extend(renewal_lines(decision_date, ENTITLEMENT_YEARS, same_year, today))
            out.append("  If the characterisation is SUSPECTED intellectual developmental disability, it")
            out.append("  is valid for one year only: re-run with --one-year.")
        if same_year:
            out.append("  (Off-cycle decision implemented in the same school year, as you indicated.)")
        early = anniversary_passed(decision_date)
        out.append("  An earlier re-hearing normally needs a year to have passed since the DECISION")
        out.append("  (not its receipt), so from about %s if the decision was made that day."
                   % early.isoformat())
        out.append("  One earlier occasion is permitted before that, and further ones with district")
        out.append("  manager approval (the circular says two more).")

    out.append("")
    out.append("Protocol")
    out.append("  Due as far as possible at the end of the hearing, and no later than %d days from"
               % PROTOCOL_DAYS)
    out.append("  the end of the hearing or from delivery of the decision, whichever is EARLIER.")

    if hearing_date:
        out.append("")
        out.append("Pre-hearing disclosure (for a hearing on %s)" % hearing_date.isoformat())
        out.append("  Every document the committee may use was due to you by: %s  (%d days before)"
                   % ((hearing_date - timedelta(days=DISCLOSURE_DAYS)).isoformat(), DISCLOSURE_DAYS))
        out.append("  If it arrived later than that, say so at the hearing and ask for it to be")
        out.append("  recorded in the protocol.")

    out.append("")
    if source == "committee":
        out.append("After the objections committee")
        out.append("  Its decision is called final in the statute. That closes the administrative ladder")
        out.append("  only. An administrative petition lies to the District Court sitting as a court for")
        out.append("  administrative affairs. Where no other period is set, the court rules require the")
        out.append("  petition without delay and not later than 45 days from publication, from notice, or")
        out.append("  from the day the petitioner learned of the decision, whichever is EARLIEST. The court")
        out.append("  may extend that, and may also dismiss for delay inside the 45 days.")
        out.append("  That step is a lawyer's work; this tool does not advise on it.")
    else:
        out.append("After the entitlement committee decides the objection")
        out.append("  The circular allows a further objection to the district ועדת השגה, filed per the")
        out.append("  details in the decision letter. Diarise 21 days from receiving that decision, as for")
        out.append("  any entitlement-committee decision (s.13(a)), the day of receipt not counted. A team")
        out.append("  objection carries no setting choice; this tool does not compute choice or renewal")
        out.append("  dates for a decision on a team objection.")
    return out


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--decision-date", help="date the decision was RECEIVED, as YYYY-MM-DD")
    p.add_argument("--from", dest="source", choices=sorted(BODY), default="committee",
                   help="which body issued the decision")
    p.add_argument("--has-choice", action="store_true",
                   help="the parents have a choice of setting type for this disability and level")
    p.add_argument("--one-year", action="store_true",
                   help="the characterisation is suspected intellectual developmental disability")
    p.add_argument("--same-year", action="store_true",
                   help="off-cycle decision implemented in the current school year")
    p.add_argument("--off-cycle", action="store_true",
                   help="decision of an off-cycle committee (ועדה חריגה), whenever implemented")
    p.add_argument("--hearing-date", help="optional hearing date, to check the disclosure deadline")
    p.add_argument("--today", help="override today's date (YYYY-MM-DD), for testing")
    p.add_argument("--example", action="store_true")
    a = p.parse_args()

    today = parse_date(a.today, "--today") if a.today else None
    if a.example:
        print("Example: committee decision received 2026-05-20, parents have a choice,\n"
              "hearing was held on 2026-05-14\n")
        for line in report(date(2026, 5, 20), "committee", True, date(2026, 5, 14), today=today):
            print(line)
        return
    if not a.decision_date:
        p.error("--decision-date is required (or use --example)")
    hearing = parse_date(a.hearing_date, "--hearing-date") if a.hearing_date else None
    for line in report(parse_date(a.decision_date, "--decision-date"), a.source, a.has_choice,
                       hearing, a.one_year, a.same_year, today, a.off_cycle):
        print(line)


if __name__ == "__main__":
    main()
