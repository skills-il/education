# Printable book template (no script needed)

For hosts that cannot run `scripts/make_storybook.py`. Fill this in, give it to the parent as
a file named `book.html` (or as text to save under that name), and have them open it in Chrome
or Edge, then Print, destination "Save as PDF" (or a printer), Margins "None", Scale 100, and
"Background graphics" on.

How to fill it:

- One `<section class="page">` per page, in reading order. The cover is first, the back cover
  last. The browser prints them in this order; a Hebrew book opens from the right, which the
  `dir="rtl"` on the page takes care of.
- Put the vocalized text exactly as checked. Do not retype niqqud.
- Pictures: save them next to `book.html` in a folder `art/` and point each page at its file.
  A page without a picture keeps an empty frame (or write ציירו כאן in it, and the child draws).
- Fonts: the link loads Noto Sans Hebrew from Google Fonts when the file is opened (needs
  internet once). Other checked fonts with full niqqud: Fredoka, Frank Ruhl Libre, Assistant,
  Varela Round, David Libre. Change the family name in both places.
- Square book: change `148mm 210mm` to `210mm 210mm` and the `.page` width and height to match.
- Text size: `22pt` suits a first reader; use `17pt` for a read-aloud book.

```html
<!doctype html>
<html lang="he" dir="rtl">
<head>
<meta charset="utf-8">
<title>שם הספר</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Noto+Sans+Hebrew:wght@400;700&display=block">
<style>
  * { box-sizing: border-box; margin: 0; padding: 0; }
  body { font-family: 'Noto Sans Hebrew', sans-serif; color: #1b1b1b;
         -webkit-print-color-adjust: exact; print-color-adjust: exact; }
  @page { size: 148mm 210mm; margin: 0; }
  .page { width: 148mm; height: 210mm; padding: 12mm; display: flex; flex-direction: column;
          gap: 6mm; position: relative; overflow: hidden; break-after: page; }
  .art { flex: 1 1 auto; border-radius: 4mm; background-size: cover; background-position: center; }
  .art.empty { border: 0.4mm dashed #b8b8b8; display: flex; align-items: center; justify-content: center; color: #999; }
  .text { font-size: 22pt; line-height: 2; text-align: center; }
  .folio { position: absolute; bottom: 8mm; left: 0; right: 0; text-align: center; font-size: 10pt; color: #777; }
  .cover { justify-content: center; text-align: center; }
  .cover h1 { font-size: 30pt; line-height: 1.7; }
  .back { justify-content: flex-end; text-align: center; font-size: 9pt; color: #555; }
  @media screen { body { background: #eee; } .page { margin: 6mm auto; background: #fff; } }
</style>
</head>
<body>

<section class="page cover">
  <div class="art" style="background-image:url('art/cover.png')"></div>
  <h1>נוֹעָה וְהַדִּינוֹזָאוֹר הַקָּטָן</h1>
</section>

<section class="page">
  <div class="art" style="background-image:url('art/p1.png')"></div>
  <div class="text">נוֹעָה אוֹהֶבֶת דִּינוֹזָאוֹרִים.</div>
  <div class="folio">1</div>
</section>

<section class="page">
  <div class="art empty">ציירו כאן</div>
  <div class="text">...</div>
  <div class="folio">2</div>
</section>

<section class="page back">
  <p>ניקוד: ...<br>גופן: Noto Sans Hebrew, ברישיון SIL Open Font License</p>
</section>

</body>
</html>
```

## A folded booklet without the script

A Hebrew booklet is bound on the right, so the pages go onto A4 landscape sheets in a fixed
order. Do not use the printer's own booklet mode: it usually binds on the left, and the story
then runs backwards when folded.

1. Count the pages including the cover and the back cover. If the count does not divide by 4,
   add empty pages just before the back cover.
2. The numbers below are physical pages: the cover is page 1, the dedication (if any) page 2,
   and so on to the back cover. They are not the folios printed on the story pages.
   With N pages, sheet k (k = 1 for the outermost sheet) has an outside face with page
   2k-1 on the LEFT half and page N-2k+2 on the RIGHT half, and an inside face with page
   N-2k+1 on the LEFT and page 2k on the RIGHT.

| Pages | Sheet | Outside face (left, right) | Inside face (left, right) |
|---|---|---|---|
| 8 | 1 | 1, 8 | 7, 2 |
| 8 | 2 | 3, 6 | 5, 4 |
| 12 | 1 | 1, 12 | 11, 2 |
| 12 | 2 | 3, 10 | 9, 4 |
| 12 | 3 | 5, 8 | 7, 6 |
| 16 | 1 | 1, 16 | 15, 2 |
| 16 | 2 | 3, 14 | 13, 4 |
| 16 | 3 | 5, 12 | 11, 6 |
| 16 | 4 | 7, 10 | 9, 8 |

3. Change the page CSS to A4 landscape and wrap each face in a sheet that holds two pages:

```html
<style>
  @page { size: A4 landscape; margin: 0; }
  .sheet { width: 297mm; height: 210mm; display: flex; direction: ltr; break-after: page; }
  .sheet .page { width: 148.5mm; height: 210mm; direction: rtl; break-after: auto; }
</style>

<!-- sheet 1, outside face of an 8-page book: page 1 (cover) on the left, page 8 (back) on the right -->
<div class="sheet">
  <section class="page cover">...</section>
  <section class="page back">...</section>
</div>
<!-- sheet 1, inside face: page 7 on the left, page 2 on the right -->
<div class="sheet">
  <section class="page">... page 7 ...</section>
  <section class="page">... page 2 ...</section>
</div>
```

`direction: ltr` on the sheet is what puts the first page in the code on the LEFT; without it the
right-to-left page flips every pair.

4. Print the first sheet double-sided as a test (usually "flip on short edge"): page 2 must sit
   behind the cover, the right way up. If not, switch the flip setting. A printer without
   double-sided printing: print the odd PDF pages, turn the stack over into the tray, print the
   even pages; if the backs land on the wrong sheets, print the even pages in reverse order.
   Fold, nest the sheets in order, staple on the fold.
