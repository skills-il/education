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
    for label, value in (("exam score", exam_score), ("magen score", magen_score)):
        if not 0 <= value <= 100:
            raise ValueError(f"{label} must be between 0 and 100, got {value}")
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
    "english": 25,
    # The Technion and TAU both pay 25 for this group, not the generic 20.
    "history": 25,
    "literature": 25,
    "bible": 25,
    "arabic": 25,
}
DEFAULT_BONUS_5U_OTHER = 20

# Not on any bonus-eligible list checked. Awarding a bonus here silently inflates
# the whole average, which is the failure mode SKILL.md warns about.
NOT_BONUS_ELIGIBLE = {"hebrew", "lashon", "civics"}

# A 4-unit bonus DOES exist. Returning 0 here told 4-unit students they get nothing,
# which is wrong at every institution checked (Technion 10; TAU 12.5 for maths and
# English, 10 otherwise).
DEFAULT_BONUS_4U = {
    "math": 12.5,
    "mathematics": 12.5,
    "english": 12.5,
}
DEFAULT_BONUS_4U_OTHER = 10
MIN_GRADE_FOR_BONUS = 60

# The audience is Hebrew-speaking, and an English-only lookup silently returned the
# generic bonus for a Hebrew subject name: "מתמטיקה" scored +20 instead of +30.
SUBJECT_ALIASES = {
    "מתמטיקה": "math",
    "מתמטיקה מוגברת": "math",
    "פיזיקה": "physics",
    "כימיה": "chemistry",
    "ביולוגיה": "biology",
    "מדעי המחשב": "computer science",
    "אנגלית": "english",
    "היסטוריה": "history",
    "ספרות": "literature",
    "תנך": "bible",
    "תנ\"ך": "bible",
    "עברית": "hebrew",
    "לשון": "hebrew",
    "אזרחות": "civics",
    "ערבית": "arabic",
}


def normalize_subject(subject: str) -> str:
    """Map a Hebrew or English subject name onto the lookup key."""
    s = (subject or "").strip().lower()
    return SUBJECT_ALIASES.get(s, SUBJECT_ALIASES.get((subject or "").strip(), s))


def get_bonus_points(grade: float, units: int, subject: str = "", override=None) -> float:
    """Flat per-subject 5-unit bonus, gated at grade >= 60.

    Both 5-unit and 4-unit bonuses are modelled. The 4-unit values are Tel Aviv
    University's; the Technion publishes no 4-unit row, so do not read a 4-unit
    result as a Technion figure. If `override` is given it is used as the exact
    bonus for this subject. The bonus is NOT tiered by score, and a subject that is
    not on the institution's bonus-eligible list gets nothing.
    """
    if grade < MIN_GRADE_FOR_BONUS:
        return 0
    if override is not None:
        return override
    key = normalize_subject(subject)
    if key in NOT_BONUS_ELIGIBLE:
        return 0
    if units == 5:
        return DEFAULT_BONUS_5U.get(key, DEFAULT_BONUS_5U_OTHER)
    if units == 4:
        return DEFAULT_BONUS_4U.get(key, DEFAULT_BONUS_4U_OTHER)
    return 0


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
    Rough illustrative blend ONLY. This is NOT any institution's sekhem.

    No Israeli institution publishes a 0-100 sekhem or a percentage blend of the two
    components. Tel Aviv University, for example, uses an affine formula with its own
    coefficients and a cap of 117 on the bagrut average; the Hebrew University uses an
    optimal-elective average. A number produced here must never be compared against a
    published faculty cut-off, and the output says so.
    """
    if not 0 <= bagrut_avg <= 130:
        raise ValueError("bagrut average must be between 0 and 130 (bonuses can exceed 100)")
    if not 200 <= psychometric <= 800:
        raise ValueError("psychometric score must be between 200 and 800")
    if round(bagrut_weight + psychometric_weight, 6) != 100:
        raise ValueError(
            f"weights must sum to 100, got {bagrut_weight} + {psychometric_weight} "
            f"= {bagrut_weight + psychometric_weight}"
        )
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
        try:
            units = int(parts[1])
            grade = float(parts[2])
            bonus = float(parts[3]) if len(parts) == 4 else None
        except ValueError:
            print(
                f"Error: Invalid subject '{item}'. Units must be a whole number and "
                f"grade must be a number. Use name:units:grade[:bonus]"
            )
            sys.exit(1)
        if not 2 <= units <= 5:
            print(f"Error: '{item}' has {units} study units. Israeli subjects run 2 to 5.")
            sys.exit(1)
        if not 0 <= grade <= 100:
            print(f"Error: '{item}' has grade {grade}. Bagrut grades run 0 to 100.")
            sys.exit(1)
        subjects.append({
            "name": parts[0],
            "units": units,
            "grade": grade,
            "bonus": bonus,
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
                help="Bagrut weight for the illustrative blend. REQUIRED in sekhem mode: there is no defensible default, see SKILL.md.",
    )
    parser.add_argument(
        "--psychometric-weight",
        type=float,
                help="Psychometric weight for the illustrative blend. REQUIRED in sekhem mode.",
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
        if not result['total_units']:
            print("Weighted average:    n/a (no study units, nothing to average)")
            sys.exit(1)
        print(f"Weighted average:    {result['average']}")

    elif args.mode == "sekhem":
        if args.bagrut_avg is None or args.psychometric is None:
            parser.error(
                "--bagrut-avg and --psychometric are required for sekhem mode"
            )
        if args.bagrut_weight is None or args.psychometric_weight is None:
            parser.error(
                "--bagrut-weight and --psychometric-weight are REQUIRED in sekhem mode.\n"
                "There is no defensible default. A 40/60 blend used to be the default here and "
                "was removed: no Israeli institution publishes a percentage blend of the two "
                "components, so any default would reconstruct a discredited figure. Supply your "
                "target institution's own coefficients deliberately, or use its calculator."
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
            "\nNOT a real sekhem. No Israeli institution publishes a 0-100 sekhem or a\n"
            "percentage blend of the two components. Tel Aviv University uses an affine\n"
            "formula with a cap of 117 on the bagrut average; the Hebrew University uses an\n"
            "optimal-elective average. Never compare this number to a published cut-off.\n"
            "Use the target institution's own calculator."
        )

    elif args.mode == "bonus":
        if args.grade is None or args.units is None:
            parser.error("--grade and --units are required for bonus mode")
        if args.units in (4, 5):
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
            print("University bonus points are awarded for 4- and 5-unit subjects only.")


if __name__ == "__main__":
    try:
        main()
    except ValueError as exc:
        # Range and weight-sum violations are user input errors, not crashes.
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(2)
