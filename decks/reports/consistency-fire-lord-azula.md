# Consistency gate: fire-lord-azula (PASS)

Plan: Fire Lord Azula attacks every turn (haste and hexproof from equipment, counterspells and redirects behind her); while she attacks she copies every instant and flash spell cast with her firebending mana and the cost reducers, so each draw, removal and burn spell is a two-for-one, Horizon Stone, Electro and Ozai keep the leftover window mana, and she closes against all three opponents with copied multi-target X burn (Comet Storm, Electrodominance) and with combat by herself, Helm of the Host copies of her and Ozai.
Backup: When Azula is answered or the board stalls, the same pieces close without her: Thermo-Alchemist pings every opponent on each instant, Comet Storm and Electrodominance are cast uncopied with the mana Horizon Stone stores, Archmage Emeritus, Storm-Kiln Artist and Black Market Connections keep the hand and the mana full, and Ozai attacks with haste.
Archetype: spellslinger + combat_attackers (modifier)

## Failures

- none

## Warnings

- support line attackers: 3 pieces, the spellslinger profile asks 12; write the reason in the profile table or promote the line to a declared function
- support line team_evasion: 4 pieces, the spellslinger profile asks 6; write the reason in the profile table or promote the line to a declared function

## Functions

Pieces count the commander (guaranteed) and the tutors that can fetch for the function; the odds are WITHOUT the commander, and a function the commander guarantees says so.

| Function | Needed by | Required | Pieces | Without commander | P(1+ in 7 cards) | P(1+ in 12 cards) | P(1+ in 16 cards) | P(1+ in 20 cards) |
|---|---|---|---|---|---|---|---|---|
| spell_density | early (judged at 12 cards) | 30 | 31 | 31 | 93% | 99% | 100% | 100% |
| spell_payoffs | late (judged at 20 cards) | 6 | 10 | 9 (commander guaranteed) | 50% | 70% | 81% | 88% |
| through_wide_board | early (judged at 12 cards) | 10 | 11 | 11 | 57% | 78% | 87% | 93% |
| through_big_creatures | early (judged at 12 cards) | 10 | 13 | 13 | 64% | 83% | 91% | 96% |
| window_mana | late (judged at 20 cards) | 6 | 11 | 11 | 57% | 78% | 87% | 93% |

## Support lines

| Line | Pieces | Profile minimum | Reported |
|---|---|---|---|
| cost_reducers | 4 | 2 | yes |
| attackers | 3 | 12 | yes |
| haste | 5 | 4 | yes |
| team_evasion | 4 | 6 | yes |
| defense_while_tapped | 7 | 4 | yes |
| combat_draw | 4 | 4 | yes |
| wipe_insurance | 3 | 2 | yes |

## Tags

Plan cards (engine, payoff, backup): 17 of 63 non-land cards (27%). Plan cards in no function and no route: 0.

| Tag | Cards (primary tag) |
|---|---|
| backup | 2 |
| draw | 12 |
| engine | 7 |
| land | 36 |
| payoff | 8 |
| protection | 9 |
| ramp | 10 |
| removal | 11 |
| tutor | 2 |
| wipe | 2 |

Base functions, counting second tags too: ramp 12, draw 13, removal 14, wipe 2, protection 9.

## Win routes

- copied burn to each opponent (noncombat): comet storm, electrodominance, thermo-alchemist. Against three opponents: Comet Storm multikicked twice names all three opponents and Azula copies it (2X to each); Horizon Stone stores colorless mana between turns so X reaches 8 to 12; Electrodominance copied adds 2X to one player plus two free spells; Thermo-Alchemist pings all three every time an instant or sorcery is cast. None of it needs combat damage through blockers.
- Azula and her copies in combat (combat): fire lord azula, helm of the host, ozai, the phoenix king, unleash fury. Against three opponents: Helm of the Host makes a hasty nonlegendary Azula every combat, so two or three Azulas attack different opponents and each copies every spell; Ozai (7/7 trample, haste, flying and indestructible with six floating mana) hits a second player; Unleash Fury copied quadruples an unblocked Azula (16 or more commander damage) to remove the last one; copied burn finishes players left low.

Cards bad when drawn (early and late only): {'early': 5, 'late': 2}
