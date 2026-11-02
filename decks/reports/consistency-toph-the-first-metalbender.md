# Consistency gate: toph-the-first-metalbender (PASS)

Plan: Put two to four lands onto the battlefield every turn from turn 4 (land ramp that puts lands into play, four fetch lands, Druid Class and Explore, The Earth King, and with Toph every nontoken artifact cast), re-enter Toph's earthbent lands through Zuran Orb, Goblin Bombardment and the land-sacrifice ramp, and turn each entry into 1 damage to EACH opponent with Tannuk, Sabotender, Arbaaz Mir and Valakut Exploration while Terrasymbiosis, Tireless Tracker and Tannuk refill the hand; Ragost's 3-damage-to-each-opponent sacrifices end the game.
Backup: The same entries build a land army (Toph's earthbent lands, Rampaging Baloths beasts, Titania elementals, The Earth King's bear): power-4+ attacks make The Earth King fetch more lands, Garruk's Uprising and Earthbender Ascension give trample, Seismic Tutelage doubles counters and Bumi untaps the lands for an extra combat.
Archetype: landfall_lands

## Failures

- none

## Warnings

- none

## Functions

Pieces count the commander (guaranteed) and the tutors that can fetch for the function; the odds are WITHOUT the commander, and a function the commander guarantees says so.

| Function | Needed by | Required | Pieces | Without commander | P(1+ in 7 cards) | P(1+ in 12 cards) | P(1+ in 16 cards) | P(1+ in 20 cards) |
|---|---|---|---|---|---|---|---|---|
| land_entries | early (judged at 12 cards) | 12 | 26 | 25 (commander guaranteed) | 88% | 98% | 99% | 100% |
| landfall_payoffs | early (judged at 12 cards) | 10 | 12 | 12 | 61% | 81% | 90% | 94% |
| through_wide_board | early (judged at 12 cards) | 10 | 14 | 14 | 67% | 86% | 93% | 97% |
| through_big_creatures | early (judged at 12 cards) | 10 | 17 | 17 | 74% | 91% | 96% | 99% |

## Support lines

| Line | Pieces | Profile minimum | Reported |
|---|---|---|---|
| extra_land_drops | 7 | 5 | yes |
| land_recursion | 4 | 3 | yes |
| mana_sinks | 7 | 3 | yes |
| wipe_insurance | 5 | 2 | yes |

## Tags

Plan cards (engine, payoff, backup): 23 of 61 non-land cards (38%). Plan cards in no function and no route: 0.

| Tag | Cards (primary tag) |
|---|---|
| draw | 5 |
| engine | 8 |
| land | 38 |
| payoff | 15 |
| protection | 4 |
| ramp | 17 |
| removal | 9 |
| tutor | 2 |
| wipe | 1 |

Base functions, counting second tags too: ramp 20, draw 10, removal 12, wipe 1, protection 4.

## Win routes

- landfall burn (noncombat): arbaaz mir, sabotender, tannuk, memorial ensign, valakut exploration. Against three opponents: Every land entry (Arbaaz: every artifact or legendary entry) deals 1 damage to EACH opponent per pinger, and Valakut Exploration deals end-step damage to each opponent equal to the unplayed exiled cards; with two pingers and 3 entries a turn that is 6 to every opponent each turn (Annie Joins Up doubles Tannuk and Arbaaz), so all three opponents fall together, never one at a time.
- artifact burst (noncombat): goblin bombardment, ragost, deft gastronaut. Against three opponents: Ragost turns every artifact (Treasures, Clues, Foods, rocks, the artifact-lands Toph makes) into 3 damage to EACH opponent and untaps at every end step after any lifegain (Zuran Orb at instant speed, Druid Class, Arbaaz Mir), so it fires up to four times per turn cycle, 12 to each opponent; Goblin Bombardment converts land creatures and tokens into the last points on whoever is left.
- land army (combat): bumi, unleashed, rampaging baloths, seismic tutelage, the earth king, titania, protector of argoth, toph, the blind bandit. Against three opponents: Attacks with several power-4+ creatures make The Earth King fetch that many basics (more Baloths beasts and pings), Garruk's Uprising and Earthbender Ascension give trample over chump blockers, Bumi's connection untaps every land for a second combat of land creatures; attackers are split to finish the weakest players while the pings hit all three, and the earthbent attackers return to play when they die.

Cards bad when drawn (early and late only): {'early': 11}
