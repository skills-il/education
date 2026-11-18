---
name: hebrew-kids-story-maker
description: "Create a personalized, illustrated Hebrew children's book starring the user's child, ready to print. Writes age-appropriate Hebrew with correct gender forms, gets niqqud from Dicta (never the model itself), checks it word by word and adapts it to the reading stage, builds a consistent character sheet with text-free picture prompts, and lays out a right-to-left printable book (A5, square or folded booklet). Use when a parent asks for a bedtime story starring their child, a first reader with niqqud for grade 1 or 2, a book for a new sibling, starting gan or moving home, or pastes niqqud from Dicta and wants it checked and made into the final book. Prevents broken niqqud, wrong gender forms and garbled letters in pictures. Do NOT use for typesetting a manuscript (hebrew-book-typesetter), other documents (hebrew-document-generator), grading tests (hebrew-exam-grader), school systems (israel-school) or curriculum material."
license: MIT
compatibility: "The bundled scripts need only Python, with no network and no packages, so run them on any host that can execute Python: agents with a shell (Claude Code, Cursor, Codex, Gemini CLI and similar), Gemini, and chat apps with code execution turned on. Hosts that cannot run code follow the manual route in each step: niqqud through the Nakdan website, a manual check, and an HTML template the parent prints from the browser. Only route A (Dicta's model run locally) needs a shell with network."
---

# Hebrew Kids Story Maker

## Problem

Parents want a book where their own child is the hero: a bedtime story about the dinosaurs she loves, a first reader with niqqud for a boy starting grade 1, a gentle book before a new baby arrives. AI assistants write the story easily but fail at the parts that make it a usable Hebrew book: they add niqqud themselves and get it wrong, mix masculine and feminine forms for the child, put garbled Hebrew letters inside the pictures, draw a different child on every page, and hand back text instead of something that can be printed.

## Instructions

Work through the steps in order. Ask only what you cannot infer, and keep every question
short; most parents are not technical.

**Deliver in the first reply.** When the request already says who the child is and what the
book is about, do not stop at questions. Pick sensible defaults for what is missing (say which,
in one line each), and deliver the whole first draft: page texts, character sheet, one complete
illustration prompt per page, and the printable HTML. Put open questions at the end; the
parent's answers become the second round. Stop before writing only when the child's gender for
grammar, or who reads the book, is genuinely unknown.

**If the parent pasted text that already came back from Dicta (or another vocalizer), start
here, before anything else:**

1. Compare every word with what the parent typed. A word whose letters changed beyond a dropped
   vav or yod (הבובה came back as הַבֻּבּוֹת) is an error: say so and restore the parent's word.
2. Report the child's name: every occurrence as typed and as returned (נועה came back as נֹעָה),
   then use one agreed form on every page.
3. Check every second-person form against the child's gender (table in
   `references/reading-stages.md`).
4. Grade 2 reader: put back every vav and yod the parent typed (בּוּבָּה, נוֹעָה, הוֹלֶכֶת,
   כִּיתָּה), as in Step 4. Never deliver Dicta's defective spelling to a grade 2 child.
5. Grade 1 reader: include the grade 1 niqqud section (Step 4).
6. Deliver the final book: the corrected page texts, and the complete HTML in the reply.

### Step 1: Intake

Collect:

| Question | Why it matters |
|---|---|
| The child's first name, and how it is pronounced | The name appears on every page and vocalizers often respell names |
| How to address the child grammatically (boy / girl) | Hebrew verbs, adjectives and "you" change with gender. Ask; never infer it from the name (נועם, טל, עדי, שי are given to both) |
| Age, and who will read the book: the parent aloud, or the child alone | Picks the reading stage and the niqqud profile (Step 2) |
| For a child reading alone: which letters and vowel signs they already read (the parent or the teacher knows) | A book for a beginner must use only those, or the child cannot decode it |
| What the child loves (animals, trucks, space, a toy, a pet's name) | The story is built around it |
| The theme or gentle message, if any (bedtime, courage, sharing, a new sibling, starting gan, moving home, a doctor visit) | Shapes the plot |
| Other people or pets in the story, first names only | Each one needs their own gender forms |
| Size: A5 portrait, square, or a folded home booklet. Printing at home or at a print shop | Picks the layout (Step 6) |
| Will the book ever be sold or published, or is it for the family | Decides the niqqud route and what to say about image rights |

Privacy: use the first name only. Do not ask for a surname, the gan or school name, an address,
health details beyond what the theme needs, or a photo. The book does not need a photo of the
child (Step 5). Say which outside services will see the story text: the AI assistant itself,
any image tool, and Dicta's website if route B is used (Step 4).

If the parent describes something heavier than a story can carry, such as a child who regularly
refuses to go to sleep or to gan out of fear, persistent nightmares, frequent unexplained
tantrums, or any talk of self-harm, say kindly that these are signs worth raising with the
child's pediatrician or a child psychologist (the AACAP list of signs that a child may need
help includes them), and point to the israeli-mental-health-navigator skill. Talk of self-harm
is an immediate referral, not story material: if anyone is in danger now, emergency services;
for emotional first aid, ער"ן on 1201; and the israeli-emergency-guide skill. A story can still be written alongside, as a
conversation starter, never as treatment.

### Step 2: Pick the reading stage

Full table and sources in `references/reading-stages.md`. In short, from the Ministry of
Education guideline on vocalizing primary-school texts:

| Reader | Niqqud profile | Text per page (default) |
|---|---|---|
| Toddler or gan, read aloud by a parent | Optional; full niqqud helps the adult | one to four short sentences |
| Grade 1, reading alone | Nearly full, without the strong dagesh, the mappiq and the shin dot | one or two short sentences |
| Grade 2 | Heavy niqqud with the vowel letters kept (בּוּבָּה, כִּיתָּה) | two or three sentences |
| Grade 3 | Stories always fully vocalized | a short paragraph |
| Grades 4 to 6 | Little supporting niqqud, on names and hard words | a short paragraph |

At every stage the guideline vocalizes poetry in full and gives uncommon names full or
supporting niqqud. This skill also treats a rhymed refrain as poetry (its own choice, not a
Ministry rule). Tell the parent which profile you chose and why, in one sentence.

**A child reading alone needs a decodable text**, not just niqqud: only the letters and vowel
signs the child has learned, short words, heavy repetition. Check the vocalized text (Step 4)
with `niqqud_tools.py inventory --letters ... --vowels ... --max-syllables 3`, which lists every
word that uses something the child has not learned (write בּ / ב, כּ / כ, פּ / פ and שׁ / שׂ
separately if they were taught as separate sounds, and add sheva to the vowels only once it was
taught), every long word, and every qamats qatan (כׇּל is said with "o", but a beginner reads
every ָ as "a"). Swap those words before printing. Some words cannot go: the child's name, the
word for what they love (כַּדּוּרֶגֶל). Agree them with the parent as sight words
(`--sight "איתי,כדורגל"`), and early in the year use a split page: the parent reads the
narration, and the child reads one short line or the refrain, which alone must be decodable. Without code execution, do it by hand: on the
draft, list every word with a letter outside the parent's list; after vocalizing, list every
word with a vowel sign outside it, every word of more than three syllables and every כָּל-type
word, and show the parent the table.

### Step 3: Write the story

Write in standard unvocalized Hebrew first (the spelling the parent reads every day). Niqqud
comes in Step 4.

- **The child is the hero and solves the problem.** One small problem, a few tries, a warm
  ending. Grown-ups help but do not rescue.
- **One scene per page.** Each page must be drawable as a single picture.
- **Match the stage.** For a first reader: short familiar words, one idea per line, line breaks
  at phrase boundaries, and a repeated refrain the child can anticipate. For read-aloud books:
  rhythm, sounds, a refrain.
- **Gender agreement everywhere.** Every verb, adjective and second-person word that refers to
  the child matches the gender the parent gave. The dedication ("this book is for you") is
  where errors cluster. Forms table: `references/reading-stages.md`.
- **Help the vocalizer with gender.** Unvocalized, הצלחת, ראית, לך, שלך, שמך and את are the same
  for a boy and a girl. Put a form whose letters show the gender next to them (אתה / את with a
  gendered verb, הוא / היא), or rephrase ("כל הכבוד, איתי! הוא הבקיע!" rather than "הצלחת!").
  In a first reader, prefer the rephrasing.
- **Themes, gently.** New sibling: the older child gets a real role and stays loved. Starting
  gan: name the worry, show a small first success, end with pickup. Moving home: what comes
  along (the toy, the family), what is new and good. Fears: the scary thing stays small and is
  tamed on the page; a bedtime book ends calm. Present the book as something to read together
  and talk about, not as therapy, and do not promise it will fix a behavior.
- **No brand characters** (Peppa, Paw Patrol, Disney). Invent your own; it also keeps the book
  free to print.
- **Length.** Match the page counts in `references/reading-stages.md`. Write the title and the
  dedication as the first two paragraphs of the text, so they go through the vocalizer and the
  check with the pages; the cover and dedication page are placed in layout.

Show the parent the text page by page with the rest of the draft. If they change a word after
vocalizing, that word goes through the vocalizer again.

### Step 4: Niqqud from Dicta, then a word-by-word check

Do NOT add niqqud yourself. Language models vocalize Hebrew unreliably and the errors are
invisible to a parent skimming the page. Use Dicta (details, code and terms in
`references/niqqud-routes.md`):

| Route | When |
|---|---|
| A. Dicta's open model, run locally (CC BY 4.0, credit Dicta on the back cover) | Shell agent with network; the route for a book that may be sold |
| B. The Nakdan website (nakdan.dicta.org.il): the parent pastes the text and pastes the result back | Any host. Personal use only: Dicta's Terms of Use apply Attribution-NonCommercial-ShareAlike 4.0 |
| C. No niqqud | A read-aloud book for a toddler, if the parent prefers |

Never script the Nakdan website: Dicta's terms forbid access by any method other than its
interface. Before route B, tell the parent that text sent to Dicta's services is licensed to
Dicta, and offer to use a stand-in name while vocalizing.

What comes back differs by route. The model drops the vowel letters by default (נועה becomes
נֹעָה); for grade 2 run it with `mark_matres_lectionis="*"` so it keeps and marks them. The
website keeps the letters the parent typed but can leave a vav bare beside the vowel (נֹועָה,
הַבֻּובָּה), which is neither standard nor the grade 2 form, and it writes the qamats qatan of
כָּל as a plain qamats. `adapt` repairs the first in every profile; `check` flags the second.
The website also gets gender wrong: in a test on 2026-11-17, a girl's text containing "את ילדה"
came back with מָצָאתָ, רָאִיתָ and הָלַכְתָּ, all masculine.

Then adapt and check every word (adapt first, so the check sees the text that will print):

```bash
python3 scripts/niqqud_tools.py adapt --stage grade1 --in story_menukad.txt --out story_final.txt
python3 scripts/niqqud_tools.py check --plain story.txt --vocalized story_final.txt \
    --gender f --name "נועה"
```

`check` lists: words whose letters changed, second-person forms that do not match the child
(past tense הִצְלַחְתָּ / הִצְלַחְתְּ, מָצָאתָ / מָצָאת, suffixes לְךָ / לָךְ, שִׁמְךָ / שְׁמֵךְ, and
mixed forms like לְךְ that are neither), words ending in ך, את or ית whose gender it cannot see,
every occurrence of each name as sent and as returned, words left without niqqud, malformed
marks (including a bare vav beside a vowel), ש without a dot, and כָּל-type words with a plain
qamats.
Exit code 1 means something must be fixed. `adapt` applies the stage profile: `grade1` removes
the strong dagesh (except in ב כ פ, where it changes the sound), the mappiq and the shin dot
(keeping it on שֹׁ, where the holam would otherwise read as a sin dot); `grade2` turns the kept
vowel letters into holam male and shuruk (נוֹעָה, בּוּבָּה); `full` is standard niqqud. Website
output already keeps the vowel letters, so `grade2` works on route B too.

The script cannot see a wrong choice between words spelled alike (the Ministry's own example:
מדבר can be מִדְבָּר or מְדַבֵּר; also סֵפֶר / סָפַר, אֶת / אַתְּ). Read every page aloud with
the parent once before layout.

Without code execution, do the same pass by hand in the same order and show the parent a short
table (page, word, what to check). Three mark repairs are safe by hand, as fixed substitutions
on a bare vav inside a word (never a doubled וו): a holam, a qamats or ׇ before it moves onto it
as holam male (נֹועָה, יָופִי, אָוזְנַיִם become נוֹעָה, יוֹפִי, אוֹזְנַיִם), and a qubuts before it
becomes a shuruk (הַבֻּובָּה becomes הַבּוּבָּה). Fix only gendered forms whose correct spelling is in the forms
table, and words the parent confirms. Agree the vocalized form of the child's name once and use
it on every page. Never re-vocalize a whole sentence yourself. The grade 1 profile is safe by
hand because it only deletes marks: remove the shin dot (not on שֹׁ), the mappiq, and the dagesh
in every letter except ב כ פ, a word's first letter and a shuruk וּ. Never add or change a vowel,
and list the words you changed.

**Grade 1 niqqud section (always, for a grade 1 reader).** The answer carries its own short
section headed "ניקוד לכיתה א'" that states, for this child, the Ministry of Education's grade 1
recommendations: (1) drop the strong dagesh (keep it in ב כ פ, where it changes the sound),
(2) drop the mappiq (the dot in a final ה), (3) drop the shin dot (keep the sin dot, and keep the
dot on שֹׁ). It says that this child's text should follow them, and applies them: with
`adapt --stage grade1`, or by hand as deletions (above) once the niqqud is back. Never describe
plain full niqqud as the grade 1 text. A passing mention elsewhere does not replace this section.

**Grade 2 needs the parent's vowel letters back.** Dicta's model drops them by default (נועה
comes back נֹעָה, בובה comes back בֻּבָּה). With code execution, `adapt --stage grade2 --plain
story.txt` puts back every vav and yod the parent typed and writes them as the Ministry's
grade 2 examples do. Without it, repair each such word from the parent's spelling: a holam
before the restored vav becomes holam male (נוֹעָה, הוֹלֶכֶת, יוֹשֶׁבֶת), a qubuts becomes a
shuruk (בּוּבָּה, שׁוּלְחָן), and a hiriq keeps its letter and gets the yod after it (כִּיתָּה).
Never deliver Dicta's defective spelling as a grade 2 text.

### Step 5: Illustrations

Details: `references/illustration-guide.md`.

1. **Character sheet.** With the parent, fix the child character's look in one English
   paragraph: age, hair, face and skin tone (neutral words), one outfit, one signature item.
   Same for a pet or a toy. No photo of the real child, and no attempt at a real likeness: if the
   parent offers a photo, decline it, say why (a recognizable child's likeness should not go to
   third-party image tools, and the book does not need it), and let the parent choose the look
   instead of copying the child's features.
2. **Style line.** One fixed line for the whole book (medium, palette, shapes, mood). No "in
   the style of" a studio, franchise or living artist.
3. **Scene per page**, in English, where the text will sit (top, bottom, or a band over the
   picture).
4. **Assemble and lint the prompts:**
   ```bash
   python3 scripts/build_prompts.py prompts.json --out prompts.md
   ```
   Every prompt carries the style line, the full character sheet word for word, the scene, a
   composition note and a no-text rule. The lint flags Hebrew or quotations in prompts, objects
   with writing (signs, labels, book titles), photo or likeness requests, frightening words and
   studio names. Without code execution, assemble the same blocks by hand in the same order.
   Deliver each page's prompt fully assembled, one copy-paste block per page with the style
   line, the complete character sheet of everyone in the scene, the scene, and the no-text rule.
   Never hand over parts for the parent to combine. Use this output template for the prompts
   section, every time:
   - First, in Hebrew, one short line for each change you made to what the parent asked, with the
     reason: a sign or welcome line moves into the page text (image models garble Hebrew); a
     studio or franchise name ("Pixar look") becomes a described look (a studio's style is
     someone else's brand, which matters when copies are sold); no photo of the child.
   - Then a block labelled `CHARACTER BLOCK (paste unchanged)`, in English only: every
     character's sheet, the child's toy or pet included.
   - Then one block per page, headed only "Page N" (no Hebrew story text beside the prompts),
     in English only, with no Hebrew letters at all: the style line, the character block copied
     word for word, the scene, the composition note, and the line "No text, letters or writing
     in the image."

   Rules that keep the pictures consistent:
   - Every block repeats the FULL sheet of every character in that picture, word for word, on
     every page, even when the reply gets long. A later page is never just a "Scene:" line.
   - Everyone who appears gets a sheet, parents and a baby included, written once and reused.
   - One outfit for the whole book, bedtime pages included (no switch to pajamas). A change the
     story needs (a pregnancy, a new baby in the arms) goes in the scene line, never into an
     edited sheet.
   - No sign, banner, poster, label or book cover in the picture, not even a blank one. Words
     the parent wants shown (a welcome line) go on the page as text, over a plain wall or sky.
5. **Generate.** Character reference first, then each page, attaching the reference image when
   the tool allows it. Reject images with letters, a changed outfit, extra fingers or a
   frightening face. If the host has no image tool, deliver `prompts.md` and tell the parent to
   save the pictures as `art/p1.png`, `art/p2.png` and so on next to the book file.

All text lives in the layout, never in the picture: image models garble and mirror Hebrew
letters.

### Step 6: Layout

Write a `story.json` (format in the script's `--help`) with the title, optional dedication, the
checked page texts, image paths, layout per page, font and credits, then:

```bash
python3 scripts/make_storybook.py story.json --out book.html --embed-images
python3 scripts/make_storybook.py story.json --out booklet.html --booklet --embed-images
```

- `size`: `a5` (148 x 210 mm) or `square` (210 x 210 mm). `--bleed 3` (or the shop's figure)
  for a print shop; ask the shop for its bleed and safe area.
- Fonts: use one checked for every niqqud mark: Noto Sans Hebrew (clearest print letters, the
  default for first readers), Fredoka (rounded), Frank Ruhl Libre (classic serif), Assistant,
  Varela Round, David Libre. All are OFL fonts, which may be embedded and used in a printed or
  sold book. Avoid handwriting-style fonts for a child still learning letter shapes. With
  `font_file` the script embeds a local font and, if fontTools is installed, refuses a font
  missing any character in the book, since the browser would otherwise borrow the missing mark
  from another font letter by letter and break the niqqud.
- Layouts per page: `image-top`, `image-bottom`, `image-full` (text on a light band over the
  picture), `text-only`. `--draw-frames` writes ציירו כאן in empty frames for a book the child
  finishes with crayons.
- `--booklet` (A5 only) puts two pages on each A4 landscape sheet in the order a book bound on
  the RIGHT needs: the front cover on the left half of the outer sheet, page 2 behind it, and
  the sheets nested. Blank pages are added before the back cover to reach a multiple of four.

Without code execution, fill `references/storybook-template.md` page by page and give the parent the
HTML file. If you cannot write files, paste the complete HTML in your reply as one code block
for the parent to save as `book.html`; never stop at describing the layout. For a folded booklet the template has the sheet layout and a page-order table for
8, 12 and 16 pages: never fall back to the printer's own booklet mode, which usually binds on
the left. Number the PHYSICAL pages first (cover = 1, then every page in order, back cover
last) and fill the table from those numbers, never from story-page numbers. For 8 pages (cover,
six story pages, back cover):

| Sheet | Face | Left half (physical page) | Right half (physical page) |
|---|---|---|---|
| 1 (outer) | outside | 1 (front cover) | 8 (back cover) |
| 1 (outer) | inside | 7 (story page 6) | 2 (story page 1) |
| 2 (inner) | outside | 3 (story page 2) | 6 (story page 5) |
| 2 (inner) | inside (centre) | 5 (story page 4) | 4 (story page 3) |

Give the parent the table in this form: physical page numbers first, the content in brackets.

Printing (tell the parent): open the file in Chrome or Edge, Print, "Save as PDF" or the
printer, Margins None, Scale 100, Background graphics on. Most home printers leave a small
unprinted margin on plain paper, so keep important parts of a picture away from the edges. For the booklet, print the first two pages double-sided as a test, usually with
"flip on short edge" since the sheets are landscape: page 2 must sit behind the front cover, the
right way up. If it is upside down, switch to the other flip setting and test again. A printer
without double-sided printing: print the odd pages of the PDF, put the stack back in the tray
turned over, print the even pages, and check the first sheet before the rest; if page 2 landed
behind the wrong sheet, print the even pages again in reverse order. Then fold the
stack and staple on the fold.

### Step 7: Deliver

Give the parent: the HTML (and the PDF when your host can produce one), `prompts.md` if the
pictures are still to be made, and a short checklist: name spelled and vocalized as agreed,
every "you" form read aloud (אַתְּ, not אֶת, in a girl's dedication), no letters inside pictures, one page printed and the niqqud checked
on paper (marks sit under the right letters, nothing shows as a box), booklet test sheet done.

Put credits on the back cover: the niqqud source (route A: "ניקוד: מודל
dictabert-large-char-menaked של דיקטה, ברישיון CC BY 4.0") and the font and its licence. If the
book may be sold or published, always say both of these, even when the parent asked about
something else: (1) niqqud from the Nakdan website is for personal use only, so a sold book
needs route A with the Dicta credit, or no niqqud; (2) check the image tool's terms, and pictures
made from prompts alone may not be protected by copyright (the US Copyright Office's January
2025 position), so others could copy them.

## Examples

### Example 1: Bedtime story, read aloud

User says: "תכין סיפור לפני השינה על הבת שלי מאיה, בת 4, שמתה על דינוזאורים"

Actions:
1. Intake: girl, read aloud by the parent, dinosaurs, bedtime; A5 assumed and stated.
2. Stage: read-aloud, niqqud optional; the parent wants it, route B.
3. Ten pages, a refrain ("לילה טוב, דינוזאור קטן"), Maya helps a little dinosaur who cannot fall
   asleep, calm ending in bed.
4. Parent pastes the text into the Nakdan website and back. Manual check finds לְךְ on the
   dedication page; fixed to לָךְ. Name agreed with the parent as מָאיָה (same letters as
   written, only vowels added).
5. Character sheet for Maya and the toy dinosaur; ten prompts; host has an image tool.

Result: an A5 HTML book with eleven pictures, ready to save as PDF, plus a back-cover credit.

### Example 2: First reader with grade 1 niqqud

User says: "I want a book my son Itai can read by himself, he's in first grade and loves fire trucks"

Actions:
1. Boy, grade 1, reading alone: grade 1 profile, `text_size` large, short sentences, a refrain.
2. Ask which letters and vowels Itai reads; run `inventory` until only approved sight words
   remain, or split each page into a parent part and a short line for Itai.
3. Route A on a shell agent; `adapt --stage grade1` removes the strong dagesh, the mappiq and
   the shin dot, then `check` with `--gender m --name "איתי"`.
4. Fire trucks without fire or danger: the truck helps a cat down from a tree.
5. `make_storybook.py --booklet` for a stapled A5 booklet printed at home.

Result: a grade 1 booklet with near-full niqqud, a test-sheet instruction and the Dicta credit.

### Example 3: Preparing for a new sibling

User says: "נולד לנו תינוק בעוד חודש, אני רוצה ספר שיכין את יואב (5) לאח הקטן"

Actions: Yoav gets a real "big brother" job, the parents' love stays unchanged; gender forms
checked for Yoav and the baby; distress that worries the parent goes to the pediatrician.

Result: a twelve-page square book, prompts for a host without an image tool, and the HTML.

## Bundled Resources

### Scripts
- `scripts/niqqud_tools.py`: `check` lists words to fix against what was sent; `adapt` applies the grade 1, grade 2 (with `--plain`, restoring vowel letters) or full profile; `inventory` lists words a beginner cannot decode yet. Run: `python3 scripts/niqqud_tools.py --help`
- `scripts/build_prompts.py`: assembles and lints consistent, text-free illustration prompts. Run: `python3 scripts/build_prompts.py --help`
- `scripts/make_storybook.py`: builds the printable RTL book (A5 or square, booklet, bleed, embedded images and font). Run: `python3 scripts/make_storybook.py --help`

### References
- `references/reading-stages.md`: niqqud profile per grade with the Ministry's wording, text defaults per stage, the gender forms table. Consult in Steps 2 to 4.
- `references/niqqud-routes.md`: the three niqqud routes, Dicta's terms, the local-model code with a pinned revision, and the check. Consult in Step 4.
- `references/illustration-guide.md`: character sheet, style line, no-text rule, safety, generating, image rights. Consult in Step 5.
- `references/storybook-template.md`: a fill-in HTML book and booklet sheet table for hosts that cannot run code. Consult in Step 6.
- `references/domain-checklist.md`: the coverage checklist this skill is reviewed against.

## Gotchas

- Agents add niqqud themselves when asked for a "menukad" book. Route the text through Dicta and check it; never vocalize a sentence by hand.
- Agents trust the vocalizer on לך, שלך, שמך, הצלחת, ראית and את. They are spelled alike for both genders, and come back wrong or mixed (לְךְ). Check each against the child's gender.
- Agents call a text with full niqqud "readable by a first grader". A beginner can decode only the letters and vowel signs already taught; check the words against them.
- Agents infer the child's gender from the name. Ask.
- Agents print Dicta's asterisks or lose the vowel letters a grade 2 reader needs. The model drops vowel letters by default; for grade 2 request them and convert with `adapt --stage grade2`.
- Agents ask image models for a sign, a book cover or a name banner in the picture. Hebrew comes out garbled. The layout carries all words.
- Agents paraphrase the character description from page to page, so the child changes. Paste the same sheet word for word into every prompt.
- Agents lay out a booklet in left-to-right order, so the story runs backwards when folded. Hebrew binds on the right: the cover is the outer sheet's left half.
- Agents tell parents that Dicta is free to use for anything. The open model is CC BY 4.0; the website is NonCommercial-ShareAlike.

## Reference Links

| Source | URL | What to Check |
|---|---|---|
| Ministry of Education, vocalizing primary-school texts | https://meyda.education.gov.il/files/Mazkirut_Pedagogit/HebrewPrimary/learning-teaching/books/nikod.pdf | Niqqud profile per grade |
| Dicta niqqud model (Hugging Face) | https://huggingface.co/dicta-il/dictabert-large-char-menaked | Licence, usage, vowel-letter option, revisions |
| Dicta Terms of Use | https://dicta.org.il/tos | NonCommercial-ShareAlike clause, licence on submitted text |
| Dicta Nakdan website | https://nakdan.dicta.org.il/ | The web tool for route B |
| SIL Open Font License FAQ | https://openfontlicense.org/ofl-faq/ | Embedding and print use of OFL fonts |
| US Copyright Office, AI report Part 2 | https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-2-Copyrightability-Report.pdf | Copyright in AI-generated pictures |

## Troubleshooting

### The vocalized text came back with letters missing from words
Cause: the model drops vowel letters (yod, vav) by default; the check lists these separately from real changes. Verified in testing: נועה came back as נֹעָה.
Solution: for standard niqqud this is expected. For grade 2, re-run with `mark_matres_lectionis="*"` and `adapt --stage grade2`. Agree the child's name form with the parent.

### The local model returns repeated words without niqqud
Cause: observed with transformers 5.x; the same revision worked with 4.57.
Solution: `pip install "transformers<5"`, keep the pinned revision.

### Niqqud marks sit in the wrong place or show as boxes in the PDF
Cause (inferred from per-character font substitution): the font lacks marks, or the web font did not load. The six fonts in Step 6 were checked.
Solution: use one of them, or a checked `font_file`, and open the file online once.

### The booklet pages are in the wrong order after folding
Cause: the wrong flip setting, or one-sided printing; not a page-order bug if the test sheet shows page 2 behind the cover.
Solution: switch between long-edge and short-edge flip and keep the sheets in order.

### The pictures do not print
Cause: the file cannot find the pictures (wrong folder or file name), so the frames stay empty.
Solution: put them in `art/` next to the HTML with the exact names, or rebuild with `--embed-images`.
