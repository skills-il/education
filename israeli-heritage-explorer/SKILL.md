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

**Authentication:** Requires an API key passed as `api_key` query parameter. Users can get a free key at https://api2.nli.org.il/signup/. The `nli-search` MCP server ships with a default visitor key for basic access.

**Recommended MCP Server:** Install the `nli-search` MCP for direct AI-powered access to the NLI API with natural language queries, IIIF image retrieval, and media streaming.

| MCP Server | What it provides |
|------------|-----------------|
| [nli-search](https://agentskills.co.il/he/mcps/nli-search) | Natural language search, image retrieval via IIIF, media streaming, batch result processing |

### Search Parameters

The API accepts structured queries in `field,operator,value` format:

| Parameter | Description | Example |
|-----------|-------------|---------|
| `query` | Main search (field,operator,value) | `subject,contains,Tel Aviv history` |
| `material_type` | Filter by type | `books`, `images`, `manuscripts`, `maps`, `audio`, `videos`, `articles`, `journals`, `rareBooks` |
| `language` | Filter by language | `heb`, `eng`, `ara`, `yid`, `lad` |
| `creator` | Filter by author/creator | `creator,contains,Ben Gurion` |
| `subject` | Filter by subject heading | `subject,contains,Zionism` |
| `publication_year_from` / `publication_year_to` | Date range | `1920` to `1948` |
| `rows` | Results per page (max 500) | `50` |
| `start` | Pagination offset | `0` |
| `output_format` | Response format | `json` or `xml` |

### Research Workflow

Follow these steps when a user requests historical research:

**Step 1: Clarify the research scope**

Ask or infer:
- Time period (Ottoman 1517-1917, British Mandate 1917-1948, early statehood 1948-1967, modern 1967-present)
- Geographic focus (specific city, region, or all of Israel)
- Material types wanted (photographs, documents, books, maps, audio)
- Language preference (Hebrew, English, Arabic, Yiddish, Ladino)

**Step 2: Search the NLI API**

Build targeted queries. For best results, combine subject search with material type and date filters:

```
# Historical photographs of Jaffa during British Mandate
query=subject,contains,Jaffa&material_type=images&publication_year_from=1917&publication_year_to=1948

# Hebrew manuscripts about Jerusalem
query=subject,contains,Jerusalem&material_type=manuscripts&language=heb

# David Ben-Gurion's writings
query=creator,contains,Ben Gurion&material_type=books&language=heb
```

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
| National Sound Archive | Music, oral histories, radio broadcasts | `material_type=audio` |
| Manuscripts Institute | Hebrew, Arabic, and other manuscripts | `material_type=manuscripts` |
| Shapell Archive | Ottoman and British Mandate era documents | `subject,contains,Palestine` + date range |
| Press Collections | Historical Hebrew newspapers | `material_type=journals` |

### IIIF Image Access

For visual materials, the NLI provides IIIF (International Image Interoperability Framework) endpoints:

- **Image API:** `https://iiif.nli.org.il/IIIFv21/{identifier}/full/max/0/default.jpg`
- **Manifest API:** `https://iiif.nli.org.il/IIIFv21/MARC/{recordid}/manifest`

Use the manifest to get all available images for a multi-page item (manuscript, book, newspaper).

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

4. **Material type filtering:** The `material_type` parameter is strict. Using `photos` instead of `images` returns zero results. Always use the exact values: `books`, `images`, `manuscripts`, `maps`, `audio`, `videos`, `articles`, `journals`, `rareBooks`.

5. **Cloudflare protection:** The NLI API is protected by Cloudflare. Requests from cloud/datacenter IPs may be blocked. The API works reliably from residential IPs and local development environments. If blocked, the MCP server running locally on the user's machine will work.

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
The API key may be invalid or expired. Get a new free key at https://api2.nli.org.il/signup/. If using the nli-search MCP, it includes a default visitor key.

### IIIF image not loading
Some items have restricted access. Check the `accessRights` field in the search result. Items marked `online_resources_nli` may require NLI library membership for full access.
