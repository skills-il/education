# Getting niqqud from Dicta, and checking it

Language models add niqqud unreliably, so the story text is never vocalized by the assistant
itself. Dicta (the Israel Center for Text Analysis) offers two sanctioned routes. Pick by host
and by whether the book may be sold.

| Route | Runs on | Terms | Can the book be sold? |
|---|---|---|---|
| A. Dicta's open model on your machine | Agents with a shell and network (Claude Code, Cursor, Codex, Gemini CLI and similar) | Model card licence: CC BY 4.0, credit Dicta and link the licence | Yes, with the credit line |
| B. The Nakdan website, pasted by hand | Any host, any device | Dicta's Terms of Use: "Any use of our Services will be in accordance to Attribution-NonCommercial-ShareAlike 4.0" | No, personal and family use |
| C. No niqqud | Read-aloud books for toddlers and gan | Nothing to license | Yes |

Never call the website from a script. Dicta's terms forbid accessing its services "using a
method other than the interface and the instructions that we provide", and its developers page
documents open models, not a Nakdan API.

## Route A: the open model (dicta-il/dictabert-large-char-menaked)

Needs Python, PyTorch and `transformers` below version 5 (the model's own code was tested with
4.57; a 5.x release returned garbled, repeated text). The first run downloads the model from
Hugging Face. The model loads custom code from its repository, so pin the revision you have
reviewed rather than whatever is newest:

```python
# pip install torch "transformers<5"
from transformers import AutoModel, AutoTokenizer

REPO = "dicta-il/dictabert-large-char-menaked"
REV = "<full hash of commit 4dfc20b>"  # copy it from the model's Commits page; the revision this skill was tested with

tokenizer = AutoTokenizer.from_pretrained(REPO, revision=REV)
model = AutoModel.from_pretrained(REPO, revision=REV, trust_remote_code=True)
model.eval()

pages = [p.strip() for p in open("story.txt", encoding="utf-8").read().split("\n\n") if p.strip()]
# Grade 2 keeps the vowel letters: ask the model to mark them with '*' and let adapt handle it.
vocalized = model.predict(pages, tokenizer, mark_matres_lectionis="*")
open("story_menukad.txt", "w", encoding="utf-8").write("\n\n".join(vocalized) + "\n")
```

Read `BertForDiacritization.py` at that revision before the first run if you have not seen it.

What the model does to spelling: by default it drops the vowel letters that unvocalized
spelling adds (נועה becomes נֹעָה, לישון becomes לִישֹׁן). With `mark_matres_lectionis="*"` it
keeps them and marks each one with an asterisk (נֹו*עָה). Never print the asterisks:
`niqqud_tools.py adapt` turns them into the grade 2 form (נוֹעָה, בּוּבָּה, כִּיתָּה) or drops
the marked letters for standard niqqud. If you already have the default output (no asterisks),
`adapt --stage grade2 --plain story.txt` puts back the vav and yod letters the parent typed.

The model card says it is meant for modern prose, not for poetic texts. For a rhyming story,
check the rhyming words by ear after vocalizing.

Credit line for the back cover: "ניקוד: מודל dictabert-large-char-menaked של דיקטה, ברישיון
CC BY 4.0 (creativecommons.org/licenses/by/4.0)". dicta-onnx is a third-party wrapper that Dicta
says it is not affiliated with; if you use it, its own licence applies.

## Route B: the Nakdan website

1. Write the story in standard unvocalized spelling, one page per paragraph.
2. Open nakdan.dicta.org.il, paste the text, let it vocalize, copy the result.
3. Paste the result back into the conversation exactly as copied. The assistant does not
   re-type or "tidy" it.

What the website returned in a test on 2026-11-17 (default settings): it kept the vowel letters
that were typed, but left a vav bare next to the vowel (נֹועָה, הַבֻּובָּה, לִישֹׁון), wrote the
qamats qatan of כָּל as a plain qamats, and returned masculine past forms (מָצָאתָ, רָאִיתָ,
הָלַכְתָּ) for a girl although the same text said "אַתְּ יַלְדָּה". `adapt` (any stage) turns the
bare vav into holam male or shuruk (נוֹעָה, הַבּוּבָּה), and `adapt --stage grade2` works on
this output because the vowel letters are already there. `check` flags the plain-qamats כָּל and
the gender forms. The website also has a setting for vocalizing in defective or full spelling
(ניקוד בכתיב חסר / ניקוד בכתיב מלא); whatever it returns, run adapt and check.

Before pasting, tell the parent two things. Text sent to Dicta's services is licensed to Dicta
for running and improving them, so if the parent prefers, write the story with a stand-in first
name of the same gender and swap the real name back in afterwards (then vocalize the name by
hand with the parent). And the result is for personal use: the website's terms are
NonCommercial-ShareAlike.

## The check (every route)

Hosts that can run Python (adapt first, so the check sees the text that will print):

```bash
python3 scripts/niqqud_tools.py adapt --stage grade1 --in story_menukad.txt --out story_final.txt
python3 scripts/niqqud_tools.py check --plain story.txt --vocalized story_final.txt \
    --gender f --name "נועה" --name "דני"
```

`check` exits 1 when there is something to fix. It reports, page by page:

- CHANGED: the letters of a word differ from what was sent (a typo introduced, a word dropped).
- GENDER: a second-person form that does not match the child (past tense such as הִצְלַחְתְּ /
  הִצְלַחְתָּ, suffixes such as לָךְ / לְךָ or שְׁמֵךְ / שִׁמְךָ), or a mixed form like לְךְ that is
  neither. A form addressed to another character of the other gender is fine; check who is
  spoken to. Fix the rest from the gender table in `reading-stages.md`.
- COULD BE 'YOU': words ending in ך, את or ית whose gender the script cannot see (שְׁמֵךְ-type
  nouns outside its list, past forms like זָכִית or הֵבֵאת it does not know). Nouns such as מַשָּׂאִית
  appear here too; read them aloud and move on.
- QAMATS QATAN written as a plain qamats (כָּל): a beginner reads it with "a". Use ׇ (כׇּל) or
  another word in a first reader.
- NAME: every occurrence of each name, as sent and as returned. The model often respells a name
  (נועה came back as נֹעָה in testing). Agree the name's vocalized form with the parent once and
  use it everywhere.
- UNVOCALIZED words, MALFORMED marks (a mark with no letter, two vowels on one letter, a bare
  vav beside a holam or qubuts that adapt was not run on), and ש without a shin or sin dot.
- The full list of second-person forms, to read aloud.

What no script catches: a wrong choice between words spelled alike (מִדְבָּר / מְדַבֵּר, the
Ministry's own example; סֵפֶר / סָפַר; אֶת / אַתְּ). Read every page aloud with the parent once.

Hosts that cannot run code: the three bare-vav repairs are fixed substitutions and safe by hand,
on a bare vav inside a word, never a doubled וו (a holam, qamats or ׇ before it moves onto it as
holam male: יָופִי becomes יוֹפִי; a qubuts before it becomes a shuruk). The grade 1
profile is also safe by hand, because it only deletes marks: remove the shin dot (not on שֹׁ),
the mappiq, and the dagesh in every letter except ב כ פ, a word's first letter and a shuruk וּ.
Never add or change a vowel, and list the words you changed.

Chat hosts without a shell do the same pass by hand, in the same order, and show the parent a
short table: word, page, what to check. Fix only what the parent confirms, or a gendered form
whose correct spelling is in the table; never re-vocalize whole sentences by hand.
