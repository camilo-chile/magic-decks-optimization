# Collection review: Fire Lord Azula (Phase 2 step 10.2, iteration 3, 2026-11-14)

Independent adversarial review of `decks/phase2/fire-lord-azula.txt` (built by Fable 5.2 high), with its
`.plan.json`, `.build.md` and `decks/reports/consistency-fire-lord-azula.md`, under
`docs/proposals/collection-optimization-brief-20261114.md`. Pool: `data/model/phase2/pool-fire-lord-azula.json` (frozen
collection, no purchases, loans or exchanges). Web read today as data: Scryfall API (rulings of Fire Lord Azula, Return the
Favor, The Last Agni Kai, Tome of Legends), EDHREC JSON for Azula (40,394 decks). No deck file was edited.

**Verdict: FIX.** No Bracket 3 rule is broken and the gate passes; the list is legal and strong. It must take Return the
Favor (owner's decision), and the plan file overstates draw and haste. Ranked change list at the end.

Process note: running `check_phase2_bracket.py` on a scratch copy wrote `decks/reports/bracket-fire-lord-azula.md` (the
script names its report by file name). I re-ran it on the real list at once; the file again holds the real list's report
(5 variants, 1 flagged, PASS). Later scratch tests wrote only to the scratchpad.

## 1. Independent reading (blind pass, from the Oracle text before the plan file)

**Commander.** {1}{U}{B}{R} 4/4. Firebending 2: {R}{R} on attack, kept until end of combat. Every spell cast while she
attacks is copied (permanent spells become tokens). Scryfall rulings (2025-10-02): copies are not cast; X is kept; extra
costs are not paid again; choices made on resolution are made again for the copy; firebending mana "is lost as normal" on
leaving combat (so Horizon Stone, Ozai and Electro's "if you would lose unspent mana" apply to it).
- Fuel: instants and flash cards in hand, and mana inside her combat. The copy needs her ATTACKING, not connecting: chump
  blockers never stop the engine.
- Dependence: **attack engine** (she does nothing unless attacking). She costs 4, so the skill's promotion test (SKILL 3.1)
  points haste toward a gate line.
- Dies to: instant removal during the attack, wipes, blocks by creatures with power 4+, the crack-back while tapped.

**Plan (my reading).** Attack with Azula from turn 4 to 5 behind hexproof and cheap counters; double every instant in the
window (draw, removal, tutors); win in one protected combat by a loop with her (Narset's Reversal + Turnabout, Frantic
Search or Storm-Kiln Artist; Snap + Dualcaster Mage) or a copied Comet Storm. Backup: Godo + Helm of the Host (no Azula
needed), Ozai, uncopied burn with banked mana. Same as the builder's.

**Recount of every function (skill 3.4 weights).**

| Function | Cards (Oracle) | My count | Builder |
|---|---|---|---|
| Lands | 19 nonbasic + 7 Island, 5 Mountain, 5 Swamp | 36 | 36 |
| Colored land sources | U 19, B 18, R 17 (Tower and Orchard in each; Rogue's Passage colorless) | same | same |
| Always-tapped lands | none; Smoldering Marsh and Sunken Hollow are tapped on turns 1 to 2 (need two basics) | 0 + 2 de facto | 0 |
| Ramp (lasting) | Sol Ring, Arcane Signet, Everflowing Chalice, Izzet Signet, Dimir Signet, Mind Stone, Bender's Waterskin; reducers Goblin Electromancer, Stormcatch Mentor, Nightscape Familiar | 10 (+ Black Market Connections' Treasure) | 11 |
| Draw that nets cards | Archmage Emeritus 1, Black Market Connections 1, Narset 1, Fact or Fiction 1, Pull from Tomorrow 1, Gleam of Death 1; Frostcliff Siege 0.5 (Jeskai mode only); Thirst 0.5; Big Score 0.5 (net 0 out of the window); Thrill 0.5; Abandon Attachments 0.5; Expedite 0 (cantrip); Brainstorm 0 (cantrip) | **about 8.5 to 9** | 12 "by tag" |
| Tutors | Mystical Teachings (instant or flash), Solve the Equation (instant or sorcery), Shred Memory (transmute MV 2), Godo (Equipment) | 3 + Godo | 3 + Godo |
| Spot answers | Heartless Act, Terminate, Go for the Throat, Hero's Downfall, Abrade, Chaos Warp, Failed Fording, Amphibian Downpour, Imprisoned in the Moon, Snap; counters Spell Pierce, Swan Song, Negate, Mana Leak (+ Narset's Reversal) | 14 (+1) | 15 |
| Mass answers | Day of Black Sun, Aether Gale (one-sided bounce) | 2 | 2 |
| Commander protection | Swiftfoot Boots, Champion's Helm, Octopus Form, Deflecting Swat, Redirect Lightning, Narset's Reversal + 4 counters | 10 | 6 + 4 + 1 |
| Wipe insurance | 4 counters; also Snap and Failed Fording bounce Azula in response (no tax), not listed by the builder | 6 | 4 |
| Haste for Azula | Swiftfoot Boots, Hidden Footblade, Expedite (one-shot, half), Frostcliff Siege (Temur only) | **2.5 to 3.5** (+4 tutors) | 4 |
| Spell payoffs | Azula, Archmage, Storm-Kiln, Thermo-Alchemist, Electro, Gearhulk, Dualcaster (copy) | 7 | 9 (adds Helm and the Reversal, which pay off nothing) |
| Window cards | 30 instants + 4 flash (Dualcaster, Gearhulk, Footblade, Downpour) | 34 | 34 |
| Graveyard hate | Shred Memory (also the MV-2 tutor: one use only) | 1 | 1 |

**Curve.** MV 0/1/2/3/4/5/6: 1/8/26/16/7/2/3 (X = 0), average 2.60, 35 cards at MV 2 or less. Matches the builder.

**How it loses.**
- To a wipe: Azula and the 2-toughness engines (Archmage, Storm-Kiln, Dualcaster, reducers) die; four counters, Narset's
  Reversal (returns the wipe to hand) and Snap or Failed Fording on Azula in response are the insurance; Boots and Siege stay
  for a hasty recast at 6; Gearhulk, Pull, Fact or Fiction and Godo rebuild.
- To eight 1/1 chump blockers: the engine does not care; combat damage does. Comet Storm, Thermo, the loops, Day of Black
  Sun at X = 0 or 1 (it misses token COPIES, which keep the original's mana value), Aether Gale, Siege's trample.
- To two bigger creatures: Azula (4/4) dies in a block by a 5/5. Answers after blocks are copied (8 instant kills), Hidden
  Footblade's first strike, Champion's Helm 6/6, Octopus Form; attack the player without them.

## 2. Differences with the builder

| Point | Builder | Review | Effect |
|---|---|---|---|
| Draw | 12 by tag | about 9 effective: Expedite and Brainstorm are cantrips; Thrill, Abandon, Big Score net 0 outside the window (half weight when copied); Siege draws only in Jeskai | Spellslinger floor is 12 (`archetypes.json`); owner L2: Azula needs the MOST draw |
| Haste | 4 (support) | Siege is counted in haste AND draw, but one mode is chosen on entry; Expedite is a one-shot; the promotion test is not written | 30 % to see a haste card by turn 4 with Siege on Jeskai (38 % with it on Temur); 52 to 57 % with the tutors |
| Spell payoffs | 9 | 7: Helm of the Host and Narset's Reversal pay off no spell | Still above the late minimum 6 |
| Azula on curve | "by turn 4 in 88 % (colors ignored)" | 75 % by turn 4, 84 % by turn 5 WITH colors (my Monte Carlo, 40,000 games, rocks and Nightscape modeled; 87.5 % colors ignored, which reproduces the builder) | The three-color pip need costs about 13 points on turn 4 |
| Wipe insurance | 4 counters | also Snap and Failed Fording (bounce her in response) | The list is better than written here |
| Board 1 | "Day of Black Sun at X = 0 kills every token" | Token copies of creatures keep their mana value (note N3 of the 2026-11-08 review, not applied) | Wording |
| R1 (bankers) | "no joint ruling" | Confirmed: the Azula ruling says firebending mana is lost "as normal" on leaving combat, so the "if you would lose unspent mana" replacements apply | Route B stands |
| Loop with Archmage | "never loop Frantic Search with Archmage out" | The Reversal + Turnabout loop with Archmage out draws 6 cards per cycle (mandatory magecraft): about 10 cycles before decking; enough for an X of 60+, but count them | Guide note |
| The Stasis Coffin | "OUT (Toph's)" | The copy is FREE in the pool; the right reason is that it protects the player, not Azula (and Toph wants it) | Reason fixed, verdict stands |
| Evie Frye | "the Fryes need each other" | Evie loots alone ({1},{T}); OUT stands because a 2-mana looter is below every 2-drop here | Reason fixed |

## 3. Rules

| Check | Result |
|---|---|
| Card count | 100 (commander + 99), summed from the file |
| `python scripts/check_phase2_bracket.py decks/phase2/fire-lord-azula.txt` | PASS, floor 3, 1 Game Changer (Narset, Parter of Veils), 0 extra turns, 0 mass land denial, 0 reversible; Godo + Helm classed late |
| Same check with Return the Favor for Hero's Downfall (scratch) | PASS, floor 3: variant 11-5940 reads "reviewed by the owner" (`data/bracket-reviewed.json`); the Azula self-copy hazard is floor 3 |
| Same check with the full change list below (scratch) | PASS, floor 3, 1 Game Changer |
| `python scripts/plan_density.py` | PASS, 0 failures, 3 WARNs (attackers 5/12, team evasion 4/6, ramp 11/12) |
| Gate with the full change list (scratch plan) | PASS, 4 WARNs (attackers, team evasion, ramp 10/12, draw 11/12 by tag); spell_density 34, payoffs 13, wide board 14, big creatures 18, window mana 13 |
| Game Changers | 1 of 3; the pool holds no other Game Changer in Grixis identity (only Narset is flagged), so R34 cannot be filled |
| Early two-card infinite | None. Every loop needs Azula attacking + 2 cards (three with the commander) |
| Copies | Every card has a copy: free, or Azula's own today; one claim (Black Market Connections from Ezio, section 6) |
| Language | Correct: Spanish only where no English copy is free (Gearhulk CMM 128 and Aether Gale SOC 186 new; Command Tower ES because both English copies sit in Toph and Ezio); everything else English |
| Reversible cards | None (Glamdring // Gleam of Death is an Adventure) |

## 4. Findings

### BLOCKING
None. No rule is broken.

### IMPORTANT

**I1. Return the Favor is out against the owner's decision of 2026-11-14.** [owner decision]
- Evidence: the bracket script now passes it (floor 3, section 3). Oracle: {R}{R} spree, +{1} copy target instant or
  sorcery spell OR activated or triggered ability, +{1} change the target of a single-target spell or ability.
- What it does here: firebending pays {R}{R}; copied in the window it forks Comet Storm twice (four Comet Storms with
  Azula's copy, X kept per ruling); it redirects removal aimed at Azula, including an edict (a ninth win-turn shield piece
  that also hits ABILITIES, which Swat and Redirect Lightning also do but the counters do not); it copies firebending (+{R}{R}),
  Godo's extra-combat trigger, Helm's token trigger or Electro's leave trigger. With Azula attacking, her copy of Return the
  Favor can target the original, so each copy makes another: with Storm-Kiln Artist that is unbounded Treasures, with
  Archmage unbounded draw (you stop the chain by retargeting). A seventh loop piece.
- Loop access (my Monte Carlo, pieces or tutors seen, colors ignored): 28.3 % by turn 6 and 34.5 % by turn 8 today;
  **31.0 % and 37.8 %** with Return the Favor.
- Fix: rank 1 below (it replaces Hero's Downfall; reasons there).

**I2. Draw is overstated and below the spellslinger floor.** [sourced: `archetypes.json` spellslinger draw min 12 "count
only draw that nets cards; cantrips ... go in spell_density"; SKILL 3.4 weights; owner L2]
- Evidence: section 1 recount, about 9 effective against 12 by tag. The builder cut Waterbending Lesson (net +2) and Fists of
  Flame and added two engines (Black Market Connections, Siege), so the real count rose only about 1.
- The pool has little better draw (Tome of Legends, Commander's Sphere, Cryogen Relic, Notion Rain, Waterbending Lesson,
  Divination; none is copied in the window). Fix: write the effective count and the reason in the profile table (the WARN
  must be honest); keep one draw ENGINE whatever happens to Black Market Connections (rank 2: Tome of Legends).

**I3. Haste is double-counted and the promotion test is not written.** [sourced: SKILL 3.1 promotion test; 3.4
conditional pieces; owner L3; the Azula study S6 "haste was considered, but full mana during attacks was preferred"]
- Evidence: Frostcliff Siege sits in `support.haste`, `support.combat_draw` and the `draw` tag, but its mode is chosen once
  as it enters. The build notes play it on Jeskai when Boots is on, which is when haste matters least, and the owner wants it
  for its constant draw. Expedite is a one-shot (half weight). Honest count: Boots, Footblade, half of Expedite, and Siege
  only when on Temur = 2.5 to 3.5 pieces. Tutors reach Boots (Shred Memory, Godo), Footblade (Teachings, Godo) and Expedite
  (Teachings, Solve).
- Odds of seeing haste by turn 4 (11 cards, no mulligan): 30 % with Siege on Jeskai, 38 % on Temur; 52 to 57 % counting the
  tutors.
- Fix: write the promotion test result in the profile table. My reading: haste stays support, because the sourced strong
  lists accept the turn and spend on protection (B4 average: Boots 49 %, Greaves; study S6). Count Siege in ONE line per
  game state. Optional card fix in MINOR M3.

**I4. Black Market Connections claim: the copy adds more in Ezio.** [J] Section 6. Recommended: return it, take Tome of
Legends.

### MINOR

- **M1. The weakest slot, Abandon Attachments, has a better free card: Venser, Shaper Savant (EN 2X2 66, free).** [J; skill 9
  "last slots prefer high floor"; R19, R20]
  - Abandon is a rummage: net 0 cards outside the window, +1 when copied.
  - Venser has flash and returns a SPELL or a permanent. Only Mana Leak answers a creature spell or a commander on the
    stack today, and Mana Leak is soft after turn 5.
  - In the window Azula copies Venser: two bounces, of blockers, a commander or spells.
  - On an opponent's turn it is a flash 2/2 blocker. The builder logged it as "first in if a counter leaves".
- **M2. Red needs more sources than black once Return the Favor is in.** [J; Karsten table, `mana-and-ramp.md` 4]
  - Off-window red double pips: Return the Favor ({R}{R}+1 on opponents' turns), Dualcaster and Electro ({1}{R}{R}), Comet
    Storm and Electrodominance at end steps.
  - Black double pips left after Hero's Downfall goes: Day of Black Sun (a sorcery), Ozai, Shred Memory's transmute.
  - Swap one Swamp for one Mountain. The Monte Carlo shows no change to Azula's own odds (symmetric), so it is low impact.
- **M3. Optional haste card.** [J] Haunted Cloak (EN CMM 389, the copy this list released) for Champion's Helm.
  - Gains: haste, vigilance (defense while tapped, owner L3) and trample (chump blocks become bad, owner's signal).
  - Costs: the second hexproof and the +2/+2 against Board 2.
  - Not in the change list: protection stays at 10 either way, and the call is the lead's.
- **M4. Plan file honesty (no card change).** Drop Helm of the Host and Narset's Reversal from `spell_payoffs`; tag
  Propaganda as defense, not protection; count Shred Memory once (tutor OR graveyard hate per game).
- **M5. Build notes.** Write Azula's colour-aware curve odds (75 % by turn 4, 84 % by turn 5). Fix the Day of Black Sun
  token line (N3). Mark R1 confirmed by the ruling. Add the Archmage note on the Turnabout loop. Fix the reasons for The
  Stasis Coffin and Evie Frye. Add Ty Lee, Chi Blocker (free, 14 % EDHREC) and Cunning Maneuver to the cut log.
- **M6. Kilo may contest Azula's Spanish-only copies.**
  - Swan Song (1 copy), Negate and Thirst for Knowledge (the second copies; Kilo holds one each) exist only in Spanish, and
    Kilo plays Spanish only.
  - A lead decision of 2026-11-02 in `owner-decisions.md` gave Swan Song to Kilo; today Azula holds it.
  - Azula's fallbacks: It'll Quench Ya! (EN, 3 free) for Swan Song or Negate; Divination or Cryogen Relic (EN free) for
    Thirst. The lead decides when Kilo is optimized.

## 5. Every slot, the curve and the ratios

**Weakest ten nonland cards and the best free candidate** (puzzle check: alone, on the turn drawn, with which cards).

| # | Card | Problem | Best free replacement | Swap? |
|---|---|---|---|---|
| 1 | Hero's Downfall | 3 mana {B}{B}; a fifth creature kill | Return the Favor | **Yes (rank 1)** |
| 2 | Abandon Attachments | Rummage | Venser, Shaper Savant | **Yes (rank 3)** |
| 3 | Black Market Connections | Claimed copy; adds more in Ezio | Tome of Legends | **Lead (rank 2)** |
| 4 | Expedite | One-shot haste, cantrip | Haunted Cloak | No (haste count) |
| 5 | Everflowing Chalice | Colorless 2-drop | Commander's Sphere (+1.6 points for Azula by turn 4 in my simulation, -2.5 points on turn 3; the owner wants it in Ezio) | No |
| 6 | Champion's Helm | Second hexproof | Haunted Cloak | Optional (M3) |
| 7 | Day of Black Sun | Sorcery, never copied; X 2+ kills my 2-drops | none better (Blasphemous Act, Chain Reaction kill my engines) | No |
| 8 | Aether Gale | 5-mana sorcery (owner's card) | | No: owner's card, one-sided, and Electrodominance can cast it in the window |
| 9 | Mind Stone | Colorless | | No (ramp at 10) |
| 10 | Thrill of Possibility | Net 0 outside the window | The Last Agni Kai (EDHREC 46 %, keeps red mana into main phase 2, excess-damage ritual) | No: draw is short |

The Last Agni Kai deserves a fairer reason in the cut log than "Azula takes the damage, twice". The copy may choose another
of my creatures and another target. Against a 1/1 token, Azula adds {R}{R}{R} per fight and keeps all red mana for main
phase 2. It still needs a creature of mine that wins the fight, so it stays out.

**Curve and ratios.**
| Item | Value | Anchor | Verdict |
|---|---|---|---|
| Lands | 36 | spellslinger band 34 to 36 (lean-low rule met: average MV 2.60, 10+ cheap pieces); Karsten formula about 36 | OK |
| Lands + lasting ramp | 46 (lands 78 %) | R8: 46+, lands two thirds | OK (reducers counted) |
| Ramp | 10 + Treasure makers | 12 for a 4-drop commander; window mana makes up the rest | WARN accepted |
| Draw | about 9 effective | 12 to 18 | Short (I2) |
| Spot answers | 14, 10 at MV 2 or less, all instant or flash except Imprisoned | R19: 8, 5 at MV 2 or less | OK |
| Counters | 4 + Reversal | R20 spellslinger 4 to 6 | OK |
| Wipes | 2 | 2 to 3 | OK |
| Win-turn shield | 8 (9 with Return the Favor) | R24: 3+ | OK |
| Tutors to the route | 3 + Godo; route access 13 (14) | R18: 10+ | OK |
| Bad when drawn | 10 | 12 | OK |
| Curve | 35 cards at MV 2 or less; 5 at 5+ (each wins, answers six permanents or refills) | R35 | OK |

## 6. The owner's two decisions

**Return the Favor: IN, for Hero's Downfall.** I agree with the builder's choice of card.
- Why Hero's Downfall goes:
  - It is the fifth instant creature kill: Heartless Act, Terminate, Go for the Throat and Abrade remain.
  - It carries the list's heaviest black pips ({1}{B}{B}).
  - Planeswalkers stay answered by Chaos Warp, Failed Fording, Imprisoned in the Moon, Comet Storm and Electrodominance
    (any target) and Aether Gale, plus Venser with rank 3.
- Why not the alternatives:
  - Turnabout, Snap, Frantic Search and Narset's Reversal are loop pieces.
  - Expedite, Footblade and Boots are the haste line.
  - Day of Black Sun and Aether Gale are the two mass answers.
  - Amphibian Downpour and Imprisoned in the Moon are the two answers to commanders without a zone change.
- Impact:
  - Loop access +2.7 points by turn 6, +3.3 by turn 8.
  - The shield gains a piece that redirects abilities and edicts.
  - Removal goes from 14 to 13 spot answers, still above R19.
  - Answers no longer outnumber closers (the red flag of SKILL 15).

**Black Market Connections (one English copy, claimed from Ezio).**
| | In Azula | In Ezio |
|---|---|---|
| Card each turn | Yes (2 life); works while Azula is dead | Yes |
| Treasure each turn | Window mana ({R}{R} already comes free each combat); any color | Fixing for Ezio's kill, which pays {W}{U}{B}{R}{G} in one turn: a five-color deck's scarcest resource |
| 3/2 changeling | A blocker for 3 life | An Assassin each turn: freerunning enabler, attacker, pumped by Arno and Ramses |
| Its best free substitute | **Tome of Legends** ({2}): a page each time Azula attacks (every turn of her plan); {1},{T} draws, and the {1} can be paid with firebending mana in combat. No life cost, but no card while she is dead and no Treasure | Tome of Legends as well (Ezio attacks every turn), but no Treasure and no Assassin |
| Loss if it goes | Small: the Treasure and the draw while Azula is dead | Larger: fixing, a body each turn and draw |

- Recommendation [J]: the copy adds more in Ezio. Return it, and Azula plays Tome of Legends (EN MKC 246, English binder,
  free), its builder's own fallback.
- Expected cost to Azula: about -0.02 to -0.05 real power.
- The owner asked for Tome of Legends in Ezio. If the lead gives Ezio both cards, Azula's next fallback is Cryogen Relic
  (EN, free: draws on enter and on leave; the sacrifice stuns a tapped attacker so it cannot block).

## 7. Knowledge audit (what each source demands, and whether the list meets it)

| # | Source | What it demands of this deck | Met? |
|---|---|---|---|
| 1 | Skill `SKILL.md`, references, `archetypes.json` (spellslinger + combat modifier) | Lands 34 to 36; ramp 10 to 12; draw 12+ effective (cantrips are fuel); 30+ window cards; payoffs; protection for an attack engine 6 to 8; haste promotion test (3.1); both boards; 2 routes, one noncombat; honest plan file (section 14) | Lands, ramp, window cards, protection, boards, routes: yes. **Draw: no (about 9). Haste test: not written. Plan file: Siege counted twice, Helm and the Reversal as payoffs, Expedite as draw** |
| 2 | Champion addendum, 41 items | See the checklist below | 34 met, 4 thin, 3 n/a |
| 3 | Mana study, notes/02 and notes/13 | Karsten sources: a gold 4-drop needs about 17 per color at 41 lands (about 15 at 36): U 19, B 18, R 17 + Signets meet it. Double pips: {U}{U} cards at 4 want about 23 at 36 lands: blue has 19 + 3 Signets. At most 4 to 6 tapped lands (notes/02 S5): 0 + 2 de facto. Curve densest at 2 and 3: yes | Met. Gap: the "88 % on turn 4" claim ignores colors (75 % with them); red should outnumber black once Return the Favor is in (M2) |
| 4 | Notes 01 to 12 | notes/03 S2: 15 to 20 draw for a commander that draws (the [J] extension covers spenders), never cantrips. notes/04: spot 5 to 8 + wipes 2 to 4; graveyard hate 1; protection 5 to 7. notes/05: one big turn, team-wide finishers. notes/06: haste (one source, 6 cards). notes/07 S4: Treasure spells. notes/10 S7: rituals do not count. notes/11 S15: tutors median 4. notes/12: menace fails against chumps | All met except draw (notes/03) and haste (notes/06), the I2 and I3 findings |
| 5 | Primers `fire-lord-azula*.md` | Instant-speed spellslinger; mana storage (Ozai, Electro, Horizon Stone, The Last Agni Kai); copied draw; Swat, Boots, counters; three-card loops; "take tutors and cheap instant answers back, do not trade them for more draw" | Mostly met. Gaps: no rituals or flash enablers owned. Three 1-mana instants left (Fatal Push, Firebending Lesson, Undying Malice); the cheap-answer share still meets R19. The Last Agni Kai's rejection reason is weak (section 5) |
| 6 | Owner lessons L1 to L10, play reviews, gate review (f) | Checklist below. Play review: Siege Temur "almost always right" (misplay 7); "9 sorceries never copied" (now 3 + Gleam); "a second each-opponent payoff" (Thermo and the loops cover it). Gate review (f): declare every leaned-on function, name dead clauses, both boards, bad-when-drawn | Met, except draw counted by tag and the Siege double count |
| 7 | Final review of 2026-11-08; iteration-1 lists | F1 (Shred Memory), F2 (Chalice), F3 (Expedite) all applied; N3 (Day of Black Sun tokens) not applied; N6 politics now written. Iteration-1 cards he won with: Torrential Gearhulk, Frostcliff Siege, Mystical Teachings are all IN. round4-step27 also ran Black Market Connections, The Last Agni Kai, Fatal Push and Undying Malice | Met; N3 open |
| 8 | Owner's card review of 2026-11-14 | A verdict for every in-color card. Multiple-copies rule: no strong staple left idle where it beats a list card | Verdicts: all present, sound except Return the Favor (now IN by his decision) and the reasons for The Stasis Coffin and Evie Frye. Idle copies that could play here: Fatal Push (3 free), Lightning Strike (2 free), the extra Abandon Attachments, Octopus Form, Mystical Teachings, Dualcaster and Brainstorm (singleton: only one copy per deck). Only Venser (one copy, free) clearly beats a list card |

**Champion addendum, item by item** (A = applied, T = thin, N = not applicable).
1 A one plan + backup · 2 A every card alone · 3 A redundancy (6 loop pieces, 4 finishers) · 4 T multi-role count not
reported this time · 5 A about 5 blank without Azula · 6 A 36 lands · 7 A colored sources (T: the odds claim ignores
colors) · 8 A 46 · 9 A Sol Ring, Arcane, Signets (no Talismans owned) · 10 A 0 always tapped · 11 A window mana 11 · 12 A
curve · 13 A recast with haste written · 14 A · 15 A engines · 16 N no Rhystic, Remora or Sentinel owned · 17 A cheap
early draw · 18 A 3 tutors + Godo, access 13 · 19 A 14 answers, 10 at MV 2 or less · 20 A 4 counters + Reversal · 21 A Day
(X chosen), Gale (one-sided) · 22 A Shred Memory (T: shared with its tutor use) · 23 A layers · 24 A shield 8 · 25 A
types · 26 A 3-card routes · 27 A 3 routes · 28 A Godo route without Azula · 29 A · 30 A · 31 A politics written · 32 A 6
rebuild pieces · 33 A 88 % with the free mulligan · 34 N 1 of 3, none owned · 35 A · 36 A (T: Venser and The Last Agni
Kai under-argued) · 37 A script PASS · 38 A 20 hands, 5 goldfish, 3 disrupted · 39 A gauntlet · 40 A cut log · 41 A
proven cards in. Totals: 34 A, 4 T (items 4, 7, 22, 36), 3 N (16, 34, and 9 partly).

## 8. Lessons checklist (owner L1 to L10)

| # | Lesson | Status | Cards |
|---|---|---|---|
| L1 | One consistent plan | Covered | Azula window plan; three routes reuse the window pieces |
| L2 | Ratios follow the plan: Azula needs the most draw | **Thin** | About 9 effective draw (I2); engines Archmage, Black Market Connections or Tome, Siege (Jeskai), Narset |
| L3 | Attackers: connect, survive, haste, defend while tapped | Covered, haste thin | Boots, Footblade, Expedite, Siege; Propaganda, Thermo, Nightscape, Gearhulk at flash; protection 10 |
| L4 | Dependence sets protection | Covered | Attack engine, 10 pieces |
| L5 | Value depends on the curve | Covered | Chalice cast turn 2 for 1, not late; Waterbending Lesson cut as a sorcery |
| L6 | Proven role-players | Covered | Horizon Stone, Propaganda IN; Gearhulk, Siege, Teachings IN |
| L7 | No dead clauses or mini-combos | Covered | Dead clauses named (Failed Fording's Desert line, the changeling types); every loop piece works alone |
| L8 | Two reference boards | Covered | Section 1 |
| L9 | Salt is not the measure | Covered | Not measured in this step |
| L10 | The guide says how to use each card | Covered | Build notes section 2 |

## 9. Mana and flow numbers (recomputed)

- Keepable hand: 88 % with the free mulligan (builder's 40,000-hand run; probability C gives 87 to 91 % at 36 lands).
- Azula castable WITH colors: 34 % on turn 3, 75 % on turn 4, 84 % on turn 5. My Monte Carlo (40,000 games): one land a
  turn, 2- and 3-mana rocks and Nightscape modeled, Exotic Orchard as any color, filter lands as duals.
- Loop pieces, or tutors for them, seen by turn 6 / turn 8: 28 % / 35 % today, 31 % / 38 % with Return the Favor. Both
  pieces in hand with no tutor: 5 % / 7 % today, 8 % / 10 % with it.
- Haste by turn 4: 30 to 38 % (57 % with the tutors). A draw engine by turn 7: 46 % (4 engines in 14 cards).
- Card flow: a window turn spends 2 to 3 cards and gains 2 to 4 with Azula attacking; with Azula dead the hand empties by
  turn 6 to 7 unless an engine is out. That is why one engine that works without her matters (Black Market Connections) and
  why Tome of Legends is the weaker fallback.

## 10. Multiplayer check

- **How it beats three opponents.** Comet Storm kicked twice and copied (each opponent takes 2X); Thermo-Alchemist pings
  each opponent in a loop; Godo + Helm's unlimited combats; Return the Favor forks a Comet Storm twice more. Every route
  hits the whole table in one turn.
- **The pod's interaction.**
  - Instant removal on Azula after she attacks is the main risk: Swat, Redirect Lightning, the Reversal, Return the Favor
    and four counters, with Boots and Champion's Helm up first.
  - A sweeper: the counters, or Snap or Failed Fording on Azula in response.
  - Graveyard hate blanks only Gearhulk's recasts and Teachings' flashback.
  - Attack taxes: pay or attack another player.
  - "One spell a turn" or "only at sorcery speed" locks stop the plan cold. Answers: Chaos Warp, Failed Fording, Aether
    Gale, Abrade (artifacts), Venser (rank 3).
- **Single card that ends the plan.** Instant removal on Azula when the window opens.
- **The second route.** Godo + Helm of the Host: Godo costs 6, then the Helm's equip costs 5 a turn later, and Godo must
  survive a turn cycle. Artifact removal on the Helm ends it. A third fallback is an uncopied Comet Storm with banked mana
  (Horizon Stone, Ozai, Electro).

## 11. Verdict: FIX

**Ranked change list** (cards out go back to the English binder; 100 cards after the change; both scripts PASS on a scratch
copy with ranks 1 to 4 applied).

| Rank | Out | In (language, copy, source) | Reason | Expected impact |
|---|---|---|---|---|
| 1 | Hero's Downfall (EN THS 90) | **Return the Favor** (EN, SOA 47, English binder, free) | Owner's decision; section 6 | Loop access +3 points; a ninth shield piece that redirects abilities and edicts; copies Comet Storm, firebending, Godo and Helm triggers; +0.05 to +0.1 |
| 2 | Black Market Connections (EN ACR 87, back to **Ezio**) | **Tome of Legends** (EN, MKC 246, English binder, free) | The copy adds more in Ezio: fixing for the five-color kill and an Assassin each turn (section 6) | Azula -0.02 to -0.05; Ezio gains more. **Lead's decision**; if it stays in Azula, skip this row |
| 3 | Abandon Attachments (EN TLA 205) | **Venser, Shaper Savant** (EN, 2X2 66, English binder, free) | The weakest slot (a rummage) for the highest-floor free card: flash answer to any spell, creature spells and commanders included; two bounces in the window | +0.03 to +0.05; draw tag 11 (write the WARN reason: Abandon was half a draw piece) |
| 4 | 1 Swamp (EN) | 1 Mountain (EN, English binder, 32 free) | Red pips outnumber black after rank 1 (M2) | Small; Azula's own odds unchanged |
| 5 | none | none | Plan file and notes: honest draw count (about 9) and its reason (I2); haste promotion test written and Siege counted once (I3); payoffs without Helm and the Reversal; Propaganda as defense; colour-aware Azula odds; Day of Black Sun token line; R1 confirmed; the Archmage note on the Turnabout loop; The Stasis Coffin and Evie Frye reasons; Ty Lee and Cunning Maneuver in the cut log | Honesty of the gate, no power change |
| opt. | Champion's Helm (EN) | Haunted Cloak (EN, CMM 389, English binder) | Only if the lead wants the haste line closed with a card (M3) | Neutral to +0.02 |

**Real power.** As built 7.5 to 7.9 (builder 7.6 to 8.1; the project's estimates run high). With ranks 1 to 4, 7.6 to 8.0.
Confidence medium-low; no games played.

**For the owner.**
1. Black Market Connections: Azula or Ezio. My recommendation is Ezio, with Tome of Legends in Azula, which means Tome is
   not in Ezio as he asked.
2. Frostcliff Siege's mode: he wants the constant draw (Jeskai). The play review says Temur is "almost always right" for
   haste. Both are fine: the guide should say Temur when Azula has no Boots or was just recast, Jeskai otherwise.
3. Swan Song, Negate and Thirst for Knowledge are Spanish-only copies that Kilo may claim later (M6).
