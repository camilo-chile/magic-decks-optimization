# Adversarial review of the consistency gate (2026-10-31)

Reviewer: Opus 5.5 (high), read-only. Subject: the consistency gate of `docs/proposals/phase2-collection-optimization.md`
(section "Consistency gate"), its survey `docs/research/phase2-consistency-survey-20261031.md` and its code
`scripts/plan_density.py` (thresholds in `GATE`, tests in `tests/test_plan_density.py`). Evidence: the Ezio list as owned
(`decks/scanned/ezio-auditore-da-firenze.txt`, checked identical in cards to `decks/phase2/ezio-auditore-da-firenze.txt`: the
only diff is the `// Main` header and 8 Swamps written as 4 + 4), Oracle texts from `data/cache/cards-facts.json` (87 entries,
basics excluded), power and toughness from `data/cache/oracle-cards-20261011210156.jsonl.gz`, and the play review
`docs/research/play-review-ezio-20261026.md`. Every run below was done in a scratch folder; nothing under `scripts/`, `tests/`,
`decks/` or `data/` was changed. The owner's account of the two games is signal from two games, not proof; it was not verified.

## Task 1: the gate on the deck that failed

### The plan file
`docs/research/phase2-gate-test-ezio.plan.json`, written as an honest builder who wants the list to pass, from the Oracle texts:

- Plan: Assassin tempo. Connect on turn 2 to 3 with cheap menace or evasive Assassins and Ezio, cast more Assassins for
  freerunning {B}{B} after a hit, draw off every hit, then set one player to 10 with Magister Sphinx (cast, tutored, reanimated
  or copied) and kill that player with Ezio's trigger paying {W}{U}{B}{R}{G}.
- Backup: Etrata, the Silencer as unblockable removal that accumulates hit counters (Ravenloft Adventurer, copiers), and plain
  Assassin beatdown with Arno Dorian.
- Win routes: "Ezio kill after Magister Sphinx" (Ezio, Magister Sphinx, Chromatic Lantern); "Etrata hit counters" (Etrata, the
  Silencer, Ravenloft Adventurer, Strionic Resonator, Lithoform Engine, Return the Favor).
- Functions and pieces (Oracle based):

| Function | Pieces | Cards |
|---|---|---|
| Connect: evasion past blockers | 8 | Desmond Miles, Winter Soldier, Etrata the Silencer, Lydia Frye, Evie Frye, Secret Tunnel, Assassin Gauntlet, Magister Sphinx |
| Cheap Assassins (MV 3 or less) for freerunning | 8 | Desmond, Winter Soldier, Evie, Lydia, Jacob Frye, Adewale, Etrata Deadly Fugitive, Royal Assassin |
| Card flow on combat damage | 8 | Coastal Piracy, Ezio Blade of Vengeance, Assassin Gauntlet, Desmond, Etrata Deadly Fugitive, Jacob, Theater of Horrors, Tome of Legends |
| Kill setup: a player at 10 | 5 | Magister Sphinx, Loyal Inventor, Reckless Handling, Seismic Sense, Entomb |
| Any-color mana for {W}{U}{B}{R}{G} | 8 | Chromatic Lantern, Command Tower, Arcane Signet, Exotic Orchard, Abstergo, Rumble Arena, White Lotus Hideout, Survivors' Encampment |
| Recursion of Sphinx or an Assassin | 6 | Restart Sequence, The Revelations of Ezio, Jacob Frye, Kolaghan's Command, Abstergo, Starfall Invocation |
| Re-use an enter or combat trigger | 7 | Deadeye Navigator, Venser, Kaya, Ember Island Production, Strionic Resonator, Lithoform Engine, Return the Favor |

- Tags (86 non-basic cards, one each): land 22 (+13 basics = 35), ramp 8, draw 9, removal 18, protection 3, engine 20,
  payoff 3, backup 2, orphan 1 (Intruder Alarm). Single-tag choices that were forced: Dualcaster Mage and Mana Leak as removal,
  Mystical Teachings and Seismic Sense as draw (there is no tutor tag), Kaya as draw, Secret Tunnel as land although it is the
  best evasion piece, Kolaghan's Command as removal although it is also recursion.

### Result (scratch run, `.../scratchpad/gate/reports/consistency-ezio-auditore-da-firenze.md`)
**FAIL**, three reasons, all density:
1. Kill setup: 5 pieces (minimum 8), 57 % to see one in 15 cards.
2. Recursion: 6 pieces, 64 %.
3. Re-use of triggers: 7 pieces, 70 %.

Warnings: 8 ramp (template 10), 35 lands (template 36 to 38). Orphans 1 (limit 3), routes 2 and disjoint: both pass.

### Did it fail for the owner's reasons?
Only partly, and by luck of honest declaration:
- It catches the graveyard plan (recursion 6) and the thin Sphinx access, which the owner did not name but which is the real
  weakness of the kill line.
- It PASSES the evasion function at exactly 8, while the owner lost to chump blockers and big creatures. Against eight 1/1
  goblins, menace (Ezio, Desmond, Winter Soldier) and "can't be blocked by power 3 or greater" (Lydia) do nothing; the cards
  that actually get through are Etrata the Silencer, Secret Tunnel, Evie Frye (conditional), Assassin Gauntlet (one opponent)
  and the flying Sphinx: 5 pieces, 45 % by 11 cards, 57 % by 15. The board has one sweeper (Starfall Invocation). 11 of the
  24 creatures have toughness 2 or less (Evie, Deathcap, Royal Assassin, Nekrataal, Adewale 4/1, Lydia, Venser, Ezio, Jacob,
  Winter Soldier, Dualcaster).
- Ember Island Production, Adewale's Vehicle clause and Winter Soldier's Equipment clause are invisible: each has a real use
  for the stated plan (copy Sphinx or Ezio; reveal-six ETB; a 2-mana menace Assassin), so an honest tag is engine, not orphan.
  The gate has no notion of a dead clause or of "bad when drawn early".
- Both win routes need combat damage to a player; the independence check only compares card names.
- The same list PASSES with no card changed if the builder drops the three short functions (run G1 below).

Verdict: the gate fails the Ezio list only because the plan file was written honestly; it does not see the failure mode the
owner described (combat into wide or big boards) and it can be passed by editing the plan file alone.

## Task 2: adversarial review

### (a) Owner's observed failures: caught or not

| Observed failure | Caught? | Evidence |
|---|---|---|
| Many strategies, 1 to 3 cards each | Partly: only functions the builder declares | Undeclared packages found by regex over the Oracle texts: Vehicle 1 (Adewale), Equipment 2 (+ Swiftfoot Boots by type line), face-down 2 to 3, monarch/initiative 3, hit counters 2, return-to-battlefield 3, copy 4, blink 3. None is checked unless declared |
| Graveyard plan with 2 reanimation spells | Yes if declared (6 pieces fails); no if the builder drops the function (G1 passes) | Runs below |
| Combat damage into 8 chump blockers and 2+ big creatures | **No.** Item 4 of the proposal ("an answer to wide boards and to bigger creatures") is not in the code at all | `check()` has no such test; "evasion" passes at 8 with menace pieces that 1/1s block |
| Ember Island sat in hand (partner never came) | No | Honest tag is engine (copies Sphinx or Ezio); the problem is timing and board state, which the gate does not model |
| Adewale's Vehicle recursion with no Vehicles | No | The proposal calls Adewale an orphan, but his ETB needs no partner; the defect is a dead clause, not an orphan |
| Winter Soldier wants Equipment, list has ~2 | No | Same: dead clause |
| Salt rewards ideal draws | Partly | The function odds table is the only draw-dependent number; no curve, mulligan or mana test |

### (b) How it can be gamed (each verified on the Ezio list in scratch, with the 3 short functions removed as base "G1")

| Trick | Result | Cheap counter-check |
|---|---|---|
| G1: drop the functions that come out short | PASS, list unchanged | Every engine, payoff and backup card must appear in a declared function or win route. On G1 this flags 10 cards (Entomb, Restart Sequence, Revelations, Loyal Inventor, Reckless Handling, Deadeye, Ember Island, Roshan, Arno, Queen Marchesa); on the honest plan 3 |
| G2: merge three short functions into one ("get Sphinx triggers", 18 pieces) | PASS | Cap a function's pieces to those that do the SAME job (one verb); Opus review of function names; report each function's pieces grouped by its role (find, return, copy) |
| G3: win routes naming cards not in the list, single-card routes, or EMPTY routes `{"A": [], "B": []}` | PASS in all three cases | Route cards must be in the list or the command zone, at least one card each (bug: routes are never validated, unlike functions) |
| Independent-looking routes: both need combat damage to a player | PASS | Each route declares its axis (combat, non-combat, alternate win) and what it needs to resolve; require one route that wins through the reference wide board |
| G4: tag Mishra's Bauble as land, Loyal Inventor and Evie Frye as ramp | PASS and both warnings vanish | Check tags against the type line (land only on lands) and, where cached, against Scryfall oracle tags (`function_tags.py` cache has only ramp, mana-rock, mana-dork today; it agrees with the honest ramp count of 8) |
| Relabel the orphan (Intruder Alarm as protection); tag the commander "orphan" | PASS, no warning | Commander tags should warn; orphans should come from an objective rule (plan card in no function) rather than self-declaration |
| Evasion function padded with menace and conditional evasion | PASS at 8 | Define evasion against named reference boards (see d) |
| Repeating a card 8 times in a function | Correctly FAILS (set) | none needed |

### (c) Where it would fail a good deck

- **Commander-centric decks.** A function supplied by the commander counts 0 pieces (run G7: a function listing only Ezio fails
  with "0 pieces"). Ezio himself is a 2-mana menace Assassin always available, so "turn on freerunning" is near-guaranteed; a
  Voltron or commander-engine deck would be forced to pad. Fix: the commander counts as a guaranteed piece (odds 100 % when
  castable).
- **Small, high-impact functions.** Sweepers (templates: 2 to 3), finishers (3 to 5 strong ones), a two-card combo plus 4 to 6
  tutors. Five strong finishers are 57 % by 15 cards but 68 % by 20 and higher with 10 draw spells; the gate ignores draw volume
  and tutors unless they are listed as pieces, and it applies the same 8 to an early engine and a late finisher.
- **One robust route.** A go-wide deck with five overrun effects and anthems has one route; the rule "2 routes" makes it split
  the route artificially (which G3 shows costs nothing).
- **Aggro is the opposite case: false PASS.** Creature-based functions reach 8 trivially, which is exactly why the Ezio list
  passes on evasion and cheap Assassins.
- **Low-curve lists** get the 36 to 38 land warning (warning only; Ezio averages MV 2.88 over 64 non-land cards with 8 ramp).

### (d) Missing checks that matter in 3 to 4 player pods

| Missing check | Ezio data | Cheap implementation |
|---|---|---|
| Reference boards: (1) eight 1/1 chump blockers, (2) two creatures bigger than yours | Outs vs (1): 5 (Etrata Silencer, Secret Tunnel, Evie, Gauntlet, Sphinx) + 1 sweeper; vs (2): 12 spot removal, deathtouch on 5 creatures | Two mandatory functions in the plan file ("through a wide board", "through big blockers"); the same density rule |
| Sweeper resilience | 23 creatures, 11 with toughness 2 or less; insurance: Swiftfoot Boots (one creature), recursion 6, no team protection | Count plan pieces that are creatures (type line); warn when over 60 % and "rebuild after a wipe" has under 4 pieces |
| Spot removal on the commander | Both routes use Ezio's combat or need combat; commander protection: Swiftfoot Boots, Venser, Return the Favor, Mana Leak | If the commander is in a win route, a "commander protection" function with a minimum (judgment: 4) |
| Closing a multiplayer game | Ezio's kill removes ONE player per trigger, each needing a player at 10 and {W}{U}{B}{R}{G}; Etrata needs 3 counters per player | Each route states how it beats 3 opponents, not 1 |
| Mana and curve | 35 lands; about 6 lands make colorless by default; Clifftop, Fortified Village, Game Trail often tapped (1 Plains, 1 Mountain, 1 Forest); Monte Carlo: 77 % of 7-card hands hold 2 to 5 lands, 76 % hit 3 lands by turn 3 on the draw | Report tapped-land count and colored sources per color from the type lines; flag any color the plan needs on curve with under about 15 sources (Karsten-style number, unverified) |
| Bad when drawn early or late | Early: Ember Island, Strionic, Lithoform, Tome, Deadeye (6 MV), Sphinx (7); late: Mana Leak, Fatal Push, Mishra's Bauble, 2-mana rocks, Rampant Growth | Builder adds "bad when" per card (early, late, never); warn when the total is over 12 (judgment) |
| Interaction versus plan | 18 cards tagged removal versus 25 plan cards (39 % of non-lands); 12 spot kills is heavy one-for-one in a 4-player pod (play review) | Report the ratio; warn when removal exceeds plan pieces or plan share falls under 40 % (judgment) |
| Opening hand / mulligan | not modeled | A goldfish simulation with the London mulligan: P(keepable 7 with 2 to 5 lands and an early plan piece or ramp) and P(plan online by turn N); about 60 lines, offline |
| Wipes | 1 (Starfall); templates 2 to 3 (sourced) | Count wipes separately (new tag or function) |

### (e) The numbers in `GATE`

| Threshold | Value | Status | Proposal and reason |
|---|---|---|---|
| `max_orphans` | 3 | Judgment (no source) | 2 declared, plus every engine/payoff/backup card that sits in no function counts as an orphan. Self-declared orphans are trivially relabeled (G5) |
| `min_function_pieces` | 8 | Weakly sourced: the 8x8 method is a theme size, not a probability target; the 75 % is derived | Split by timing, counting tutors that can fetch a piece and the commander as guaranteed: EARLY functions (needed by turn 4 to 5): at least 10 effective pieces (71 % by 11 cards; 13 gives 81 %); LATE functions (finisher, recursion, closing): at least 6 effective pieces measured at 20 cards (75 %). Judgment, from the hypergeometric table |
| `min_win_routes` | 2, disjoint card names | Judgment; survey section 4 only says "at least one non-combat or evasive route" | Keep 2, but validate cards, require one route that does not need combat damage to a blocked player or that wins through the wide reference board, and state how each route beats 3 opponents |
| `seen_by` | (11, 15) | Math sourced (hypergeometric); the turns are judgment. The "on the play" count (6 + turn) is a two-player convention: in multiplayer no player skips the first draw (Comprehensive Rules 103.8c, recalled, not re-read here), so every seat sees 7 + turn (12 by turn 5, 16 by turn 9); the gate is one card pessimistic | Report (7, 12, 16, 20) and judge each function at the turn the builder says it is needed |
| `base_min.ramp` | 10 | Sourced (templates 8 to 13, ScrollVault median 13) | Keep 10 (warning) |
| `base_min.draw` | 8 | Sourced (templates 10, flag under 8) | Keep 8 warning; count tutors separately (new tag) so draw is not inflated |
| `base_min.removal` | 8 | Sourced (8 to 10 incl. wipes; ScrollVault 5 + 2) | Keep 8; add wipes 2 or more (sourced: 2 to 3; Draftsim 3 to 5) or "mass answers" 2 or more for creature decks (judgment); add a soft maximum (removal over plan pieces, judgment) |
| `base_min.protection` | 3 | Judgment (no source, as the code says) | Split into commander protection (4 when the commander is in a route) and wipe insurance (2); both judgment |
| `land_band` | (36, 38) | Sourced (secondary sources; Karsten's own numbers not found) | Keep as a warning; allow 35 when average MV is under 3 and ramp is 10 or more (judgment) |

Also wrong in the proposal text: "Adewale with no vehicles or blink is an orphan" contradicts the play review (his ETB is a
2-for-1 alone) and the gate's own orphan definition; the right label is a dead clause.

### (f) Paragraph for the deck-building agents (196 words)

> The consistency gate (`scripts/plan_density.py`) is a floor, not the goal, and a reviewer will try to break your plan file.
> Write it from Oracle text before you fix the last twenty cards. Declare every function the list leans on, including the
> ones that come out short; you may drop a function only if you also cut every card that exists for it. Every engine, payoff
> or backup card must sit in a declared function or win route; name any dead clause (a Vehicle, Equipment or partner the list
> lacks). Count the commander as a guaranteed piece and count the tutors that can fetch a piece. Test the list against two
> boards common in 3 to 4 player pods: eight 1/1 chump blockers, and two creatures bigger than yours. Name the cards that win
> through each, the cards that rebuild after one sweeper, and the cards that protect the commander. At least one win route
> must not depend on combat damage through blockers, and every route must say how it beats three opponents, not one. For each
> card, say when it is bad to draw (early, late, never). Commander Salt only breaks ties; never trade consistency for points.

### Table of proposed changes

| Change | Why | Sourced or judgment | Effort to implement |
|---|---|---|---|
| Validate win routes: every card in the list or command zone, at least one card per route | Absent cards and empty routes PASS today (G3) | Bug fix | 10 lines + 1 test |
| Every engine/payoff/backup card must appear in a function or route, else it counts as an orphan | Dropping short functions passes with the list unchanged (G1); flags 10 cards there | Judgment | 10 lines + 1 test |
| Two mandatory reference-board functions ("through 8 chump blockers", "through 2 bigger creatures") with the density rule | Item 4 of the proposal is not implemented; the owner's actual loss mode | Judgment (survey: no numbers for wide boards) | 15 lines + plan-file schema change |
| Commander counts as a guaranteed piece; tutors counted as pieces of what they can fetch | False FAIL for commander-centric decks (G7); tutors are the cheapest density | Judgment (math sourced) | 20 lines |
| Early/late function classes: 10 effective pieces by 11 cards, 6 by 20 cards | One number for engines and finishers is wrong both ways | Judgment from the hypergeometric table | 15 lines + schema field `needed_by_turn` |
| Tag checks against the type line (land) and Scryfall oracle tags when cached | Mistags clear the warnings (G4) | Objective (Scryfall tags, community-made) | 20 lines; run `function_tags.py` to completion first (cache holds 3 of 26 tags) |
| Route axis and multiplayer close: each route says combat or not, and how it beats 3 opponents | Both Ezio routes need combat; Ezio kills one player per trigger | Judgment (survey section 4, qualitative) | Schema + 10 lines |
| Wipes counted (2 or more) and wipe insurance (2 or more) | Ezio has 1 sweeper and no team protection with 23 creatures | Wipes sourced (2 to 3); insurance judgment | New tags, 10 lines |
| Allow a secondary tag, add `tutor` and `wipe` tags | One tag forced Dualcaster and Mana Leak into removal, Teachings into draw, Secret Tunnel out of evasion | Judgment | 15 lines |
| "Bad when drawn" field per card; warn over 12 | Ember Island and 6 to 7 MV cards rot in hand; Mana Leak and Fatal Push rot late | Judgment | Schema + 5 lines |
| Mana report: tapped lands, colorless lands, sources per color | Ezio: 6 colorless-default lands, 3 reveal/check lands often tapped | Judgment (Karsten-style thresholds unverified) | 30 lines over cards-facts |
| Goldfish and mulligan simulation (London) | No opening-hand or "online by turn N" test; Salt measures ideal draws | Math sourced; keep rules judgment | About 60 lines + tests |
| Rewrite the proposal's Adewale example as a dead clause, not an orphan | Contradicts the play review | Evidence (Oracle text) | 1 line of docs |

Unverified: the owner's game details; Karsten's land and source numbers; rule 103.8c (no first-draw skip in multiplayer;
recalled, not checked against a rules snapshot here); the Monte Carlo figures (one seeded run, 200,000 hands, approximate); Scryfall oracle tags other than ramp, mana-rock and mana-dork (not cached).
