# Consistency gate: fire-lord-azula (PASS)

Plan: Fire Lord Azula attacks every turn from turn 4 (haste from Swiftfoot Boots, Frostcliff Siege, Hidden Footblade or Expedite; hexproof from Boots, Champion's Helm and Octopus Form, free redirects and four cheap counters behind her); while she attacks she copies every instant and flash spell, so draw, removal, tutors and Torrential Gearhulk are two-for-ones, and Archmage Emeritus, Tome of Legends and Theater of Horrors keep the hand full; the win comes in one protected combat: a three-card loop with her (Narset's Reversal with Turnabout, Frantic Search or Storm-Kiln Artist; Snap with Dualcaster Mage; Return the Favor with Storm-Kiln Artist) makes unbounded mana or casts, which a multikicked, copied Comet Storm or Thermo-Alchemist pings turn into lethal damage to each opponent.
Backup: Without a loop the same window cards win fairly: Turnabout, Snap, Frantic Search, Big Score, Storm-Kiln Artist and banked mana (Horizon Stone, Ozai, Electro, Treasures) fuel a copied Comet Storm or Electrodominance (2X to each opponent), with Torrential Gearhulk recasting Turnabout, Frantic Search or the draw spells for free; with Azula answered, Godo fetches Helm of the Host for unlimited combats, Ozai attacks with haste, and Comet Storm is cast uncopied with the banked mana.
Archetype: spellslinger + combat_attackers (modifier)

## Failures

- none

## Warnings

- support line attackers: 5 pieces, the spellslinger profile asks 12; write the reason in the profile table or promote the line to a declared function
- support line haste: 3 pieces, the spellslinger profile asks 4; write the reason in the profile table or promote the line to a declared function
- support line team_evasion: 4 pieces, the spellslinger profile asks 6; write the reason in the profile table or promote the line to a declared function
- base: 11 ramp cards, the spellslinger profile asks for 12 or more

## Functions

Pieces count the commander (guaranteed) and the tutors that can fetch for the function; the odds are WITHOUT the commander, and a function the commander guarantees says so.

| Function | Needed by | Required | Pieces | Without commander | P(1+ in 7 cards) | P(1+ in 12 cards) | P(1+ in 16 cards) | P(1+ in 20 cards) |
|---|---|---|---|---|---|---|---|---|
| spell_density | early (judged at 12 cards) | 30 | 32 | 32 | 94% | 99% | 100% | 100% |
| spell_payoffs | late (judged at 20 cards) | 6 | 11 | 10 (commander guaranteed) | 54% | 74% | 84% | 91% |
| through_wide_board | early (judged at 12 cards) | 10 | 14 | 14 | 67% | 86% | 93% | 97% |
| through_big_creatures | early (judged at 12 cards) | 10 | 17 | 17 | 74% | 91% | 96% | 99% |
| window_mana | late (judged at 20 cards) | 6 | 13 | 13 | 64% | 83% | 91% | 96% |

## Support lines

| Line | Pieces | Profile minimum | Reported |
|---|---|---|---|
| cost_reducers | 4 | 2 | yes |
| attackers | 5 | 12 | yes |
| haste | 3 | 4 | yes |
| team_evasion | 4 | 6 | yes |
| defense_while_tapped | 5 | 4 | yes |
| combat_draw | 5 | 4 | yes |
| wipe_insurance | 5 | 2 | yes |

## Tags

Plan cards (engine, payoff, backup): 16 of 63 non-land cards (25%). Plan cards in no function and no route: 0.

| Tag | Cards (primary tag) |
|---|---|
| backup | 1 |
| draw | 12 |
| engine | 5 |
| land | 36 |
| payoff | 10 |
| protection | 10 |
| ramp | 11 |
| removal | 8 |
| tutor | 4 |
| wipe | 2 |

Base functions, counting second tags too: ramp 11, draw 12, removal 14, wipe 2, protection 13.

## Win routes

- Azula three-card loops (noncombat): dualcaster mage, frantic search, narset's reversal, return the favor, snap, storm-kiln artist, thermo-alchemist, turnabout. Against three opponents: While Azula attacks (she need not connect): Narset's Reversal with Turnabout (unbounded mana from 4 lands), with Storm-Kiln Artist (unbounded Treasures) or with Frantic Search (about +1 mana and four new cards a cycle: library-bound, it digs for Turnabout or Comet Storm and is not a kill alone); or Snap with Dualcaster Mage (unbounded untapped lands, every opposing creature bounced). With unbounded mana the Reversal also returns any instant to hand each cycle, so Comet Storm, Electrodominance or any draw spell repeats: Comet Storm kicked twice and copied is X lethal to all three at once; Thermo-Alchemist untaps on every cast and pings EACH opponent. Mystical Teachings (copied in combat: two pieces) and Solve the Equation find every instant piece; Shred Memory transmutes for a mana-value-2 card (the Reversal, Snap, Comet Storm, Electrodominance). Never loop Frantic Search with Archmage Emeritus out (mandatory draws).
- Copied X burn to each opponent (noncombat): comet storm, electrodominance. Against three opponents: Comet Storm kicked twice names all three opponents; Azula copies it, 2X to each. Turnabout copied in combat untaps every land twice; Torrential Gearhulk cast in the window is copied and its two triggers recast Turnabout and Frantic Search (or two draw spells) for free, each copied again; Horizon Stone, Ozai and Electro bring mana from earlier turns and Big Score and Storm-Kiln Artist leave Treasures: X of 8 to 12 by turn 7 to 8, twice if needed. Without Azula it is cast once with banked mana. Electrodominance copied adds 2X to one or two players and casts two free spells (Gearhulk, Aether Gale, Godo). No combat damage needed.
- Azula, Helm and Godo in combat (combat): fire lord azula, godo, bandit warlord, helm of the host, ozai, the phoenix king. Against three opponents: Godo puts Helm of the Host onto the battlefield and, with Helm equipped, every combat makes a new hasty Godo token whose first attack adds another combat: unlimited combats WITHOUT Azula (late two-card line, the route that survives her removal), spread over the opponents who lack two solid blockers, and an arbitrarily large army for the next turn; Aether Gale or Turnabout removes the blockers first. Helm on Azula makes a hasty Azula every combat (each spell copied twice). Ozai hits another player with 7 trample, indestructible and flying with six floating mana. Frostcliff Siege gives the team haste and trample; Rogue's Passage makes one attacker unblockable.

Cards bad when drawn (early and late only): {'early': 8, 'late': 1}
