#!/usr/bin/env python3
"""Israeli special education committee deadlines, from a decision date.

Pure date arithmetic. No network access, so it runs on every host including sandboxed ones.

The periods encoded here are statutory and stable: 21 days to file an objection at both stages,
21 days for the deciding body to answer, and 14 days for the parents to notify their choice of
setting. The annual CYCLE dates are set by circular and are re-issued every year, so this script
does not encode them. Read them off the current circular.

Usage:
  python3 deadline_calc.py --decision-date 2026-05-20 --from committee
  python3 deadline_calc.py --decision-date 2026-05-20 --from team --has-choice
  python3 deadline_calc.py --example
"""

import argparse
from datetime import date, timedelta


def add_years(d, n):
    """Add n years, clamping 29 February to 28 February in a non-leap target year."""
    try:
        return d.replace(year=d.year + n)
    except ValueError:
        return d.replace(year=d.year + n, day=28)

OBJECTION_DAYS = 21       # s.13(a) and s.20e(a)
BODY_DECIDES_DAYS = 21    # s.13(c) and s.20e(b)
CHOICE_DAYS = 14          # s.7(b)(2)
POSITION_DAYS = 14        # s.7(b)(4)(b), parents' opportunity before an override
DISCLOSURE_DAYS = 14      # s.9(b)(3), documents due BEFORE the hearing
PROTOCOL_DAYS = 14        # s.9(c)(2)
ENTITLEMENT_YEARS = 3     # circular; s.10(a) sets the re-hearing duty, not the validity
EARLY_REVIEW_DAYS = 365   # s.10(b), a year must pass, with one permitted exception

BODY = {
    "committee": ("ועדת זכאות ואפיון", "ועדת השגה"),
    "team": ("the school multidisciplinary team", "ועדת זכאות ואפיון"),
}


def parse_date(s):
    y, m, d = (int(x) for x in s.split("-"))
    return date(y, m, d)


def report(decision_date, source, has_choice=False, hearing_date=None):
    out = []
    decided_by, appeal_to = BODY[source]
    out.append("Decision from: %s" % decided_by)
    out.append("Decision received: %s" % decision_date.isoformat())
    out.append("")

    out.append("Appeal (השגה)")
    deadline = decision_date + timedelta(days=OBJECTION_DAYS)
    out.append("  File with %s by: %s  (%d days)" % (appeal_to, deadline.isoformat(), OBJECTION_DAYS))
    out.append("  They must decide by: %s if filed on the last day  (%d days from filing)"
               % ((deadline + timedelta(days=BODY_DECIDES_DAYS)).isoformat(), BODY_DECIDES_DAYS))
    out.append("  This filing date is HARD. The recorded-reasons extension in the statute applies to")
    out.append("  the body's own time to ANSWER, not to your time to file.")

    if source == "committee":
        out.append("")
        if has_choice:
            cd = decision_date + timedelta(days=CHOICE_DAYS)
            out.append("Choice of setting type")
            out.append("  Notify the committee by: %s  (%d days)" % (cd.isoformat(), CHOICE_DAYS))
            out.append("  Miss it and the committee may decide the setting itself, giving priority")
            out.append("  to integration in a regular school.")
            out.append("")
            out.append("  If the committee moves to override your choice: you get %d days to state"
                       % POSITION_DAYS)
            out.append("  your position, and the override needs the approval of the head of the")
            out.append("  special education division or the deputy. It is itself appealable.")
        else:
            out.append("Choice of setting type")
            out.append("  Not applicable, or not yet established. Whether a choice exists depends on")
            out.append("  the disability AND the function level. Check the choice table before")
            out.append("  telling a parent they may choose; several combinations carry no choice.")

        out.append("")
        out.append("Entitlement and renewal")
        renew = add_years(decision_date, ENTITLEMENT_YEARS)
        out.append("  Generally runs %d years, so to about: %s, or until an earlier committee convenes."
                   % (ENTITLEMENT_YEARS, renew.isoformat()))
        out.append("  EXCEPTION: ANY suspected intellectual developmental disability")
        out.append("  characterisation, mild, moderate or severe/profound, is recorded as")
        out.append("  valid for ONE year only. If that is the characterisation, the")
        out.append("  renewal is %s, not the date above."
                   % add_years(decision_date, 1).isoformat())
        early = decision_date + timedelta(days=EARLY_REVIEW_DAYS)
        out.append("  An earlier re-hearing normally needs a year to have passed, so from about %s."
                   % early.isoformat())
        out.append("  One earlier occasion is permitted before that, and further ones with district")
        out.append("  manager approval.")

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
    out.append("After the objections committee")
    out.append("  Its decision is called final in the statute. That closes the administrative ladder")
    out.append("  only. An administrative petition lies to the District Court sitting as a court for")
    out.append("  administrative affairs. Where no other period is set, the court rules require the")
    out.append("  petition without delay and not later than 45 days from publication, from notice, or")
    out.append("  from the day the petitioner learned of the decision, whichever is EARLIEST.")
    out.append("  That step is a lawyer's work; this tool does not advise on it.")
    return out


def main():
    p = argparse.ArgumentParser(description=__doc__,
                                formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--decision-date", help="date the decision was RECEIVED, as YYYY-MM-DD")
    p.add_argument("--from", dest="source", choices=sorted(BODY), default="committee",
                   help="which body issued the decision")
    p.add_argument("--has-choice", action="store_true",
                   help="the parents have a choice of setting type for this disability and level")
    p.add_argument("--hearing-date", help="optional hearing date, to check the disclosure deadline")
    p.add_argument("--example", action="store_true")
    a = p.parse_args()

    if a.example:
        print("Example: committee decision received 2026-05-20, parents have a choice,\n"
              "hearing was held on 2026-05-14\n")
        for line in report(date(2026, 5, 20), "committee", True, date(2026, 5, 14)):
            print(line)
        return
    if not a.decision_date:
        p.error("--decision-date is required (or use --example)")
    hearing = parse_date(a.hearing_date) if a.hearing_date else None
    for line in report(parse_date(a.decision_date), a.source, a.has_choice, hearing):
        print(line)


if __name__ == "__main__":
    main()
