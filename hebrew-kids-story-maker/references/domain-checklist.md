# Domain Coverage Checklist: hebrew-kids-story-maker

Generated: 2026-11-17 via research on: Ministry of Education niqqud guideline (nikod.pdf, already established), Ministry of Education Pajama Library pages (pop.education.gov.il), Dicta Nakdan terms page (nakdan.dicta.org.il/terms-and-services, read from the SPA bundle), Dicta main-site Terms of Use (dicta.org.il, Creative Commons section, read from the SPA bundle), Hugging Face model card dicta-il/dictabert-large-char-menaked, SIL OFL FAQ (openfontlicense.org), google/fonts METADATA.pb plus a local cmap check of five OFL Hebrew fonts, OpenAI Terms of Use (search snippets only, page returned 403), US Copyright Office "Copyright and Artificial Intelligence, Part 2: Copyrightability" (January 2025, text extracted from the PDF), AACAP Facts for Families No. 24, Hebrew Language Academy unvocalized spelling rules (PDF returned an HTML block page, topic only).

Fetch notes: nakdan.dicta.org.il and dicta.org.il are SPA shells; the terms text was read from the shipped JS bundles, not guessed. openai.com returned 403 to WebFetch; OpenAI wording below is from search snippets of openai.com pages and must be re-read on the live page before quoting. The Hebrew Academy PDF returned a bot-block HTML page.

## Must cover (core)

### Reading stages and niqqud
- [ ] Reading stage drives niqqud density: grade 1 nearly full niqqud but omit strong dagesh and mappiq and do not mark the shin dot; grade 2 heavy niqqud plus matres lectionis alongside niqqud; grade 3 stories always fully vocalized; grades 4 to 6 little supporting niqqud: https://meyda.education.gov.il/files/Mazkirut_Pedagogit/HebrewPrimary/learning-teaching/books/nikod.pdf : why core: wrong density is the most common way a "learner" book becomes unreadable for its target child.
- [ ] Mid grade 2 is the transition point from decoding-based reading (same Ministry guideline, "נוהגים להתייחס לאמצע כיתה ב' כשלב מעבר מקריאה המבוססת בעיקרה על תהליכי קידוד"): nikod.pdf above : why core: maps the parent's "age" input to a niqqud profile.
- [ ] Pre-readers (gan, roughly ages 2 to 5) are read TO, not reading alone: the book is a read-aloud text, so full niqqud helps the adult reader and the child's later decoding, but page text length is set by listening, not decoding. Pajama Library serves daycare through grade 2, with toddler tracks for ages 1 to 2 and 2 to 3: pop.education.gov.il/kindergarten/developmental-program-early-childhood-education-care/pajama-library-little-ones/ : why core: the skill must ask "who reads it, the parent or the child" before picking a profile.
- [ ] Matres lectionis handling: the Dicta model removes matres lectionis by default; `mark_matres_lectionis='*'` keeps them, marked with asterisks: https://huggingface.co/dicta-il/dictabert-large-char-menaked : why core: grade 2 profile requires matres alongside niqqud (Ministry), so the default model output is wrong for grade 2 and the asterisks must be stripped, not printed.
- [ ] Unvocalized vs vocalized spelling relation: the Academy's unvocalized-spelling rules take vocalized spelling as given and add letters (vav, yod) to it; a full-spelling input word fed to a vocalizer may keep an extra vav/yod that a vocalized text would not carry: hebrew-academy.org.il/wp-content/uploads/כללי-הכתיב-חסר-הניקוד.pdf (topic surfaced by search; PDF blocked, quote not captured) : why core: explains why a word-by-word check after vocalization is required.
- [ ] Word-by-word check after vocalization (structural): every word in the child's name, every gendered form, and every homograph is checked by a human or second pass; flag words the model is unsure of rather than silently accepting: why core: the model is context-based and the child's name is usually out of vocabulary.
- [ ] The child's name: vocalize it by asking the parent how it is pronounced (e.g. stress and vowel of a rare or foreign name), never trust the model's guess: (structural) : why core: a mis-vocalized name on every page is the most visible error.

### Gender agreement
- [ ] Gender drives every form that refers to the child: 3rd-person verbs (הוּא הָלַךְ / הִיא הָלְכָה), adjectives (גָּדוֹל / גְּדוֹלָה), and 2nd-person address in dialogue or the dedication (אַתָּה / אַתְּ, לְךָ / לָךְ, שֶׁלְּךָ / שֶׁלָּךְ, imperatives לֵךְ / לְכִי, בּוֹא / בּוֹאִי) : source: standard Hebrew morphology; Academy primary source for the pronoun-suffix forms not captured (search found only Leshonenu La'am noun-inflection rules, hebrew-academy.org.il/wp-content/uploads/2025/07/לשוננו-לעם-מחזור-52-51-חוברת-4-תשס-תשסא-כללי-נטיית-השם-מהדורה-חדשה__1_.dictaocr.pdf, not opened) : why core: unvocalized לך, את, שלך are ambiguous and a vocalizer picks by context, so a girl's book can come back with לְךָ.
- [ ] Pass gender explicitly into the vocalization context (e.g. keep the full sentence with a gendered verb next to an ambiguous pronoun) and re-check every 2nd-person form after vocalization (structural) : why core: same failure as above.
- [ ] Ask, do not infer, the child's gender from the name (many Israeli names are unisex, e.g. נוֹעַם, טַל) (structural) : why core: inferring gender from a name produces wrong grammar for a real child.

### Vocalization tool terms
- [ ] Local model licence: dicta-il/dictabert-large-char-menaked is CC BY 4.0; attribution required (credit DICTA, link the licence); trust_remote_code=True is required to load it: https://huggingface.co/dicta-il/dictabert-large-char-menaked : why core: a sold or shared book must carry the attribution line.
- [ ] Model scope: trained on modern Hebrew prose; not intended for Biblical, Rabbinic, premodern, or poetic texts: same model card : why core: rhyming verse stories are "poetic"; warn the parent and tighten the word check for rhymed text.
- [ ] Dicta web services (nakdan.dicta.org.il) are covered by Dicta's Terms of Use, whose Creative Commons section says "Any use of our Services will be in accordance to Attribution-NonCommercial-ShareAlike 4.0 International": dicta.org.il (Terms of Use page, SPA) : why core: text vocalized via the website is NC-SA, so a book meant for sale must use the locally run CC BY model, not the website.
- [ ] No undocumented endpoints: Nakdan terms say "do not ... try to access them using a method other than the interface and the instructions that we provide": https://nakdan.dicta.org.il/terms-and-services : why core: the skill must not script the website's internal API; web path = parent pastes text manually.
- [ ] Upload licence: by submitting text to Dicta services the user gives Dicta "a worldwide licence to use, host, store, reproduce ..." for operating and improving the services: https://nakdan.dicta.org.il/terms-and-services : why core: feeds the privacy row below (story text contains the child's name).

### Font
- [ ] Use an OFL Hebrew font that covers niqqud codepoints U+05B0 to U+05BC, U+05C1, U+05C2 (shin/sin dots), U+05C7 (qamats qatan). Local cmap check 2026-11-17: Noto Sans Hebrew, Noto Serif Hebrew, Frank Ruhl Libre, David Libre cover all; Alef covers that range but lacks U+05BD (meteg), U+05BF (rafe) and U+05C4 to U+05C6, none of them used in modern children's text. All five are "OFL" per google/fonts METADATA.pb: github.com/google/fonts/tree/main/ofl : why core: a font without mark glyphs or GPOS mark positioning prints dotted circles or collided points.
- [ ] Print (block) letterforms, not cursive script, for any book the child reads alone; learners decode print letters (structural, follows from the Ministry decoding stage) : why core: cursive fonts defeat a learner book.
- [ ] Render test: print one page with every niqqud mark under the chosen font and inspect, since codepoint coverage does not prove good mark placement (structural).
- [ ] OFL permits embedding in a document, full or subset (FAQ 1.12), print publications are welcome without extra permission (FAQ 1.1), and embedding does not change the document's licence (FAQ 1.13): https://openfontlicense.org/ofl-faq/ : why core: answers "can I sell the printed book" for the font layer.

### Illustration consistency and child safety
- [ ] Never request or use a photo of the real child; describe the character with neutral, parent-chosen traits (hair, clothing, a signature item) in a fixed character sheet reused verbatim in every page prompt (structural) : why core: privacy and the scope statement.
- [ ] No text in images: Hebrew text rendered by image models is unreliable and RTL text is often mirrored; text goes only in the HTML layer (structural) : why core: wrong letters in a learner book.
- [ ] Age-appropriate fear level: bedtime and fear themes keep the threat small, named, and resolved on-page, with a safe ending; no peril to parents, no medical or death imagery unless the parent explicitly chose that theme (structural) : why core: a bedtime book that scares the child fails its purpose.
- [ ] Hosts without image generation: output one prompt per page plus the character sheet; chat-only hosts: page text + prompts + an HTML file (scope) : why core: required output contract.

### Privacy
- [ ] Collect first name only; no surname, ID, school/gan name, address, photo, or health details beyond what the theme needs (structural, data minimization) : why core: the story is sent to third-party tools.
- [ ] Tell the parent which third parties see the text: the host LLM, any image tool, and Dicta if they use the website (Dicta takes a licence to submitted content, see above); the local model sends nothing out: nakdan.dicta.org.il/terms-and-services : why core: informed choice before pasting the child's name into a web tool.
- [ ] Israel has no child-specific rule in the Privacy Protection Law per a Linklaters overview (secondary, may be stale): www.linklaters.com/en/insights/data-protected/data-protected---israel : why core: do not claim a statutory regime that does not exist; keep the advice to minimization.

### Print layout
- [ ] RTL page order: a Hebrew book binds on the right and the cover opens leftward; the PDF must be `dir="rtl"` with page 1 as the front cover so a print shop or viewer shows spreads correctly (structural) : why core: an LTR-ordered spread reverses the story.
- [ ] Home folded booklet: imposition for saddle-stitch (sheets of 4 pages, page count a multiple of 4, outer sheet carries the last page and page 1 in RTL order); browsers do not impose, so the skill outputs a pre-imposed booklet HTML or instructs the printer's booklet mode with right-edge binding (structural) : why core: the most common home-print failure.
- [ ] Print-shop file: add bleed and trim per the shop's own spec, keep text inside the safe margin; do not hardcode a bleed figure (no primary source verified) (structural) : why core: art cut off at the trim.
- [ ] Page sizes offered: A5 and square, as scoped; set CSS `@page { size: ... }` and verify the PDF dimensions (structural).

### Commercial use
- [ ] AI-image copyright: the US Copyright Office concludes "given current generally available technology, prompts alone do not provide sufficient human control to make users of an AI system the authors of the output"; human-authored text, perceptible human inputs, and creative selection, coordination, arrangement, or modification can be protected: https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-2-Copyrightability-Report.pdf : why core: a parent selling the book should not be told they own copyright in the pictures; US position only, Israeli law not settled by this report.
- [ ] Image-tool output terms: OpenAI Terms of Use state that as between user and OpenAI, to the extent permitted by law, the user owns the Output and OpenAI assigns its rights, if any; outputs may not be unique: https://openai.com/policies/row-terms-of-use/ (403 to fetch; wording from search snippets, re-read before quoting) : why core: contractual ownership is not copyright, and each image tool has its own terms.
- [ ] Vocalization path decides sale: local CC BY model = sale allowed with attribution; Dicta website output = NonCommercial and ShareAlike (see above) : why core: the single biggest commercial trap in this workflow.

### Bibliotherapy themes and referral
- [ ] Present themes (new sibling, starting gan, moving, fears) as a shared-reading conversation starter, never as therapy or treatment; no claims of therapeutic effect (structural) : why core: overclaiming is a health-claim and trust risk.
- [ ] Referral signals to surface to the parent, verbatim category list from AACAP for younger children: severe worry or anxiety shown by regular refusal to go to school or to sleep, persistent nightmares, frequent unexplainable tantrums, frequent physical complaints, threats to harm or kill oneself: https://www.aacap.org/AACAP/Families_and_Youth/Facts_for_Families/FFF-Guide/When-To-Seek-Help-For-Your-Child-024.aspx : why core: a parent asking for a "fears" book may be describing a clinical picture; route to the child's pediatrician or טיפת חלב / child psychologist rather than a story. Sibling skill: israeli-mental-health-navigator.
- [ ] Self-harm statement from a child is an immediate escalation to emergency services or a crisis line (route via israeli-emergency-guide / israeli-mental-health-navigator), not story material (structural, consistent with AACAP last item) : why core: safety.

## Should cover (advanced / edge cases)
- [ ] Text per page by stage: read-aloud books can carry a few sentences per page; early-reader books one or two short sentences per page with line breaks at phrase boundaries (structural; no Ministry numeric figure found, the Ministry first-grade "special guidelines" were not located): meyda.education.gov.il/files/Mazkirut_Pedagogit/HebrewPrimary/learning-teaching/books/sfarim.pdf
- [ ] Font size for early readers: larger than adult body text with generous line spacing so niqqud below a line does not touch the next line's ascenders; no Ministry numeric value located, so present as a render-and-check step, not a number (structural).
- [ ] Repetition and predictable refrains help emergent readers and read-aloud engagement; Pajama suggests pausing on pages after several readings to imagine what happens next: www.pjisrael.org (activity pages via search) (structural use).
- [ ] Rhymed text: Hebrew rhyme depends on vocalization and stress; rhyme check after vocalization, plus the model's "not for poetic texts" limitation.
- [ ] Siblings or friends named in the story: same first-name-only rule, same gender agreement for each named character.
- [ ] Multiple children or plural address (אַתֶּם / אַתֶּן, בּוֹאוּ) when the book is for twins or siblings.
- [ ] Religious or cultural framing (Shabbat, holidays) only when the parent asks; a Haredi profile has its own textbook guideline: meyda.education.gov.il/files/Mazkirut_Pedagogit/HebrewPrimary/learning-teaching/books/haredi.pdf
- [ ] Accessibility of the PDF: real text (not images of text) so screen readers and copy work; contrast between text and background, Ministry digital accessibility guidance favours clean straight-edged fonts and clear contrast: meyda.education.gov.il/files/Pop/0files/mada-technology/heker/tshpa/accessibility.pdf
- [ ] Dicta third-party ONNX wrapper (dicta-onnx) exists and is not affiliated with DICTA; if used, its own licence applies: model card above.
- [ ] Unicode normalization of niqqud order (NFC vs NFD can reorder dagesh and vowel); normalize before the word check and before typesetting (structural).
- [ ] Dedication page in 2nd person addresses the child directly and is the page most likely to carry gender errors.

## Out of scope (explicit, with rationale)
- Typesetting an existing manuscript the parent already wrote: hebrew-book-typesetter.
- General Hebrew documents (letters, certificates, invitations): hebrew-document-generator.
- Grading a child's writing or reading test: hebrew-exam-grader.
- School systems, report cards, Mashov / SmartSchool data: israel-school.
- Marketing copy, blog posts about the book: hebrew-content-writer.
- Clinical assessment, diagnosis, or a therapeutic protocol for anxiety, grief, or trauma: refer out (israeli-mental-health-navigator); the skill is not a therapist.
- Publishing logistics (ISBN, legal deposit, distribution, pricing): not part of a personal book workflow.
- Training or fine-tuning a vocalizer, or scraping Dicta's web API: barred by Dicta terms and outside scope.
- Photo-to-cartoon of the real child: excluded by design (privacy).
- Audio narration: not in the output contract.

## Known bad figures / common errors (with the correct value and source)
- "Run the model with the newest transformers": in testing on 2026-11-17 a transformers 5.x release returned garbled, repeated, unvocalized text from this model; 4.57 worked. Pin `transformers<5` and the reviewed model revision (references/niqqud-routes.md).
- "The vocalizer keeps the child's name as written": in testing it respelled נועה as נֹעָה (vowel letter dropped). Agree the name's form with the parent.
- "A feminine context makes לך come out feminine": in testing, a girl's story containing אַתְּ still came back with the mixed forms לְךְ, שֶׁלְּךְ, בִּשְׁבִילְךְ, which are neither masculine nor feminine. The check script flags them.
- "Dicta is open, so its website output is free to sell": wrong. Website/service use is CC BY-NC-SA 4.0 (dicta.org.il Terms of Use, Creative Commons section). Only the Hugging Face model is CC BY 4.0 (model card).
- "The Dicta model keeps matres lectionis": wrong. Default output removes them; `mark_matres_lectionis='*'` keeps them with asterisks (model card).
- "Grade 1 text should have every mark including dagesh chazak and the shin dot": wrong. Grade 1 omits strong dagesh and mappiq and does not mark the shin dot (nikod.pdf).
- "Grade 2 text drops the matres when niqqud is present": wrong. Grade 2 uses heavy niqqud plus matres alongside it (nikod.pdf).
- "Grade 3 can reduce niqqud in stories": wrong for stories. Grade 3 stories are always fully vocalized; only other texts reduce (nikod.pdf).
- "A detailed prompt makes me the copyright author of the picture": wrong under the US Copyright Office Part 2 report (January 2025), prompts alone do not suffice (report text, conclusion section).
- "Using an OFL font makes the book OFL-licensed": wrong. FAQ 1.13: embedding does not change the document's licence.
- "Alef has no niqqud": wrong. Alef covers U+05B0 to U+05BC, U+05C1, U+05C2 and U+05C7; it lacks U+05BD (meteg), U+05BF (rafe) and U+05C4 to U+05C6 (local cmap check of google/fonts Alef-Regular.ttf, 2026-11-17).
- "לך is fine, the vocalizer will get it right": unsafe. Ambiguous 2nd-person forms resolve by context and must be checked against the child's gender every time.

## Authoritative sources
- Ministry of Education, ניקוד טקסטים בספרי לימוד לבית הספר היסודי: https://meyda.education.gov.il/files/Mazkirut_Pedagogit/HebrewPrimary/learning-teaching/books/nikod.pdf
- Ministry of Education, textbook criteria (language education): meyda.education.gov.il/files/Mazkirut_Pedagogit/HebrewPrimary/learning-teaching/books/sfarim.pdf
- Ministry of Education, Pajama Library for Little Ones: pop.education.gov.il/kindergarten/developmental-program-early-childhood-education-care/pajama-library-little-ones/
- Dicta Terms of Use (Creative Commons section): dicta.org.il (SPA; terms rendered client-side)
- Dicta Nakdan Terms and Privacy (last modified 27 November 2017): https://nakdan.dicta.org.il/terms-and-services
- DictaBERT large char menaked model card (CC BY 4.0): https://huggingface.co/dicta-il/dictabert-large-char-menaked
- CC BY-NC-SA 4.0 legal code: creativecommons.org/licenses/by-nc-sa/4.0/legalcode
- SIL OFL FAQ (1.1, 1.12, 1.13): https://openfontlicense.org/ofl-faq/
- google/fonts OFL directory (METADATA.pb licence field): github.com/google/fonts/tree/main/ofl
- US Copyright Office, Copyright and Artificial Intelligence Part 2: Copyrightability (January 2025): https://www.copyright.gov/ai/Copyright-and-Artificial-Intelligence-Part-2-Copyrightability-Report.pdf
- OpenAI Terms of Use (re-verify live): https://openai.com/policies/row-terms-of-use/
- AACAP Facts for Families No. 24, When to Seek Help for Your Child: https://www.aacap.org/AACAP/Families_and_Youth/Facts_for_Families/FFF-Guide/When-To-Seek-Help-For-Your-Child-024.aspx
- Hebrew Language Academy, כללי הכתיב חסר הניקוד (PDF blocked to fetch): hebrew-academy.org.il/wp-content/uploads/כללי-הכתיב-חסר-הניקוד.pdf
