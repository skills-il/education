# NLI OpenLibrary API Reference

## Base URL

```
https://api.nli.org.il/openlibrary/search
```

## Authentication

All requests require an `api_key` query parameter.

- Free signup: https://api2.nli.org.il/signup/
- The `nli-search` MCP server includes a default visitor key

## Query Format

The `query` parameter uses structured format: `field,operator,value`

### Supported Fields

| Field | Description |
|-------|-------------|
| `subject` | Subject headings (topical, geographic, personal) |
| `creator` | Author, photographer, artist, or creator |
| `title` | Title of the work |
| `publisher` | Publishing body or institution |
| `contributor` | Contributors other than primary creator |
| `isbn` | International Standard Book Number |
| `issn` | International Standard Serial Number |
| `collection` | NLI collection name |

### Operators

| Operator | Description |
|----------|-------------|
| `contains` | Partial match (most common) |
| `exact` | Exact match |

### Filter Parameters

| Parameter | Values |
|-----------|--------|
| `material_type` | `books`, `images`, `manuscripts`, `maps`, `audio`, `videos`, `articles`, `journals`, `rareBooks` |
| `language` | ISO 639-3 codes: `heb`, `eng`, `ara`, `yid`, `lad`, `fre`, `ger`, `rus` |
| `publication_year_from` | Year (YYYY) |
| `publication_year_to` | Year (YYYY) |
| `availability_type` | Filter by access level |
| `start_date` | Start date filter |
| `end_date` | End date filter |

### Pagination

| Parameter | Default | Max |
|-----------|---------|-----|
| `rows` | 10 | 500 |
| `start` | 0 | -- |

### Output

| Parameter | Values |
|-----------|--------|
| `output_format` | `json` (default), `xml` |

### Faceting

| Parameter | Description |
|-----------|-------------|
| `facet.field` | Field to facet on |
| `facet.limit` | Max facet values |
| `facet.offset` | Facet pagination offset |
| `facet.sort` | Facet sort order |

## Response Format

Results are JSON-LD using Dublin Core elements:

```json
{
  "@id": "https://www.nli.org.il/en/books/NNL_ALEPH...",
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

### Manifest (multi-page items)

```
https://iiif.nli.org.il/IIIFv21/MARC/{recordid}/manifest
```

## Example Queries

```bash
# British Mandate photographs
curl "https://api.nli.org.il/openlibrary/search?query=subject,contains,Palestine&material_type=images&publication_year_from=1920&publication_year_to=1948&rows=10&output_format=json&api_key=YOUR_KEY"

# Hebrew manuscripts about Kabbalah
curl "https://api.nli.org.il/openlibrary/search?query=subject,contains,Kabbalah&material_type=manuscripts&language=heb&rows=20&output_format=json&api_key=YOUR_KEY"

# Maps of Jerusalem
curl "https://api.nli.org.il/openlibrary/search?query=subject,contains,Jerusalem&material_type=maps&rows=10&output_format=json&api_key=YOUR_KEY"
```

## Rate Limits

The API uses standard rate limiting. The free tier allows reasonable research usage. Heavy automated scraping may be throttled.
