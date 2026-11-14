# Consistency gate: toph-the-first-metalbender (PASS)

Plan: Put two to four lands onto the battlefield every turn from turn 3 (cheap land ramp, four fetch lands, Druid Class, Explore and The Earth King, and with Toph every nontoken artifact cast, Mishra's Bauble, cheap rocks and 0-1 mana artifacts above all), re-enter Toph's earthbent lands through Zuran Orb, Goblin Bombardment and the instant land-sacrifice ramp, and turn every land entry into 1 damage to EACH opponent with Sabotender, Tannuk and Valakut Exploration, and every artifact or legend entering into 1 more with Arbaaz Mir, while Terrasymbiosis, Tireless Tracker and Tannuk refill the hand; Ragost, Goblin Bombardment and Legion Guildmage turn the spare artifacts and mana into the last points, and an infinite-landfall loop (Springheart Nantuko with Lotus Cobra or Tireless Provisioner, or Toph, Hardheaded Teacher with Gruul Turf and Zuran Orb) ends it at once when it assembles.
Backup: The same entries build a land army that survives a creature wipe (earthbent lands return when they die): The Earth King's bear and every power-4+ land creature fetch more basics when they attack, Earthbender Ascension and Bumi give trample, Seismic Tutelage doubles the counters of an unblockable earthbent Secret Tunnel, and Bumi untaps every land for an extra combat.
Archetype: landfall_lands

## Failures

- none

## Warnings

- none

## Functions

Pieces count the commander (guaranteed) and the tutors that can fetch for the function; the odds are WITHOUT the commander, and a function the commander guarantees says so.

| Function | Needed by | Required | Pieces | Without commander | P(1+ in 7 cards) | P(1+ in 12 cards) | P(1+ in 16 cards) | P(1+ in 20 cards) |
|---|---|---|---|---|---|---|---|---|
| land_entries | early (judged at 12 cards) | 12 | 25 | 24 (commander guaranteed) | 87% | 97% | 99% | 100% |
| landfall_payoffs | early (judged at 12 cards) | 10 | 12 | 12 | 61% | 81% | 90% | 94% |
| through_wide_board | early (judged at 12 cards) | 10 | 14 | 14 | 67% | 86% | 93% | 97% |
| through_big_creatures | early (judged at 12 cards) | 10 | 15 | 15 | 70% | 88% | 94% | 97% |

## Support lines

| Line | Pieces | Profile minimum | Reported |
|---|---|---|---|
| extra_land_drops | 8 | 5 | yes |
| land_recursion | 4 | 3 | yes |
| mana_sinks | 8 | 3 | yes |
| wipe_insurance | 4 | 2 | yes |

## Tags

Plan cards (engine, payoff, backup): 17 of 61 non-land cards (28%). Plan cards in no function and no route: 0.

| Tag | Cards (primary tag) |
|---|---|
| backup | 4 |
| draw | 4 |
| engine | 3 |
| land | 38 |
| orphan | 1 |
| payoff | 10 |
| protection | 5 |
| ramp | 19 |
| removal | 10 |
| tutor | 4 |
| wipe | 1 |

Base functions, counting second tags too: ramp 21, draw 10, removal 12, wipe 1, protection 5.

## Win routes

- landfall burn (noncombat): arbaaz mir, sabotender, tannuk, memorial ensign, valakut exploration. Against three opponents: Every land entry is 1 damage to EACH opponent per pinger (Sabotender, Tannuk), every nontoken artifact or legend entering (not fetched basics or returning lands) is 1 more to each opponent from Arbaaz Mir, so with Toph a cheap artifact triggers both Arbaaz and the landfall pingers, and Valakut Exploration deals its end-step damage to each opponent. Two pingers at three entries a turn are 6 to every opponent a turn, so the table of 120 life falls together from turn 6 to 8; Chord (X=2-3), Seismic Sense and Water Tribe Rallier find the creature pingers.
- artifact burst (noncombat): goblin bombardment, legion guildmage, ragost, deft gastronaut. Against three opponents: Ragost turns every artifact (Treasures, Clues, rocks, the artifact-lands Toph makes; earthbent artifacts come back) into 3 damage to EACH opponent and untaps at every end step after any lifegain (Arbaaz, Druid Class, Zuran Orb at instant speed), so it fires on every player's end step; Legion Guildmage turns the late surplus mana into 3 to each opponent per turn cycle; Goblin Bombardment converts land creatures (they return) and chump blockers into the last points on whoever is left.
- infinite landfall (noncombat): ashaya, soul of the wild, gruul turf, lotus cobra, springheart nantuko, tireless provisioner, toph, hardheaded teacher. Against three opponents: Organic loops of on-plan cards (Spellbook 3470-5702-6871, 3875-5702-6871, 573-1315-6871-7115, 539-1315-7037, 539-5147-7037): (A) Springheart Nantuko CAST for bestow on a land Toph earthbent (a basic Forest) plus Lotus Cobra or Tireless Provisioner: every copy is an untapped land that pays the next copy: infinite landfall; (B) Toph + Toph, Hardheaded Teacher + Gruul Turf + Zuran Orb: sacrifice the earthbent Turf, it returns and bounces the Orb (a land under Toph), recast the Orb for 0, the cast trigger earthbends the Turf again: infinite landfall, casts and life; (C) Ashaya + Toph, the Blind Bandit + Zuran Orb or Goblin Bombardment. With any pinger, Valakut (the whole library to each opponent at end step), Arbaaz (loop B) or Bombardment, every opponent dies at once.
- land army (combat): bumi, unleashed, seismic tutelage, the earth king, toph, the blind bandit. Against three opponents: Power-4+ attackers (the 4/4 bear, Bumi and his 4/4 land, the Bandit, Ashaya, earthbent lands grown by Toph every end step) make The Earth King fetch that many basics, each a ping to every opponent; Earthbender Ascension and Bumi give trample, Secret Tunnel is unblockable and carries Seismic Tutelage (counters double each attack, Terrasymbiosis draws that many); Bumi untaps every land for a second combat of land creatures. Attackers split to finish the weakest players while the pings hit all three; earthbent attackers return when they die.

Cards bad when drawn (early and late only): {'early': 7}
