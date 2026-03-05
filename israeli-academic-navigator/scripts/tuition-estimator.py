#!/usr/bin/env python3
"""
Israeli Tuition Estimator

Estimates annual tuition costs based on institution type, degree level, and
student status (citizen, oleh, international). Includes additional fees and
potential scholarship offsets.

Usage:
    python scripts/tuition-estimator.py --institution university --degree bachelor --status citizen
    python scripts/tuition-estimator.py --institution college --degree master-professional --status oleh
    python scripts/tuition-estimator.py --institution open-university --degree bachelor --status citizen --courses 8
    python scripts/tuition-estimator.py --help
"""

import argparse
import sys


# Tuition data (NIS, approximate for 2025-2026 academic year)
TUITION_DATA = {
    "university": {
        "bachelor": {"base": 10300, "label": "BA/BSc (regulated by CHE)"},
        "master-research": {"base": 13500, "label": "MA/MSc Research Track"},
        "master-professional": {"base": 45000, "label": "MA Professional/MBA (avg)"},
        "phd": {"base": 2500, "label": "PhD (minimal/waived)"},
        "medical": {"base": 10300, "label": "MD (regulated, 6-7 year program)"},
    },
    "college": {
        "bachelor": {"base": 11500, "label": "BA/BSc (academic college)"},
        "master-research": {"base": 14000, "label": "MA Research Track"},
        "master-professional": {"base": 35000, "label": "MA Professional (avg)"},
    },
    "teacher-college": {
        "bachelor": {"base": 10300, "label": "B.Ed (teacher training)"},
        "master-research": {"base": 12000, "label": "M.Ed Research Track"},
    },
    "open-university": {
        "bachelor": {"per_course": 2800, "label": "BA (per course, ~10 courses/year)"},
        "master-research": {"per_course": 3200, "label": "MA (per course)"},
    },
    "private": {
        "bachelor": {"base": 25000, "label": "BA (private institution avg)"},
        "master-professional": {"base": 55000, "label": "MA/MBA (private institution avg)"},
    },
}

# Student status adjustments
STATUS_ADJUSTMENTS = {
    "citizen": {
        "label": "Israeli Citizen",
        "multiplier": 1.0,
        "discount_note": None,
    },
    "oleh": {
        "label": "Oleh Chadash (New Immigrant)",
        "multiplier": 0.85,
        "discount_note": "Absorption Ministry may provide additional scholarships (up to 13,000 NIS/year)",
    },
    "international": {
        "label": "International Student",
        "multiplier": 2.5,
        "discount_note": "International tuition varies widely; contact institution directly",
    },
}

# Additional annual fees
ADDITIONAL_FEES = {
    "student_union": 500,       # Aguda fee (approx)
    "health_insurance": 300,    # Student health supplement (approx)
    "registration": 400,        # Annual registration fee (approx)
}

# Perach offset
PERACH_OFFSET = 3500  # Approximate annual value of Perach tuition waiver


VALID_INSTITUTIONS = list(TUITION_DATA.keys())
VALID_STATUSES = list(STATUS_ADJUSTMENTS.keys())


def get_valid_degrees(institution):
    """Return valid degree options for a given institution type."""
    return list(TUITION_DATA.get(institution, {}).keys())


def estimate_tuition(institution, degree, status, courses=None, perach=False):
    """Calculate estimated annual tuition."""
    inst_data = TUITION_DATA.get(institution)
    if not inst_data:
        return None, "Invalid institution type"

    degree_data = inst_data.get(degree)
    if not degree_data:
        valid = ", ".join(get_valid_degrees(institution))
        return None, f"Degree '{degree}' not available at {institution}. Valid options: {valid}"

    status_info = STATUS_ADJUSTMENTS.get(status)
    if not status_info:
        return None, "Invalid student status"

    # Calculate base tuition
    if "per_course" in degree_data:
        num_courses = courses if courses else 10
        base_tuition = degree_data["per_course"] * num_courses
        per_course_note = f"  Per course: {degree_data['per_course']:,} NIS x {num_courses} courses"
    else:
        base_tuition = degree_data["base"]
        per_course_note = None

    # Apply status multiplier
    adjusted_tuition = base_tuition * status_info["multiplier"]

    # Additional fees
    total_fees = sum(ADDITIONAL_FEES.values())

    # Perach offset
    perach_savings = PERACH_OFFSET if perach else 0

    # Total
    total = adjusted_tuition + total_fees - perach_savings

    return {
        "institution": institution,
        "degree": degree_data["label"],
        "status": status_info["label"],
        "base_tuition": base_tuition,
        "per_course_note": per_course_note,
        "status_multiplier": status_info["multiplier"],
        "adjusted_tuition": adjusted_tuition,
        "additional_fees": ADDITIONAL_FEES.copy(),
        "total_fees": total_fees,
        "perach": perach,
        "perach_savings": perach_savings,
        "total": total,
        "discount_note": status_info["discount_note"],
    }, None


def format_result(result):
    """Format the estimation result for display."""
    lines = []
    lines.append("")
    lines.append("=" * 60)
    lines.append("  ISRAELI TUITION ESTIMATE (2025-2026)")
    lines.append("=" * 60)
    lines.append("")
    lines.append(f"  Institution Type:  {result['institution'].replace('-', ' ').title()}")
    lines.append(f"  Degree Program:    {result['degree']}")
    lines.append(f"  Student Status:    {result['status']}")
    lines.append("")
    lines.append("-" * 60)
    lines.append("  TUITION BREAKDOWN")
    lines.append("-" * 60)
    lines.append("")
    lines.append(f"  Base annual tuition:       {result['base_tuition']:>10,} NIS")

    if result["per_course_note"]:
        lines.append(result["per_course_note"])

    if result["status_multiplier"] != 1.0:
        lines.append(f"  Status adjustment (x{result['status_multiplier']}): {result['adjusted_tuition']:>10,.0f} NIS")

    lines.append("")
    lines.append("  Additional fees:")
    for fee_name, fee_amount in result["additional_fees"].items():
        label = fee_name.replace("_", " ").title()
        lines.append(f"    {label:<30} {fee_amount:>6,} NIS")
    lines.append(f"  {'':30} {'------':>6}")
    lines.append(f"    Total additional fees:      {result['total_fees']:>6,} NIS")

    if result["perach"]:
        lines.append("")
        lines.append(f"  Perach tuition waiver:       {-result['perach_savings']:>7,} NIS")

    lines.append("")
    lines.append("-" * 60)
    lines.append(f"  ESTIMATED ANNUAL TOTAL:      {result['total']:>10,.0f} NIS")
    lines.append(f"  ESTIMATED MONTHLY:           {result['total'] / 12:>10,.0f} NIS")
    lines.append("-" * 60)

    if result["discount_note"]:
        lines.append("")
        lines.append(f"  Note: {result['discount_note']}")

    if result["perach"]:
        lines.append("")
        lines.append("  Perach requires 4 hours/week of tutoring throughout the")
        lines.append("  academic year. Register through your institution's Perach")
        lines.append("  coordinator.")

    lines.append("")
    lines.append("  Disclaimer: These are estimates based on publicly available")
    lines.append("  data. Contact your institution for exact current figures.")
    lines.append("  Scholarships and need-based grants may reduce costs further.")
    lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Estimate annual tuition at Israeli higher education institutions.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --institution university --degree bachelor --status citizen
  %(prog)s --institution college --degree master-professional --status oleh
  %(prog)s --institution open-university --degree bachelor --status citizen --courses 8
  %(prog)s --institution university --degree bachelor --status citizen --perach

Institution types: university, college, teacher-college, open-university, private
Student statuses: citizen, oleh, international
        """,
    )

    parser.add_argument(
        "--institution",
        required=True,
        choices=VALID_INSTITUTIONS,
        help="Type of institution (university, college, teacher-college, open-university, private)",
    )
    parser.add_argument(
        "--degree",
        required=True,
        help="Degree level (bachelor, master-research, master-professional, phd, medical)",
    )
    parser.add_argument(
        "--status",
        required=True,
        choices=VALID_STATUSES,
        help="Student status (citizen, oleh, international)",
    )
    parser.add_argument(
        "--courses",
        type=int,
        default=None,
        help="Number of courses per year (for Open University only, default: 10)",
    )
    parser.add_argument(
        "--perach",
        action="store_true",
        help="Include Perach tutoring program tuition offset",
    )

    args = parser.parse_args()

    # Validate degree for institution
    valid_degrees = get_valid_degrees(args.institution)
    if args.degree not in valid_degrees:
        print(f"Error: Degree '{args.degree}' is not available at '{args.institution}'.")
        print(f"Valid degrees for {args.institution}: {', '.join(valid_degrees)}")
        sys.exit(1)

    # Validate courses argument
    if args.courses is not None and args.institution != "open-university":
        print("Warning: --courses flag is only relevant for open-university. Ignoring.")
        args.courses = None

    if args.courses is not None and args.courses < 1:
        print("Error: Number of courses must be at least 1.")
        sys.exit(1)

    result, error = estimate_tuition(
        institution=args.institution,
        degree=args.degree,
        status=args.status,
        courses=args.courses,
        perach=args.perach,
    )

    if error:
        print(f"Error: {error}")
        sys.exit(1)

    print(format_result(result))


if __name__ == "__main__":
    main()
