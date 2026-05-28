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


def calculate_subject_grade(exam_score: float, magen_score: float) -> float:
    """Calculate final Bagrut subject grade: 70% exam + 30% magen."""
    return round(exam_score * 0.7 + magen_score * 0.3, 1)


# Representative flat 5-unit bonus by subject (varies by university; these are
# typical values). University bonuses are NOT tiered by score; they are a flat
# per-subject amount awarded only when the subject grade is at least 60.
DEFAULT_BONUS_5U = {
    "math": 30,
    "mathematics": 30,
    "physics": 25,
    "chemistry": 25,
    "biology": 25,
    "computer science": 25,
    "cs": 25,
    "english": 20,
}
DEFAULT_BONUS_5U_OTHER = 20
MIN_GRADE_FOR_BONUS = 60


def get_bonus_points(grade: float, units: int, subject: str = "", override=None) -> float:
    """Flat per-subject 5-unit bonus, gated at grade >= 60.

    Bonuses apply to 5-unit subjects (4-unit math/English get smaller bonuses at
    most universities, not modeled here). If `override` is given it is used as the
    university's exact bonus for this subject. Otherwise a representative typical
    value is used. The bonus is NOT tiered by score.
    """
    if units != 5 or grade < MIN_GRADE_FOR_BONUS:
        return 0
    if override is not None:
        return override
    return DEFAULT_BONUS_5U.get(subject.strip().lower(), DEFAULT_BONUS_5U_OTHER)


def calculate_weighted_average(subjects: list[dict]) -> dict:
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
        bonus = get_bonus_points(grade, units, name, subj.get("bonus"))
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
        subjects.append({
            "name": parts[0],
            "units": int(parts[1]),
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
        default=40,
        help="Bagrut weight in sekhem (default: 40)",
    )
    parser.add_argument(
        "--psychometric-weight",
        type=float,
        default=60,
        help="Psychometric weight in sekhem (default: 60)",
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
        result = calculate_weighted_average(subjects)
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

    elif args.mode == "sekhem":
        if args.bagrut_avg is None or args.psychometric is None:
            parser.error(
                "--bagrut-avg and --psychometric are required for sekhem mode"
            )
        result = calculate_sekhem(
            args.bagrut_avg,
            args.psychometric,
            args.bagrut_weight,
            args.psychometric_weight,
        )
        print(f"\nSekhem (Admission Score) Estimation")
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
            f"\nNote: This is an estimate. Each university uses its own formula."
        )

    elif args.mode == "bonus":
        if args.grade is None or args.units is None:
            parser.error("--grade and --units are required for bonus mode")
        if args.units == 5:
            bonus = get_bonus_points(args.grade, args.units, args.subject or "", args.bonus)
            print(f"\nBonus Points Calculation")
            print(f"{'='*40}")
            print(f"Grade:           {args.grade}")
            print(f"Units:           {args.units}")
            print(f"Subject:         {args.subject or '(generic)'}")
            print(f"Bonus points:    +{bonus}")
            print(f"Grade for avg:   {args.grade + bonus}")
            if args.grade < MIN_GRADE_FOR_BONUS:
                print(f"\nNote: grade is below {MIN_GRADE_FOR_BONUS}, so no bonus is awarded.")
            if args.bonus is None:
                print("\nNote: bonuses are flat per subject and vary by university.")
                print("Pass --bonus to use your target university's exact value.")
        else:
            print(
                f"\nNo bonus points for {args.units}-unit subjects."
            )
            print("University bonus points are awarded for 5-unit subjects (and partial for 4-unit math/English).")


if __name__ == "__main__":
    main()
