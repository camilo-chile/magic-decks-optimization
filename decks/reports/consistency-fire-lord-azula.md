# Consistency gate: fire-lord-azula (PASS)

Plan: Fire Lord Azula attacks every turn from turn 4 (haste and hexproof from equipment, a shield of one- and two-mana counters and free redirects held behind her); while she attacks she copies every instant and flash spell, so draw, removal and dig are two-for-ones, and the win comes in one protected combat: a three-card loop with her (Narset's Reversal with Turnabout, Frantic Search or Storm-Kiln Artist; Snap with Dualcaster Mage) makes unbounded mana or casts (the Frantic Search loop is library-bound: mana and dig, not a kill alone), which a multikicked, copied Comet Storm or Thermo-Alchemist pings turn into lethal damage to each opponent.
Backup: Without a loop the same window cards win fairly: Turnabout, Snap, Frantic Search, Big Score and Storm-Kiln Artist fuel a copied Comet Storm or Electrodominance (2X to each opponent); with Azula answered, Godo fetches Helm of the Host for unlimited combats, Ozai attacks with haste, and Comet Storm is cast uncopied with the mana Horizon Stone and Turnabout bank.
Archetype: spellslinger + combat_attackers (modifier)

## Failures

- none

## Warnings

- support line attackers: 4 pieces, the spellslinger profile asks 12; write the reason in the profile table or promote the line to a declared function
- support line team_evasion: 5 pieces, the spellslinger profile asks 6; write the reason in the profile table or promote the line to a declared function
- base: 10 ramp cards, the spellslinger profile asks for 12 or more

## Functions

Pieces count the commander (guaranteed) and the tutors that can fetch for the function; the odds are WITHOUT the commander, and a function the commander guarantees says so.

| Function | Needed by | Required | Pieces | Without commander | P(1+ in 7 cards) | P(1+ in 12 cards) | P(1+ in 16 cards) | P(1+ in 20 cards) |
|---|---|---|---|---|---|---|---|---|
| spell_density | early (judged at 12 cards) | 30 | 35 | 35 | 96% | 100% | 100% | 100% |
| spell_payoffs | late (judged at 20 cards) | 6 | 11 | 10 (commander guaranteed) | 54% | 74% | 84% | 91% |
| through_wide_board | early (judged at 12 cards) | 10 | 12 | 12 | 61% | 81% | 90% | 94% |
| through_big_creatures | early (judged at 12 cards) | 10 | 16 | 16 | 72% | 90% | 95% | 98% |
| window_mana | late (judged at 20 cards) | 6 | 12 | 12 | 61% | 81% | 90% | 94% |

## Support lines

| Line | Pieces | Profile minimum | Reported |
|---|---|---|---|
| cost_reducers | 4 | 2 | yes |
| attackers | 4 | 12 | yes |
| haste | 4 | 4 | yes |
| team_evasion | 5 | 6 | yes |
| defense_while_tapped | 5 | 4 | yes |
| combat_draw | 5 | 4 | yes |
| wipe_insurance | 3 | 2 | yes |

## Tags

Plan cards (engine, payoff, backup): 15 of 63 non-land cards (24%). Plan cards in no function and no route: 0.

| Tag | Cards (primary tag) |
|---|---|
| backup | 1 |
| draw | 11 |
| engine | 5 |
| land | 36 |
| payoff | 9 |
| protection | 12 |
| ramp | 10 |
| removal | 10 |
| tutor | 3 |
| wipe | 2 |

Base functions, counting second tags too: ramp 10, draw 12, removal 15, wipe 2, protection 13.

## Win routes

- Azula three-card loops (noncombat): dualcaster mage, frantic search, narset's reversal, snap, storm-kiln artist, thermo-alchemist, turnabout. Against three opponents: While Azula attacks (she need not connect): Narset's Reversal with Turnabout (unbounded mana), with Frantic Search (library-bound, about +1 mana and four cards seen a loop, at most about 26 Thermo pings: NOT a kill alone, it digs and funds Comet Storm) or with Storm-Kiln Artist (unbounded Treasures); or Snap with Dualcaster Mage (unbounded untapped lands and Dualcaster tokens). Thermo-Alchemist untaps on every cast and pings EACH opponent per cast; unbounded mana goes into Comet Storm kicked twice and copied, X lethal to all three at once. Mystical Teachings (copied in combat: two pieces) and Solve the Equation find every piece, Shred Memory transmutes for the Reversal or Snap; Narset, Parter of Veils, Gleam of Death, Brainstorm and Thirst for Knowledge dig. Never loop Frantic Search with Archmage Emeritus out (mandatory draws).
- Copied X burn to each opponent (noncombat): comet storm, electrodominance. Against three opponents: Comet Storm kicked twice names all three opponents; Azula copies it, 2X to each. Turnabout copied in combat untaps every land twice, Horizon Stone and Electro keep mana from earlier steps and turns: X of 8 to 12 by turn 7. Without Azula it is cast once with banked mana. Electrodominance copied adds 2X to one or two players and casts two free spells. No combat damage needed.
- Azula, Helm and Godo in combat (combat): fire lord azula, godo, bandit warlord, helm of the host, ozai, the phoenix king. Against three opponents: Helm of the Host on Azula makes a hasty Azula every combat (each spell copied twice, attacks spread across opponents); Godo puts Helm onto the battlefield and, with Helm equipped, gives unlimited combats with growing hasty Godo tokens WITHOUT Azula (late two-card line, the route that survives her removal); Ozai hits another player with 7 trample, indestructible with six floating mana. Copied Fists of Flame and removal after blocks make blocking a losing trade; Rogue's Passage makes her unblockable.

Cards bad when drawn (early and late only): {'early': 6, 'late': 3}
