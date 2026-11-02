# Adversarial review: spanish-deck (Kilo, Apogee Mind), 2026-11-02

Reviewer: Opus 5.5 high, `commander-deckbuilding` skill, Phase 2 rules of CLAUDE.md. Inputs: `decks/phase2/spanish-deck.txt`,
`data/model/phase2/pool-spanish-deck.json` (Oracle text), Scryfall API (Kilo Oracle and its 5 rulings, live `is:gamechanger`,
53 cards, 2026-11-02), then `spanish-deck.plan.json`, `spanish-deck.build.md`, `decks/reports/consistency-spanish-deck.md`,
`decks/phase2/owner-decisions.md` (three rounds), `docs/research/phase2-spanish-commander-20261101.md`,
`data/model/phase2/assignment.json`. Live stock read on gameofmagicsingles.cl (product `.js` variant data, 2026-11-02).
Owner decisions are binding and are not findings: Kilo is the commander; up to 5,000 CLP at Game of Magic Singles; Spanish
copies only; Freed from the Real wanted if affordable and the late three-card line is welcome; Swiftfoot Boots may be bought
outside the cap; every combo inside the Bracket 3 rules is accepted.

Scripts run by the reviewer: `python scripts/check_phase2_bracket.py decks/phase2/spanish-deck.txt` (PASS, floor 1, 0 Game
Changers, 0 Spellbook variants inside, 47 one card away) and `python scripts/plan_density.py` (spanish-deck PASS, 0 failures,
1 warning: ramp 9 of 10). Both scripts rewrite their own reports (`bracket-spanish-deck.md`, `consistency-*.md`); their
content is the builder's, regenerated. A Monte Carlo of Kilo's casting cost and a Spellbook "one card away" listing were run in
the scratchpad (models described where used).

## 1. Independent reading (written before opening the plan file and the build notes)

**Commander.** Kilo, Apogee Mind {U}{R}{W}, Legendary Artifact Creature (Robot Artificer) 3/3, Haste. "Whenever Kilo becomes
tapped, proliferate." Rulings 2025-07-25: tapping Kilo to station resolves its proliferate before the station ability;
proliferate may choose any permanent or player, including none.
- Rewards: Kilo becoming tapped (attack, crew, station, improvise, waterbend, any cost that taps it, an untap and re-tap).
- Fuel: permanents that already carry counters (charge on rocks and engines, +1/+1 on artifact creatures, stun on opposing
  creatures), and tap events (one per untap unless an untapper or a tap-for-cost loop exists).
- Window: any time it becomes tapped; crew and waterbend are instant speed, station is sorcery speed.
- Wins by itself: no. It multiplies counters; the kill comes from the 99.
- Dies to: any creature or artifact removal (3/3), creature and artifact wipes, blocks if it attacks into Board 2.
- Dependence: I read it as **between enabler and engine**. It is the only guaranteed proliferate; without it the 99 has 8
  cards that proliferate by themselves, 4 of them one-shots (about 6 weighted), and the counter growth falls from "every
  countered permanent +1 per tap" to "each source +1". It is cheap (MV 3, recast 5 and 7) and has haste, which softens it.
  Protection floor I would set: 4, target 5.
- Dead clauses: none on Kilo.

**Archetype and plan.** `plus_one_counters` (all counter kinds) with `artifacts` as fuel. Plan: tap Kilo every turn (at home
via crew, station, waterbend, improvise) to proliferate a board of growing rocks and charge engines; convert counters into
mana, cards and threats; close with Lux Artillery or Darksteel Reactor (noncombat) or an animated artifact alpha strike
(Cyberdrive Awakener, Depthshaker Titan).

**Recount from Oracle text (62 nonland cards, 37 lands).**

| Function | My count | Cards and notes |
|---|---|---|
| Ramp cast by turn 2 (timed) | 4 rocks + 2 reducers at half = **5** | Sol Ring, Arcane Signet, Everflowing Chalice (kicked once), Pentad Prism; Etherium Sculptor, Enthusiastic Mechanaut reduce only artifact spells and do nothing for Kilo ({U}{R}{W} has no generic). Commander's Sphere, Solar Array, Astral Cornucopia (X=1) are 3-mana plays that compete with Kilo on turn 3: by the timed rule they are turn-4 ramp. Crystalline Crawler, Empowered Autogenerator are late mana engines. |
| Counter sources | ~24 | Agree with the builder's list (Chalice, Prism, Cornucopia, Solar Array, Coretapper, Steel Overseer, Hangarback, Insight Engine, Uthros, Inspirit, Long-Range Sensor, Golem Foundry, Titan Forge, Crawler, Autogenerator, Lux Cannon, Etched Oracle, Mindless Automaton, Peacemaker, Kappa, Thunderhulk, Seedshark, Reactor, Lux Artillery). |
| Proliferate (alone, without Kilo) | **8** (4 repeatable, 4 one-shot) | Surge Conductor, Thrummingbird, Patrolling Peacemaker, Karn's Bastion; one-shots Tezzeret's Gambit, Experimental Augury, Ripples of Potential, plus Deepglow Skate (doubling, not proliferate, but the same job). Tekuthal only doubles another proliferate; North Pole Patrol only untaps Kilo. |
| Kilo tap outlets | 10 | Brute Suit, Ovalchase Dragster (crew 1), Inspirit, Uthros (station), Katara, Waterbending Lesson, North Pole Patrol (waterbend; Patrol also untaps), Kappa Cannoneer, Universal Surveillance, Organic Extinction (improvise, one-shot). |
| Draw (nets cards) | 13 | Insight Engine, Uthros, Jhoira, Etched Oracle, Mindless Automaton, Long-Range Sensor (half), Katara (half), Tezzeret's Gambit, Thirst for Knowledge, Universal Surveillance, Waterbending Lesson, Thought Monitor, Inspiring Overseer. |
| Spot removal | 8 + graveyard | Tranquilize, Dispatch, Chaos Warp, Airbending Lesson, Firebending Lesson, Sandbenders' Storm (power 4+), Detained by Legionnaires, Lux Cannon (slow, repeatable); North Pole Patrol taps; Soul-Guide Lantern is graveyard hate. |
| Wipes | 2 | Fumigate (symmetric unless Inspirit is at 8+), Organic Extinction (spares artifact creatures: most of mine). |
| Commander protection | **~3 weighted** | Swan Song (instants and sorceries only), Airbending Lesson (exile and recast for {2}), Ripples (needs a counter on Kilo), Inspirit (needs 8 station). |
| Closers | 2 noncombat + 4 combat | Lux Artillery, Darksteel Reactor; Cyberdrive Awakener, Depthshaker Titan, Threefold Thunderhulk, Titan Forge. Secondary: Kappa Cannoneer, Uthros at 12+, Reckless Fireweaver (chip). No tutor in the list. |

**Lands and colored sources.** 37 lands: 22 nonbasic + 7 Island, 4 Plains, 4 Mountain. Lands that make the color with no
condition or partner: **W 13, U 16, R 13**. Conditional: Rugged Prairie and Cascade Bluffs (filters, need a colored mana from
another land), Skycloud Expanse ({1},T: WU, consumes another land's mana), The Mycosynth Gardens ({1},T: one color, so it
converts and nets nothing), Spire of Industry (needs an artifact, 1 life), Exotic Orchard (depends on the opponents). Colorless
only: Karn's Bastion, Buried Ruin. Always tapped: Path of Ancestry, Mystic Monastery, three Bridges (5). Pips: U 26 (+2
Phyrexian), W 11, R 9. Curve (nonland): MV 0: 3 (X costs), 1: 5, 2: 12, 3: 20, 4: 14, 5: 2, 6: 2, 7+: 4; average 3.19.

**How it loses.**
- *To a wipe.* A creature wipe kills Kilo and the artifact creatures but leaves every noncreature artifact with its counters;
  recast Kilo for 5 with haste and keep going: survivable. An artifact wipe (Vandalblast overloaded, Bane of Progress, Austere
  Command) takes rocks, engines and both noncombat finishers at once; insurance is Inspirit at 8+, the indestructible Reactor
  and Bridges, Ripples (phase out countered permanents), Swan Song (sorcery wipe), Emry and Buried Ruin.
- *To eight chump blockers.* It does not need combat: Lux Artillery and the Reactor ignore blockers; Cyberdrive flies,
  Depthshaker tramples, Kappa is unblockable. The risk is the pingers such decks carry: Coretapper, Steel Overseer,
  Sculptor, Thrummingbird, Inspiring Overseer, Peacemaker die to 1 to 2 damage.
- *To two bigger creatures.* Kilo never attacks into them (taps at home); 8 spot answers plus Patrol's tap and Titan Forge
  9/9s. The real loss here is speed: if neither noncombat finisher shows up, the deck must alpha strike through them.
- *Its own failure modes.* Kilo not cast on turn 3 (three colors, few cheap rocks), and the noncombat route resting on two
  cards with no tutor.

## 2. Differences with the builder

| Point | Builder (plan file, build.md) | Reviewer | Effect |
|---|---|---|---|
| Colored sources | U 18, W 15, R 15 lands "+ partial" = 21.5 / 18.5 / 18.5; "met for all three" (17 needed) | Unconditional lands U 16, W 13, R 13; filters and Mycosynth are conditional; simulated Kilo-on-turn-3 rate is 76 % with 3+ lands (finding I-1) | The mana is the weakest part of the list; the builder's "met" is not supported |
| Ramp | 9 (WARN 9 of 10) | 5 timed (finding I-2) | The WARN understates the gap |
| Commander dependence | Enabler, floor 3, protection 4 tags (~3.25 weighted) | Between enabler and engine, floor 4 | Boots (owner-approved extra) matter more than the build says |
| counter_doublers | 11 with Kilo, 10 without | 10 real with Kilo (North Pole Patrol is not proliferate); 8 that work without Kilo | Passes, but the planned Thrummingbird cut would take it under 10 (finding M-1) |
| Win route 1 | 3 closers (Lux, Reactor, Fireweaver) | 2 closers + chip damage; 30 % to see one by turn 9 with no tutor (finding I-3) | The declared main route closes a minority of games |
| through_wide_board | 16 | 7 team-level + 9 single flyers of power 1 to 3 (finding M-2) | Passes; the count is inflated by small flyers |
| bad_when_drawn | early 8, late 1 | add Katara (early: builder's own note), Astral Cornucopia (bad as the turn-3 play), Etherium Sculptor (late) | 12, at the warning line (finding M-3) |
| Curve | MV1 6, MV3 19, average 3.16 | MV1 5, MV3 20, average 3.19 (pool cmc) | Cosmetic |
| Purchases | Relic of Legends, Freed from the Real, Command Tower, Boots (stock "not verified") | Relic, Freed, and both fallbacks (Springleaf Drum, Pemmin's Aura) have **no stock** at Game of Magic Singles today; Freed has no Spanish copy in stock and costs 5,200 CLP or more in every printing listed (finding B-1) | The ranking must be redone |
| Everything else | | Agreed: counter sources, payoffs, tap outlets, draw 13, removal 8, wipes 2, lands 37, the rules points, the boards analysis | |

## 3. Findings

### BLOCKING

**B-1. The purchase ranking cannot be executed: ranks 1 and 2 and both fallbacks are out of stock, and Freed from the Real
does not fit the cap in any printing.** (Blocks the purchase step, not the 100-card list, which is all owned Spanish copies.)
- Evidence (live product data, gameofmagicsingles.cl, 2026-11-02, `available` per variant):
  - Freed from the Real: 5 products. Saviors of Kamigawa (NM 9,360 down to Damaged 5,640), Masters 25 (8,920 to 5,360), The
    List (8,640 to 5,200), Secret Lair: **every variant unavailable**. The only one in stock is the Secret Lair "Neon Ink
    Yellow" foil, English, 28,800 CLP. No Spanish variant exists in any of the five products. Even a restock costs at least
    5,200 (Damaged, English), above the 5,000 cap on its own.
  - Relic of Legends: 7 products; the only Spanish variant (Dominaria United, NM, 2,500) is unavailable; nothing in stock.
  - Springleaf Drum (fallback of 1): 9 products, nothing in stock (Spanish BRR variants 645 and 742, unavailable).
  - Pemmin's Aura (fallback of 2): 1 product (Scourge), unavailable.
- So the "late three-card line" (Kilo + Freed + Relic) cannot be bought in this iteration. The owner's decision ("wanted now if
  affordable") is respected by reporting that it is not available; the restock rule applies (`decks/phase2/restock.md` is for
  loans, so this is a note for the next iteration's store list, not a restock entry).
- Fix: re-rank with in-stock Spanish cards (section 3b below). Sourced (live store data).

### IMPORTANT

**I-1. Kilo is castable on turn 3 in only about 76 % of the games that have three lands; white and red are the short colors.**
- Evidence: Monte Carlo, 5,000 trials per turn, 99-card library, 7 + N cards seen, best land order, Sol Ring turn 1, Arcane
  Signet or Pentad Prism turn 2, Sphere or Solar Array from turn 4, check lands and Radiant Summit by their conditions, filters
  consuming another land's mana, Spire with an artifact, Exotic Orchard right half the time, no mulligan:

  | List | Turn 3: all games / with 3+ lands | Turn 4 | Turn 5 |
  |---|---|---|---|
  | As built | 64.5 % / **76.4 %** | 75.4 % / 85.2 % | 82.1 % / 88.8 % |
  | Talisman of Conviction for Inspiring Overseer | 67.0 % / **78.4 %** | 77.0 % / 86.7 % | 83.4 % / 90.4 % |
  | Same, plus Command Tower for The Mycosynth Gardens | 69.8 % / **81.3 %** | 77.7 % / 87.7 % | 84.0 % / 90.7 % |

  Of the failures with 3+ lands, the missing color was white 34 %, red 35 %, blue 18 % of the time. Karsten's consistency
  target for a gold three-drop is about 92 % conditional (`mana-and-ramp.md` section 4: 89 + M %). Unconditional land
  sources: W 13, R 13, U 16; the builder's 15 / 15 / 18 count the filter lands (Rugged Prairie, Cascade Bluffs, Skycloud
  Expanse) as full sources, which the reference says to treat as colorless until the condition holds most games.
- Why it matters: the deck's engine is the commander; every turn Kilo is late is a turn without proliferate, and the 20
  three-drops all want turn 3 as well. Even with both fixes the turn-3 rate stays near 80 %: the pool has no more untapped
  Spanish tri-color sources (Battlefield Forge went to Toph), so the remaining gap is accepted and the guide should say to
  mulligan hands that cannot make all three colors by turn 4.
- Fix: (a) a two-mana R/W rock: **Talisman of Conviction, Spanish, in stock, 1,500 CLP** (Tarkir: Dragonstorm Commander, NM
  Español, verified 2026-11-02); it also closes the ramp WARN; (b) Command Tower in place of **The Mycosynth Gardens** (which
  converts one mana into one other and is the weakest early land), not in place of a Plains (the Plains also turns on Clifftop
  Retreat, Glacial Fortress and Radiant Summit; the simulation gives 79.7 % against 77.9 % on turn 3). Sourced (Karsten table)
  plus [J] (simulation model).

**I-2. Timed ramp is about 5, not 9.**
- Evidence: castable by turn 2 and helping Kilo: Sol Ring, Arcane Signet, Everflowing Chalice, Pentad Prism (4); Etherium
  Sculptor and Enthusiastic Mechanaut reduce artifact spells only and do nothing for Kilo's {U}{R}{W}, so half each.
  Commander's Sphere, Solar Array and Astral Cornucopia (X=1) cost 3 and compete with Kilo for turn 3; the builder's own
  guide says "Bad as a turn-3 play instead of Kilo" for Cornucopia. Odds of a 2-mana-or-less rock by turn 2 (9 cards): 4 pieces
  32 %, 5 pieces 39 %.
- Mitigation is real (Chalice, Prism, Cornucopia, Autogenerator and Crawler grow with every proliferate), so the deck is not
  mana-starved from turn 5; the gap is turns 2 to 4.
- Fix: Talisman of Conviction (I-1). The pool has no other Spanish 1-2 mana rock free (Mind Stone is in Azula). [J] with the
  skill's timed-ramp rule.

**I-3. The declared main route rests on two cards with no tutor; it closes a minority of games.**
- Evidence: route 1 is Lux Artillery and Darksteel Reactor (Reckless Fireweaver is chip damage, 1 per artifact entry). One of
  two specific cards in 99: **23 % by turn 5, 30 % by turn 9, 36 % by turn 13** (no extra draw; draw engines raise it).
  Long-Range Sensor's Discover 4 can hit either (both MV 4): with it as a third piece 41 % by turn 9. Lux Artillery then needs
  30 counters and four of my end steps to kill a table at 40 life (the builder says so), each turn exposing one artifact to
  removal. Metamorph, Emry and Buried Ruin only work after one was drawn.
- So most games are actually closed by the backup (Cyberdrive, Depthshaker, Thunderhulk, Titan Forge, plus Kappa, Uthros 12+);
  all six named closers together: 66 % by turn 9, 75 % by turn 13. That is acceptable, but the plan sentence and the guide
  should say it, and the deck has room for a tutor.
- Fix: an artifact tutor that is also a value card: Fabricate ({2}{U} sorcery, any artifact: Lux, Reactor, Insight Engine,
  Inspirit) or Whir of Invention (instant, improvise, so Kilo pays for it and proliferates). Each would also raise Commander
  Salt, whose measured "structural ceiling" penalizes win conditions with no tutors (CLAUDE.md, power drivers 2026-10-18).
  Neither fits this iteration (section 3b: Spanish Fabricate in stock only at 9,800, Whir out of stock). This iteration: rewrite
  the plan sentence so the combat route is co-primary, and keep Long-Range Sensor, Emry and Buried Ruin as the route's access.
  Next iteration: Fabricate or Whir for Inspiring Overseer. [J] plus sourced odds.

**I-4. Commander protection is about 3 weighted for a commander the plan starts with.**
- Evidence: Swan Song 1 (spells only), Airbending Lesson 1, Ripples of Potential 0.75 (Kilo needs a counter: Steel Overseer,
  Inspirit, Lux sunburst), Inspirit 0.5 (needs station 8). Three to four pieces give 39 to 49 % to hold one by turn 8 (15
  cards); the table has seen about 2.3 spot removal by then (`interaction-and-protection.md`).
- The owner already decided to buy Swiftfoot Boots outside the cap. Live: **Swiftfoot Boots, Spanish, in stock, 3,280 CLP**
  (The Brothers' War Retro Artifacts, schematic art, NM Español). Boots' hexproof does not stop Kilo's own targeting (Inspirit's
  counter, Freed later), unlike Lightning Greaves' shroud. Equip {1} does not tap Kilo.
- Fix: buy it (owner decision), replacing Ovalchase Dragster (tap outlets 10 to 9, still above 6). Sourced (owner decision,
  live stock).

### MINOR

**M-1. North Pole Patrol is listed in `counter_doublers` but never proliferates; the planned Thrummingbird cut would put the
function under its declared minimum.** Patrol untaps Kilo (a tap-outlet multiplier, already in `kilo_tap_outlets`). Real
count with Kilo: 10 (Kilo, Surge Conductor, Thrummingbird, Peacemaker, Tekuthal, Karn's Bastion, Gambit, Augury, Ripples,
Skate), exactly the declared min 10. The build's purchase plan cut Thrummingbird for Freed, which is a tap outlet, not a
proliferate piece: honest count 9 < 10, a gate failure hidden by Patrol's tag. Fix: move Patrol to `kilo_tap_outlets` only;
when a purchase replaces a card, take it from outside `counter_doublers` (Inspiring Overseer, Ovalchase Dragster, Etherium
Sculptor late). [J] on the counting rule (skill 3.4: one verb per function).

**M-2. `through_wide_board` counts nine single flyers of power 1 to 3.** Team-level pieces are 7 (Lux Artillery, Reactor,
Fireweaver, Cyberdrive, Depthshaker, Organic Extinction, Fumigate). Thrummingbird 1/1, Mechanaut 2/2, Inspiring Overseer 2/1,
Thought Monitor 2/2, Seedshark 2/4, Tekuthal 3/5, Hangarback Thopters 1/1 do fly over chump blockers, so they count by the
skill's rule, but none closes. The function passes (16); it is weaker than the number says. No change needed; say it in the
plan's Board 1 text. [J]

**M-3. `bad_when_drawn` is under-marked.** The builder's own guide calls Katara "Bad early", Astral Cornucopia "Bad as a
turn-3 play", Etherium Sculptor "Weak late (a 1/2)"; all three are tagged `never`. Corrected count about 12, at the warning
line (skill step 9). Fix: tag them. [J]

**M-4. Command Tower should replace The Mycosynth Gardens, not a Plains** (I-1 simulation; the Plains feeds three check-type
lands). [J]

**M-5. Curve figures.** Pool cmc gives MV1 5 and MV3 20 (average 3.19), not 6 and 19 (3.16). Cosmetic.

### 3b. Purchase ranking re-checked (Game of Magic Singles, live 2026-11-02, Spanish only, cap 5,000 CLP; Boots outside)

| Rank | Card | Live Spanish stock and price | Need | Replaces | Note |
|---|---|---|---|---|---|
| extra | Swiftfoot Boots | **in stock**, 3,280 (BRR retro schematic, NM ES) | commander protection (I-4) | Ovalchase Dragster | Owner decision: outside the cap |
| 1 | Talisman of Conviction | **in stock**, 1,500 (TDC, NM ES) | Kilo on turn 3, ramp WARN (I-1, I-2) | Inspiring Overseer (draw 13 to 12) | Replaces the builder's rank 1 (Relic, no stock) |
| 2 | Command Tower | **no Spanish copy in stock among the products read**: AFC NM ES 570, Zendikar Rising Commander NM ES 1,000 and Aetherdrift Commander NM ES 1,000 all unavailable; EOC (1,200), LCC (1,200) and TMNT (1,500) are in stock but English only; about 25 other printings unread (HTTP 429) | untapped tri-color source (I-1) | The Mycosynth Gardens | buy only if a Spanish copy is in stock at purchase time; otherwise keep the list as is |
| over cap | Fabricate / Whir of Invention | Fabricate: only Spanish in stock is the Warhammer 40,000 NM foil, 9,800; Mirrodin LP ES 8,240 unavailable. Whir of Invention: Aether Revolt LP ES 6,150 unavailable | a tutor for route 1 (I-3) | Inspiring Overseer or Etherium Sculptor (not Thrummingbird, M-1) | does not fit 5,000 this iteration; first candidate for the next one |
| out | Relic of Legends | no stock in any of 7 products | | | wait for a restock |
| out | Freed from the Real | no Spanish stock; cheapest listed printing 5,200 (English, Damaged, unavailable); in stock only a 28,800 English foil | | | over the cap even when restocked |
| out | Springleaf Drum, Pemmin's Aura | no stock | | | |

Reading notes: prices are CLP from each product's `.js` variant data (price / 100), `available` per variant, read 2026-11-02;
the store began answering HTTP 429 during the reads, so the Command Tower, Fabricate and Whir rows cover only the products
listed. Verified in stock and Spanish: Swiftfoot Boots 3,280 and Talisman of Conviction 1,500. **Within the cap: Talisman
1,500, leaving 3,500** for a Spanish Command Tower if one appears, or for the owner to redirect to the bilingual decks. Re-verify
stock within 24 hours of buying (CLAUDE.md stock rule).

**Commander Salt (second objective).** Every swap above should raise or keep Salt: a two-mana rock and Command Tower improve
Manabase Quality (which moved Azula 5.5 to 6.9 in Phase 1 measurements), a tutor addresses the "no tutors for the win
conditions" ceiling, Boots add protection. Nothing in the list or in these swaps should drop Salt significantly; the cuts
(Inspiring Overseer, The Mycosynth Gardens, Ovalchase Dragster, Thrummingbird or Sculptor) are the lowest-impact cards of the
list. Spellbook lists 47 combos one card away; the ones that are Bracket 3 legal and buyable later include Freed from the Real
or Pemmin's Aura with Solar Array and Cyberdrive Awakener (four variants each) and Aura of Dominion with Kilo and Crystalline
Crawler (infinite proliferate). Magistrate's Scepter with Kilo and Inspirit is an infinite-turns line: never (chained extra
turns are a Bracket 3 rule).

## 4. Lessons checklist (docs/research/phase2-owner-lessons-20261031.md)

| # | Covered | Evidence |
|---|---|---|
| L1 one plan | Yes | One counters plan; the backup reuses the same artifacts; 0 orphans; gate PASS. Caveat I-3: the "main" route is the rarer one. |
| L2 ratios follow the plan | Yes, except ramp | Counter sources 24, proliferate 10, tap outlets 10; ramp is 5 timed (I-2). |
| L3 attacking decks | Not an attacking deck by plan | Kilo taps at home; haste on Kilo, Depthshaker gives haste, Ovalchase has it; defense while tapped is thin (Brute Suit vigilance, flying blockers Tekuthal 3/5, Seedshark 2/4, Titan Forge 9/9s), acceptable because the plan does not swing every turn. |
| L4 dependence sets protection | Partly | Declared enabler; reviewer reads it higher (I-4). Boots fix it. |
| L5 card by this deck's curve | Yes | Chalice is cast for 2 and grows with proliferate (the lesson's own example, inverted correctly). Cornucopia as a turn-3 play is the exception (M-3). |
| L6 proven role-players | Not applicable | New deck; the owner's proven cards (The Earth King, Seismic Tutelage, Horizon Stone, Propaganda, Eagle Vision) belong to other decks or have no Spanish copy in this pool. Nothing that wins games was cut for a score. |
| L7 dead clauses, mini-combos | Yes | 2 Vehicles and 2 Spacecraft all crewed or stationed by Kilo itself; no equipment; Golem Foundry and Thrummingbird clauses named. The Freed line is three cards that each work alone (moot now, B-1). |
| L8 both boards | Yes | Board 1: Lux, Reactor, Cyberdrive, Depthshaker, Organic Extinction; Board 2: 8 spot answers, Patrol, Titan Forge, Kappa. |
| L9 Salt is not the measure | Yes | Swaps judged by function first. |
| L10 guide says how to use | Yes | build.md section 4 gives timing and pairings per card. |

## 5. Rules checklist

| Rule | Result |
|---|---|
| Pool and copies | Every card in the pool; `assignment.json` gives 100 of 100, 0 missing, 0 problems. |
| Language policy (es) | Every pick in `assignment.json` is `es`, basics included (7 Island, 4 Plains, 4 Mountain Spanish). |
| Loans | None, correctly: the loan candidates are English cards. |
| Owed cards | Smoldering Marsh (B/R) is outside Kilo's colors: not used, correctly. |
| Scarce copies | Named in build.md section 7 and resolved by the lead (Swan Song, Insight Engine, Thirst, Soul-Guide Lantern, Sphere, Spire, Glacial Fortress, Monastery, Radiant Summit to Kilo; Swords, Pull from Tomorrow, Battlefield Forge, Command Tower elsewhere). Shared names with other decks (Sol Ring, Signet, Orchard, Sulfur Falls, Clifftop, Rugged Prairie, Shivan Reef, Cascade Bluffs, Chaos Warp, Sandbenders' Storm, Path of Ancestry, Lantern) each have separate physical copies in the assignment. |
| Purchases | None in the list. Ranks 1 and 2 not purchasable (B-1); cap math redone in 3b. |
| Bracket 3 | `check_phase2_bracket.py`: PASS, 0 Game Changers (live Scryfall list of 53, 2026-11-02: none in the list), no mass land denial, no extra turns, no reversible cards, 0 Spellbook combos inside the list. No card cut or combo held back to look weaker. |
| Consistency gate | `plan_density.py`: PASS, 1 warning (ramp). |

## 6. Multiplayer check

- **Against three opponents.** Route 1 deals with the whole table at once (10 to each per end step; the Reactor is an
  alternate win); route 2 is team-wide (flying or trample). Fireweaver pings all three. Good shape; the weakness is how often
  route 1 appears (I-3) and its speed (Lux needs four end steps).
- **Single card removal that ends the plan.** Kilo: slows the engine but does not end it (8 proliferate pieces, cheap recast
  with haste). Lux Artillery or the Reactor: ends route 1 until Emry, Buried Ruin or Metamorph; route 2 remains. An artifact
  wipe is the real plan-ender (rocks, engines and both finishers); insurance is Inspirit 8+, Ripples, Swan Song, the
  indestructible Reactor and Bridges, Emry and Buried Ruin: 7 pieces, adequate.
- **Graveyard hate** in the pod costs it only Emry and Buried Ruin. **Tax effects** (Propaganda-type) do not matter: it does not
  need to attack. **Pingers** kill the 1-toughness engines (Coretapper, Steel Overseer); keep them for value, not as the
  plan's only sources.

## 7. Verdict

**PASS for the 100-card list (ship to Salt), FIX for the purchase plan.**
The list itself passes the gate, the bracket rules and the language and copy rules, and its plan is sound. No finding forces a
change before measuring it. The purchase plan must be redone (B-1): Relic of Legends and Freed from the Real cannot be bought
now. Recommended purchases, Spanish and in stock today: Swiftfoot Boots 3,280 (extra, owner decision, for Ovalchase Dragster) and
Talisman of Conviction 1,500 (inside the cap, for Inspiring Overseer); Command Tower only if a Spanish copy is in stock at
purchase time (for The Mycosynth Gardens). Then the plan-file fixes M-1 and M-3, and a plan sentence that admits the combat
route closes most games (I-3). After the swaps the list should be re-run through `plan_density.py` and measured on Salt.
