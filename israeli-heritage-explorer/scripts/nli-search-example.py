#!/usr/bin/env python3
"""
Example script: Search the NLI OpenLibrary API and format results.

Filtering follows the official NLI docs: language and date are query CLAUSES
(joined with ",AND;"), while material_type and availability_type are standalone
"&" filters. There is no rows/start or publication_year_from/_to; pagination
uses items_per_page (1-50) and result_page.

Usage:
    python nli-search-example.py "subject,contains,Tel Aviv" --type images --lang heb --per-page 10
    python nli-search-example.py "creator,contains,Herzl" --type books --from-year 1890 --to-year 1910
"""

import argparse
import json
import os
import sys
import urllib.request
import urllib.parse

NLI_API_BASE = "https://api.nli.org.il/openlibrary/search"
NLI_API_KEY = os.getenv("NLI_API_KEY", "")

# Valid material_type values per the official NLI search-api user-help page.
VALID_TYPES = [
    "books", "journals", "images", "audio_video", "scores", "maps",
    "archives", "sheets", "dissertations", "manuscripts", "media",
    "databases", "NEWSPAPER", "Identity",
]

VALID_SORT_FIELDS = ["title", "creator", "date_desc", "date_asc"]


def build_query(base_query: str, language: str = None,
                year_from: int = None, year_to: int = None) -> str:
    """Compose the query string. Language and dates are query CLAUSES joined
    with ',AND;', not standalone parameters (the API silently ignores unknown
    params and returns unfiltered results)."""
    clauses = [base_query.strip()]
    if language:
        clauses.append(f"language,exact,{language}")
    if year_from:
        clauses.append(f"start_date,contains,{year_from}")
    if year_to:
        clauses.append(f"end_date,contains,{year_to}")
    return ",AND;".join(clauses)


def search_nli(query: str, language: str = None, material_type: str = None,
               year_from: int = None, year_to: int = None,
               per_page: int = 10, sort_field: str = None) -> list:
    """Search the NLI OpenLibrary API."""
    full_query = build_query(query, language, year_from, year_to)
    params = {
        "api_key": NLI_API_KEY,
        "query": full_query,
        "output_format": "json",
        "items_per_page": str(per_page),
    }
    if material_type:
        params["material_type"] = material_type
    if sort_field:
        params["sort_field"] = sort_field

    # urlencode with safe=',;' so the clause delimiters stay readable.
    url = f"{NLI_API_BASE}?{urllib.parse.urlencode(params, safe=',;')}"
    req = urllib.request.Request(url, headers={"User-Agent": "NLI-Heritage-Explorer/1.0"})

    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def extract_field(item: dict, field: str) -> str:
    """Extract a Dublin Core field value from an NLI result item."""
    key = f"http://purl.org/dc/elements/1.1/{field}"
    values = item.get(key, [])
    if not values:
        return ""
    first = values[0]
    return first.get("@value", first.get("@id", ""))


def format_results(results: list) -> str:
    """Format NLI results as a markdown bibliography."""
    lines = [f"## Search Results ({len(results)} items)\n"]

    for i, item in enumerate(results, 1):
        title = extract_field(item, "title") or "Untitled"
        item_type = extract_field(item, "type") or "unknown"
        date = extract_field(item, "date") or "undated"
        language = extract_field(item, "language") or "unknown"
        link = item.get("@id", "")

        lines.append(f"{i}. **{title}**")
        lines.append(f"   - Type: {item_type} | Language: {language} | Date: {date}")
        if link:
            lines.append(f"   - Link: {link}")
        lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Search the NLI OpenLibrary API")
    parser.add_argument("query", help="Base query clause (e.g., 'subject,contains,Jerusalem')")
    parser.add_argument("--type", choices=VALID_TYPES, help="material_type filter")
    parser.add_argument("--lang", help="Language code, added as a clause (heb, eng, ara, yid, lad)")
    parser.add_argument("--from-year", type=int, help="start_date clause (yyyyMMdd or yyyy)")
    parser.add_argument("--to-year", type=int, help="end_date clause (yyyyMMdd or yyyy)")
    parser.add_argument("--per-page", type=int, default=10, help="items_per_page, 1-50 (default: 10)")
    parser.add_argument("--sort", choices=VALID_SORT_FIELDS, help="sort_field")
    parser.add_argument("--json", action="store_true", help="Output raw JSON")

    args = parser.parse_args()

    if not 1 <= args.per_page <= 50:
        print("Error: --per-page must be in the range 1-50 (items_per_page).", file=sys.stderr)
        sys.exit(1)

    if not NLI_API_KEY:
        print("Error: NLI_API_KEY environment variable not set.", file=sys.stderr)
        print("Get a free key at https://api2.nli.org.il/signup/", file=sys.stderr)
        sys.exit(1)

    results = search_nli(
        query=args.query,
        language=args.lang,
        material_type=args.type,
        year_from=args.from_year,
        year_to=args.to_year,
        per_page=args.per_page,
        sort_field=args.sort,
    )

    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
    else:
        print(format_results(results))


if __name__ == "__main__":
    main()
