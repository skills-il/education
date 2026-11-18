#!/usr/bin/env python3
"""Build a printable right-to-left Hebrew picture book (HTML) from a story JSON file.

Open the HTML in Chrome or Edge, Print, "Save as PDF" (or print directly).
No network access from this script and no external packages required.

Story JSON:
{
  "title": "נוֹעָה וְהַדִּינוֹזָאוֹר הַקָּטָן",
  "subtitle": "",                       optional
  "dedication": "",                     optional, its own page after the cover
  "size": "a5",                         "a5" (portrait 148x210 mm) or "square" (210x210 mm)
  "font": "Fredoka",                    a Google Fonts family name, see FONTS below
  "font_file": "",                      optional local .ttf/.otf to embed instead (works offline)
  "text_size": "large",                 "large" (first readers), "medium", "small"
  "cover_image": "art/cover.png",       optional
  "pages": [
    {"text": "...", "image": "art/p1.png", "layout": "image-top"}
  ],
  "credits": ["ניקוד: ..."],             optional lines for the back cover
  "back_text": ""                       optional blurb for the back cover
}
layout: image-top (default), image-bottom, image-full (text on a band over the picture),
text-only. A page without an image gets an empty frame (or a "draw here" frame with --draw-frames).

Usage:
  python3 make_storybook.py story.json --out book.html
  python3 make_storybook.py story.json --out booklet.html --booklet      (A5 only: A4 sheets to fold)
  python3 make_storybook.py story.json --out book.html --embed-images    (one self-contained file)
  python3 make_storybook.py story.json --out book.html --bleed 3         (print-shop bleed, mm)
"""

import argparse
import base64
import html
import json
import mimetypes
import os
import sys
import unicodedata

# Families checked on 2026-11-17 for every niqqud codepoint (U+05B0-U+05BC, U+05C1,
# U+05C2, U+05C7) and for GPOS mark positioning in the Hebrew script. All are OFL.
FONTS = {
    "Fredoka": "rounded, friendly",
    "Noto Sans Hebrew": "clean print letters, the safest choice for first readers",
    "Frank Ruhl Libre": "classic book serif",
    "Assistant": "plain sans",
    "Varela Round": "rounded",
    "David Libre": "traditional serif",
}
TEXT_SIZES = {"large": ("22pt", 25), "medium": ("17pt", 50), "small": ("14pt", 90)}
SIZES = {"a5": (148, 210), "square": (210, 210)}
NIQQUD = [chr(c) for c in range(0x05B0, 0x05BD)] + ["ׁ", "ׂ", "ׇ"]


def safe_path(base_dir, rel):
    """Resolve a path from story.json and refuse anything outside the story's folder."""
    base = os.path.realpath(base_dir)
    full = os.path.realpath(os.path.join(base, rel))
    if os.path.commonpath([base, full]) != base:
        sys.exit(f"ERROR: {rel} is outside the story folder. Put pictures and fonts next to story.json.")
    return full


def esc(s):
    return html.escape(s or "", quote=True)


def para(text):
    lines = [esc(x) for x in (text or "").strip().split("\n")]
    return "<br>".join(lines)


def image_src(path, base_dir, embed):
    if not path:
        return None
    if path.startswith(("http://", "https://")):
        sys.exit(f"ERROR: image {path} is a web address. Download it next to the story file first.")
    full = safe_path(base_dir, path)
    if not os.path.exists(full):
        print(f"WARNING: image not found: {full} (the page will show an empty frame)", file=sys.stderr)
        return None
    if not embed:
        return path
    mime = mimetypes.guess_type(full)[0] or "image/png"
    with open(full, "rb") as f:
        return f"data:{mime};base64," + base64.b64encode(f.read()).decode("ascii")


def check_font_file(font_file, text):
    """If fontTools is installed, confirm the font covers every character in the book."""
    try:
        from fontTools.ttLib import TTFont  # optional
    except ImportError:
        print("NOTE: fontTools not installed, skipping the font coverage check "
              "(pip install fonttools to enable it).", file=sys.stderr)
        return
    cmap = TTFont(font_file).getBestCmap()
    needed = {ch for ch in text if not ch.isspace()}
    missing = sorted(ch for ch in needed if ord(ch) not in cmap)
    if missing:
        names = ", ".join(f"U+{ord(c):04X} {unicodedata.name(c, '?')}" for c in missing)
        sys.exit("ERROR: the font is missing characters used in the book. The browser would borrow "
                 f"them from another font letter by letter and the niqqud would break: {names}")
    print(f"font check: {os.path.basename(font_file)} covers all characters in the book", file=sys.stderr)


def font_css(story, base_dir):
    family = story.get("font") or "Noto Sans Hebrew"
    ff = story.get("font_file")
    if ff:
        full = safe_path(base_dir, ff)
        with open(full, "rb") as f:
            data = base64.b64encode(f.read()).decode("ascii")
        fmt = "opentype" if full.lower().endswith(".otf") else "truetype"
        return family, "", (f"@font-face{{font-family:'BookFont';src:url(data:font/{fmt};base64,{data}) "
                            f"format('{fmt}');}}"), "'BookFont'"
    if family not in FONTS:
        print(f"WARNING: font '{family}' is not on the checked list ({', '.join(FONTS)}). "
              "Make sure it has every niqqud mark, or pass font_file.", file=sys.stderr)
    link = ("<link rel=\"stylesheet\" href=\"https://fonts.googleapis.com/css2?family="
            + family.replace(" ", "+") + ":wght@400;700&amp;display=block\">")
    return family, link, "", f"'{family}'"


def page_html(inner, cls=""):
    return f'<section class="page {cls}">{inner}</section>'


def frame(src, draw):
    if src:
        return f'<div class="art" style="background-image:url(&quot;{esc(src)}&quot;)"></div>'
    label = '<span class="draw">ציירו כאן</span>' if draw else ""
    return f'<div class="art empty">{label}</div>'


def build_pages(story, base_dir, embed, draw):
    pages = []
    cover_src = image_src(story.get("cover_image"), base_dir, embed)
    cover = (frame(cover_src, False) if cover_src else "") + \
        f'<h1>{para(story.get("title"))}</h1>' + \
        (f'<p class="sub">{para(story.get("subtitle"))}</p>' if story.get("subtitle") else "")
    pages.append(page_html(cover, "cover"))
    if story.get("dedication"):
        pages.append(page_html(f'<p class="dedication">{para(story["dedication"])}</p>', "dedication"))
    for n, p in enumerate(story.get("pages", []), start=1):
        layout = p.get("layout", "image-top")
        src = image_src(p.get("image"), base_dir, embed)
        text = f'<div class="text">{para(p.get("text"))}</div>'
        num = f'<div class="folio">{n}</div>'
        if layout == "text-only":
            inner = text
        elif layout == "image-bottom":
            inner = text + frame(src, draw)
        elif layout == "image-full":
            inner = frame(src, draw) + f'<div class="band">{para(p.get("text"))}</div>'
        else:
            inner = frame(src, draw) + text
        pages.append(page_html(inner + num, layout))
    back = ""
    if story.get("back_text"):
        back += f'<p class="blurb">{para(story["back_text"])}</p>'
    if story.get("credits"):
        back += '<div class="credits">' + "<br>".join(esc(c) for c in story["credits"]) + "</div>"
    pages.append(page_html(back, "back"))
    return pages


def impose_rtl(pages):
    """Saddle-stitch imposition for a book bound on the RIGHT.

    Pages are padded with blanks to a multiple of 4 (the back cover stays last).
    Each sheet has an outside face [left, right] = [1+2k, n-2k] and an inside face
    [n-2k-1, 2+2k], 1-based, sheet k counted from the outermost sheet.
    """
    blank = page_html("", "blank")
    pages = list(pages)
    while len(pages) % 4:
        pages.insert(len(pages) - 1, blank)
    n = len(pages)
    sides = []
    for k in range(n // 4):
        sides.append((pages[2 * k], pages[n - 2 * k - 1]))           # outside: left, right
        sides.append((pages[n - 2 * k - 2], pages[2 * k + 1]))       # inside: left, right
    return sides, n


CSS = """
*{box-sizing:border-box;margin:0;padding:0}
html,body{background:#fff}
body{font-family:%(font)s,sans-serif;color:#1b1b1b;-webkit-print-color-adjust:exact;print-color-adjust:exact}
@page{size:%(page_size)s;margin:0}
.page{width:%(pw)smm;height:%(ph)smm;padding:%(pad)smm;display:flex;flex-direction:column;
 gap:6mm;overflow:hidden;position:relative;page-break-after:always;break-after:page}
.sheet .page{page-break-after:auto;break-after:auto}
.art{flex:1 1 auto;min-height:0;border-radius:4mm;overflow:hidden;display:flex;align-items:center;justify-content:center}
.art{background-size:cover;background-position:center;background-repeat:no-repeat}
.art.empty{border:0.4mm dashed #b8b8b8}
.draw{color:#9a9a9a;font-size:14pt}
.text{font-size:%(fs)s;line-height:2.0;text-align:center;flex:0 0 auto}
.image-full .art{position:absolute;inset:0;border-radius:0}
.band{position:absolute;inset-inline:%(pad)smm;bottom:%(pad)smm;background:rgba(255,255,255,.9);
 border-radius:4mm;padding:4mm 6mm;font-size:%(fs)s;line-height:2.0;text-align:center}
.text-only .text{margin:auto}
.folio{position:absolute;bottom:8mm;inset-inline-start:0;inset-inline-end:0;text-align:center;font-size:10pt;color:#777}
.image-full .folio{display:none}
.cover{justify-content:center}
.cover h1{font-size:30pt;line-height:1.7;text-align:center}
.cover .sub{font-size:16pt;text-align:center}
.cover .art{max-height:120mm}
.dedication{margin:auto;font-size:16pt;line-height:2;text-align:center}
.back{justify-content:flex-end;text-align:center}
.blurb{font-size:14pt;line-height:2;margin-bottom:auto;margin-top:20mm}
.credits{font-size:8.5pt;color:#555;line-height:1.6}
.sheet{width:297mm;height:210mm;display:flex;flex-direction:row;direction:ltr;page-break-after:always;break-after:page}
.sheet .page{width:148.5mm;height:210mm;direction:rtl}
@media screen{body{background:#eee}.page,.sheet{margin:6mm auto;background:#fff;box-shadow:0 1px 4px #0003}}
"""


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("story")
    ap.add_argument("--out", required=True)
    ap.add_argument("--booklet", action="store_true", help="A5 book imposed on A4 landscape sheets, bound on the right")
    ap.add_argument("--embed-images", action="store_true")
    ap.add_argument("--draw-frames", action="store_true", help='empty frames say "ציירו כאן"')
    ap.add_argument("--bleed", type=float, default=0.0, help="extra mm on every edge for a print shop")
    args = ap.parse_args()

    with open(args.story, encoding="utf-8") as f:
        story = json.load(f)
    base_dir = os.path.dirname(os.path.abspath(args.story))
    for k in ("title", "subtitle", "dedication", "back_text"):
        if story.get(k):
            story[k] = unicodedata.normalize("NFC", story[k])
    for p in story.get("pages", []):
        p["text"] = unicodedata.normalize("NFC", p.get("text", ""))

    size = story.get("size", "a5")
    if size not in SIZES:
        sys.exit(f"ERROR: size must be one of {list(SIZES)}")
    if args.booklet and size != "a5":
        sys.exit("ERROR: --booklet works with size a5 only (two A5 pages per A4 sheet).")
    if args.booklet and args.bleed:
        sys.exit("ERROR: bleed is for a print shop file, not a home booklet. Drop one of the two flags.")

    fs, max_words = TEXT_SIZES.get(story.get("text_size", "large"), TEXT_SIZES["large"])
    all_text = " ".join([story.get("title", ""), story.get("dedication", ""), story.get("back_text", "")]
                        + [p.get("text", "") for p in story.get("pages", [])])
    for n, p in enumerate(story.get("pages", []), start=1):
        words = len(p.get("text", "").split())
        if words > max_words:
            print(f"WARNING: page {n} has {words} words, more than the {max_words} this text size fits well. "
                  "Split the page or use a smaller text_size.", file=sys.stderr)
    if story.get("font_file"):
        check_font_file(safe_path(base_dir, story["font_file"]), all_text)
    if not any(ch in all_text for ch in NIQQUD):
        print("NOTE: the text has no niqqud. Fine for a read-aloud book; a first reader needs it.", file=sys.stderr)

    family, link, face, stack = font_css(story, base_dir)
    pw, ph = SIZES[size]
    pw, ph = pw + 2 * args.bleed, ph + 2 * args.bleed
    pad = 12 + args.bleed
    page_size = "A4 landscape" if args.booklet else f"{pw}mm {ph}mm"
    css = CSS % {"font": stack, "page_size": page_size, "pw": pw, "ph": ph, "pad": pad, "fs": fs}

    pages = build_pages(story, base_dir, args.embed_images, args.draw_frames)
    if args.booklet:
        sides, n = impose_rtl(pages)
        # .sheet is direction:ltr so the first child really is the LEFT half
        body = "".join(f'<div class="sheet">{left}{right}</div>' for left, right in sides)
        print(f"booklet: {n} pages on {n // 4} A4 sheet(s). Print double-sided at actual size (no fit-to-page), "
              "then fold and staple on the fold.", file=sys.stderr)
    else:
        body = "".join(pages)
        print(f"book: {len(pages)} pages, {size}", file=sys.stderr)

    doc = (f'<!doctype html><html lang="he" dir="rtl"><head><meta charset="utf-8">'
           f'<title>{esc(story.get("title", "ספר"))}</title>{link}<style>{face}{css}</style></head>'
           f'<body>{body}</body></html>')
    with open(args.out, "w", encoding="utf-8") as f:
        f.write(doc)
    print(f"wrote {args.out}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
