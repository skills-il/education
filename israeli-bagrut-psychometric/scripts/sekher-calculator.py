#!/usr/bin/env python3
"""
Sekher (University Admission Score) Calculator

Calculates the weighted university admission score (sekher, סכר) based on
Bagrut average and Psychometric (PET) score for major Israeli universities.

Each university uses its own formula to combine the Bagrut average and
Psychometric score into a single admission score (sekher). This script
implements approximate formulas for:
  - Hebrew University of Jerusalem (huji)
  - Tel Aviv University (tau)
  - Technion (technion)
  - Ben-Gurion University of the Negev (bgu)

Usage:
    python scripts/sekher-calculator.py --bagrut 95 --psychometric 700 --university tau
    python scripts/sekher-calculator.py --bagrut 90 --psychometric 650 --university all

Note: These formulas are approximations based on publicly available information.
Actual university formulas may vary by faculty and year. Always verify with
the specific university admissions office.
"""

import argparse
import sys


# University formula definitions
# Each university converts Bagrut and Psychometric to its own scale
# and applies different weights.

UNIVERSITIES = {
    "huji": {
        "name": "Hebrew University of Jerusalem (Ha'Universita Ha'Ivrit)",
        "hebrew": "האוניברסיטה העברית בירושלים",
        "description": "Typically weights Psychometric slightly higher for most faculties.",
    },
    "tau": {
        "name": "Tel Aviv University (Universitat Tel Aviv)",
        "hebrew": "אוניברסיטת תל אביב",
        "description": "Balanced formula for most faculties. Competitive programs require higher scores.",
    },
    "technion": {
        "name": "Technion - Israel Institute of Technology",
        "hebrew": "הטכניון - מכון טכנולוגי לישראל",
        "description": "Strong emphasis on Math and Science bagrut subjects. Psychometric quantitative heavily weighted.",
    },
    "bgu": {
        "name": "Ben-Gurion University of the Negev (Universitat Ben Gurion)",
        "hebrew": "אוניברסיטת בן-גוריון בנגב",
        "description": "Generally more accessible thresholds with balanced weighting.",
    },
}


def normalize_bagrut(bagrut_avg: float) -> float:
    """
    Normalize Bagrut average to a 200-800 scale for comparison with Psychometric.
    Bagrut averages typically range from 56 to 120 (with bonus points).
    """
    # Linear mapping: 56 maps to ~200, 120 maps to ~800
    normalized = 200 + (bagrut_avg - 56) * (600 / 64)
    return max(200, min(800, normalized))


def calculate_sekher_huji(bagrut_avg: float, psychometric: int) -> float:
    """
    Hebrew University approximate sekher formula.
    Generally: 40% Bagrut (normalized) + 60% Psychometric for many faculties.
    Some faculties use 50/50 or other ratios.
    """
    normalized_bagrut = normalize_bagrut(bagrut_avg)
    return 0.40 * normalized_bagrut + 0.60 * psychometric


def calculate_sekher_tau(bagrut_avg: float, psychometric: int) -> float:
    """
    Tel Aviv University approximate sekher formula.
    Generally: 50% Bagrut (normalized) + 50% Psychometric for most faculties.
    """
    normalized_bagrut = normalize_bagrut(bagrut_avg)
    return 0.50 * normalized_bagrut + 0.50 * psychometric


def calculate_sekher_technion(bagrut_avg: float, psychometric: int) -> float:
    """
    Technion approximate sekher formula.
    Generally: 45% Bagrut (normalized) + 55% Psychometric.
    The Technion places heavy emphasis on Math and science Bagrut scores,
    which should be reflected in the Bagrut average entered.
    """
    normalized_bagrut = normalize_bagrut(bagrut_avg)
    return 0.45 * normalized_bagrut + 0.55 * psychometric


def calculate_sekher_bgu(bagrut_avg: float, psychometric: int) -> float:
    """
    Ben-Gurion University approximate sekher formula.
    Generally: 50% Bagrut (normalized) + 50% Psychometric.
    """
    normalized_bagrut = normalize_bagrut(bagrut_avg)
    return 0.50 * normalized_bagrut + 0.50 * psychometric


CALCULATORS = {
    "huji": calculate_sekher_huji,
    "tau": calculate_sekher_tau,
    "technion": calculate_sekher_technion,
    "bgu": calculate_sekher_bgu,
}


def validate_inputs(bagrut_avg: float, psychometric: int) -> list:
    """Validate input values and return list of error messages."""
    errors = []
    if bagrut_avg < 56 or bagrut_avg > 130:
        errors.append(
            f"Bagrut average {bagrut_avg} is out of range. "
            f"Expected 56-130 (including bonus points)."
        )
    if psychometric < 200 or psychometric > 800:
        errors.append(
            f"Psychometric score {psychometric} is out of range. "
            f"Expected 200-800."
        )
    return errors


def print_result(university_key: str, bagrut_avg: float, psychometric: int) -> None:
    """Calculate and print the sekher for a specific university."""
    info = UNIVERSITIES[university_key]
    calculator = CALCULATORS[university_key]
    sekher = calculator(bagrut_avg, psychometric)
    normalized_bagrut = normalize_bagrut(bagrut_avg)

    print(f"\n  {info['name']}")
    print(f"  {info['hebrew']}")
    print(f"  {info['description']}")
    print(f"  Normalized Bagrut (200-800 scale): {normalized_bagrut:.1f}")
    print(f"  Sekher Score: {sekher:.1f}")
    print(f"  {'=' * 50}")


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Calculate university admission weighted score (sekher) "
            "based on Bagrut average and Psychometric score."
        ),
        epilog=(
            "Example: python sekher-calculator.py --bagrut 95 --psychometric 700 --university tau\n"
            "         python sekher-calculator.py --bagrut 90 --psychometric 650 --university all"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "--bagrut",
        type=float,
        required=True,
        help="Bagrut weighted average (56-130, including bonus points)",
    )
    parser.add_argument(
        "--psychometric",
        type=int,
        required=True,
        help="Psychometric (PET) score (200-800)",
    )
    parser.add_argument(
        "--university",
        type=str,
        required=True,
        choices=list(UNIVERSITIES.keys()) + ["all"],
        help="University to calculate for (huji, tau, technion, bgu, or all)",
    )

    args = parser.parse_args()

    # Validate inputs
    errors = validate_inputs(args.bagrut, args.psychometric)
    if errors:
        print("Input validation errors:")
        for error in errors:
            print(f"  - {error}")
        sys.exit(1)

    # Print header
    print("\n" + "=" * 60)
    print("  SEKHER (University Admission Score) Calculator")
    print("  מחשבון סכר (ציון קבלה לאוניברסיטה)")
    print("=" * 60)
    print(f"\n  Input:")
    print(f"  Bagrut Average (ממוצע בגרות): {args.bagrut}")
    print(f"  Psychometric Score (ציון פסיכומטרי): {args.psychometric}")

    # Calculate and display results
    if args.university == "all":
        print(f"\n  Results for all universities:")
        print(f"  {'=' * 50}")
        for key in UNIVERSITIES:
            print_result(key, args.bagrut, args.psychometric)
    else:
        print(f"\n  Result:")
        print(f"  {'=' * 50}")
        print_result(args.university, args.bagrut, args.psychometric)

    # Print disclaimer
    print("\n  DISCLAIMER (הערה חשובה):")
    print("  These are approximate calculations based on publicly available")
    print("  information. Actual sekher formulas vary by faculty and change")
    print("  yearly. Always verify with the university admissions office")
    print("  (minhal rishum) for the most current formula.")
    print()


if __name__ == "__main__":
    main()
