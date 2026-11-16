# Collection review: Kilo, Apogee Mind, the 100 % Spanish deck (Phase 2 step 13.2, iteration 3, 2026-11-15)

Reviewer: an independent champion (Opus 5.5 high) who tries to beat the list. Under review: `decks/phase2/spanish-deck.txt`
with `.plan.json` and `.build.md` (builder: Fable 5.2 high, step 13.1). Mandate: `docs/proposals/collection-optimization-brief-20261114.md`
("What the reviewer writes"), frozen collection, no purchases, loans or exchanges, Spanish copies only.

**Owner decision received during the review (2026-11-15, overrides point (b)):** Azula, Toph and Ezio are built and frozen;
Kilo may take no copy from them. Swan Song stays in Azula and Kilo keeps Titan Forge (the builder's own fallback). This
review judges the list WITH that change (Swan Song out, Titan Forge in), and every change proposed below uses only free
Spanish copies (`held_by` "free") or copies Kilo already holds.

**Verdict: FIX** (one mandatory change from the owner's decision, two card swaps, one optional land swap, plan-file
corrections). No blocker: the list is legal, Spanish, 100 cards, and passes both scripts.

## 1. Rules

| Check | Result |
|---|---|
| Card count | 100 (1 commander + 99): 37 lands, 62 nonland. Counted by script on the list as written and on every scratch list. |
| `python scripts/check_phase2_bracket.py decks/phase2/spanish-deck.txt` | **PASS**: floor 1, target 3, 0 Game Changers, 0 review items; Spellbook: 1 variant inside the list (Crawler + Lux + Excavation), 0 flagged. Re-run on the real list LAST, after the scratch tests. |
| Live Game Changer check | Scryfall `is:gamechanger` read today: 53 cards; none in the list, none in the Spanish pool. |
| `scripts/plan_density.py` | **PASS**, 0 failures, 0 warnings. Run through `run_plan` into the scratchpad so no other deck's report was touched; the output is byte-identical to `decks/reports/consistency-spanish-deck.md`. |
| Spanish copies | Script over the pool: every card of the list has a Spanish copy that is free or already in Kilo, **except Swan Song** (one Spanish copy, held by Azula: now refused by the owner's decision). Kilo commander: Spanish EOC 3 foil. Islands: Kilo holds 9 Spanish, plays 8. |
| Reversible cards, extra turns, mass land denial | None. |
| Three-card infinite (Lux Artillery + Crystalline Crawler + Meticulous Excavation) | Allowed: three cards, none of them the commander, no early two-card infinite. See (a). |
| Scratch lists | A = owner decision applied; B = A + fixes 1 to 3; C = A + fixes 1 and 2. All 100 cards, gate PASS with 0 warnings, bracket PASS (B). The scratch bracket run wrote `decks/reports/bracket-kilo-scratch-B.md`; I deleted it at once, and the real report was regenerated last. |

## 2. Independent reading (written before opening the plan file and the build notes)

**Commander.** Kilo, Apogee Mind {U}{R}{W}, 3/3 legendary ARTIFACT creature, haste: "Whenever Kilo becomes tapped,
proliferate." Being an artifact matters: improvise (Kappa Cannoneer, Universal Surveillance, Organic Extinction), waterbend
(Waterbending Lesson, North Pole Patrol), station (Inspirit, Uthros) and Relic of Legends all tap him at home, so he never
has to attack into blockers; Steel Overseer pumps him; Alibou triggers when he attacks; Cyberdrive gives him flying; Inspirit
at 8+ gives him hexproof and indestructible. Fuel: permanents already carrying counters. Dependence: **enabler** (13 other
proliferate effects; every closer works without him). MV 3 with haste: a recast is a trigger the same turn.

**Plan.** Rocks and engines with charge or +1/+1 counters; Kilo proliferates them once or twice a round (North Pole Patrol is
the only untapper; Strionic Resonator and Lithoform Engine copy the trigger); counters become mana, cards and removal; close
with Darksteel Reactor (20 charge counters) or Lux Artillery (30 counters: 10 to each opponent every end step). Backup: the
artifact board attacks (Cyberdrive Awakener, Kappa Cannoneer, Alibou, Steel Overseer). Archetype: `plus_one_counters` +
`artifacts`.

**My recount from Oracle text (list with the owner's change: Swan Song out, Titan Forge in).**

| Function | My count | Cards and notes |
|---|---|---|
| Counter sources that feed the closers | 19 | Chalice, Prism, Cornucopia, Crawler, Coretapper, Overseer, Insight Engine, Uthros, Inspirit, Sensor (needs an attack first), Oracle, Peacemaker, Seedshark (Incubators), Lux Cannon, Reactor, Lux Artillery (sunburst), Solar Array, Kappa, Titan Forge. Tranquilize's stun counters sit on an opponent's creature: they count for neither closer. |
| Proliferate and trigger copies | Kilo + 14 | Surge Conductor, Tekuthal (doubles), Thrummingbird (on combat damage), Peacemaker (on crimes), Karn's Bastion, Strionic, Lithoform, Gambit, Augury, Contentious Plan, Volt Charge, Ripples, Skate (doubles counters), Trophy Mage (fetches Surge Conductor). |
| Kilo tap outlets at home | 8 + attack | Relic (instant speed), Inspirit, Uthros (station, sorcery), Waterbending Lesson, North Pole Patrol (waterbend and untap), Universal Surveillance, Organic Extinction, Kappa (improvise). |
| Draw that nets cards | 10 | Uthros, Insight Engine, Sensor, Oracle, Gambit, Thirst, Waterbending Lesson, Universal Surveillance, Jhoira, Thought Monitor. Not counted: Augury, Plan, Star, Sphere, Lantern, Airbending (cantrips). |
| Ramp (lasting) | 9 | Sol Ring, Signet, Chalice, Prism (burst), Relic, Sphere, Solar Array, Cornucopia, Crawler; Mechanaut reduces. Barrels and Star are fixers, not ramp. Cast by turn 3: Sol Ring, Signet, Chalice, Prism (Barrels and Star fix). |
| Spot answers | 9 | Swords, Dispatch, Fateful Absence, Tranquilize, Negate (MV 2 or less: 5); Chaos Warp, Airbending Lesson, Volt Charge (3); Lux Cannon (4, repeatable). Instants 7. Second roles: Barrels (5 damage late), Alibou, North Pole Patrol. |
| Counterspells | 1 | Negate (Swan Song gone). |
| Wipes | 2 | Starfall Invocation (symmetric, the gift returns one creature); Organic Extinction (nonartifact creatures: it also kills 9 of my 21 creatures: Tekuthal, Jhoira, Fireweaver, Seedshark, Patrol, Skate, Trophy Mage, Emry, Thrummingbird). |
| Commander protection | 4 | Airbending Lesson (exile and recast for {2}), Ripples (only if Kilo carries a counter), Inspirit at 8+, Negate. |
| Win-turn shield (R24, MV 2 or less) | **2** | Negate, Ripples. |
| Table-wide closers | 2 (+2 copies) | Darksteel Reactor, Lux Artillery; Phyrexian Metamorph and The Mycosynth Gardens copy Lux once it is out; Fireweaver is a slow drain or the loop's kill. |
| Tutors | 1 | Trophy Mage (MV 3 artifacts only: 10 targets incl. Titan Forge; never Reactor or Lux, MV 4). |
| Graveyard hate | 1 | Soul-Guide Lantern. |

**Lands and colors.** 37 lands: 3 always tapped (Rustvale Bridge, Mystic Monastery, Path of Ancestry) and Radiant Summit,
which needs two basics and so is tapped on turns 1 to 2 in most games (R10 counts it as tapped). Colorless or conditional:
Karn's Bastion (C only), The Mycosynth Gardens ({1} to filter), Rugged Prairie and Cascade Bluffs (filters), Spire of
Industry (needs an artifact and 1 life), Exotic Orchard (needs opponents' lands). Land sources: blue about 18, white about
17, red about 16 (Orchard partial), plus Signet, Sphere, Prism, Relic, Solar Array. Pips: blue 30, white 14, red 9.

**How it loses.**
- *To a wipe.* A creature wipe barely matters (Reactor, Lux, rocks stay). An artifact wipe (Vandalblast, Austere Command,
  Farewell, Bane of Progress) takes the engine, the mana and most closers at once. Before: Negate (the only counter now),
  Ripples, Inspirit at 8+. After: Resourceful Defense moves counters to the indestructible Reactor (a destroy wipe only),
  Emry recasts one artifact a turn, Kilo returns. No mass recovery.
- *To a wide board of small blockers.* It does not need to attack: the Reactor, Lux and Fireweaver ignore blockers; Kilo
  taps at home. Starfall and Organic Extinction clear it. Fine.
- *To two bigger creatures.* Same: noncombat closers; 9 spot answers, Alibou's shot, Tranquilize, Titan Forge's 9/9s.
  The risk is speed, not the board: a big-creature deck kills it before the Reactor reaches 20.
- *To time.* Two table-wide closers and no tutor: P(Reactor or Lux in hand) is 26 % by 14 cards seen (turn 7), 38 % by 21,
  52 % by 30. With the five other closers (Fireweaver, Cyberdrive, Kappa, Alibou, Titan Forge) it is 82 % by 21 cards, but
  those kill one player at a time or slowly.

## 3. Differences with the builder

| Point | Builder | Me | Effect |
|---|---|---|---|
| Swan Song | In (contested from Azula) | Out by the owner's decision; Titan Forge back | Shield 3 to 2, counters 2 to 1, spot answers 10 to 9, protection 5 to 4 |
| counter_sources | 19 + Trophy Mage | 18 + Titan Forge = 19; Tranquilize is not a source for this plan | Still far above 12 |
| through_wide_board | 13 incl. Meticulous Excavation | 12: Excavation passes Board 1 only inside the three-card loop | Still at or above 10 |
| artifact_payoffs | 21 incl. Spire of Industry, The Mycosynth Gardens, Dispatch | 18: two lands and a removal spell are not plan payoffs | Still above 10 |
| Relic of Legends | "taps five other legends" | Tekuthal, Jhoira, Emry, Alibou: four (Inspirit only at 8+) | Wording |
| Organic Extinction | "spares my artifact creatures" | True, and it kills 9 of my 21 creatures, incl. Tekuthal, Jhoira, Fireweaver | Guide note |
| Alibou | "gives haste to everything Cyberdrive animates" | Animated artifacts that were already under my control are not summoning sick; haste matters for Cyberdrive itself and new artifact creatures | Wording |
| Empowered Autogenerator | "Considered and left out", no reason | The best free counter card not in the list (finding I2) | Change |
| Hangarback Walker | Out: "its Thopter token is not owned" | Not a deck reason: the exact-token rule is a check, and the builder accepted Swan Song's unowned Bird the same way | Change (I3) |
| Tapped lands | 3, each paid back | 3 + Radiant Summit (tapped on turns 1 to 2) = 4 under R10's reading; the trade still pays (I5) | Accepted |
| Everything else | | Function counts, routes, closers, draw 10, mana numbers, rules points R1 to R8: confirmed from Oracle text and rulings | |

## 4. Verifications asked by the lead

### (a) Rules claim: off-color mana and the three-card infinite. **Confirmed.**
- The Comprehensive Rules in force (`MagicCompRules 20261106.txt`, downloaded today from media.wizards.com, the link on
  magic.wizards.com/en/rules) section 903 (903.1 to 903.12) has no rule that turns mana outside the commander's identity into
  colorless; identity limits only deck construction (903.4, 903.5c, 903.5d: basic land types). The Commander RC page
  (mtgcommander.net/index.php/rules/, read today) has none either.
- Crystalline Crawler ruling 2016-11-08: an extra cost may be paid {W}{U}{B}{R}{G} for five counters; colors are W, U, B, R, G.
  Lux Artillery ruling 2023-02-04 and CR 702.44d: each instance of sunburst works separately, so converge + Lux's sunburst
  give two counters per color. Commander Spellbook (project cache) lists the loop as variant 1034-1350-2060 with identity W
  and "{4} in four different colors".
- The loop: Lux out; Crawler cast for {4} with four colors enters with 8 counters; remove them for 8 mana of any colors;
  {2}{W} to Meticulous Excavation (my turn only) returns Crawler; recast with four colors (black or green from Crawler's own
  mana): +1 mana per loop, unlimited artifact casts and entries. The first iteration needs about one extra mana (a first
  cast with W, U, R and colorless gives 6 counters).
- Caveats the notes should keep: (1) a cost reducer cuts the colors (Crawler ruling): with Enthusiastic Mechanaut out the loop
  nets 0 (still unlimited entries); with two reducers it breaks; (2) the three cards alone give infinite mana and entries,
  not a kill: the kill needs a fourth card on the battlefield or reachable (Reckless Fireweaver; Surge Conductor + Reactor;
  Jhoira or a stationed Uthros to draw into one; Excavation re-buying Thought Monitor or Etched Oracle with infinite mana;
  Kappa Cannoneer for one player). Most games one of these is present when the loop is assembled.
- **Cards whose value the corrected rule raises** (the previous review assumed the opposite): Crystalline Crawler and Etched
  Oracle (four colors: Oracle draws three the turn it lands), Solar Array and every sunburst card (four or five colors when the
  spell costs that much), Meticulous Excavation (the loop is three cards, not four). Pentad Prism ({2}) is unchanged. No card
  loses value.
- Bracket 3: three-card combo, not the commander, not reachable as an intentional early two-card line: **allowed**.

### (b) Swan Song: closed by the owner's decision.
Swan Song stays in Azula; Kilo plays Titan Forge. The cost in Kilo, for the record: the win-turn shield drops to Negate +
Ripples (R24 asks 3), Kilo has one counterspell, and nothing protects an artifact wipe except Negate and Ripples. **No free
Spanish card restores the shield**: the Spanish pool's free stack and protection cards at MV 2 or less are none (no
counterspell, no phasing, no redirect); Airbending Lesson (MV 3) is the nearest. Titan Forge is a sound fallback here: MV 3
(Trophy Mage target), a charge-counter battery that every proliferate fills and Moxite Refinery or Resourceful Defense can
pour into the Reactor, Lux's count, and 9/9 bodies against Board 2 (Golem tokens: the owner has three Spanish TEOC Golem
tokens, 12 x2 and 14 x1; confirm one is the 9/9 face).

### (c) Meticulous Excavation against Hangarback Walker: **keep Excavation, add Hangarback in another slot.**
- Excavation is the only compact infinite in the pool and has real late uses: re-buy Deepglow Skate (a second doubling: a
  Reactor at 5 becomes 20 in one turn for about 13 mana), Trophy Mage, Thought Monitor, Etched Oracle; reset Chalice or
  Cornucopia with a bigger X; rescue my own permanent on my turn; Kilo back to hand without tax. Bad early, a 1-mana card.
- Hangarback is better than the card it should replace (Thrummingbird, I3): a counter source from turn 2 that every
  proliferate grows, a body for station, waterbend and improvise, an artifact creature for Steel Overseer, Alibou and
  Cyberdrive, and a pile of flying Thopters when it dies (wipe insurance and evasion against Board 1). The unowned Thopter
  token is a token-list line (any marker works), never a deck-building reason.

### (d) The closer access gap: **no real fix exists in the free Spanish pool.**
Searched all 197 pool cards: no artifact tutor beyond Trophy Mage (MV 3), no transmute, no Fabricate or Whir, no Tezzeret,
no Urza's Saga, no Inventors' Fair; Arbaaz Mir (a second Fireweaver for historic entries) is Ezio's Spanish copy and frozen.
What partly closes it, all already in or proposed:
- more cards seen: Empowered Autogenerator (I2) turns into 5 to 8 mana a turn by turn 8, which is X for Universal
  Surveillance and Insight Engine activations;
- faster single closers: Moxite Refinery and Resourceful Defense move Autogenerator's and Titan Forge's charge counters onto
  the Reactor (two batteries more than the builder's list);
- second copies: Metamorph and Gardens copy Lux once it is out; Strionic and Lithoform copy its trigger;
- Long-Range Sensor's discover 4 can hit either closer.
Odds stay at 38 % for Reactor or Lux by 21 cards seen (hypergeometric, 2 of 99); the realistic answer is that the deck
wins with whichever of its seven closers arrives, and that is the ceiling of a Spanish-only collection (no Enlightened Tutor,
Fabricate, Prologue to Phyresis, Walking Ballista or Freed from the Real owned in Spanish).

## 5. Findings, ranked

### BLOCKING
None.

### IMPORTANT

**I1. The list still holds Swan Song (owner decision).** Evidence: `decks/phase2/spanish-deck.txt` line "1 Swan Song";
pool `held_by` {"fire-lord-azula": 1}, one Spanish copy. Fix: -Swan Song, +Titan Forge (Kilo's own Spanish copy). Plan
file: Titan Forge tag `payoff`, bad_when_drawn `never` (as in the HEAD plan), in `counter_sources`, `counter_payoffs`,
`artifact_density`, `through_big_creatures` and the "Artifact alpha strike and Alibou" route; Swan Song out of `tags`,
`bad_when_drawn` and `support.wipe_insurance`. Build notes: sections 3 (shield 2, counters 1, spot 9), 4, 6, 7, 8.
Scratch A: 100 cards, gate PASS 0 warnings (marking Titan Forge `early` instead gives the warning "13 bad when drawn").
Sourced: owner decision 2026-11-15.

**I2. Empowered Autogenerator (free Spanish) is left in the binder with no written reason; Contentious Plan holds a slot.**
- Autogenerator: "{T}: Put a charge counter on this artifact. Add X mana of any one color, where X is the number of charge
  counters." With Kilo's one or two proliferates a round it gives 1, 3, 5, 7 mana on successive turns from the turn after
  it lands: the deck's biggest mana engine, fuel for its sinks (Universal Surveillance X, Insight Engine, Karn's Bastion,
  Excavation, the loop's first iteration, recasting Kilo), a 6-to-10-counter charge battery that Moxite Refinery or
  Resourceful Defense pours into the Reactor, and a chunk of Lux's 30. Enters tapped; MV 4 (same class as the Reactor, which
  the builder marks `never` bad).
- Contentious Plan: a 2-mana sorcery proliferate that replaces itself; the deck has Kilo and 13 other proliferate effects.
Fix: -Contentious Plan, +Empowered Autogenerator (Spanish binder). Scratch C: counter_sources 21 to 22, counter_doublers
15 to 14 (min 10), ramp 12 to 13 by tag, gate PASS. [J], with EDHREC as a prior only (Kilo page: owned and unplayed).

**I3. Thrummingbird is the weakest proliferate; Hangarback Walker (free Spanish) does more here.**
- Thrummingbird proliferates only on combat damage to a player: a 1/1 flier that the builder marks bad late, in a plan that
  keeps its creatures home. Hangarback: see (c). It also raises wipe insurance (Thopters after a destroy wipe, artifact or
  creature) and Board 1 evasion.
Fix: -Thrummingbird, +Hangarback Walker (Spanish binder). Add a Thopter (1/1 colorless artifact creature, flying) to the token
list (not owned; a marker until then). Scratch C: counter_doublers 14 to 13 (min 10, 81 % by 12 cards), through_wide_board
13 to 14, gate PASS 0 warnings. [J].

### MINOR

**M1. Optional: Karn's Bastion for a ninth Spanish Island (already in Kilo).** Three colors needed on turn 3, and the
list has five colorless or conditional lands (Bastion, Gardens, two filters, Spire). My land-play simulation (40,000 games,
free mulligan for 0-1 and 6-7 landers, simple rock model; absolute numbers are conservative, deltas are what count): Kilo
castable on turn 3 rises from 67.5 % to 68.6 % (lands only 59.0 % to 60.1 %). Bastion's {4} instant-speed proliferate is the
15th proliferate effect. Scratch B (all three changes): counter_doublers 13 to 12 (min 10, 78 % by 12 cards), gate PASS.
Small either way; I would make it, the lead may skip it. [J]

**M2. Plan-file honesty (no list change).** Remove Tranquilize from `counter_sources` (stun counters on an opponent's
creature feed no closer), Meticulous Excavation from `through_wide_board` (it passes Board 1 only inside the loop), Spire of
Industry, The Mycosynth Gardens and Dispatch from `artifact_payoffs`. Every function stays above its minimum (19, 12, 18).

**M3. Guide notes.** Organic Extinction kills 9 of my own creatures (cast it when the table loses more); Relic taps four
other legends, not five; the loop needs a fourth card to kill (list them, as in (a)); with Mechanaut out the loop nets 0.

**M4. Tapped lands (asked by the lead).** Rustvale Bridge, Mystic Monastery and Path of Ancestry are always tapped, and Radiant
Summit is tapped on turns 1 to 2 in most games: four under R10's reading of conditional lands, one over its line. The trade
pays: my simulation gives the current land set 67.5 % against 61.6 % for the HEAD land set (Buried Ruin, one more Island
and Mountain), and Path alone is worth 1.3 points over a Plains. Each tapped tri-land is played on turn 1 or 2, when it
costs nothing. Accept; play order: tapped land on turn 1, a two-drop on turn 2 from an untapped land. Path's scry is a dead
clause (5 Robot or Artificer creatures), written by the builder. [J]

**M5. Win-turn shield and counters under the owner's decision.** R24 (3 pieces) and R20 (2 to 4 counters for a tap-out
deck) are now unmet with no free Spanish fix. Not a list change: write it in build section 3, and sequence the win around
Negate and Ripples (hold {1}{U}, bait with a draw spell first).

## 6. Knowledge audit

| # | Source | What it demands of this deck | Met? |
|---|---|---|---|
| 1 | Skill + `archetypes.json` (`plus_one_counters` + `artifacts`) | Gate functions at 10 early / 6 late, band 36 to 37, draw that nets cards (10), a modal card in one function per state, 2 disjoint routes, both boards, tags by job | Yes. Draw 10 nets cards (cantrips excluded, correctly). Small mis-tags in M2. Volt Charge counted as removal and proliferate: fine, both happen on one cast |
| 2 | Champion addendum, 41 items | R8 46 sources, R9 non-GC fast mana, R10 at most 3 tapped, R16 scaling draw, R18 10 access cards, R19 8 spot / 5 cheap / 5 instants, R20 2 to 4 counters, R21 asymmetric wipes, R24 shield 3, R32 4 rebuild pieces, R33 85 % keeps, R34 Game Changers, R36 high-power non-GC | Met: 1 to 8, 11 to 15, 17, 19, 22, 23, 25 to 33, 35 to 41. Not met: **18** (1 tutor, no fix exists), **20** (1 counter after I1), **24** (shield 2 after I1), 10 at the line (M4), 21 partly (Starfall symmetric, Organic Extinction hits 9 of mine). N/A: 9 beyond Sol Ring and Signet, 16 and 34 (none owned in Spanish). With I2 and I3: R8 47 sources, R32 7 pieces |
| 3 | Mana study, `notes/02`, `notes/13` | Karsten regression about 38 lands; 19 sources per color for a gold 3-drop (scaled 17); untapped early; tapped lands 4 to 6 tolerated but R10 caps at 3 | Lands 37; land sources about 18 / 17 / 16 plus 5 any-color rocks: met. Tapped-land trade judged in M4: accept. Colorless lands: M1 |
| 4 | Other notes (01, 03, 04, 05, 07, 10, 11, 12) | One plan; ramp by turn cast; engines over one-shots; "one source is a trap"; team-wide closers; wipe recovery | Met. I2 and I3 replace two one-shot or conditional cards with repeatable counter engines (notes/07, notes/10) |
| 5 | Kilo primer, Spanish commander study | Tap Kilo with costs, not attacks; counters first; close with Lux or the Reactor; the strong lines (Freed from the Real, Pemmin's Aura, Prologue, Ballista, Enlightened) have no Spanish copy; the study's counter-source list names Autogenerator, Hangarback, Golem Foundry, Mindless Automaton, Gavel | Met; the study's two best unplayed sources are I2 and I3. Commander not re-opened |
| 6 | Owner lessons L1 to L10, play reviews, gate review (f) | Section 7 | Met |
| 7 | Previous final review (2026-11-08) | F1 Strionic, F2 Lithoform, F4 Starfall, F7 plan sentence, F8 keep rate, F10 Cyberdrive from lands; F9 tutors | All applied; F9 still open (no Spanish copy). Its claim that a three-color deck cannot make a fourth color was wrong (see (a)); the builder corrected it |
| 8 | Owner card review | Sphere, Waterbending Lesson, Alibou IN; Evie Frye, Torrential Gearhulk, Aether Gale OUT | All six verdicts sound. Sphere: three-color fixer, Trophy target, a card when sacrificed. Waterbending Lesson: Kilo is an artifact creature, so the waterbend taps him for a proliferate and 40+ permanents can pay. Alibou: Kilo attacking is an artifact creature attacking, so every Kilo attack is also a shot of X (tapped artifacts). Evie (Ezio's only copy), Gearhulk and Aether Gale (Azula's only copies) are now also frozen by the owner's decision |
| 9 | Dead clauses | Name every clause the deck barely supports | Path's scry (5 creatures, accepted); Long-Range Sensor needs an attack before proliferate can grow it (fliers Mechanaut, Seedshark, Tekuthal, Monitor attack safely: acceptable); Etched Oracle needs four colors or a proliferate to draw (10 off-color sources: acceptable); Excavation's loop clause needs two specific cards (its re-buy clause carries it); Thrummingbird's combat clause (cut, I3) |
| 10 | Multiple copies, free Spanish staples | No strong staple left idle | Two left idle with no reason (I2, I3). Others checked and left out with reason: Etherium Sculptor (a second reducer cuts sunburst colors and breaks the loop: Crawler ruling), Wake the Past (7 mana; only mass artifact recovery, a fair alternative to Organic Extinction if the pod wipes artifacts often), Silverbluff and Razortide Bridge (tapped, two colors; R10), Temples and cycling lands (tapped), Mindless Automaton and Golem Foundry (weaker than Oracle and Titan Forge), Gavel of the Righteous (voltron on one player), Fumigate (symmetric), Evolving Wilds (tapped). Spare copies of in-list staples (Chaos Warp, Exotic Orchard, Clifftop, Monastery, Tranquilize) cannot be played twice |

Web read today (pauses between requests): https://media.wizards.com/2026/downloads/MagicCompRules%2020261106.txt;
https://mtgcommander.net/index.php/rules/; Scryfall API rulings for Kilo, Crystalline Crawler, Lux Artillery, Meticulous
Excavation and Solar Array; https://api.scryfall.com/cards/search?q=is:gamechanger. EDHREC Kilo data from the project cache
`data/cache/edhrec/kilo-apogee-mind.json` (2026-11-01), used as a prior only.

## 7. Lessons checklist

| # | Covered? | Card or evidence |
|---|---|---|
| L1 One plan | Yes | Counters + proliferate into Reactor or Lux; backup reuses the board; gate PASS |
| L2 Ratios follow the plan | Yes | 19 counter sources, 15 proliferate pieces, 37 artifacts; draw 10 |
| L3 Attacking decks | N/A (main plan noncombat) | Backup has Alibou (haste), Cyberdrive (team flying), Kappa (unblockable) |
| L4 Dependence | Yes | Enabler, 4 protection pieces after I1 (class asks 3 to 4) |
| L5 Value in context | Yes | Chalice and Cornucopia grow with proliferate; Sphere judged as a fixer |
| L6 Proven role-players | Yes | None exist for Kilo (no games played); his liked cards Sphere and Alibou are in |
| L7 Dead clauses | Yes, with I3 | Section 6 item 9 |
| L8 Two boards | Yes | Board 1: Reactor, Lux, Fireweaver, wipes, fliers, Hangarback's Thopters. Board 2: 9 spot answers, Alibou, Titan Forge, noncombat closers |
| L9 Salt not the measure | Yes | Not chased |
| L10 Guide says how to use | Yes | Build section 2; add M3 notes |

## 8. Multiplayer check

- **How it beats three opponents:** the Reactor ends the game for all at once; Lux deals 10 to each opponent per end step
  (20 when copied); Fireweaver drains each opponent; the loop kills the table with a fourth card. Kappa and Alibou are
  one-player backups.
- **The pod's interaction:** 2.3 spot removal, 0.9 wipes and 0.45 counters seen by turn 8 (skill medians). Spot removal on
  Kilo costs a turn (recast with haste). The wipe is the danger, and only if it hits artifacts; after I1 the stack answer is
  Negate alone, plus Ripples. Graveyard hate does nothing here. A tax effect does nothing (no attacks needed). Artifact-
  ability hate (Collector Ouphe, Stony Silence) stops rocks, Insight Engine and Lux Cannon but not the Reactor's or Lux's
  triggers or Kilo.
- **Single card that ends the plan:** an artifact wipe that exiles (Farewell) or an exile on the Reactor. Second answer to the
  wipe: Ripples (if a counter is on what matters). After the wipe: Emry, Kilo, Hangarback's Thopters (I3), Resourceful
  Defense's counters on the Reactor (destroy wipes only).

## 9. Verdict: FIX

Exact changes, ranked (every IN card is a free Spanish copy or already in Kilo):

| Rank | OUT | IN (Spanish source) | Reason | Expected impact |
|---|---|---|---|---|
| 1 (owner decision) | Swan Song (back to Azula) | **Titan Forge** (already in Kilo) | Owner 2026-11-15: no copy from the frozen decks | Shield 3 to 2, counters 2 to 1; Board 2 and charge battery +1; gate PASS 0 WARN with Titan Forge `never` |
| 2 | Contentious Plan | **Empowered Autogenerator** (Spanish binder) | A repeatable counter engine that becomes 5 to 8 mana a turn and a charge battery for the Reactor, over a one-shot cantrip proliferate | Faster Reactor and Lux, more X for draw sinks; doublers 15 to 14 (min 10) |
| 3 | Thrummingbird | **Hangarback Walker** (Spanish binder) | Counter source from turn 2 that every proliferate grows, artifact body for station and improvise, Thopters as wipe insurance and evasion; Thrummingbird needs combat damage | Doublers 14 to 13; wide board 14; one more rebuild piece. Thopter token to the token list |
| 4 (optional) | Karn's Bastion | **Island** (the ninth Spanish Island Kilo holds) | A colored source for a three-color turn-3 commander; Bastion is the 15th proliferate | +1.1 points Kilo on turn 3 (my simulation); doublers 13 to 12 (min 10) |
| 5 | (plan file) | | M2 tag corrections; M3 and M5 notes in the build file | Honest counts; all functions still above min |

Real power, my estimate (1 to 10): the builder's list with Swan Song 5.6 to 6.0; with the owner's decision (Titan Forge for
Swan Song) 5.4 to 5.8; with changes 2 to 4, 5.6 to 6.0. Confidence medium-low (no game played with any Kilo list). The
ceiling is the Spanish collection: no tutor reaches the two table-wide closers, and no free Spanish counterspell remains.
