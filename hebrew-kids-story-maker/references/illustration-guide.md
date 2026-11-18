# Illustrations: one character, every page, no text

## The character sheet

Consistency comes from repetition, not from the model remembering. Write one sheet per
recurring character and paste it word for word into every prompt where that character appears.

A good sheet fixes:

- age and build ("a 4-year-old girl, small for her age")
- hair: color, length, texture, style ("curly brown shoulder-length hair with a yellow clip")
- face and skin tone, described neutrally ("round face, light olive skin, brown eyes")
- one outfit for the whole book, with colors ("yellow raincoat, red rain boots")
- one signature item ("a small green dinosaur patch on the raincoat")

The parent chooses these. Never ask for, accept or describe a photo of the real child, and do
not try to make the character "look like" a real child; a recognizable likeness of a minor in
images sent to third-party tools is exactly what the book does not need. A pet or toy gets its
own short sheet (colors, shape, one detail).

Write the sheet and the scenes in English, even for a Hebrew book: the prompts go to the image
tool, and Hebrew words inside a prompt invite the model to draw Hebrew letters. Use words the
image model reads the Israeli way: כדורגל is "soccer" (many models draw "football" as the
American game), and a jersey or a ball is "plain", with no number or name.

## The style line

One line, fixed for the whole book: medium, palette, shapes, mood. For example "soft watercolor
picture-book illustration, warm pastel palette, rounded shapes, gentle evening light". Do not
name a studio, franchise or living artist ("in the style of ..."): describe the look instead.
That keeps the book clear of someone else's brand, which matters if it may ever be sold.

## No text in the picture

Image models break Hebrew letters and often mirror them. All words live in the layout, never
in the art. Every prompt ends with the no-text rule, and scenes avoid objects that carry
writing (signs, book covers, labels, birthday banners). If a scene needs a sign, make it
blank or seen from behind. Check every generated image for stray letters before using it.

## Composition

Tell the model where the text will sit: keep the lower or upper third calm (plain sky, floor,
wall) for an image-top or image-bottom page, or a calm strip along the bottom edge for a page
with a text band over the picture. Ask for one scene per page, the child clearly visible, and
the same side of the page for the main character across a spread when possible.

## Safety for young readers

- The worry in the story stays small, named and solved on the page, and the book ends safe and
  calm (bedtime books especially).
- No blood, weapons, injury, fire, drowning, death or medical procedures, unless the parent
  chose that theme on purpose (a hospital stay, a pet that died), and then shown gently.
- No peril to the parents, and no adult figure who is frightening.
- `build_prompts.py` flags writing words, quotations, Hebrew, photo or likeness requests,
  frightening words and studio names. Treat every flag as a question to resolve, not noise.

## Delivering the prompts

Give the parent one complete block per page, ready to paste: the style line, the full sheet of
every character in the scene, the scene, the composition note and the no-text rule. Do not hand
over the parts separately for the parent to combine; that is where the descriptions start to
drift. `build_prompts.py` produces exactly this.

Repeat the full sheet in every block, on every page, even when the reply gets long; a later
page is never just a scene line. Give every person who appears a sheet (parents, a baby). Keep
one outfit for the whole book, bedtime included, and put changes the story needs (a pregnancy,
a baby in someone's arms) in the scene line, not in an edited sheet. No sign or banner in the
picture, not even a blank one: a welcome line goes on the page as text.

## Generating

1. Generate the character reference sheet first and keep the image.
2. For each page, if the image tool accepts a reference image, attach the character sheet image
   with the page prompt. If it does not, the verbatim sheet text is what keeps the look stable.
3. Reject and regenerate any image with letters, extra fingers, a changed outfit or hair, or a
   frightening expression.
4. Hosts without image generation: deliver the prompts file. The parent pastes each block into
   any image tool, then saves the images as `art/p1.png`, `art/p2.png`, and so on.

## Using the pictures beyond the family

If the parent may print copies for sale or publish the book:

- Read the terms of the image tool that made the pictures. OpenAI's terms, for example, assign
  the output to the user "to the extent permitted by applicable law" and warn that output "may
  not be unique", so another user can receive a similar image.
- Ownership by contract is not copyright. The US Copyright Office concluded in January 2025
  that "prompts alone do not provide sufficient human control to make users of an AI system the
  authors of the output". Pictures made from prompts alone may not be protected, so others could
  copy them. The text the parent wrote, and real hand edits, are a different matter.
- The niqqud route decides too: text vocalized on the Nakdan website is NonCommercial (see
  `niqqud-routes.md`).
