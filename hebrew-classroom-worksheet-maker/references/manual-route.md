# Print template for hosts that cannot run scripts

Claude.ai, ChatGPT, Manus, Grok and Claude Desktop without a code tool cannot run the bundled scripts. The mandatory pre-send pass is in SKILL.md, Step 5. Do it first. This file only adds the printable page.

Say what happened: "לא הרצתי את הבדיקה האוטומטית. בדקתי ביד את הסעיפים שברשימה, וכדאי לקרוא את הדף לפני הצילום." Never write that a check "passed" or "ran".

Give the teacher one complete HTML file to open in a browser and print, or the sheet as text if the host cannot produce a file. Keep this structure.

```html
<!doctype html><html lang="he" dir="rtl"><head><meta charset="utf-8"><title>דף עבודה</title>
<style>
@page { size: A4; margin: 14mm 16mm; }
body { font-family: "Noto Sans Hebrew", Arial, sans-serif; font-size: 22pt; line-height: 1.6; color: #000; background: #fff; }
.page { break-after: page; } section { border: 1.2pt solid #000; border-radius: 3mm; padding: 3mm 4mm; margin-bottom: 4mm; break-inside: avoid; }
bdi.math { direction: ltr; unicode-bidi: isolate; font-family: Arial, sans-serif; white-space: nowrap; }
.blank { display: inline-block; min-width: 18mm; border-bottom: 1.4pt solid #000; height: 1em; }
</style></head><body>
<div class="page"><h1>כותרת</h1><p>שם: ________ &nbsp; תאריך: ________</p>
<section><h2>1. פִּתְרוּ</h2><p><bdi dir="ltr" class="math">3 + 2 = <span class="blank"></span></bdi></p></section></div>
<div class="page"><h1>דף תשובות למורים, לא לצילום לתלמידים</h1><p>1. <bdi dir="ltr" class="math">3 + 2 = 5</bdi></p>
<p>הדף הוכן בעזרת בינה מלאכותית. זה לא אישור של משרד החינוך. לפני הצילום קראו את הדף ובדקו את הניקוד.</p></div>
</body></html>
```

Put every math expression, in every part of the page, inside `<bdi dir="ltr" class="math">`. Repeat the name line on each student page. Print settings to tell the teacher: A4, no headers and footers, scale 100, then "שמירה כ-PDF" or print. Use black outlines only, and no emoji. Draw simple pictures as inline SVG with black strokes, and number each one so the key can refer to it.
