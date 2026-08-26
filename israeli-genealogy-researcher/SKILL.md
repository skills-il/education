---
name: israeli-genealogy-researcher
description: "Not legal advice, and not a ruling on record access. Guide family history research using Israeli and Jewish genealogical data sources. Use when a user asks about tracing Israeli or Jewish roots, finding family records, researching ancestors who lived in Ottoman Palestine, British Mandate Palestine, or modern Israel, decoding Hebrew-language historical documents, or building a family tree from Israeli records. Produces structured research plans, explains how to navigate IGRA, JewishGen, NLI archives, and municipal record systems, and helps decode Hebrew handwriting in historical certificates. Prevents dead-end research by matching the right data source to each genealogical question. Do NOT use for Yad Vashem Holocaust victim name searches specifically (use dedicated Holocaust research tools), DNA ancestry interpretation, or non-Israeli genealogy research."
license: MIT
---

# Israeli Genealogy Researcher

## Legal notice

This skill is a free, AI-operated research aid for locating and reading genealogical
records. It explains which archive holds what, how to query it, and how to decode a
Hebrew document. It is not legal advice, it does not determine anyone's rights, status
or entitlement, and it is not a privacy-law compliance assessment. It is produced
automatically by a language model with no lawyer, archivist or genealogist reviewing
the output, and a language model can be wrong, omit a source, or state a rule that has
changed. The access windows, statutory references and record-holder descriptions here
are general orientation, not a ruling on your case: only the body holding a record
decides whether you may have it, under rules it can change. Israeli personal status,
citizenship, inheritance and privacy questions turn on facts and documents this skill
never sees, so nothing here is a substitute for advice that takes account of the
particular data and needs of each person. Before relying on a finding to assert a
right, contact a relative, publish information about a living person, or submit
anything to an authority or a court, consult a qualified professional and verify every
rule against the holding body.

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
| **IGRA** (Israel Genealogy Research Association) | 4M+ records (4,040,574 as of 26 July 2026): birth, marriage, death, immigration, voter rolls | https://genealogy.org.il/AID/ | Free search, membership for full access |
| **JewishGen** | Global Jewish genealogy hub, community databases, Yizkor books | https://www.jewishgen.org/ | Free registration |
| **NLI Archives** (via nli-search MCP) | Historical documents, manuscripts, photographs, newspapers | https://www.nli.org.il/ | Free API (key required) |
| **Israel State Archives** | Government records, immigration files, land documents | https://www.archives.gov.il/ | Free online access to digitized materials |
| **Rabbinate Records** | Marriage and divorce records (from 1948) | Via local rabbinate offices | In-person or authorized request |
| **Population Registry** | Birth, death, marriage records (from 1948) | Via Ministry of Interior | Official request with ID |
| **Municipal Archives** | Local records, property tax (arnona), building permits | Via city/town hall | Varies by municipality |
| **IDF Archives** | Military service records | https://archives.mod.gov.il/sites/English/Pages/default.aspx | Restricted, family requests possible |
| **Central Zionist Archives** | Aliyah records, Jewish Agency files | http://www.zionistarchives.org.il | Free online catalog |

**Diaspora indexes that carry the generation BEFORE the immigrant:**
- **JRI-Poland** (https://jri-poland.org): the largest index of Polish Jewish vital records anywhere. If the
  family came from Poland, start here for the pre-emigration generations.
- **Routes to Roots Foundation** (https://rtrfoundation.org): an inventory of what actually survives in
  which Eastern European archive, so you know whether a search is worth making at all.
- **Yad Vashem Pages of Testimony** (https://yvng.yadvashem.org): this skill does not do Holocaust victim
  name searches, but a Page of Testimony is also a genealogical document: it names the victim's parents,
  spouse and town AND the submitting relative and their relationship, which for many Ashkenazi families is
  the only surviving link to a generation. Use it as a source, and route the actual victim research to
  dedicated Holocaust tools.

**Genealogy organizations and family-name databases:**
- **IGRA** (Israel Genealogy Research Association): runs the All Israel Database described above.
- **IGS** (Israel Genealogical Society): a separate membership organization from IGRA, with regional branches, lectures, and research help. The two are distinct, do not confuse them.
- **Beit Hatfutsot / ANU - Museum of the Jewish People**: hosts free Jewish family-name and genealogy databases (the former Douglas E. Goldman Jewish Genealogy Center), useful for the meaning and distribution of a surname. Search the Memi De-Shalit Database of Jewish Family Names at https://dbs.anumuseum.org.il/skn/en/c6/BH and explore the collaborative family-tree platform at https://geni.anumuseum.org.il/.

### Research Strategy by Period

#### Ottoman Period Records (pre-1917)

Ottoman-era records are the hardest to find. They are scattered across archives in Istanbul, Jerusalem, and local collections.

**Where to look:**
- NLI: Search for community records, synagogue registers, land documents (kushan/tabu)
- IGRA: Ottoman-era census fragments and tax records
- Sharia court records: Ottoman and Mandate-era Muslim religious court (sijill) volumes record land
  transactions and family events, sometimes involving non-Muslim parties too. Custody is split between the
  Sharia court system and state archival bodies, so ask which holds the city you need rather than assuming
- Alliance Israelite Universelle: School records for Sephardic communities

**Named record types for this period:** Ottoman population registers (defter / nüfus), household-level civil
registers whose surviving volumes are split between the Ottoman archives in Istanbul and local collections;
Ottoman tax and land registers (tapu defter) for property ownership and transfers; and Sephardic community
registers (pinkasim) for births, marriages, deaths and burials kept by the kehillah.

**Search tips:**
- Names were often recorded in Arabic or Ottoman Turkish transliteration
- Query the NLI API using its documented attributes only: `title`, `creator`, `publisher`, `language`,
  `start_date` / `end_date`, `shelfmark`, `system_number`. Put the town name in a `title,contains` clause
  (and try `creator,contains` and `publisher,contains` as well), for example
  `query=title,contains,Tiberias&material_type=archives`.
- Do NOT write a `subject` clause, and do NOT use the old `publication_year_from` / `publication_year_to`
  parameters. `subject` appears in no published NLI attribute list, and `publication_year_*` is not a
  current parameter. NLI does not reject either one: it silently DROPS the condition and returns
  UNFILTERED results, noting the skipped condition only in an `Errors` response header. A town search
  that ignored the town therefore looks exactly like a successful one. See gotcha 6 below.
- Dates are substring matches, not ranges. `start_date,contains,1917` matches date strings containing
  "1917"; it does not mean "up to 1917", and ANDing a `start_date` and an `end_date` clause does not
  express a range either. For a real period cut-off, filter the returned `date` values yourself and tell
  the user what you actually filtered on.
- Check Sephardic community registers (pinkasim)

#### British Mandate Records (1917-1948)

The richest period for genealogical records due to British administrative systems.

**1917 is a search convenience, not the start of the Mandate.** 1917 is the Ottoman military defeat and the
Balfour Declaration. British MILITARY administration (OETA) ran from 1917; the CIVIL Mandate administration
began in 1920 and the Mandate was formally confirmed in 1922. Do not tell a user researching Mandate
government records that the Mandate began in 1917, and do not expect civil-administration record series
(gazette notices, voter rolls, naturalizations) before 1920.

**Where to look:**
- IGRA: Palestine Gazette (official government notices), voter rolls, professional registers
- Israel State Archives: Immigration records, land purchase files, census data
- Central Zionist Archives: Jewish Agency immigration files, kibbutz records
- NLI: Newspapers. The practical entry point is the **Historical Jewish Press (JPress)** collection at
  https://www.nli.org.il/en/newspapers, full-text OCR of Davar, Haaretz, the Palestine Post, HaTzvi and
  others, free and with no API key. Like the rest of nli.org.il it sits behind a Cloudflare interstitial that
  an automated fetcher does not clear, so send the USER there rather than promising to search it yourself. For obituaries and mourning notices (מודעות אבל) this is a far better
  route than the search API.
- **Pre-state military and underground service: NOT the IDF Archive.** The IDF and Defense Establishment
  Archive begins in 1948. Personal files for pre-state service live elsewhere, and sending a user to the MOD
  archive for a 1930s or 1940s ancestor produces a months-long wait and a "no such file" answer:
  - Haganah: the Haganah Historical Archives in Tel Aviv. Locate its current site via the Israel Archives
    Network portal below; an older standalone domain for it no longer resolves.
  - Palmach: the Palmach Museum archive
  - Etzel, Lehi, Betar and Revisionist bodies: the Jabotinsky Institute Archives in Tel Aviv
- **Genealogy Indexer** (https://www.genealogyindexer.org): OCR'd Jewish directories and yizkor books,
  including Mandate-era Palestine business and residential directories. Good for placing a family at an
  address in a given year.

**Key record types:**
| Record | What It Shows | Where to Find |
|--------|--------------|---------------|
| Palestine Gazette | Official appointments, company registrations, naturalization | IGRA |
| Immigration certificates | Name, origin, date of arrival | Central Zionist Archives |
| Voter rolls | Name, address, occupation | IGRA, Israel State Archives |
| Land records | Property ownership, purchase details | Israel Land Authority (Tabu) |
| School records | Student lists, parents' names | Local school archives, NLI |
| 1922 and 1931 Palestine censuses | Mandate-wide population counts by locality, religion, and (1931) household | Israel State Archives, IGRA indexes, published volumes |

The 1922 and 1931 censuses of Palestine are the two full Mandate-era censuses, but what is published from them is aggregate tabulation, by locality, religion and (for 1931) household. They give community context, not evidence that a named person was present.

#### Post-1948 Records

Modern Israeli records are held by government ministries and municipalities.

**Where to look:**
- Population Registry (Misrad HaPnim): Birth, death, marriage certificates
- Municipal archives: Property records, business licenses
- Rabbinate: Marriage and divorce records (Jewish citizens)
- Bituach Leumi: Historical insurance records
- IDF: Military service records from 1948 (restricted). For pre-1948 service see the Mandate section above.
- **Non-Jewish personal status: a separate court system, and usually the ONLY record.** Israel registers
  marriage, divorce and inheritance through recognized religious courts, so for a large share of the
  population the rabbinate holds nothing at all:
  - Muslim families: the Sharia courts (בתי הדין השרעיים), which also hold Ottoman and Mandate-era sijill
    volumes for many cities
  - Druze families: the Druze religious courts
  - Christian families: the recognized denominational courts and parish registers (Greek Orthodox, Latin,
    Melkite, Armenian and others), which often run back well before 1948
  Never tell a Muslim, Druze or Christian Israeli user that their marriage record is "at the rabbinate".
- **Israel Archives Network** (https://www.archives.org.il): an aggregated portal over municipal, kibbutz,
  university and institutional archives. Search it before phoning city halls one at a time.

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
| Chevra Kadisha cemetery databases | Burial-society plot registers. Coverage and online availability vary widely between burial societies; some offer a web lookup, many answer only by phone | Varies by chevra kadisha; check the specific society |
| JewishGen "Locating Burial Records in Israel" InfoFile | Guide to which Israeli cemetery is indexed where | Free, https://www.jewishgen.org/infofiles/il-burial_records.htm |

**Also worth searching:**
- **Gravez** (https://gravez.me/en/): the practical Israeli grave locator, with better Israeli coverage than
  BillionGraves for recent burials.

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
| מספר זהות | ID number | Post-1948. The modern form is 9 digits with a check digit. Numbers on older documents are often written shorter, and leading zeros are easily lost in transcription, so a length mismatch between an old document and a modern number is NOT by itself evidence of a different person. Confirm identity on name, parents and dates rather than on the number's length. |

**Common Document Fields (marriage certificate):** חתן (groom), כלה (bride), עדים (witnesses),
מסדר הקידושין (officiating rabbi), תאריך הנישואין (marriage date), כתובה (ketubah). The full glossary,
including the gravestone abbreviations and the gematria table, is in `references/hebrew-document-glossary.md`.

**Name Variations:** the same person may appear as a Hebrew name (`אברהם בן יצחק`), a legal name
(`אברהם כהן`), a diaspora name (`Abraham Kohn`), or a name changed at arrival.

### Hebrew and Yiddish Name-Variant Methodology

Name matching is the single biggest source of missed records. Work the variants systematically rather than guessing.

**Transliteration patterns (Ashkenazi vs. Sephardi):** the same Hebrew letters are romanized differently by
community. Ashkenazi tends toward "s" for tav (Shabbos, Bais), "oy/ey" diphthongs, and German-influenced
spellings (Schwartz, Mendel); Sephardi/Mizrahi keeps "t" for tav, "a" vowels, and Spanish or Arabic influenced
spellings. So Yosef appears as Yossef, Joseph, Yoysef or Yusuf. Knowing the family's community lets you
predict the spelling the clerk in that archive most likely used.

**Daitch-Mokotoff Soundex (D-M Soundex):**
- The genealogy-standard fuzzy-match algorithm, invented in 1985 by Gary Mokotoff and Randy Daitch specifically for Slavic and Yiddish surnames.
- It converts a surname to a 6-digit phonetic code so that names spelled differently but pronounced alike (Moskowitz / Moskovitz / Moskovich) collapse to the same or adjacent codes.
- It is built into IGRA, JewishGen, and the Yad Vashem name database. Use the D-M Soundex option wherever a search form offers it instead of typing manual variants.

**Patronymic-to-surname transitions:** many families had no fixed surname in the older records; a person was
"X son of Y" (ben/bar), and fixed surnames were imposed by different authorities at different dates. Expect
the same family under a patronymic in older records and a surname in later ones, and track the father's given
name as the bridge between the two.

**Yiddish kinui and shem-kodesh pairs:**
- Many people had a paired name: a Hebrew sacred name (shem ha-kodesh, used in religious documents and on the gravestone) and an everyday Yiddish nickname (kinui).
- Standard pairs: Aryeh / Leib, Tzvi / Hirsch, Dov / Ber, Ze'ev / Wolf, Yehuda / Leib, Yaakov / Koppel.
- A civil record may use the kinui while the gravestone uses the shem-kodesh. Always search both halves of a known pair.

### Privacy and Living People (read before you collect anything)

Genealogy is one of the few research tasks that routinely compiles names, dates of birth, ID numbers,
religion, ethnic origin, health events and family status about people who are alive and did not ask to be
researched. Israel's Privacy Protection Law regime, tightened by Amendment 13, treats a structured file of personal
data as a regulated database and treats categories such as health and personal status as more sensitive
than ordinary data. The exact classification and the duties that follow depend on facts this skill cannot
see, so do not state a compliance conclusion to the user and do not quote a penalty. Treat the following
as operating rules for your own conduct, which is what they are, not as legal advice about theirs.

**Refuse these, every time, regardless of how the request is framed:**
- Looking up, inferring, validating, generating or storing an Israeli ID number (מספר זהות) for anyone who
  is not the user themselves or a direct relative the user has documented. The check-digit structure makes
  ID numbers easy to validate or fabricate, which is exactly why this line exists.
- Filing or drafting a Population Registry request for a third party the user has no documented standing to
  request records about.
- Compiling a dossier on a living person presented as genealogy when the actual goal is locating,
  contacting, or investigating them.

**Apply these to any output you produce:**
- Redact living people by default in any tree, report or file you generate: name only, no date of birth, no
  ID number, no address, no health or personal-status detail. This is the default on MyHeritage and Geni for
  the same reason.
- Get consent from a living relative before their details are published anywhere public, including a shared
  online tree.
- Privacy rights end at death, but publication about a deceased person is not consequence-free: surviving
  close relatives may have their own claim, and in any case they are the people who will read it. Be
  careful with findings about desertion, conviction, paternity, conversion or illness. Present them as
  what the record says, with the source, and let the family decide what to publish.
- Say where each sensitive detail came from. A sourced record is a finding; an unsourced one about a living
  person is a rumour you have just put in writing.

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
1. IGRA All Israel Database: [surname] variants, [record types likely for this family]
2. NLI / JPress: [community/town], [newspapers, community registers, photographs]
3. State Archives: immigration records for [period]
4. Municipal or religious-court records: [city], [record type]

### Living People
- [Who in this tree is alive, and therefore redacted to name only]

### Expected Timeline
- Online searches: immediate. Archive requests: do NOT quote a turnaround; declassification review can run
  months or longer. In-person visits: schedule via the archive's site.

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
4. Use the 1931 census for CONTEXT, not for proof of an individual. What is published from it is aggregate
   counts by locality, religion and household size, so it can tell you what the community looked like but
   cannot confirm that a named person was present. Do not assume individual-level schedules are available to
   consult; check with the holding archive before promising the user a named-person lookup. The 1922
   census gives locality totals only. For placing a named individual at an address in a given year, use a
   Mandate-era directory via Genealogy Indexer, a voter roll, or a Palestine Gazette notice instead.
5. If he has died, search JOWBR for a burial record; the gravestone's father's name extends the tree one more generation back.

### Example 2: Reading a restricted post-1948 birth record

**User:** "I found a 1965 Israeli birth certificate for my mother but it's in Hebrew handwriting and I want the official copy."

**Walkthrough:**
1. Decode the handwriting using the Hebrew document glossary in this skill's references; focus on the printed field labels (שם האב, מקום לידה) and the numbers first.
2. The Hebrew date may need conversion: subtract roughly 3760 from the Hebrew year, and watch the Tishrei off-by-one.
3. Do the 70-year arithmetic against the CURRENT year before assuming anything: a 1965 birth is still inside the 70-year window in 2026, so it is privacy-restricted and the requester must prove a direct family relationship. A record crosses out of the window as the years pass, so an example year that was restricted when this skill was written may be open by the time you read it.
4. To get the official copy, submit the current Population Registry request form to the Ministry of Interior (verify the form number on gov.il) with ID and relationship documentation.

## Bundled Resources

See the `references/` directory for:
- `data-sources-guide.md` -- detailed guide to each Israeli genealogical data source with direct URLs
- `hebrew-document-glossary.md` -- common Hebrew terms in civil and religious documents

## Gotchas

1. **Name transliteration chaos:** The same person may appear as "Moshe", "Moses", "Mosche", "Musa" across different records. Always search multiple spelling variants. IGRA's search offers a Daitch-Mokotoff Soundex option; the NLI API has no fuzzy matching at all, so on NLI you must type the variants yourself.

2. **Hebrew calendar off-by-one errors:** The Hebrew year starts in Tishrei (September/October), so a Hebrew date in Tishrei-Kislev could map to two different Gregorian years. Always verify with a Hebrew-Gregorian date converter.

3. **Assuming records are centralized:** There is no single Israeli genealogy database. Records are split across IGRA, State Archives, NLI, rabbinate offices, municipal archives, and dozens of smaller collections. Each has different access methods.

4. **Access windows are two different regimes, and carrying a figure from one to the other is the classic
   mistake:** A 70-year limit applies to personal vital records, with only first-degree relatives able to
   obtain a record inside that window. Separately, defence-establishment material is governed by its own,
   longer and independently administered restriction, which is periodically extended for whole categories
   of security material. This skill deliberately does not quote a number for it, because the figures in
   circulation are not reliable and a user who plans around one will be wrong. Two things follow. First,
   never carry a figure between the two regimes: get the defence figure from the defence archive itself. Second, the Population
   Registry is a live administrative register, not an archive: it does not "open" on a timetable the way
   deposited archival material does, and it has no public search interface at any age. If a user needs the
   exact rule for their case, have them confirm it with the holding body rather than repeating a number
   from this skill.

5. **Confusing kibbutz records:** Kibbutz members often appear in kibbutz internal records (pinkas) rather than municipal records. For kibbutz families, contact the kibbutz archive directly or check the Central Zionist Archives.

6. **A wrong NLI attribute or parameter fails SILENTLY, and that is the most dangerous failure mode in this
   skill:** NLI does not reject a condition it cannot parse. It drops the condition, returns UNFILTERED
   results, and reports the skip only in an `Errors` response header. A query built on an unrecognised
   attribute (`subject`) or a retired parameter (`publication_year_from` / `publication_year_to`) therefore
   hands back a full, plausible, well-formed result set that ignored the user's town or date entirely, with
   nothing in the body to signal it. Use only the documented attributes listed under Recommended MCP
   Servers, and read the `Errors` header on every call before reporting anything. An empty result set is
   equally untrustworthy: report what you searched, on which attributes, and what came back, never "NLI
   holds nothing on this".

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

### "My NLI search returned plenty of results but none are about my town"
Almost always a silently dropped condition. Check in this order:
1. Read the `Errors` response header. If it lists a skipped condition, the result set is unfiltered and
   means nothing.
2. Check you used a documented attribute. `subject` and `publication_year_from` / `publication_year_to` are
   not recognised and are dropped without an error in the body.
3. Check the query carries at least a three-character string over one of the search attributes.
4. Re-run with `title,contains,{town}` and, separately, `publisher,contains,{town}`, since a local
   newspaper or community publication is often indexed by publisher rather than title.
5. If the body is HTML rather than JSON, that is Cloudflare answering, not the API. Send a User-Agent other
   than curl's default and retry.

### "The records I need are restricted"
1. For Population Registry: submit the current Population Registry request form with proof of relationship (verify the form on gov.il first)
2. For IDF records: submit a formal request through the Ministry of Defense archives
3. For rabbinate records: contact the specific rabbinate with a written request
4. Do NOT assume a record older than 70 years is publicly accessible. The 70-year window governs who may
   OBTAIN a vital record, not whether it appears in any public database, and the Population Registry has no
   public search at any age. An old record may still have to be requested, and may sit with the Israel State
   Archives rather than the registry. Ask the holding body which of the two has the file.

## Recommended MCP Servers

| MCP Server | Why It Helps | Notes |
|------------|--------------|-------|
| [`nli-search`](https://agentskills.co.il/he/mcp/nli-search) (National Library of Israel) | Lets an AI agent query the NLI catalog directly for historical newspapers, photographs, manuscripts, and community records, the primary-source backbone of Israeli genealogy research | Requires an NLI API key. Search on documented attributes, for example `query=title,contains,Tiberias&material_type=archives`. See the NLI API notes below. |

**NLI API notes (read before your first call):**
- **Get a key.** A free personal key is issued at https://api2.nli.org.il/signup/. NLI also publishes a
  shared guest key on its own Search API page (`DVQyidFLOAjp12ib92pNJPmflmB5IessOq1CJQDK`), but it is
  heavily throttled and in testing returned `429 OVER_RATE_LIMIT` rather than results. Treat the guest key
  as a way to check query syntax, not as a research key.
- **Documented query attributes:** `title`, `creator`, `publisher`, `language`, `start_date` / `end_date`,
  `shelfmark`, `system_number`. Operators are `contains` and `exact`. Clauses join with `,AND;` or `,OR;`;
  standalone filters and commands (`material_type`, `availability_type`, `sort_field`, `items_per_page`,
  `result_page`, `output_format`, `count_mode`) are appended with `&`.
- **Three-character minimum.** NLI documents that a basic query must carry at least a three-character
  string over one of the search attributes. Single Hebrew letters and very short tokens fail this.
- **`sort_field` vs `sortField`.** NLI's parameter table says `sort_field` while a worked example on the
  same page uses `sortField`. Prefer `sort_field`; if sorting looks ignored, check the `Errors` header and
  try the other spelling.
- **Cloudflare blocks the `curl/*` User-Agent specifically**, not your IP and not a missing header. A bare
  `curl` with no `-A` still sends `curl/x.y.z` and gets an HTML challenge page; any other User-Agent, or
  genuinely no `User-Agent` at all, reaches the API and returns JSON. When debugging, check whether the
  body is HTML (Cloudflare) or JSON (the API answering).

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
