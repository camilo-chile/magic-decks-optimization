# Purchase review, Phase 2 step 7.4 (2026-11-08)

Independent final review (Opus 5.5 high) of `decks/reports/purchase-plan-20261108.md` and the four
`decks/phase2/moxfield/<slug>-after-purchases.txt`. Nothing was bought or committed; `decks/phase2/<slug>.txt`, `.plan.json`
and `.build.md` were not edited. Evidence: the three reading files in `data/prices/`, `data/cache/collection_inventory.json`
(2026-11-02, from the 2026-11-01 export), `data/model/phase2/assignment.json` (2026-11-08 00:12), Scryfall API (printings,
tokens, Game Changer flag, full-art flag, read 2026-11-08), the bracket script and an adapted consistency-gate run (scratchpad).

## Verdicts

| Deck | Verdict | Why |
|---|---|---|
| Azula | GO WITH FIXES | Owned free Soul-Guide Lantern applied (saves 742). DROP Talisman of Creativity (2,100): applied by the owner |
| Toph | GO | All four buys KEEP; bracket and gate pass |
| Ezio | GO WITH FIXES | Spanish Command Tower at the same price applied. DROP Mind Stone (742) and Ezio's Soul-Guide Lantern (742, Hookblade stays): applied by the owner |
| Kilo | GO | All buys KEEP; gate passes with wipes at the minimum (2 of 2) |
| Whole order | GO WITH FIXES | Fixes applied below; before paying: the live check of every line (all readings over 24 h), Narset and Muddle first (prices not in `data/prices/`) |

No blocker found.

## Corrected totals (CLP; factual fixes applied, DROP proposals NOT applied)

| Block | GoM | P2W | RIV | Total |
|---|---|---|---|---|
| Inside the shared 5,000 cap (Azula 1,440; Toph 1,470; Ezio 2,054) | 4,064 | 900 | 0 | 4,964 |
| Inside Kilo's 7,000 cap | 1,500 | 2,100 | 3,200 | 6,800 |
| Over-cap Azula / Toph / Ezio / Kilo | 2,235 (Ezio) + 2,500 (Kilo) | 2,100 + 2,940 + 1,440 + 5,600 | 0 | 2,100 / 2,940 / 3,675 / 8,100 = 16,815 |
| Section A | 10,299 | 15,080 | 3,200 | 28,579 |
| Section B: loans 31,597; extras 3,100; basics 2,700; recommended stock 6,105 | 22,447 | 20,155 | 900 | 43,502 |
| Cards | 32,746 | 35,235 | 4,100 | 72,081 |
| Shipping (5,000 per store) | 5,000 | 5,000 | 5,000 | 15,000 |
| Grand total | 37,746 | 40,235 | 9,100 | 87,081 |
| Elephant tokens x2 (P2W search price, not in the totals) | | about 4,400 | | about 91,481 with them |

If the owner accepts the three DROPs: Section A 24,995 (Azula over-cap 0, Ezio inside 570 + over-cap 3,675), cards 68,497,
grand total 83,497 (saves 3,584). The original plan's arithmetic was correct (every subtotal recomputed: 29,321 / 43,502 /
72,823 / 87,823); the totals change only because of fix F1.

## Findings

| # | Sev. | Finding | Evidence | Fix |
|---|---|---|---|---|
| F1 | fix (APPLIED) | Azula's Soul-Guide Lantern was bought although he owns a free one | Inventory: 2 Spanish copies (DRC 139 in Kilo; EOC 143 in no deck). Toph build.md: "Soul-Guide Lantern (left Toph in step 6: both copies free...)" | GoM line 2 removed; Azula's list now `Soul-Guide Lantern (EOC) 143`; Ezio's copy (742) moved inside the shared cap, which stays at 4,964; Ezio over-cap 4,417 to 3,675; GoM needs 1 copy, not 2 |
| F2 | fix (APPLIED) | Command Tower bought in English while the same store has the Spanish copy at the same price | P2W psv: `command tower|enn|900` CMR 350 LP and `esn|900` C17 LP Spanish. Rule: Spanish wins at the same price; the builder's section 8 named the C17 Spanish copy | P2W line 13 now ES C17 242 (Scryfall-checked); Ezio's list `Command Tower (C17) 242`; Kilo keeps Ezio's PIP 259 |
| F3 | fix (APPLIED) | Full-art Mountains bought in English while a Spanish full-art copy is at the same price | P2W psv: DSK 275 LP 900 and BFZ 268 LP Spanish 900; Scryfall BFZ 268 `full_art: true` | P2W line 14: 3 x BFZ 268 Spanish LP; fallback 3 x DSK 275 EN LP (one printing either way) |
| F4 | fix (APPLIED) | Elephant token line had no store or printing | Generous Gift's token is TMSC 28, 3/3 green, no text. P2W "Elephant // Wurm Double-Sided Token [Double Masters Tokens]" (Elephant face T2XM 14, 3/3 green: exact), search price 2,200, variant page refused (HTTP 429). GoM's "Elephant // Treasure [Tarkir: Dragonstorm Tokens]" is TTDM 14, a 5/5: wrong token | P2W line 15 filled, about 4,400 for 2, shown apart from the totals; read the variant price and quantity at the live check, else "Sin stock" |
| F5 | fix (APPLIED) | Stale Salt figures in the summary | Salt reports v3: Ezio 6.7 measured (plan said "6.8 to 6.9, not measured"); Kilo 4.6 measured, floor 4.5 (plan said "4.0 expected, measure against the 4.0 floor") | Summary table updated |
| F6 | fix (APPLIED, text) | "The colorless Rogue's Passage replaces the colorless Rumble Arena, so the color count does not change" is false | Rumble Arena: `{1}, {T}: Add one mana of any color`; Ezio's payment_enablers 8 to 7. Ezio's lands W 13 to 11, U 13 to 12, B 12, R 12 to 10, G 8 to 7 after all swaps | Plan text corrected; the swap itself stays (KEEP, see table) |
| F7 | fix (APPLIED, text) | Kilo's function margins quoted before all cuts | Gate re-run: through_wide_board 12 of 10 (not 15), wipes 2 of 2, counter_doublers 9 + Kilo of 10 (WARN, as before) | Plan text corrected |
| F8 | note (APPLIED, text) | "Toph and Azula play no Swords" is false | assignment.json: Toph plays Spanish Swords EOC 45 | Plan text corrected; no order change |
| F9 | fix (open) | Narset (GoM 1,440) and Muddle the Mixture (P2W 3,000, Spanish) have no reading file in `data/prices/` | Neither name is in `browser-gameofmagic-20261107-wishlist.psv` or `browser-paytowin-20261107-wishlist.psv`; source is the unsaved scratchpad `overcap/result.txt` | Verify both first at the live check; save the reading; Muddle above 3,000 needs the owner's OK (pre-approval is "under about 3,000"); Muddle's printing must be Spanish |
| F10 | note (proposal) | Chaos Warp stock line (915) buys a 5th copy while 2 are free | Inventory: 4 copies (MBC 72 EN in Azula, EOC 49 ES in Kilo, SOC 239 EN and FIC 291 ES free); only Azula and Kilo play it (the plan's "red in all four decks" is false) | Propose removing it from stock (saves 915). Not applied: the owner approved the 8 stock cards |
| F11 | note | Exotic Orchard stock line (915) | 5 owned, 4 used, 1 free | Low value; owner's call |
| F12 | note | Beast Within (optional stock) makes a 3/3 green Beast | He owns one Beast token (TTDC 20, 3/3 green), used for Toph's copy | Only if a second Beast Within enters a deck: one more Beast token |
| F13 | note | Bayek of Siwa replacement now 2,320 (GoM Showcase), not 915 as in `decks/phase2.json` | GoM psv | Still under 5,000: stays automatic; update `replacement_clp` when bought |
| F14 | note | Every reading is over 24 h old at purchase time | GoM 2026-11-07 22:01, P2W 22:10, RIV 2026-11-08 03:56 | Already flagged in the plan's section 5 |

Checked and correct (no finding):
- Every price, store, variant and fallback of the other lines matches its reading file (GoM 21 lines, P2W 19, RIV 6).
- Printings: every set and collector number in the after-purchase lists exists on Scryfall (29 checked, including HOB 142, DRC 37,
  MSC 266, BLC 272, ZNC 114, M3C 321, C20 286, CMM 426/624, KHC 115, WOC 68, BRO 16/257, ONE 155/238, DMU 236, TDC 329/330).
- Languages: Kilo's 11 incoming cards are all Spanish (bought Spanish lines, Ezio's Spanish Swords FRC 37 and Command Tower PIP 259);
  every other line is the cheaper of EN/ES or the Spanish at the same price, after F2 and F3.
- Same printing in one store: the only multi-copy lines (Mountains, Elephant tokens) are one printing; the two Generous Gifts and
  two Battlefield Forges differ only because Kilo needs Spanish.
- Lists: 100 cards each; every bought upgrade is in its list; every cut is out; every owned card matches its assigned copy in
  `assignment.json` (only expected exceptions: Ezio's proxy commander, Smoldering Marsh owed, Swords FRC 37 and Command Tower
  PIP 259 moved from Ezio to Kilo); no copy is used twice (Battlefield Forge: Toph keeps the owned Spanish EOC 58, Ezio and Kilo
  buy theirs).
- Loans: the 8 restock rows with stock are in the order; the real Ezio is left out with the owner's reason (waits for the normal
  printing). Smoldering Marsh is claimed (GoM line 22).
- Full-art basics (Scryfall `full_art`, owned minus the four after-purchase lists): Plains 13, Island 12, Swamp 10, Forest 14,
  Mountain 7, so 3 Mountains is exact.
- Tokens: Scryfall `all_parts` of all 41 cards of the order: only Generous Gift (and the optional Beast Within) make tokens.

## Bracket 3 rules (after-purchase lists, `check_phase2_bracket.py` logic, reports in the scratchpad)

| Deck | Verdict | Game Changers | Mass land denial / extra turns | Two-card infinite lines |
|---|---|---|---|---|
| Azula | PASS, 100/100 recognized | 1 (Narset) | none / none | Godo + Helm of the Host: 6 + 4 = 10 mana to assemble, late |
| Toph | PASS, 100/100 | 2 (Crop Rotation, Drannith Magistrate) | none / none | see below |
| Ezio | PASS, 100/100 | 0 | none / none | Ezio + Magister Sphinx: 2 + 7 = 9, late |
| Kilo | PASS, 100/100 | 0 | none / none | none (Excavation + Lux + Crawler is three cards) |

**Toph's two 2-card lines (Salt), both legal under Bracket 3:**
1. **Bumi, Unleashed + Ashaya, Soul of the Wild** (infinite combats). Pieces {3}{R}{G} + {3}{G}{G} = 10 mana to assemble; the
   project's rule (`docs/power-scale.md`: 6 or less early, 7-8 borderline, 9+ late) reads it LATE. Ashaya makes Bumi a land,
   so each combat damage untaps the lands and adds a combat for land creatures. Accepted by the owner 2026-11-02.
2. **Toph, the First Metalbender + The Stasis Coffin** (Salt: "opponents locked"). Under Toph the Coffin is a land, so Toph's
   end-step earthbend can target it; `{2}, {T}`, exile it gives protection from everything until my next turn, and the earthbend
   returns it tapped. Repeatable once per turn cycle for 2 mana. It is NOT infinite and does not win: it is a defensive loop
   (non-targeted life loss still hits him). Pieces 4 + 3 = 7 mana plus 2 to start (borderline by MV, so checked by hand).
   It breaks no Bracket 3 rule; the script tags it "review: lock" (floor 1) and Salt's own criteria show "early-game
   infinites 0".

## Consistency gate (plan_density logic on the after-purchase lists)

Each `plan.json` was copied to the scratchpad with the cut cards removed and the bought cards added to the functions their Oracle
text supports (Wood Elves, Cultivate, Myriad in land_entries; Generous Gift and Swords in through_big_creatures; Rogue's Passage
in through_wide_board; Volt Charge in counter_doublers; Relic in kilo_tap_outlets; Prism, Talismans, Relic, Boots in
artifact_density). Result: **no FAIL in any deck.**

| Deck | New WARN vs base | Key counts after |
|---|---|---|
| Azula | ramp 10 of 12 (was 11), team_evasion 5 of 6 (Malcolm out) | through_wide_board 10 of 10 (at the minimum) |
| Toph | none | all functions above minimum |
| Ezio | none (team_evasion 4 of 6 and ramp 7 of 10 were already WARN) | payment_enablers 7 (Rumble Arena out) |
| Kilo | ramp WARN cleared (10) | wipes 2 of 2 (minimum), through_wide_board 12 of 10, counter_doublers 9 + Kilo |

## KEEP / DROP of every deck-upgrade buy (owner's request; proposals, not applied)

Salt evidence: Azula 7.2 owned, 7.3 with Narset + Lantern (v2), 7.3 with the Talisman too (v3). Toph 7.0 owned, 7.0 with Wood
Elves + Cultivate (v2), 7.0 with all four (v3). Ezio 6.6 owned and after the first package, 6.7 in v3 (lands, Lantern,
Swords). Kilo 3.8 owned, 3.8 in v2, 4.6 in v3 (whole package; the combo is the driver). No buy was measured alone.

| Deck | Card in | Card out | CLP | Salt effect | Concrete gain | Verdict |
|---|---|---|---|---|---|---|
| Azula | Narset, Parter of Veils | Malcolm, the Eyes | 1,440 | +0.1 (with the Lantern) | Fills the first of 3 Game Changer slots; -2 digs 4 deep twice for one of 30 instants/sorceries; static stops opponents' wheels and extra draws. Cost: team_evasion 6 to 5 | KEEP |
| Azula | Soul-Guide Lantern (owned EOC 143) | Dimir Locket | 0 | Salt's "no graveyard interaction" suggestion disappears | Graveyard hate 0 to 1 (skill floor 1) | KEEP |
| Azula | Talisman of Creativity | Bender's Waterskin | 2,100 | 0.0 (7.3 to 7.3) | Only one mana cheaper. Azula already has five rocks at 2 MV or less (Sol Ring, Arcane Signet, Mind Stone, Dimir and Izzet Signets). Waterskin untaps in every other player's untap step: any-color mana on each opponent's turn for an instant deck. Ramp count unchanged | **DROP** |
| Toph | Wood Elves | Bender's Waterskin | 570 | 0.0 | An untapped Forest onto the battlefield: a landfall trigger and a permanent land that works without Toph on board (the Waterskin is a land entry only under Toph) and survives artifact removal; a nontoken creature for Ashaya | KEEP |
| Toph | Cultivate | Chromatic Lantern | 900 | 0.0 | Two lands from one card: a landfall now and a land in hand for the 7 extra-land-drop cards. The Lantern's fixing is already done by Great Divide Guide | KEEP |
| Toph | Myriad Landscape | Forest | 1,440 | 0.0 (tapped-land penalty offsets it) | A land slot becomes 3 land entries (two extra landfall triggers) and +1 land on the battlefield. Cost: one more tapped land | KEEP |
| Toph | Generous Gift | Fateful Absence | 1,500 | 0.0 | Answers artifacts, enchantments and lands as well as creatures (Interaction is Toph's lowest Salt pillar). Cost: gives a 3/3, not a Clue | KEEP |
| Ezio | Golgari Signet | Deathcap Cultivator | 570 | not separable | Turns 1 generic (Rogue's Passage, Sol Ring, Path) into {B}{G} for the five-color kill, including G, the thinnest color (7 lands), and survives creature wipes | KEEP |
| Ezio | Mind Stone | Boros Locket | 742 | not separable | Ramp stays 7 (a rock for a rock); only one mana cheaper on a 2-MV commander. It loses an {R}/{W} source when red and white already drop to 10 and 11 lands for the {W}{U}{B}{R}{G} kill | **DROP** |
| Ezio | Battlefield Forge | Clifftop Retreat | 915 | +0.1 with the land package | Untapped every time: Clifftop is tapped without a Mountain or Plains, and Ezio has 1 of each among 15 basics. Tapped lands are a major Salt driver for Ezio | KEEP |
| Ezio | Llanowar Wastes | Jungle Shrine | 1,320 | same package | One fewer always-tapped land; B for freerunning {B}{B}; G kept. Cost: one R and one W source | KEEP |
| Ezio | Rogue's Passage | Rumble Arena | 1,440 | same package | Repeatable unblockable for Ezio, the kill trigger: it needs combat damage. Cost: a rainbow source (payment_enablers 8 to 7) | KEEP |
| Ezio | Soul-Guide Lantern | Hookblade | 742 | same package | Graveyard hate is already 1 (Abstergo Entertainment exiles all graveyards), and Ezio uses its own yard (Jacob Frye, recursion). Hookblade gives Ezio flying on his turn at no cost on the kill turn | **DROP** (Hookblade stays) |
| Kilo | Meticulous Excavation | Chromatic Star | 300 | main driver of 3.8 to 4.6 | Completes the Spellbook line Excavation + Lux Artillery + Crystalline Crawler (1034-1350-2060) | KEEP |
| Kilo | Volt Charge | Firebending Lesson | 200 | package | Proliferate: counter_doublers back to 9 + Kilo after Thrummingbird leaves; hits any target | KEEP |
| Kilo | Prophetic Prism | Etherium Sculptor | 200 | package | With line A's infinite colored mana, Excavation loops the Prism to draw the deck and find the payoff (Fireweaver, Surge Conductor, Etched Oracle); a cantrip artifact for Fireweaver. Cost: artifact_payoffs 17 to 16 | KEEP |
| Kilo | Generous Gift | Brute Suit | 2,100 | package (Interaction 107 to 139) | An instant answer to any permanent; through_big_creatures +1 | KEEP |
| Kilo | Talisman of Conviction | Inspiring Overseer | 1,500 | package | A turn-2 rock: brings ramp to the profile's 10 (the WARN clears); an artifact for improvise. Cost: a flier that draws | KEEP |
| Kilo | Relic of Legends | Hangarback Walker | 2,500 | package | Tapping Kilo for mana is an instant, repeatable Kilo tap: a proliferate every turn without attacking, plus ramp. Margins stay wide | KEEP |
| Kilo | Swords to Plowshares (Ezio's Spanish copy; the English one is bought for Ezio) | Thrummingbird | 2,500 | package | The best 1-mana answer for big creatures; Thrummingbird was a weak late proliferator (counter_doublers covered by Volt Charge) | KEEP |
| Kilo | Muddle the Mixture | Chain Reaction | 3,000 | package | A 2-mana counter for the combo turn and against sorcery wipes on his artifact board; Chain Reaction also killed his own creatures. Transmute finds MV-2 cards. Cost: wipes at the minimum (2 of 2) | KEEP (verify price) |
| Kilo | Battlefield Forge (Spanish) | Path of Ancestry | 2,600 | package (tapped-land penalty -0.31 with 5 tapped) | One fewer tapped land on the combo turn. Cost: loses a {U} source and scry. Kilo is 0.1 over its 4.5 floor, so dropping it risks the floor | KEEP (borderline) |
| Kilo | Swiftfoot Boots (owner's extra) | Ovalchase Dragster | 2,200 | package | Hexproof for Kilo, the enabler commander (Kilo already has haste). Cost: an instant crew outlet, kilo_tap_outlets 10 | KEEP (owner decided the buy) |
| Kilo | Command Tower (Ezio's Spanish PIP 259; Ezio gets the bought C17) | Mountain | 900 | package | A three-color source instead of a mono-red one | KEEP (owner decided) |

**Count: 24 rows, 21 KEEP, 3 DROP** (Talisman of Creativity 2,100; Mind Stone 742; Ezio's Soul-Guide Lantern 742; saves
3,584). If accepted: Azula's list keeps Bender's Waterskin, Ezio's keeps Boros Locket and Hookblade; Salt floors are not at risk
(Azula 7.3 was measured without the Talisman; Ezio 6.7 against 6.5).

## Better swaps at the same or lower price (three stores)
- None found in the three readings beyond the DROPs above. The readings cover only the wishlist cards, so this is not an
  exhaustive search of the stores.

## Fixes applied (log)
1. `purchase-plan-20261108.md`: GoM line 2 removed (F1); GoM line 9 reclassified A-cap; P2W lines 13 (F2), 14 (F3) and 15 (F4)
   rewritten; summary table, totals table and section 5 quantities updated; text corrections F5 to F8, plus a note that the
   KEEP/DROP proposals are not applied.
2. `decks/phase2/moxfield/fire-lord-azula-after-purchases.txt`: `Soul-Guide Lantern (WOE) 251` to `(EOC) 143`.
3. `decks/phase2/moxfield/ezio-auditore-da-firenze-after-purchases.txt`: `Command Tower (CMR) 350` to `(C17) 242`.
4. Both lists still have 100 cards; Salt is unaffected (same cards, different printings).

## Owner's decision applied (2026-11-08, after this review)

Rule: a card with no real gain is not bought. Applied:
- Azula: Talisman of Creativity not bought; Bender's Waterskin (TLA 255) stays. P2W line 3 struck.
- Ezio: Mind Stone not bought; Boros Locket (C21 236) stays. GoM line 5 struck.
- Ezio: Soul-Guide Lantern not bought; Hookblade (ACR 6) stays. GoM line 9 struck; no Lantern is bought at all now.
- Chaos Warp stock line removed (2 free copies owned). GoM line 19 struck; recommended stock 7 lines, 5,190.
- Accounting: with room left in the shared cap, Toph's Generous Gift (1,500) moved from over-cap to inside the cap.
- Lists: `fire-lord-azula-after-purchases.txt` and `ezio-auditore-da-firenze-after-purchases.txt` updated; both 100 cards,
  CRLF and sorting kept; bracket check re-run: both PASS (Azula 1 Game Changer, Ezio 0). Salt not re-measured: Azula's v2
  score of 7.3 was this exact list; Ezio's 6.7 was measured with Mind Stone and the Lantern (floor 6.5).

| Block | GoM | P2W | RIV | Total |
|---|---|---|---|---|
| Inside the shared cap (Azula 1,440; Toph 2,970; Ezio 570) | 2,580 | 2,400 | 0 | 4,980 of 5,000 |
| Inside Kilo's cap | 1,500 | 2,100 | 3,200 | 6,800 of 7,000 |
| Over-cap: Azula 0; Toph 1,440; Ezio 3,675; Kilo 8,100 | 4,735 | 8,480 | 0 | 13,215 |
| Section A | 8,815 | 12,980 | 3,200 | 24,995 |
| Section B: loans 31,597; extras 3,100; basics 2,700; recommended stock 5,190 | 21,532 | 20,155 | 900 | 42,587 |
| Cards | 30,347 | 33,135 | 4,100 | 67,582 |
| Shipping | 5,000 | 5,000 | 5,000 | 15,000 |
| Grand total | 35,347 | 38,135 | 9,100 | 82,582 |
| With the 2 Elephant tokens at the search price | | +4,400 | | about 86,982 |

These supersede the "Corrected totals" table above (saving against it: 3,584 + 915 = 4,499).

## Open items for the owner
1. The Elephant tokens at about 2,200 each (only exact match found, P2W): buy, or "Sin stock"?
