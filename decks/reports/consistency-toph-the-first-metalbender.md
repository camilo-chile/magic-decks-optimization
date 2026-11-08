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
| land_entries | early (judged at 12 cards) | 12 | 27 | 26 (commander guaranteed) | 89% | 98% | 100% | 100% |
| landfall_payoffs | early (judged at 12 cards) | 10 | 13 | 13 | 64% | 83% | 91% | 96% |
| through_wide_board | early (judged at 12 cards) | 10 | 12 | 12 | 61% | 81% | 90% | 94% |
| through_big_creatures | early (judged at 12 cards) | 10 | 16 | 16 | 72% | 90% | 95% | 98% |

## Support lines

| Line | Pieces | Profile minimum | Reported |
|---|---|---|---|
| extra_land_drops | 7 | 5 | yes |
| land_recursion | 3 | 3 | yes |
| mana_sinks | 8 | 3 | yes |
| wipe_insurance | 4 | 2 | yes |

## Tags

Plan cards (engine, payoff, backup): 21 of 61 non-land cards (34%). Plan cards in no function and no route: 0.

| Tag | Cards (primary tag) |
|---|---|
| draw | 5 |
| engine | 7 |
| land | 38 |
| orphan | 1 |
| payoff | 14 |
| protection | 5 |
| ramp | 17 |
| removal | 7 |
| tutor | 4 |
| wipe | 1 |

Base functions, counting second tags too: ramp 20, draw 10, removal 10, wipe 1, protection 5.

## Win routes

- landfall burn (noncombat): sabotender, tannuk, memorial ensign, valakut exploration. Against three opponents: Every land entry deals 1 damage to EACH opponent per pinger (Tannuk, Sabotender) and Valakut Exploration deals end-step damage to each opponent; one pinger at 3 entries a turn is 3 to every opponent a turn, two at once double it. The tutors now reach the pingers too (Chord X=2-3, Seismic Sense, Water Tribe Rallier). All three opponents fall together; this route also turns the infinite-landfall loops into a table kill.
- artifact burst (noncombat): goblin bombardment, ragost, deft gastronaut. Against three opponents: Ragost turns every artifact (Treasures, Clues, Foods, rocks, the artifact-lands Toph makes) into 3 damage to EACH opponent and untaps at every end step after any lifegain (Zuran Orb at instant speed, Druid Class, Arbaaz Mir), so it fires up to four times per turn cycle, 12 to each opponent; Goblin Bombardment converts land creatures and tokens into the last points on whoever is left.
- land army (combat): bumi, unleashed, rampaging baloths, seismic tutelage, the earth king, toph, the blind bandit. Against three opponents: Attacks with several power-4+ creatures make The Earth King fetch that many basics (more Baloths beasts and pings), Garruk's Uprising and Earthbender Ascension give trample over chump blockers, Bumi's connection untaps every land for a second combat of land creatures; attackers are split to finish the weakest players while the pings hit all three, and the earthbent attackers return to play when they die.
- infinite landfall (noncombat): ashaya, soul of the wild, lotus cobra, springheart nantuko, tireless provisioner. Against three opponents: Three-card loops made of on-plan cards (Spellbook 3470-5702-6871, 3875-5702-6871, 539-1315-7037, 539-5147-7037): R8 Toph + Springheart Nantuko (found by Seismic Sense or Water Tribe Rallier, never by Chord) CAST for bestow on her end-step earthbent land + Lotus Cobra or Tireless Provisioner = infinite landfall (each copy is a land that enters untapped and pays the next {1}{G}); closers: Sabotender, Tannuk, Valakut Exploration (whole library to each opponent at end step), Rampaging Baloths (unlimited 4/4s). R9 Ashaya + Toph, the Blind Bandit + Zuran Orb (Reckless Handling, Brightglass Gearhulk find it) or Goblin Bombardment = the Bandit is a land, earthbends herself on entry and returns when sacrificed: infinite landfall; Bombardment alone kills the table. Every opponent dies at once.

Cards bad when drawn (early and late only): {'late': 2, 'early': 10}
