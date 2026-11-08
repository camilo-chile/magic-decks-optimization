# Commander Salt report: Toph v2, owned and after purchases (2026-11-07)

Measured 2026-11-07 to 2026-11-08 in the owner's signed-in Chrome (Moxfield) and on Commander Salt (public pages, no sign-in).

## Scoring version

- Latest release on https://commandersalt.com/changelog: **2026.4196, Nov 6, 2026** (scope: Scoring / UI / Data).
- The result pages do not print a version number. The version above is the latest release at measuring time, not a stamp read from the page.

## Summary

| | Owned (deck 1) | After purchases (deck 2) |
|---|---|---|
| Moxfield deck (Unlisted) | https://moxfield.com/decks/xgvn5RIoP0qkliiaVyevOQ | https://moxfield.com/decks/uMnH3pZ79kCXqutrQz26Ug |
| Commander Salt result | https://commandersalt.com/details/deck/eec85dc9ac528c198e89bf539abf652b | https://commandersalt.com/details/deck/3658ddd6707115711340f2e6dac6f906 |
| Power (page) | **7.0** (Optimized, inferred type Casual, tier T4) | **7.0** (Optimized, inferred type Casual, tier T4) |
| Bracket | **3** (Upgraded); WotC 3, Commandersalt 3, delta in sync | **3** (Upgraded); WotC 3, Commandersalt 3, delta in sync |
| Salt | **85.1** (Combo Assassin), rage meter 28.4 % | **85.4** (Combo Assassin), rage meter 28.5 % |
| Mainboard | 99 + commander | 99 + commander |
| Import errors | none | none |

Field report on both pages (a user review, not evidence) says "7.1". The page value is 7.0; only the page value is used.

## Pillars (power level tab, vs casual baseline; value / pillar scale)

| Pillar | Owned | After purchases |
|---|---|---|
| Consistency | 307 / 100 (307 %) | 305 / 100 (305 %) |
| Efficiency | 295 / 100 (295 %) | 290 / 100 (290 %) |
| Interaction | 147 / 140 (105 %) | 147 / 140 (105 %) |
| Win conditions | 1222 / 200 (611 %) | 1223 / 200 (612 %) |

Report card (owned / after purchases): Saltiness C (85.1 / 85.4), Interaction C+ (147 / 147), Wincons A+ (1038.9 / 1039.9), Synergy A+ (608.4 / 602.0).

## Score drivers, ceilings and anti-patterns (both decks, same labels)

- Pushed up: tournament-grade execution (minor).
- Pulled down: other penalties (major); too slow for its pieces (capped, major).
- Structural ceiling (major): "Wincon combos with no tutors to assemble them (-0.37)". The same page shows Tutors 14.0 (avg quality "High-fidelity"), so the page is internally inconsistent on tutors; reported as printed.
- 1 mechanical anti-pattern flagged (minor); the algorithm capped the final score.
- Suggestions printed by Salt: the one board wipe is too thin; counterspell coverage is essentially absent; no graveyard interaction detected.

## Salt breakdown (salt tab)

- Deck 1 (85.1): locks 20.0, infinite combos 15.0, board wipes 7.0, group slug 5.0, extra combats 3.0, "you can't do that" 3.0.
- Deck 2 (85.4): same categories and values.
- Lock pieces: The Stasis Coffin with Toph, the First Metalbender (24 % of salt in deck 1, 23 % in deck 2).
- Infinite combos: 5 cards, about 18 % of salt, led by Ashaya, Soul of the Wild and Bumi, Unleashed.

## Combos (Commander Salt combos tab; identical in both decks)

Salt reports 6 combos, 3 independent game-winning lines, redundancy 0.60x. Top combos:

| Pieces | Outcome | Pieces count | Mana | Score |
|---|---|---|---|---|
| Ashaya, Soul of the Wild + Bumi, Unleashed | Infinite combat (2-card) | 2 | 0 | 14 |
| The Stasis Coffin + Toph, the First Metalbender | Opponents locked (2-card) | 2 | 2 | 14 |
| Ashaya + Goblin Bombardment + Toph, the Blind Bandit | Infinite ETB / flicker | 3 | 0 | 14 |
| Ashaya + Toph, the Blind Bandit + Zuran Orb | Infinite ETB / flicker | 3 | 0 | 14 |
| Lotus Cobra + Springheart Nantuko + Toph, the First Metalbender | Infinite landfall | 3 | 2 | 14 |

Combo score (deck 1): 84. Deck 2 combo score was not captured.

## Bracket and Game Changers (brackets tab; identical in both decks)

- Game Changers: 2 (Drannith Magistrate, which Moxfield and Salt show as "Mayor Tong of Chin Village", and Crop Rotation).
- Two-card combos: 2 (the two 2-card lines above). Mass land denial: 0. Extra turns: 0. Early-game infinites: 0.
- Commandersalt verdict: "Upgraded", bracket 3, delta in sync with WotC 3.
- Shift to bracket 2 suggested by Salt: cut the 2 Game Changers, or thin the tutor package.
- Shift to bracket 4 suggested by Salt: mass land denial, an early-game infinite, 4 or more Game Changers, or more fast mana (rocks and rituals; fast mana is light).

## Manabase (manabase tab; identical in both decks)

- Manabase score 87 / 300 (29 %): fixing 99, quality 62, curve 102.
- 38 lands (21 basic, 17 nonbasic, including 3 fetches), 35 untapped vs 3 tapped, 23 sources of any colour, 1 fast-mana land.
- Manabase label on the page: Moderate, 3-colour.

## Mainboard counts (Moxfield, verified on the page)

- Deck 1: Creatures 21, Sorceries 7, Instants 12, Artifacts 11, Enchantments 10, Lands 38 = 99. Commander: Toph, the First Metalbender.
- Deck 2: Creatures 22, Sorceries 8, Instants 12, Artifacts 9, Enchantments 10, Lands 38 = 99. Commander: Toph, the First Metalbender.

## Differences between the two lists (diff of the files)

- Bender's Waterskin (owned) is replaced by Wood Elves (after purchases).
- Chromatic Lantern (owned) is replaced by Cultivate (after purchases).
- Both lines have no set code, so Moxfield chose their printings. Those printings were not checked.

## Notes

- Import: no errors on either deck; "Override with preferred printings" was OFF for both; both decks are Unlisted (badge checked on both Moxfield pages).
- Flavor name: Drannith Magistrate appears as "Mayor Tong of Chin Village" on Moxfield and Salt. Same card, not edited.
- Untrusted page text: the Salt pages carry user field reports. None addressed an AI. No instructions were followed from page content.
- Model: this browser run was done in a Haiku 5.5 agent session. The project routes browser work through the stock-verifier agent (Haiku 5.5 @ medium). Flagged for the owner.
- Nothing else was touched: no other Moxfield deck, no account setting, no sign-in, no deletion. The owner's Game of Magic Singles tab was not used.

## After purchases v3 (2026-11-08)

- Source file: `decks/phase2/moxfield/toph-the-first-metalbender-after-purchases.txt` (pasted as is, "Override with preferred printings" OFF).
- Moxfield: https://moxfield.com/decks/e9acG_oOzEKspu1-qxNd-A (name "Phase2 Toph after purchases 2026-11-08 v3", Commander, Unlisted).
- Commander Salt: https://commandersalt.com/details/deck/83275dd65006ec4ebee8923afa8c9190
- Import check: commander Toph, the First Metalbender; mainboard 99 (Creatures 22, Sorceries 8, Instants 12, Artifacts 9, Enchantments 10, Lands 38); total 100. No import error. Set codes per row were not checked on the Moxfield text view.

| Measure | After purchases v3 |
|---|---|
| Power | 7.0 (Optimized); field report text says 7.1 |
| Bracket (Salt / WotC spec) | 3 (Upgraded) / 3, in sync |
| Salt | 84.7, C (Combo Assassin) |
| Commander tier | T4 |
| Pillars | Consistency 293 / 100; Efficiency 293 / 100; Interaction 147 / 140; Win conditions 1171 / 200 |
| Report card | Saltiness C 84.7; Interaction C+ 147; Wincons A+ 995.3; Synergy A+ 601.8 |
| Manabase | Score 84 / 300; Fixing 99, Quality 53, Curve 102; 38 lands (20 basic, 18 nonbasic, 4 fetch); 34 untapped vs 4 tapped; tapped-land penalty -0.27 |
| Combos | 6 combos, 3 independent game-winning lines, redundancy 0.60x. Ashaya + Bumi (2 cards, infinite combat); The Stasis Coffin + Toph, the First Metalbender (2 cards, opponents locked); Ashaya + Goblin Bombardment + Toph, the Blind Bandit; Ashaya + Toph, the Blind Bandit + Zuran Orb; Lotus Cobra + Springheart Nantuko + Toph, the First Metalbender (infinite landfall). Combo score 84 |
| Bracket criteria | Game Changers 2 (B3); two-card infinite combos 2 (B3); mass land denial 0; extra turns 0; early-game infinites 0 |

- Drivers: pushed up by Tournament-grade execution (minor). Pulled down by Structural ceiling (major, wincon combos with no tutors to assemble them, -0.34), Other penalties (major), Too slow for its pieces (capped, major). 1 mechanical anti-pattern flagged (minor); score capped.
- Suggestions (page, 3): the one board wipe is too thin; counterspell coverage essentially absent; no graveyard interaction detected. Manabase suggestions (3): premium duals, modal DFCs, more utility lands. Bracket: cutting the 2 Game Changers would read bracket 2; mass land denial, an early infinite, or 4+ Game Changers would read bracket 4.
- Comparison with the previous after-purchases score (7.0): same power (7.0, floor met); Salt 84.7 against 85.4 in the earlier after-purchases run (down 0.7; this is a new Commander Salt measurement of a new Moxfield copy of the same file).
