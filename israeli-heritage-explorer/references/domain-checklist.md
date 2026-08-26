# Domain Checklist: NLI OpenLibrary Search (heritage research)

Scope: what a skill that searches the National Library of Israel (NLI) digital
collections, combining creator + subject + date, fetching permalinks, and
respecting the API key + rate limits, MUST/SHOULD cover. Used to review
`israeli-heritage-explorer`.

NOTE ON SOURCING: the canonical NLI search-api docs page
(`www.nli.org.il/en/research-and-teach/open-library/search-api`) and the docs on
`api2.nli.org.il` are Cloudflare-blocked (HTTP 403) from datacenter IPs. Items
below are cited to the search-engine index of those official pages and to live
hosts that did respond. Anything that could only be confirmed via the blocked
docs is marked [needs residential-IP confirm].

## Must cover (a researcher's queries fail or are wrong without these)

1. **Correct base endpoint + auth.** `https://api.nli.org.il/openlibrary/search`
   with `api_key` passed as a GET query parameter on every request (even for
   POST). Cited: search-index of the official search-api page; api2 api-key doc
   ("pass the key as a GET parameter in the URL even when using POST/PUT").
2. **Correct `query` clause grammar.** `field,operator,value`; multiple clauses
   joined by `;` with an explicit `AND`/`OR` appended to the clause they follow,
   e.g. `title,exact,jerusalem,AND;creator,contains,Jerusalem,AND;language,exact,eng,AND;start_date,contains,1951`.
   Operators include `exact` and `contains`. Cited: the verbatim official
   example surfaced in the search index of the search-api page.
3. **Filtering by language and date must be expressed in a form the API
   actually accepts.** Verified via Playwright (2026-06-04): language and date
   filtering are query CLAUSES (`language,exact,eng`, `start_date,contains,1951`),
   NOT standalone parameters. `material_type=` and `availability_type=` ARE real
   standalone filters; `language=` and `publication_year_from/_to=` are NOT
   documented and are silently ignored (request returns unfiltered results, with
   an `Errors` header). The skill must use clause-form for language/date.
4. **Permalink retrieval from results.** Each result carries an `@id` permalink
   (NNL_ALEPH form on `www.nli.org.il`); the skill must instruct using the
   returned `@id` rather than hand-constructing URLs. Cited: indexed manifest
   DocId `NNL_ALEPH11357291990005171`; live IIIF URL below.
5. **Cloudflare / IP reality + key acquisition.** Datacenter IPs are blocked;
   residential IP or a locally-running MCP is needed; a free key is obtained via
   NLI signup. Cited: live 403 on the docs/IIIF hosts; signup host reachable.

## Should cover (completeness / quality, not correctness-breaking)

6. **`sort_field` and `output_format`.** Both are documented standalone commands;
   a daily researcher wants `sort_field` (values `title`, `creator`, `date_desc`,
   `date_asc`) and `output_format=json|xml`. The skill documents `output_format`
   but originally omitted `sort_field`. Cited: official user-help example
   `...&output_format=xml&result_page=2&sort_field=title` (verified via Playwright
   2026-06-04; note the parameter name is `sort_field` with an underscore, not
   `sortField`).
7. **Guest vs. registered access + query limits.** Guest accounts work on a
   trial basis with limited query counts; heavy use needs a registered key.
   Cited: search-index of the search-api/user-help page.
8. **IIIF image + Presentation (manifest) access.** Real host `iiif.nli.org.il`;
   `linkToMarc` resolves to `IIIFv21/marc/bib/<docid>` and NLI exposes a separate
   Presentation API (manifest). Cited: live URL
   `https://iiif.nli.org.il/IIIFv21/marc/bib/990000681800205171`; indexed
   Presentation API page.
9. **Hebrew/English metadata asymmetry + defensive date parsing.** Many records
   are Hebrew-only; `date` values are mixed (`YYYYMMDD`, `YYYY`, free text,
   Hebrew era). Reasonable secondary-source / domain knowledge.
10. **Material-type vocabulary.** Verified via Playwright (2026-06-04): the exact
    accepted set is `books`, `journals`, `images`, `audio_video`, `scores`,
    `maps`, `archives`, `sheets`, `dissertations`, `manuscripts`, `media`,
    `databases`, `NEWSPAPER`, `Identity`. `audio`, `videos`, `articles`,
    `rareBooks` are invalid.

## Out of scope

- Yad Vashem Holocaust victim databases (separate system; skill correctly excludes).
- Paywalled academic journals / modern news / current events.
- Z39.50 / MARC bulk bibliographic export (separate `hasadna/nli-z3950` path).
- Writing to NLI (the API is read/search only).

## Authoritative sources

- NLI Search API docs (Cloudflare-blocked; via search index):
  https://www.nli.org.il/en/research-and-teach/open-library/search-api
- NLI Search API common-usage / user-help (via index):
  https://www.nli.org.il/en/research-and-teach/open-library/search-api/user-help
- NLI API signup: https://api2.nli.org.il/signup/
- NLI Search API docs (live pages are behind Cloudflare and return 403 to fetchers; the readable captures are):
  - user-help: http://web.archive.org/web/20240912225154/https://www.nli.org.il/en/research-and-teach/open-library/search-api/user-help
  - search-api: http://web.archive.org/web/20250523021247/https://www.nli.org.il/en/research-and-teach/open-library/search-api
- NLI Presentation (Manifest) API:
  https://www.nli.org.il/en/research-and-teach/open-library/presentation-api
- Live IIIF resource (confirms host + linkToMarc form):
  https://iiif.nli.org.il/IIIFv21/marc/bib/990000681800205171
- NLI (Wikipedia, secondary, for collection scale): https://en.wikipedia.org/wiki/National_Library_of_Israel
