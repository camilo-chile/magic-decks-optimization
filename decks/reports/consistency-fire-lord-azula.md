# Consistency gate: fire-lord-azula (PASS)

Plan: Fire Lord Azula attacks every turn (haste and hexproof from equipment, counterspells and redirects behind her); while she attacks she copies every instant and flash spell cast with her firebending mana and the cost reducers, so each draw, removal and burn spell is a two-for-one, Horizon Stone, Electro and Ozai keep the leftover window mana, and she closes against all three opponents with copied multi-target X burn (Comet Storm, Electrodominance) and with combat by herself, Helm of the Host copies of her, extra combats (Overpowering Attack, Godo) and Ozai; copied pump tricks make blocking her a losing trade.
Backup: When Azula is answered or the board stalls, the same pieces close without her: Thermo-Alchemist pings every opponent on each instant, Comet Storm and Electrodominance are cast uncopied with the mana Horizon Stone stores, Archmage Emeritus, Storm-Kiln Artist and Black Market Connections keep the hand and the mana full, and Ozai attacks with haste.
Archetype: spellslinger + combat_attackers (modifier)

## Failures

- none

## Warnings

- support line attackers: 6 pieces, the spellslinger profile asks 12; write the reason in the profile table or promote the line to a declared function
- base: 11 ramp cards, the spellslinger profile asks for 12 or more

## Functions

Pieces count the commander (guaranteed) and the tutors that can fetch for the function; the odds are WITHOUT the commander, and a function the commander guarantees says so.

| Function | Needed by | Required | Pieces | Without commander | P(1+ in 7 cards) | P(1+ in 12 cards) | P(1+ in 16 cards) | P(1+ in 20 cards) |
|---|---|---|---|---|---|---|---|---|
| spell_density | early (judged at 12 cards) | 30 | 30 | 30 | 93% | 99% | 100% | 100% |
| spell_payoffs | late (judged at 20 cards) | 6 | 10 | 9 (commander guaranteed) | 50% | 70% | 81% | 88% |
| through_wide_board | early (judged at 12 cards) | 10 | 13 | 13 | 64% | 83% | 91% | 96% |
| through_big_creatures | early (judged at 12 cards) | 10 | 15 | 15 | 70% | 88% | 94% | 97% |
| window_mana | late (judged at 20 cards) | 6 | 10 | 10 | 54% | 74% | 84% | 91% |

## Support lines

| Line | Pieces | Profile minimum | Reported |
|---|---|---|---|
| cost_reducers | 4 | 2 | yes |
| attackers | 6 | 12 | yes |
| haste | 4 | 4 | yes |
| team_evasion | 6 | 6 | yes |
| defense_while_tapped | 5 | 4 | yes |
| combat_draw | 6 | 4 | yes |
| wipe_insurance | 2 | 2 | yes |

## Tags

Plan cards (engine, payoff, backup): 19 of 63 non-land cards (30%). Plan cards in no function and no route: 0.

| Tag | Cards (primary tag) |
|---|---|
| backup | 2 |
| draw | 12 |
| engine | 7 |
| land | 36 |
| payoff | 10 |
| protection | 8 |
| ramp | 10 |
| removal | 9 |
| tutor | 3 |
| wipe | 2 |

Base functions, counting second tags too: ramp 11, draw 15, removal 11, wipe 2, protection 8.

## Win routes

- copied burn to each opponent (noncombat): comet storm, electrodominance. Against three opponents: Comet Storm multikicked twice names all three opponents and Azula copies it (2X to each); Horizon Stone stores colorless mana between turns so X reaches 8 to 12, and the loops of the third route make X as large as needed; Mystical Teachings and Solve the Equation fetch it; Electrodominance copied adds 2X to one or two players plus two free spells. Recast for free an X spell has X=0: never do that. None of it needs combat damage through blockers.
- Azula and her copies in combat (combat): fire lord azula, godo, bandit warlord, helm of the host, overpowering attack, ozai, the phoenix king. Against three opponents: Overpowering Attack (freerunning {2}{R} once Azula has dealt combat damage) and Godo give extra combats, each a new firebending and a new round of copies; Helm of the Host makes a hasty nonlegendary Azula every combat, so two or three Azulas attack different opponents; Godo with Helm gives unlimited combats WITHOUT Azula (two-card late line, the route's redundancy when she is answered); Ozai (7/7 trample, haste, flying and indestructible with six floating mana) hits another player; copied pump tricks and removal after blocks make blocking a losing trade.
- Azula loops for unbounded mana (noncombat): dualcaster mage, frantic search, narset's reversal, snap, thermo-alchemist. Against three opponents: While Azula attacks: (a) Dualcaster Mage plus Snap: Snap stays on the stack, each Dualcaster cast is copied, both bodies copy Snap, four lands untap for a 3-mana spell: unbounded mana and Dualcaster tokens; (b) Frantic Search plus Narset's Reversal (the Reversal's copy returns the Reversal itself, its copy returns Frantic Search): +1 mana per loop, +3 with the two reducers, about a dozen loops before the library runs low (never loop with Archmage Emeritus out: it decks you). Thermo-Alchemist untaps on each cast of loop (b) and pings all three opponents twice per loop; the unbounded mana of (a) goes into Comet Storm with X and kicks for all three. Mystical Teachings and Solve the Equation fetch every loop piece.

Cards bad when drawn (early and late only): {'early': 6, 'late': 2}
