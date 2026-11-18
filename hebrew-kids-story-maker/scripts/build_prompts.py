#!/usr/bin/env python3
"""Assemble consistent, text-free illustration prompts for a picture book, and lint them.

Every page prompt is built the same way: the style line, the FULL character sheet of
each character on the page (copied word for word, never paraphrased), the scene, a
composition note that keeps room for the text, and a fixed no-text rule. Copying the
sheet verbatim is what keeps the child looking the same from page to page.

Input JSON:
{
  "style": "soft watercolor picture-book illustration, warm pastel palette, rounded shapes",
  "characters": [
    {"id": "noa", "sheet": "Noa, a 4-year-old girl with curly brown shoulder-length hair, round face,
                            yellow raincoat with a small green dinosaur patch, red rain boots"}
  ],
  "pages": [
    {"page": 1, "scene": "Noa sits on her bed reading a picture book, evening light",
     "characters": ["noa"], "text_space": "bottom"}
  ]
}
text_space: "bottom" (default), "top", or "none" (full-bleed art with a text band).

Usage:
  python3 build_prompts.py prompts.json --out prompts.md
Exit code 1 when the lint finds something to fix (the file is still written).
"""

import argparse
import json
import re
import sys

NO_TEXT = ("No text, letters or writing in the image. No signs, banners, labels, numbers, book "
           "titles or speech bubbles anywhere in the scene.")
SAFE = "Gentle, safe, age-appropriate scene for a young child."
SPACE = {
    "bottom": "Keep the lower third calm and simple (plain ground or sky) to leave room for text.",
    "top": "Keep the upper third calm and simple (plain sky or wall) to leave room for text.",
    "none": "Keep a calm, uncluttered strip along the bottom edge for a text band.",
}
TEXT_WORDS = (r"\b(text|sign|signs|label|letters?|words?|writing|written|caption|title|banner|poster|says|saying|"
              r"speech bubble|alphabet|newspaper|logo|numbers?|numbered|scoreboard|(his|her|their|the) name|"
              r"name tag|named after|initials?|digits?|clock face|calendar|menu|license plate)\b")
PHOTO_WORDS = r"\b(photo|photograph|selfie|real child|looks like (my|our)|based on (the|my|a) (photo|picture)|realistic portrait)\b"
SCARY_WORDS = r"\b(blood|bloody|weapon|gun|knife|sword|kill|killed|dead|death|corpse|injur\w*|wound\w*|horror|scary|monster\w*|terrifying|scream\w*|attack\w*|scrap(e|ed|es)\b|bruis\w*|bleed\w*|bandage\w*|cut (knee|finger|hand|leg)|fire(?!\s*(truck|engine|fighter|station|man|men))|flames?|drown\w*)\b"
BRAND_WORDS = r"\b(disney|pixar|ghibli|dreamworks|peppa|paw patrol|pokemon|marvel|bluey|in the style of)\b"


def lint(label, text, issues):
    if re.search(r"[֐-׿]", text):
        issues.append(f"{label}: contains Hebrew. Image models garble Hebrew letters; describe in English and keep words out of the picture.")
    if re.search(r"[\"“”״]", text):
        issues.append(f"{label}: contains a quotation. A quoted phrase invites the model to write it into the image.")
    for rx, msg in ((TEXT_WORDS, "asks for something with writing on it"),
                    (PHOTO_WORDS, "refers to a real photo or real likeness; describe the character instead"),
                    (SCARY_WORDS, "may be frightening for a young child; soften it or confirm the parent chose it"),
                    (BRAND_WORDS, "names a studio, franchise or artist style; describe the look instead (and avoid it if the book may be sold)")):
        m = next((m for m in re.finditer(rx, text, flags=re.I)
                  if not re.search(r"\b(no|without|not|never)\s+(\w+\s+){0,2}$", text[:m.start()], flags=re.I)), None)
        if m:
            issues.append(f"{label}: '{m.group(0)}' {msg}.")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("prompts_json")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    with open(args.prompts_json, encoding="utf-8") as f:
        data = json.load(f)

    issues = []
    style = data.get("style", "").strip()
    if not style:
        issues.append("style: missing. One fixed style line for the whole book keeps the pictures consistent.")
    lint("style", style, issues)
    chars = {c["id"]: c["sheet"].strip() for c in data.get("characters", [])}
    for cid, sheet in chars.items():
        lint(f"character {cid}", sheet, issues)
        if len(sheet.split()) < 12:
            issues.append(f"character {cid}: the sheet is short. Pin the look (a person: hair, face, skin tone, "
                          "clothes, one signature item; an animal or toy: colors, shape, one signature detail), "
                          "or the character will change between pages.")

    out = ["# Illustration prompts", "",
           "Generate the character reference first, then each page. Paste each block as is.", "",
           "## CHARACTER BLOCK (paste unchanged)", "", "```"]
    out += [f"{cid}: {sheet}" for cid, sheet in chars.items()]
    out += ["```", ""]
    for cid, sheet in chars.items():
        out += [f"## Character reference: {cid}", "", "```",
                f"{style}. Character reference sheet on a plain white background: {sheet}. "
                f"Show the same character from the front, from the side and from the back, full body, "
                f"neutral standing pose. {SAFE} {NO_TEXT}", "```", ""]
    for p in data.get("pages", []):
        n = p.get("page")
        scene = p.get("scene", "").strip()
        lint(f"page {n}", scene, issues)
        ids = p.get("characters", [])
        unknown = [i for i in ids if i not in chars]
        if unknown:
            issues.append(f"page {n}: unknown character id(s) {unknown}")
        sheets = " ".join(f"Character: {chars[i]}." for i in ids if i in chars)
        space = SPACE.get(p.get("text_space", "bottom"), SPACE["bottom"])
        prompt = f"{style}. {sheets} Scene: {scene}. {space} {SAFE} {NO_TEXT}"
        out += [f"## Page {n}", "", "```", re.sub(r"\s+", " ", prompt).strip(), "```", ""]

    with open(args.out, "w", encoding="utf-8") as f:
        f.write("\n".join(out))
    print(f"wrote {args.out}: {len(chars)} character(s), {len(data.get('pages', []))} page prompt(s)")
    if issues:
        print("\nFIX BEFORE GENERATING:")
        for i in issues:
            print("- " + i)
        return 1
    print("lint: clean")
    return 0


if __name__ == "__main__":
    sys.exit(main())
