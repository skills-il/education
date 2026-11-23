# Reading stages, niqqud and gender forms

## Niqqud by stage (Ministry of Education guideline)

Source: the Ministry of Education guideline for vocalizing primary-school textbooks (nikod.pdf). It governs textbooks. Applying it to clue cards is this skill's choice.

| Who reads the card | `reading_stage` | Niqqud | What the guideline says |
|---|---|---|---|
| Pre-reader | `gan` | The child never needs to read: `adult_reads` or `picture` | "הוראה פורמלית של הקריאה והכתיבה בשנות הגן אינה מומלצת" |
| Grade 1 | `grade1` | Nearly full, without strong dagesh, mappiq and the shin dot | "הטקסטים ינוקדו כמעט במלואם", "מומלץ לא לנקד ש' ימנית" |
| Grade 2 | `grade2` | Heavy | "בדרך כלל ניקוד מרובה עם חשיפה לכתיב חסר הניקוד" |
| Grade 3 | `grade3` | Supportive, and full for a rhyme (the guideline's poetry sentence sits in its grade 3 section) | "ניקוד מסייע, אך הולך ופוחת", "סיפורים, שירים וטקסטים מן המקורות ינוקדו תמיד בניקוד מלא" |
| Grades 4 to 6 | `grade4-6` | Sparse: rare words, names, homographs | "ניקוד מסייע מועט" |

Grade is a starting point, not a reading assessment. If the parent says a child reads below grade, use the lower stage. For a child who is still struggling, use `adult_reads`.

The checker's word limits per card (14, 26, 40 and 60 words for grade 1, grade 2, grade 3 and grades 4 to 6, and 8 for a child who just started reading) are this skill's working defaults, not official figures. Exceeding one is a warning.

## Puzzle types by age (common practice, no official source)

| Age | Works well |
|---|---|
| 3 to 4 | Picture matching, colors, "find the same", an adult reads aloud |
| 5 to 6 | Picture riddles, first letter, counting, a simple jigsaw |
| 7 to 8 | Short rhyming riddles with niqqud, picture cipher, mirror writing |
| 9 to 10 | Atbash, logic grids, wordplay |
| 11 to 12 | Multi-step ciphers, homographs, gematria, a final meta-puzzle |

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
ך whose gender it cannot see; read each one aloud against this table. On a grade 1 card, the simplest fix is to avoid these forms and write the riddle in the third person. Twins or
siblings addressed together take the plural: אַתֶּם (boys or mixed), אַתֶּן (girls), בּוֹאוּ.

