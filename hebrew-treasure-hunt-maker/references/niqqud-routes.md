# Getting niqqud for clue cards

Language models add niqqud unreliably, so the assistant never vocalizes a card itself. Pick a route by host.

| Route | Runs on | Terms |
|---|---|---|
| A. Dicta's open model on the machine | Hosts with a shell and network | Model card licence: CC BY 4.0, credit Dicta |
| B. The Nakdan website, pasted by hand | Any host, any device | Dicta's Terms of Use: Attribution-NonCommercial-ShareAlike 4.0, so family use only |
| C. No niqqud, an adult reads aloud | Any host | Nothing to license |

Never call the website from a script. Dicta's terms forbid access "using a method other than the interface and the instructions that we provide".

## Route A: the open model

Needs Python, PyTorch and `transformers` below version 5. The first run downloads the model from Hugging Face. It loads custom code from its repository, so pin the reviewed revision:

```python
# pip install torch "transformers<5"
from transformers import AutoModel, AutoTokenizer
REPO = "dicta-il/dictabert-large-char-menaked"
REV = "4dfc20b94565d7868e1c8c00bf039d38c071a062"  # pragma: allowlist secret (Hugging Face commit pin, not a credential)
tokenizer = AutoTokenizer.from_pretrained(REPO, revision=REV)
model = AutoModel.from_pretrained(REPO, revision=REV, trust_remote_code=True)
model.eval()
lines = [x.strip() for x in open("clues.txt", encoding="utf-8") if x.strip()]
open("clues_menukad.txt", "w", encoding="utf-8").write("\n\n".join(model.predict(lines, tokenizer)) + "\n")
```

The model is meant for modern prose, not poetry, and it makes mistakes. In testing for this skill it wrote `וַעַמּוּדִים` and `מְנִּיחִים`. Read every card. When a word comes back wrong, the easy fix is to reword the riddle and run it again, not to hand-edit marks.

It also drops vowel letters from names (נועה can come back as נֹעָה). Print the child's name on the card header unvocalized, and avoid putting the name inside a grade 1 riddle.

## Route B: the Nakdan website

1. Write each clue in plain spelling, one per line. Use no child names in the text you paste, since text sent to Dicta's services is licensed to Dicta to run and improve them.
2. Open nakdan.dicta.org.il, paste, let it vocalize, copy the result.
3. Paste it back into the conversation exactly as copied. The assistant does not re-type it.

## Then, on every route

Hosts with Python, for a grade 1 reader:

```bash
python3 scripts/niqqud_tools.py adapt --stage grade1 --in clues_menukad.txt --out clues_grade1.txt
```

`check_hunt.py` then rejects any grade 1 card that still has a strong dagesh, a mappiq or a shin dot.

Hosts without code can apply the grade 1 profile by hand, because it only deletes marks: remove the shin dot (not on שֹׁ), the mappiq, and the dagesh in every letter except ב כ פ, a word's first letter and a shuruk וּ. Never add or change a vowel. List the words you changed.

What no script catches: a wrong choice between words spelled alike (סֵפֶר / סָפַר, אֶת / אַתְּ). Ask the parent to read each card aloud once.
