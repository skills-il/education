# Calendar and Shabbat

## Hanukkah dates

Never state a Hanukkah date from memory. Run `python3 scripts/check_hunt.py --dates <year>`, which computes the eight candle-lighting evenings from the arithmetic Hebrew calendar. Its first-night dates were compared with Hebcal for 2024 to 2031. On a host without code, read the year's page on Hebcal (`https://www.hebcal.com/holidays/chanukah-2026`, changing the year). Always write the year next to the date. A hunt in early January belongs to the Hanukkah that began in December, and the daytime after the eighth candle is still Hanukkah.

Worked example from Hebcal: "Chanukah for Hebrew Year 5787 begins at sundown on Friday, 4 December 2026 and ends at nightfall on Saturday, 12 December 2026."

| Night | Date | Lighting |
|---|---|---|
| 1 | Fri 4 Dec 2026 | Before sundown |
| 2 | Sat 5 Dec | At nightfall |
| 3 to 7 | Sun 6 to Thu 10 Dec | At dusk |
| 8 | Fri 11 Dec | Before sundown |
| none | Sat 12 Dec | Eighth day, no lighting that night |

In 2026 the first and last lightings both fall on a Friday, so the two most natural party nights are the most constrained for families who keep Shabbat.

Candle-lighting and Havdalah times depend on the city. Take them from Hebcal for the family's city, and ask only for the city, never an address.

## Friday and Saturday night order

From Peninei Halakha, Zmanim 13:5, cited as the source and not as this skill's ruling:

- Friday: "ובשבת חנוכה צריך להדליק נרות חנוכה לפני הדלקת נרות שבת."
- Saturday night: "במוצאי שבת, מתפללים ערבית תחילה, ואח\"כ מדליקים נרות חנוכה."
- Havdalah or candles first: families differ. "לשני המנהגים יש מקום בהלכה". Do not pick one.

A hunt timed "right after candle lighting" on a Friday lands inside Shabbat.

## Shabbat mode

Applies only when the parent says the family keeps Shabbat and the hunt falls on Shabbat or a festival. Never impose it on anyone else, and do not mention it to a family who said no.

Planning defaults, from one source (Peninei Halakha, Shabbat 24:7):

- The source speaks of children below mitzvah age, and says of joining letters "ואף שמבוגרים צריכים להחמיר בזה". The skill does not state the rule for older players: a player aged 12 or older is sent to ask the family's rabbi before the game.
- "כל משחק שכולל כתיבה או הדבקה או גזירה או קליעה אסור בשבת. אבל מותר לקטנים להרכיב פאזל או ליצור מילים על ידי חיבור אותיות זו לזו או על גבי לוח."
- A game where the winner gets a real prize of money or food: "אבל במשחק שיש למנצח רווח ממשי של כסף או מאכל". So everyone gets the same treasure, with no winner.
- Everything is printed, cut and placed before Shabbat.
- No phones, timers, flashlights or lights. This one is general knowledge and was not read in a specific citation.

Other authorities differ, and the same source separates children from adults. Say: "this is based on Peninei Halakha, and your family's rabbi decides". The checker applies the same limits to a festival as a cautious default. The source cited speaks about Shabbat.

## How the checker decides

- Saturday, before the `havdalah` time or with no time given: on Shabbat.
- The eve of Shabbat or a festival: needs `end` and `candle_lighting`. Without them it stops and asks (`SHABBAT_TIME`), because it cannot tell.
- Festival days are computed for Israel: Rosh Hashana (both days), Yom Kippur, the first day of Sukkot, Shemini Atzeret, the first and seventh days of Pesach, and Shavuot. The computed dates matched Hebcal for 2026 to 2031. Diaspora second days are out of scope. A family can set `yom_tov: true` for any other day it treats the same way.
- Any other day: not Shabbat or a festival.

## Candles on Shabbat and festivals

The candle question is asked on any date. If candles will burn during the game, no station goes in that room. Extending the Hanukkah candle guidance to Shabbat and festival candles is this skill's inference.
