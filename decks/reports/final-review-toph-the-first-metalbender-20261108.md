# Final review: Toph, the First Metalbender (Phase 2 step 7.7, 2026-11-08)

Reviewer: an independent champion (Opus 5.5 high). The list under review is `decks/phase2/toph-the-first-metalbender.txt`, with
its `.plan.json` and `.build.md`. The mandate is `docs/proposals/final-rebuild-brief-20261108.md`, corrected budget:
- 8,000 CLP all-in for Toph;
- every buy under 3,000 CLP, from the three stores;
- any condition better than Damaged.

Read: the skill and its Champion standard, the champion addendum (41 items), the Toph primer, the play review of
2026-10-26, `real-power-iterations-20261108.md`, the pool, the current list, the iteration-1 list, and the final Ezio and
Azula lists. Card text comes from the Oracle cache `oracle-cards-20261011210156` and the Scryfall rulings API (read
2026-11-09 01:45 UTC). Combo data comes from `spellbook_variants_slim.jsonl.gz`.

**Verdict: FIX.** Three card swaps, all with owned cards. No new buy. The fixes save about 2,800 CLP.

## 1. Rules

| Check | Result |
|---|---|
| `python scripts/check_phase2_bracket.py decks/phase2/toph-the-first-metalbender.txt` | **PASS**: floor 3; 2 Game Changers (Crop Rotation, Drannith Magistrate); no extra turns; no mass land denial; no reversible card; 2 review items (Bumi + Ashaya, late; the template line Toph + Teacher + Turf + Bombardment). |
| `python scripts/plan_density.py` | **PASS**: 0 failures, 0 warnings for Toph. |
| Card count | 100 by script: the commander, 61 nonland, 38 lands. |
| Reversible cards | None. Every layout is `normal` or `class`. |
| Language | The English copy is used wherever one is free. One exception: Chaos Warp plays a Spanish copy, because Ezio and Azula hold both English copies (scarce copy, allowed). Say it in build section 8. |
| Copies against Ezio, Azula and Kilo (script over the four final lists and the pool) | One shortage: **Battlefield Forge**, a single Spanish copy that Ezio also plays. It is covered, because Ezio buys an English copy (order line 5, Game of Magic, 915). Every other card has enough copies. Not in the pool and listed as buys: Wood Elves, Veil of Summer, Make a Stand, Return to Nature. |
| Reports | The scripts were rerun on the real lists after the scratch tests. `decks/reports/bracket-toph-the-first-metalbender.md` and `consistency-*.md` show the real list. |

## 2. Combo verdicts (Oracle text, rulings, Spellbook cache)

Rules basis:
- CR 603.6d: triggers look at the permanent as it exists right after the event.
- CR 707.2: an earthbend effect and counters are not copiable values.
- Earthbend rulings (2025-10-02): a land that dies returns tapped; any other zone does not return.
- Ashaya ruling (2020-09-25): creatures "enter the battlefield as lands".
- Springheart Nantuko rulings: bestow applies only when the card is cast; Chord puts it onto the battlefield unattached.

| Claim | Verdict | How it loops, what it needs | Cards | Early two-card infinite? |
|---|---|---|---|---|
| **A. Springheart Nantuko + Lotus Cobra** (Spellbook 3470-5702-6871 and 3470-5702--143) | **VERIFIED.** The earlier "unverifiable" note is wrong. | 1. Nantuko must be CAST with bestow on a land creature: a land earthbent by Toph's end step, Bandit, Bumi, Ascension or Ba Sing Se, or a land animated by Wrenn's +1.<br>2. Each landfall makes a token copy of the plain land (earthbend is not copied), and it enters untapped.<br>3. The token taps for 1 and Cobra adds 1, which pays the next {1}{G}.<br>Net mana is 0, so the result is infinite landfall only. Setup is about 3 to 4 mana on the turn after the earthbend. | Toph (or another earthbender) + Nantuko + Cobra, plus Sabotender, Tannuk or Valakut to win. That is 3 cards from the 99 plus the commander. | **No.** Infinite landfall wins nothing by itself, and the line uses 3 or more cards with the commander. Earliest kill is turn 4 to 5 in a perfect draw. It is legal under the project's three-card rule. |
| **A'. Nantuko + Tireless Provisioner** (3875-5702-6871) | **VERIFIED.** | The new land plus a Treasure pay {1}{G}. With Cobra AND Provisioner out, the loop nets +1 mana: infinite mana and Food. Food alone has no sink that kills (Ragost and Guildmage tap once). | Same as A. | **No**, same as A. |
| **B. Toph + Hardheaded Teacher + Gruul Turf + Zuran Orb** (573-1315-6871-7115--44) | **VERIFIED.** | 1. Sacrifice the earthbent Turf to the Orb; it returns tapped.<br>2. Turf's enter trigger bounces the Orb, which is a land under Toph.<br>3. Recast the Orb for 0. Teacher's cast trigger earthbends the Turf.<br>4. Repeat. Each pass gives infinite landfall, Orb entries, casts and life.<br>Zero mana. Toph must be on the battlefield. **Main phase only**: the Orb is an artifact, cast at sorcery speed. | Four cards with the commander. To win, add Arbaaz (the Orb is historic), a landfall pinger or Valakut. The Bombardment variant (573-5147-...) needs Teacher, Turf, Bombardment and a 0-cost artifact that stays (Chalice, the Orb, or Mishra's Bauble after fix F3) and deals infinite damage. | **No.** At least 4 cards, and Teacher and Toph are 4-drops. Late. |
| **C. Ashaya + Toph, the Blind Bandit + Goblin Bombardment or Zuran Orb** (539-5147-7037, 539-1315-7037) | **VERIFIED.** | Ashaya makes the Bandit a Forest land, so the Bandit's enter trigger can earthbend HERSELF. Sacrifice her and she returns tapped, triggers again, and so on. Chord (X=3) can fetch her, because the trigger is "enters". Bombardment gives infinite damage directly. The Orb gives infinite life and landfall and needs a pinger. Costs {2}{G} after Ashaya. Toph is not needed. | 3 cards (Bombardment) or 4 (Orb + a pinger). | **No.** Three cards and 8 MV of creatures. Late. |
| Bumi + Ashaya (539-7033) | **VERIFIED.** | Bumi is a land creature under Ashaya. When he connects, every land untaps, and he and the team attack again: infinite combats. Each combat needs Bumi to connect (he has trample). | 2 cards, 10 MV. | It IS a two-card infinite, but **late** (two 5-drops, turn 6 at the earliest), as the bracket script says. Allowed. |
| Sabotender | **VERIFIED.** | 1 damage to each opponent per land entry. | | |
| Tannuk | **VERIFIED.** | 1 damage to each opponent per land entry, and a card on the second entry each turn. It is legendary, so Annie doubles it. | | |
| Arbaaz Mir | **PARTLY WRONG in the plan text.** | It triggers only on nontoken HISTORIC permanents: artifacts, legends, Sagas. Fetched basics, land ramp and earthbent basics that return do NOT trigger it. It is right in build section 2 but wrong in the plan sentence "turn each entry into 1 damage ... Arbaaz Mir". | About 21 historic cards (11 nontoken artifacts, 10 legends) | |
| Valakut Exploration | **VERIFIED, with a timing note.** | The damage is dealt at YOUR end step and counts only the cards still exiled. After a loop, opponents get a window until then to remove the enchantment. | | |
| "Cheap artifacts count as lands entering with Toph" | **VERIFIED.** | CR 603.6d plus the Ashaya ruling. Toph's own ruling: she does not let you PLAY artifacts as lands. | Each nontoken artifact cast is landfall, and also an Arbaaz trigger. | |

## 3. Strength, as a champion

**Plan and routes.** The plan is sound: one repeatable board engine (landfall drain) and four routes with no shared failure
point. In real games the drain is the route that wins. The loops show up in about 1 game in 8 by turn 7.

Damage density is the real limit:
- The deck has only three true landfall pingers (Sabotender, Tannuk, Valakut).
- Arbaaz counts artifacts and legends only.
- Ragost is the best closer. With Toph earthbending an artifact-land at each end step, it fires every turn: the returning
  artifact is the next Food, and Arbaaz, Druid Class or the Orb supply the lifegain that untaps it.

**Curve and mana.**
- Average MV is 2.34. 38 lands plus 21 ramp pieces give R8 well above 46.
- 38 lands is the bottom of the landfall profile band. Flood is likelier than screw, but the drain turns lands into damage
  and there are 8 sinks.
- Colored sources, fetches included: G 22, R 18, W 18. That is enough for {G}{G}{W}{W} by turn 5 (fix F2).
- Tapped lands: Gruul Turf plus 4 fetches to tapped basics. This is over R10's 3, but the exception is written (each fetch
  is two entries). Accepted.

**Interaction.**
- 11 spot answers plus Annie. 8 cost 2 or less, Hardlight included: Swords, Path, Fateful Absence, Hardlight, Haywire
  Mite, Collective Resistance, Origin of Metalbending, Return to Nature.
- 10 are instant-speed. 7 hit artifacts and 7 hit enchantments.
- This restores the iteration-1 level (the real-power review's main lever). R19 is met.

**Protection.**
- Collective, Origin, Haystack and Make a Stand, plus Veil, which is not confirmed (see F1).
- The win-turn shield (R24) has 3 pieces at MV 2 or less even without Veil.

**Game Changers (2 of 3).** No other Game Changer is owned in Naya. Every RGW Game Changer costs over 3,000. Accepted.

**The cuts.**

| Cut | Right? | Reason |
|---|---|---|
| Rampaging Baloths | Yes | 6 MV; its 4/4 Beast token is not in stock anywhere. |
| Generous Gift | Yes | 1,440 plus a 4,300 Elephant token. Chaos Warp (owned) does the job. |
| Cultivate | Yes | 900 for a fourth 3-MV ramp spell; Chalice is a free landfall with Toph. |
| Myriad Landscape | Yes | 1,440 for a slow tapped fetch; four fetches remain. |
| Solemn Simulacrum | Yes | 4 MV; Haywire Mite is the better slot. |
| **Brightglass Gearhulk** | **No** | See F2. The cut reason ("GGWW 4 MV") ignores what it does here: a two-card tutor and a 4/4 first-strike trampler. It is an artifact, so under Toph it is a land: an entry and an Arbaaz ping, it survives Planar Outburst, and it is a Ragost Food. It finds Zuran Orb (loop B), Mishra's Bauble, Wayfarer's Bauble, Sol Ring, Chalice, Haywire Mite and Hardlight Containment. It is in 82 % of cEDH Toph lists, and the play review rated it medium-high, keep. |

**The 10 weakest nonland cards** (contribution where drawn), each against the best unplayed candidate:

| # | Card | Best candidate | Decision |
|---|---|---|---|
| 1 | Elsewhere Flask (2-MV cantrip) | Brightglass Gearhulk (owned EN, free) | **SWAP** (F2) |
| 2 | Stocking the Pantry (1 card per {2}, needs counters; Terrasymbiosis already uses the same trigger) | Mishra's Bauble (owned EN, free) | **SWAP** (F3) |
| 3 | Veil of Summer (unconfirmed buy, blue and black only) | Redirect Lightning (owned EN, free) | **SWAP** (F1) |
| 4 | Legion Guildmage | Soul-Guide Lantern (owned ES, 1 free copy) | Keep: a 2-drop blocker and tapper, and a 3-to-each sink in floods. |
| 5 | Water Tribe Rallier | none better | Keep: instant-speed, repeatable selection. Earthbent land creatures and artifacts help pay the waterbend cost. |
| 6 | Shared Roots | Nature's Lore (about 2,100) | Keep: an untapped Forest is not worth 2,100. |
| 7 | Explore | none | Keep: an entry and a card for 2. |
| 8 | Haystack | Angelic Intervention (owned) | Keep: the only answer to exile, and an entry with Toph. |
| 9 | Drannith Magistrate | none (Game Changer slot) | Keep: it shuts off commander recasts for the whole table. |
| 10 | Planar Outburst | Fumigate (owned) | Keep: one-sided for this deck (lands, earthbent lands and artifact creatures live). |

**Against the other lists.** It is clearly stronger than iteration 1:
- more real entries that work without Toph;
- the same cheap answers;
- a second engine route;
- a lower failure rate.

It is moderately stronger than the current list:
- 7 to 8 cheap answers instead of 4;
- an average MV of 2.34 instead of 2.61;
- Arbaaz and Chalice back;
- loop B;
- Make a Stand in place of Hakoda.

It is not a new tier. It still has no counterspells and no draw that scales with three opponents (R16).

## 4. Findings and exact changes

| # | Severity | Finding | Exact change |
|---|---|---|---|
| F1 | **fix** | **Veil of Summer fails the money rule.** No price file holds a reading. Live on 2026-11-09:<br>- Game of Magic: the cheapest listing is 3,040 (Core Set 2020; `price_min` across all variants), over the 3,000 line;<br>- Rivendel: no copy;<br>- PayToWin: HTTP 429, not read.<br>The builder's 2,700 to 2,800 is a search hint. The fallback Autumn's Veil is out of stock at Game of Magic and absent at Rivendel.<br>Redirect Lightning is owned and stronger here than the cut log says: for {R} plus {2} or 5 life it moves ANY single-target spell, a counterspell included (onto the Redirect itself), or removal of any color. | `-1 Veil of Summer`, `+1 Redirect Lightning` (owned EN; the free copy, Azula holds the other).<br>Optional: if the lead's live read at PayToWin shows a better-than-Damaged copy at 2,999 or less, the owner may swap back. It has the lowest gain per CLP of all the buys. |
| F2 | **fix** | Gearhulk was cut on a thin reason (section 3). Elsewhere Flask is the weakest artifact slot. | `-1 Elsewhere Flask`, `+1 Brightglass Gearhulk` (owned EN DFT foil, free). The Flask's only copy (Spanish) becomes free for Kilo. |
| F3 | **fix** | Mishra's Bauble is owned, free and a must-have in the primer (B4 average deck; "cheap artifacts are extra land drops"). It is missing from the list and the cut log (R36). With Toph it is a FREE landfall and Arbaaz ping, a delayed card, the 0-cost survivor of the loop B Bombardment variant, and a Gearhulk target. The pool marks it "held by Ezio", but Ezio's final list does not play it. | `-1 Stocking the Pantry`, `+1 Mishra's Bauble` (owned EN, free). |
| F4 | **fix** | Plan file and notes for F1 to F3, plus the Arbaaz wording. | In `.plan.json`:<br>- `tags`: remove Elsewhere Flask, Veil of Summer and Stocking the Pantry; add `"Brightglass Gearhulk": ["tutor", "draw"]` (it puts two cards in hand), `"Mishra's Bauble": "draw"` and `"Redirect Lightning": "protection"`;<br>- `tutors`: add `"Brightglass Gearhulk": ["land_entries"]` (Zuran Orb, both Baubles, Sol Ring, Chalice);<br>- `support.mana_sinks`: remove Stocking the Pantry;<br>- `bad_when_drawn`: replace Elsewhere Flask with `"Mishra's Bauble": "never"`;<br>- plan sentence: replace "turn every entry into 1 damage to EACH opponent with Sabotender, Tannuk, Arbaaz Mir and Valakut Exploration" with "turn every land entry into 1 damage to EACH opponent with Sabotender, Tannuk and Valakut Exploration, and every artifact or legend entering into 1 more with Arbaaz Mir".<br>Update build sections 2, 3, 6, 9 and 11 to match. **Tested on scratch copies:** `plan_density` PASS with 0 failures and 0 warnings, the bracket script PASS, 100 cards, average MV about 2.36. Without the Gearhulk `draw` tag a WARN appears (9 draw cards against 10). |
| F5 | note | The cut log says Aang's Iceberg is "sorcery-speed". It has **Flash**. | Correct the line. The decision stands: Stroke and Chaos Warp cover the slot. |
| F6 | note | The play notes miss two timings: loop B is main-phase only, because the Orb recast is sorcery speed; and Valakut's infinite kill waits for your end step, giving opponents a window. | Add both to build section 5 (win turn: Valakut needs Haystack or Collective up until the end step). |
| F7 | note | The prices of Make a Stand and Return to Nature were cited from a read that was never saved. I re-read them live on Rivendel at 2026-11-09 01:50 UTC: Make a Stand ES 300 (stock 2); Return to Nature ES 150 (stock 7), EN 300. Wood Elves (The Hobbit, Game of Magic) shows 342 to 570 (NM 570). | The lead saves these readings with the final order. |
| F8 | note | There is no table-scaling draw (R16) and no politics section (item 31). Nothing owned or under 3,000 fills R16 in Naya. | Write the reason in the build notes, nothing more. |

## 5. Buys, ranked by gain per CLP (after the fixes)

| Rank | Card | Store | Price (live 2026-11-09) | Gain | Verdict |
|---|---|---|---|---|---|
| 1 | Return to Nature | Rivendel El Concilio | 150, ES "no foil", stock 7 | An instant answer to an artifact or enchantment, and the only graveyard hate | Buy |
| 2 | Make a Stand | Rivendel El Concilio | 300, ES, stock 2 | Team indestructible against destroy wipes; the job Hakoda did | Buy |
| 3 | Wood Elves | Game of Magic Singles | 570 NM (342 for a lower condition, variant not read) | Untapped ramp that is also a creature for Chord, convoke and Ashaya | Buy |
| - | Veil of Summer | none under 3,000 | 3,040+ at Game of Magic; PayToWin unread | Small over Redirect Lightning | **Drop** (F1) |

Toph all-in after the fixes: **1,020 CLP**.
- Builder's plan: about 3,820.
- Earlier plan: 8,650.
- Envelope: 8,000.

No token is needed: the Bear, Beast, Human, Insect, Clue, Food, Treasure and copy tokens are owned, and so is Wrenn's
emblem (TMOM 23, English binder). The new cards make no token.

Spare envelope is no reason to spend. None of the readable candidates under 3,000 beats the owned swaps. Fellwar Stone (1,560),
Farseek (1,640), Nature's Lore (about 2,100) and Lightning Helix (800) are marginal here.

## 6. Real power (1-10; 4 = precon, 7-8 = high power, 9-10 = cEDH)

| List | Salt | Real power | Note |
|---|---|---|---|
| Iteration 1 (`round3-step21`) | 7.4 | 6.6-7.1 | From the real-power review |
| Current after purchases | 7.0 | 7.0-7.4 | From the real-power review |
| New (builder) | not measured | builder 7.3-7.8; **reviewer 7.2-7.6 (central 7.4)** | 0.1 lower than the builder: only 3 true landfall pingers, loops about 1 game in 8, no counterspells, and Veil not secured |
| **New with fixes F1-F3** | to measure | **7.3-7.7 (central 7.5)** | Gearhulk adds a tutor and body, Bauble a free entry and card, and Redirect answers counters and removal of any color |

Confidence: medium-low. No games were played.

## 7. Champion checklist (addendum, 41 items)

| # | Item | Status | Evidence |
|---|---|---|---|
| 1 | One plan plus a backup | APPLIED | Landfall drain; the land army reuses the same entries |
| 2 | Synergy density | APPLIED | Puzzle notes per card; 49 of 61 multi-role |
| 3 | Redundancy of key effects | APPLIED | 24 entry pieces; 3 pingers + Arbaaz + 3 burst pieces; 10 draw |
| 4 | Multi-role slots | APPLIED | R4 count 49 of 61 |
| 5 | Commander-centric balance | APPLIED | About 3 to 5 near-blank without Toph (Chalice, Turf, Orb): 12 or fewer |
| 6 | Land count from curve and ramp | APPLIED | 38, bottom of the profile band, argued |
| 7 | Colored sources | APPLIED | G 22, R 18, W 18 with fetches (recounted) |
| 8 | Total mana sources | APPLIED | 38 + 9 rocks or dorks + 12 land ramp, over 46 |
| 9 | Non-GC fast mana | APPLIED | Sol Ring, Arcane Signet, Talisman; no 3-MV rocks |
| 10 | Tapped-land cost | APPLIED | Turf + 4 fetches; written landfall exception |
| 11 | Window mana | APPLIED | Instant ramp at opponents' end steps; Provisioner Treasures |
| 12 | Curve by archetype | APPLIED | Average MV 2.34; 36 cards at 2 or less |
| 13 | Commander MV and tax | APPLIED | 4-MV enabler, recast twice |
| 14 | Lands and curve at higher power | APPLIED | Compared with B4 (34) and cEDH (29) |
| 15 | Engines versus one-shots | APPLIED | Terrasymbiosis, Tracker, Tannuk, Valakut |
| 16 | Card advantage that scales | **NOT APPLIED** | No such piece owned or under 3,000 in Naya (F8, note) |
| 17 | Development before card advantage | APPLIED | Draw at turns 2-3 costs 2 or less, or is an engine |
| 18 | Tutors | APPLIED | Chord, Seismic Sense, Rallier, Crop Rotation (+ Gearhulk after F2) |
| 19 | Cheap instant answers | APPLIED | 11 spot, 8 at 2 MV or less, 10 instant, 7 artifact and 7 enchantment |
| 20 | Stack interaction | APPLIED | Veil, which F1 replaces with Redirect Lightning |
| 21 | Wipes as a reset | APPLIED | Planar Outburst is one-sided for a land deck |
| 22 | Graveyard hate | APPLIED | Return to Nature (thin: one piece) |
| 23 | Commander protection in layers | APPLIED | Collective, Origin, Haystack, Make a Stand, Veil or Redirect |
| 24 | Win-turn shield | APPLIED | 3 at MV 2 or less without Veil |
| 25 | Answers across permanent types | APPLIED | Creature, artifact, enchantment, planeswalker and graveyard covered |
| 26 | Compact routes | APPLIED | Primary is a repeatable engine; loops are backups |
| 27 | Disjoint routes against three opponents | APPLIED | 4 routes, each hitting every opponent |
| 28 | No shared failure point | APPLIED | Failure-point table in build section 1 |
| 29 | Threat assessment | APPLIED | Gauntlet and fears written |
| 30 | Archenemy timing | APPLIED | "Never present lethal one turn before protecting it"; instant-speed ramp |
| 31 | Politics | **NOT APPLIED** | No section; low impact for a symmetric drain (note) |
| 32 | Wipe recovery | APPLIED | Lands return; Valakut stays; Chord, Rallier, Wrenn; commit rule written |
| 33 | Mulligan standards | APPLIED | Keep checklist; 95.6 % keep with the free mulligan |
| 34 | Game Changer slots | APPLIED | 2 of 3; the third is priced out, with the reason written |
| 35 | Efficiency over value | APPLIED | The three 5-drops each win or reset |
| 36 | High-power non-GC cards | **NOT APPLIED** | Mishra's Bauble (owned) was never considered; Gearhulk was cut on a thin reason (F2, F3) |
| 37 | Bracket 3 combos | APPLIED | Loops flagged; verified here (section 2) |
| 38 | Goldfish protocol | APPLIED | 20 hands, 5 goldfish games, 3 disrupted games |
| 39 | Gauntlet | APPLIED | Five opponent types written |
| 40 | Cut process and log | APPLIED | Cut log and final pass written (Iceberg error, F5) |
| 41 | Real-game evidence over score | APPLIED | Play review and real-power review used; proven cards in |

**Count: 38 APPLIED, 3 NOT APPLIED, 0 N/A.** Item 36 matters, and fixes F2 and F3 close it. Items 16 and 31 are notes.

## 8. Verdict

**FIX**, ranked:
1. F3: `-1 Stocking the Pantry +1 Mishra's Bauble`.
2. F2: `-1 Elsewhere Flask +1 Brightglass Gearhulk`.
3. F1: `-1 Veil of Summer +1 Redirect Lightning`, and drop the Veil buy.
4. F4: update the plan file and the notes.

All three swaps use owned, free copies. The gate and the bracket check pass on the fixed list. Toph's spend falls to 1,020 CLP.

Champion-level for this collection and this budget: **yes, after the fixes.** The remaining gaps cannot be closed under
the 3,000-per-card rule or in Naya:
- a third Game Changer;
- counterspells;
- draw that scales with the table;
- Urza's Saga, Dryad or Amulet-type fast landfall.
