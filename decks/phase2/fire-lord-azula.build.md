# Fire Lord Azula: final rebuild (Phase 2 step 7.7, 2026-11-08)

Rebuilt FROM SCRATCH under `docs/proposals/final-rebuild-brief-20261108.md` (corrected budget), the skill
`.claude/skills/commander-deckbuilding/SKILL.md` with its champion standard, `champion-addendum-20261108.md` and the primers
`commanders/fire-lord-azula.md` and `fire-lord-azula-primers-20261108.md`. Priority 2: Ezio's final list keeps its copies.
Language: bilingual, the English copy whenever one is owned (section 8 lists the Spanish-only copies).

**Fix round (2026-11-08)** after the independent review `decks/reports/final-review-fire-lord-azula-20261108.md` (FIX):
F1 Soul-Guide Lantern out, Shred Memory in (buy, to read); F2 Fellwar Stone out, Everflowing Chalice in (owned, saves 1,560);
F3 Cunning Maneuver out, Expedite in (owned; haste WARN closed); the checklist items NOT APPLIED: tutors (F1 makes three
real tutors to the loops), politics (section 4), goldfish (five games now played turn by turn, section 5), Game Changers
(budget-blocked, unchanged); notes N2 (prices), N3 (Day of Black Sun), N6 (politics), N7 (Frantic loop is not a kill) and the
iteration-1 tutor claim (section 9) corrected.

Checks (run 2026-11-08):
- `python scripts/check_phase2_bracket.py decks/phase2/fire-lord-azula.txt`: **PASS** (floor 3, 1 Game Changer: Narset,
  Parter of Veils; 0 extra turns, 0 mass land denial, 0 reversible cards; Spellbook: 5 variants inside the list, one flagged
  and classed late: Godo + Helm of the Host).
- `python scripts/plan_density.py`: **PASS**, 0 failures, 3 WARNs (reasons in section 3.3). Report:
  `decks/reports/consistency-fire-lord-azula.md`.
- 100 cards (commander + 99), counted by script; every non-bought card is an owned copy free after Ezio (section 8).

## 1. Profile

**Commander reading.** {1}{U}{B}{R} 4/4. Firebending 2: when she attacks, {R}{R} that lasts until end of combat. Whenever you
cast a spell while she is attacking, copy it (new targets allowed; a copied permanent spell becomes a token).
- Rewards: spells cast in HER combat window. Fuel: instants and flash cards in hand, and mana inside the window.
- Dependence: **attack engine** (protection 6 to 8). She does not need to connect: the copy happens on cast while she is an
  attacking creature, so chump blockers never stop the engine; blocks only threaten her life.
- Dies to: targeted removal, wipes, blocks by bigger creatures, the crack-back while tapped, "spells only at sorcery speed".
- Copies are not cast (no cast triggers: Electro's {R}, Thermo-Alchemist's untap and prowess see only the original; magecraft
  says "cast or copy" and triggers twice). Additional costs are not paid by the copy (Big Score's discard), X and kicker are
  kept (Comet Storm keeps X and its targets count). A spell cast without paying its mana cost has X = 0.

Rules points to verify:
| # | Point | Status | What falls if wrong |
|---|---|---|---|
| R1 | Horizon Stone keeps firebending mana (firebending ruling 2025-10-02: the mana lasts until end of combat; Horizon Stone ruling 2020-11-10: unspent mana becomes colorless instead of being lost). | Confirmed by both rulings (no joint ruling). | Horizon Stone as banker. |
| R2 | Copies keep X and multikicker choices; copies skip additional costs. | Confirmed (Azula rulings). | Comet Storm 2X, Big Score. |
| R3 | Turnabout copied while she attacks: the copy resolves first (untap all lands), you tap them again with priority, then the original untaps them all again. Mana stays in the pool until the step ends. | Rules reasoning (rule 500.4 mana empties between steps). | Mana burst size. |
| R4 | Reversal + Turnabout loop: cast Turnabout, then Narset's Reversal targeting it; Azula's copy of the Reversal targets the original Reversal (returns it to hand and copies it), the resulting copy returns and copies Turnabout... each cycle nets lands untapped minus {U}{U} and Turnabout's {2}{U}{U}. Commander Spellbook lists Azula + Reversal + Turnabout (tag S). | Spellbook variant; not checked in a ruling. | Loop (a). |
| R5 | Reversal + Frantic Search and Reversal + Storm-Kiln, Snap + Dualcaster with Azula attacking. | Spellbook variants (all three listed; Frantic is library-bound). | Loops (b) to (d). |
| R6 | Godo + Helm of the Host: unlimited combats, late (11 mana over two main phases). | Script: "two-card combo, late" (floor turn 4, typical 7 to 9). | Combat route without Azula. |
| R7 | Day of Black Sun X=0 destroys tokens CREATED with no mana cost (mana value 0); token COPIES of creatures keep the copied mana value and need a bigger X (review N3). | Rules knowledge (copiable values include mana cost). | Board 1 answer. |
| R8 | Deflecting Swat is free while I control a commander. | Oracle. | Free shield. |
| R9 | Spell Pierce and Swan Song stop a sorcery wipe or removal spell; Narset's Reversal returns the spell aimed at Azula. | Oracle. | Win-turn shield. |

**Plan (one sentence).** Azula attacks every turn from turn 4 with haste and hexproof from equipment and a shield of 1- and
2-mana counters behind her; in her window every instant is a two-for-one, and the win comes in ONE protected combat: a
three-card loop with her (Narset's Reversal + Turnabout, Frantic Search or Storm-Kiln Artist; Snap + Dualcaster Mage) makes
unbounded mana or casts, turned into Thermo-Alchemist pings at all three opponents or a twice-kicked, copied Comet Storm.

**Backup (same pieces).** Without a loop, Turnabout, Snap, Frantic Search, Big Score and Storm-Kiln fuel a copied Comet Storm
or Electrodominance (2X to each opponent, two turns of it kills the table); with Azula answered, Godo fetches Helm of the Host
for unlimited combats, Ozai attacks with haste, and Comet Storm is cast once with mana banked by Horizon Stone and Turnabout.

**Speed.** Azula lands turn 3 (Sol Ring, Everflowing Chalice, Signets) or 4; first copied combat turn 4 to 5; first lethal threat to
the table turn 6 to 8 (loop) or 7 to 9 (fair copied burn). Goldfish in section 5.

**Win routes, scored (R26, R28).**
| Route | Cards (incl. Azula) | Mana on the win turn | Access (pieces + tutors + dig) | Pieces useful alone | Single failure points |
|---|---|---|---|---|---|
| A. Loops: Reversal + Turnabout / Frantic / Storm-Kiln; Snap + Dualcaster | 3 | 6 to 8 (firebending pays 2) | 6 pieces + Teachings (copied: 2 pieces) + Solve + Narset, Gleam, Brainstorm, Thirst dig | all six (removal, draw, mana, treasure, counter-copy) | Azula removed; a counter on the key spell (shield answers it) |
| B. Copied X burn | 2 (Azula + Comet Storm or Electrodominance) | 10+ for lethal-ish | 2 + Teachings + Solve | both (removal early) | a counter (shield); without Azula half damage |
| C. Combat: Helm on Azula; Godo + Helm; Ozai | 2 to 3 | 9 to 11 over two turns | Godo fetches Helm | Helm on Azula alone doubles copies | wipe; Godo line does NOT need Azula |
No failure point is shared by all three: Route C (Godo + Helm) and B (uncopied Comet Storm) work with Azula dead; A and B do
not use the graveyard; artifact removal hits only C.

**How it beats three opponents.** Every route hits all three at once (Comet Storm kicked twice and copied, Thermo-Alchemist
pings each opponent, Helm/Godo combats spread attackers). It wins in one turn from banked resources, not by attrition.

**What it fears.** Fast combo before turn 6 (answers: Swan Song, Spell Pierce, Negate, Narset's Reversal, Deflecting Swat on a
targeted spell, instant creature removal); "can't cast spells during combat/only sorcery speed" stax; a wipe after she is
equipped (Undying Malice, Swan Song/Negate/Spell Pierce on the wipe); a pinger killing the 1-2 toughness engines.

## 2. The puzzle: every card by function, how to use it, main synergies

Commander: **Fire Lord Azula**. Cast turn 3 to 4; equip Boots or Cloak before attacking; attack every turn; cast instants in
the declare-blockers step, after blocks. Never present a lethal threat one turn before you can protect it (R30).

**Ramp (7 rocks + 3 reducers).** Development first (R17): every one is a turn-1 to turn-2 play.
- Sol Ring: turn 1; Azula on turn 3 with any 2-drop rock. Bad late.
- Arcane Signet: turn 2, fixes the third color. Bad late.
- Everflowing Chalice: turn 2 for one counter (colorless); late, cast for two or three counters to pay X and equips. Never bad.
- Izzet Signet, Dimir Signet: turn 2; filter into {U}{R}/{U}{B} double pips. Bad late.
- Mind Stone: turn 2; late, crack for a card.
- Bender's Waterskin: turn 3 if no 2-drop rock; untaps on every opponent's turn: counters and Pull from Tomorrow at instant speed.
- Goblin Electromancer, Stormcatch Mentor: turn 2; every instant in the window costs 1 less (loops get cheaper: Reversal {U}{U} cannot be reduced, Turnabout and Frantic can). Die to pingers.
- Nightscape Familiar: turn 2; blue and red spells cost 1 less (Azula, Dualcaster, Godo too); regenerates to block.

**Loop pieces (5).** Each is a good card alone; hold them until the protected combat.
- Snap: free bounce of a blocker or commander (untaps two lands, four copied); with Dualcaster Mage the Snap loop.
- Narset's Reversal: the hub. Alone, return a removal spell aimed at Azula and keep a copy, or steal an opponent's draw/burn; in her window with Turnabout, Frantic Search or Storm-Kiln it loops.
- Frantic Search: free in the window (untap 3, six copied) and loots. With the Reversal it loops, but the loop is library-bound (about +1 mana and four cards a cycle, at most about 13 cycles and 26 Thermo pings): it is NOT a kill alone; use it to dig and to fund Comet Storm (review N7). Never loop it with Archmage out.
- Turnabout (BUY): copied in combat untaps all lands twice (8 lands = 16 extra mana for Comet Storm); with the Reversal, unbounded mana. Out of combat, untap your lands at an opponent's end step for Pull or Fact or Fiction, or tap their creatures before your attack. Bad early (4 mana with no window).
- Dualcaster Mage: flash in the window, copies the best instant (three copies with Azula); out of combat, copy an opponent's removal or tutor; with Snap, the loop.

**Spell payoffs and engines (5).**
- Storm-Kiln Artist: two Treasures per spell in the window (cast + copy); loop with the Reversal; Treasures fund Comet Storm.
- Archmage Emeritus: two cards per instant in her window. Cast with protection up.
- Thermo-Alchemist: turn 2 defender; untaps on every instant cast and pings each opponent: the loop finisher, and 3 to 6 damage a turn cycle alone.
- Electro, Assaulting Battery: {R} per instant cast; keeps red mana between steps; leaving, burns a player for X.
- Horizon Stone (proven role-player): keeps firebending, Turnabout and end-step mana as colorless for X, equips and Godo.

**Finishers (2) and combat route (3).**
- Comet Storm: two kicks name all three opponents; copied, 2X each. Early, X=2 to 3 kills blockers.
- Electrodominance: X to any target and a free spell from hand (cast a sorcery or Godo at instant speed in the window: copied).
- Helm of the Host: equip Azula: a hasty Azula token every combat (every spell copied twice). Godo fetches it. Bad early.
- Godo, Bandit Warlord: turn 6+; Helm onto the battlefield; with Helm on Godo, unlimited combats without Azula. Bad early.
- Ozai, the Phoenix King: hasty 7/7 trample, firebending 4, keeps mana as red; second must-answer threat. Bad early.

**Tutors and dig (7).**
- Mystical Teachings: in her window it is copied: TWO instants or flash cards (both missing loop pieces, or a piece + Spell Pierce). Otherwise at an opponent's end step.
- Solve the Equation: main phase: the missing loop piece, Comet Storm, or the answer you lack.
- Narset, Parter of Veils (BUY, Game Changer 1 of 3): turn 3; -2 twice digs eight cards for noncreature spells (every loop piece, both tutors, both finishers are noncreature); her static shuts off the table's extra draws.
- Glamdring // Gleam of Death: Gleam first (mill six, take every instant and sorcery: often a loop piece); Glamdring on Azula later: her spells cost up to 4 less.
- Shred Memory (BUY): main phase, transmute ({1}{B}{B}, sorcery speed) for a mana-value-2 card: Narset's Reversal (the hub of three loops) or Snap; or, at instant speed, exile up to four cards from one graveyard (copied: two graveyards) against reanimation, Breach and flashback. The deck's graveyard hate.
- Brainstorm: end of an opponent's turn to dig for a piece; in the window it is copied (six cards seen).
- Thirst for Knowledge (BUY, stock line): draw three at an opponent's end step (discard an artifact you no longer need); copied in the window, six.

**Draw (8 more, incl. Expedite).** Azula empties her hand fastest of his decks: refill every turn cycle.
- Big Score: in the window the copy draws two and makes two Treasures with no discard: discard 1, draw 4, 4 Treasures.
- Thrill of Possibility: in the window, discard one, draw four. Alone a loot.
- Fact or Fiction: end of the last opponent's turn, or copied in the window.
- Pull from Tomorrow: end of the last opponent's turn with all lands (Turnabout first doubles it); copied, 2X cards. Bad early.
- Abandon Attachments: cheap rummage; copied, one more pair. Bin extra lands.
- Waterbending Lesson: main phase, tap rocks to waterbend {2}: draw three, keep all. The refill after a wipe.
- Fists of Flame: after blocks: two cards drawn copied, and trample with +1/+0 per card drawn, twice: the blocker dies, the rest tramples over.
- Expedite: {R} cantrip; copied in the window it draws two; out of combat it gives a recast Azula, Godo or Ozai haste.

**Spot removal (8 + the loop pieces Snap and the Reversal).** All instant (Amphibian Downpour has flash). In the window each answers two permanents.
- Fatal Push: {B} on an early threat or a blocker; sacrifice a Treasure/Clue first for revolt. Bad late.
- Firebending Lesson: {R} 2 damage (5 kicked) at instant speed: pingers, mana dorks, a blocker. Bad late unkicked.
- Terminate, Go for the Throat, Hero's Downfall: kill the blocker after blocks; the copy kills a second creature. Downfall also hits planeswalkers.
- Abrade: 3 damage or destroy an artifact (stax pieces, combo artifacts).
- Chaos Warp: any permanent (the enchantment answer), commanders included.
- Failed Fording: {1}{U} bounce any nonland permanent (an enchantment, a stax piece, a token) or a blocker; copied, two.
- Amphibian Downpour: flash in the window; storm plus the copy turn several creatures (or a commander) into vanilla 1/1 Frogs.

**Counters and the win-turn shield (R24).** Shield pieces at MV 2 or less or free: Spell Pierce, Swan Song, Negate, Narset's
Reversal, Deflecting Swat (free), Octopus Form, Redirect Lightning. Sequence: on the win turn, keep {U} for Spell Pierce/Swan
Song and Deflecting Swat in hand; cast the loop's cheapest piece first to draw out a counter; hold the Reversal last.
- Spell Pierce (BUY): {U}: stops a removal spell or wipe aimed at Azula early, and the answer to your loop on the win turn.
- Swan Song: {U}: counters an instant, sorcery or enchantment (wipe, removal, combo spell, stax enchantment).
- Negate: {1}{U}: any noncreature spell; hold it after a big attack.

**Commander protection and haste (8).**
- Swiftfoot Boots: hexproof and haste; recast is hasty for {1}.
- Champion's Helm: hexproof on a legend, +2/+2 (6/6 Azula wins most blocks).
- Haunted Cloak: vigilance (she still blocks after attacking), trample, haste.
- Hidden Footblade: {R} flash after blocks for first strike; haste on a recast.
- Octopus Form: hexproof in response, +1/+1 in a fight, or untap her as a blocker.
- Deflecting Swat: free while she is out: send the removal to their creature.
- Redirect Lightning: redirect a single-target removal spell (Lesson).
- Undying Malice: in response to destroy or a wipe she returns with a counter, no tax.

**Wipes (2).**
- Day of Black Sun: X=0 for {B}{B} kills every token (Board 1); X=3 spares Azula and the 4-drops. Sorcery: never copied.
- Ritual of Soot: everything at MV 3 or less: the reset against a go-wide or dork-heavy table; it also kills your reducers, Thermo, Electro and Dualcaster (Narset, a planeswalker, and Azula survive). Cast when they are absent or worth losing.

**Utility (1).**
- Propaganda (proven role-player): turn 3; each attacker costs {2}: they hit the others while Azula is tapped.

**Lands (36).** 6 Island, 6 Mountain, 5 Swamp; Command Tower, Exotic Orchard; check/reveal lands (Drowned Catacomb, Dragonskull
Summit, Sulfur Falls, Choked Estuary, Foreboding Ruins, Frostboil Snarl); Smoldering Marsh and Sunken Hollow (untapped with two
basics); pain lands (Shivan Reef, Sulfurous Springs, Underground River); filter lands (Cascade Bluffs, Sunken Ruins, Darkwater
Catacombs, Shadowblood Ridge); Fire Nation Palace (firebending 4 on the big turn); Rogue's Passage (Azula unblockable for {4}).

Multi-role count (R4): 31 of 63 nonland cards count in two or more profile functions (every window instant is spell_density
plus its job). Commander-centric count (R5): cards that do nothing useful without Azula: Turnabout's combo use only (it still
untaps lands), Fists of Flame (still a trick on Ozai/Godo), Hidden Footblade: 3 or fewer, under 12.

## 3. Curve, ratios and the reasons

| MV (X = 0) | 0-1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Cards | 11 | 26 | 14 | 9 | 1 | 2 |

Average MV 2.51 (nonland, X at 0) against 2.71 for the current list and 2.60 for iteration 1. Only three cards at 5+: Horizon
Stone (proven role-player), Godo and Ozai (each wins a game or a route by itself).

### 3.1 Profile table (spellslinger + combat_attackers as modifier)
| Function | Tier | Min | Target | Actual | Reason |
|---|---|---|---|---|---|
| Lands | band | 36 | 36 | 36 | Overlap of the two bands; X spells and Horizon Stone sink every land; 3 colors for a 4-MV gold commander. R8: lands + lasting ramp 36 + 7 rocks = 43 (+3 reducers = 46). |
| Ramp (turn 1 to 3) | base | 12 | 12 | 10 (WARN) | 3.3. |
| Draw (nets cards) | base | 12 | 18 | 12 by tag (Archmage, Narset, Gleam, Big Score, Thrill, Thirst, FoF, Pull, Abandon, Waterbending Lesson, Fists, Expedite at half), and about 16 effective in her window (Big Score, Thrill, Thirst, Fists, Expedite, Abandon double; Brainstorm copied). | Azula spends cards fastest (owner L2). |
| Spot answers (incl. counters) | base | 8 | 10 | 14 (11 at MV 2 or less, 13 instant + 1 flash) | R19. Fatal Push, Firebending Lesson, Spell Pierce, Swan Song, Terminate, Go for the Throat, Abrade, Failed Fording, Snap, Negate, Narset's Reversal, Hero's Downfall, Chaos Warp, Amphibian Downpour. Artifact answers: Abrade, Chaos Warp, Failed Fording; enchantment answers: Chaos Warp, Failed Fording, Swan Song (spell). |
| Wipes | base | 2 | 3 | 2 | Day of Black Sun (X controlled), Ritual of Soot. |
| Commander protection | attack engine | 6 | 8 | 8 + 3 counters | Boots, Champion's Helm, Haunted Cloak, Octopus Form (hexproof layers); Deflecting Swat, Redirect Lightning, Narset's Reversal (redirect/return); Undying Malice (destroy/wipe); plus Spell Pierce, Swan Song, Negate. 61 % to see two by turn 5 [J, 11 pieces]. |
| spell_density | gate early | 30 | 36 | 35 | Instants and flash only (the window). 100 % to see 3+ by turn 5. |
| spell_payoffs | gate late | 6 | 8 | 8 + tutors (10) | Azula, Archmage, Storm-Kiln, Dualcaster, Electro, Helm, Narset's Reversal, Thermo-Alchemist; Teachings, Godo. |
| through_wide_board | gate early | 10 | 12 | 10 + 2 tutors | Comet Storm, Electrodominance, Thermo-Alchemist, Day of Black Sun, Ritual of Soot, Rogue's Passage, Haunted Cloak, Fists of Flame, Electro (flier), Ozai (trample). Chumps never stop the copies. |
| through_big_creatures | gate early | 10 | 12 | 13 + 3 tutors | Removal after blocks (copied: two blockers), Snap, Failed Fording, Amphibian Downpour, Comet Storm, Electrodominance, Firebending Lesson kicked, Fists of Flame, Champion's Helm 6/6, Rogue's Passage. |
| window_mana | declared late | 6 | 8 | 9 + 2 tutors | Horizon Stone, Electro, Ozai (keepers); Storm-Kiln, Big Score (Treasures); Frantic Search, Snap, Turnabout (untaps); Fire Nation Palace. |
| Route access (R18) | champion | 10 | 12 | 14 | Six loop pieces + Mystical Teachings + Solve + Shred Memory + Narset + Gleam + Brainstorm + Thirst + the two finishers' tutors. |
| Win-turn shield (R24) | champion | 3 | 5 | 7 | Section 4. |
| haste | support | 4 | 6 | 4 | Swiftfoot Boots, Haunted Cloak, Hidden Footblade (equipment: stay after she dies), Expedite (one-shot, also a copied cantrip). |
| team_evasion | support | 6 | 8 | 5 (WARN) | 3.3. |
| defense_while_tapped | support | 4 | 6 | 5 | Propaganda, Haunted Cloak (vigilance), Thermo-Alchemist (defender), Nightscape Familiar (regenerate), Octopus Form (untap). |
| combat_draw | support | 4 | 6 | 5 | Archmage, Fists, Expedite, Thrill, Big Score. |
| wipe_insurance | support | 2 | 3 | 3 | Undying Malice, Negate, Swan Song; equipment, Helm and Horizon Stone survive creature wipes. |
| attackers | support (modifier) | 12 | 16 | 4 (WARN) | 3.3. |
| cost_reducers | support | 2 | 4 | 4 | Electromancer, Stormcatch, Nightscape, Glamdring. |
| Graveyard hate | floor | 1 | 1 | 1 | Shred Memory (instant; copied in the window: two graveyards). |
| Answers to commanders | floor | 2 | 3 | 4 | Chaos Warp, Amphibian Downpour (no tax reset), Failed Fording and Snap (tempo). |
| Rebuild after a wipe (R32) | champion | 4 | | 5 | Azula recast with haste from equipment left behind, Undying Malice, Waterbending Lesson, Pull from Tomorrow, Godo (fetches Helm). |

Fit check (each card once, primary function): ramp 10 + draw and dig 15 + spot answers 14 + wipes 2 + protection 8 +
loop pieces and engines 8 (Frantic, Turnabout, Dualcaster, Storm-Kiln, Archmage counted in draw, Thermo, Electro, Horizon
Stone) + finishers and combat route 5 + tutors 3 (Teachings, Solve, Shred Memory, which is also the graveyard hate) + Propaganda = 63 nonland; 36 + 63 = 99.

Answers against closers (red flag check): 14 spot answers + 2 wipes against 13 closers (Azula, Comet Storm, Electrodominance,
Thermo, Ozai, Godo, Helm, Storm-Kiln, Dualcaster, Snap, Reversal, Frantic, Turnabout). Answers lead by three because in this
deck every instant answer is also window fuel (it is copied, a two-for-one, and it untaps Thermo and makes Treasures); the
closers are a compact three-card engine, not a pile of answers without a finish.

### 3.2 Colors
Lands: blue 18 (6 Island + 12), black 18 (5 Swamp + 13), red 17 (6 Mountain + 11) + rocks (Arcane Signet,
Waterskin any color; Everflowing Chalice colorless; Izzet Signet U/R; Dimir Signet U/B). Karsten for a 4-drop gold commander with one pip of each: 17 per
color: met. Red has the most pips (Comet Storm, Electrodominance, Dualcaster, Electro, Ozai {R}{R}); firebending pays {R}{R}
in the window. Tapped lands: none always tapped (R10); conditional: check/reveal lands, Smoldering Marsh, Sunken Hollow,
Fire Nation Palace (untapped with a basic).

### 3.3 WARN reasons (none passed by relabeling)
- **Ramp 10 of 12.** Seven rocks at MV 1 to 3 and three cost reducers, all castable by turn 2 or 3. The two missing pieces are
  replaced by mana that only this commander makes, in the window where the deck spends it: firebending {R}{R}, Turnabout
  (copied: all lands twice), Snap and Frantic Search untaps, Big Score and Storm-Kiln Treasures, Fire Nation Palace; Horizon
  Stone banks the rest. A twelfth rock would cut a window card (spell_density 35) or an answer. Everflowing Chalice (owned)
  is the tenth; the review found Fellwar Stone worth only +0.01 over it for 1,560. Lands + lasting ramp 46 (R8) holds with the reducers.
- **Team evasion 5 of 6.** Azula's engine triggers on attacking, not on connecting: chump blockers cannot stop the copies, so
  the line matters only for combat damage, which is the third route. Rogue's Passage, Haunted Cloak, Fists of Flame, Electro
  (flier) and Ozai (trample) cover it; the noncombat routes do the rest.
- **Attackers 4 of 12** (support line of the modifier). Her trigger needs one attacker, herself; Helm of the Host adds a hasty
  Azula every combat. Twelve creatures would replace window instants (the iteration-1 review saw sorceries and permanents
  never copied).

## 4. Interaction plan and protection plan

- **Interaction:** 14 spot answers, 11 at MV 2 or less, all instant or flash (R19: at least 8, 5 at MV 2 or less, 5 instant).
  Three or more castable on an opponent's turn that stop a creature combo or a lethal attack: Fatal Push, Terminate, Go for
  the Throat, Hero's Downfall, Snap, Failed Fording, Firebending Lesson, Chaos Warp. Stack: Spell Pierce, Swan Song, Negate,
  Narset's Reversal (4 counters, R20: blue midrange/combo 4 to 6, chosen to protect its own win), plus Deflecting Swat and
  Redirect Lightning. Use removal on the few blockers that matter and on combo pieces, never on value creatures.
- **Protection of Azula:** layers: hexproof (Boots, Champion's Helm, Octopus Form), redirects (Swat free, Redirect Lightning,
  the Reversal), counters (Pierce, Swan Song, Negate), recursion (Undying Malice), recast with equipment haste. Equip before
  attacking; attack with {U} up when possible.
- **Win-turn shield (R24): 7 pieces at MV 2 or less or free:** Spell Pierce, Swan Song, Negate, Narset's Reversal, Deflecting
  Swat, Octopus Form, Redirect Lightning. Sequence: equip hexproof first; attack; cast the cheapest loop piece first (bait);
  keep {U} for Pierce/Swan Song and Swat in hand; cast the Reversal last; if Teachings is in hand, cast it in the window and
  take a loop piece AND a shield piece with the two copies.
- **Politics (review N6):** Swan Song gives the caster's opponent a 2/2 flier: aim it at the spell of the table's leader, and the
  Bird then pressures him too; Deflecting Swat and Redirect Lightning send a removal spell at the leader's best creature, which
  turns the attacker's own table against him; Propaganda pushes attacks toward the other players while Azula is tapped;
  Narset's static hurts the draw engines of the strongest player first. Do not take an early lead you cannot protect (R30).
- **Against wipes:** do not commit more than Azula and one engine before a win turn when two or more opponents can wipe;
  equipment, Horizon Stone and Propaganda survive; Undying Malice and the three counters cover the wipe turn.

## 5. Mulligan and play pattern

**Keep checklist (R33):** 2 to 4 lands (3+ when the hand has no 1-2 mana rock or reducer) AND a play by turn 2 or 3 AND a plan
piece or a way to find one. "Keep almost any land-good hand with": Sol Ring, Everflowing Chalice, Arcane Signet, Mystical Teachings,
Narset, Archmage Emeritus. Ship 0-1 landers, 6+ landers, hands of only answers.

**20 seeded hands (seed 20261108, scratch `az/sim` method):** kept 10 of 20 on the first seven (hands 2, 3, 7, 9, 10, 11, 12,
13, 15, 16); seven ships were 0-1 landers, three were 2-landers with no cheap rock (4, 5, 19, and 14 with only Waterskin).
Monte Carlo over 40,000 hands with the same rule: 66 % keep on the first seven, **89 % with the free mulligan** (target 85 %+).

**Turns 1 to 5:** turn 1 land, Sol Ring; turn 2 a 2-drop rock or reducer, Thermo-Alchemist, or hold Spell Pierce/Swan Song;
turn 3 Azula (with Sol Ring or a turn-2 rock) or Narset/Propaganda; turn 4 equip and attack: copy draw (Big Score, Thrill),
removal on blockers and Brainstorm; turn 5 Archmage or Storm-Kiln with a shield up, or the first copied Teachings.
**Turns 6 to 9:** the win turn when the loop is in hand and the shield is up; otherwise copied Comet Storm for 2X to each
opponent (X 5 to 8), Helm of the Host on Azula, Godo if she is answered. **Late:** Turnabout + Horizon Stone for a single huge
Comet Storm; Godo + Helm; Pull from Tomorrow at end steps.

**Goldfish, five games played turn by turn (seed 1108, first five shuffles with 3 to 4 lands in the opening seven; no
opponents; draw from turn 1) [R38]:**
| Game | Opening seven | Azula cast | First copied combat | What happened to turn 9 |
|---|---|---|---|---|
| 1 | Snap, Sol Ring, Glamdring, Thermo-Alchemist, 3 lands | T3 (Sol Ring) | T4: Fact or Fiction copied (two piles) | Narset T5 digs; Thermo pings 2 a turn cycle; Snap waits for Dualcaster/tutor; table threat by copied burn about T8 |
| 2 | Spell Pierce, Thermo, Comet Storm, Nightscape Familiar, 3 lands | T4 (Nightscape discount, Pierce up) | T5: Dualcaster flashed in, Comet Storm copied three times (X 2, two kicks): 6 to each opponent | Second Comet Storm turn impossible without a tutor; kill about T8-9 with Thermo and combat |
| 3 | Champion's Helm, Izzet Signet, Narset, Ritual of Soot, 3 lands | T4 | T5: hexproof 6/6, copies Abrade and Failed Fording | No finisher or loop seen by T9 despite two Narset digs: a slow game won only by combat with Helm; the weakest of the five |
| 4 | Expedite, Propaganda, Octopus Form, Thirst, 3 lands | T4 | T5: Thirst copied (six cards), Snap and Fists of Flame found | Electromancer and Sol Ring T5-6; table threat about T8 |
| 5 | Firebending Lesson, Thirst, Narset, Abrade, 3 lands (two enter tapped) | T4 | T5: Terminate and Negate held; Thermo pings | Horizon Stone T6 banks mana; Day of Black Sun for a board; threat about T9 |
Summary: Azula on T3 once, T4 four times; first copied combat T4 to 5; no loop assembled by T9 in these five (two of them
saw a loop piece without its partner); the first table-wide threat came on T8 to 9 from copied burn and Thermo-Alchemist.
The loops are the ceiling, the copied fair game is the floor. Raw odds over 40,000 shuffles (draw spells NOT counted, so
conservative): all pieces of a loop seen or tutorable 17 % by turn 6, 22 % by turn 8, 27 % by turn 10 (current list
15/20/24 %, iteration 1 15/19/24 %), slightly more with Shred Memory as a third tutor; a finisher or a tutor 42 % by turn 6.
**Disrupted (on games 1, 2 and 4):** (a) game 1, Azula killed on her first attack T4: recast T6 for 6 mana with no equipment
yet, she attacks T7: the plan slips two turns; (b) game 2, wipe on T6: Spell Pierce held and countered it (the opponent at
three open mana could not pay 2); (c) game 4, the first Thirst copy countered: the hand still held Snap and Fists, the next
combat retried, one turn lost.

**Gauntlet (R39):**
1. Fast combo (turns 5 to 7): Swan Song, Spell Pierce, Negate, Narset's Reversal on the stack; Fatal Push, Terminate,
   Firebending Lesson, Snap on creature combos at instant speed; Shred Memory against graveyard combos; Narset's static
   blanks draw-based engines.
2. Stax and taxes: cheap threats (Azula at 4, Thermo at 2); Abrade, Chaos Warp, Failed Fording, Swan Song (enchantment spell)
   against the pieces. Weak point: "spells only at sorcery speed" (answer it with Chaos Warp/Failed Fording first).
3. Go-wide tokens (Board 1): Day of Black Sun X=0, Ritual of Soot, Thermo-Alchemist, copied Comet Storm; chumps never stop the
   copies; Propaganda taxes the swarm.
4. Big creatures (Board 2): copied removal after blocks kills two, Snap and Failed Fording bounce two, Amphibian Downpour,
   Champion's Helm 6/6, Fists of Flame wins the block, Rogue's Passage.
5. Control (counters and wipes): Narset's static and her dig, threats spread (Azula, Ozai, Godo, Thermo), instant-speed draw at
   end steps, the shield counters on the win turn, rebuild in section 3.1.

## 6. BUY (owner, 2026-11-08: each card under 3,000 CLP, three stores, Azula all-in 6,000)

Ranked by gain per CLP (the review's ranking, gain in real-power points [J]). The lead verifies live stock before buying.
"To read" prices come from suggest.json on 2026-11-08 (product JSON answered HTTP 429): the "from" figure can be a sold-out or
played variant, so the ceiling is budgeted; any copy better than Damaged is acceptable (owner's condition rule, 2026-11-08).
| # | Card | Store | Price (CLP) | Language | Gain | Plays until it arrives |
|---|---|---|---|---|---|---|
| 1 | Thirst for Knowledge | Rivendel El Concilio | 300 (read 2026-11-08, 2 in stock) | ES | +0.03: instant draw three, six copied; the order's "stock" copy becomes Azula's, Kilo keeps its own | Lightning Strike (owned) |
| 2 | Narset, Parter of Veils (Game Changer 1 of 3) | Game of Magic Singles | 1,440 (read live 2026-11-08) | EN | +0.10: two -2 digs for noncreature spells (every loop piece, tutor and finisher); static stops the table's extra draws | Zuko, Exiled Prince (owned) |
| 3 | Shred Memory | Game of Magic Singles (from 680) or PayToWin (from 1,100, Ravnica: City of Guilds) | 1,100 ceiling (to read) | EN or ES | +0.06: third real tutor to the loops (transmute for the Reversal or Snap) and the graveyard hate | Soul-Guide Lantern (owned, free ES copy) |
| 4 | Spell Pierce | Game of Magic Singles (Double Masters, NM EN) | 570 (read live 2026-11-08) | EN | +0.03: {U} shield for the win turn and Azula's first turns | Mana Leak (owned, free) |
| 5 | Turnabout | Game of Magic Singles (from 445) or PayToWin (from 960; DMR, RVR retro) | 1,560 ceiling (to read; GoM's DMR retro is sold out) | EN | +0.07: a fourth Reversal partner (Azula + Reversal + Turnabout, unbounded mana) and alone a copied double untap of all lands for Comet Storm | Opt (owned) |
| | **Total buys** | | **4,970** | | | |

Cut order if the global target needs room (review): Spell Pierce (Mana Leak plays, -570) → Turnabout (Opt plays, -1,560) →
Shred Memory (Soul-Guide Lantern plays) → Thirst (stock line) → Narset last.

Rejected (over 3,000 each or no stock in the three stores, suggest.json 2026-11-08): Fellwar Stone (1,560: the review found
+0.01 over the owned Everflowing Chalice), Crackle with Power (7,200+; the best finisher: 6 mana copied = 30 to each
opponent), Dark Ritual (2,500+), Seething Song (4,650+), Pyretic and Desperate Ritual (4,700+), Merchant Scroll (3,800),
Lim-Dûl's Vault (3,900), Mystic Remora (9,300), Pyroblast (8,100+), Deadly Rollick (18,900+); Notion Thief, Valley Floodcaller,
Arcane Denial: no stock. Counterspell (PayToWin 1,700 to 3,400) and Muddle the Mixture (1,700 to 8,100): next in if the
envelope grows, with Lightning Bolt (PayToWin from 900).

**Game Changers (checklist item 34, not applied for budget):** 1 of 3. No Game Changer is owned for Azula and none other is in
stock under 3,000 in the three stores (Mystical Tutor 21,600 and up; Rhystic Study, Fierce Guardianship, Jeska's Will,
Underworld Breach, Cyclonic Rift all far above). The two free slots stay open; nothing in the list blocks them.

## 7. Loans and replacements

- **Overpowering Attack: returned, no replacement.** The loan is dropped and its replacement (PayToWin 1,440, line 10 of the
  final order) is NOT bought: a 5-mana sorcery that needs Azula to connect first; Turnabout buys a bigger second window of mana.
  For the lead: remove Azula's `borrowed` entry in `decks/phase2.json`, the restock row and order line 10 (shared files, not
  edited here).
- No other loan. Propaganda and Hidden Footblade are the owner's own scanned copies (Ezio plays the loan Hidden Footblade
  and buys its replacement).

## 8. Scarce copies and languages

| Card | Copies (language) | Held by | Azula's claim |
|---|---|---|---|
| Swan Song | 1 (ES) | Kilo's current list | **Claim.** The only 1-mana counter in the pool that stops a wipe or the removal aimed at Azula; English copies cost 79,000+. Kilo loses one counter (review N1: with Swan Song and Negate both in Azula, Kilo is left with one Spanish counter). If the lead rules for Kilo, the fallback here is Azula's Negate → It'll Quench Ya! (owned EN), keeping Swan Song. |
| Thirst for Knowledge | 1 owned (ES) + 1 bought (stock line, Rivendel 300, ES) | Kilo keeps the owned copy | Azula takes the bought one: no conflict. |
| Everflowing Chalice | 3 (2 EN, 1 ES) | Kilo 1 | Azula takes an English copy: no conflict. |
| Black Market Connections | 1 (EN) | Ezio (final) | Not claimed: Ezio keeps it; replaced by Everflowing Chalice (ramp) and Thirst (draw). |
| Mystical Teachings, Swiftfoot Boots, Haunted Cloak, Propaganda, Terminate, Chaos Warp, Drowned Catacomb, Dragonskull Summit, Sunken Hollow, Sulfur Falls | 2+ | Ezio holds one | Azula takes the other (English). |
| Command Tower, Exotic Orchard, Sol Ring, Arcane Signet, Rogue's Passage, Shivan Reef, Cascade Bluffs | enough | Toph / Kilo / Ezio | Azula takes the English copy where Kilo needs the Spanish one (Shivan Reef, Cascade Bluffs, Sulfur Falls, Chaos Warp: EN for Azula). Command Tower: the English copy if free, else Spanish. |
| Smoldering Marsh | EN (LTC) + ES (owed) | Ezio takes the owed Spanish copy | Azula plays the English LTC copy. |

Soul-Guide Lantern is no longer claimed (Shred Memory replaces it). Spanish-only copies Azula plays (no English owned):
Choked Estuary, Darkwater Catacombs, Sulfurous Springs, Exotic Orchard, Helm of the Host, Mind Stone, Narset's Reversal,
Negate, Nightscape Familiar, Pull from Tomorrow, Solve the Equation, Swan Song, Thrill of Possibility, Thirst for Knowledge
(bought); Shred Memory may be either language.

## 9. Comparison with the current list and iteration 1

Against the current list after purchases (`decks/phase2/moxfield/fire-lord-azula-after-purchases.txt`, Salt 7.3):
| Out | Why | In | Why |
|---|---|---|---|
| Overpowering Attack (loan) | 5-mana sorcery, needs a connect; returned, no replacement | Turnabout | Fourth Reversal partner; copied double untap of all lands |
| Black Market Connections | Ezio's (scarce copy, Ezio final) | Everflowing Chalice | Turn-2 ramp, scales late |
| Torrential Gearhulk | 6 mana (R35), recasts X spells at X = 0 | Thirst for Knowledge | Instant draw three, six copied |
| Zuko, Exiled Prince | 4-mana creature, a slow impulse sink | Spell Pierce | 1-mana win-turn shield |
| Azula, On the Hunt | 4-mana second attacker, loses life, dies in blocks | Swan Song | 1-mana counter for wipes and removal |
| Frostcliff Siege | 3-mana enchantment, one mode at a time | Firebending Lesson | 1-mana instant removal |
| Lightning Strike | 2 mana for 3 damage | Failed Fording | 2-mana instant bounce of ANY nonland permanent |
| Opt | Cantrip | Redirect Lightning | Redirect: shield and protection |
| Cunning Maneuver | Trick whose Clues cost {2} more each | Expedite | {R} cantrip (two cards copied), haste for a recast |
| Soul-Guide Lantern | Graveyard hate only | Shred Memory | Graveyard hate AND a transmute tutor for the Reversal or Snap |

Against iteration 1 (`decks/measured/fire-lord-azula/round4-step27.txt`, Salt 8.4): out Entomb, Lo and Li, Loyal Inventor,
Reckless Handling, Ember Island Production, Goblin Bombardment, Banefire, Aether Gale, The Last Agni Kai, Imprisoned in the
Moon, Heartless Act, Ultimate Price, Mana Leak, Lightning Strike, Consider, Ponder, Opt, Torrential Gearhulk, Frostcliff
Siege, Black Market Connections; in Turnabout, Narset, Everflowing Chalice, Spell Pierce, Swan Song, Thirst, Shred Memory,
Expedite, Firebending Lesson, Failed Fording, Thermo-Alchemist, Horizon Stone, Propaganda, Haunted Cloak, Hidden Footblade,
Pull from Tomorrow, Thrill, Abandon Attachments, Waterbending Lesson, Fists of Flame.

**Iteration 1's four tutors (corrected after the review).** None of the four could fetch a LOOP piece: the six pieces are
instants (Snap, Reversal, Frantic Search, Turnabout) and creatures that are neither Lesson nor Noble nor artifact (Dualcaster,
Storm-Kiln); Lo and Li fetch only Lessons and Nobles (Octopus Form, Redirect Lightning, Ozai), Loyal Inventor and Reckless
Handling only artifacts, Entomb only bins a card. But they were not useless for winning: Loyal Inventor and Reckless Handling
reached Helm of the Host (the Godo + Helm line and Helm on Azula), and Entomb could bin Mystical Teachings for its 7-mana
flashback. So the earlier sentence "never reached a win line" was wrong; "never fetched a loop piece" is right, and the
simulation agrees: iteration 1's loop access (15/19/24 % by turns 6/8/10) equals the current list's (15/20/24 %) although it
had four more tutors. Godo already fetches Helm, so those four do not come back. What this list adds instead is a third REAL
tutor to the loops, Shred Memory (transmute for the Reversal, the hub of three lines, or Snap), next to Mystical Teachings
(copied in combat: two pieces) and Solve the Equation, plus a sixth loop piece (Turnabout), copied instant dig (Narset, Gleam,
Brainstorm, Thirst, Thrill, Big Score) and a shield so the assembled loop resolves.

**Cheap removal came back:** 15 spot answers (11 at MV 2 or less, all instant or flash, counting Shred Memory's graveyard
mode apart) against about 10 cheap instant answers in the current list and 14 in iteration 1, with four counters instead of
two (Spell Pierce, Swan Song, Negate, the Reversal) and two or more answers each to enchantments and artifacts.

## 10. Real-power estimate (1-10 scale: 4 precon, 6 upgraded, 7-8 high power, 9-10 cEDH)

**7.5 to 7.9, confidence medium-low** [J; the review's figure after F1 to F3; project estimates have run 0.3 to 2.1 high].
Against the current list (7.2-7.7): +0.2 to +0.3 from a lower curve, 35 window cards instead of 30, a fifth combo line, a
third real tutor to the loops, a 7-piece win-turn shield, cheap instant removal restored and haste at 4. It loses Black
Market Connections (Ezio's) and two value creatures. The goldfish shows the floor honestly: without a loop the deck kills on
turn 8 to 9. Commander Salt expected 7.3 to 7.7 (floor 7.0); to be measured by the lead.

## 11. Total spend of the deck (all-in)

| Item | CLP |
|---|---|
| Thirst for Knowledge (moved from the stock line, read) | 300 |
| Narset, Parter of Veils (read) | 1,440 |
| Shred Memory (ceiling, to read) | 1,100 |
| Spell Pierce (read live, Game of Magic) | 570 |
| Turnabout (ceiling, to read) | 1,560 |
| Loan replacements (Overpowering Attack returned, no replacement) | 0 |
| Tokens (decks/reports/tokens-20261108.md): Treasure (Big Score, Storm-Kiln) owned; the 2/2 blue flying Bird that Swan Song gives an opponent is not owned and was "Sin stock" in the three stores (it moves with the card from Kilo); Dualcaster, Helm and Godo copies need no printed token. Re-run `scripts/token_needs.py` on the final lists. | 0 |
| **All-in** | **4,970 of 6,000** (1,030 margin; the two "to read" prices are budgeted at their ceilings) |

Against the order before the rebuild: Azula 2,880 → 4,970 (+2,090); the stock section falls by 300 (Thirst moves to Azula),
so the grand total moves by +1,790 (91,792 → about 93,582 before the other decks' rebuilds), under the 100,000 cap.

## Cut log (cards considered, with the reason)

| Card | Function | Count after | Replacement | Reason |
|---|---|---|---|---|
| Overpowering Attack | extra combat | combat route 4 closers | Turnabout | Sorcery that needs Azula to connect; a 1,440 replacement buy. |
| Torrential Gearhulk | payoff | payoffs 8 (6) | Thirst for Knowledge | MV 6 (R35); its free recast sets X to 0 for the finishers. |
| Zuko, Exiled Prince; Azula, On the Hunt | window mana, draw | window_mana 9 (6) | Spell Pierce, Swan Song | Two 4-drops that die in blocks; the shield is the missing champion function. |
| Frostcliff Siege | haste, evasion | haste 4 (4) | Firebending Lesson | One mode at a time; cheap answers restored instead. |
| Lightning Strike | removal | spot 15 (8) | Failed Fording | Failed Fording answers any nonland permanent. |
| Opt, Mana Leak | cantrip, soft counter | density 35 (30) | Redirect Lightning; 36th land | Opt is not draw; Mana Leak is soft late; the land restores the band. |
| Black Market Connections | draw/ramp | draw 12 (12) | Everflowing Chalice | Ezio's final list holds the only copy. |
| Fellwar Stone (fix F2) | ramp | ramp 10 | Everflowing Chalice | Owned card doing nearly the same job; saves 1,560. |
| Cunning Maneuver (fix F3) | trick, Clues | through_big_creatures 13 + 3 tutors (10) | Expedite | Weakest window card; Expedite closes the haste line. |
| Soul-Guide Lantern (fix F1) | graveyard hate | graveyard hate 1 (1) | Shred Memory | Same floor plus a tutor to the loop hub. |
| Entomb, Lo and Li, Loyal Inventor, Reckless Handling | tutors | real tutors to the loops 3 | (section 9) | Fetch no loop piece; Helm is already fetched by Godo. |
| Malcolm, Ember Island Production, Goblin Bombardment, Banefire, The Last Agni Kai, Heartless Act, Ultimate Price, Imprisoned in the Moon, Lightning Axe, It'll Quench Ya!, Dimir Locket | various | | | Mini-combo, sorcery speed, narrower than the chosen answer, or slower; Heartless Act is the next removal in. |

Proven role-players: Horizon Stone and Propaganda IN.

## Self-review (step 15)

1. Plan in one sentence: yes; 0 orphans. 2. Every gate function at or above min; no early plan-critical function under 10.
3. Fuel: copied draw keeps the hand at 4+ through turns 4 to 8 (spends about 2 cards a combat, draws 3 to 5 in it).
4. 36 lands, 17 to 18 sources per color, turn-2 and turn-3 plays in most keeps. 5. Attack engine, 8 protection + 3 counters,
layered against removal and wipes. 6. Boards: sections 4 and 5. 7. Three routes, disjoint closers, two noncombat, each hits
three opponents; the Frantic loop is listed as dig and mana, not as a kill. 8. Haste 4, evasion 5 (WARN with reason),
defense 5; toughness: Azula 4 (6 with Champion's Helm), the 2-toughness engines are kept home. 9. Bracket 3: 1 Game Changer
(live list via the script), no extra turns, no land denial, Godo + Helm late. 10. Cut log above; rules points R1 to R9 with
status. Checklist: 40 of 41 items applied after the fix round; item 34 (Game Changer slots) stays at 1 of 3 for budget.
