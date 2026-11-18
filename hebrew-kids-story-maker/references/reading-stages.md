# Reading stages, niqqud profiles and gender forms

## Niqqud by stage (Ministry of Education guideline)

Source: the Ministry of Education guideline for vocalizing primary-school textbooks,
"ניקוד טקסטים בספרי לימוד לבית הספר היסודי" (meyda.education.gov.il, nikod.pdf). The guideline
is written for textbooks; a story book for a child at that stage follows the same logic.

| Who reads the book | Niqqud profile | What the guideline says | `niqqud_tools.py adapt --stage` |
|---|---|---|---|
| A parent reads aloud (gan) | Optional. Full niqqud helps the adult and does no harm | Not covered by the guideline (it starts at grade 1) | `full`, or none |
| Grade 1, reading alone | Nearly full niqqud, without the strong dagesh, the mappiq and the shin dot | "הטקסטים ינוקדו כמעט במלואם. כדאי להשמיט ... דגשים חזקים ומפיק. מומלץ לא לנקד ש' ימנית" | `grade1` |
| Grade 2 | Heavy niqqud, with the vowel letters (yod, vav) kept next to the niqqud: בּוּבָּה rather than בֻּבָּה, כִּיתָּה rather than כִּתָּה | "בכיתה ב' מומלץ להסתייע באימות הקריאה לצד הניקוד" | `grade2` |
| Grade 3 | Stories are always fully vocalized | "סיפורים, שירים וטקסטים מן המקורות ינוקדו תמיד בניקוד מלא" | `full` |
| Grades 4 to 6 | Little supporting niqqud: uncommon words, names, homographs | "ניקוד מסייע מועט" | `full` on chosen words only, by hand |

Rules that apply at every stage: poetry and texts from the sources are vocalized in full,
uncommon names and foreign words get full or supporting niqqud, and the middle of grade 2 is where children usually
move from decoding letter by letter to reading whole words. Toward the end of grade 2 the
guideline also wants children to meet partly vocalized text; a family book can ignore that.

What `grade1` removes, exactly: the strong dagesh, which does not change the sound (in every
letter outside ב ג ד כ פ ת, and in ג ד ת after a vowel inside the word; in ב כ פ the dagesh
changes the sound, so it stays), the dot in a final ה (mappiq), and the right-hand dot of ש.
The guideline's list is open-ended ("כמו"); these are the marks it names. The sin dot (שׂ) stays,
since it changes the sound, and a ש that carries holam (שֹׁ) keeps its dot, because the holam
dot alone sits where a sin dot does and would be read as sin. The vav of a shuruk (וּ) keeps its
dot.

A beginner reads every ָ as "a". Dicta's open model marks the qamats qatan (the "o" in כׇּל,
חׇכְמָה, צׇהֳרַיִם) with its own sign ׇ, which the six fonts in the skill all draw; the website, in
a test on 2026-11-17, wrote כָּל with a plain qamats. For a grade 1 reader, prefer words without
it: `niqqud_tools.py inventory` lists the marked ones and `check` lists common ones written with
a plain qamats.

This skill treats a rhymed refrain as poetry, which the guideline vocalizes in full at every
stage; that reading is the skill's own choice, not a Ministry rule. In a
grade 1 book, either run the refrain through `adapt --stage full` separately or accept the
grade 1 profile for it knowingly.

## Text shape by stage (defaults, adjust to the child)

These are working defaults, not official figures. The layout script warns when a page is
longer than its text size fits.

| Stage | Pages of story | Text per page | Sentences | `text_size` |
|---|---|---|---|---|
| Toddler, read aloud | 8 to 12 | one or two short sentences | concrete, repetitive, a refrain | `medium` |
| Gan, read aloud | 10 to 16 | two to four sentences | a small problem solved by the child | `medium` |
| Grade 1 reader | 8 to 12 | one or two short sentences (early in the year: a parent part plus one short line for the child) | short words, one idea per line, break lines at phrase boundaries, sight words agreed with the parent | `large` |
| Grade 2 reader | 10 to 14 | two to three sentences | simple dialogue allowed | `large` |
| Grade 3 and up | 12 to 16 | a short paragraph | richer vocabulary, still one scene per page | `small` |

## Gender forms that refer to the child

Ask the parent how to address the child grammatically. Never infer it from the name: many
Israeli names are given to both girls and boys (נועם, טל, עדי, שי).

| Form | Boy | Girl |
|---|---|---|
| Third-person past | הוּא הָלַךְ, הוּא שָׂמַח | הִיא הָלְכָה, הִיא שָׂמְחָה |
| Adjective | גָּדוֹל, אַמִּיץ | גְּדוֹלָה, אַמִּיצָה |
| You | אַתָּה | אַתְּ |
| To you | לְךָ | לָךְ |
| Yours | שֶׁלְּךָ | שֶׁלָּךְ |
| For you | בִּשְׁבִילְךָ | בִּשְׁבִילֵךְ |
| You (object) | אוֹתְךָ | אוֹתָךְ |
| On you | עָלֶיךָ | עָלַיִךְ |
| Come! | בּוֹא | בּוֹאִי |
| Go! | לֵךְ | לְכִי |
| Look! (imperative) | רְאֵה | רְאִי |
| You did it (past tense) | הִצְלַחְתָּ, רָאִיתָ, שָׂמַחְתָּ, מָצָאתָ, נִסִּיתָ | הִצְלַחְתְּ, רָאִית, שָׂמַחְתְּ, מָצָאת, נִסִּית |
| Your name, like you, yourself | שִׁמְךָ, כָּמוֹךָ, עַצְמְךָ | שְׁמֵךְ, כָּמוֹךְ, עַצְמֵךְ |

Unvocalized, לך, שלך, בשבילך, שמך, הצלחת, ראית and את look the same for both genders, so a
vocalizer decides from context and can get it wrong, or return a mixed form such as לְךְ that is
neither. The check script lists every second-person form it recognizes and every word ending in
ך whose gender it cannot see; read each one aloud against this table. In a first reader, the
simplest fix is to avoid these forms: address the child by name in the third person, which
spells the gender out in letters (הוּא הִצְלִיחַ / הִיא הִצְלִיחָה). Twins or
siblings addressed together take the plural: אַתֶּם (boys or mixed), אַתֶּן (girls), בּוֹאוּ.

The dedication page is written to the child in the second person, so it is where these errors
cluster.
