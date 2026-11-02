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
| spell_payoffs | late (judged at 20 cards) | 6 | 11 | 10 (commander guaranteed) | 54% | 74% | 84% | 91% |
| through_wide_board | early (judged at 12 cards) | 10 | 13 | 13 | 64% | 83% | 91% | 96% |
| through_big_creatures | early (judged at 12 cards) | 10 | 16 | 16 | 72% | 90% | 95% | 98% |
| window_mana | late (judged at 20 cards) | 6 | 10 | 10 | 54% | 74% | 84% | 91% |

## Support lines

| Line | Pieces | Profile minimum | Reported |
|---|---|---|---|
| cost_reducers | 4 | 2 | yes |
| attackers | 6 | 12 | yes |
| haste | 4 | 4 | yes |
| team_evasion | 7 | 6 | yes |
| defense_while_tapped | 5 | 4 | yes |
| combat_draw | 7 | 4 | yes |
| wipe_insurance | 2 | 2 | yes |

## Tags

Plan cards (engine, payoff, backup): 20 of 63 non-land cards (32%). Plan cards in no function and no route: 0.

| Tag | Cards (primary tag) |
|---|---|
| backup | 2 |
| draw | 12 |
| engine | 5 |
| land | 36 |
| payoff | 13 |
| protection | 8 |
| ramp | 10 |
| removal | 8 |
| tutor | 3 |
| wipe | 2 |

Base functions, counting second tags too: ramp 11, draw 16, removal 10, wipe 2, protection 8.

## Win routes

- copied burn to each opponent (noncombat): comet storm, electrodominance, thermo-alchemist. Against three opponents: Comet Storm multikicked twice names all three opponents and Azula copies it (2X to each); Horizon Stone stores colorless mana between turns so X reaches 8 to 12; Mystical Teachings and Solve the Equation fetch it (access 4 cards, 60 % by turn 13); Electrodominance copied adds 2X to one or two players plus two free spells; Thermo-Alchemist pings all three on every instant. Recast by Gearhulk an X spell has X=0: never do that. None of it needs combat damage through blockers.
- Azula and her copies in combat (combat): fire lord azula, godo, bandit warlord, helm of the host, overpowering attack, ozai, the phoenix king, unleash fury. Against three opponents: Overpowering Attack (freerunning {2}{R} once Azula has dealt combat damage) and Godo give extra combats, each a new firebending and a new round of copies; Helm of the Host makes a hasty nonlegendary Azula every combat, so two or three Azulas attack different opponents and each copies every spell; late, Helm on Godo gives unlimited combats (allowed late line); Ozai (7/7 trample, haste, flying and indestructible with six floating mana) hits another player; copied Unleash Fury on an unblocked or trampling Azula is 16 commander damage (24 with Champion's Helm); copied burn finishes players left low.

Cards bad when drawn (early and late only): {'early': 7, 'late': 1}
