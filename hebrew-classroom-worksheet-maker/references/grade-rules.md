# Grade rules (checked for school year תשפ"ז, 2026-27)

These are published Ministry of Education guidelines, written mostly for textbook authors and curricula. They are the default, and the teacher can override them. Never present a sheet as approved by the Ministry. Where this file says "inference", the rule is this skill's reading and not the Ministry's text.

## Niqqud by grade

| Grade | Default | Ministry wording |
|---|---|---|
| א | Heavy niqqud. No strong dagesh, no mappiq, no shin dot | "ניקוד מרובה. הטקסטים ינוקדו כמעט במלואם. כדאי להשמיט סימנים שאינם תומכים בפענוח המדויק של המילה, כמו דגשים חזקים ומפיק. מומלץ לא לנקד ש' ימנית." |
| ב | Heavy, with some unpointed exposure | "בדרך כלל ניקוד מרובה עם חשיפה לכתיב חסר הניקוד. בכיתה ב' מומלץ להסתייע באימות הקריאה לצד הניקוד." |
| End of ב | Partial, in short texts and repeated instructions | "לקראת סוף כיתה ב' חשוב להפגיש את התלמידים עם טקסטים מנוקדים חלקית, בעיקר בטקסטים קצרים ובהוראות החוזרות על עצמן." |
| ג | Supportive, decreasing | "ניקוד מסייע, אך הולך ופוחת." |
| ג, by text | Stories and poems full. Instructions partial or none | "סיפורים, שירים וטקסטים מן המקורות ינוקדו תמיד בניקוד מלא." and "טקסטים מידעיים קצרים, הוראות ומשימות מוכרות החוזרות על עצמן ינוקדו בניקוד מסייע חלקי או ללא ניקוד כלל." |
| End of ג | Basic and pragmatic | "לקראת סוף כיתה ג', כדאי להפחית בהדרגה את הניקוד לניקוד בסיסי, פרגמטי, ולהסתייע בכתיב המלא כחלופה לניקוד." |
| ד-ו | Sparse | "ניקוד מסייע מועט. יש להפעיל שיקול דעת ולהוסיף ניקוד במילים מורכבות שאינן שכיחות, במונחים, בשמות, במילים הומוגרפיות." |

At every grade: "שירה וטקסטים מן המקורות, כגון מן המקרא או מן התפילה, ינוקדו במלואם באופן שבו הם מובאים במקור." This is about pointing. It gives no permission to print a protected poem. Also: "שמות שאינם שכיחים ומילים זרות ינוקדו בניקוד מלא או מסייע."

## The grade 1 marks rule

Ministry text: omit strong dagesh and mappiq, and do not point the right shin. Its examples prefer הַמַיִם over הַמַּיִם and a shin with no dot.

**One mechanical rule, used by hand and by the checker:**

1. Remove every dagesh, except in ב, כ, פ and a shuruk (וּ).
2. Remove the shin dot, except on a shin that also carries holam (שֹׁ).
3. Keep the sin dot (שׂ) and every vowel.

Sheet option: for a class whose primer prints the dagesh in ג ד ת, set `gdt_dagesh` to `keep`. It stays at the start of a word and after a closed syllable, and one form is used across the sheet. A dagesh that doubles a letter after a vowel is still removed. The final ת with sheva in אַתְּ is not a doubling, so in this setting it stays. Mixed forms on one sheet are an error under every setting. The check for a missing dagesh inside a word is a pattern, so a word that correctly has none after a closed syllable goes in `sight_words`.

Inference: the Ministry does not list which letters keep a dagesh. This rule keeps it where it changes the sound (ב כ פ), drops it in ג ד ת where it does not, and keeps the dot on שֹׁ so the holam is not read as a sin dot.

Grade 2 prefers a vowel letter together with the niqqud: בּוּבָּה rather than בֻּבָּה, and כִּיתָּה rather than כִּתָּה. The Ministry says so openly: "אלו הן דוגמאות לניקוד שאינו מתיישב עם כללי הניקוד".

Grades 4-6: do not point every homograph. "טוב יהיה לאפשר לתלמידים בכיתות הגבוהות (ד'-ו') להתלבט ולהתחבט בפענוח הומוגרפים", while "יש להימנע מהעמסת יתר של מצבים עמומים".

## Letters, vowels and reading stages

There is no national order: "במהלך כיתה א נלמדים סימני הניקוד זה אחר זה (סדר הוראת הסימנים משתנה לעיתים בין שיטות קריאה שונות)". Ask what this class has learned, including final letters, the soft and hard sounds of ב כ פ, and sin.

- Language curriculum: "תוכנית לימודים להוראת השפה והאוריינות בעברית" (2026), kindergarten to grade 2. The Haredi textbook criteria (2017) still rest on an earlier program.
- End of grade 1, from the Hebrew supervisor's circular for תשפ"ו (no תשפ"ז circular was found): "יש לשאוף להשלים את תהליך רכישת הקריאה והכתיבה לכל המאוחר עד סוף כיתה א."
- Grades 2-3, same circular: "זהו שלב משמעותי בתהליך התבססות שטף הקריאה."
- Mid grade 2: "נוהגים להתייחס לאמצע כיתה ב' כשלב מעבר מקריאה המבוססת בעיקרה על תהליכי קידוד פונולוגיים לקריאה התופסת את המילים כיחידות אורתוגרפיות שלמות."

## Kindergarten

The kindergarten chapter (PDF dated 2013): "הוראה פורמלית ותרגול של כתיבה תקנית בגן אינם מומלצים", and "בגן חובה יש לטפח עיצוב אותיות." The newer 2026 curriculum describes children trying phonetic writing from gan onward, and says: "הכתיבה הפונטית בכיתה א היא דרך יעילה מאוד לביסוס הידע האלפביתי". Reading the two together (inference): a child's own attempts at writing are welcome, and drills of copying standard letters are not. This skill builds sound and picture games for gan, not copying sheets. No source gave a numeric math range by kindergarten age, so use the range the teacher states.

## Math: which program

"בשנה זו, יצטרפו תלמידי כיתות ג' לתלמידי כיתות א' ו-ב' וילמדו על פיה." Grades 4-6: "תלמידי כיתות ד'-ו' ימשיכו בשנת הלימודים תשפ"ז ללמוד על פי התוכנית משנת 2006." The rollout moves one grade each year, so recheck this each school year.

| Grade | Numbers | Operations |
|---|---|---|
| א | "הכרת המספרים הטבעיים בתחום 100 וה-0" | Addition and subtraction to 20, whole tens to 100. No multiplication or division. "תחילה פועלים בתחום העשר, ואחר כך בתחום העשרים." |
| ב | To 1,000 | Meaning of × and the colon. "לוח הכפל יילמד בהדרגה כך שבסוף כיתה ב' ישלטו כל התלמידים בכפולות של 2, של 4, של 5 ושל 10" |
| ג | To 10,000 | "השלמה וביסוס הכפולות בלוח הכפל של 10 × 10", division with remainder within the table ("חילוק עם שארית בתחום לוח הכפל של 10 × 10") with a one-digit divisor ("המחלק הוא חד-ספרתי"), "הכרת ערכי האותיות א-ת." |
| ד-ו | 2006 program | **Not covered by this skill's math rules or checker.** See SKILL.md |

No negative numbers through grade 3. Answers are whole numbers, except the remainder form below.

## Staying in the program

When a request goes past the grade, keep the sheet in program, say why in one line, and offer an in-program challenge. The circular supports challenge inside the program: "יש לשלב משימות בדרגות קושי שונות" and "לחשוף תלמידים גם למשימות מאתגרות". Grade 1 examples: a missing addend, the equals sign on the left, a word problem ("יש לשלב שאלות מילוליות מתאימות", and read it against its exercise, since no script checks the operation). The teacher decides. If they keep the out-of-program items, list those item ids in `teacher_override`.

## Math notation

- Multiplication is ×. Division is a colon. Never ÷.
- Remainder: "כתיבת פתרונות של תרגילי חילוק עם שארית צריכה להיעשות באחת משתי הדרכים", in numbers `13 : 4 = 3 + (1 : 4)` or in words. On this skill's sheets the child fills one blank: `13 : 4 = ___ + (1 : 4)` or `13 : 4 = 3 + (___ : 4)`. The quotient is the whole part, and the remainder is smaller than the divisor. The old form `17 : 7 = 2(3)` is flagged in the program: "בצורה זו עלולה להוביל לתפיסה מוטעית".
- Include equations with the equals sign on the left: "יש לשלב משוואות, כולל כאלו שבהן סימן השוויון ממוקם משמאל לתרגיל", such as `10 = ___ + 4`.
- Expressions run left to right inside the Hebrew line. Each exercise on a sheet has exactly one blank and one answer.
- The grade 2 program covers vertical arithmetic ("במאונך"). The builder does not print it. Write it by hand in a left-to-right block with units under units, and read it on the rendered page.
- Terms: מחובר, סכום, מכפלה, מחלק, מחולק, מנה, שארית, ישר המספרים, יחידות, עשרות, מאות, אלפים.

## Streams

Holidays and texts differ by community. Ask only when it changes the content. For a Haredi class, follow the teacher on texts and images: "בחירת הטקסטים הספרותיים תישען על רשימת יצירות הספרות למגזר החרדי". Arab and Druze schools learn Hebrew as a second language, so this grade table does not apply. Ask for the learners' level instead.

## Items and pictures

- From the Haredi-sector textbook criteria (2017), used here as good practice for every stream and not as a rule binding them: "על הוראות הביצוע להיות מנוסחות ברמת קריאות מתאימה לתלמידים (אפשר להיעזר בסמלילים)" and "יש להקפיד שהאיורים המייצגים מילים ומשמשים להקניית הצלילים יהיו אסתטיים, ברורים וחד-משמעיים."
- One correct option per question: "לבדוק שלכל בסיס פריט (שאלה) יש רק מסיח (תשובה) אחד נכון." Distractors come from typical mistakes: "להשתמש בטעויות טיפוסיות/מאפיינות בניסוח המסיחים". (A higher-education checklist. No school-level equivalent was found.)
- Plural address: "מחקרים מעידים כי פנייה בלשון רבים בהקשרים לימודיים משפרת את הישגי התלמידות מבלי לפגוע בהישגי התלמידים". Plural imperative and past tense look alike, so: "כדי למנוע כפל משמעות, מומלץ להשתמש בניקוד עזר".
- Layout, from special-education guidance on adapted materials and used here as common practice: "הימנעות מעומס חזותי, רקע נקי, ריווח".

## Adapted material

For special-education math, point the teacher to the Ministry's adaptation document linked from the math circular. It is partial: "נכון לעת זו, מסמך ההתאמות כולל התייחסות לנושא המספרים הטבעיים והפעולות בהם". For a student with low vision, offer the editable HTML or text so the teacher can change size and spacing with the vision teacher. Formal accommodations belong to the school.

## Common practice, not a rule

No official source was found for these. Present them as common practice only: type size by age, black-and-white copier safety, identical look for differentiated versions, and computed answer keys. No Israeli source supports a special font for dyslexia, so make no such claim.
