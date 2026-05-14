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
| **IDF Archives** | Military service records | https://archives.mod.gov.il/sites/English/Pages/default.aspx | Restricted, family requests possible |
| **Central Zionist Archives** | Aliyah records, Jewish Agency files | http://www.zionistarchives.org.il | Free online catalog |

**Genealogy organizations and family-name databases:**
- **IGRA** (Israel Genealogy Research Association): runs the All Israel Database described above.
- **IGS** (Israel Genealogical Society): a separate membership organization from IGRA, with regional branches, lectures, and research help. The two are distinct, do not confuse them.
- **Beit Hatfutsot / ANU - Museum of the Jewish People**: hosts Jewish family-name and genealogy databases (the former Douglas E. Goldman Jewish Genealogy Center), useful for the meaning and distribution of a surname.

### Research Strategy by Period

#### Ottoman Period Records (pre-1917)

Ottoman-era records are the hardest to find. They are scattered across archives in Istanbul, Jerusalem, and local collections.

**Where to look:**
- NLI: Search for community records, synagogue registers, land documents (kushan/tabu)
- IGRA: Ottoman-era census fragments and tax records
- Sharia court records: The Israel State Archives holds Ottoman and Mandate-era Muslim religious court (sijill) collections for some cities, useful for land transactions and family events even for non-Muslim parties
- Alliance Israelite Universelle: School records for Sephardic communities

**Named record types for this period:**
- Ottoman population registers (defter / nüfus): household-level civil registers kept by the Ottoman administration; surviving volumes are split between the Ottoman archives in Istanbul and local collections
- Ottoman tax and land registers (tapu defter): record property ownership and transfers
- Sephardic community registers (pinkasim): births, marriages, deaths, and burials kept by the kehillah

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
| 1922 and 1931 Palestine censuses | Mandate-wide population counts by locality, religion, and (1931) household | Israel State Archives, IGRA indexes, published volumes |

The 1922 and 1931 censuses of Palestine are the two full Mandate-era censuses; surviving enumeration detail is limited but locality and household summaries help place a family in a town at a known date.

#### Post-1948 Records

Modern Israeli records are held by government ministries and municipalities.

**Where to look:**
- Population Registry (Misrad HaPnim): Birth, death, marriage certificates
- Municipal archives: Property records, business licenses
- Rabbinate: Marriage and divorce records (Jewish citizens)
- Bituach Leumi: Historical insurance records
- IDF: Military service records (restricted)

**How to request:**
- Population Registry records: Submit the current Population Registry request form at the Ministry of Interior (Population and Immigration Authority) with ID proof and relationship documentation. Confirm the exact form on gov.il before sending, since form numbers change.
- Rabbinate records: Contact the relevant city rabbinate with names and approximate dates
- Municipal records: Contact the city historian or archive department

### Cemetery and Gravestone Records

Gravestones (matzevot) are a high-value genealogical source: they typically carry the deceased's Hebrew name, the father's name, the Hebrew death date, and often the town of origin. They are especially useful when civil records are restricted or lost.

**Where to look:**
| Resource | What It Contains | Access |
|----------|-----------------|--------|
| JOWBR (JewishGen Online Worldwide Burial Registry) | Worldwide Jewish burial records, including many Israeli cemeteries; indexed names, dates, and cemetery descriptions | Free, https://www.jewishgen.org/databases/cemetery/ |
| BillionGraves | Crowd-sourced GPS-tagged headstone photos and transcriptions, growing Israeli coverage | Free search, https://billiongraves.com/ |
| Chevra Kadisha cemetery databases | Burial-society plot registers; many large Israeli chevra kadisha bodies (Jerusalem, Tel Aviv area, Haifa) publish online plot lookups | Varies by chevra kadisha; some online, some by phone request |
| JewishGen "Locating Burial Records in Israel" InfoFile | Guide to which Israeli cemetery is indexed where | Free, https://www.jewishgen.org/infofiles/il-burial_records.htm |

**Search tips:**
- A Hebrew death date on a matzevah uses the Hebrew calendar; convert it before cross-referencing civil records
- The father's name on a gravestone often unlocks a generation that civil records do not show
- If a person is missing from JOWBR, try BillionGraves and then the specific city's chevra kadisha directly, since indexing coverage is uneven

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

### Hebrew and Yiddish Name-Variant Methodology

Name matching is the single biggest source of missed records. Work the variants systematically rather than guessing.

**Transliteration patterns (Ashkenazi vs. Sephardi):**
- The same Hebrew letters are romanized differently by community. Ashkenazi pronunciation tends toward "s" for tav (Shabbos, Bais), "oy/ey" for diphthongs, and German-influenced spellings (Schwartz, Mendel). Sephardi/Mizrahi pronunciation keeps "t" for tav, "a" vowels, and Spanish or Arabic influenced spellings.
- Example: the name Yosef appears as Yossef, Joseph, Yoysef, Yusuf depending on community and recording clerk.
- When you know the family's community, predict the spelling the clerk likely used in that archive.

**Daitch-Mokotoff Soundex (D-M Soundex):**
- The genealogy-standard fuzzy-match algorithm, invented in 1985 by Gary Mokotoff and Randy Daitch specifically for Slavic and Yiddish surnames.
- It converts a surname to a 6-digit phonetic code so that names spelled differently but pronounced alike (Moskowitz / Moskovitz / Moskovich) collapse to the same or adjacent codes.
- It is built into IGRA, JewishGen, and the Yad Vashem name database. Use the D-M Soundex option wherever a search form offers it instead of typing manual variants.

**Patronymic-to-surname transitions:**
- Many families had no fixed surname before the 19th century; a person was "X son of Y" (ben/bar). Fixed surnames were often imposed by Austro-Hungarian, Russian, or Ottoman authorities at different dates.
- Expect the same family to appear under a patronymic in older records and a fixed surname in later ones. Track the father's given name as a bridge between the two.

**Yiddish kinui and shem-kodesh pairs:**
- Many people had a paired name: a Hebrew sacred name (shem ha-kodesh, used in religious documents and on the gravestone) and an everyday Yiddish nickname (kinui).
- Standard pairs: Aryeh / Leib, Tzvi / Hirsch, Dov / Ber, Ze'ev / Wolf, Yehuda / Leib, Yaakov / Koppel.
- A civil record may use the kinui while the gravestone uses the shem-kodesh. Always search both halves of a known pair.

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

## Examples

### Example 1: Tracing a Mandate-era immigrant

**User:** "My great-grandfather Moshe Rosenberg came to Palestine from Poland in the 1920s. Where do I start?"

**Walkthrough:**
1. Build the variant set first: Rosenberg / Rozenberg / Rosenburg, and run it through Daitch-Mokotoff Soundex on IGRA so spelling differences collapse automatically.
2. Search IGRA's All Israel Database for the surname plus "Poland" plus the 1920s window, focusing on voter rolls and the Palestine Gazette (naturalization notices).
3. Check the Central Zionist Archives (http://www.zionistarchives.org.il) for a Jewish Agency immigration certificate, which would give origin town and arrival date.
4. Cross-reference the 1931 census summary for the locality he settled in to confirm he was there by then.
5. If he has died, search JOWBR for a burial record; the gravestone's father's name extends the tree one more generation back.

### Example 2: Reading a restricted post-1948 birth record

**User:** "I found a 1955 Israeli birth certificate for my mother but it's in Hebrew handwriting and I want the official copy."

**Walkthrough:**
1. Decode the handwriting using the Hebrew document glossary in this skill's references; focus on the printed field labels (שם האב, מקום לידה) and the numbers first.
2. The Hebrew date may need conversion: subtract roughly 3760 from the Hebrew year, and watch the Tishrei off-by-one.
3. A 1955 birth is under 70 years old, so it is privacy-restricted. The requester must prove a direct family relationship.
4. To get the official copy, submit the current Population Registry request form to the Ministry of Interior (verify the form number on gov.il) with ID and relationship documentation.

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
1. For Population Registry: submit the current Population Registry request form with proof of relationship (verify the form on gov.il first)
2. For IDF records: submit a formal request through the Ministry of Defense archives
3. For rabbinate records: contact the specific rabbinate with a written request
4. For records older than 70 years: they should be publicly accessible

## Recommended MCP Servers

| MCP Server | Why It Helps | Notes |
|------------|--------------|-------|
| `nli-search` (National Library of Israel) | Lets an AI agent query the NLI catalog directly for historical newspapers, photographs, manuscripts, and community records, the primary-source backbone of Israeli genealogy research | Requires a free NLI API key (https://api2.nli.org.il/signup/). Search by town name and date range, for example `query=subject,contains,{town}&publication_year_to=1917`. |

Other archives (IGRA, State Archives, Central Zionist Archives) do not currently expose an MCP server; use their web search interfaces directly.

## Reference Links

| Source | URL |
|--------|-----|
| IGRA (Israel Genealogy Research Association) | https://genealogy.org.il/AID/ |
| JewishGen | https://www.jewishgen.org/ |
| National Library of Israel | https://www.nli.org.il/ |
| Israel State Archives | https://www.archives.gov.il/ |
| Central Zionist Archives | http://www.zionistarchives.org.il |
| IDF and Defense Establishment Archives | https://archives.mod.gov.il/sites/English/Pages/default.aspx |
| JOWBR (JewishGen Online Worldwide Burial Registry) | https://www.jewishgen.org/databases/cemetery/ |
