---
name: hebrew-treasure-hunt-maker
description: "Make a personalized Hebrew treasure hunt or home escape room for your kids, ready to print: riddles fitted to each child's reading level and gender, a route through your rooms, cut-out clue cards, a host answer sheet, a hint ladder and a certificate. Hiding places and prizes come from short closed menus, set by the youngest child in the home. Also flags some riddle wording, Hanukkah dates and Shabbat limits. An adult reads every card, walks the route first and stays with the children. Use when a parent asks for a treasure hunt, escape room, clue game, afikoman hunt or birthday or holiday riddle game at home. Helps avoid clues on balconies or in appliances, choking-hazard prizes and candle risks. Do NOT use for a personalized story book (use hebrew-kids-story-maker), classroom worksheets, classroom or school-group games, standalone riddles with no game, outdoor or public hunts, commercial party businesses, first aid or medical advice."
license: MIT
---

# Hebrew Treasure Hunt Maker

## Legal notice

An adult reads every card, walks the route first and stays with the children.

Use at your own risk. This tool is not a substitute for advice from a qualified professional.

## Problem

Parents want a treasure hunt built around their own kids and home. AI assistants write charming riddles, but they also send a 6-year-old to the balcony, hide a card on top of the fridge, put the treasure by the lit hanukkiyah, print the answer inside the riddle, and fill the prize bag with things a visiting toddler can choke on. This skill limits places and prizes to short menus and checks the plan before anything is printed.

## Instructions

Reply in the parent's language. Most parents are not technical: never show them JSON, commands, menu IDs or check codes. Say "I checked" only about checks that actually ran.

### Step 1: Two stages: the kit in the first reply, the printable file after

**Stage 1, the first reply.** When the message says who is playing, write the whole kit in the reply: route, riddles for each child, hint ladder, host sheet and siren line. Follow the pre-send pass in Step 6 by hand. State in one line which details you assumed, handle them conservatively in the plan itself (table below), and **say plainly that the automatic check has not run**. End by inviting a correction. Never end the reply with only questions.

**Stage 2, the printable kit through the script.** On a host with a shell, the checker and builder run only on the parent's real answers. **Never fill a checker field with an assumed value to make it pass.** If a required field is missing, ask for just those fields at this point, after the parent already has the kit in the reply. See Step 7.

**Ages are never invented.** Ask first, in one short round, only when nobody's age or who is playing is known.

Do not ask for last names, addresses, school names or photos, and say a nickname works fine. Never ask for the names of children who are not playing: their ages are enough.

| Detail | If the parent did not say, in the first reply |
|---|---|
| A child's age, when others are known | Do not guess a number. Treat that child as possibly under 3 for prizes and possibly under 6 for the adult-presence rule, and an adult reads their card |
| **How to address each child in Hebrew** | Use the child's name or a neutral plural form. Never infer gender from a name: נועם, טל, עדי and שי are given to everyone |
| How well each child reads | An adult reads the cards aloud |
| **Anyone younger or any guests in the home** | A younger child might be present: the prize is a large book, a large soft toy without small parts, or the certificate alone. No food and no small parts |
| Whether a child of 3 or 4 still puts things in the mouth | Treat it as yes |
| Rooms, and whether there is a mamad | Use the menu rooms the parent named, or the kids' room if none. **No station in the mamad unless the parent confirmed that nothing breakable is in it and the way stays clear. Otherwise route through other rooms.** In the first reply, no bed spot unless the parent confirmed the bed is low and not a bunk. The siren line names the protected space, and you invite a family with no mamad to say where they go |
| Date, time, occasion | Leave the date blank. Never write a date or year the parent did not give |
| **Whether the family keeps Shabbat and festivals** | If an observant family's timing is unclear, or you do not know and the date may be Friday evening, Shabbat or a festival, plan a game that needs: everything placed in advance, no writing, cutting, sticking, phone or timer, no stickers or coloring book, and the same treasure for everyone. Do not tell the parent that the game suits Shabbat. For a family you know is observant, defer to their rabbi. When observance is unknown and the date is unknown, a Friday, Shabbat or a festival, the host sheet carries this line next to the siren line: "משפחה ששומרת שבת: לגבי כיבוי בשבת שואלים מראש את הרב של המשפחה." Keep it off an ordinary weekday and off a reply to a family that said it does not keep Shabbat. Never tell anyone to put out candles on Shabbat as a flat instruction |
| **Candles during the game** | Keep stations and treasure away from any candles: out of the living room and dining area. If those are the only rooms, the host sheet says to play only before lighting or after the candles are out. If the date is unknown or in Hanukkah, the host sheet also says not to play while anyone is frying |
| **How many adults stay** | Plan for one. So with possible candles, the host sheet says to play before lighting or after the candles are out. With guests and a child under 6 or of unknown age, keep the game in one room |

These assumptions shape the plan in the reply and never go into a checker field. They never loosen a limit: refused places and prizes, the adult-presence rule and the siren line stay as they are.

### Step 2: Build the route from the menus

Every station is one room and one spot from these lists, and nothing else. The menus are this skill's own design choice, not a rule from any source.

**Rooms:** living room, dining area, kids' room, second kids' room, bedroom, study, mamad. The kitchen, balcony, bathroom, laundry, storage, hallway, stairs and anything outside the apartment are not on the menu. If the parent names one, say you left it out and move that stop to a menu room. An unusual room either maps to a menu room or the station is dropped.

**Spots:** under a sofa cushion; on the rug; on the floor in the room corner; under the table, on the floor (not under a desk in the study, where cables sit); under a chair, on the floor; on the bottom bookshelf; inside an open toy basket on the floor; under the blanket on a low bed (the parent confirms it is not a bunk, and with more than one child you say whose bed); beside a large soft toy on the floor.

In an escape room, a box or an envelope may sit at one of these spots. "Locks" are pretend codes on a box or envelope. No door is ever locked or shut, and children can walk out at any moment.

- **The youngest person present sets the level**, including guests and toddlers who are not playing. List each child separately, so a pair or team can never hide a younger child's age.
- The mamad can be a station if the way stays clear, nothing breakable is added and its door stays out of the game.
- **If candles will be lit, no station goes in that room, and one adult stays with them.** That adult does not count as supervising the children: if nobody else is there, offer to play before lighting or after the candles are out. For a family that keeps Shabbat, a hunt after candle lighting on Friday or a festival eve counts as candles lit. The living room and dining area count as one space unless a wall separates them. Applying this to Shabbat and festival candles is this skill's inference from Hanukkah safety guidance.
- Rules and their sources: `references/safety-rules.md`.

For a mixed-age group, give each child their own riddle at every step, leading to the same place. The youngest solves first, whoever finishes does not tell, and an early finisher keeps the cards (common practice).

### Step 3: Pick prizes from the menu

| Prize | Allowed when the youngest present is |
|---|---|
| Large book, large soft toy without small parts, the certificate alone | Any age |
| Paper crown, sticker sheet, coloring book | 3 or older, and at 3 or 4 only if the child no longer mouths objects. No coloring or stickers on Shabbat or a festival |
| Large dreidel with a standards mark | 5 or older |
| Biscuit, pretzel, wafer, nut-free chocolate, nut-free chocolate coins (an adult peels them) | 5 or older |

**No food prizes at all when anyone under 5 is present.** This is the skill's own stricter choice. Anything off this menu is refused: ask the parent to pick from it. With guests, ask their parents about allergies before choosing food. Food is eaten sitting down, after the game.

### Step 4: Write the riddles

- Each riddle leads to the menu spot of the next station and is solvable from the card. Build it from what the child loves.
- **Never print the answer**, not with a prefix, in another spelling, inside a longer word, as a synonym, reversed or spelled out letter by letter.
- A child who just started reading gets about 6 to 8 familiar words per card (the skill's default). A pre-reader never has to read: use a card an adult reads aloud, or a picture of the destination.
- Never suggest a dangerous action in a riddle or hint: no climbing, standing on furniture, jumping, tasting, lighting, hiding inside anything, leaving the home, shutting a door, moving furniture, or "look where the fire lives". A holiday word is fine in a story line ("I am not a candle"), as long as the card does not send a child toward it.
- Each clue has three hints: a nudge, a stronger hint, and the answer with why. Only the third states the answer.
- Reading stages, puzzle types by age and the gender table: `references/reading-stages.md`.

### Step 5: Niqqud from Dicta, and the calendar

Language models vocalize Hebrew unreliably, so do not vocalize cards yourself. Follow `references/niqqud-routes.md`: Dicta's open model where a shell exists, the Nakdan website pasted by the parent otherwise, or an adult-read card. For grade 1, apply `scripts/niqqud_tools.py adapt --stage grade1`. Read the output: the model makes mistakes, and rewording a riddle is safer than hand-editing marks.

Run `python3 scripts/check_hunt.py --dates <year>`, or read Hebcal on a host without code. When the parent gave a date, state Hanukkah dates with the year. Without a date, write no year. For a family that keeps Shabbat and festivals, follow `references/calendar-shabbat.md`: on those days, switch to Shabbat mode as a planning default from the cited source, and say the family's rabbi decides. For a family that does not, apply none of this and do not bring it up.

### Step 6: Mandatory pre-send pass (every host)

Before you send a kit, go through this list. In the first reply this **is** the check, on every host, so do it line by line, fix what fails, and never say a script ran.

1. **Youngest person present**, guests and babies included. Write the age. If the parent did not rule out younger children, write "a younger child may be present" and treat the youngest as possibly under 3 for prizes. A child of unknown age counts as possibly under 3 for prizes and possibly under 6 for the adult-presence rule.
2. **Each station** is one menu room plus one menu spot. Replace anything else and tell the parent what you replaced. In the first reply, a mamad station needs the parent's confirmation that nothing breakable is in it and the way stays clear. The heavy door stays out of the game, and the host sheet states all three conditions. In the first reply, no bed spot unless the parent confirmed the bed is low and not a bunk. When stations are in the kids' room, the host sheet carries: "אם חדר הילדים הוא גם הממ"ד: שומרים על דרך פנויה, לא מכניסים אליו שום דבר שביר, והדלת הכבדה לא חלק מהמשחק."
3. **Each prize** is on the menu for that age. With anyone under 5, no food. If a child under 3 may be present, only a large book, a large soft toy without small parts or the certificate alone, so chocolate coins, dreidels, stickers and other restricted items are out.
4. **Read every riddle and hint yourself.** Name the one place it leads to, which must be the next station. It does not contain its answer, name a place off the menu, or ask for a dangerous action.
5. **The hint ladder is actually in the kit**: for each child and step, hint 1, hint 2, then the answer with why.
6. **The siren line is in the host guide**, word for word: "עוצרים את המשחק ונכנסים מיד למרחב המוגן. אם יש זמן ורק אם זה לא מעכב אתכם, מכבים בדרך כיריים, תנור, תנורי חימום ונרות." With no protected space, name the place the family gave you. If the family is observant, or observance is unknown and the date is unknown, a Friday, Shabbat or a festival, add right after it: "משפחה ששומרת שבת: לגבי כיבוי בשבת שואלים מראש את הרב של המשפחה."
7. **Say how the niqqud was made** (Dicta's model, the Nakdan website, or "an adult reads aloud"). If it did not come from Dicta, do not print self-made niqqud.
8. **Candles:** if any will be lit, no station or treasure is in that room or a space open to it, and a second adult is with the children. If candles are unknown, apply the same check to the living room and dining area, and print on the host sheet itself: "משחקים לפני ההדלקה או אחרי שהנרות כבו." If the date is unknown or in Hanukkah, also print there: "לא משחקים בזמן טיגון."
9. **Observant family on Shabbat or a festival:** the kit defers to the family's rabbi in words, and any player aged 12 or older is sent to ask the rabbi first.
10. **With guests or several rooms:** the kit carries the headcount, closed-front-door and adults-present lines (common practice). With guests, a child under 6 or of unknown age, and one adult, keep the game in one room or add an adult.
11. **The host guide tells the adult to read every card before hiding it.**
12. **The first reply contains the whole kit:** route, riddles for each child, hint ladder and host sheet, with your assumptions in one line at the top, a plain statement that the automatic check has not run, and an invitation to correct them at the end. It does not end with only questions.

### Step 7: Validate and build (hosts with a shell)

```bash
python3 scripts/check_hunt.py hunt/hunt.json
python3 scripts/build_kit.py hunt/hunt.json --out kit.html
```

This is stage 2. Write `hunt/hunt.json` per `references/hunt-schema.md`, in its own folder, using only the parent's real answers. If a required field is missing, ask for just those fields, and never fill one with an assumed value. Fix every error and run the check again. Never edit the data just to silence an error. The builder refuses to build while an error remains. The scan of card text is advisory: a clean result does not mean a card is fine, which is why Step 6 line 4 stays mandatory.

Render a PDF from the HTML with a browser (Print, Save as PDF, at 100 percent). If you can, look at the pages and trace the RTL order, niqqud, cut lines and hints.

**On a host without a shell** (claude-ai, chatgpt, manus, grok, claude-desktop without a local tool), there is no stage 2 and Step 6 is the check. Build the kit in the reply or as a document, following `references/manual-route.md`, and state that the automatic check did not run.

### Step 8: Hand over

Give the parent the file and a short note:

- What you changed for safety and why, in plain words.
- What was checked, and what was not: **nobody has seen your home. An adult reads every card, walks the route first and stays with the children until the end.** Never call the hunt "safe".
- The automatic scan of card text is partial and will not catch every wording.
- The host guide has the siren rule and emergency numbers (101, 102, poison center 04-7771900).
- With guests: ask their parents about allergies, and do not post photos of other people's children without their parents' consent.

## Examples

### Example 1: Hanukkah hunt, two ages

User says: "I'm mom to Noa (6, first grade, just started reading) and Itai (9). I want a Hanukkah treasure hunt. We have a living room, kitchen, mamad, kids' room and balcony. Noa loves cats, Itai loves football. 6 stations, one PDF."

Actions: open with one line: "I assumed a younger child may be around, one adult stays, and you will play before lighting or after the candles are out. I left the mamad out until you confirm that nothing breakable is in it and the way stays clear. The automatic check has not run." Leave the balcony and kitchen out. Because candles may be lit, keep the living room out too, so all the stations and the treasure are in the kids' room. The prize is a large book. Plan a game that needs everything placed in advance and no writing, cutting, sticking, phone or timer. Write paired riddles, with Dicta niqqud and the grade 1 profile for Noa, or cards an adult reads aloud if Dicta is not available. The host sheet carries a blank date line, the siren line, and, because observance and the date are unknown, the line "משפחה ששומרת שבת: לגבי כיבוי בשבת שואלים מראש את הרב של המשפחה." It also prints "משחקים לפני ההדלקה או אחרי שהנרות כבו.", "לא משחקים בזמן טיגון." and "אם חדר הילדים הוא גם הממ"ד: שומרים על דרך פנויה, לא מכניסים אליו שום דבר שביר, והדלת הכבדה לא חלק מהמשחק." Write the whole kit in this reply, and end by inviting a correction.

Result: the whole kit in the first reply (route, riddles, hint ladder, host sheet with the siren, candle and frying lines), a note saying the balcony and kitchen were replaced, and an invitation to correct any assumption. The PDF comes from the script after the parent gives the missing answers.

### Example 2: Birthday with a toddler sibling

User says: "Escape room for my son's 8th birthday, 5 friends, his little sister is 2. Prizes are marbles and balloons."

Actions: open with one line: "I assumed one adult stays, so the game is in the kids' room, away from any candles, and an adult reads the friends' cards because I don't have their ages. The automatic check has not run." The youngest present is 2, so marbles and balloons are off the menu, and the prize is a large book or a soft toy without small parts. The friends' ages are unknown, so they count as possibly under 6 and the game stays in one room. No locked doors. The date is unknown, so plan a game that needs everything placed in advance and no writing, cutting, sticking, phone or timer. The host sheet carries a blank date line, the siren line, the line "משפחה ששומרת שבת: לגבי כיבוי בשבת שואלים מראש את הרב של המשפחה.", and the lines "משחקים לפני ההדלקה או אחרי שהנרות כבו.", "לא משחקים בזמן טיגון." and "אם חדר הילדים הוא גם הממ"ד: שומרים על דרך פנויה, לא מכניסים אליו שום דבר שביר, והדלת הכבדה לא חלק מהמשחק." Write the whole kit in this reply, and end by inviting a correction, such as a second adult or the friends' ages.

Result: a complete kit in the kids' room in the first reply, with the same prize for everyone and an invitation to correct the assumptions. The printable file comes after the parent gives the friends' ages and the number of adults.

### Example 3: Family that keeps Shabbat

User says: "We want a hunt on Shabbat afternoon of Hanukkah, we're observant."

Actions: switch to Shabbat mode. Everything is printed, cut and placed before Shabbat. No writing, cutting, timers or phones. Use spoken riddles. Everyone gets the same treasure. Cite Peninei Halakha, which speaks of children below mitzvah age and is stricter for older players, and defer to the family's rabbi. Send any player aged 12 or older to ask the rabbi first.

Result: a kit that needs no writing or electricity during the game.

## Bundled Resources

### Scripts

- `scripts/check_hunt.py`: checks a hunt built from menu IDs (rooms, spots, prizes, protected space, candles, route, answers in riddles, reading level, gender forms, Shabbat and festivals, locks) and runs an advisory scan of card text. Exit 0 clean, 1 errors, 2 could not check. `--dates <year>` prints the Hanukkah nights and `--menus` prints the menus. Run: `python3 scripts/check_hunt.py hunt/hunt.json`
- `scripts/build_kit.py`: builds the RTL A4 kit (host guide, answer sheet, hint ladder, clue cards, certificates) in grayscale-safe HTML, printing each place from its menu label. Refuses a hunt with errors. Run: `python3 scripts/build_kit.py hunt/hunt.json --out kit.html`
- `scripts/niqqud_tools.py`: applies the grade 1 niqqud profile and checks vocalized text. Run: `python3 scripts/niqqud_tools.py adapt --stage grade1 --in clues.txt --out clues_grade1.txt`

All three work offline, use only the Python standard library, and read and write only inside the hunt folder.

### References

- `references/safety-rules.md`: the menus and each rule with its source and how firm it is.
- `references/calendar-shabbat.md`: Hanukkah dates, Friday and Saturday order, festivals, Shabbat mode.
- `references/reading-stages.md`: niqqud by grade, puzzles by age, gender forms.
- `references/niqqud-routes.md`: how to get niqqud from Dicta on each host.
- `references/hunt-schema.md`: the hunt.json format.
- `references/manual-route.md`: the full path for hosts that cannot run scripts.

## Gotchas

- Agents treat the player list as the people in the home. A visiting 2-year-old changes which prizes are allowed even though they are not playing.
- Agents accept a parent's list of rooms as is. A balcony or kitchen on that list stays off the route.
- Agents treat appliances as ordinary hiding places. The CPSC notice documents hide-and-seek deaths in latch-type freezers, refrigerators, dryers and coolers, and an Israeli toddler died in a washing machine. It does not address modern fridges, so keeping every appliance out is this skill's stricter choice.
- Agents treat a birthday during Hanukkah as an ordinary day. The frying question follows the date, and the candle question is asked on any date.
- Agents write "Hanukkah 2026 starts on December 5" or put a Friday hunt "right after candle lighting". The first candle is Friday 4 December 2026 before sundown, and after candle lighting it is already Shabbat.
- Agents vocalize Hebrew themselves, adding the strong dagesh and shin dot that the Ministry guideline drops for grade 1.
- Agents infer gender from a name. Ask.

## Recommended MCP Servers

| Server | What it adds |
|---|---|
| `hebcal` (in the Skills IL MCP directory) | Holiday dates (`jewish-holidays-year`) and candle-lighting and Havdalah times for a city (`shabbat-times`). Optional: the skill works without it |

## Reference Links

| Source | URL | What to Check |
|---|---|---|
| Beterem, choking prevention | https://beterem.org/%D7%9E%D7%9E%D7%94-%D7%A0%D7%A4%D7%92%D7%A2%D7%99%D7%9D-%D7%99%D7%9C%D7%93%D7%99%D7%9D/%D7%9E%D7%A0%D7%99%D7%A2%D7%AA-%D7%97%D7%A0%D7%A7/ | Food and toy table by age |
| Beterem, Hanukkah safety | https://beterem.org/%D7%91%D7%97%D7%A0%D7%95%D7%9B%D7%94-%D7%A0%D7%A8%D7%99-%D7%99%D7%90%D7%99%D7%A8-%D7%9B%D7%9A-%D7%AA%D7%A9%D7%9E%D7%A8%D7%95-%D7%A2%D7%9C-%D7%99%D7%9C%D7%93%D7%99%D7%9B%D7%9D-%D7%91%D7%97%D7%92/ | Candles, frying, chocolate coins |
| Ministry of Health, Hanukkah safety | https://me.health.gov.il/parenting/raising-children/safe-environment/safety-during-the-holidays/safety-during-hanukkah/ | Coins, dreidels, batteries |
| Home Front Command, protected space | https://www.oref.org.il/heb/articles/the-protected-space/main/1503 | Keeping the way clear |
| Ministry of Education, niqqud guideline | https://meyda.education.gov.il/files/Mazkirut_Pedagogit/HebrewPrimary/learning-teaching/books/nikod.pdf | Niqqud by grade |
| Hebcal, Hanukkah | https://www.hebcal.com/holidays/chanukah-2026 | Dates, change the year |
| Peninei Halakha, games on Shabbat | https://ph.yhb.org.il/01-24-07/ | Writing and prizes |
| Privacy Protection Authority, sharing children's information | https://www.gov.il/he/pages/sharenting_for_parents1 | Photos of other children |

## Troubleshooting

### The parent wants a place or prize that is not on the menu

Cause: the menus are closed on purpose, and some limits are stricter than the sources (Beterem allows supervised balcony play, for example).
Solution: explain the reason once and offer the nearest menu item. The kit is not built with that item. A parent can of course run their own game differently, but this skill does not print it.

### The check reports an answer inside a riddle that looks unrelated

Cause: the check ignores vav and yod to catch more spellings, so a different word can collide with the answer. Common cases are already excluded (למטה, סיפור, מספר).
Solution: reword the riddle. It is a one-word change.

### Niqqud marks show as boxes or sit in the wrong place in the PDF

Cause: the browser fell back to a font without Hebrew marks.
Solution: rebuild with `--font-file` and a Hebrew font placed in the hunt folder, such as Noto Sans Hebrew.

### A grade 1 card fails with `NIQQUD_GRADE1`

Cause: the text kept marks the guideline drops.
Solution: run `niqqud_tools.py adapt --stage grade1` on the vocalized text and rebuild.
