#!/usr/bin/env python3
"""Reference implementation of the scholarship-surfacing logic.

Takes a student profile and returns possible matches. Dates checked 23.11.2026.

The matcher FAILS OPEN. Hiding a scholarship someone qualifies for costs far more
than showing one they turn out not to fit, so anything the profile cannot settle
is printed with status CHECK and the question to verify. A track is left out only
when a published rule clearly excludes the stated degree level.

This is not an eligibility determination. Only the awarding body decides. Verify
every amount and date on the source listed in SKILL.md Reference Links.

Usage:
    python match_scholarships.py --example
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from datetime import date
from typing import List

NOTICE = ("This list is NOT complete and can miss tracks you may qualify for. Check the official pages. "
          "These are possible matches to verify with each awarding body, not an eligibility determination.")
ACADEMIC = ("BA", "MA", "PhD", "postdoc", "certificate")
TECHNICAL = ("hendesai", "technician")
LEVEL_ALIASES = {
    "ba": "BA", "bsc": "BA", "bachelor": "BA", "bachelors": "BA", "undergraduate": "BA", "תואר ראשון": "BA",
    "ma": "MA", "msc": "MA", "master": "MA", "masters": "MA", "תואר שני": "MA",
    "phd": "PhD", "doctorate": "PhD", "doctoral": "PhD", "דוקטורט": "PhD", "תואר שלישי": "PhD",
    "postdoc": "postdoc", "post-doc": "postdoc", "פוסט דוק": "postdoc", "פוסט-דוק": "postdoc",
    "certificate": "certificate", "תעודה": "certificate", "mechina": "mechina", "מכינה": "mechina",
    "hendesai": "hendesai", "handsai": "hendesai", "handasai": "hendesai", "hendesai_student": "hendesai",
    "hand-engineer": "hendesai", "hand_engineer": "hendesai", "hand engineer": "hendesai",
    "practical engineer": "hendesai", "הנדסאי": "hendesai", "הנדסאים": "hendesai",
    "technician": "technician", "טכנאי": "technician", "טכנאים": "technician",
}


def normalize_level(value: str) -> str:
    """An unrecognized level becomes "unknown", which shows every track as CHECK."""
    return LEVEL_ALIASES.get(str(value).strip().lower(), "unknown")


@dataclass
class StudentProfile:
    degree_level: str  # BA / MA / PhD / postdoc / certificate / mechina / hendesai / technician
    institution: str = ""
    field_of_study: str = ""  # informational only, never used to hide a track
    is_incoming_freshman: bool | None = None  # None means unknown
    served_idf: bool | None = None  # None means unknown; only False hides service tracks
    served_sherut_leumi: bool | None = None
    is_combat_veteran: bool = False
    is_combat_support_veteran: bool = False
    is_mimadim_special_population: bool = False
    is_mashpim_special_population: bool = False
    discharge_date: str | None = None  # YYYY-MM-DD
    is_oleh_chadash: bool | None = None  # None means unknown. Includes children of olim, citizen-olim, returning minors
    aliyah_years_ago: float | None = None
    age: int | None = None
    is_periphery_resident_5_of_6: bool = False
    finished_funded_mechina: bool = False
    has_prior_degree: bool = False
    is_national_team_athlete: bool | None = None
    is_single_parent: bool = False
    socioeconomic_score: int | None = None  # self-estimate, never used to hide a track
    willing_to_tutor_perach: bool = True
    iron_swords_reserve_days: int | None = None  # None means unknown
    has_children_under_14: bool = False
    is_bereaved_family_member: bool | None = None
    is_wounded_soldier: bool | None = None
    is_evacuated_household: bool | None = None  # None means unknown

    def __post_init__(self) -> None:
        self.degree_level = normalize_level(self.degree_level)


def lv(p: "StudentProfile", *levels: str) -> bool:
    return p.degree_level == "unknown" or p.degree_level in levels


@dataclass
class ScholarshipMatch:
    name: str
    track: str
    typical_grant: str
    deadline_window: str
    notes: str
    status: str = "CHECK"  # the matcher never asserts eligibility


def check(name: str, track: str, grant: str, deadline: str, notes: str) -> ScholarshipMatch:
    return ScholarshipMatch(name, track, grant, deadline, notes, "CHECK")


def may_have_served(p: StudentProfile) -> bool:
    """Hide service tracks only when the profile says no and nothing implies service."""
    implied = (p.served_idf or p.served_sherut_leumi or p.is_combat_veteran or p.is_combat_support_veteran
               or p.is_mimadim_special_population or p.is_mashpim_special_population
               or bool(p.discharge_date) or p.finished_funded_mechina or bool(p.iron_swords_reserve_days)
               or p.is_wounded_soldier)
    explicit_no = p.served_idf is False and p.served_sherut_leumi is False
    return bool(implied) or not explicit_no


def discharge_note(profile: StudentProfile) -> str:
    if not profile.discharge_date:
        return "Discharge date unknown: check the first-application window (5 years, up to 8 with extensions)."
    try:
        years = (date.today() - date.fromisoformat(profile.discharge_date)).days / 365.25
    except ValueError:
        return "Discharge date unreadable: check the first-application window (5 years, up to 8 with extensions)."
    if years > 8:
        return f"Discharged about {years:.0f} years ago, past the 5 to 8 year first-application window unless an application was already made. Check."
    return f"Discharged about {years:.1f} years ago. First-application window: 5 years, up to 8 with extensions."


def mimadim_window(p: StudentProfile) -> str:
    """inside, outside or unknown. Years 6 to 8 depend on extensions the profile does not record."""
    if not p.discharge_date:
        return "unknown"
    try:
        years = (date.today() - date.fromisoformat(p.discharge_date)).days / 365.25
    except ValueError:
        return "unknown"
    if years <= 5:
        return "inside"
    return "outside" if years > 8 else "unknown"


def fund_order_note(p: StudentProfile) -> str:
    window = mimadim_window(p)
    if window == "inside":
        return "If you hold or may still apply for Mimadim, or are entitled to MoD periphery, use it first and never cancel it."
    if window == "outside":
        return ("Past the Mimadim first-application window. If you already hold Mimadim, keep it. Otherwise check MoD periphery, "
                "and if neither applies go to the Fund.")
    return ("Check whether you hold or may still apply for Mimadim (first application: 5 years, up to 8 with extensions) or are "
            "entitled to MoD periphery. If so, use it first and never cancel it. If not, go to the Fund.")


def match_universal(p: StudentProfile) -> List[ScholarshipMatch]:
    out: List[ScholarshipMatch] = []
    if p.willing_to_tutor_perach and lv(p, "BA", "MA", "PhD", "certificate", "mechina", *TECHNICAL):
        out.append(check(
            "PEREACH", "Tutoring grant",
            "NIS 7,000 (~114 hrs). Enhanced NIS 10,000 (130 hrs) with Mifal HaPais in some cities only",
            "תשפ\"ז: ends around the end of November (Milgapo lists 29.11.2026); check perach.org.il today",
            "First-come-first-served; commitments are audited.",
        ))
    if lv(p, "BA", "mechina", *TECHNICAL) and not p.has_prior_degree:
        ladder = ("BA or mechina NIS 12,480 / 10,000 / 7,500 / 5,000; hand-engineer or technician NIS 8,600 / 6,000 / 4,500 / 3,000"
                  if p.degree_level == "unknown" else
                  "NIS 8,600 / 6,000 / 4,500 / 3,000" if p.degree_level in TECHNICAL else "NIS 12,480 / 10,000 / 7,500 / 5,000")
        out.append(check(
            "MilGo (CHE + PEREACH)", "Socioeconomic, 4 levels",
            f"Levels: {ladder}. Placement is relative to that year's applicants",
            "תשפ\"ז expected December 2026 to January 2027; CHE will publish the date",
            "Check the exclusions: other aid above NIS 8,400 (state-funded institutions, listed exceptions) or NIS 16,800 "
            "(others), tuition under NIS 6,519, teacher-training tracks, foreign-institution branches, Reuyim LeSiyua, "
            "and hand-engineers on listed funding (MAHAT, Ashbal, Haredi procedure, employer). Ask how the MoD's 90% counts. Mimadim does not count against it since 18.5.2026.",
        ))
    if p.is_incoming_freshman is not False and lv(p, "BA"):
        out.append(check(
            f"{p.institution or 'Institution'} merit at admission", "Institutional merit",
            "Varies by institution", "Check the institution",
            "Thresholds vary; there is no universal bagrut cutoff. University tuition figure NIS 12,203 (תשפ\"ז).",
        ))
    return out


def match_post_service(p: StudentProfile) -> List[ScholarshipMatch]:
    out: List[ScholarshipMatch] = []
    if not may_have_served(p):
        return out
    out.append(check(
        "Pikadon Hayashi", "Personal deposit (own funds)", "The user's own deposit",
        "Within the post-discharge window (typically 5 years; verify for reservists and lone soldiers)",
        "Your own money: claim grants first and use it for what remains or as a bridge. An orphan who takes the Family Branch benefit cannot use it for the same purpose. After 5 years the MoD has separate deposit rules.",
    ))
    if lv(p, "BA"):
        out.append(check(
            "MoD periphery tracks 44 / 45 / 46 (only one)", "Priority-area residence or institution",
            "44 and 45: up to full first-year tuition (45 capped at NIS 12,017, תשפ\"ו). "
            "46 (funded-mechina graduates): up to 50% for up to three years, NIS 6,008.5 a year",
            "45, 46: תשפ\"ו registration closed 31.10.2026, documents until 31.1.2027; תשפ\"ז unpublished. "
            "44: no registration, sign the commitment when notified",
            "Only at institutions whose budget the state participates in. Track 46 must be applied for again EVERY year and cannot combine with Mimadim. Track 45 can. Track 44 delays "
            "Mimadim to year two. " + ("Funded mechina reported: compare 46." if p.finished_funded_mechina else "Ask whether a funded mechina was completed."),
        ))
    if lv(p, "BA", "MA", "certificate"):
        note = discharge_note(p) + (" Art certificates only." if p.degree_level == "certificate" else "")
        if p.degree_level == "MA":
            note += " MA students should confirm at *5266."
        if p.is_oleh_chadash:
            note += " Check whether you were defined as a new immigrant during service."
        note += " Requires a gold honorable discharge or a listed special population. Years 6 to 8 need a defined extension."
        m = check(
            "Mimadim LiLimudim", "Gold-discharge combat veterans + special populations",
            "Refund over 3 study years (4 for engineering, medicine, architecture): up to 85% each year but the last, "
            "NIS 10,372.55 on the NIS 12,203 ceiling in תשפ\"ז, final-year top-up of the withheld 15%",
            "תשפ\"ז OPEN 8.11.2026 to 31.8.2027",
            note + " At or below the ceiling carry ~15% until the final year; above it the excess is never refunded. "
            "Keep payment statements. If you hold or may still apply for it, use it before any reservist tuition grant and do not cancel it.",
        )
        out.append(m)
    if lv(p, "mechina", *TECHNICAL):
        out.append(check(
            "MoD hand-engineer / technician funding", "Discharged soldiers at MAHAT colleges",
            "90% of the MAHAT tuition", "Through the college at registration",
            "Mimadim does not cover hand-engineer or technician studies. This covers pre-engineering mechinot too; a third year is not funded.",
        ))
    out.append(check(
        "Mashpim BeLimudim", "MoD + Rothschild living stipend for defined special populations",
        "NIS 12,000 for 90 social-activity + 10 training hours", "תשפ\"ז: 3.11.2026 to 31.12.2026",
        "Check: combat or combat-support veteran from a listed population (lone soldiers, Tashmash, minorities, "
        "Ethiopian origin, immigrants, Haredi). Extra NIS 6,000 for 60+ frontline reserve days in 2027.",
    ))
    if lv(p, "BA", "certificate", *TECHNICAL):
        out.append(check(
            "IMPACT! (FIDF)", "Combat and combat-support veterans, socioeconomic basis",
            "USD 5,000 per study year through the BA or a recognized certificate of a year or more; 130 community hours each funded year",
            "Registration 1.3 to 31.5 every year",
            "Apply within five years of discharge, or up to age 30 with 180+ war reserve days to 31.12.2025. Start in year one or two. Hand-engineers should confirm their studies count.",
        ))
    return out


def match_reservist(p: StudentProfile) -> List[ScholarshipMatch]:
    """Each grant counts its own window, so a single day total can only prompt a check."""
    days = p.iron_swords_reserve_days
    if days is None:
        if not may_have_served(p):
            return []
        days_text = "Reserve days unknown"
    elif days == 0:
        return []
    else:
        days_text = f"{days} days reported in total"
    return [
        check(
            "Reservist tuition grant (Reserve Aid Fund)", "Per academic year, by unit tier",
            "תשפ\"ו: A+ 100%, A 85%, B 65%, C and D 30%, E 22%. תשפ\"ה: combat to NIS 11,653. תשפ\"ד: combat to NIS 11,296. "
            "Other units in those two years: 30% or 33%, official pages differ",
            "תשפ\"ו: 1.8.2026 to 30.6.2027. תשפ\"ד and תשפ\"ה: by 31.12.2026. תשפ\"ז unpublished",
            f"{days_text}. Needs 50+ days in that year's window (60+ for תשפ\"ד). "
            + fund_order_note(p) + " All Fund entitlements from 7.10.2023 to 31.12.2025: file by 31.12.2026 without waiting for any MoD answer. "
            "Only the Fund decides whether a difference remains.",
        ),
        check(
            "Reservist private-lesson reimbursement", "Reserve Aid Fund, against receipts",
            "Up to NIS 2,000 to 3,000 by year and tier",
            "Through 31.12.2025, including early תשפ\"ו: by 31.12.2026. From 1.1.2026: within one year of each event",
            "Needs 21+ days. 2026 claims can start expiring from 1.1.2027. See references/reservist-benefits.md.",
        ),
        check(
            "Personal-expenses and family grants", "IDF, automatic",
            "NIS 1,100 for 8+ Order 8 days to 31.12.2025. 2026: 40+ days, daily from day 41. Child under 14: NIS 2,000",
            "Automatic", "Confirm the bank details on file.",
        ),
        check(
            "Credit-point relief", "Through the reserve coordinator",
            "BA cap 10 credits across the degree, MA up to 4",
            "Ask the institution",
            "Rules differ by year. In תשפ\"ד, licensed-profession students get 8 credits at 100+ days, not 10.",
        ),
    ]


def match_statutory(p: StudentProfile) -> List[ScholarshipMatch]:
    out: List[ScholarshipMatch] = []
    if p.is_bereaved_family_member is not False:
        out.append(check("Bereaved-family tuition track", "Statutory", "Per case", "Through the case manager",
                         "Start with the MoD Family & Commemoration Branch. The discharged-soldiers division also offers benefits; an orphan cannot use the same field from both, or the Pikadon for what the Family Branch funds."))
    if p.is_wounded_soldier is not False:
        out.append(check("Wounded-veteran tuition and rehabilitation", "Statutory", "Per case", "Through the case manager",
                         "Start with the Rehabilitation Branch. The discharged-soldiers division also offers benefits."))
    if p.is_evacuated_household is not False:
        out.append(check("Evacuee tuition tracks", "Foundation and institutional funds",
                         "Heznek La'Atid and university funds; amounts vary", "Per fund",
                         "Check heznek.org and the institution's aid office."))
    return out


def match_olim(p: StudentProfile) -> List[ScholarshipMatch]:
    if p.is_oleh_chadash is False and p.aliyah_years_ago is None:
        return []
    return [check(
        "Student Authority (Minhal HaStudentim)", "Olim tuition funding",
        "Tuition funding up to the government tariff, excluding fees; requires community service, yearly re-application, a year-one advisor meeting, and a Hebrew ulpan by year two for non-Hebrew programs",
        "New semester A students 10 November, continuing 1 October (both passed this year, contact the district office). "
        "Those STARTING in semester B 1 April, summer starters 15 August",
        "Aid is not retroactive: ask what can still be covered and file by 1.10.2027 for next year. Limits vary by track: usually start "
        "by 27 (BA, hand-engineer, certificate) or 30 (MA, conversion), later in some programs, within 36 months of status excluding "
        "service. Current age alone does not decide this, so ask the district office.",
    )]


def match_foundations(p: StudentProfile) -> List[ScholarshipMatch]:
    out = [check(
        "ISEF Foundation", "Underserved background, strong academics",
        "400-500 scholarships a year on 20 campuses, with mentorship", "Check the current cycle",
        "Weighs background alongside academics; no published bagrut cutoff.",
    )] if lv(p, "BA", "MA", "PhD", "postdoc") else []
    if lv(p, "BA"):
        out.append(check("Rashi Foundation Katzir", "Ask whether a direct track is open",
                         "Amount not published; ask Rashi", "Check the current cycle",
                         "Ask the foundation."))
        out.append(check("Maskila and Rakia (Welfare Ministry, via Pitchon Lev)", "Ask the ministry",
                         "Ask the ministry", "Ask the ministry", "Moved from Rashi at the start of תשפ\"ד."))
    return out


def match_graduate(p: StudentProfile) -> List[ScholarshipMatch]:
    out: List[ScholarshipMatch] = []
    if lv(p, "PhD"):
        field = f" Your field: {p.field_of_study}." if p.field_of_study else ""
        out.append(check(
            "Adams Fellowship", "Doctoral, nominated by the institution",
            "Full tuition + NIS 100,000/year + USD 3,000/year academic travel; up to 3 years, extendable to 4",
            "2027-28: until 5.1.2027, only through the institution (earlier internal deadline)",
            "Check your field against the call: exact and life sciences, math, computer science, information science, "
            "engineering. Not humanities or social sciences. From the second doctoral year, by PhD start date: regular track after 1.10.2025, "
            "direct or combined after 1.10.2024, both by 1.10.2026; reserve duty or maternity leave can adjust it. No parallel application "
            "to Clore, Azrieli, Edmond de Rothschild or CHE quantum and data-science programs. No other living stipend." + field,
        ))
        out.append(check(
            "Alix de Rothschild Fellowship (Israel Academy)", "Doctoral, humanities and social sciences",
            "USD 15,000", "Through the institution, until 5.1.2027 for the current call",
            "Check your field against the call. Israeli citizens with an approved research proposal who need a fellowship." + field,
        ))
        out.append(check(
            "PBC / MALAG doctoral scholarships", "Council for Higher Education", "Per cohort", "Per cohort",
            "Check the current terms on che.org.il, including periphery and socioeconomic conditions.",
        ))
    if lv(p, "postdoc"):
        out.append(check(
            "Rothschild Fellowship (Yad Hanadiv)", "First postdoc abroad after an Israeli PhD",
            "USD 75,000/year ceiling on OTHER counted funding",
            "2027-28 university nominations closed 1.11.2026",
            "PhD awarded after November 2023 (exceptions may be considered).",
        ))
    return out


def match_specialized(p: StudentProfile) -> List[ScholarshipMatch]:
    out: List[ScholarshipMatch] = []
    if p.is_national_team_athlete is not False:
        out.append(check("Mifal HaPais athlete track", "National-team athletes", "Per track", "Per cycle",
                         "National-team verification required."))
    return out


def match_all(p: StudentProfile) -> List[ScholarshipMatch]:
    return (match_universal(p) + match_post_service(p) + match_reservist(p) + match_statutory(p)
            + match_olim(p) + match_foundations(p) + match_graduate(p) + match_specialized(p))


def main() -> int:
    print(NOTICE)
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--example", action="store_true", help="Run a worked example")
    args = parser.parse_args()
    if not args.example:
        parser.print_help()
        return 0
    profile = StudentProfile(
        degree_level="BA", institution="HUJI", field_of_study="computer science", is_incoming_freshman=True,
        served_idf=True, is_combat_veteran=True, discharge_date="2024-06-15", is_periphery_resident_5_of_6=True,
        iron_swords_reserve_days=72,
    )
    print("Example profile: combat veteran from a periphery yishuv, incoming HUJI CS freshman, 72 reserve days")
    print("=" * 80)
    for m in match_all(profile):
        print(f"\n[{m.status}] {m.name}\n  Track:    {m.track}\n  Grant:    {m.typical_grant}\n  Deadline: {m.deadline_window}\n  Notes:    {m.notes}")
    print("\n" + "=" * 80)
    print("ORDER NOTE: if you hold or may still apply for Mimadim, or are entitled to MoD periphery, use it first and do not")
    print("cancel it. The Reserve Aid Fund pays only a difference. All Fund entitlements to 31.12.2025: file by 31.12.2026.")
    print(NOTICE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
