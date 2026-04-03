#!/usr/bin/env python3
"""
Example script: Search the NLI OpenLibrary API and format results.

Usage:
    python nli-search-example.py "subject,contains,Tel Aviv" --type images --lang heb --rows 10
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

VALID_TYPES = [
    "books", "images", "manuscripts", "maps",
    "audio", "videos", "articles", "journals", "rareBooks"
]


def search_nli(query: str, material_type: str = None, language: str = None,
               year_from: int = None, year_to: int = None, rows: int = 10) -> list:
    """Search the NLI OpenLibrary API."""
    params = {
        "query": query,
        "output_format": "json",
        "rows": str(rows),
        "api_key": NLI_API_KEY,
    }
    if material_type:
        params["material_type"] = material_type
    if language:
        params["language"] = language
    if year_from:
        params["publication_year_from"] = str(year_from)
    if year_to:
        params["publication_year_to"] = str(year_to)

    url = f"{NLI_API_BASE}?{urllib.parse.urlencode(params)}"
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
    parser.add_argument("query", help="Search query (e.g., 'subject,contains,Jerusalem')")
    parser.add_argument("--type", choices=VALID_TYPES, help="Material type filter")
    parser.add_argument("--lang", help="Language code (heb, eng, ara, yid, lad)")
    parser.add_argument("--from-year", type=int, help="Publication year from")
    parser.add_argument("--to-year", type=int, help="Publication year to")
    parser.add_argument("--rows", type=int, default=10, help="Number of results (default: 10)")
    parser.add_argument("--json", action="store_true", help="Output raw JSON")

    args = parser.parse_args()

    if not NLI_API_KEY:
        print("Error: NLI_API_KEY environment variable not set.", file=sys.stderr)
        print("Get a free key at https://api2.nli.org.il/signup/", file=sys.stderr)
        sys.exit(1)

    results = search_nli(
        query=args.query,
        material_type=args.type,
        language=args.lang,
        year_from=args.from_year,
        year_to=args.to_year,
        rows=args.rows,
    )

    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
    else:
        print(format_results(results))


if __name__ == "__main__":
    main()
