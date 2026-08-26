#!/usr/bin/env python3
"""
Example script: Search the NLI OpenLibrary API and format results.

Filtering follows the official NLI docs: language and date are query CLAUSES
(joined with ",AND;"), while material_type and availability_type are standalone
"&" filters. There is no rows/start or publication_year_from/_to; pagination
uses items_per_page (1-50) and result_page.

Usage:
    python nli-search-example.py "title,contains,Tel Aviv" --type images --lang heb --per-page 10
    python nli-search-example.py "creator,contains,Herzl" --type books --year 1890
    python nli-search-example.py "title,contains,Jerusalem" --online-only --count

NOTE ON DATES: `contains` is a SUBSTRING match, not a range. `--year 1890`
matches date strings containing "1890". There is no range query; to cover a
span, run several years or filter the returned `date` values yourself. The old
--from-year/--to-year pair ANDed two substring clauses, which asked for a date
containing BOTH years and therefore matched almost nothing.
"""

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
import urllib.parse

NLI_API_BASE = "https://api.nli.org.il/openlibrary/search"

# NLI publishes a guest key on its own Search API page. It is shared and heavily
# throttled (it commonly returns 429 OVER_RATE_LIMIT), so it is only good for
# checking that a query parses. Set NLI_API_KEY to a personal key for real work.
NLI_GUEST_KEY = "DVQyidFLOAjp12ib92pNJPmflmB5IessOq1CJQDK"
API_KEY_ENV = "NLI_API_KEY"


def resolve_api_key(use_guest: bool) -> str:
    """Resolve the API key once, in one place.

    The key is read here and passed explicitly to search_nli() rather than
    held in a module-level global. Same behaviour, narrower credential
    surface, and the flow from environment to request is obvious.
    """
    if use_guest:
        return NLI_GUEST_KEY
    return os.environ.get(API_KEY_ENV, "")

# NLI's Cloudflare rule targets the curl User-Agent signature specifically.
# Any other UA gets through, and so does sending no UA header at all; only
# `curl/x.y.z` returns an HTML challenge page instead of the API.
USER_AGENT = "NLI-Heritage-Explorer/1.0"

# Valid material_type values per the official NLI search-api user-help page.
VALID_TYPES = [
    "books", "journals", "images", "audio_video", "scores", "maps",
    "archives", "sheets", "dissertations", "manuscripts", "media",
    "databases", "NEWSPAPER", "Identity",
]

VALID_SORT_FIELDS = ["title", "creator", "date_desc", "date_asc"]


def build_query(base_query: str, language: str = None, year: int = None) -> str:
    """Compose the query string. Language and dates are query CLAUSES joined
    with ',AND;', not standalone parameters (the API silently ignores unknown
    params and returns unfiltered results).

    Only ONE year clause is emitted. `contains` is a substring match, so
    ANDing a start_date and an end_date clause asks for a date string
    containing both years, which matches almost nothing.
    """
    clauses = [base_query.strip()]
    if language:
        clauses.append(f"language,exact,{language}")
    if year:
        clauses.append(f"start_date,contains,{year}")
    return ",AND;".join(clauses)


def search_nli(api_key: str, query: str, language: str = None,
               material_type: str = None, year: int = None, per_page: int = 10,
               sort_field: str = None, availability: str = None,
               result_page: int = None, count_only: bool = False):
    """Search the NLI OpenLibrary API."""
    full_query = build_query(query, language, year)
    params = {
        "api_key": api_key,
        "query": full_query,
        "output_format": "json",
        "items_per_page": str(per_page),
    }
    if material_type:
        params["material_type"] = material_type
    if sort_field:
        params["sort_field"] = sort_field
    if availability:
        params["availability_type"] = availability
    if result_page:
        params["result_page"] = str(result_page)
    if count_only:
        params["count_mode"] = "true"

    # urlencode with safe=',;' so the clause delimiters stay readable.
    url = f"{NLI_API_BASE}?{urllib.parse.urlencode(params, safe=',;')}"
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})

    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            body = resp.read().decode("utf-8")
            if "<html" in body[:400].lower():
                raise SystemExit(
                    "The API returned HTML, not JSON. That is a Cloudflare "
                    "challenge, triggered by the curl/* User-Agent string."
                )
            errors = resp.headers.get("Errors")
            if errors:
                # A condition the API did not recognise is DROPPED, and the
                # request still succeeds with UNFILTERED results. Surface it
                # rather than presenting a broad result set as a filtered one.
                print(f"WARNING: the API ignored part of your query: {errors}",
                      file=sys.stderr)
            try:
                return json.loads(body)
            except json.JSONDecodeError:
                raise SystemExit(f"Could not parse the API response: {body[:300]}")
    except urllib.error.HTTPError as exc:
        raw = exc.read().decode("utf-8", "replace")
        errors = exc.headers.get("Errors")
        if errors:
            print(f"WARNING: the API ignored part of your query: {errors}",
                  file=sys.stderr)
        if "cloudflare" in raw.lower():
            raise SystemExit(
                "Blocked by Cloudflare bot protection, not by the API. This is "
                "triggered by the curl/* User-Agent string, not by your IP."
            )
        try:
            payload = json.loads(raw)
            # The code has been observed nested under "error"; accept a
            # top-level "code" too rather than losing the guidance below.
            code = payload.get("error", {}).get("code") or payload.get("code")
        except Exception:
            code = None
        if not code:
            raise SystemExit(f"HTTP {exc.code} from the NLI API: {raw[:300]}")
        hints = {
            "API_KEY_MISSING": "No api_key was sent.",
            "API_KEY_INVALID": "The key is wrong or revoked. Get one at "
                               "https://api2.nli.org.il/signup/",
            "OVER_RATE_LIMIT": "The key is valid but throttled. This is normal "
                               "for the shared guest key; use a personal key.",
        }
        raise SystemExit(f"HTTP {exc.code} {code}: {hints.get(code, raw[:200])}")
    except urllib.error.URLError as exc:
        raise SystemExit(f"Could not reach the NLI API: {exc.reason}")


def extract_field(item: dict, field: str) -> str:
    """Extract a Dublin Core field value from an NLI result item."""
    key = f"http://purl.org/dc/elements/1.1/{field}"
    values = item.get(key, [])
    if not values:
        return ""
    first = values[0]
    return first.get("@value", first.get("@id", ""))


def format_results(results) -> str:
    """Format NLI results as a markdown bibliography."""
    if not isinstance(results, list):
        # The API answers errors as a JSON object, not a list.
        return f"Unexpected response shape from the API: {str(results)[:300]}"
    if not results:
        return ("## Search Results (0 items)\n\n"
                "No matches. This does NOT mean NLI holds nothing: the API "
                "searches catalogued records only, and a dropped condition can "
                "empty a result set silently.\n"
                "Try: the other language; `contains` instead of `exact`; "
                "spelling variants; widening or REMOVING the --year clause "
                "(it is a substring match, not a range); dropping --type. "
                "Check stderr for an ignored-condition warning, and consider "
                "that the material may be held by another institution.\n")
    lines = [f"## Search Results ({len(results)} items)\n"]

    for i, item in enumerate(results, 1):
        title = extract_field(item, "title") or "Untitled"
        creator = extract_field(item, "creator") or "unknown creator"
        item_type = extract_field(item, "type") or "unknown"
        date = extract_field(item, "date") or "undated"
        language = extract_field(item, "language") or "unknown"
        recordid = extract_field(item, "recordid")
        link = item.get("@id", "")

        # These are the fields the skill's citation rule requires. Do not trim
        # them: a title and a URL is not a citation.
        lines.append(f"{i}. **{title}** / {creator}")
        lines.append(f"   - Type: {item_type} | Language: {language} | Date: {date}")
        lines.append("   - Held by: National Library of Israel")
        if recordid:
            lines.append(f"   - System number: {recordid}")
        if link:
            lines.append(f"   - Permalink: {link}")
        lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Search the NLI OpenLibrary API")
    parser.add_argument("query", help="Base query clause (e.g., 'title,contains,Jerusalem')")
    parser.add_argument("--type", choices=VALID_TYPES, help="material_type filter")
    parser.add_argument("--lang", help="Language code, added as a clause (heb, eng, ara, yid, lad)")
    parser.add_argument("--year", type=int,
                        help="start_date substring clause (yyyy or yyyyMMdd). "
                             "NOT a range: contains is a substring match")
    parser.add_argument("--online-only", action="store_true",
                        help="availability_type=online_access (material you can actually read now)")
    parser.add_argument("--page", type=int, help="result_page, for paging past the first page")
    parser.add_argument("--count", action="store_true",
                        help="count_mode=true, return only the number of matches")
    parser.add_argument("--per-page", type=int, default=10, help="items_per_page, 1-50 (default: 10)")
    parser.add_argument("--sort", choices=VALID_SORT_FIELDS, help="sort_field")
    parser.add_argument("--json", action="store_true", help="Output raw JSON")
    parser.add_argument("--guest", action="store_true",
                        help="Use NLI's published shared guest key (throttled)")

    args = parser.parse_args()

    if not 1 <= args.per_page <= 50:
        print("Error: --per-page must be in the range 1-50 (items_per_page).", file=sys.stderr)
        sys.exit(1)

    if args.guest:
        print("Using NLI's shared guest key. Expect 429 OVER_RATE_LIMIT; "
              "get a personal key at https://api2.nli.org.il/signup/",
              file=sys.stderr)
    api_key = resolve_api_key(args.guest)
    if not api_key:
        print(f"Error: {API_KEY_ENV} environment variable not set.", file=sys.stderr)
        print("Get a free key at https://api2.nli.org.il/signup/", file=sys.stderr)
        print("Or pass --guest to try NLI's shared (throttled) guest key.",
              file=sys.stderr)
        sys.exit(1)

    results = search_nli(
        api_key=api_key,
        query=args.query,
        language=args.lang,
        material_type=args.type,
        year=args.year,
        per_page=args.per_page,
        sort_field=args.sort,
        availability="online_access" if args.online_only else None,
        result_page=args.page,
        count_only=args.count,
    )

    if args.json:
        print(json.dumps(results, indent=2, ensure_ascii=False))
    else:
        print(format_results(results))


if __name__ == "__main__":
    main()
