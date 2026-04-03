---
name: israeli-genealogy-researcher
description: "Guide family history research using Israeli and Jewish genealogical data sources. Use when a user asks about tracing Israeli or Jewish roots, finding family records, researching ancestors who lived in Ottoman Palestine, British Mandate Palestine, or modern Israel, decoding Hebrew-language historical documents, or building a family tree from Israeli records. Produces structured research plans, explains how to navigate IGRA, JewishGen, NLI archives, and municipal record systems, and helps decode Hebrew handwriting in historical certificates. Prevents dead-end research by matching the right data source to each genealogical question. Do NOT use for Yad Vashem Holocaust victim name searches specifically (use dedicated Holocaust research tools), DNA ancestry interpretation, or non-Israeli genealogy research."
license: MIT
---

# Israeli Genealogy Researcher

## Problem

Tracing family roots through Israeli records is uniquely challenging. Records span Ottoman Turkish, British English, Hebrew, Arabic, and Yiddish across multiple unconnected archives. Date systems shift between Hebrew calendar, Islamic calendar, and Gregorian dates. Names change across transliteration systems (Sephardic vs. Ashkenazi spelling, Hebrew vs. Latin script). Without knowing which archive holds which records and how to query each one, researchers hit dead ends quickly and miss critical connections between documents.

## Instructions

### Overview

This skill helps users research family history using Israeli and Jewish genealogical data sources. It covers the major archives, explains record types, guides search strategies, and helps decode Hebrew-language historical documents.

### When to Use

- User wants to trace family roots to Israel/Palestine
- User has a family name and wants to find records
- User found a Hebrew document (birth/marriage/death certificate) and needs help reading it
- User wants to research a specific community or town in Israel
- User is planning a genealogy research trip to Israel
- User needs to navigate Israeli municipal or religious record systems

### Key Data Sources

| Source | What It Contains | URL | Access |
|--------|-----------------|-----|--------|
| **IGRA** (Israel Genealogy Research Association) | 3.9M+ records: birth, marriage, death, immigration, voter rolls | https://genealogy.org.il/AID/ | Free search, membership for full access |
| **JewishGen** | Global Jewish genealogy hub, community databases, Yizkor books | https://www.jewishgen.org/ | Free registration |
| **NLI Archives** (via nli-search MCP) | Historical documents, manuscripts, photographs, newspapers | https://www.nli.org.il/ | Free API (key required) |
| **Israel State Archives** | Government records, immigration files, land documents | https://www.archives.gov.il/ | Free online access to digitized materials |
| **Rabbinate Records** | Marriage and divorce records (from 1948) | Via local rabbinate offices | In-person or authorized request |
| **Population Registry** | Birth, death, marriage records (from 1948) | Via Ministry of Interior | Official request with ID |
| **Municipal Archives** | Local records, property tax (arnona), building permits | Via city/town hall | Varies by municipality |
| **IDF Archives** | Military service records | https://www.archives.mod.gov.il/ | Restricted, family requests possible |
| **Central Zionist Archives** | Aliyah records, Jewish Agency files | https://www.czarchives.org.il/ | Free online catalog |

### Research Strategy by Period

#### Ottoman Period Records (pre-1917)

Ottoman-era records are the hardest to find. They are scattered across archives in Istanbul, Jerusalem, and local collections.

**Where to look:**
- NLI: Search for community records, synagogue registers, land documents (kushan/tabu)
- IGRA: Ottoman-era census fragments and tax records
- Sharia court records: Available at the Israel State Archives for some cities
- Alliance Israelite Universelle: School records for Sephardic communities

**Search tips:**
- Names were often recorded in Arabic or Ottoman Turkish transliteration
- Use the NLI API: `query=subject,contains,{town name}&publication_year_to=1917`
- Check Sephardic community registers (pinkasim)

#### British Mandate Records (1917-1948)

The richest period for genealogical records due to British administrative systems.

**Where to look:**
- IGRA: Palestine Gazette (official government notices), voter rolls, professional registers
- Israel State Archives: Immigration records, land purchase files, census data
- Central Zionist Archives: Jewish Agency immigration files, kibbutz records
- NLI: Newspapers (search announcements, obituaries)

**Key record types:**
| Record | What It Shows | Where to Find |
|--------|--------------|---------------|
| Palestine Gazette | Official appointments, company registrations, naturalization | IGRA |
| Immigration certificates | Name, origin, date of arrival | Central Zionist Archives |
| Voter rolls | Name, address, occupation | IGRA, Israel State Archives |
| Land records | Property ownership, purchase details | Israel Land Authority (Tabu) |
| School records | Student lists, parents' names | Local school archives, NLI |

#### Post-1948 Records

Modern Israeli records are held by government ministries and municipalities.

**Where to look:**
- Population Registry (Misrad HaPnim): Birth, death, marriage certificates
- Municipal archives: Property records, business licenses
- Rabbinate: Marriage and divorce records (Jewish citizens)
- Bituach Leumi: Historical insurance records
- IDF: Military service records (restricted)

**How to request:**
- Population Registry records: Submit Form 1404 at the Ministry of Interior with ID proof and relationship documentation
- Rabbinate records: Contact the relevant city rabbinate with names and approximate dates
- Municipal records: Contact the city historian or archive department

### Decoding Hebrew Documents

Israeli historical documents often contain:

**Hebrew Calendar Dates:**
- Hebrew year format: `ה'תשי"ח` = 5718 = 1957/1958 CE
- Conversion: Subtract 3760 from the Hebrew year (approximate; depends on month)
- Months: Tishrei (Sep/Oct), Cheshvan, Kislev, Tevet, Shevat, Adar, Nisan (Mar/Apr), Iyar, Sivan, Tammuz, Av, Elul

**Common Document Fields (birth certificate):**
| Hebrew | Translation | Notes |
|--------|-------------|-------|
| שם פרטי | First name | |
| שם משפחה | Family name | |
| תאריך לידה | Date of birth | May be Hebrew or Gregorian |
| מקום לידה | Place of birth | |
| שם האב | Father's name | |
| שם האם | Mother's name | Often includes maiden name |
| מספר זהות | ID number | 9 digits, post-1948 |

**Common Document Fields (marriage certificate):**
| Hebrew | Translation |
|--------|-------------|
| חתן | Groom |
| כלה | Bride |
| עדים | Witnesses |
| מסדר הקידושין | Officiating rabbi |
| תאריך הנישואין | Marriage date |
| כתובה | Ketubah (marriage contract) |

**Name Variations:**
Israeli records may show different name forms:
- Hebrew name: `אברהם בן יצחק` (Avraham son of Yitzhak)
- Legal name: `אברהם כהן` (Avraham Cohen)
- Diaspora name: `Abraham Kohn` (German variant)
- Immigration name: name may have been changed at arrival

### Building a Research Plan

When a user asks to research their family, follow this template:

```markdown
## Family Research Plan: [Family Name]

### Known Information
- [List what the user already knows: names, dates, locations, documents]

### Research Goals
1. [Specific goal: Find great-grandparents' immigration record]
2. [Specific goal: Locate marriage certificate]
3. [Specific goal: Identify town of origin]

### Search Strategy

#### Step 1: Start with IGRA
- Search the All Israel Database for [surname] variations
- Check: [specific record types likely to contain this family]

#### Step 2: Check NLI Archives
- Search for [community/town] records in NLI
- Look for: [newspapers, community registers, photographs]

#### Step 3: State Archives
- Check immigration records for [time period]
- Look for: [specific document types]

#### Step 4: Municipal Records
- Contact [city] municipal archive for [record type]

### Expected Timeline
- Online searches: immediate
- Archive requests: 2-4 weeks for responses
- In-person visits: schedule via archive websites

### Tips for This Family
- [Specific advice based on the family's background]
```

## Bundled Resources

See the `references/` directory for:
- `data-sources-guide.md` -- detailed guide to each Israeli genealogical data source with direct URLs
- `hebrew-document-glossary.md` -- common Hebrew terms in civil and religious documents

## Gotchas

1. **Name transliteration chaos:** The same person may appear as "Moshe", "Moses", "Mosche", "Musa" across different records. Always search multiple spelling variants. IGRA supports fuzzy matching; the NLI API does not.

2. **Hebrew calendar off-by-one errors:** The Hebrew year starts in Tishrei (September/October), so a Hebrew date in Tishrei-Kislev could map to two different Gregorian years. Always verify with a Hebrew-Gregorian date converter.

3. **Assuming records are centralized:** There is no single Israeli genealogy database. Records are split across IGRA, State Archives, NLI, rabbinate offices, municipal archives, and dozens of smaller collections. Each has different access methods.

4. **Privacy restrictions on recent records:** Israeli privacy law restricts access to vital records less than 70 years old (births) or 50 years old (marriages/deaths) unless the requester can prove a direct family relationship. Don't assume all records are publicly searchable.

5. **Confusing kibbutz records:** Kibbutz members often appear in kibbutz internal records (pinkas) rather than municipal records. For kibbutz families, contact the kibbutz archive directly or check the Central Zionist Archives.

## Troubleshooting

### "I can't find anyone with my surname in IGRA"
Try:
1. Alternate spellings (Cohen/Kohn/Kohen, Levy/Levi/Lewi)
2. Remove diacritics and try partial matches
3. Search by first name + location instead of surname
4. Check if the family changed their name upon immigration (Hebraization was common)

### "I found a Hebrew document but can't read the handwriting"
1. Use the NLI's digitized handwriting guides for common document types
2. Focus on numbers (dates, ID numbers) first, as they're easier to read
3. Look for printed headers/stamps that identify the document type
4. Compare against the Hebrew document glossary in this skill's references

### "The records I need are restricted"
1. For Population Registry: submit Form 1404 with proof of relationship
2. For IDF records: submit a formal request through the Ministry of Defense archives
3. For rabbinate records: contact the specific rabbinate with a written request
4. For records older than 70 years: they should be publicly accessible
