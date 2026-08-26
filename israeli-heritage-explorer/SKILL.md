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

**Authentication:** Every request needs an `api_key` query parameter. There are two ways to get one:
- **Sign up for a free personal key** at https://api2.nli.org.il/signup/. This is the right answer for any real research session.
- **Use NLI's published guest key** for a quick trial with no signup. NLI prints it on its own Search API page: `DVQyidFLOAjp12ib92pNJPmflmB5IessOq1CJQDK`. It is shared and heavily throttled: in testing it returned `429 OVER_RATE_LIMIT` rather than results, so treat it as a way to check your query syntax, not as a working research key.

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
| ~~`subject`~~ | **NOT USED IN THIS SKILL.** Widely used in the wild, but absent from every published NLI attribute list and example, and we could not test it against a live keyed call. Because an unrecognised attribute is dropped SILENTLY and returns UNFILTERED results (gotcha 5), a `subject` clause that is not recognised produces a populated, plausible result set that ignored the user's topic, with nothing in the output to signal it. Use `title,contains` and `creator,contains` instead. If you use `subject` anyway, you MUST read the `Errors` response header and tell the user what it said. | n/a |
| `publisher` | Publishing body | `publisher,contains,jaffa` |
| `language` | Content language (filter as a clause) | `language,exact,eng` |
| `start_date` / `end_date` | Date filter (format `yyyyMMdd` or `yyyy`) | `start_date,contains,1951` |
| `system_number` | Exact NLI system number | `system_number,exact,990023677080205171` |
| `shelfmark` | Shelfmark / call number | `shelfmark,exact,Jer344` |

Operators: `contains` (partial match, most common) and `exact`.

Standalone filters and commands (appended with `&`, outside the `query`):

| Parameter | Type | Values |
|-----------|------|--------|
| `material_type` | filter | `books`, `journals`, `images`, `audio_video`, `scores`, `maps`, `archives`, `sheets`, `dissertations`, `manuscripts`, `media`, `databases`, `NEWSPAPER`, `Identity` |
| `availability_type` | filter | `online_access`, `all_items`, `online_and_api_access`, `online_access_no_api`, `online_in_library_only`, `no_online_access` |
| `sort_field` | command | `title`, `creator`, `date_desc`, `date_asc` (NLI's own docs are inconsistent here: the parameter table says `sort_field` while a worked example on the Search API page uses `sortField`. Prefer `sort_field`, and if sorting appears to be ignored, check the `Errors` response header and try the other spelling) |
| `items_per_page` | command | a number in the range 1-50 |
| `result_page` | command | page number (total items / 50) |
| `output_format` | command | `json` (default) or `xml` |
| `count_mode` | command | `true` or `false` (return only a match count) |

**`availability_type` is the single most important parameter for a remote researcher, and it is the one most often left off.** A catalogue record is not a scan. A large share of NLI holdings are catalogued but not freely viewable online, and the default result set mixes the two, so an unfiltered search returns items the user cannot actually open. If the user needs material they can read now, filter to `online_access` (or `online_and_api_access`). If they are building a bibliography and can visit or request items, leave it open, but say in the output which items are viewable and which are not.

Unknown parameters (such as the old `rows`, `start`, `publication_year_from/_to`) are silently IGNORED by the API: the request still returns results, just unfiltered, with the skipped condition listed in an `Errors` response header. Always filter via the documented attributes above.

### Two routes: pick the one your host can actually run

This skill's data path is the NLI API, and not every host can reach it the same way. Check which tier you are on BEFORE promising the user a search:

| Your host | Route |
|---|---|
| Anything with a shell (Claude Code, Cursor, Codex, Windsurf, OpenCode, Gemini CLI) | **Route A**: call the API directly, or run `scripts/nli-search-example.py` |
| Claude Desktop | **Route A** via the local `nli-search` MCP (it runs as a local process), not via the bundled script |
| ChatGPT, Claude.ai, Manus, and any host with no shell and no local process | **Route B** below. You cannot run the bundled script and you cannot run a local stdio MCP |

**Route B: the public catalogue, in the USER's browser.** NLI's public discovery layer is Merhav, at `merhav.nli.org.il` (the main site is `nli.org.il`). It needs no API key and no signup.

**Be honest with the user about who does the searching here.** On these hosts you cannot run the search yourself. `merhav.nli.org.il` and `www.nli.org.il` sit behind a Cloudflare interstitial that an automated fetcher does not clear: in testing a headless browser was held at "Just a moment..." indefinitely, and even an interactive browser session took around twelve seconds to clear it. **Do not present a Merhav URL as an endpoint you can call, and do not promise the user results you have not seen.** Instead, hand them something they can execute: the search terms to type, which attributes to put them in, which filters to set, and what to look for. Then work from what they report back.

The interface uses the same `field,operator,value` grammar as the API (`any,contains,...`, `title,contains,...`, `creator,contains,...`), so the search thinking below transfers directly. Merhav also exposes facets the API does not surface as cleanly, notably **Usage Rights** and **Availability**, which is why it is worth sending a user there even when Route A is available to you.

### Research Workflow

Follow these steps when a user requests historical research:

**Step 1: Clarify the research scope**

Ask or infer:
- Time period. Useful search ranges: Ottoman to 1917/18, British rule 1917-1948 (military administration until 1920, civil Mandate administration from 1920), early statehood 1948-1967, modern 1967-present. These are search conveniences for building date clauses, not NLI classifications, and the boundaries are conventions rather than facts to quote at the user.
- Geographic focus (specific city, region, or all of Israel)
- Material types wanted (photographs, documents, books, maps, audio)
- Language preference (Hebrew, English, Arabic, Yiddish, Ladino)

**Step 2: Search the NLI API**

Build targeted queries. Filter by language and date INSIDE the `query` as clauses; use `material_type` and `availability_type` as standalone `&` filters. Join multiple clauses with a semicolon plus an explicit connector (`,AND;` or `,OR;`); the connector belongs to the clause it follows, and the final clause has no trailing connector. Format:

```
query=field,operator,value,AND;field,operator,value&material_type=...
```

**A caution on date clauses.** The `contains` operator is a substring match, not a
range. `start_date,contains,1917` matches dates containing "1917"; it does NOT
express "from 1917 onward", and pairing it with an `end_date,contains` clause does
not express a range either. NLI's own documentation contains an example with this
confusion in it. For a genuine range, expect to filter the returned `date` values
yourself, and tell the user what you actually filtered on rather than implying a
range query succeeded.

```
# Photographs relating to Jaffa, with a 1917 date string (type as a filter)
query=title,contains,Jaffa,AND;start_date,contains,1917&material_type=images

# Hebrew manuscripts about Jerusalem (language as a clause)
query=title,contains,Jerusalem,AND;language,exact,heb&material_type=manuscripts

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

1. **[Title]** / [Creator] ([Date])
   - Type: [manuscript/photograph/map/etc.] | Language: [Hebrew/English/etc.]
   - Held by: National Library of Israel[, Collection if the record names one]
   - Shelfmark: [shelfmark] | System number: [recordid]
   - Permalink: [NNL_ALEPH permalink, not a session URL]
   - Access: [viewable online / in library only / no online access, from availability]
   - Rights: [usage-rights status, or "not established"]
   - Relevance: [1-2 sentence annotation explaining significance]
   - Consulted: [date]

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
[Full citation list, each entry in the form given under "Citing an NLI item": title, creator, date, holding institution, collection, shelfmark, system number, permalink, access status, rights status and consultation date]

### Search Limits
[What was searched, on which attributes, with which availability filter, and what this search cannot rule out. Required: see the null-result rule under Troubleshooting]
```

### Key NLI Collections

When guiding research, be aware of these major collections:

| Collection | Content | Best search terms |
|------------|---------|------------------|
| Eran Laor Cartographic Collection | Historical maps of Jerusalem and the Holy Land, plus atlases and travel books | `material_type=maps` + geographic terms |
| Avraham Schwadron Autograph and Portrait Collections | Portraits and autographs of Jewish figures; a special collection inside the Archives Collection rather than a standalone one | `creator,contains,Schwadron` + `material_type=images` |
| National Sound Archive | Music, oral histories, radio broadcasts | `material_type=audio_video` |
| Manuscripts Collection | Hebrew, Arabic, Islamic and other manuscripts held by NLI | `material_type=manuscripts` |
| Institute of Microfilmed Hebrew Manuscripts (IMHM) | A different thing from the above: microfilm and digital SURROGATES of Hebrew manuscripts held in other collections worldwide. Use it to locate a manuscript NLI does not own | `material_type=manuscripts` |
| Historical Jewish Press (JPress) | Digitised newspapers, and NOT Hebrew-only: the collection includes Arabic and other languages | `material_type=NEWSPAPER` |
Note on collection names: NLI reorganises and renames collections, and some names in circulation (for example "Shapell") refer to a digitisation PROJECT that funded work across several collections rather than to a holding of its own. Confirm a collection name on nli.org.il before presenting it to the user as the place their material lives, and prefer describing the material to naming the collection.

### IIIF Image Access

For visual materials, the NLI provides IIIF (International Image Interoperability Framework) endpoints:

- **Image API:** `https://iiif.nli.org.il/IIIFv21/{identifier}/full/max/0/default.jpg`
- **Manifest (linkToMarc) form:** `https://iiif.nli.org.il/IIIFv21/marc/bib/{docid}` (lowercase `marc/bib`)

Prefer the `linkToMarc` / `@id` value returned in each result rather than hand-building these URLs. Use the manifest to get all available images for a multi-page item (manuscript, book, newspaper).

### Period-Specific Research Tips

**Ottoman period (search range to 1917/18):**
- Search in Ottoman Turkish, Arabic, and Hebrew
- Key subjects: land ownership (tabu), religious courts (sharia), Jewish communities (yishuv)
- Ottoman-era administrative records (land registers, sharia court records) are largely NOT NLI holdings: they sit with state and religious-court custodians. Search NLI for published, photographic, cartographic and personal-papers material about the period, and route administrative-record requests to the institutions in the table below

**British rule (search range 1917-1948):**
- 1917 is the Ottoman military defeat and the Balfour Declaration, not the start of the Mandate. British military administration ran from 1917, and civil Mandate administration began in 1920. For 1917-1920 material, search the military administration, and do not tell a user researching Mandate government records that the Mandate began in 1917
- Rich in English-language administrative documents
- Search `title,contains,Palestine` for Mandate-era materials, and try `publisher,contains,` for government and institutional imprints
- Major topics: immigration certificates, land purchases, urban planning, newspapers

**Early statehood (search range 1948-1967):**
- Government publications, Knesset records, military documents
- Immigration wave (mass aliyah) documentation
- Development town planning, cultural institution founding

**Modern period (search range 1967-present):**
- Oral history recordings, contemporary photography
- Academic research, cultural documentation

### NLI is not the only archive, and often not the right one

This skill searches NLI holdings. NLI is a library: its archival strength is personal papers, manuscripts, maps, photographs, sound and the historical press. A great deal of what users ask for is held elsewhere, and sending them to NLI for it produces a confident empty result:

| If the user wants | The primary holder is usually |
|---|---|
| Mandate-era and Israeli government administrative files, cabinet records | Israel State Archives |
| Zionist institutional records (Jewish Agency, JNF, Zionist Congresses) | Central Zionist Archives |
| Military records | IDF and Defense Establishment Archive |
| Municipal records, local planning, city council minutes | The relevant municipal archive |
| Holocaust victim and survivor records | Yad Vashem (explicitly out of scope for this skill) |
| Kibbutz and movement records | The movement archives |

Say this to the user when their question points outside NLI, rather than reporting "no results found".

### Citing an NLI item

A URL is not a citation, and the search response already contains everything a proper one needs. For each item give: title, creator, date, the holding institution (National Library of Israel), the collection where the result names one, the **shelfmark / call number**, and the **system number** (`recordid`, which also forms the stable permalink). Prefer the permalink over a session URL.

### Rights and reuse

Users of this skill routinely want to reproduce an image in a report, a slide deck or a publication. **Do not imply that anything found here is free to reuse.** Rights differ item by item: NLI's catalogue distinguishes free use, non-commercial use, use for research/study/teaching, and items where copying is prohibited outright. The Usage Rights facet in Merhav (Route B) is the fastest way to see an item's status, and NLI runs a copyright-queries service for anything unclear. State the rights status alongside any image you surface, and where it is unknown, say it is unknown.

## Bundled Resources

See the `references/` directory for:
- `nli-api-reference.md` -- full API parameter reference with examples
- `historical-periods.md` -- detailed Israeli historical periods with key search terms

## Gotchas

1. **Query minimum length:** NLI documents that a basic query must contain at least a three-character string over one of the search attributes. Single Hebrew letters and very short English words fail this. Use descriptive terms instead.

2. **Hebrew search vs. English search:** Many NLI records have metadata in Hebrew only. If an English search returns few results, retry with Hebrew terms. The API does NOT auto-translate between languages.

3. **Date format quirks:** The `date` field in results uses inconsistent formats: some items have `YYYYMMDD`, others have `YYYY`, and some have free-text dates like `[circa 1930]` or `תרצ"ב`. Parse dates defensively.

4. **Material type values are a fixed set:** The valid `material_type` values are `books`, `journals`, `images`, `audio_video`, `scores`, `maps`, `archives`, `sheets`, `dissertations`, `manuscripts`, `media`, `databases`, `NEWSPAPER`, `Identity`. There is no `audio`, `videos`, `articles`, or `rareBooks` (use `audio_video`, `NEWSPAPER`, etc.). An invalid value is silently dropped (the request returns UNFILTERED results, not zero results), with the dropped condition noted in the response `Errors` header. Newspapers use the all-caps `NEWSPAPER`.

5. **Unknown parameters are ignored, not rejected:** Passing a parameter the API does not recognize (for example the old `rows`, `start`, `publication_year_from`) does not error: the condition is silently skipped and you get unfiltered results. Filter language and dates as query clauses (`language,exact,eng`, `start_date,contains,1951`), not as standalone parameters.

6. **Cloudflare protection is triggered by the `curl/*` User-Agent string, not by your IP and not by a missing User-Agent.** This was previously documented as a datacenter-IP block, which sent people down the wrong path. Tested behaviour from a single machine: sending `curl/8.x` as the User-Agent returns an HTML Cloudflare challenge page. Sending `python-urllib/3.11`, a browser string, the bundled script's own `NLI-Heritage-Explorer/1.0`, or NO `User-Agent` header at all, all reach the real API and return structured JSON. In other words the rule targets the curl signature specifically. So: send any User-Agent other than curl's default, and if you are debugging, check whether the body is HTML (Cloudflare) or JSON (the API answering), because that distinction tells you which problem you have. One trap when diagnosing this: a bare `curl` command with no `-A` flag is NOT a request without a User-Agent, it still sends `curl/x.y.z`, which is exactly the blocked string.

7. **`subject` is UNCONFIRMED as a recognised attribute, and a wrong attribute fails SILENTLY.** NLI's documentation names the filterable attributes explicitly (`start_date` / `end_date`, `language`, `system_number`, `shelfmark`) but describes the text side only as "one / few / all descriptive attributes", without publishing a closed list. `subject` appears in none of the worked examples, and we have not been able to test it against a live keyed call. Treat it as unverified rather than as known-good or known-bad. Combined with gotcha 5, the failure mode is nasty: if the API does not recognise the attribute, it drops the condition and returns UNFILTERED results, which look like a successful broad search. Whenever you use `subject`, inspect the `Errors` response header. If it reports the condition was skipped, fall back to `title,contains` and `creator,contains`, and say so in the output rather than presenting unfiltered results as a topical search.

8. **`exact` is unforgiving on names and Hebrew orthography.** Several examples here use `title,exact`. Under `exact` a maqaf (`תל-אביב` vs `תל אביב`), defective vs plene spelling (`ירושלם` vs `ירושלים`), and Latin transliteration variants (Herzl / Hertzl / Herzel / הרצל) will not match. Use `contains` for personal and place names, and try more than one spelling before concluding NLI holds nothing.

## Troubleshooting

### Query rejected as too short
NLI documents that a basic query must include at least a three-character string over one of the search attributes. Single Hebrew letters and very short tokens fail this. Use a longer, more descriptive term. (Earlier versions of this skill quoted a specific error string here; the documented rule is the reliable thing to match on, not a remembered message.)

### Empty results for a known topic
**First, the rule that matters most: an empty result set does not prove the material does not exist.** The API searches catalogued records. Uncatalogued and unprocessed material is invisible to it, holdings elsewhere are invisible to it, and a condition the API silently dropped can distort the result in either direction. Never report "NLI has nothing on this". Report what you searched, on which attributes, with which availability filter, and what came back.

Then try:
1. Switch between English and Hebrew search terms, and try Arabic where the topic warrants it
2. Use `contains` rather than `exact`, and try spelling variants (see gotcha 8)
3. Widen or drop the date clauses. Remember they are substring matches, not ranges, so an ANDed start_date + end_date pair asks for a date string containing BOTH years and will usually match nothing
4. Remove the `material_type` filter to search across all types
5. Check the `Errors` response header before concluding anything: if a condition was dropped, your "empty" or "full" result is not what you think it is
6. Consider that the right institution may not be NLI at all (see the table above)

Note on `subject`: earlier versions of this skill recommended switching to `subject,contains` here. That recommendation has been REMOVED, and no example in this skill uses `subject` any more. `subject` is absent from every published NLI attribute list, and an unrecognised attribute is dropped silently and returns UNFILTERED results, so the recommendation could turn a zero-result search into a falsely full one with nothing in the output to signal it. Broaden with `title,contains` and `creator,contains`, or use the browser route and reuse the exact subject heading the catalogue itself shows.

### 403 or 429 response
Do not guess the cause: the API distinguishes them clearly in the response BODY, and three different problems all surface as a non-200. Read the body before telling the user anything.

| What the body contains | What it actually means | What to do |
|---|---|---|
| JSON with `"code": "API_KEY_MISSING"` | No `api_key` parameter was sent | Add the parameter |
| JSON with `"code": "API_KEY_INVALID"` | The key is wrong, mistyped or revoked | Get a fresh key at https://api2.nli.org.il/signup/ |
| JSON with `"code": "OVER_RATE_LIMIT"` (HTTP 429) | The key is valid but throttled. This is the normal outcome for NLI's shared guest key | Wait, or use a personal key |
| An HTML page mentioning Cloudflare | Bot protection, triggered by the `curl/*` User-Agent string | Send any other User-Agent and retry; see gotcha 6 |

Only the second row is "the key expired". Earlier versions of this skill asserted that cause for every 403, which sent users to re-issue a key that was working.

### IIIF image not loading
Some items are restricted rather than broken. Use `availability_type` to reason about this: `online_in_library_only` marks material viewable only on NLI premises, and `no_online_access` marks material with no digital surrogate at all, so a catalogue hit for either will never yield an image. Do not report a specific access-status field name unless you can see it in the response you actually received.
