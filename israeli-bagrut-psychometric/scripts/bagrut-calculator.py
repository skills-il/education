#!/usr/bin/env python3
"""
Bagrut & Psychometric Calculator

Calculate Bagrut subject grades, weighted averages with bonus points,
and estimated university admission scores (sekhem).

Usage:
    python bagrut-calculator.py --mode subject --exam 82 --magen 90
    python bagrut-calculator.py --mode average --subjects "math:5:88,english:5:92,history:3:78"
    python bagrut-calculator.py --mode sekhem --bagrut-avg 95.5 --psychometric 680
    python bagrut-calculator.py --mode bonus --grade 88 --units 5
"""

import argparse
import sys


GRADE_MIN, GRADE_MAX = 0, 100
PET_MIN, PET_MAX = 200, 800
VALID_UNITS = (1, 2, 3, 4, 5)


def _check_range(value: float, low: float, high: float, label: str) -> float:
    """Reject out-of-range input instead of silently computing nonsense."""
    if value < low or value > high:
        print(f"Error: {label} must be between {low} and {high} (got {value}).")
        sys.exit(1)
    return value


def calculate_subject_grade(exam_score: float, magen_score: float) -> float:
    """Calculate final Bagrut subject grade: 70% exam + 30% magen.

    70/30 is the majority rule. Some subjects publish a different split, and where
    alternative school-based assessment is heavy the school share can exceed 30%.
    Check the Ministry's current-year subject document before relying on this for a
    specific subject.
    """
    _check_range(exam_score, GRADE_MIN, GRADE_MAX, "exam score")
    _check_range(magen_score, GRADE_MIN, GRADE_MAX, "magen score")
    return round(exam_score * 0.7 + magen_score * 0.3, 1)


# Representative flat 5-unit bonus by subject (varies by university; these are
# typical values). University bonuses are NOT tiered by score; they are a flat
# per-subject amount awarded only when the subject grade is at least 60.
# Per-institution tables, transcribed from each institution's own published page.
# There is NO national bonus table, so the caller must say which institution applies
# (--institution technion|tau) or pass an explicit --bonus. Keyed in English AND
# Hebrew: the audience types Hebrew subject names, and an unrecognised name silently
# fell through to a generic value before v1.4.0.
#
# Technion (admissions.technion.ac.il/calculation-of-the-median-grade/):
#   5 units: maths 30; physics/chemistry/biology/recognised technological 25;
#   literature/Bible/history/English/Arabic/Hebrew-for-Arabic-speakers 25; other 20.
#   4 units: 10 for its listed "other subjects" group.
# TAU (go.tau.ac.il/b.a_direct/how-to-calculate):
#   5 units: maths 35; English/physics/chemistry/biology/Arabic/literature/history/
#   Bible 25; other listed 20.  4 units: English and maths 12.5; other listed 10.
TECHNION_5U = {
    "math": 30, "mathematics": 30, "מתמטיקה": 30,
    "physics": 25, "פיזיקה": 25,
    "chemistry": 25, "כימיה": 25,
    "biology": 25, "ביולוגיה": 25,
    "english": 25, "אנגלית": 25,
    "literature": 25, "ספרות": 25,
    "history": 25, "היסטוריה": 25,
    "bible": 25, "tanakh": 25, "תנך": 25, 'תנ"ך': 25,
    "arabic": 25, "ערבית": 25,
}
TECHNION_4U_OTHER = 10

TAU_5U = {
    "math": 35, "mathematics": 35, "מתמטיקה": 35,
    "physics": 25, "פיזיקה": 25,
    "chemistry": 25, "כימיה": 25,
    "biology": 25, "ביולוגיה": 25,
    "english": 25, "אנגלית": 25,
    "literature": 25, "ספרות": 25,
    "history": 25, "היסטוריה": 25,
    "bible": 25, "tanakh": 25, "תנך": 25, 'תנ"ך': 25,
    "arabic": 25, "ערבית": 25,
}
TAU_4U = {"english": 12.5, "אנגלית": 12.5, "math": 12.5, "mathematics": 12.5, "מתמטיקה": 12.5}
TAU_4U_OTHER = 10

INSTITUTIONS = {
    "technion": {"five": TECHNION_5U, "four": {}, "four_other": TECHNION_4U_OTHER,
                 "five_other": 20, "label": "Technion"},
    "tau": {"five": TAU_5U, "four": TAU_4U, "four_other": TAU_4U_OTHER,
            "five_other": 20, "label": "Tel Aviv University"},
}

# Retained only so an explicit --bonus is not required for a rough sanity check.
DEFAULT_BONUS_5U = {
    "math": 30,
    "mathematics": 30,
    "מתמטיקה": 30,
    "physics": 25,
    "פיזיקה": 25,
    "chemistry": 25,
    "כימיה": 25,
    "biology": 25,
    "ביולוגיה": 25,
    # Computer Science is deliberately ABSENT: neither the Technion's nor TAU's
    # published 5-unit table names it in a +25 row, so it falls through to the
    # generic value and emits the "pass --bonus" warning rather than guessing.
    "english": 25,
    "אנגלית": 25,
    "literature": 25,
    "ספרות": 25,
    "history": 25,
    "היסטוריה": 25,
    "bible": 25,
    "tanakh": 25,
    "תנך": 25,
    'תנ"ך': 25,
    "arabic": 25,
    "ערבית": 25,
}
DEFAULT_BONUS_5U_OTHER = 20
MIN_GRADE_FOR_BONUS = 60


def get_bonus_points(grade: float, units: int, subject: str = "", override=None,
                     institution: str = None) -> float:
    """Per-institution flat bonus, gated at grade >= 60. Covers 5 AND 4 units.

    `override` (from --bonus) always wins. Otherwise `institution` selects a
    transcribed table. With neither, a generic table is used and a warning is
    emitted, because no national bonus table exists.
    The bonus is NOT tiered by score.
    """
    if grade < MIN_GRADE_FOR_BONUS or units not in (4, 5):
        return 0
    if override is not None:
        return override
    key = subject.strip().lower()

    if institution:
        tbl = INSTITUTIONS[institution]
        if units == 5:
            return tbl["five"].get(key, tbl["five_other"])
        return tbl["four"].get(key, tbl["four_other"])

    if units == 4:
        print(
            f"Note: 4-unit bonuses differ sharply by institution (Tel Aviv University "
            f"pays 12.5 for 4-unit English and maths, the Technion 10 for its listed "
            f"group). Pass --institution or --bonus; 0 assumed for '{subject}'.",
            file=sys.stderr,
        )
        return 0
    if key not in DEFAULT_BONUS_5U:
        print(
            f"Note: '{subject}' is not in the built-in bonus table, so the generic "
            f"+{DEFAULT_BONUS_5U_OTHER} was used. Pass --bonus with your target "
            f"university's exact figure.",
            file=sys.stderr,
        )
    print(
        "Note: no institution given, so a GENERIC bonus table was used. No national "
        "table exists. Re-run with --institution technion|tau or --bonus.",
        file=sys.stderr,
    )
    return DEFAULT_BONUS_5U.get(key, DEFAULT_BONUS_5U_OTHER)


def calculate_weighted_average(subjects: list[dict], institution: str = None) -> dict:
    """
    Calculate Bagrut weighted average with bonus points.

    subjects: list of dicts with keys: name, units, grade
    Returns dict with average details.
    """
    total_weighted = 0
    total_units = 0
    details = []

    for subj in subjects:
        name = subj["name"]
        units = subj["units"]
        grade = subj["grade"]
        bonus = get_bonus_points(grade, units, name, subj.get("bonus"), institution)
        grade_with_bonus = grade + bonus

        total_weighted += grade_with_bonus * units
        total_units += units

        details.append({
            "name": name,
            "units": units,
            "grade": grade,
            "bonus": bonus,
            "grade_with_bonus": grade_with_bonus,
        })

    average = round(total_weighted / total_units, 2) if total_units > 0 else 0

    return {
        "average": average,
        "total_units": total_units,
        "subjects": details,
    }


def calculate_sekhem(
    bagrut_avg: float,
    psychometric: float,
    bagrut_weight: float = 40,
    psychometric_weight: float = 60,
) -> dict:
    """
    Calculate estimated university admission score (sekhem).

    Uses a normalized scale where both components are brought to a 0-100 range
    and then weighted.
    """
    _check_range(bagrut_avg, 0, 200, "bagrut average")
    _check_range(psychometric, PET_MIN, PET_MAX, "psychometric score")
    psychometric_normalized = (psychometric / 800) * 100
    sekhem = round(
        (bagrut_avg * bagrut_weight / 100)
        + (psychometric_normalized * psychometric_weight / 100),
        2,
    )

    return {
        "sekhem": sekhem,
        "bagrut_avg": bagrut_avg,
        "bagrut_weight": bagrut_weight,
        "psychometric": psychometric,
        "psychometric_normalized": round(psychometric_normalized, 2),
        "psychometric_weight": psychometric_weight,
    }


def parse_subjects(subjects_str: str) -> list[dict]:
    """Parse subjects like 'math:5:88,english:5:92:25,history:3:78'.

    Format: name:units:grade[:bonus]. The optional 4th field is the exact
    university bonus for that 5-unit subject; if omitted, a representative
    typical value is used.
    """
    subjects = []
    for item in subjects_str.split(","):
        parts = item.strip().split(":")
        if len(parts) not in (3, 4):
            print(f"Error: Invalid subject format '{item}'. Use name:units:grade[:bonus]")
            sys.exit(1)
        units = int(parts[1])
        if units not in VALID_UNITS:
            print(f"Error: '{parts[0]}' has {units} units; must be one of {VALID_UNITS}.")
            sys.exit(1)
        _check_range(float(parts[2]), GRADE_MIN, GRADE_MAX, f"grade for '{parts[0]}'")
        subjects.append({
            "name": parts[0],
            "units": units,
            "grade": float(parts[2]),
            "bonus": float(parts[3]) if len(parts) == 4 else None,
        })
    return subjects


def main():
    parser = argparse.ArgumentParser(
        description="Bagrut & Psychometric Calculator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  Calculate a single subject grade:
    %(prog)s --mode subject --exam 82 --magen 90

  Calculate Bagrut weighted average:
    %(prog)s --mode average --subjects "math:5:88,english:5:92,history:3:78,bible:3:80"

  Estimate university admission score (sekhem):
    %(prog)s --mode sekhem --bagrut-avg 95.5 --psychometric 680

  Check bonus points for a grade:
    %(prog)s --mode bonus --grade 88 --units 5
        """,
    )

    parser.add_argument(
        "--mode",
        choices=["subject", "average", "sekhem", "bonus"],
        required=True,
        help="Calculation mode",
    )
    parser.add_argument("--exam", type=float, help="Exam score (for subject mode)")
    parser.add_argument("--magen", type=float, help="Magen score (for subject mode)")
    parser.add_argument(
        "--subjects",
        type=str,
        help='Subjects as "name:units:grade,..." (for average mode)',
    )
    parser.add_argument(
        "--bagrut-avg", type=float, help="Bagrut average (for sekhem mode)"
    )
    parser.add_argument(
        "--psychometric", type=float, help="Psychometric score (for sekhem mode)"
    )
    parser.add_argument(
        "--bagrut-weight",
        type=float,
        help="Bagrut weight in sekhem. REQUIRED: there is no default, because no "
             "Israeli institution publishes a fixed split.",
    )
    parser.add_argument(
        "--psychometric-weight",
        type=float,
        help="Psychometric weight in sekhem. REQUIRED, see --bagrut-weight.",
    )
    parser.add_argument(
        "--institution",
        choices=sorted(INSTITUTIONS),
        help="Which institution's published bonus table to use (technion or tau). "
             "Without it a generic table is used and a warning is printed.",
    )
    parser.add_argument("--grade", type=float, help="Grade (for bonus mode)")
    parser.add_argument("--units", type=int, help="Study units (for bonus mode)")
    parser.add_argument("--subject", type=str, help="Subject name (for bonus mode, picks the typical bonus)")
    parser.add_argument("--bonus", type=float, help="Exact university bonus for the subject (overrides the typical value)")

    args = parser.parse_args()

    if args.mode == "subject":
        if args.exam is None or args.magen is None:
            parser.error("--exam and --magen are required for subject mode")
        grade = calculate_subject_grade(args.exam, args.magen)
        print(f"\nSubject Grade Calculation")
        print(f"{'='*40}")
        print(f"Exam score:      {args.exam}")
        print(f"Magen score:     {args.magen}")
        print(f"Formula:         ({args.exam} x 0.7) + ({args.magen} x 0.3)")
        print(f"Final grade:     {grade}")

    elif args.mode == "average":
        if args.subjects is None:
            parser.error("--subjects is required for average mode")
        subjects = parse_subjects(args.subjects)
        result = calculate_weighted_average(subjects, args.institution)
        print(f"\nBagrut Weighted Average Calculation")
        print(f"{'='*60}")
        print(
            f"{'Subject':<15} {'Units':>5} {'Grade':>6} {'Bonus':>6} {'With Bonus':>11}"
        )
        print(f"{'-'*60}")
        for s in result["subjects"]:
            print(
                f"{s['name']:<15} {s['units']:>5} {s['grade']:>6.1f} "
                f"{s['bonus']:>+6.1f} {s['grade_with_bonus']:>11.1f}"
            )
        print(f"{'-'*60}")
        print(f"Total units:         {result['total_units']}")
        print(f"Weighted average:    {result['average']}")
        print(
            "\nNote: this averages EVERY subject you entered. Universities compute a"
            "\nbest average, dropping the subjects that lower it, so treat this as a"
            "\nfloor rather than as the number the university will use."
        )

    elif args.mode == "sekhem":
        if args.bagrut_avg is None or args.psychometric is None:
            parser.error(
                "--bagrut-avg and --psychometric are required for sekhem mode"
            )
        if args.bagrut_weight is None or args.psychometric_weight is None:
            parser.error(
                "--bagrut-weight and --psychometric-weight are REQUIRED and have no "
                "defaults. No Israeli institution publishes a fixed bagrut/"
                "psychometric split: Tel Aviv University states its formula changes "
                "yearly and uses a linear transformation, and the Technion publishes "
                "formulas per faculty. Whatever you pass is YOUR assumption, not an "
                "institutional figure. Use the institution's own calculator for a "
                "real number."
            )
        result = calculate_sekhem(
            args.bagrut_avg,
            args.psychometric,
            args.bagrut_weight,
            args.psychometric_weight,
        )
        print(f"\nSekhem estimate on YOUR assumed weighting (not an institutional figure)")
        print(f"{'='*50}")
        print(f"Bagrut average:          {result['bagrut_avg']}")
        print(f"Bagrut weight:           {result['bagrut_weight']}%")
        print(f"Psychometric score:      {result['psychometric']}")
        print(
            f"Psychometric normalized: {result['psychometric_normalized']} (out of 100)"
        )
        print(f"Psychometric weight:     {result['psychometric_weight']}%")
        print(f"{'-'*50}")
        print(f"Estimated Sekhem:        {result['sekhem']}")
        print(
            "\nNote: this is a rough orientation figure ONLY. No Israeli university"
            "\npublishes a 40/60 split. Tel Aviv University states its formula changes"
            "\nyearly and uses a linear transformation; the Technion publishes formulas"
            "\nper faculty. Use the target institution's own sekhem calculator."
        )

    elif args.mode == "bonus":
        if args.grade is None or args.units is None:
            parser.error("--grade and --units are required for bonus mode")
        _check_range(args.grade, GRADE_MIN, GRADE_MAX, "grade")
        if args.units not in VALID_UNITS:
            print(f"Error: units must be one of {VALID_UNITS} (got {args.units}).")
            sys.exit(1)
        bonus = get_bonus_points(args.grade, args.units, args.subject or "",
                                 args.bonus, args.institution)
        print(f"\nBonus Points Calculation")
        print(f"{'='*40}")
        print(f"Grade:           {args.grade}")
        print(f"Units:           {args.units}")
        print(f"Subject:         {args.subject or '(generic)'}")
        print(f"Institution:     {args.institution or '(none given)'}")
        print(f"Bonus points:    +{bonus}")
        print(f"Grade for avg:   {args.grade + bonus}")
        if args.grade < MIN_GRADE_FOR_BONUS:
            print(f"\nNote: grade is below {MIN_GRADE_FOR_BONUS}, so no bonus is awarded.")
        if args.units not in (4, 5):
            print(f"\nNote: bonuses are awarded for 5-unit subjects and, at a lower "
                  f"rate, for some 4-unit subjects. {args.units} units earns nothing.")
        if args.bonus is None and args.institution is None:
            print("\nNote: bonuses are flat per subject and vary by university, and")
            print("there is no national table: 5-unit English is +25 at both the")
            print("Technion and Tel Aviv University, while 5-unit maths is +30 at the")
            print("Technion and +35 at TAU. Pass --institution or --bonus.")

if __name__ == "__main__":
    main()
