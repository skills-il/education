# NLI OpenLibrary API Reference

## Base URL

```
https://api.nli.org.il/openlibrary/search
```

## Authentication

All requests require an `api_key` query parameter.

- Free signup: https://api2.nli.org.il/signup/
- The `nli-search` MCP server may include a visitor key (verify with the MCP)

## Query Format

The `query` parameter uses structured format: `field,operator,value`

### Supported Fields (query attributes)

Language and date filtering are query CLAUSES (attributes inside `query`), NOT standalone parameters.

| Field | Description |
|-------|-------------|
| `subject` | Subject headings (topical, geographic, personal) |
| `creator` | Author, photographer, artist, or creator |
| `title` | Title of the work |
| `publisher` | Publishing body or institution |
| `language` | Content language, e.g. `language,exact,eng` |
| `start_date` / `end_date` | Date filter, e.g. `start_date,contains,1951` (format `yyyyMMdd` or `yyyy`) |
| `system_number` | Exact NLI system number, e.g. `system_number,exact,990023677080205171` |
| `shelfmark` | Physical shelfmark |

### Operators

| Operator | Description |
|----------|-------------|
| `contains` | Partial match (most common) |
| `exact` | Exact match |

### Combining clauses

A single `query` parameter can hold several `field,operator,value` clauses. Join them with a semicolon plus an explicit connector appended to the clause it follows: `,AND;` or `,OR;`. The last clause carries no trailing connector.

```
query=field,operator,value,AND;field,operator,value
```

```
# title is exactly "jerusalem" AND creator contains "American Colony" AND language is exactly English
query=title,exact,jerusalem,AND;creator,contains,American Colony,AND;language,exact,eng
```

Use `,AND;` to narrow results and `,OR;` to broaden them. The delimiter between the `query` and the standalone filters/commands below is `&`.

### Standalone filters

Appended outside the `query` with `&`.

| Parameter | Values |
|-----------|--------|
| `material_type` | `books`, `journals`, `images`, `audio_video`, `scores`, `maps`, `archives`, `sheets`, `dissertations`, `manuscripts`, `media`, `databases`, `NEWSPAPER`, `Identity` |
| `availability_type` | `online_access`, `all_items`, `online_and_api_access`, `online_access_no_api`, `online_in_library_only`, `no_online_access` |

There is no `audio`, `videos`, `articles`, `rareBooks`, `publication_year_from`, or `publication_year_to`. Unknown parameters are silently ignored (the request returns unfiltered results with an `Errors` response header listing the skipped condition).

### Commands

| Parameter | Values |
|-----------|--------|
| `sort_field` | `title`, `creator`, `date_desc`, `date_asc` |
| `items_per_page` | a number in the range 1-50 |
| `result_page` | page number (total items / 50) |
| `output_format` | `json` (default), `xml` |
| `count_mode` | `true`, `false` (return only a match count) |

## Response Format

Results are JSON-LD using Dublin Core elements:

The `@id` value is the item's permalink. The modern form is `https://www.nli.org.il/<lang>/<type>/NNL_ALEPH<system-number>` (for example, illustratively: `https://www.nli.org.il/en/books/NNL_ALEPH990012345670205171/NLI`). Treat the digits as a placeholder and use the actual `@id` returned for each result rather than constructing the URL yourself.

```json
{
  "@id": "https://www.nli.org.il/en/books/NNL_ALEPH990012345670205171/NLI",
  "http://purl.org/dc/elements/1.1/title": [{"@value": "Title text"}],
  "http://purl.org/dc/elements/1.1/creator": [{"@value": "Author name"}],
  "http://purl.org/dc/elements/1.1/date": [{"@value": "YYYYMMDD"}],
  "http://purl.org/dc/elements/1.1/type": [{"@value": "book"}],
  "http://purl.org/dc/elements/1.1/language": [{"@value": "heb"}],
  "http://purl.org/dc/elements/1.1/recordid": [{"@value": "997..."}],
  "http://purl.org/dc/elements/1.1/source": [{"@value": "The National Library of Israel"}],
  "http://purl.org/dc/elements/1.1/linkToMarc": [{"@id": "https://iiif.nli.org.il/IIIFv21/marc/bib/997..."}]
}
```

## IIIF Endpoints

### Single Image

```
https://iiif.nli.org.il/IIIFv21/{identifier}/full/max/0/default.jpg
```

### Manifest / linkToMarc (multi-page items)

```
https://iiif.nli.org.il/IIIFv21/marc/bib/{docid}
```

Use lowercase `marc/bib`. Prefer the `linkToMarc` / `@id` value returned in each result over hand-building this URL.

## Example Queries

```bash
# British Mandate photographs (date as a clause, type as a filter)
curl "https://api.nli.org.il/openlibrary/search?api_key=YOUR_KEY&query=subject,contains,Palestine,AND;start_date,contains,1920&material_type=images&items_per_page=10&output_format=json"

# Hebrew manuscripts about Kabbalah (language as a clause)
curl "https://api.nli.org.il/openlibrary/search?api_key=YOUR_KEY&query=subject,contains,Kabbalah,AND;language,exact,heb&material_type=manuscripts&items_per_page=20&output_format=json"

# Maps of Jerusalem, sorted by title
curl "https://api.nli.org.il/openlibrary/search?api_key=YOUR_KEY&query=subject,contains,Jerusalem&material_type=maps&items_per_page=10&sort_field=title&output_format=json"
```

## Rate Limits

The API uses standard rate limiting. The free tier allows reasonable research usage. Heavy automated scraping may be throttled.
