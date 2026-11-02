---
name: commander-deckbuilding
description: Expert method to build, upgrade, cut or review a 100-card Commander deck for casual 3 to 4 player pods at Bracket 3. Use it to read a commander and derive its profile (one plan, the functions it needs with a count and a reason for each, land count, curve, win routes, interaction mix), to choose and cut cards, to judge a list's consistency, and to write or attack the plan file that scripts/plan_density.py checks.
---

# Commander deckbuilding method

This skill turns research into a procedure. Follow the steps in order. Every number here is either sourced (the note in
`docs/research/commander-deckbuilding/notes/` is named; notes/13 holds the ratio sources K1 K2 K3 Karsten, CZ-new the
Command Zone 2025 template, E1 the EDHREC Bracket 3 averages), marked **[J]** for builder judgment, or marked
**[owner signal]** for a lesson from the owner's play kept as a general principle. The skill's own files sit
in `.claude/skills/commander-deckbuilding/`: detail lives in `references/`, machine-readable profiles in
`archetypes.json` (schema 3). Paths like `scripts/...` and `decks/...` are relative to the repository root.

## Principles (read first)

1. **One plan.** A deck wins with one declared plan and at most one backup that reuses most of the same pieces. Several
   small plans with one to three support cards each lose to a focused deck (notes/03 S5; notes/11 S3; notes/06 S14).
2. **Ratios follow the plan's fuel, not a template.** Templates (Command Zone 2025: 38 lands, 10 ramp, 12 card
   advantage, 12 targeted and 6 mass disruption, about 30 plan cards, notes/13 CZ-new) are starting points that their
   authors say must bend by strategy (notes/01 S2 "training wheels, not scripture"; notes/09 S2). A deck may need far
   more of one function than another does. Step 3 shows how to derive the counts.
3. **Every card does something alone and with many others.** A card whose only use is a partner the deck rarely has rots
   in hand (notes/11 S3 layering; notes/11 S4 engine without enablers). Name every dead clause.
4. **Judge a card in this deck, at the turn it will be cast.** Fit, role, replacement and mana decide, not raw power or
   popularity (notes/08 S2; notes/09 S8: synergy is not power, popularity is not quality).
5. **Multiplayer changes the math.** Three opponents at 40 life is 120 life (notes/12 C3); one-for-one trades leave you
   behind the players who spent nothing (notes/04 S2); a kill that removes one player per trigger needs three resolutions
   (inference and [owner signal], notes/05 section 3).
6. **Bracket 3 is a rules check, never a power cap.** Stay inside the bracket's rules (step 12) and nothing else: how
   strong the deck is, and what bracket or power number a site or a bot labels it with, never limits a choice. A power score (Commander Salt) measures ideal draws; it is
   the second objective: once a list passes the consistency gate and the review, raise its score with swaps that keep both
   passing. Never trade consistency for points.

## 0. Inputs and outputs

Inputs: the commander's exact Oracle text and rulings (Scryfall API), the card pool (what may be played), any lists the
owner or caller marks as proven, the reference boards of the pod (section 7), and the bracket target.

Outputs, in this order (the plan file is written before the last twenty cards are fixed, step 14):
1. **Commander reading** (step 1), 10 to 20 lines, ending with **rules points to verify**: each load-bearing rules
   assumption, whether the rulings confirm it, and which part of the verdict falls if it is wrong.
2. **Plan and backup**, one sentence each (step 2).
3. **Function profile table** (step 3): every function with min, target, actual count, needed_by, and the reason.
4. **The 100-card list**, grouped by function, with a one-line "how to use it in this deck" note per card: when to cast
   it, what to hold it for, what it pairs with, when it is a bad draw; never its rules text. Pattern: "Cast it in
   response to removal aimed at the engine; pairs with the engine permanents; bad draw before the engine exists."
5. **The plan file** `decks/phase2/<slug>.plan.json` for `scripts/plan_density.py` (step 14).
6. **Cut log**: every card considered and cut, with the reason (step 11).
7. **Self-review** answers (step 15).

## 0b. Upgrade mode (the deck already exists)

When the task is to upgrade, cut or review an existing deck, start from the owner's current list and play notes, never
from a blank pool. Read `references/role-players-and-upgrades.md` sections 2 and 4.
1. Each card the owner reports as having won or nearly won games is a **proven role-player** (step 9). Each loss he
   describes names a function that was missing in that game; write which one.
2. Diagnose the current list with steps 1 to 3 before choosing any card. Changes go first to the functions under min.
3. Every card that leaves the owner's list goes to the cut log with the role-player test (reference section 2). Cutting a
   proven role-player needs a written reason the owner reviews.
4. Change the fewest cards that close the gaps [J]. A list that keeps the owner's engine and fixes its short functions
   beats a rebuilt list with a higher score that nobody has played.
5. Comparing two versions: score each on (a) fuel and mana by turn 5, (b) a route that beats three opponents, (c)
   protection of the engine, (d) the functions behind the owner's reported losses. Say which failure is worse for this
   commander and why. Consistency alone does not win: a list that cannot close loses as surely as one that stumbles.

## 1. Read the commander

Read the Oracle text and the rulings, not a summary. Answer each question in writing.

| Question | What to look for |
|---|---|
| What does it reward? | Its trigger words: land entries, casts, attacks, combat damage, tokens, counters, deaths, graveyard, enters, artifacts, enchantments, a creature type, attached equipment or auras, a life threshold. Match them to `archetypes.json` `recognize`. |
| What does it need to work? | The resource it converts every turn (its **fuel**): land entries, spells in hand, attackers that connect, bodies, cards in the graveyard, counters. Also the **window** in which it acts (my combat, my end step, any time) and any mana that exists only in that window. |
| How does it win? | Does it kill by itself? One player per trigger, or the whole table? What must be true first (a life threshold, a board size, a payment)? A conditional kill is the `alternate_kill` profile. |
| How does it die? | Targeted removal, wipes (destroy, exile, -X/-X, bounce, sacrifice), blockers, graveyard hate, "can't attack" or tax effects, sorcery-speed locks, being tapped when the crack-back comes. |
| How dependent is the deck on it? | **Engine** (the plan stops without it: it must attack, cast or trigger every turn; an **attack engine** acts only by attacking or connecting and is the visible threat), **enabler** (it starts the engine, the 99 can run it), **value** (a bonus). This sets the commander protection count (step 6). |
| What does its cost imply? | Mana value and colors set the curve and ramp aims; a costly commander may be cast rarely, so the 99 must carry games (notes/01 S1). Tax arithmetic [J]: each recast costs 2 more, so an engine commander answered twice by turn 8 costs 4 extra mana and two engine turns; a cheap commander tolerates removal but needs haste and protection to matter between recasts, a costly one needs protection more than recursion. |
| Which clauses could be dead? | Any clause that needs a card type, partner or resource the pool barely has. Either commit to it (enough pieces) or accept it as dead and do not build toward it. |

Then check the clauses that interact with the rules and write each load-bearing one as a **rules point to verify**.
Families: does a copy, a token or a permanent that changed type count as what the trigger names (cast, enters, land,
artifact)? Does a permanent that gains a type also gain that type's abilities (a mana ability, summoning sickness)? Does
mana empty between steps? Does the trigger work in the window the plan uses? Unclear points go to the rulings, not to an
article summary; with no rulings at hand, mark the point "not checked".

## 2. Choose ONE plan and a backup

- Write the plan in one sentence: **engine + fuel + payoff + how it closes against three opponents.** The backup reuses
  most of the plan's pieces (for example the same token makers closing by drain instead of combat). A backup that needs its
  own package of cards is a second plan: refuse it.
- If the commander rewards two archetypes, apply the `hybrid` rule in `archetypes.json` `meta`: one primary, the secondary
  only where its pieces also serve the primary. A secondary that is only a modifier is sized as a support line.
- Pick the plan with the most functional support in the pool, not the flashiest line. A plan that leans on one
  specific card (a two-card combo, one engine permanent) needs tutors and redundancy or it is not a plan (notes/08 S12:
  resilience comes from redundancy, tutor access, protection, recovery, and pieces that keep value alone). Read
  `references/archetypes.md` for the archetype's needs, traps and what to look for.

## 3. Derive the function profile (the core step)

### 3.1 Start from the archetype profile
Open `archetypes.json`, take the matching archetype (or the hybrid), and copy its five `base` floors and its `functions`
with `min`, `target`, `tier`, `needed_by` and `why`. `base.removal` means spot answers only (wipes are separate) and
`base.protection` is COMMANDER protection by dependence class (step 6). Every count must now be adjusted to THIS
commander and written down with a reason. The base floors are counted by tag; the plan functions are sized by the fuel.
Every profile already carries the two reference-board functions `through_wide_board` and `through_big_creatures` (step 7).

Each plan function has a **tier**:
- **gate**: declared in the plan file `functions` (step 14). Its min already meets the gate's class: 10 effective
  pieces if needed early, 6 if needed late. Payoff functions have an alternative (`if_commander_is_payoff`), and so do
  source functions such as token makers, counter sources and fodder (`if_commander_is_source`): when the commander is
  itself the guaranteed payoff or source every turn it is out, the other pieces are backups for when it is removed, judged
  late (6) [J].
- **support**: a profile line with its own smaller min (for example haste 4, defense while tapped 4, extra land drops 5).
  The builder and the reviewer check it, but it is NOT declared alone in the plan file (it would fail the gate's
  class). Its cards go inside the gate function whose job they share (`counts_inside`: extra land drops inside
  `land_entries`, team evasion inside `through_wide_board`) or under their primary tag (protection, draw, ramp). Support
  mins assume REPEATABLE permanents; a one-shot effect counts half [J] (four one-shot pieces give 9 % to see two by turn 7,
  `references/probability.md` B).
- **Promotion test [J].** Promote a support line to a gate function when the plan does nothing on a turn the line is
  missing. Haste: promote when the commander acts only by attacking AND (it costs 4 or less, so it is recast the next turn
  and haste decides whether that turn counts, OR the plan needs its trigger on three or more of turns 4 to 8). Otherwise it
  stays support (4 to 6). Detail: `references/win-routes.md` section 4.

### 3.2 Size the fuel
The commander converts one resource per turn into value. A template assumes one card per turn of fuel. Ask: how much
fuel per turn does the plan want, and how much does the deck supply naturally?

| If the fuel is... | The natural supply is... | So the deck needs more of... |
|---|---|---|
| Land entries | one land drop a turn, while lands remain in hand | land ramp that puts lands onto the battlefield, extra land drops, land recursion, fetch lands, a high land count so extra drops have lands to play (notes/07 S1; notes/11 S14; notes/13 E1) |
| Spells cast (instants, sorceries) | the cards in hand, which each cast spends | card draw that nets cards (not cantrips), cheap spells, a high instant/sorcery count, mana in the commander's window (notes/03 S2: draw-built commanders 15 to 20) |
| Attacks that connect | one attack step a turn, if the attackers live and get through | haste, team evasion that beats the pod's blockers, protection, defense while tapped, combat-tied draw (notes/06; notes/12) |
| Bodies that die | the creatures you cast | token makers, recursion, free sacrifice outlets (notes/10 S11) |
| Cards in the graveyard | discards and deaths | cheap fillers, several revival spells, targets (notes/07 S3) |
| Counter placements | sources on board | counter sources plus doublers and proliferate (notes/10 S6) |
| Life lost or a threshold met by every opponent | the commander's own trigger, one player at a time | team-wide enablers and finishers, then the payment for the kill (the `alternate_kill` profile) |

**Card-flow budget [J].** For the plan's peak turns, write: cards or resources spent per turn cycle, cards gained per turn
cycle (natural draw + engines). If spending exceeds gaining by more than one card a turn, the hand empties within two or
three turns (an empty hand by turn 6 is the sign of too little draw, notes/03 S6). Add draw, or cheaper fuel, until the
budget holds through the turns the plan needs.

**Entries-per-turn budget [J].** For land entries, tokens or counters, write the rate at turns 4 to 8: 1 natural +
repeatable permanents on the board + one-shots spread over those turns; aim for 2 or more. Seven repeatable engines give
only 61 % to have one by turn 5 (`probability.md` A), so one-shots fill the gap (`mana-and-ramp.md` section 3).

### 3.3 Turn counts into odds
Cards seen by your turn N in a multiplayer game are **7 + N** (no player skips the first draw in multiplayer; Karsten
cites rule 800.7, earlier notes 103.8c; neither was re-read in the current rules). Odds of at least one of k pieces
(99-card library, no mulligan, no extra draw; full table and "at least two" table in `references/probability.md`):

| k pieces | by T3 (10) | by T5 (12) | by T7 (14) | by T9 (16) | by T13 (20) |
|---|---|---|---|---|---|
| 4 | 35 % | 41 % | 46 % | 51 % | 60 % |
| 6 | 48 % | 55 % | 61 % | 66 % | 75 % |
| 8 | 59 % | 66 % | 72 % | 77 % | 85 % |
| 10 | 67 % | 74 % | 80 % | 84 % | 91 % |
| 12 | 74 % | 81 % | 86 % | 90 % | 94 % |
| 15 | 82 % | 88 % | 92 % | 94 % | 97 % |

Targets used by the gate (judgment from this table): an **early** function (needed by turn 5) has **10+ effective pieces**
(74 %); a **late** function (finisher, recursion, closing) has **6+** (75 % by 20 cards). Plan-critical early functions
aim for 12 to 15 (81 to 88 %). Fuel that must arrive **repeatedly** (two extra land drops, two attackers with haste)
uses the "at least two" table: 16 pieces give 71 % to see two by turn 7, 20 pieces 83 %; one permanent that works every
turn counts as many one-shot pieces.

State the assumption with every "by turn N" claim. The free first mulligan in multiplayer (notes/11 S13) and every draw
spell raise the real odds, so the table is conservative; tutors add effective pieces (inference, notes/03 section 3:
draw and tutors raise cards seen for every function at once). Opening hands: 2 to 4 lands in 7 is 75 % at 38 lands;
"keepable" is 64 to 71 % per look, 87 to 91 % with the free redo (`probability.md` C) [J].

### 3.4 Counting rules
- A piece does the **same job** (one verb: "puts a land onto the battlefield", "gives haste to an attacker"). Do not merge
  three short functions into one vague function to reach a count.
- The commander counts as a guaranteed piece of any function it performs.
- A tutor counts as a piece of each function it can really fetch for (list it in `tutors`; it carries the `tutor` tag).
- A conditional piece counts only if the condition is met in this deck most games; otherwise it does not count.
  Pattern: "can't be blocked by creatures with power 3 or greater" counts against big blockers, not against small chump
  blockers; "destroy target artifact" counts only if opponents run artifacts; a revival spell counts only if the deck
  fills its graveyard.
- A multi-role card counts in every function it really serves; it carries one primary tag, and the base floors (ramp,
  draw, removal, wipe, protection) are counted on that primary tag, so write second-role counts in the profile table.
- **Weights** (`archetypes.json` `meta.weights`; `references/role-players-and-upgrades.md` section 5) [J]: a one-shot
  effect counts half in a support line; a single 1-damage ping counts half against a wide board (team effects and scaling
  damage count full); a cantrip the commander copies nets a card per copy, so it counts as half a draw piece while the
  commander is out and never as a full one; conditional draw counts half when its condition is not met most turns.
- **Commander-conditional pieces** (the condition is "the commander is on the battlefield"): graded weight (full
  for an engine commander, step 1, with protection at min, down to half with none; formula in
  `references/role-players-and-upgrades.md` section 5); list them apart [J]. When the
  commander's own mechanic performs a support function every turn it is out (extra entries, haste, draw), that line may
  be met by the commander, with the reason written.
- **A condition that is the deck's own main action** (triggers when its creatures attack in an attacking deck, when a
  land enters in a landfall deck, when a spell is cast in a spells deck) counts as met. Check how the card interacts with
  the commander's mechanic in the rulings and write HOW to use it (which permanent to put it on, when), instead of
  rejecting it for its one bad use.
- **Role-player exception.** A conditional piece reported as a game-winner keeps its slot as a role-player even when it
  does not count toward a function's min.

### 3.5 Write the profile table
One row per function: name, min, target, actual, needed_by, the cards, and the **reason the count fits this commander**
(fuel rate, odds target, source). Example rows (pattern only):

| Function | Tier | Min | Target | Needed by | Reason |
|---|---|---|---|---|---|
| token_makers | gate | 12 | 16 | early | Commander rewards bodies; natural rate is one body a turn; plan wants three a turn by turn 5 [J]. |
| counter_doublers | support | 4 | 7 | early | The rate above one placement a turn needs repeatable permanents, not one-shots [J]; cards sit inside counter_sources. |
| haste | support | 4 | 6 | early | Attackers are removed before they attack (notes/06 S4); promote with the test in 3.1. |

**Fit check (every profile, not only hybrids).** Add the mins counting each card once (support lines sit inside their gate
function; land ramp counts in both ramp and land entries) and show the arithmetic. Lands plus that sum must fit in 99. If
they do not, the plan is two plans: cut the weakest function and every card that exists only for it (step 11).

## 4. Mana: lands, ramp, colors, curve

Read `references/mana-and-ramp.md` for the numbers and the colored-source table.
- **Lands.** Start from the archetype's `land_band`. Anchors: Command Zone 2025 template 38; Bracket 3 median 36
  (IQR 34 to 37); EDHREC Bracket 3 averages 34 to 36 outside landfall and 39.5 for landfall (notes/13 CZ-new, E1; notes/11
  S15); simulated cast rates 33 to 35 compact combo, 36 to 37 midrange, 38 to 40 battlecruiser and landfall (notes/02 S2;
  notes/11 S14). Karsten starts at 42 + Sol Ring and cuts one land per 2 to 3 extra rocks, per 3 to 4 cheap cantrips or
  dorks (notes/13 K1). His formula, lands ≈ 31.42 + 3.13 × average MV − 0.28 × cheap (MV 2 or less) ramp and draw pieces,
  comes from 95,143 sixty-card TOURNAMENT decks scaled to 99 cards, not from Commander data (notes/13 K2). A band under
  36 needs both average MV under 2.8 and 10+ cheap pieces. Rule of thumb lands = 31 + colors + commander MV (notes/09 S5).
  When in doubt add a land: cutting mana is a named trap (notes/03 S1 S6).
- **Ramp.** 10, or 12 when the commander costs 4 or more (Command Zone 2025; Karsten finds rocks pay off only with a 4+ MV
  commander, notes/13); Bracket 3 median 13, IQR 10 to 18, counting rocks and rituals (notes/11 S15); big mana up to 15
  (notes/09 S17). A landfall plan sits at or above the TOP of that range (18+) [J, owner signal]: no EDHREC source gives a
  landfall total (notes/09 conflict 2), and its averages tag a median of 28.5 cards as ramp with a broad tag (notes/13 E1).
  Pick the ramp TYPE that also serves the plan: land ramp for landfall, rocks for a commander that must land on turn 3,
  treasure from spells for spellslinger (notes/02 S4; notes/11 S16; notes/07 S4). Ramp adds to land drops, never
  replaces them (notes/03 S5).
- **Ramp timing (timed ramp count).** Ramp is a turn 1 to 3 play; past about five mana a ramp card is no longer ramp
  (notes/07 S1; notes/01 S6: value depends on game stage). For every mana card write the turn THIS deck will really
  cast it, given its curve and the plays that compete for that turn (the commander's cast turn first). It counts in
  `ramp` only if that turn is 3 or earlier [J]. Cards whose output scales with the mana paid now (X-cost rocks or
  dorks, permanents that enter with counters equal to the mana spent) are judged at the size the deck can afford on
  that turn; cast late for a large X they are a turn spent on mana, unless the deck uses what they leave (counters for
  proliferate, an artifact or creature for its synergies). A deck whose turns 2 to 4 are full of plan cards wants 1- and
  2-mana ramp, not 3- and 4-mana ramp [J]. Late ramp should turn into cards or a sink (notes/07 S2). Procedure and
  worked pattern: `references/role-players-and-upgrades.md` section 3.
- **Temporary or window mana.** If the commander makes mana that drains at the end of a step or phase, list what the
  deck can spend in that window, and consider cards that keep or convert that mana (notes/02 section 4). Such a card is a
  role-player for this commander, judged by the problem it solves, not by its rating.
- **Window COSTS.** If the commander's payment must be made in a window and competes with other uses of that turn's mana
  (an alternative cost, a flash spell), count the sources untapped at that step and the colors needed at once
  (`mana-and-ramp.md` section 6).
- **Colors.** Count the pips of the cards the plan casts on curve, per color and per turn, and take the source target
  from Karsten's 99-card table (`mana-and-ramp.md` section 4); rocks and dorks are partial sources. For several colors
  needed AT ONCE, multiply the single-color chances as a floor (`probability.md` E2). Colorless utility lands cost colored
  sources; 4 to 5 color decks should probably skip them (notes/03 S6; the "three or more colors" cut is [J]). Land ramp
  that searches for basics needs enough basic land types. Tapped lands: about 4 to 6 tolerated, each with a payoff
  (notes/02 S5, uncited). Untapped sources early.
- **Curve.** Bracket 3 median average MV 3.11 (IQR 2.83 to 3.44, notes/11 S15); densest at 2 and 3, every 5+ card
  justifies itself (notes/01 S2); Command Zone 2025 shape 9 / 18 / 14 / 10 / 4 / 4 cards at MV 1 / 2 / 3 / 4 / 5 / 6+
  (notes/13 CZ-new). Six or seven cards at 7+ MV leave cards stuck in hand (notes/08 S14). Check plays on turns 2 and 3:
  skipping two-drops leaves dead turns (notes/12 C3).

## 5. Card flow

Read `references/card-flow.md`.
- **Draw.** The default floor is 10 effective pieces; a profile goes lower only with a written reason (notes/03 S1 S2 S3).
  12 card advantage (Command Zone 2025: cards that net two or more; notes/09 S17); 15 to 20 when the commander is built
  around DRAWING cards (notes/03 S2), and extending that to a commander that SPENDS cards is [J]. Count only draw that nets
  cards; cantrips are fuel, not draw (notes/03 S2, SN8). Scry and looting are selection, not draw.
- **Plan-tied draw** (draw on combat damage, on landfall, on casting) counts as draw when the deck triggers it most
  turns, at half weight otherwise. A cheap plan-tied draw card can beat a generic draw spell in its deck (notes/03 S2
  ranks repeatable and multi-card draw first, conditional draw accepted). Copied cantrips: 3.4 weights.
- **Tutors** are not card advantage (notes/03 S2); count them as pieces of what they fetch. Bracket 3 median 4 (notes/11
  S15). Tutor for the finisher or protection, not for the engine the deck should already hold in redundancy (notes/03
  inference; notes/11 S16).
- **Recursion** 2 to 3 for a non-graveyard deck, kept apart from draw (notes/04 S5); more for graveyard plans.
  **Diversity:** keep no more than about half of a critical function in one card type or zone, so one hate card or wipe
  type cannot turn it off [J] (`card-flow.md` 6).

## 6. Interaction and protection

Read `references/interaction-and-protection.md`.
- **Removal** means SPOT answers only: one target per card (destroy, exile, bounce used as an answer, counterspell, steal,
  tap-lock, edict). Wipes are counted apart; total answers = removal + wipes, floor 8 to 10 (notes/04 S2 S4: spot 5 to 8
  plus wipes 2 to 4; Command Zone 2025 targeted disruption 12; Bracket 3 spot median 5). Profile mins are spot-only; 3 to 5
  of them answer must-answer threats; aggressive decks 5 to 7, long-game decks 15+ (notes/09 S17). Prefer two-for-one,
  instant speed, and answers that hit several permanent types (notes/04 S2). Removal is a supporting role (notes/04 S3):
  if the answers outnumber the closing pieces (step 15 defines it), the deck has no plan.
- **Wipes.** Sources range 1 to 5 (notes/04 conflict 1); 3 to 5 is one source's figure for MOST decks, with creature
  decks fewer and control more (notes/04 S1); Bracket 3 median 2. Creature and token decks run 0 to 2, only one-sided or
  synergy wipes [J]; control 3 to 5.
- **Graveyard hate** at least 1 (notes/09 S17). **Answers to opponents' commanders:** 2+ that keep a commander off the
  table or neutralize it (exile-attach, tuck, pacifism-type, steal), because commanders come back (notes/04 S3) [J].
- **Commander protection follows commander dependence** (step 1): engine 5 to 7, attack engine 6 to 10, enabler 3 to 4,
  value 2 to 3 [J, anchored on 5 to 7 total protection, notes/04 S5; attack engines on the 8 to 10 protection spells of a
  voltron guide, notes/13]. Layer it: hexproof or shroud stops targeted removal; indestructible stops destroy and damage;
  phasing stops exile and -X/-X; recursion or rebuild answers sacrifice and bounce (notes/04 S1). Shroud also stops your
  own targeting (notes/04 S6).
- **Wipe insurance** for board-based plans: 2+ pieces, a separate function (team protection, recursion, rebuild
  engines) [J]. **Total protection = commander protection + wipe insurance**; a card counts in both only if it does both
  jobs, and the actual commander's class overrides the profile's default.
- **What the table holds.** From the Bracket 3 medians (spot removal 5, wipes 2, counterspells 1; notes/11 S15), three
  opponents have seen by turn 8 (15 cards each) about 2.3 spot removal, 0.9 wipes (63 % at least one) and 0.45
  counterspells (computed, `multiplayer-politics-and-threat.md` section 6). Plan protection against those numbers.

## 7. Win routes and the two reference boards

Read `references/win-routes.md`.
- **At least two routes**, with disjoint cards, at least one that does not need combat damage through blockers (gate
  rule, judgment). A route's card list holds its CLOSERS only; routes may share the engine pieces that make them work
  outside their lists. Each route says how it beats THREE opponents. Name two or three routes before play (notes/05 S4).
- **Team-wide beats single-target.** Overrun, extra combats, damage or drain to each opponent remove several players per
  resolution; a kill that removes one player per trigger needs three resolutions and is a backup, not the main route
  (notes/05 section 3 inference; notes/12 section 4).
- **Organic combos only.** A combo is welcome when its pieces are cards the plan plays anyway (notes/09 S15: organic
  combos). A card whose only use is to complete a two-card combo is a dead card most games.
- **Test both reference boards** common in 3 to 4 player pods (gate review): (1) **a wide board** of eight or more 1/1
  chump blockers that can be sacrificed; (2) **two or more creatures bigger than yours.** Name the cards that win
  through each. Against (1): flying or unblockable, "creatures can't block" effects, trample on a big attacker, one-sided
  wipes or pingers that scale, non-combat damage (a single 1-damage ping counts half). Menace fails here (notes/12 C10) and
  so does "can't be blocked by power 3+" (notes/06 S3). Against (2): removal, deathtouch, flying, forced blocks, pump,
  power-restricted evasion (notes/12 C1 C4; notes/06 S3); spend removal on the few high-impact blockers first (inference,
  notes/05 section 4, untested).

## 8. Decks that win by attacking

If any route needs combat damage, fill these functions (read `references/win-routes.md` "attacking decks"):
- **Haste**: attackers are removed before they ever attack (notes/06 S4). If the commander must attack, haste must reach
  it after a recast; apply the promotion test (3.1). One sourced deck runs six haste cards (one data point).
- **Evasion that beats the reference boards**, preferably team-wide (one card covers every attacker, notes/06 S3), and
  **protection for attackers and commander** (step 6), against removal AND against wipes.
- **Defense while tapped**: vigilance, deathtouch or reach or flying blockers kept home, attack taxes (they push attacks
  to other players; opponents who can pay still attack), punishment effects, mana held for instant responses
  (notes/05 S5; notes/12 C1 C2 C5). No source gives a count; 4 to 6 [J].
- **Toughness check** [J]: pass when at most a third of the attackers and route cards have toughness 2 or less (a board of
  them dies to pingers and small wipes, and a sacrificeable chump board also kills them, `win-routes.md` Board 1); between a
  third and a half, write the protection that covers them; above a half, fix it (tougher bodies, pump, team protection).
- **Before an all-in attack**, know how the board survives a sweeper (notes/05 S4).

## 9. Card evaluation: role-players versus staples

Read `references/evaluation-and-cuts.md`.
- **Synergy beats raw power when the plan depends on the role.** A card that supplies the commander's specific fuel, or
  fixes the commander's specific weakness (window mana, a missing mana ability, an evasion gap), outranks a stronger
  generic card that does a job the deck already covers (notes/03 S4: widely played staples are the most damaging to a
  theme; fit can outweigh efficiency).
- **Bridge cards (resource keepers and bottleneck breakers).** Judge "what does it do alone" WITH the commander on the
  battlefield, because the commander is always available. A card that keeps, stores or converts a resource the
  commander produces and would otherwise lose, or that removes the commander's specific bottleneck, does its job every
  turn the commander works: it is an engine piece, never an orphan, even if it would do nothing in another deck. Count
  it in the function it unlocks and ask: how much of the commander's output is wasted each turn without it? [J]
  Families and the test: `references/role-players-and-upgrades.md` section 1.
- **Proven role-players are strong priors.** A card the owner or the caller reports as having won games with this
  commander stays unless a written reason, reviewed by the owner, says why it goes. Never cut it because a score, an
  inclusion rate or a "better rated" staple says so.
- **Staples earn their slot** when they do two jobs or are interaction the deck needs to survive (notes/03 S4 S5);
  negative-synergy generic ramp or removal is played for its function and does not outrank an on-plan card doing the same job.
- **Dead clauses and mini-combos.** For every card, ask: what does it do alone, here, on the turn it is drawn? A clause
  that needs a card type the deck barely runs is dead; the card is judged on its other text only. A pair of cards that
  only matter together is two dead draws most games (notes/11 S3 S4).
- **Bad when drawn.** Mark each card bad early (expensive or needs setup) or bad late (narrow early answers); a card that
  is never bad is left out of the list. Cheap ramp is bad late by design, so count it as bad late only above the profile's
  ramp target [J]. More than about 12 such cards is a warning (gate, judgment).
- **The last slots**: prefer cards with a high floor (useful in most game states) over high-ceiling cards that need a
  board [J; no source covers floor against ceiling (notes/08 gap); notes/10 S10 shows board-dependent payoffs are weak
  early]. Between two cards with the same job and equal fit, take the cheaper one [J].

## 10. Fill the list (order)

1. Commander, plan, backup, profile table (steps 1 to 3).
2. Lands at the band; colored sources counted.
3. Plan functions to their min, best pieces first, multi-role cards preferred (notes/03 S5).
4. For an attacking deck, its attack lines BEFORE generic safety: haste, team evasion, defense while tapped, commander
   protection. Slot pressure cuts these first if they wait [owner signal].
5. Safety functions (ramp, draw, removal, wipe, protection) to their min, choosing pieces that also serve the plan.
6. Reference-board answers and win routes.
7. Raise functions toward target in the order of their failure cost: plan-critical early fuel first, then protection
   of the engine, then card flow, then finishers.
8. The last slots: role-players, high-floor cards. Then cut to 100 (step 11). Group by function to expose gaps, surplus
   and off-plan cards (notes/03 S5).

## 11. Cut discipline

**Never cut** (without a written reason the owner reviews):
- a piece that takes a function below its min;
- the only answer to a permanent type (the only artifact or enchantment removal, the only graveyard hate);
- a proven role-player (step 9);
- lands below the band to make room for spells.

**Cut first**: orphans (cards in no function and no route); cards with a dead clause and a weak rest; cards bad when drawn
most of the game; surplus in a function already above target; generic staples whose job is covered by on-plan cards;
a second plan's cards.

**Justify every cut** in the cut log: the function it served, that function's count after the cut against its min, and
the card that replaces it. "Lower score" or "lower inclusion" alone is never a reason.

## 12. Bracket 3

Source: `docs/research/commander-brackets-rules-snapshot.md` (beta system, snapshot of 2026-02-09, checked 2026-10-31).

**What this step is for.** It checks the RULES the bracket sets (the bullets below) so the deck does not break them. It is
not a power limit: the strongest list that obeys the rules is the goal. A power score, a bracket label or a "this looks like
Bracket 4 or 5 or competitive" verdict from Commander Salt, a bot or a site is irrelevant, and a higher one is welcome. Never
cut a card, hold back a combo or pick a weaker plan because of such a label. Only a broken rule below is a reason.
- At most **three Game Changers**, lands included. The list changes, so never trust memory or a list stored here: check
  every card against the LIVE Scryfall search `is:gamechanger` (API `https://api.scryfall.com/cards/search?q=is:gamechanger`)
  or the card field `game_changer` when you build; offline, mark a suspected Game Changer "unverified".
- **No mass land denial.** Extra turns only in low quantity, never chained or looped.
- **No intentional early-game two-card infinite combo.** Wizards' test is whether it "tends to happen" in the first six
  turns; "not reachable in the first six turns" is the project's working convention, and holding the combo back does not
  make it acceptable (snapshot, line 39). Late-game lines are allowed.
- Games last at least six turns; wins come in one big turn from earlier resources (notes/05 S1). Global locks and griefer
  cards are legal but draw the table against you (notes/11 S8). Project checks on top: Layer A and `scripts/check_list.py`.

## 13. Using numbers from EDHREC, Commander Salt and other tools

Read `references/tools.md`.
- **EDHREC inclusion, synergy and lift** (notes/09 S7 S9) describe popular decks, most of them not built optimally, and
  precon lists inflate their own cards (notes/09 S6); the Bracket 3 averages by function (notes/13 E1) are range anchors
  only. Use them as **priors**: to find candidates for a function and as a last check for omissions. A high-synergy card
  still has to pass step 9; a staple with near-zero synergy is fine when it does a needed job. Never write "high
  inclusion" or "high synergy" as the reason for a pick or a cut.
- **Commander Salt** power is the second objective: measured on every list that passes the gate and the review, then raised by swaps that keep both passing; it never overrides consistency (principle 6).
- **Scryfall oracle tags** (`otag:`) cross-check your function tags (community-made, imperfect). **Commander Spellbook**
  finds combos in the list; check each against Bracket 3 and the organic-combo rule.

## 14. The plan file for `scripts/plan_density.py`

Write `decks/phase2/<slug>.plan.json` next to the decklist `<slug>.txt` (the script reads only that folder), from Oracle
text, BEFORE fixing the last twenty cards. A reviewer will try to break it. Read `references/plan-file.md` for the schema
and the gate rules. Keys: `plan`, `backup`, `archetype` (and `secondary`, `secondary_role` for a hybrid),
`commander_dependence`, `commander_mv`, `win_routes` (closers only, with `axis` and `vs_three`), `functions` (cards and
`needed_by`; every gate function of the profile under its profile name, both reference boards `early`), `support` (the
profile's support lines, reported and never failed), `tutors` (each also tagged `tutor`), `tags` (primary tag first),
`bad_when_drawn` (`early`, `late` or `never`; only the first two count). The gate fails a function under the larger of its
class minimum (10 early, 6 late) and its profile minimum, a profile gate function that is not declared, fewer than two
disjoint routes, and more than 3 orphans. **When your archetype profile justifies a number outside its warnings (40 lands for landfall, 6 spot
removal with 2 wipes, 1 wipe for tokens), keep it and write the reason in the profile table.**

Honesty rules (gate review section f; full list in `references/plan-file.md`):
- Declare EVERY gate function the list leans on, including the ones that come out short; drop one only together with every
  card that exists for it. Support lines that come out short are reported in the profile table, never hidden.
- A card tagged engine, payoff or backup must sit in a declared function or win route, or it is an orphan. Tag by the job
  the card is in the deck for (primary), not by what makes the counts pass; a tutor counts only for what it can fetch.
- The commander counts as a guaranteed piece of any function that lists it: state the odds with and without it.
- Run `python scripts/plan_density.py` and read `decks/reports/consistency-<slug>.md`. A PASS is a floor, not the goal.

## 15. Self-review checklist and red flags

Answer each in writing before handing the list over.
1. Can I say the plan in one sentence, and does every engine, payoff and backup card appear in a function or route?
2. For each function: count, min, needed_by, odds at the turn it is needed. Any plan-critical early function under 10?
3. Fuel budget: does the plan's fuel arrive at the rate the commander needs through turns 4 to 8?
4. Land count inside the band or justified; colored sources enough for the pips on curve; plays on turns 2 and 3.
5. Commander dependence class and the protection count that follows; protection layered against removal AND wipes.
6. Both reference boards: which cards win through eight chump blockers, which through two bigger creatures?
7. Routes: two or more, disjoint, one not combat, each beating three opponents.
8. Attacking decks: haste, team evasion, protection, defense while tapped, toughness profile.
9. Bracket 3: Game Changers 3 or fewer (live Scryfall check), no mass land denial, no chained extra turns, no early
   two-card infinite.
10. Every cut logged with function and replacement; every proven role-player kept or its cut justified; every rules
    point confirmed or flagged "not checked".

**Red flags** (each needs a fix or a written reason):
- Several packages of one to three cards each beside the plan (any mechanic: reanimation, equipment, vehicles, blink,
  copies, monarch, counters...). Search the Oracle text for them; they are rarely declared.
- A card whose only use is a two-card combo; a clause that needs a card type the list barely has.
- Answers outnumber closing pieces: spot removal + wipes + counterspells above the unique cards of the payoff, attacker,
  finisher and win-route functions (the fuel and the safety tags are not closers; an attacker is a closer only if it passes Board 1 or belongs to a team effect, otherwise it is fuel); many one-for-one answers and few threats.
- Evasion counted with menace or power-restricted evasion against a wide board.
- An attacking deck with no haste, no defense while tapped, or mostly toughness 2 or less.
- A single-target kill as the only route against three opponents.
- Ramp with no payoff or sink; draw that does not advance the kill (notes/11 S17).
- A mana card judged by its rating, not by the turn it will be cast here; cuts justified by a score or inclusion rate alone.
- More than three Game Changers; a two-card infinite reachable by turn 6.

## 16. What a reviewer checks

A reviewer reads only the list, the plan file and the commander's text, and tries to break the plan:
1. Re-derives the commander reading (step 1) independently and compares the fuel and dependence class.
2. Recounts every function from Oracle text with the counting rules (3.4): merged functions, conditional pieces,
   mis-tags (land tag on a non-land, ramp tag on a creature that makes no mana), tutors that cannot fetch what they
   claim, the commander listed in every function. Re-derives every `needed_by`.
3. Looks for undeclared packages: card types or mechanics with one to three cards that serve no declared function.
4. Plays the two reference boards and one sweeper turn against the list; checks the routes (disjoint closers, axis, how
   each beats three opponents, organic combos only), the card-flow budget and the curve on turns 2 to 5.
5. Reads the cut log (proven role-players, functions pushed under min, cuts by score), Bracket 3 (live Game Changer
   search) and the rules points to verify.
6. Reports findings as: the failure, the evidence (card names and counts), the fix, and whether it is sourced or [J].

## References (read when the step says so)

`references/`: `archetypes.md` (steps 2 and 3), `probability.md` (3.3), `mana-and-ramp.md` (4), `card-flow.md` (5),
`interaction-and-protection.md` (6), `win-routes.md` (7 and 8), `multiplayer-politics-and-threat.md` (threat, pacing,
what the table holds), `evaluation-and-cuts.md` (9 to 11), `tools.md` (13), `plan-file.md` (14),
`role-players-and-upgrades.md` (steps 0b, 3.4, 4 and 9: bridge cards, role-player test, timed ramp, weights).
