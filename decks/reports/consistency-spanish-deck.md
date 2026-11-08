# Consistency gate: spanish-deck (PASS)

Plan: Kilo becomes tapped every turn (a haste attack, or at home by station, crew, waterbend and improvise) and proliferates the charge and +1/+1 counters that about 22 rocks, engines and artifact creatures place; those counters become mana and cards, and the deck closes with Darksteel Reactor: Kilo, Coretapper and Inspirit grow it, and Resourceful Defense or Moxite Refinery funnel the board's counters onto it to reach 20 (an alternate win against the whole table). Lux Artillery (10 to each opponent per end step at 30 counters) is the second noncombat route. The finishers have no tutor in the Spanish pool: Long-Range Sensor's Discover 4, Experimental Augury and the draw engines dig for them, and Emry, Buried Ruin and Phyrexian Metamorph recover or copy them.
Backup: The same countered artifact board attacks: Cyberdrive Awakener turns every noncreature artifact into a 4/4 flyer for the turn, with Titan Forge 9/9s and an unblockable Kappa Cannoneer.
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
| counter_sources | early (judged at 12 cards) | 12 | 22 | 22 | 84% | 96% | 99% | 100% |
| counter_payoffs | late (judged at 20 cards) | 6 | 16 | 16 | 72% | 90% | 95% | 98% |
| counter_doublers | early (judged at 12 cards) | 10 | 10 | 9 (commander guaranteed) | 50% | 70% | 81% | 88% |
| kilo_tap_outlets | late (judged at 20 cards) | 6 | 11 | 10 (commander guaranteed) | 54% | 74% | 84% | 91% |
| artifact_density | early (judged at 12 cards) | 20 | 42 | 41 (commander guaranteed) | 98% | 100% | 100% | 100% |
| artifact_payoffs | early (judged at 12 cards) | 10 | 17 | 17 | 74% | 91% | 96% | 99% |
| through_wide_board | early (judged at 12 cards) | 10 | 16 | 16 | 72% | 90% | 95% | 98% |
| through_big_creatures | early (judged at 12 cards) | 10 | 16 | 16 | 72% | 90% | 95% | 98% |

## Support lines

| Line | Pieces | Profile minimum | Reported |
|---|---|---|---|
| evasion | 9 | 4 | yes |
| wipe_insurance | 8 | 2 | yes |

## Tags

Plan cards (engine, payoff, backup): 31 of 62 non-land cards (50%). Plan cards in no function and no route: 0.

| Tag | Cards (primary tag) |
|---|---|
| draw | 8 |
| engine | 24 |
| land | 37 |
| payoff | 7 |
| protection | 2 |
| ramp | 9 |
| removal | 9 |
| wipe | 3 |

Base functions, counting second tags too: ramp 9, draw 12, removal 9, wipe 3, protection 4.

## Win routes

- Darksteel Reactor funnel (alternate): darksteel reactor, moxite refinery, resourceful defense. Against three opponents: Darksteel Reactor wins the game against all three opponents at 20 charge counters. Kilo proliferates it every turn (doubled by Tekuthal, doubled at once by Deepglow Skate), Coretapper and Inspirit add charge counters, and the two funnels finish it: Resourceful Defense ({4}{W}, any time) moves every counter of one permanent onto the Reactor (Inspirit's 8+ charge counters, Uthros, Empowered Autogenerator, Titan Forge, Lux Cannon, the rocks), and Moxite Refinery (sorcery) turns X counters of any kind, +1/+1 included, into X charge counters on it. Resourceful Defense also moves the counters of any permanent that dies onto the Reactor. With 25 to 40 counters on the board by turns 7 to 9, one or two funnel activations win. The Reactor is indestructible.
- Lux Artillery burn (noncombat): lux artillery, reckless fireweaver. Against three opponents: Lux Artillery deals 10 to EACH opponent at every end step once 30 counters sit on my artifacts and creatures; Reckless Fireweaver pings each opponent for every artifact entry; Phyrexian Metamorph copying Lux doubles it to 20 each.
- artifact alpha strike (combat): cyberdrive awakener, kappa cannoneer, titan forge. Against three opponents: Cyberdrive Awakener makes every noncreature artifact a 4/4 flyer for the turn (8 to 15 of them late) and gives artifact creatures flying, enough damage to split over three opponents; Titan Forge adds 9/9s; Kappa Cannoneer is unblockable after each artifact entry.

Cards bad when drawn (early and late only): {'early': 8, 'late': 2}
