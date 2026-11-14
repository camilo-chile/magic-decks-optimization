# Final review: Fire Lord Azula (Phase 2 step 7.7, 2026-11-08)

Independent champion review of the rebuilt list `decks/phase2/fire-lord-azula.txt` (with `.plan.json` and `.build.md`),
under `docs/proposals/final-rebuild-brief-20261108.md` (corrected budget: Azula all-in 6,000; every buy under 3,000 from
Game of Magic Singles, PayToWin or Rivendel; any condition better than Damaged). No deck file was edited; nothing committed.

**Verdict: FIX** (three small swaps, no blocker). The list is sound, legal and stronger than both earlier lists. The fixes add
a real tutor to the loop hub, close the haste WARN and save 632 CLP.

## 1. Rules

| Check | Result |
|---|---|
| `python scripts/check_phase2_bracket.py decks/phase2/fire-lord-azula.txt` | PASS (floor 3; 1 Game Changer: Narset, Parter of Veils; 0 extra turns, 0 mass land denial, 0 reversible) |
| `python scripts/plan_density.py` | PASS, 0 failures, 4 WARNs (ramp 10/12, haste 3/4, team_evasion 5/6, attackers 4/12) |
| Card count | 100 (commander + 99), summed from the file |
| Game Changers | 1 of 3 |
| Early two-card infinite | None. Spellbook finds 5 variants in the list; the only two-card one is Godo + Helm of the Host, classed late (6 + 5 mana over two turns). Every Azula loop needs Azula attacking + 2 cards (three cards with the commander: welcome under the owner's rules) |
| Reversible cards | None |
| Ownership | Every non-bought card has a free copy after Ezio's final list (checked against `pool-fire-lord-azula.json` and `ezio-auditore-da-firenze.txt`). Buys: Turnabout, Narset, Fellwar Stone, Spell Pierce, Thirst for Knowledge (the stock-line copy) |
| Language | English wherever an English copy is free: Cascade Bluffs (SOC EN), Shivan Reef (FRC EN), Smoldering Marsh (LTC EN; Ezio takes the owed MSC ES copy, as the build notes say). Spanish-only cards are listed in the build notes, section 8; all correct |

**Loop lines, traced on the Oracle text (project cache):**
- (a) Azula + Narset's Reversal + Turnabout. Cast Turnabout ({2}{U}{U}); Azula copies it, and before the copy resolves you tap
  every land for mana, then the copy untaps them all. Cast the Reversal ({U}{U}) on Turnabout; Azula's copy of the Reversal
  targets the ORIGINAL Reversal: it copies it (that copy targets Turnabout) and returns the Reversal to hand; the new copy
  copies Turnabout (all lands untap again) and returns Turnabout to hand. Per cycle: 6 mana paid, 2 full untaps of N lands
  (tap them before each untap resolves). Net 2N - 6 per cycle, **unbounded at 4+ lands**. Two casts per cycle: with
  Thermo-Alchemist, 2 pings to each opponent per cycle, unbounded. All mana is spent in one step (mana empties between steps).
  Works. Condition: Azula attacking, 6 mana open (8 lands in practice for the bait-and-shield sequence).
- (b) Azula + Reversal + Frantic Search: same mechanics; per cycle 5 mana paid, 6 lands untapped, **net +1** (+2 with each
  reducer; +4 with Glamdring on Azula). Four cards drawn and discarded per cycle: library-bound (about 13 cycles), 26 Thermo
  pings at most: **not a win alone** from 40 life; it is a mana and dig engine. The plan file says so ("library-bound").
- (c) Azula + Reversal + Storm-Kiln Artist: Reversal cast + Azula's copy + the copy of the Reversal = 3 magecraft Treasures for
  {U}{U}: **net +1 Treasure per cycle, unbounded** (needs any instant or sorcery on the stack as the first target). Mandatory
  draws only with Archmage out.
- (d) Azula + Snap + Dualcaster Mage: cast Dualcaster with Snap on the stack; Azula copies Dualcaster (a token); each Dualcaster
  ETB copies Snap aimed at itself: 4 lands untapped per {1}{R}{R} cast: **net +1 (+2 with Nightscape Familiar), unbounded**,
  provided the untapped lands make red. No Thermo untap (Dualcaster is a creature spell): the outlet is Comet Storm, or
  Storm-Kiln (a Treasure per Snap copy).
- Narset's Reversal alone with Turnabout and no Azula: no loop. Snap + Dualcaster without Azula: net -1. No early two-card line.

**Swan Song.** The claim is right, and it is not even a claim: the brief frees copies held by decks not yet rebuilt, and Kilo
(priority 4) is not rebuilt. Azula gains more: a {U} answer to the wipe or removal spell on its win turn (R20 lift +1.3) in a
deck whose win is one protected combat. **Note for the lead:** Negate is also a Spanish-only copy and also sits in Azula, so
Kilo is left with one Spanish counter (the bought Muddle the Mixture). If Kilo needs a second one, Azula can release Negate
for It'll Quench Ya! (owned EN, free) at a small loss (soft counter); that is Kilo's call, not a fix here.

## 2. Facts

**Buy prices** (hints from the reading files; live reads of 2026-11-08 by this review, Shopify `.js` product pages where the
stores did not answer HTTP 429):

| Card | Builder hint | Evidence found | Status |
|---|---|---|---|
| Narset, Parter of Veils | 1,440 GoM | `browser-gameofmagic-20261108-order.psv`: NM EN 1,440 | read |
| Fellwar Stone | 1,560 PayToWin | `browser-paytowin-20261107-wishlist.psv`: NM EN 1,560 (Lorwyn Eclipsed Commander) | read (one day old) |
| Thirst for Knowledge | 300 Rivendel | `rivendel-20261108.psv`: Español 300, stock 2 | read |
| Spell Pierce | 742 (to read) | **GoM live: Double Masters 2022 borderless, Near Mint, 570, available**; GoM suggest "from 342" (Zendikar); PayToWin suggest "from 600" | now read: **570** |
| Turnabout | 1,560 (to read) | No file reading. Suggest only: GoM "from 445" (Dominaria Remastered, Ravnica Remastered retro, The List); GoM Dominaria Remastered retro **sold out** (live .js); PayToWin "from 960" (DMR, RVR retro, The List) | still to read; 1,560 is a safe ceiling |
| Shred Memory (proposed, F1) | | Suggest only: GoM "from 680", PayToWin "from 1,100" (Ravnica: City of Guilds) | to read; hint 1,100 |

A suggest "from" price may be a sold-out or Damaged variant: the lead reads the product page before buying.

**Iteration 1's four tutors, checked on round4-step27.txt and the Oracle text.** The builder's claim is **right for the
loops and overstated for the win routes**:
- None of the four can fetch a loop piece: the six pieces are instants (Snap, Reversal, Frantic, Turnabout) and creatures
  that are neither Lesson nor Noble nor artifact (Dualcaster, Storm-Kiln). Lo and Li fetch Lesson or Noble (Octopus Form,
  Redirect Lightning, Ozai); Loyal Inventor and Reckless Handling fetch artifacts; Entomb only bins a card.
- But Loyal Inventor and Reckless Handling DID reach a win route: Helm of the Host (Godo + Helm; Helm on Azula). Entomb could
  bin Mystical Teachings for a 7-mana flashback instant tutor. So "never reached a win line" is false; "never fetched a loop
  piece" is true. It does not change the decision (Godo already fetches Helm), but it confirms the deck still has only **two
  real tutors to the loops** (Mystical Teachings, Solve the Equation). Fix F1 adds a third.

**Rules points of the build notes.** R1, R2, R8, R9 confirmed by Oracle/rulings; R3, R4, R5 confirmed by the traces above.
R7 is imprecise: Day of Black Sun X=0 kills tokens with mana value 0, but token COPIES of creatures keep the original's mana
value (note N3).

## 3. Strength

**Plan and routes.** One plan, three routes with disjoint failure points (R28 holds: Godo + Helm works with Azula dead; no
route needs the graveyard; a counter is answered by 7 shield pieces). The primary route is compact (3 cards with Azula) with
5 lines over 6 pieces; its weakness is access: raw 22 % by turn 8 with only two true tutors. Narset, Gleam, Brainstorm and
Thirst dig, Mystical Teachings copied in the window finds two pieces. The fair route (copied Comet Storm) is real and hits
all three opponents.

**Curve and mana.** 36 lands, 7 rocks, 3 reducers, average MV 2.51, 37 cards at MV 2 or less. 0 always-tapped lands; 9
conditional (check/reveal lands, Snarl, Smoldering Marsh, Sunken Hollow, Fire Nation Palace) with 17 basics: acceptable.
The four WARNs:
- Ramp 10/12: **acceptable.** Firebending, Turnabout, Snap, Frantic, Big Score and Storm-Kiln make window mana; lands +
  lasting ramp 46 with the reducers. A twelfth rock would cost a window card.
- Haste 3/4: **fixable for free** (F3: Expedite).
- Team evasion 5/6: **acceptable.** Azula's copies trigger on attacking, not on connecting.
- Attackers 4/12: **acceptable.** One attacker is the whole engine; Helm adds Azula tokens.

**Interaction and protection.** 14 spot answers (11 at MV 2 or less, all instant or flash), 4 counters, 2 wipes, 8
protection pieces in layers, a 7-piece win-turn shield. Artifact answers 3, enchantment answers 2: R19 met.

**Game Changers.** 1 of 3 (Narset). No Game Changer is owned in Grixis colors, and every other Game Changer in these colors
costs well over 3,000 CLP. The slots stay empty for budget reasons, not by choice (note N4).

**The 10 weakest nonland cards, with the best replacement:**

| # | Card | Problem | Best replacement | Swap? |
|---|---|---|---|---|
| 1 | Soul-Guide Lantern | Floor utility, 1 card of value | **Shred Memory** (buy ~680 to 1,100): instant graveyard hate (copied: 8 cards) AND transmute {1}{B}{B} for MV 2: Narset's Reversal (hub of 3 lines), Snap, Thermo-Alchemist, Glamdring | **F1** |
| 2 | Fellwar Stone (buy) | 1,560 for a turn-2 rock | **Everflowing Chalice** (owned, free ES copy): the same turn-2 mana, colorless; scales late | **F2** |
| 3 | Cunning Maneuver | Combat trick + Clue; card advantage costs {2} more | **Expedite** (owned EN, free): {R} instant cantrip (copied: draw 2) that gives a recast Azula or Godo haste; closes the haste WARN | **F3** |
| 4 | Ritual of Soot | Symmetric; kills 6 of 9 own creatures (R21) | none better owned (Inundate 6 mana, Blasphemous Act) | keep (wipes min 2) |
| 5 | Fatal Push | Narrow in Commander | Heartless Act (owned, free) | keep: revolt is easy here (Treasures, Clues, Mind Stone, Chalice) |
| 6 | Fists of Flame | Cantrip trick | Lightning Bolt (buy 900+) | keep (draw count 12 = min) |
| 7 | Bender's Waterskin | 3-mana rock | none cheaper owned | keep (mana on every opponent's turn feeds instant draw) |
| 8 | Abandon Attachments | Rummage | Opt / Consider (owned) | keep (nets more when copied) |
| 9 | Amphibian Downpour | 3 mana | Imprisoned in the Moon (owned, sorcery speed) | keep (flash, copied in window) |
| 10 | Hidden Footblade | Narrow | | keep (haste) |

**Test of F1 to F3** (scratch copy of the list and plan, both scripts run from the scratchpad): bracket PASS (1 GC);
consistency PASS with **3 WARNs** (haste closed); draw 12, removal 15, ramp 10, spell_density 35, spell_payoffs 10 (+1 with
the new tutor), through_big_creatures 15, window_mana 12.

**Stronger in a real 4-player game?** Yes, clearly against the current list; moderately against iteration 1.
- Against the current list (8 swaps): Lightning Strike, Opt, Frostcliff Siege, Zuko, Azula On the Hunt, Gearhulk and
  Overpowering Attack become cheap instant answers (Firebending Lesson, Failed Fording), a win-turn shield (Spell Pierce,
  Swan Song, Redirect Lightning), a fifth loop line (Turnabout), Fellwar and Thirst. It loses Black Market Connections (Ezio's)
  and the Gearhulk's value.
- Against iteration 1: better at executing a game (haste, draw 20, Horizon Stone, a shield), with fewer weak tutors and about
  the same loop access.

## 4. Money: buys ranked by gain per CLP (after the fixes)

Gain is real-power points [J].

| Rank | Card | Store | Price (CLP) | Gain | Gain per 1,000 CLP | Plays until it arrives |
|---|---|---|---|---|---|---|
| 1 | Thirst for Knowledge | Rivendel (ES, 2 in stock) | 300 | +0.03 | 0.10 | Opt (owned) |
| 2 | Narset, Parter of Veils (GC) | GoM (NM EN) | 1,440 | +0.10 | 0.07 | Zuko, Exiled Prince (owned) |
| 3 | Shred Memory (F1) | GoM (from 680) or PayToWin (from 1,100), to read | 1,100 | +0.06 | 0.055 | Soul-Guide Lantern (owned) |
| 4 | Spell Pierce | GoM (2XM NM, live 570) | 570 | +0.03 | 0.053 | Mana Leak (owned, free) |
| 5 | Turnabout | GoM (from 445) or PayToWin (from 960), to read | 1,560 ceiling | +0.07 | 0.045 | Opt or Lightning Strike (owned) |
| cut | Fellwar Stone (F2) | PayToWin | 1,560 | +0.01 vs Chalice | 0.006 | Everflowing Chalice (owned) |
| | **Total** | | **4,970** (builder: 5,602) | | | |

Margin 1,030 inside the 6,000 envelope (Turnabout and Shred Memory are at their ceilings). Cut order if the global target
needs room: Fellwar Stone (done) → Spell Pierce (Mana Leak plays, -570) → Turnabout (-1,560) → Shred Memory → Thirst
(stock line) → Narset last.

## 5. Real power (1-10: 4 precon, 6 upgraded, 7-8 high power, 9-10 cEDH)

| List | Real power | Basis |
|---|---|---|
| Iteration 1 (round4-step27, Salt 8.4) | 7.0-7.5 | real-power review 2026-11-08; six lines, slow haste, weak tutors |
| Current after purchases (Salt 7.3) | 7.2-7.7 | same review |
| New list as built | 7.4-7.8 | +0.2 over current: cheap answers, shield, fifth line. Builder's 7.5-8.0 sits at the top; project estimates have run high |
| New list with F1 to F3 | **7.5-7.9** | +0.1: a third real tutor to the hub, haste WARN closed |

Confidence: medium-low (no games played). Commander Salt expected 7.3-7.7: its "no tutors" penalty eases a little with
Shred Memory.

## 6. Findings

| ID | Severity | Finding | Exact change |
|---|---|---|---|
| F1 | fix | Only 2 true tutors reach the loops (R18; the real-power review's lesson). Shred Memory transmutes for the hub (Reversal) or Snap and keeps the graveyard-hate floor | `-1 Soul-Guide Lantern` `+1 Shred Memory` (buy ~1,100 ceiling, to read). Plan: tags `["removal","tutor"]`; `tutors` entry; add to spell_density |
| F2 | fix | Fellwar Stone buys almost nothing over the owned Everflowing Chalice | `-1 Fellwar Stone` `+1 Everflowing Chalice` (owned: free ES copy; the EN copy if Toph's final list frees it). Saves 1,560 |
| F3 | fix | Haste 3/4 WARN closable for free; Cunning Maneuver is the weakest window card | `-1 Cunning Maneuver` `+1 Expedite` (owned EN, free). Plan: tag `draw`, support haste; remove from through_big_creatures, combat_draw, payoffs |
| N1 | note | Kilo is left with one Spanish counter (Swan Song and Negate both in Azula) | Lead's call: if needed, Azula's Negate → It'll Quench Ya! |
| N2 | note | Prices: Spell Pierce now read at 570 (GoM); Turnabout and Shred Memory still to read (GoM DMR retro Turnabout is sold out) | Update build notes section 6/11 |
| N3 | note | R7: Day of Black Sun X=0 misses token copies of creatures (they keep mana value) | Fix the line in the guide |
| N4 | note | 1 of 3 Game Changer slots filled (budget-blocked: none owned, none under 3,000) | None |
| N5 | note | Goldfish runs were estimated from openings, not played to turn 8 (R38) | The lead may run 5 goldfish and 3 disrupted games when writing the guide |
| N6 | note | No politics line in the play notes | Guide: Swan Song gives an opponent a 2/2 flier; Deflecting Swat and Redirect send removal at the table's leader; Propaganda pushes attacks to the others |
| N7 | note | Loop (b) with Frantic Search is library-bound and not a kill alone | Guide: use it as mana and dig, finish with Comet Storm |

## 7. Champion checklist (41 items of `champion-addendum-20261108.md` section 1, with F1 to F3)

**Count: 36 APPLIED, 4 NOT APPLIED, 1 N/A.**

| # | Item | Status | Evidence |
|---|---|---|---|
| 1 | One plan + backup reusing pieces | APPLIED | Plan sentence; backup reuses Turnabout, Snap, Frantic, Comet Storm |
| 2 | Every card alone and with many | APPLIED | 0 orphans; loop pieces each useful alone |
| 3 | Redundancy of key effects | APPLIED | 5 loop lines over 6 pieces; 4 finishers (Thermo, Comet Storm, Electrodominance, Electro) |
| 4 | Multi-role slots | APPLIED | 31 of 63 nonland in 2+ functions |
| 5 | Commander-centric balance | APPLIED | 4 or fewer cards blank without Azula |
| 6 | Land count from curve and ramp | APPLIED | 36 lands, avg MV 2.51 |
| 7 | Colored sources | APPLIED | U 18, B 18, R 17 + rocks |
| 8 | Total mana sources 46+ | APPLIED | 36 + 7 rocks + 3 reducers = 46 (borderline: reducers counted) |
| 9 | Non-GC fast mana | APPLIED | Sol Ring, Arcane Signet, 2 Signets, Chalice/Fellwar; Talismans not owned; rituals over budget |
| 10 | Tapped lands | APPLIED | 0 always tapped; 9 conditional with 17 basics |
| 11 | Window mana | APPLIED | window_mana 12 (with F1 to F3) |
| 12 | Curve by archetype | APPLIED | 37 at MV 2 or less; 3 at 5+ |
| 13 | Commander MV, tax, recast | APPLIED | Equipment haste on recast, Undying Malice without tax |
| 14 | Lands/curve at B4 power | APPLIED | 36, within the lean-low rule (35 possible, not needed) |
| 15 | Engines vs one-shots | APPLIED | Archmage, Storm-Kiln, Thermo, Electro engines; copied draw |
| 16 | Card advantage that scales | N/A | No Rhystic, Remora or Esper Sentinel in the pool; Mystic Remora 9,300 |
| 17 | Development before card advantage | APPLIED | Turn 2-3 draw costs 1-2 (Brainstorm, Thrill, Abandon); 4+ draw draws 3+ |
| 18 | Tutors | **NOT APPLIED → F1** | 2 true tutors to the loops; F1 makes 3 (Bracket 3 median 4) |
| 19 | Cheap instant answers | APPLIED | 14, 11 at MV 2 or less, all instant/flash; 3 artifact, 2 enchantment answers |
| 20 | Counterspell count | APPLIED | 4 (Pierce, Swan Song, Negate, Reversal) |
| 21 | Wipe kind | APPLIED | Day of Black Sun with X controlled; Ritual of Soot symmetric (kept for the gate) |
| 22 | Graveyard hate | APPLIED | Lantern → Shred Memory (F1) |
| 23 | Protection in layers | APPLIED | hexproof, redirects, counters, Undying Malice, haste recast |
| 24 | Win-turn shield | APPLIED | 7 pieces at MV 2 or less or free, sequence written |
| 25 | Answers across permanent types | APPLIED | creature, artifact, enchantment, planeswalker (Downfall, Chaos Warp) |
| 26 | Compact routes | APPLIED | 3 cards with Azula; 13+ access cards |
| 27 | 2+ disjoint routes vs three | APPLIED | Loops, copied X burn, Godo + Helm |
| 28 | No shared failure point | APPLIED | Godo route without Azula; no graveyard route |
| 29 | Threat assessment | APPLIED | Removal saved for blockers and combo pieces |
| 30 | Archenemy timing | APPLIED | "Never present lethal one turn before you can protect it"; Propaganda, Thermo, Nightscape deter |
| 31 | Politics | **NOT APPLIED → N6** | No deal or griefing note |
| 32 | Wipe recovery | APPLIED | 5 rebuild pieces; commit rule written |
| 33 | Mulligan standard | APPLIED | Keep checklist; 89 % with the free mulligan |
| 34 | Game Changer slots | **NOT APPLIED (budget) → N4** | 1 of 3; none affordable |
| 35 | Efficiency over value | APPLIED | Gearhulk (MV 6) cut; 5+ drops win or bank mana |
| 36 | High-power non-GC cards considered | APPLIED | Snap, Frantic, Swat, Swan Song, Big Score, Redirect in; Bolt, rituals, Counterspell priced and rejected |
| 37 | Bracket-breaking combos | APPLIED | Script PASS; Godo + Helm late |
| 38 | Goldfish protocol | **NOT APPLIED (partial) → N5** | 20 hands done; goldfish estimated, not played |
| 39 | Gauntlet | APPLIED | 5 opponent types written |
| 40 | Cut log | APPLIED | Section "Cut log" |
| 41 | Real-game evidence over score | APPLIED | Proven Horizon Stone and Propaganda in; real power argued beside Salt |

## 8. Champion-level?

Yes, for this collection and a 6,000 CLP envelope, once F1 to F3 are in. Every high-impact card the pool or a sub-3,000 buy
offers is in, and the interaction suite and shield are cEDH-shaped. What separates it from a Bracket 4 Azula is money, not
choices:
- rituals (Dark Ritual, Seething Song);
- flash enablers (Borne Upon a Wind, Valley Floodcaller);
- Mystical Tutor and two more Game Changers;
- Rhystic Study or Mystic Remora;
- Crackle with Power.
