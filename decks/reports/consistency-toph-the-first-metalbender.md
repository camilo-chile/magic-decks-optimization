# Consistency gate: toph-the-first-metalbender (PASS)

Plan: Put two to four lands onto the battlefield every turn from turn 3 (twelve ramp pieces of mana value 2 or less, land ramp that fetches basics, three fetch lands, Urza's Cave, Druid Class, Explore and The Earth King; with Toph out every nontoken artifact cast is a land entering, and the land she earthbends each end step comes back when a sacrifice outlet or its own ability kills it), and turn every land entry into 1 damage to EACH opponent with Sabotender, Tannuk and Valakut Exploration and every artifact or legend entering into 1 more with Arbaaz Mir, while Valakut, Tireless Tracker, Terrasymbiosis, Stocking the Pantry and Tannuk refill the hand; Ragost, Goblin Bombardment and Fire Nation Archers turn spare artifacts and mana into the last points, The Stasis Coffin (earthbent by Toph, {2} a turn) keeps the table from damaging or targeting me while the drain runs, and an infinite-landfall loop (Springheart Nantuko with Lotus Cobra or Tireless Provisioner; Toph, Hardheaded Teacher with Gruul Turf and Zuran Orb; Ashaya with Toph, the Blind Bandit) ends the game at once when it assembles.
Backup: The same earthbends build a land army that survives creature wipes (earthbent lands return when they die): Hardened Scales adds a counter to every earthbend, The Earth King fetches a basic for every power-4+ attacker, Earthbender Ascension and Bumi give trample, Seismic Tutelage doubles the counters of an unblockable earthbent Secret Tunnel every attack, and Bumi untaps every land for a second combat.
Archetype: landfall_lands

## Failures

- none

## Warnings

- base: 19 ramp cards, the landfall_lands profile asks for 20 or more

## Functions

Pieces count the commander (guaranteed) and the tutors that can fetch for the function; the odds are WITHOUT the commander, and a function the commander guarantees says so.

| Function | Needed by | Required | Pieces | Without commander | P(1+ in 7 cards) | P(1+ in 12 cards) | P(1+ in 16 cards) | P(1+ in 20 cards) |
|---|---|---|---|---|---|---|---|---|
| land_entries | early (judged at 12 cards) | 12 | 26 | 25 (commander guaranteed) | 88% | 98% | 99% | 100% |
| landfall_payoffs | early (judged at 12 cards) | 10 | 11 | 11 | 57% | 78% | 87% | 93% |
| through_wide_board | early (judged at 12 cards) | 10 | 13 | 13 | 64% | 83% | 91% | 96% |
| through_big_creatures | early (judged at 12 cards) | 10 | 16 | 16 | 72% | 90% | 95% | 98% |

## Support lines

| Line | Pieces | Profile minimum | Reported |
|---|---|---|---|
| extra_land_drops | 9 | 5 | yes |
| land_recursion | 4 | 3 | yes |
| mana_sinks | 10 | 3 | yes |
| wipe_insurance | 3 | 2 | yes |

## Tags

Plan cards (engine, payoff, backup): 21 of 61 non-land cards (34%). Plan cards in no function and no route: 1 (Hardened Scales).

| Tag | Cards (primary tag) |
|---|---|
| backup | 5 |
| draw | 4 |
| engine | 5 |
| land | 38 |
| orphan | 1 |
| payoff | 11 |
| protection | 5 |
| ramp | 17 |
| removal | 8 |
| tutor | 4 |
| wipe | 1 |

Base functions, counting second tags too: ramp 19, draw 10, removal 8, wipe 1, protection 5.

## Win routes

- landfall burn (noncombat): arbaaz mir, sabotender, tannuk, memorial ensign, valakut exploration. Against three opponents: Every land entry is 1 damage to EACH opponent per landfall pinger (Sabotender, Tannuk); every nontoken artifact or legend entering (not fetched basics or returning basic lands) is 1 more to each opponent from Arbaaz Mir, so with Toph a cheap artifact, or an earthbent artifact that returns (The Stasis Coffin every turn), triggers both; Valakut Exploration deals its end-step damage to each opponent. Two pingers at three entries a turn are 6 to every opponent a turn, so the 120 life of the table falls together; Chord of Calling (X=2-3) and Seismic Sense find the creature pingers.
- artifact and mana burst (noncombat): fire nation archers, goblin bombardment, legion guildmage, ragost, deft gastronaut. Against three opponents: Ragost turns every artifact (Treasures, Clues, rocks, the artifact-lands Toph makes; earthbent artifacts come back) into 3 damage to EACH opponent and untaps at every end step after any lifegain (Arbaaz, Druid Class, Zuran Orb at instant speed), so it fires on each player's turn; Fire Nation Archers spends the deck's surplus mana with no tap, {5} for 2 to EACH opponent and a 2/2, as many times a turn as the mana allows and on the turn it is cast; Goblin Bombardment converts land creatures (they return) and tokens into the last points on whoever is left.
- infinite landfall (noncombat): ashaya, soul of the wild, gruul turf, lotus cobra, springheart nantuko, tireless provisioner, toph, hardheaded teacher. Against three opponents: Organic loops of on-plan cards (Spellbook 3470-5702-6871, 3875-5702-6871, 573-1315-6871-7115, 539-1315-7037, 539-5147-7037): (A) Springheart Nantuko CAST for bestow on a land Toph earthbent (a basic Forest) plus Lotus Cobra or Tireless Provisioner: every copy is an untapped land that pays for the next copy: infinite landfall; (B) Toph + Toph, Hardheaded Teacher + Gruul Turf + Zuran Orb: sacrifice the earthbent Turf, it returns and bounces the Orb (a land under Toph), recast the Orb for 0, the cast trigger earthbends the Turf again: infinite landfall, casts and life (Urza's Cave and Crop Rotation fetch the Turf, Brightglass Gearhulk the Orb); (C) Ashaya + Toph, the Blind Bandit + Zuran Orb or Goblin Bombardment. With any landfall pinger, Valakut (the whole library to each opponent at the end step), Arbaaz (loop B) or Bombardment (loop C), every opponent dies at once.
- land army (combat): bumi, unleashed, seismic tutelage, the earth king, toph, the blind bandit. Against three opponents: Power-4+ attackers (the 4/4 bear, Bumi and his 4/4 land, the Bandit, Ashaya, Brightglass Gearhulk, lands Toph earthbends every end step, one counter bigger each time with Hardened Scales) make The Earth King fetch that many basics, each a ping to every opponent; Earthbender Ascension and Bumi give trample, Secret Tunnel is unblockable and carries Seismic Tutelage (its counters double every attack, Terrasymbiosis draws that many); Bumi untaps every land for a second combat of land creatures. The attackers split to finish the weakest players while the pings hit all three; earthbent attackers return when they die, and The Stasis Coffin covers the crack-back.

Cards bad when drawn (early and late only): {'early': 12}
