# hunt.json

Keep the file in its own folder. Use first names or nicknames only. Fields marked "ask" come from the parent and are never guessed. Rooms, spots and prizes are IDs from the menus in `safety-rules.md` (also `python3 scripts/check_hunt.py --menus`). Free text is refused.

```json
{
  "title": "מסע האוצר של נועה ואיתי",
  "occasion": "hanukkah",
  "format": "treasure_hunt",
  "keeps_shabbat": false,
  "younger_or_guests_asked": true,
  "adults_present": 1,
  "niqqud_route": "dicta_model",
  "host_is_adult": true,
  "adult_stays_present": true,
  "schedule": {"date": "2026-12-06", "start": "16:00", "end": "16:45"},
  "candles": {"lit_during_hunt": false},
  "frying_during": false,
  "home": {"protected_space": "mamad", "protected_route_clear": true,
           "mamad_nothing_breakable": true, "bed_is_low": true},
  "participants": [
    {"id": "noa", "name": "נועה", "age": 6, "role": "player", "address": "f", "reading_stage": "grade1", "guest": false, "just_started": true},
    {"id": "baby", "age": 1, "role": "present", "guest": false}
  ],
  "start": {"next": "s1", "clues": {"noa": {"mode": "read", "text": "...",
            "hints": ["דחיפה קטנה", "רמז חזק", "ספה. כי..."]}}},
  "stations": [
    {"id": "s1", "room_id": "living", "spot_id": "sofa_cushion", "next": "s2",
     "clues": {"noa": {"...": "the clue that leads to s2"}}},
    {"id": "s2", "room_id": "living", "spot_id": "under_table", "next": null, "treasure": true}
  ],
  "treasure": {"competitive": false, "prizes": ["large_book"]}
}
```

## How the route works

`start.clues` are handed over at the start and lead to `start.next`. The clue **stored at** a station leads to that station's `next`. The answer of a card comes from the next station's menu spot, or from its room with `"answer_from": "room"`. Two stations cannot share an answer.

## Fields

| Field | Values |
|---|---|
| `occasion` | `hanukkah`, `birthday`, `purim`, `passover`, `tu_bishvat`, `sukkot`, `summer`, `rainy_day`, `other` |
| `format` | `treasure_hunt`, `escape_room` (needs `free_exit: true`) |
| `keeps_shabbat` | ask. `true` or `false` |
| `adults_present` | ask. How many adults stay for the whole game. Required |
| `younger_or_guests_asked` | ask. Must be `true` |
| `still_mouths_objects` | ask when the youngest is 3 or 4. No answer counts as yes |
| `niqqud_route` | `dicta_model` or `nakdan_site`. Prints the Dicta credit |
| `allergies_asked` | `true` once guest parents were asked. Required for food with guests |
| `schedule` | `date`, optional `start`, `end`, `candle_lighting`, `havdalah` (HH:MM), `yom_tov: true` for a day the family treats as a festival |
| `shabbat_mode`, `prepared_before_shabbat` | `true` when the hunt falls on Shabbat or a festival for an observant family |
| `older_players_asked_rabbi` | Needed on Shabbat or a festival when a player is 12 or older |
| `candles` | ask, on any date. `lit_during_hunt`. If true: `adult_stays`, `room_ids` (menu rooms), optional `separated_by_wall`. That adult is not counted for the children. An observant family cannot answer false for a hunt after candle lighting on a Friday or festival eve |
| `frying_during` | ask, for any date during Hanukkah |
| `home.protected_space` | `mamad`, `mamak`, `shelter`, `stairwell`, `none`. For `none`, `home.siren_place` is required |
| `home.protected_route_clear` | `true` after the host confirms it |
| `home.bed_is_low` | `true` after the parent confirms a `low_bed` spot is not a bunk |
| `role` | `player` or `present` (in the home, not playing; age only, no name) |
| `guest` | Required on everyone. `true` for another family's child |
| `name` | Players only. One word, one child per row |
| `address` | ask. `m`, `f` or `plural`. Never infer it from a name |
| `reading_stage` | `gan`, `grade1`, `grade2`, `grade3`, `grade4-6` |
| `just_started` | `true` for a child who has just begun reading (shorter card) |
| station `room_id`, `spot_id` | Menu IDs |
| station `owner_id` | A player id. Required on `low_bed` with more than one player |
| station `answer_from` | `spot` (default) or `room` |
| station `container` | `box` or `envelope`, escape room only |
| clue `mode` | `read`, `adult_reads`, `picture`. A picture shows the next station's menu icon |
| clue `pretend_lock` | `true` when the text names a pretend lock on a box or envelope, never a door |
| clue `rhymed` | `true` for a rhyme (needs full niqqud in grades 2 and 3) |
| clue `puzzle` | `{"type": "atbash", "cipher": "..."}` or `{"type": "scramble", "cipher": "..."}`. The checker decodes it and compares it with the answer |
| `treasure.prizes` | Prize IDs from the menu |

## Exit codes

`check_hunt.py`: 0 no errors, 1 errors, 2 the file could not be checked (never a pass). `build_kit.py` refuses to write anything when there is an error. The scan of card text is advisory.
