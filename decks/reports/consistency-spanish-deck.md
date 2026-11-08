# Consistency gate: spanish-deck (PASS)

Plan: Kilo becomes tapped every turn (a haste attack, or at home by station, crew, waterbend and improvise) and proliferates the charge and +1/+1 counters that about 23 rocks, engines and artifact creatures place; those counters become mana, cards and threats, and the deck closes through whichever route it draws: without combat through Lux Artillery (10 to EACH opponent every end step at 30 counters) or Darksteel Reactor (20 charge counters), two cards with no tutor in the Spanish pool (one of them by turn 9 in about 30 % of games, about 40 % counting Long-Range Sensor, plus Emry, Buried Ruin and Phyrexian Metamorph to recover or copy them), or with the co-primary combat route below, which closes most games.
Backup: Co-primary, same pieces: the countered artifact board attacks: Cyberdrive Awakener turns every noncreature artifact into a 4/4 flyer for the turn, Depthshaker Titan gives the artifact creatures trample and haste, and Titan Forge 9/9s and Threefold Thunderhulk Gnomes spread the damage over three opponents (all six closers of both routes: about 66 % by turn 9).
Archetype: plus_one_counters + artifacts (plan)

## Failures

- none

## Warnings

- function counter_doublers: reaches its minimum of 10 only with the commander (9 pieces without it); if the commander is removed the function fails
- base: 9 ramp cards, the plus_one_counters profile asks for 10 or more

## Functions

Pieces count the commander (guaranteed) and the tutors that can fetch for the function; the odds are WITHOUT the commander, and a function the commander guarantees says so.

| Function | Needed by | Required | Pieces | Without commander | P(1+ in 7 cards) | P(1+ in 12 cards) | P(1+ in 16 cards) | P(1+ in 20 cards) |
|---|---|---|---|---|---|---|---|---|
| counter_sources | early (judged at 12 cards) | 12 | 23 | 23 | 85% | 97% | 99% | 100% |
| counter_payoffs | late (judged at 20 cards) | 6 | 15 | 15 | 70% | 88% | 94% | 97% |
| counter_doublers | early (judged at 12 cards) | 10 | 10 | 9 (commander guaranteed) | 50% | 70% | 81% | 88% |
| kilo_tap_outlets | late (judged at 20 cards) | 6 | 11 | 10 (commander guaranteed) | 54% | 74% | 84% | 91% |
| artifact_density | early (judged at 12 cards) | 20 | 44 | 43 (commander guaranteed) | 98% | 100% | 100% | 100% |
| artifact_payoffs | early (judged at 12 cards) | 10 | 18 | 18 | 77% | 92% | 97% | 99% |
| through_wide_board | early (judged at 12 cards) | 10 | 16 | 16 | 72% | 90% | 95% | 98% |
| through_big_creatures | early (judged at 12 cards) | 10 | 16 | 16 | 72% | 90% | 95% | 98% |

## Support lines

| Line | Pieces | Profile minimum | Reported |
|---|---|---|---|
| evasion | 9 | 4 | yes |
| wipe_insurance | 7 | 2 | yes |

## Tags

Plan cards (engine, payoff, backup): 32 of 62 non-land cards (52%). Plan cards in no function and no route: 0.

| Tag | Cards (primary tag) |
|---|---|
| draw | 8 |
| engine | 25 |
| land | 37 |
| payoff | 7 |
| protection | 2 |
| ramp | 9 |
| removal | 9 |
| wipe | 2 |

Base functions, counting second tags too: ramp 9, draw 13, removal 9, wipe 2, protection 4.

## Win routes

- counter burn and the Reactor (noncombat): darksteel reactor, lux artillery, reckless fireweaver. Against three opponents: Lux Artillery deals 10 to EACH opponent at every end step once the board holds 30 counters (four end steps kill a full table at 40 life, fewer after combat or Fireweaver chip damage); Darksteel Reactor wins against all three at 20 charge counters (one per upkeep plus every proliferate, doubled by Tekuthal; Deepglow Skate doubles it at once); Reckless Fireweaver hits each opponent for 1 per artifact entry (Thunderhulk Gnomes, Hangarback Thopters, Golem tokens). None needs combat damage; Buried Ruin, Emry and Phyrexian Metamorph (a copy of Lux Artillery is a second 10 to each) back the two finishers.
- artifact alpha strike (combat): cyberdrive awakener, depthshaker titan, threefold thunderhulk, titan forge. Against three opponents: Team-wide: Cyberdrive makes every noncreature artifact (8 to 15 rocks and engines by the late game) a 4/4 flyer this turn and gives every artifact creature flying, enough flying damage to split over the three opponents; Depthshaker gives every artifact creature trample, haste and melee (+3/+3 when all three opponents are attacked); Thunderhulk makes Gnomes on entering and on each attack, and Titan Forge makes a 9/9 every time three counters build. Damage is split so each opponent falls in two swings, with Lux Artillery finishing the ones left low.

Cards bad when drawn (early and late only): {'early': 10, 'late': 2}
