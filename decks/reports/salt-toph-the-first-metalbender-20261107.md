# Commander Salt score: Toph, the First Metalbender (Phase 2 list), 2026-11-07

## Links

| Item | Value |
|---|---|
| Moxfield deck | https://moxfield.com/decks/39nTTDb9R02vm8BrTCJlXA |
| Moxfield name | Phase2 Toph 2026-11-07 (Commander, Unlisted, "Override with preferred printings" OFF, 100 main deck, 0 sideboard) |
| Commander Salt result | https://commandersalt.com/details/deck/8d3ec3cfd045c0981fdc9c35bfe24e3c |
| Source list | `decks/phase2/moxfield/toph-the-first-metalbender.txt` |

## Scoring version and date

- Scoring version: **2026.4196**, the newest release in the Commander Salt changelog (dated Nov 6, 2026, scope Scoring / UI / Data). The result page itself prints no version number; its footer shows "META 08.03.24", which is not a scoring version.
- Scored on: 2026-11-07 (the result page's field report is dated NOV 7, 2026).

## Result

| Metric | Value |
|---|---|
| Power | 6.9 / 10, "Focused Casual", commander tier T4 |
| Bracket | 3, "Upgraded"; WotC spec 3, Commander Salt 3, delta "in sync" |
| Salt | 65.7, "Combo Assassin"; report card C- |

Bracket criteria (Brackets tab):

| Criterion | Value | Bracket tier |
|---|---|---|
| Game Changers | 2 | B3 |
| Mass land denial | 0 | B2 |
| Extra turns | 0 | B2 |
| Two-card infinite combos | 1 ("upgraded tier") | B3 |
| Early-game infinite combos | 0 | B2 |

Pillars (Power level tab, as displayed against the casual baseline; the page also offers a cEDH baseline toggle, not used here):

| Pillar | Value |
|---|---|
| Consistency | 283 / 100 (+283 %) |
| Efficiency | 293 / 100 (+293 %) |
| Interaction | 141 / 140 (101 %) |
| Win conditions | 1244 / 200 (+622 %) |

Report card: Saltiness C- (65.7), Interaction C+ (141), Win conditions A+ (1057.4), Synergy A+ (617.3).

Score drivers and anti-patterns (as displayed):
- Structural score ceiling, major: "wincon combos with no tutors to assemble them" (-0.45). The score is capped.
- Pushed up: tournament-grade execution (minor).
- Pulled down: too slow for its pieces (major); other penalties (major).
- Flagged for 1 mechanical anti-pattern (minor).
- Site suggestions: the one board wipe is too thin; counterspell coverage is essentially absent.

## Combos (Combos tab)

Combo score 70. Two independent win lines, 5 combo lines in total, redundancy 0.56x. Salt marks the deck as "Infinite mana" in its headline, with 0 early-game infinite combos.

| # | Pieces | Outcome | Mana | Salt score |
|---|---|---|---|---|
| 1 | Ashaya, Soul of the Wild + Bumi, Unleashed | Infinite combat (2 pieces) | 0 | 14 |
| 2 | Ashaya + Goblin Bombardment + Toph, the Blind Bandit | Infinite ETB / flicker | 0 | 14 |
| 3 | Ashaya + Toph, the Blind Bandit + Zuran Orb | Infinite ETB / flicker | 0 | 14 |
| 4 | Lotus Cobra + Springheart Nantuko + Toph, the First Metalbender | Infinite landfall | 2 | 14 |
| 5 | Springheart Nantuko + Tireless Provisioner + Toph, the First Metalbender | Infinite landfall | 2 | 14 |

Line 1 is the only two-card combo. It is a late-game line by Salt's classification (0 early-game infinite combos). The project gate `scripts/check_phase2_bracket.py` was not run for this report.

## Manabase, curve and profile

- Manabase: 3 colors, 38 lands (21 basic, 17 nonbasic including 3 fetch). Manabase Quality 61 %, Manafixing 99 %.
- Curve: average MV 2.68, peak MV 9, 1 card below MV 2.
- Ramp: 5 rocks, 3 dorks, 15 land ramp.
- Tutors: 14.7 average quality (as displayed).
- Types (a card counts in each type it has): creatures 24, artifacts 14, enchantments 11, instants 12, sorceries 5.
- Archetype: Leans Human (11 humans, 46 % of creatures). Commander reliance: 10 type matches.

## Import errors

- Moxfield showed no import error dialog. The deck has 99 mainboard cards plus Toph in the commander zone, which matches the file (100 copies including the commander).
- One line does not match. The file has `1 Drannith Magistrate (TLE) 2`. Moxfield lists "Mayor Tong of Chin Village" in its place (Creatures), and Drannith Magistrate does not appear in the Moxfield deck.
- Commander Salt holds "Drannith Magistrate" and no "Mayor Tong", so the Salt score uses the intended card. Scryfall's record for `tle/2` is Drannith Magistrate (Creature, Human Wizard), so the file is correct and the fault is in how Moxfield displays that row.
- I did not change the Moxfield deck. Check that row in Moxfield before using it again.

## Upgrades (Bracket 3, staples mode)

Scope: "Bracket 3 - Staples", described on the page as the most-played cards in real Toph decks at the selected bin (1.765 decks, as displayed). Percentages are as displayed. Staples mode shows no card that each suggestion would replace.

| # | Card | Shown % |
|---|---|---|
| 1 | Toph, Greatest Earthbender | 55 % |
| 2 | The Stasis Coffin | 54 % |
| 3 | Liquimetal Torque | 54 % |
| 4 | Stomping Ground | 51 % |
| 5 | Evolution Sage | 50 % |
| 6 | Toph, Earthbending Master | 50 % |
| 7 | Yavimaya, Cradle of Growth | 48 % |
| 8 | Haywire Mite | 48 % |
| 9 | Badgermole Cub | 46 % |
| 10 | The Earth Crystal | 46 % |

Next on the list: Temple Garden (46 %), Swiftfoot Boots (45 %), Felidar (cut off in the page text).

## Notes

- The Moxfield deck was created in the owner's account. Nothing else was edited or deleted. No sign-in, registration or settings change was made.
- No page text seen addressed an AI.
