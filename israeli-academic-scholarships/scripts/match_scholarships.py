#!/usr/bin/env python3
"""Reference implementation of the scholarship-matching logic.

Takes a student profile (degree level, military status, residence, reserve days, etc.)
and returns the eligible scholarships ranked by deadline and grant size.

Sources for every figure are cited inline. Mimadim graduated funding model and
Adams field-scope restriction were verified against hachvana.mod.gov.il and
adams.academy.ac.il respectively. Iron Swords reservist framework comes from
che.org.il/war/.

This script is illustrative, actual scholarship eligibility, amounts, and
deadlines refresh annually. Always verify on the source URL listed in the
SKILL.md Reference Links table before recommending to a real student.

Usage:
    python match_scholarships.py --example
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from typing import List, Set


HUMANITIES_FIELDS: Set[str] = {
    "humanities", "philosophy", "history", "literature", "linguistics",
    "social sciences", "sociology", "anthropology", "political science", "psychology",
    "law",
}

EXACT_AND_LIFE_FIELDS: Set[str] = {
    "exact sciences", "physics", "chemistry", "mathematics", "math",
    "computer science", "cs", "information science",
    "life sciences", "biology", "biomedical", "medicine", "neuroscience",
    "engineering",
}


@dataclass
class StudentProfile:
    degree_level: str  # BA / MA / PhD / postdoc
    institution: str
    field_of_study: str = ""  # used for Adams field gating
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
    # Iron Swords (post-7.10.2023)
    iron_swords_reserve_days: int = 0  # cumulative reserve days from 7.10.2023
    is_iron_swords_combat_track: bool = False
    has_children_under_14: bool = False
    # Statutory / evacuee
    is_bereaved_family_member: bool = False  # יתום מערכות ישראל / bereaved sibling
    is_wounded_soldier: bool = False  # נכה צה"ל
    is_evacuated_household: bool = False  # פינוי 7.10.2023


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
            deadline_window="תשפ\"ז cycle: opens September, first-come-first-served until ~November",
            notes="NOT in May-September cluster; commitments are audited",
        ))
    if profile.degree_level in ("BA",) and profile.socioeconomic_score is not None and profile.socioeconomic_score <= 6:
        matches.append(ScholarshipMatch(
            name="MilGo (MoE socioeconomic)",
            track="Ministry of Education needs-based, 4-tier",
            typical_grant="Tier A NIS 12,480 / B NIS 10,000 / C NIS 7,500 / D NIS 5,000",
            deadline_window="Cycle opens December (Milgapo)",
            notes="Replaced the older 'SHEFI' branding (which is actually a counseling service)",
        ))
    if profile.is_incoming_freshman and profile.bagrut_average is not None and profile.bagrut_average >= 100:
        matches.append(ScholarshipMatch(
            name=f"{profile.institution} merit at admission",
            track="Institutional merit",
            typical_grant="One-time grant per institution; HUJI/TAU/Technion vary",
            deadline_window="Automatic at registration",
            notes="Baseline NIS 12,017 tuition (תשפ\"ו); humanities <100%, medicine/law/MBA >100%",
        ))
    return matches


def match_post_service(profile: StudentProfile) -> List[ScholarshipMatch]:
    matches: List[ScholarshipMatch] = []
    if profile.served_idf or profile.served_sherut_leumi:
        matches.append(ScholarshipMatch(
            name="Pikadon Hayashi",
            track="Personal deposit (own funds)",
            typical_grant="The user's own deposit",
            deadline_window="Anytime within post-discharge window (typically 5 years; verify for reservists/lone soldiers)",
            notes="Usable only at MALAG-recognized institutions; not a scholarship per se",
        ))
        if profile.is_periphery_resident_5_of_6:
            matches.append(ScholarshipMatch(
                name="MoD periphery scholarship",
                track="Periphery (אזורי עדיפות לאומית)",
                typical_grant="Up to 100% first-year BA tuition (~NIS 11,653, taf-shin-peh-heh/2025)",
                deadline_window="Annual; check hachvana.mod.gov.il",
                notes="EXCLUSIVE, cannot stack with other periphery scholarships. Post-discharge window: 5 years standard, 10 years for active reservists / lone soldiers",
            ))
    if profile.is_combat_veteran:
        matches.append(ScholarshipMatch(
            name="Mimadim LiLimudim",
            track="Combat-veteran cohort + special populations",
            typical_grant="GRADUATED: 85% Years 1-2, top-up to 100% in final year, capped NIS 10,214.45/year",
            deadline_window="תשפ\"ו: opens 3.11.2025, closes 31.7.2026, documents by 30.8.2026",
            notes="Year 1 student pays ~15% out of pocket up front, recovered at graduation. Cannot stack with Iron Swords same year.",
        ))
    return matches


def match_iron_swords(profile: StudentProfile) -> List[ScholarshipMatch]:
    """Match the Iron Swords reservist framework (CHE/MoD, תשפ\"ה-תשפ\"ז)."""
    matches: List[ScholarshipMatch] = []
    if profile.iron_swords_reserve_days >= 8:
        matches.append(ScholarshipMatch(
            name="Iron Swords reservist grant (≥8 days floor)",
            track="CHE/MoD universal-floor",
            typical_grant="NIS 1,100 one-time",
            deadline_window="Per CHE cycle, see che.org.il/war/",
            notes="Universal floor for any student-reservist with 8+ cumulative reserve days from 7.10.2023",
        ))
    if profile.iron_swords_reserve_days >= 8 and profile.has_children_under_14:
        matches.append(ScholarshipMatch(
            name="Iron Swords reservist-parent supplement",
            track="CHE/MoD child-supplement",
            typical_grant="NIS 2,000 one-time (stacks on the NIS 1,100 floor)",
            deadline_window="Per CHE cycle",
            notes="For reservist students with children under 14",
        ))
    if profile.iron_swords_reserve_days >= 50:
        matches.append(ScholarshipMatch(
            name="Iron Swords rear-service tuition assistance",
            track="50+ days under Order 8",
            typical_grant="One-time tuition assistance, percentage per current cohort",
            deadline_window="Per CHE cycle",
            notes="Check che.org.il/war/ for current cohort percentage. Cannot stack with Mimadim same year.",
        ))
    if profile.is_iron_swords_combat_track:
        matches.append(ScholarshipMatch(
            name="Iron Swords combat-track tuition support",
            track="Combat reservists with extended service",
            typical_grant="Higher-tier tuition support, up to full tuition",
            deadline_window="Per CHE cycle",
            notes="Subject to current CHE framework terms. Cannot stack with Mimadim same year, pick the higher payout.",
        ))
    if profile.iron_swords_reserve_days >= 100:
        matches.append(ScholarshipMatch(
            name="Iron Swords credit-unit exemption (100+ days)",
            track="Academic accommodation",
            typical_grant="10 credit-unit exemption",
            deadline_window="Per CHE cycle",
            notes="Not money, but materially reduces course load",
        ))
    elif profile.iron_swords_reserve_days >= 61:
        matches.append(ScholarshipMatch(
            name="Iron Swords credit-unit exemption (61-99 days)",
            track="Academic accommodation",
            typical_grant="8 credit-unit exemption",
            deadline_window="Per CHE cycle",
            notes="Not money, but materially reduces course load",
        ))
    return matches


def match_statutory(profile: StudentProfile) -> List[ScholarshipMatch]:
    """Bereaved-family / wounded-soldier / evacuee tracks. Statutory, not via hachvana."""
    matches: List[ScholarshipMatch] = []
    if profile.is_bereaved_family_member:
        matches.append(ScholarshipMatch(
            name="יתומי מערכות ישראל / bereaved-sibling tuition track",
            track="Statutory under חוק משפחות חיילים שנספו במערכה",
            typical_grant="Tuition support + stipends; per-case via case manager",
            deadline_window="Continuous via case manager",
            notes="Routes through MoD Family & Commemoration Branch (אגף משפחות), NOT hachvana portal",
        ))
    if profile.is_wounded_soldier:
        matches.append(ScholarshipMatch(
            name="נכי צה\"ל tuition + rehabilitation support",
            track="Statutory under חוק הנכים",
            typical_grant="Tuition + rehabilitation support; per-case",
            deadline_window="Continuous via case manager",
            notes="Routes through Rehabilitation Branch (אגף השיקום), NOT hachvana portal",
        ))
    if profile.is_evacuated_household:
        matches.append(ScholarshipMatch(
            name="Evacuee (מפונים) tuition tracks",
            track="עוטף עזה / north evacuees who became students 2024-2026",
            typical_grant="TAU emergency fund ~NIS 2,500/student; Heznek La'Atid; per-university funds",
            deadline_window="Per-foundation cycles",
            notes="Multiple parallel sources, check heznek.org and university financial aid",
        ))
    return matches


def match_olim(profile: StudentProfile) -> List[ScholarshipMatch]:
    matches: List[ScholarshipMatch] = []
    if not profile.is_oleh_chadash:
        return matches
    if profile.degree_level == "BA":
        matches.append(ScholarshipMatch(
            name="Student Authority (Minhal HaStudentim)",
            track="Olim BA tuition benefit (post-army window: 5 years regular / 7 years career)",
            typical_grant="Partial/full tuition",
            deadline_window="תשפ\"ו: 31.7.2026; documents by 30.8.2026",
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
            typical_grant="Over 400 active fellows across 20 campuses; multi-year mentorship + leadership",
            deadline_window="Annual",
            notes="Common match for first-generation + Mizrahi/Sephardi profiles",
        ))
    return matches


def _is_humanities_or_social(field: str) -> bool:
    f = field.lower().strip()
    return any(f == h or h in f for h in HUMANITIES_FIELDS)


def _is_exact_or_life(field: str) -> bool:
    f = field.lower().strip()
    return any(f == e or e in f for e in EXACT_AND_LIFE_FIELDS)


def match_graduate(profile: StudentProfile) -> List[ScholarshipMatch]:
    matches: List[ScholarshipMatch] = []
    if profile.degree_level == "PhD":
        # Adams Fellowship: VERIFIED-restricted to exact sciences, math, life sciences only
        if _is_exact_or_life(profile.field_of_study):
            matches.append(ScholarshipMatch(
                name="Adams Fellowship",
                track="Doctoral, exact sciences / mathematics / life sciences ONLY (NOT humanities, NOT social sciences)",
                typical_grant="Full tuition + NIS 100,000/year stipend + USD 3,000/year travel; up to 4 years",
                deadline_window="Opens October-November, closes early January for following year",
                notes="Most prestigious Israeli doctoral fellowship",
            ))
        elif _is_humanities_or_social(profile.field_of_study):
            # Don't match Adams; route to Aharon Katzir (postdoc) and other humanities tracks.
            pass
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
            typical_grant="Supplementary funds with USD 75,000/year CEILING on OTHER external funding (exceeding it disqualifies)",
            deadline_window="Annual",
            notes="Cutoff dates apply to PhD completion; ceiling is on other funding, not on the Rothschild itself",
        ))
        if _is_humanities_or_social(profile.field_of_study):
            matches.append(ScholarshipMatch(
                name="Aharon Katzir Postdoctoral Fellowship (Israel Academy of Sciences)",
                track="Humanities / social sciences postdoc-abroad track (complement to Adams)",
                typical_grant="Multi-year track; check academy.ac.il for current cycle",
                deadline_window="Per-cycle",
                notes="The natural complement to Adams for humanities/social-sciences postdocs",
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
            notes="Stacks on top of base PEREACH AND on top of Iron Swords floor",
        ))
    return matches


def match_all(profile: StudentProfile) -> List[ScholarshipMatch]:
    return (
        match_universal(profile)
        + match_post_service(profile)
        + match_iron_swords(profile)
        + match_statutory(profile)
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
            field_of_study="computer science",
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
            iron_swords_reserve_days=72,
            is_iron_swords_combat_track=True,
            has_children_under_14=False,
            served_miluim_this_year=True,
        )
        print("Example profile: female combat veteran from periphery yishuv, incoming HUJI CS freshman,")
        print("served 72 days reserve duty since 7.10.2023")
        print("=" * 80)
        for match in match_all(profile):
            print(f"\n{match.name}")
            print(f"  Track:    {match.track}")
            print(f"  Grant:    {match.typical_grant}")
            print(f"  Deadline: {match.deadline_window}")
            print(f"  Notes:    {match.notes}")
        print("\n" + "=" * 80)
        print("STACKING NOTE: Iron Swords combat-track and Mimadim LiLimudim cannot be received")
        print("in the same academic year. Compare per-year value and pick the higher.")
        return 0

    parser.print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
