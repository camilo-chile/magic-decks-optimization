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
| landfall_payoffs | early (judged at 12 cards) | 10 | 13 | 13 | 64% | 83% | 91% | 96% |
| through_wide_board | early (judged at 12 cards) | 10 | 15 | 15 | 70% | 88% | 94% | 97% |
| through_big_creatures | early (judged at 12 cards) | 10 | 16 | 16 | 72% | 90% | 95% | 98% |

## Support lines

| Line | Pieces | Profile minimum | Reported |
|---|---|---|---|
| extra_land_drops | 7 | 5 | yes |
| land_recursion | 4 | 3 | yes |
| mana_sinks | 7 | 3 | yes |
| wipe_insurance | 4 | 2 | yes |

## Tags

Plan cards (engine, payoff, backup): 24 of 61 non-land cards (39%). Plan cards in no function and no route: 0.

| Tag | Cards (primary tag) |
|---|---|
| draw | 5 |
| engine | 8 |
| land | 38 |
| orphan | 2 |
| payoff | 16 |
| protection | 4 |
| ramp | 17 |
| removal | 6 |
| tutor | 2 |
| wipe | 1 |

Base functions, counting second tags too: ramp 20, draw 10, removal 9, wipe 1, protection 4.

## Win routes

- landfall burn (noncombat): arbaaz mir, fire nation archers, sabotender, tannuk, memorial ensign, valakut exploration. Against three opponents: Every land entry deals 1 damage to EACH opponent per pinger (Arbaaz: every artifact or legendary entry), Valakut Exploration deals end-step damage to each opponent, and Fire Nation Archers turns spare mana into 2 to each opponent per {5} (10 to 15 mana by turns 7 to 8: 4 to 6 to everyone a turn). Realistic board: one pinger (46 % by turn 7, 54 % with Chord) at 3 entries a turn = 3 to each opponent a turn, plus Archers late; two pingers at once is the best case (9.5 % by turn 7). All three opponents fall together.
- artifact burst (noncombat): goblin bombardment, ragost, deft gastronaut. Against three opponents: Ragost turns every artifact (Treasures, Clues, Foods, rocks, the artifact-lands Toph makes) into 3 damage to EACH opponent and untaps at every end step after any lifegain (Zuran Orb at instant speed, Druid Class, Arbaaz Mir), so it fires up to four times per turn cycle, 12 to each opponent; Goblin Bombardment converts land creatures and tokens into the last points on whoever is left.
- land army (combat): bumi, unleashed, rampaging baloths, seismic tutelage, the earth king, titania, protector of argoth, toph, the blind bandit. Against three opponents: Attacks with several power-4+ creatures make The Earth King fetch that many basics (more Baloths beasts and pings), Garruk's Uprising and Earthbender Ascension give trample over chump blockers, Bumi's connection untaps every land for a second combat of land creatures; attackers are split to finish the weakest players while the pings hit all three, and the earthbent attackers return to play when they die.
- infinite landfall (noncombat): ashaya, soul of the wild, lotus cobra, springheart nantuko, tireless provisioner. Against three opponents: Three-card loops made of on-plan cards (Spellbook 3470-5702-6871, 3875-5702-6871, 539-1315-7037, 539-5147-7037): R8 Toph + Springheart Nantuko CAST for bestow on her end-step earthbent land + Lotus Cobra or Tireless Provisioner = infinite landfall (each copy is a land that enters untapped and pays the next {1}{G}); closers: Sabotender, Tannuk, Valakut Exploration (whole library to each opponent at end step), Fire Nation Archers when the loop also nets mana (Cobra and Provisioner both out); Arbaaz does NOT trigger (the copies are tokens). R9 Ashaya + Toph, the Blind Bandit + Zuran Orb or Goblin Bombardment = the Bandit is a land, earthbends herself on entry and returns when sacrificed: infinite landfall, and Arbaaz triggers too (a nontoken legend enters each loop); Bombardment alone kills the table. Every opponent dies at once.

Cards bad when drawn (early and late only): {'late': 2, 'early': 10}
