# Menus, prizes and game rules

The youngest child PRESENT sets the level, including guests and toddlers who are not playing.

Label key: **Source** means an Israeli or official source says this. **Applied** means the skill applies a cited source to a hunt, and the source does not discuss hunts. **Skill's choice** means a design decision of this skill. **Practice** means common practice with no authoritative source. Present Practice items as suggestions, never as rules.

## Rooms and spots (Skill's choice)

Every station is one room ID and one spot ID. Free text is not accepted as a place. The menus are this skill's design. They are not taken from any source.

| `room_id` | Printed as |
|---|---|
| `living` | הסלון |
| `dining` | פינת האוכל |
| `kids_room` | חדר הילדים |
| `kids_room_2` | חדר הילדים השני |
| `bedroom` | חדר השינה |
| `study` | חדר העבודה |
| `mamad` | הממ"ד |

| `spot_id` | Printed as |
|---|---|
| `sofa_cushion` | מתחת לכרית בספה |
| `rug` | על השטיח |
| `floor_corner` | על הרצפה בפינת החדר |
| `under_table` | מתחת לשולחן, על הרצפה. Not in the study, where cables and power strips usually sit (Skill's choice) |
| `under_chair` | מתחת לכיסא, על הרצפה |
| `low_books` | על המדף התחתון של הספרים |
| `toy_basket` | בתוך סל צעצועים פתוח שעל הרצפה |
| `low_bed` | מתחת לשמיכה במיטה נמוכה. The parent confirms it is not a bunk, and with more than one child the station names whose bed |
| `big_toy` | ליד בובה גדולה על הרצפה |

An escape-room box or envelope is a `container` placed at one of these spots.

## Why common places are not on the menu

| Place | Basis | Label |
|---|---|---|
| Balcony, window, sill, railing, roof | Beterem: "נפילות הן הגורם המרכזי לאשפוז ילדים מהיפגעות". Beterem allows supervised balcony play, so excluding it is stricter, because a hunt splits adult attention | Applied |
| Washing machine, dryer, fridge, freezer, dishwasher, chest, cooler, suitcase, wardrobe | US CPSC on latch-type freezers, refrigerators, dryers and coolers: "the doors could not be easily pushed open from the inside", often during hide-and-seek. An Israeli toddler died in a washing machine during hide-and-seek (Jerusalem Post, 2019). No Beterem or Ministry of Health page covers entrapment, and the CPSC notice does not address modern fridges, so excluding all of them is this skill's stricter choice | Applied |
| Kitchen, stove, oven, kettle, urn, Shabbat hotplate, heaters | Beterem: "מרבית מקרי הכוויות של ילדים בבית, מתרחשות במטבח". Leaving the whole kitchen off the menu is stricter | Applied |
| Medicine, cleaning products, tablets, under the sink | Beterem: store them "בארון נעול או גבוה". Ministry of Health: "חומרי ניקוי הם סכנת הרעלה עבור ילדים וילדות בכל גיל" | Applied |
| High shelves, drawers, anything needing a stool or moving furniture | Beterem on furniture near windows, and escape-room design guidance against moving heavy furniture | Applied |
| Bath, toilet, shower, sink, bucket | Beterem: "ילדים עלולים לטבוע גם במים רדודים בעומק סנטימטרים בודדים" | Applied |
| String trails, cords, curtains | Beterem on keeping cords from babies. Applying it to older children is stricter | Applied |
| Knives, tools, glass, trash, plastic bags, outlets | No specific source read | Practice |
| Stairs, stairwell, building shelter, yard, street | Scope: this skill covers the inside of the home | Skill's choice |

## Candles

Asked on **any** date. If candles will be lit in the home during the game, no station goes in that room, and the living room and dining area count as one space unless a wall separates them (Skill's choice). One adult stays with the candles and does not count as supervising the children. If no other adult is there, the hunt is refused, with the option to play before lighting or after the candles are out (Skill's choice). For a family that keeps Shabbat, a hunt that runs after candle lighting on a Friday or festival eve counts as candles lit.

Beterem writes about Hanukkah: "אין להשאיר ילדים בסביבות נרות דולקים ללא השגחה". Extending this to Shabbat and festival candles is **this skill's inference**. No source was read on Shabbat candles and children's games.

## The protected space

The mamad **can** be a station. No source forbids play there, and Beterem even suggests "פינת משחקים בממ\"ד". Conditions:

- The way there stays clear. Home Front Command: "יש לוודא שהדרך אל המרחב המוגן פנויה ממכשולים".
- Nothing that can shatter or ignite is added. Home Front Command: "פריטים וחפצים שעלולים להתנפץ או להתלקח כמו זכוכית וקרמיקה".
- The heavy door is never part of the game (Applied).
- The host sheet carries a siren rule, and reaching shelter comes first. Home Front Command: "בעת קבלת התרעה (אזעקה), יש להיכנס למרחב מוגן מיטבי בהתאם לזמן ההתגוננות העומד לרשותנו". Beterem also lists turning off the stove, oven, heaters and Hanukkah candles before going ("בחורף חשוב לסגור תנורי חימום ובחנוכה לכבות את הנרות"). The kit keeps those items but only "if there is time and only if it does not delay you", a wording choice of this skill that puts the Home Front Command instruction first. On Shabbat, turning things off is a halachic question, so the kit tells observant families to ask their rabbi in advance and does not rule on it.
- With no protected space, the kit prints the place the family named.

## Prize menu

Anything off this menu is refused. The menu and its limits are the **skill's choice**. The sources behind particular limits are listed under it.

| `prize` ID | Printed as | Youngest present |
|---|---|---|
| `large_book` | ספר גדול | Any age |
| `big_soft_toy` | בובה רכה גדולה בלי חלקים קטנים (large soft toy without small parts) | Any age |
| `certificate_only` | התעודה בלבד | Any age |
| `paper_crown` | כתר נייר | 3+, and at 3 or 4 only if not mouthing |
| `sticker_sheet` | דף מדבקות | 3+, and at 3 or 4 only if not mouthing. Not on Shabbat or a festival |
| `coloring_book` | חוברת צביעה | 3+, and at 3 or 4 only if not mouthing. Not on Shabbat or a festival |
| `big_dreidel` | סביבון גדול עם תו תקן | 5+ |
| `biscuit`, `pretzel`, `wafer`, `nut_free_chocolate` | ביסקוויט, בייגלה, וופל, שוקולד בלי אגוזים | 5+ |
| `chocolate_coins` | מטבעות שוקולד בלי אגוזים (מבוגר מקלף) | 5+ |

- **No food at all when anyone under 5 is present. This is the skill's own stricter choice.** Beterem's food table is more detailed and allows some foods earlier, with conditions. The skill does not try to apply that table to a specific child.
- For 5 and up, the food items are ones Beterem's table lists with no age limit (biscuit, pretzel, wafers, nut-free chocolate). Eaten sitting down: "פעוטות המסוגלים לשבת, אוכלים אך ורק בישיבה ובהשגחת מבוגר" is the source's rule for toddlers, and the skill keeps it for everyone.
- **Dreidels and coins:** Ministry of Health: "ילדים וילדות מתחת לגיל 5: הרחיקו מהם סביבונים ומטבעות".
- **Small parts:** Ministry of Health on the surprise-egg capsule test for under 3. Beterem: "לאחר גיל 3, אם הילד נוטה עדיין להכניס חפצים לפה - אין לתת לו צעצועים קטנים". Stopping the mouthing question at 5 is the skill's choice.
- **Chocolate coins:** Beterem: peel the foil and bin it.
- **Not on the menu, with sources:** balloons (Beterem: "עד גיל 8 יש סכנת חנק"), magnets (Beterem and Ministry of Health, up to 5), button batteries (Ministry of Health on swallowing), snaps and firecrackers (Ministry of Health, Purim).
- **Guest allergies:** ask each parent before choosing food. The risk is recognized by the Ministry of Education. The specific steps are Practice.

## Game rules

- **An adult stays present.** Ministry of Health: "החוק במדינת ישראל קובע כי אסור להשאיר ילד מתחת לגיל 6 ללא השגחה ראויה". An older sibling helps but is not the responsible host.
- **No real locks, nobody shut in, a free way out.** "Locks" are boxes, envelopes or pretend codes. In the 2019 Koszalin escape-room fire, five girls at a birthday party had been "locked inside the room"; postmortems found carbon monoxide inhalation.
- **No darkness, fire, heat-reveal ink or restraints.**
- **Hint ladder:** a nudge, a stronger hint, then the answer with why. Early hints ask basic questions, and "Solutions should be the last resort".
- **Fair puzzles:** solvable from the card, and never printing the answer.
- **Photos of guests:** Privacy Protection Authority: "הימנעו מפרסום ברבים של מידע אישי על אודות ילדיהם של אחרים". Certificates carry a first name only.

## The card text scan is advisory

Card text is free Hebrew. The script scans it for some place words, unsafe verbs, locks and answers, but **it does not catch every wording**. For example, a riddle describing "the place where food stays cold" contains none of the listed words. So the adult reads every card before hiding it, and the agent names the one place each card leads to.

## Facilitation (Practice)

With guests or several rooms: count the children at the start, at each station and at the end, and keep the front door closed, with an adult answering it. With guests, a child under 6 and one adult across several rooms, keep the game to one room or add an adult. Keep a phone number for each guest's parent. The youngest solves first, nobody tells, early finishers get a job. Teams rather than elimination, the same prize for everyone, a clear start and stop signal, a quiet option for an overwhelmed child. For under-fives, keep each station short: the CDC says a child of about 5 "Pays attention for 5 to 10 minutes during activities".

## Holiday notes

- **Purim**: no cap guns, snaps or firecrackers. Masks need openings for nose, mouth and eyes (Ministry of Health).
- **Tu BiShvat**: nuts and dried fruit are the natural treasure and are not on the menu.
- **Passover**: the afikoman custom varies (a parent hides it, or the children do), so use neutral wording. Keep the hunt clear of cleaning products.
- **Hanukkah**: buy only dreidels with a standards mark. Homemade hanukkiyot are not for lighting. Children up to 9 light only with an adult. A smoke detector is recommended.

## Out of scope

First-aid instruction (route to 101 and the poison center), certifying a home as safe, installing childproofing, halachic rulings, legal advice on photos, judging whether a food is safe for a specific child, public or outdoor hunts, commercial party businesses, reading assessment.
