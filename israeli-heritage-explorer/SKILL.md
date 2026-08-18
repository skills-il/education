---
name: israeli-heritage-explorer
description: "Research Israeli and Jewish cultural heritage using the National Library of Israel's digital archives. Use when a user asks about Israeli history, Jewish heritage, historical photographs, ancient manuscripts, British Mandate documents, immigration waves, or wants primary source citations from NLI. Produces annotated research reports with direct links to NLI assets including manuscripts, photographs, maps, government records, and oral histories. Prevents hours of manual archive browsing and missed primary sources by leveraging the NLI OpenLibrary API with structured field queries. Do NOT use for modern news, current events, academic journal articles behind paywalls, or Yad Vashem Holocaust victim searches (use dedicated Holocaust research tools)."
license: MIT
---

# Israeli Heritage Explorer

## Problem

Researching Israeli and Jewish cultural history requires navigating millions of records across the National Library of Israel's digital archives. Without structured access, researchers spend hours browsing the NLI website manually, miss relevant primary sources, and struggle to connect related materials across collections. This skill provides AI-powered search and report generation directly through the NLI OpenLibrary API, transforming raw archive data into organized, citation-ready research output.

## Instructions

### Overview

This skill searches the National Library of Israel (NLI) digital archives via the OpenLibrary API. The NLI holds millions of items spanning Jewish heritage and Israeli culture: ancient manuscripts, government records, historical photographs, maps, music recordings, oral histories, and scholarly publications.

### When to Use

- User asks about Israeli history (any period: Ottoman, British Mandate, early statehood, modern)
- User wants primary sources on Jewish heritage topics
- User needs historical photographs or maps of Israeli locations
- User asks about immigration waves (aliyah) to Israel
- User wants to research a specific community, neighborhood, or institution's history
- User needs an annotated bibliography on an Israeli cultural topic

### API Access

The NLI OpenLibrary API is free. The base endpoint is:

```
https://api.nli.org.il/openlibrary/search
```

**Authentication:** Requires an API key passed as `api_key` query parameter. Users can get a free key at https://api2.nli.org.il/signup/. The `nli-search` MCP server may include a visitor key for basic access (verify with the MCP).

**Recommended MCP Server:** Install the `nli-search` MCP for direct AI-powered access to the NLI API with natural language queries, IIIF image retrieval, and media streaming.

| MCP Server | What it provides |
|------------|-----------------|
| [nli-search](https://agentskills.co.il/he/mcp/nli-search) | Natural language search, image retrieval via IIIF, media streaming, batch result processing |

### Search Parameters

A request is `query={clauses}` plus optional standalone filters and commands, joined with `&`. Most filtering happens INSIDE the `query` as `field,operator,value` clauses (this is the documented mechanism). Language and date filtering are query clauses, NOT standalone parameters.

The query attributes (used as the `field` in a clause):

| Attribute | Description | Example clause |
|-----------|-------------|----------------|
| `title` | Title of the work | `title,exact,jerusalem` |
| `creator` | Author, photographer, artist | `creator,contains,Ben Gurion` |
| `subject` | Subject heading (topical, geographic, personal) | `subject,contains,Zionism` |
| `publisher` | Publishing body | `publisher,contains,jaffa` |
| `language` | Content language (filter as a clause) | `language,exact,eng` |
| `start_date` / `end_date` | Date filter (format `yyyyMMdd` or `yyyy`) | `start_date,contains,1951` |
| `system_number` | Exact NLI system number | `system_number,exact,990023677080205171` |

Operators: `contains` (partial match, most common) and `exact`.

Standalone filters and commands (appended with `&`, outside the `query`):

| Parameter | Type | Values |
|-----------|------|--------|
| `material_type` | filter | `books`, `journals`, `images`, `audio_video`, `scores`, `maps`, `archives`, `sheets`, `dissertations`, `manuscripts`, `media`, `databases`, `NEWSPAPER`, `Identity` |
| `availability_type` | filter | `online_access`, `all_items`, `online_and_api_access`, `online_access_no_api`, `online_in_library_only`, `no_online_access` |
| `sort_field` | command | `title`, `creator`, `date_desc`, `date_asc` |
| `items_per_page` | command | a number in the range 1-50 |
| `result_page` | command | page number (total items / 50) |
| `output_format` | command | `json` (default) or `xml` |
| `count_mode` | command | `true` or `false` (return only a match count) |

Unknown parameters (such as the old `rows`, `start`, `publication_year_from/_to`) are silently IGNORED by the API: the request still returns results, just unfiltered, with the skipped condition listed in an `Errors` response header. Always filter via the documented attributes above.

### Research Workflow

Follow these steps when a user requests historical research:

**Step 1: Clarify the research scope**

Ask or infer:
- Time period (Ottoman 1517-1917, British Mandate 1917-1948, early statehood 1948-1967, modern 1967-present)
- Geographic focus (specific city, region, or all of Israel)
- Material types wanted (photographs, documents, books, maps, audio)
- Language preference (Hebrew, English, Arabic, Yiddish, Ladino)

**Step 2: Search the NLI API**

Build targeted queries. Filter by language and date INSIDE the `query` as clauses; use `material_type` and `availability_type` as standalone `&` filters. Join multiple clauses with a semicolon plus an explicit connector (`,AND;` or `,OR;`); the connector belongs to the clause it follows, and the final clause has no trailing connector. Format:

```
query=field,operator,value,AND;field,operator,value&material_type=...
```

```
# Historical photographs of Jaffa during British Mandate (date as a clause, type as a filter)
query=subject,contains,Jaffa,AND;start_date,contains,1917&material_type=images

# Hebrew manuscripts about Jerusalem (language as a clause)
query=subject,contains,Jerusalem,AND;language,exact,heb&material_type=manuscripts

# David Ben-Gurion's writings in Hebrew
query=creator,contains,Ben Gurion,AND;language,exact,heb&material_type=books

# American Colony photographs of Jerusalem in English
query=title,exact,jerusalem,AND;creator,contains,American Colony,AND;language,exact,eng&material_type=images
```

Use `,OR;` to broaden instead of narrow. To page through more than 50 results add `&result_page=2`; to change ordering add `&sort_field=date_asc`. Do NOT use `material_type=images` with the old values like `photos` or `videos`; only the values in the Search Parameters table are valid (invalid values are silently dropped).

**Step 3: Process results**

Each result contains:
- `title` -- item title (often in Hebrew)
- `type` -- material type (book, archive, image, etc.)
- `date` -- publication/creation date
- `publisher` -- publishing body
- `language` -- content language
- `recordid` -- unique NLI identifier
- `@id` -- direct link to the item on nli.org.il
- `linkToMarc` -- IIIF manifest link for images

**Step 4: Generate research output**

Format findings into one of these deliverables:

**Annotated Bibliography:**
```markdown
## Annotated Bibliography: [Topic]

### Primary Sources

1. **[Title]** ([Date])
   - Type: [manuscript/photograph/map/etc.]
   - Language: [Hebrew/English/etc.]
   - NLI Link: [direct URL]
   - Relevance: [1-2 sentence annotation explaining significance]

2. ...

### Secondary Sources
...

### Suggested Further Research
- [Related topics or collections to explore]
```

**Research Report:**
```markdown
## Research Report: [Topic]

### Historical Context
[2-3 paragraphs providing context based on found sources]

### Key Primary Sources
[Numbered list with annotations]

### Visual Materials
[Photographs, maps with descriptions and NLI links]

### Timeline
[Chronological list of key events with source citations]

### Source List
[Full citation list]
```

### Key NLI Collections

When guiding research, be aware of these major collections:

| Collection | Content | Best search terms |
|------------|---------|------------------|
| Eran Laor Map Collection | 30,000+ historical maps of the Holy Land | `material_type=maps` + geographic terms |
| Schwadron Portrait Collection | Historical portraits of Jewish figures | `subject,contains,Schwadron` + `material_type=images` |
| National Sound Archive | Music, oral histories, radio broadcasts | `material_type=audio_video` |
| Manuscripts Institute | Hebrew, Arabic, and other manuscripts | `material_type=manuscripts` |
| Shapell Archive | Ottoman and British Mandate era documents | `subject,contains,Palestine,AND;start_date,contains,1920` |
| Press Collections | Historical Hebrew newspapers | `material_type=NEWSPAPER` |

### IIIF Image Access

For visual materials, the NLI provides IIIF (International Image Interoperability Framework) endpoints:

- **Image API:** `https://iiif.nli.org.il/IIIFv21/{identifier}/full/max/0/default.jpg`
- **Manifest (linkToMarc) form:** `https://iiif.nli.org.il/IIIFv21/marc/bib/{docid}` (lowercase `marc/bib`)

Prefer the `linkToMarc` / `@id` value returned in each result rather than hand-building these URLs. Use the manifest to get all available images for a multi-page item (manuscript, book, newspaper).

### Period-Specific Research Tips

**Ottoman Period (1517-1917):**
- Search in Ottoman Turkish, Arabic, and Hebrew
- Key subjects: land ownership (tabu), religious courts (sharia), Jewish communities (yishuv)
- The NLI holds Ottoman-era land records and court documents

**British Mandate (1917-1948):**
- Rich in English-language administrative documents
- Search `subject,contains,Palestine` for Mandate-era materials
- Major topics: immigration certificates, land purchases, urban planning, newspapers

**Early Statehood (1948-1967):**
- Government publications, Knesset records, military documents
- Immigration wave (mass aliyah) documentation
- Development town planning, cultural institution founding

**Modern Period (1967-present):**
- Oral history recordings, contemporary photography
- Academic research, cultural documentation

## Bundled Resources

See the `references/` directory for:
- `nli-api-reference.md` -- full API parameter reference with examples
- `historical-periods.md` -- detailed Israeli historical periods with key search terms

## Gotchas

1. **Query minimum length:** The NLI API requires search terms longer than 2 characters. Single Hebrew letters or very short English words return errors. Use descriptive subject terms instead.

2. **Hebrew search vs. English search:** Many NLI records have metadata in Hebrew only. If an English search returns few results, retry with Hebrew terms. The API does NOT auto-translate between languages.

3. **Date format quirks:** The `date` field in results uses inconsistent formats: some items have `YYYYMMDD`, others have `YYYY`, and some have free-text dates like `[circa 1930]` or `תרצ"ב`. Parse dates defensively.

4. **Material type values are a fixed set:** The valid `material_type` values are `books`, `journals`, `images`, `audio_video`, `scores`, `maps`, `archives`, `sheets`, `dissertations`, `manuscripts`, `media`, `databases`, `NEWSPAPER`, `Identity`. There is no `audio`, `videos`, `articles`, or `rareBooks` (use `audio_video`, `NEWSPAPER`, etc.). An invalid value is silently dropped (the request returns UNFILTERED results, not zero results), with the dropped condition noted in the response `Errors` header. Newspapers use the all-caps `NEWSPAPER`.

5. **Unknown parameters are ignored, not rejected:** Passing a parameter the API does not recognize (for example the old `rows`, `start`, `publication_year_from`) does not error: the condition is silently skipped and you get unfiltered results. Filter language and dates as query clauses (`language,exact,eng`, `start_date,contains,1951`), not as standalone parameters.

6. **Cloudflare protection:** The NLI API is protected by Cloudflare. Requests from cloud/datacenter IPs may be blocked. The API works reliably from residential IPs and local development environments. If blocked, the MCP server running locally on the user's machine will work.

## Troubleshooting

### "Please use more than two characters" error
The search query is too short. Use a longer, more descriptive term.

### Empty results for a known topic
Try different search strategies:
1. Switch between English and Hebrew search terms
2. Broaden the date range
3. Remove the `material_type` filter to search across all types
4. Use `subject,contains` instead of a free-text query

### 403 Forbidden response
The API key may be invalid or expired. Get a new free key at https://api2.nli.org.il/signup/. If using the nli-search MCP, it may include a visitor key (verify with the MCP).

### IIIF image not loading
Some items have restricted access. Check the `accessRights` field in the search result. Items marked `online_resources_nli` may require NLI library membership for full access.
