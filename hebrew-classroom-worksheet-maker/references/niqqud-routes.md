# Getting niqqud

Language models point Hebrew unreliably. Prefer Dicta, then apply the grade rule, then have a person read the page. If you point a short text yourself, say so on the key page.

| Route | Runs on | Terms |
|---|---|---|
| A. The Nakdan website, pasted by hand (nakdan.dicta.org.il) | Any host, any device | Dicta's terms: "Any use of our Services will be in accordance to Attribution-NonCommercial-ShareAlike 4.0 International Creative Commons license." That means noncommercial use, credit to Dicta, and ShareAlike. Sold sheets and paid teaching are outside this route unless the user confirms permission with Dicta |
| B. Dicta's open model `dictabert-large-char-menaked` | Agents with Python and PyTorch | "This work is licensed under a Creative Commons Attribution 4.0 International License". Credit Dicta. See the model card at https://huggingface.co/dicta-il/dictabert-large-char-menaked |
| C. Author-pointed short decodable text | Any host | For a few simple words. Tell the teacher it was not run through a nakdan |

To print the credit, set `niqqud_credit` in the worksheet, for example: "ניקוד: הנקדן של דיקטה, ברישיון CC BY-NC-SA 4.0". On the manual route, add the same line to the key page.

Never call the website from a script. Dicta's terms forbid access "using a method other than the interface and the instructions that we provide". Terms: https://dicta.org.il/tos and https://nakdan.dicta.org.il/terms-and-services

Text sent to Dicta is licensed to Dicta to run and improve its services, so never paste student names or details.

The model drops vowel letters by default, and is "not intended for earlier layers of Hebrew (e.g. Biblical, Rabbinic, Premodern), nor for poetic texts". Do not run verses, prayers or poems through it. Copy them in their original pointing.

After any route, for grade 1, apply the marks rule in `grade-rules.md`. It only removes marks. Never add or change a vowel.

What no script catches: the wrong word among words spelled alike (סֵפֶר or סָפַר). A person reads every page.
