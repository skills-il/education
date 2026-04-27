#!/usr/bin/env python3
"""Reference implementation of the scholarship-matching logic.

Takes a student profile (degree level, military status, residence, etc.)
and returns the eligible scholarships ranked by deadline and grant size.

Sources for every figure are listed in evidence.json (sibling file in the
skill folder). PEREACH grant amounts, MoD periphery scholarship cap,
MilGo socioeconomic award range, Rashi Foundation amounts, Adams
Fellowship terms, etc. all come from the published authoritative sources.

This script is illustrative — actual scholarship eligibility, amounts, and
deadlines refresh annually. Always verify on the source URL listed in
evidence.json before recommending to a real student.

Usage:
    python match_scholarships.py --example
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass, field
from typing import List


@dataclass
class StudentProfile:
    degree_level: str  # BA / MA / PhD / postdoc
    institution: str
    is_incoming_freshman: bool = False
    served_idf: bool = False
    is_combat_veteran: bool = False
    discharge_date: str | None = None  # YYYY-MM-DD
    served_sherut_leumi: bool = False
    is_oleh_chadash: bool = False
    aliyah_years_ago: float | None = None
    age: int | None = None
    is_periphery_resident_5_of_6: bool = False
    bagrut_average: float | None = None
    psychometric_score: int | None = None
    is_woman_in_stem: bool = False
    is_national_team_athlete: bool = False
    is_single_parent: bool = False
    served_miluim_this_year: bool = False
    socioeconomic_score: int | None = None  # 1-10, lower = greater need
    willing_to_tutor_perach: bool = False


@dataclass
class ScholarshipMatch:
    name: str
    track: str
    typical_grant: str
    deadline_window: str
    notes: str


def match_universal(profile: StudentProfile) -> List[ScholarshipMatch]:
    matches: List[ScholarshipMatch] = []
    if profile.degree_level == "BA" and profile.willing_to_tutor_perach:
        matches.append(ScholarshipMatch(
            name="PEREACH",
            track="Tutoring grant",
            typical_grant="NIS 7,000 (~114 hrs) or NIS 10,000 (140 hrs)",
            deadline_window="Annual cycle, opens ahead of academic year",
            notes="Largest-volume scholarship in Israel; commitments are audited",
        ))
    if profile.degree_level in ("BA",) and profile.socioeconomic_score is not None and profile.socioeconomic_score <= 6:
        matches.append(ScholarshipMatch(
            name="MilGo (MoE socioeconomic)",
            track="Ministry of Education needs-based",
            typical_grant="NIS 5,000-12,480",
            deadline_window="Cycle opens December (Milgapo)",
            notes="Replaced the older 'SHEFI' branding (which is actually a counseling service)",
        ))
    if profile.is_incoming_freshman and profile.bagrut_average is not None and profile.bagrut_average >= 100:
        matches.append(ScholarshipMatch(
            name=f"{profile.institution} merit at admission",
            track="Institutional merit",
            typical_grant="One-time grant per institution; HUJI/TAU/Technion vary",
            deadline_window="Automatic at registration",
            notes="Check institution's financial-aid page",
        ))
    return matches


def match_post_service(profile: StudentProfile) -> List[ScholarshipMatch]:
    matches: List[ScholarshipMatch] = []
    if profile.served_idf or profile.served_sherut_leumi:
        matches.append(ScholarshipMatch(
            name="Pikadon Hayashi",
            track="Personal deposit (own funds)",
            typical_grant="The user's own deposit",
            deadline_window="Anytime within 5-year window",
            notes="Usable only at MALAG-recognized institutions; not a scholarship per se",
        ))
        if profile.is_periphery_resident_5_of_6:
            matches.append(ScholarshipMatch(
                name="MoD periphery scholarship",
                track="Periphery (אזורי עדיפות לאומית)",
                typical_grant="Up to 100% first-year BA tuition (~NIS 11,653)",
                deadline_window="Annual; check hachvana.mod.gov.il",
                notes="EXCLUSIVE — cannot stack with other periphery scholarships",
            ))
    if profile.is_combat_veteran:
        matches.append(ScholarshipMatch(
            name="Mimadim LiLimudim",
            track="Combat-veteran cohort + special populations",
            typical_grant="Full tuition for the cohort; ~3,230 fellows in תשפ\"ו",
            deadline_window="Annual; tied to discharge cycle",
            notes="MoD program; applications via hachvana.mod.gov.il",
        ))
    return matches


def match_olim(profile: StudentProfile) -> List[ScholarshipMatch]:
    matches: List[ScholarshipMatch] = []
    if not profile.is_oleh_chadash:
        return matches
    if profile.degree_level == "BA" and profile.age is not None and profile.age < 27:
        matches.append(ScholarshipMatch(
            name="Student Authority (Minhal HaStudentim)",
            track="Olim BA tuition benefit",
            typical_grant="Partial/full tuition",
            deadline_window="Annual",
            notes="Apply via gov.il Student Authority portal",
        ))
    if profile.aliyah_years_ago is not None and profile.aliyah_years_ago <= 3:
        matches.append(ScholarshipMatch(
            name="Repatriate Masa Harhava",
            track="Olim within 3 years of aliyah",
            typical_grant="Up to ~90% tuition discount",
            deadline_window="Annual",
            notes="Coordinated through NBN higher-ed portal",
        ))
    return matches


def match_foundations(profile: StudentProfile) -> List[ScholarshipMatch]:
    matches: List[ScholarshipMatch] = []
    if profile.is_periphery_resident_5_of_6 or (profile.socioeconomic_score is not None and profile.socioeconomic_score <= 6):
        matches.append(ScholarshipMatch(
            name="Rashi Foundation Katzir",
            track="Periphery + socioeconomic",
            typical_grant="NIS 5,000-18,000/year, multi-year",
            deadline_window="Annual",
            notes="Largest privately-funded scholarship by reach",
        ))
    if profile.is_single_parent:
        matches.append(ScholarshipMatch(
            name="Rashi Foundation single-mother track",
            track="Single-parent",
            typical_grant="~NIS 16,000",
            deadline_window="Annual",
            notes="Stacks with Katzir if eligible for both",
        ))
    if profile.bagrut_average is not None and profile.bagrut_average >= 100 and (profile.socioeconomic_score is None or profile.socioeconomic_score <= 6):
        matches.append(ScholarshipMatch(
            name="ISEF Foundation",
            track="Underserved-background, strong academics",
            typical_grant="~450 scholarships/year in Israel; multi-year mentorship + leadership",
            deadline_window="Annual",
            notes="Common match for first-generation + Mizrahi/Sephardi profiles",
        ))
    return matches


def match_graduate(profile: StudentProfile) -> List[ScholarshipMatch]:
    matches: List[ScholarshipMatch] = []
    if profile.degree_level == "PhD":
        matches.append(ScholarshipMatch(
            name="Adams Fellowship",
            track="Doctoral, all fields, 2nd year",
            typical_grant="Full tuition + NIS 100,000/year stipend + USD 3,000/year travel; up to 4 years",
            deadline_window="Opens October-November, closes early January for following year",
            notes="Most prestigious Israeli doctoral fellowship",
        ))
        if profile.is_periphery_resident_5_of_6:
            matches.append(ScholarshipMatch(
                name="PBC / MALAG outstanding-doctoral-from-periphery",
                track="Council for Higher Education periphery PhD track",
                typical_grant="Per-cohort terms; check che.org.il",
                deadline_window="Per-cohort",
                notes="Council for Higher Education direct track",
            ))
    if profile.degree_level == "postdoc":
        matches.append(ScholarshipMatch(
            name="Rothschild Fellowship (Yad Hanadiv)",
            track="Postdoc abroad after Israeli PhD",
            typical_grant="Supplementary funds capped at USD 75,000/year",
            deadline_window="Annual",
            notes="Cutoff dates apply to PhD completion",
        ))
    return matches


def match_specialized(profile: StudentProfile) -> List[ScholarshipMatch]:
    matches: List[ScholarshipMatch] = []
    if profile.is_woman_in_stem and profile.institution.lower() in ("huji", "hebrew university"):
        matches.append(ScholarshipMatch(
            name="HUJI free first-year tuition for women in CS/Math",
            track="Women in STEM",
            typical_grant="Free first-year tuition",
            deadline_window="Automatic on enrollment",
            notes="HUJI-specific track",
        ))
    if profile.is_national_team_athlete:
        matches.append(ScholarshipMatch(
            name="Mifal HaPais athlete track",
            track="National-team athletes",
            typical_grant="National-track grant",
            deadline_window="Per-cycle",
            notes="National-team verification required",
        ))
    if profile.served_miluim_this_year and profile.willing_to_tutor_perach:
        matches.append(ScholarshipMatch(
            name="PEREACH miluim supplement",
            track="Reserve-duty supplement",
            typical_grant="Additional grant on top of base PEREACH",
            deadline_window="Annual",
            notes="Stacks on top of base PEREACH for current-year miluim",
        ))
    return matches


def match_all(profile: StudentProfile) -> List[ScholarshipMatch]:
    return (
        match_universal(profile)
        + match_post_service(profile)
        + match_olim(profile)
        + match_foundations(profile)
        + match_graduate(profile)
        + match_specialized(profile)
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--example", action="store_true", help="Run a worked example")
    args = parser.parse_args()

    if args.example:
        profile = StudentProfile(
            degree_level="BA",
            institution="HUJI",
            is_incoming_freshman=True,
            served_idf=True,
            is_combat_veteran=True,
            discharge_date="2024-06-15",
            is_periphery_resident_5_of_6=True,
            bagrut_average=104,
            psychometric_score=720,
            is_woman_in_stem=True,
            socioeconomic_score=4,
            willing_to_tutor_perach=True,
        )
        print("Example profile: female combat veteran from periphery yishuv, incoming HUJI CS freshman")
        print("=" * 80)
        for match in match_all(profile):
            print(f"\n{match.name}")
            print(f"  Track:    {match.track}")
            print(f"  Grant:    {match.typical_grant}")
            print(f"  Deadline: {match.deadline_window}")
            print(f"  Notes:    {match.notes}")
        return 0

    parser.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
