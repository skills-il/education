# Israeli Genealogical Data Sources

## IGRA - Israel Genealogy Research Association

- **URL:** https://genealogy.org.il/AID/
- **Records:** 4M+ records (4,040,574 as of 26 July 2026)
- **Coverage:** Birth, marriage, death, immigration, voter rolls, professional registers
- **Access:** Free basic search, full membership for detailed records
- **Strengths:** Largest single Israeli genealogy database, a Daitch-Mokotoff Soundex search option, Palestine Gazette index
- **Limitations:** Not all records are digitized; some require in-person visits

## JewishGen

- **URL:** https://www.jewishgen.org/
- **Records:** Global Jewish genealogy databases
- **Key databases:** JOWBR (burial records), Yizkor Book translations, community databases
- **Access:** Free registration
- **Strengths:** Global scope, community-contributed data, discussion groups
- **Limitations:** Focus on diaspora communities; less coverage of post-1948 Israel

## National Library of Israel (NLI)

- **URL:** https://www.nli.org.il/
- **API:** https://api.nli.org.il/openlibrary/search
- **MCP Server:** nli-search (recommended for AI-assisted research)
- **Records:** Millions of items: manuscripts, photographs, newspapers, maps, audio
- **Access:** Free API key at https://api2.nli.org.il/signup/
- **Strengths:** Primary sources, historical newspapers (for obituaries/announcements), photographs
- **Query attributes (the only ones that work):** `title`, `creator`, `publisher`, `language`,
  `start_date` / `end_date`, `shelfmark`, `system_number`. Operators `contains` and `exact`. Clauses join
  with `,AND;` / `,OR;`; standalone filters and commands (`material_type`, `availability_type`,
  `sort_field`, `items_per_page`, `result_page`, `output_format`, `count_mode`) append with `&`.
- **Do NOT use `subject`, `publication_year_from`, or `publication_year_to`.** They are not recognised, and
  NLI drops an unrecognised condition SILENTLY and returns UNFILTERED results, reporting the skip only in
  an `Errors` response header. Read that header on every call.
- **Three-character minimum:** a basic query must carry at least a three-character string over one of the
  search attributes.
- **Guest key:** NLI publishes a shared key (`DVQyidFLOAjp12ib92pNJPmflmB5IessOq1CJQDK`) on its Search API
  page; it is heavily throttled and returned `429 OVER_RATE_LIMIT` in testing. Use a personal key for real
  work.
- **Cloudflare blocks the `curl/*` User-Agent signature specifically.** Any other User-Agent (or none at
  all) reaches the API. An HTML body means Cloudflare answered; a JSON body means the API did.
- **Limitations:** Not a genealogy database per se; requires creative searching

## Israel State Archives

- **URL:** https://www.archives.gov.il/
- **Records:** Government records, immigration files, census data, land documents
- **Access:** Free online access to digitized materials
- **Strengths:** Official government records, immigration certificates, Mandate-era files
- **Limitations:** Not all materials digitized; some restricted

## Central Zionist Archives

- **URL:** http://www.zionistarchives.org.il
- **Records:** Jewish Agency files, aliyah records, kibbutz records, organizational records
- **Access:** Free online catalog, reading room by appointment
- **Strengths:** Best source for pre-state immigration records and Zionist organization files
- **Limitations:** Physical archive in Jerusalem; not fully digitized

## Rabbinate Records

- **Access:** Via local rabbinate offices
- **Records:** Marriage and divorce records. Commonly described as running from 1948, but Knesset Yisrael community marriage registers predate the state; for a pre-1948 marriage ask about community registers rather than assuming nothing exists.
- **How to request:** Written request with names, approximate dates, and proof of relationship
- **Limitations:** Decentralized (each city has its own rabbinate), not digitized

## Population Registry (Ministry of Interior)

- **Access:** Submit the current Population Registry request form with ID and relationship proof (verify the exact form number on gov.il, since form numbers change)
- **Records:** Birth, death, marriage certificates, from the establishment of the registry in 1948
- **Limitations:** A 70-year limit applies to personal vital records, with only first-degree relatives able
  to obtain one inside that window. The registry is a LIVE administrative register, not an archive: it has
  no public search interface at any record age, and it does not "open" on a timetable. An older file may
  have been transferred to the Israel State Archives, which is a different holder under a different access
  regime. Ask which body holds the file rather than assuming an age threshold makes it public.
- **Do not carry the defence-archive rule here.** Defence-establishment material is under a separate,
  longer and independently administered restriction that does not apply to births, marriages or deaths. Get
  its current terms from the defence archive itself rather than from any figure quoted elsewhere.

## Municipal Archives

Major city archives:
- **Jerusalem:** Jerusalem Municipal Archives
- **Tel Aviv:** Tel Aviv-Yafo Municipal Archives (Beit Ariela)
- **Haifa:** Haifa Municipal Archives
- **Access:** Varies by municipality; contact the city historian or archive department
- **Records:** Property tax (arnona), building permits, business licenses, local council minutes

## IDF Archives (Ministry of Defense)

- **URL:** https://archives.mod.gov.il/sites/English/Pages/default.aspx
- **Records:** Military service records **from 1948 onward**
- **Access:** Restricted; family members can submit formal requests
- **Limitations:** Long processing times; some records permanently classified. Restriction periods for
  defence material are set and extended by the defence establishment itself; ask the archive for the current
  terms rather than relying on a figure quoted elsewhere.
- **Does NOT hold pre-state service.** For Haganah, Palmach, Etzel, Lehi and Betar files see below.

## Pre-State Military and Underground Archives (pre-1948)

- **Haganah Historical Archives** (Tel Aviv). Locate the current site via https://www.archives.org.il; an
  older standalone domain for this archive no longer resolves, so do not hand the user a hard-coded URL.
- **Palmach Museum archive**: Palmach personnel and unit records
- **Jabotinsky Institute Archives** (Tel Aviv), for Etzel, Lehi, Betar and Revisionist bodies
- **Why this matters:** the IDF Archive begins in 1948. Sending a user there for a 1930s or 1940s ancestor
  costs months and returns "no such file".

## Non-Jewish Personal Status Records

Marriage, divorce and inheritance for non-Jewish Israelis are registered by recognized religious courts, so
the rabbinate holds nothing for these families:
- **Sharia courts** (בתי הדין השרעיים) for Muslim families; also hold Ottoman and Mandate-era sijill volumes
- **Druze religious courts** for Druze families
- **Christian denominational courts and parish registers** (Greek Orthodox, Latin, Melkite, Armenian and
  others), many of which run well before 1948

## Aggregated and Diaspora Portals

- **Israel Archives Network:** https://www.archives.org.il, aggregated search over municipal, kibbutz,
  university and institutional archives. Use before contacting individual city halls.
- **Historical Jewish Press (JPress):** https://www.nli.org.il/en/newspapers, free full-text OCR of Davar,
  Haaretz, the Palestine Post, HaTzvi and others. The best route to obituaries and mourning notices, and it
  needs no API key.
- **JRI-Poland:** https://jri-poland.org, the largest index of Polish Jewish vital records.
- **Genealogy Indexer:** https://www.genealogyindexer.org, OCR'd Jewish directories, yizkor books and
  Mandate-era Palestine business and residential directories.
- **Routes to Roots Foundation:** https://rtrfoundation.org, inventory of surviving Eastern European
  archival holdings.
- **Gravez:** https://gravez.me/en/, Israeli grave locator with strong recent-burial coverage.
- **Yad Vashem Pages of Testimony:** https://yvng.yadvashem.org, genealogically useful because a Page names
  the victim's parents, spouse and town AND the submitting relative and their relationship. Route actual
  Holocaust victim research to dedicated tools.

## Cemetery and Gravestone Records

- **JOWBR (JewishGen Online Worldwide Burial Registry):** https://www.jewishgen.org/databases/cemetery/ (free; worldwide Jewish burial records including many Israeli cemeteries)
- **JewishGen "Locating Burial Records in Israel" InfoFile:** https://www.jewishgen.org/infofiles/il-burial_records.htm (guide to which Israeli cemetery is indexed where)
- **BillionGraves:** https://billiongraves.com/ (crowd-sourced GPS-tagged headstone photos and transcriptions)
- **Chevra Kadisha cemetery databases:** burial-society plot registers; many large Israeli chevra kadisha bodies publish online plot lookups, others answer by phone request

## Genealogy Organizations and Family-Name Databases

- **IGS (Israel Genealogical Society):** membership organization with regional branches, lectures, and research help; distinct from IGRA. Search for the current society site on gov.il or a genealogy portal, since the organization's web address has changed over time.
- **Beit Hatfutsot / ANU - Museum of the Jewish People:** free Jewish family-name and genealogy databases (formerly the Douglas E. Goldman Jewish Genealogy Center). Database of Jewish Family Names (Memi De-Shalit): https://dbs.anumuseum.org.il/skn/en/c6/BH . Collaborative family-tree platform: https://geni.anumuseum.org.il/

## Additional Resources

- **MyHeritage:** https://www.myheritage.com/ (Israeli-founded, large database)
- **Geni:** https://www.geni.com/ (collaborative family trees)
- **FamilySearch:** https://www.familysearch.org/ (LDS Church, includes some Israeli records)

Note: This skill does not cover Yad Vashem Holocaust victim name searches. For Holocaust victim research, use Yad Vashem's Central Database of Shoah Victims' Names directly at https://yvng.yadvashem.org/.
