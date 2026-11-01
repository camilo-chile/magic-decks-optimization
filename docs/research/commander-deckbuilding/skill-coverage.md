# Coverage of the commander-deckbuilding skill (2026-10-31, revision 2 on 2026-11-01)

Skill: `.claude/skills/commander-deckbuilding/` (`SKILL.md`, `archetypes.json` schema 3, `references/*.md`). Revision 2 is
described in section 5; sections 1, 2 and 4 are brought up to date with it. This file maps (1) the
owner's lessons L1 to L10 (`docs/research/phase2-owner-lessons-20261031.md`) to the general principle that covers each,
and (2) each research note's key claims to where they landed or why they were left out. It is for a later auditor.

Blindness rule applied: the skill names none of the owner's commanders, none of the specific cards in the lessons, and no
complaint phrased about his decks. Every lesson enters as a general principle. The three commander studies in
`commanders/` were used only to check that the method yields a sensible profile (section 3), not as content.

Section references: "S-n" = SKILL.md step n; "P-n" = SKILL.md principle n; file names are under `references/`.

## 1. Owner lessons

| Lesson | General principle in the skill | Where | Coverage |
|---|---|---|---|
| L1 One consistent strategy, never many plans with 1 to 3 support cards each | One plan plus a backup that reuses its pieces; a backup needing its own package is a second plan; packages of 1 to 3 cards of any mechanic are a red flag to search for in Oracle text; a function is dropped only with its cards; routes list closers only (engine pieces may be shared); the fit check (mins counted once must fit in 99 minus lands) now applies to every profile, not only hybrids; a secondary that is only a modifier is sized as a support line | P-1; S-2; S-3.5; S-7; S-14 and `plan-file.md`; S-15 red flags; S-16 item 3; `archetypes.json` meta.hybrid; archetypes.md reanimator note and hybrids | Full |
| L2 Ratios follow the strategy, not a template | Size each function by the commander's fuel and fuel rate; card-flow budget and, new, an entries-per-turn budget (repeatable permanents versus one-shots); landfall ramp 18 to 20 (at or above the top of the Bracket 3 range), land entries 12 to 16 with extra land drops 5 to 7 and land recursion 3 to 5; spellslinger density 30 to 36 and draw 12 to 18; attackers need haste, team evasion, protection and defense while tapped; template numbers are floors for safety functions only; profile numbers outside the gate's generic warnings are kept with a reason; gate and support tiers | P-2; S-3.1 to S-3.5; S-4; S-14; `archetypes.json`; archetypes.md (with the EDHREC behaviour table) | Full in principle; many plan counts are now sourced from notes/13 (section 5), the rest stay [J] because no source measures them |
| L3 Attackers: connect, survive, haste, defend while tapped | A dedicated step for decks that win by attacking: haste with a promotion test (attack-only engine that is cheap to recast, or needed on 3+ of turns 4 to 8), evasion that beats the two reference boards (menace and power-restricted evasion fail against chump walls), team-wide evasion as a role-player, protection layered against removal and wipes, defense while tapped, a toughness check with a pass line (at most a third of attackers at toughness 2 or less), and a fill order that puts the attack lines before generic safety | S-3.1; S-7; S-8; S-10 item 4; win-routes.md sections 2 and 4; `combat_attackers` profile (both reference boards now in the JSON); archetypes.md typal note on type-wide effects | Full in principle; team evasion and defense while tapped stay [owner signal] (community averages run almost none, notes/13 E1) |
| L4 Commander dependence differs | Classify the commander as engine, attack engine, enabler or value; COMMANDER protection follows the class (5 to 7, 6 to 10, 3 to 4, 2 to 3) and is a separate count from WIPE INSURANCE (a function of board plans, 2 to 4); total protection is their sum, a card counting in both only if it does both jobs; what the table holds (computed) sizes both | S-1 table; S-6; `archetypes.json` meta.commander_dependence and base.protection; multiplayer-politics section 6 | Full; counts [J] anchored on the one sourced 5 to 7 and now on the table-holds arithmetic |
| L5 A card's value depends on this deck's curve and mechanics | Judge every card at the turn this deck will cast it; timed ramp; mana that scales with what was paid or a growing count is a turn 2 to 3 card unless the deck grows it; late ramp must become cards or a sink; window COSTS are budgeted like window mana | P-4; S-4 ramp timing and window costs; S-9; mana-and-ramp.md sections 2 and 6; evaluation-and-cuts.md section 1 | Full |
| L6 Cards that won games were cut by a score-driven builder | Role-player definition; proven role-players are strong priors, cut only with a written reason the owner reviews; never cut by score or inclusion; upgrade mode (S-0b) starts from the owner's list and play notes; bridge cards; a conditional piece reported as a game-winner keeps its slot; window-mana cards judged by the problem they solve; attack taxes as a defense-while-tapped tool | S-0b; S-3.4; S-4 temporary mana; S-5; S-9; S-11 never cut; S-13; evaluation-and-cuts.md section 2; role-players-and-upgrades.md; win-routes.md section 4 | Partial by design: the skill cannot know WHICH cards are proven; it asks the owner or caller to supply them, and S-0b gives the procedure |
| L7 Dead clauses and mini-combos rot in hand | Every card must do something alone; name every dead clause; a combo is allowed only if organic; bad-when-drawn marking with a threshold that does not fire on every list (ramp counts as bad late only above the ramp target; only early and late values are listed); cards two steps from the plan become dead draws | P-3; S-7 organic combos; S-9; S-15 red flags; evaluation-and-cuts.md section 3; win-routes.md section 1 | Full |
| L8 The pod's two reference boards | Test every list against eight small sacrificeable chump blockers and two creatures bigger than yours; every profile carries both as early gate functions; a sacrificeable chump board also removes low-toughness attackers; a single 1-damage ping counts half | S-7; S-15 item 6; S-16 item 4; win-routes.md section 2; `archetypes.json` meta.required_functions | Full |
| L9 Commander Salt is not the measure | Salt measures ideal draws; tie-break only among lists that pass the gate and the review | P-6; S-13; tools.md section 2 | Full |
| L10 The guide says how to USE each card | Output 4: one line per card on when to cast it, what to hold it for, what it pairs with and when it is a bad draw, never the rules text; the pattern is given | S-0 output 4 | Partial: the skill gives the template and a pattern but does not teach guide writing (the dashboard playbook format is outside this skill) |

## 2. Research notes: key claims and where they landed

Legend: **In** = in the skill with its source; **Adapted** = used with a stated choice or as [J]; **Out** = left out, with
the reason.

### notes/01 foundations
| Claim | Status | Where / why |
|---|---|---|
| 8x8 method (35 lands, eight themes of eight); "training wheels, not scripture" | Adapted | probability.md A: eight is a theme size (66 % by turn 5), not a guarantee |
| 36 to 38 lands beginner; 10 to 12 draw beginner | In | card-flow.md 1; mana-and-ramp.md 1 |
| 25 to 35 creatures; 35 to 38 lands; curve peaks 3 to 4 vs bulk at 2 to 3 (conflict) | In | archetypes.md generic base; mana-and-ramp.md 5 (lean 2 to 3) |
| Commander as centre; costly commanders need card flow; backups for the engine | In | S-1; S-2 |
| Bracket facts (Draftsim) | In, superseded by the project snapshot | S-12; multiplayer-politics-and-threat.md 5 |
| Pet cards and mini-quests (conflict of three positions) | Adapted | evaluation-and-cuts.md 3: pet cards pass the same tests; owner rule on mini-combos chosen |
| Card value depends on game stage (Kosin) | In | P-4; mana-and-ramp.md 2 |
| Sol Ring in 99 % of decks (estimate) | Out | an estimate, not useful to building decisions |

### notes/02 mana
| Claim | Status | Where / why |
|---|---|---|
| Land bands by archetype (ScrollVault simulation), Playgroup bands, Karsten-attributed formula | In; the formula was read in the primary in revision 2 and corrected: it is a 60-card tournament regression scaled to 99 cards, not Commander data | mana-and-ramp.md 1; probability.md D |
| Sol Ring win-rate edge shrinks in 4-player pods; only Sol Ring survives correction | In | mana-and-ramp.md 2 |
| Arcane Signet editorial rank vs measurement | Adapted | mana-and-ramp.md 2: editorial ranks are opinion |
| Colored-source targets (19, 30) and their failure to reproduce; computed table | In; conflict resolved in revision 2 (Karsten's definition is conditional on land drops) and his 99-card table added | probability.md E; mana-and-ramp.md 4 |
| Tapped lands 4 to 6 tolerated (uncited); utility lands last | In | mana-and-ramp.md 4 |
| MDFC land weights | Out | project rule: no reversible cards |
| Eleven ramp forms; ramp that does more | In | mana-and-ramp.md 2 |
| Mana retention mechanics (drain per step; colorless vs color retention) | Adapted | mana-and-ramp.md 6 as a general window-mana rule; specific cards left out (blindness rule and card text unverified) |
| Opening-hand peak at about 42 lands is a window property, not a target | Out | not needed once the computed tables are given |

### notes/03 card flow
| Claim | Status | Where / why |
|---|---|---|
| Draw baseline 10; 15 to 20 for draw-built commanders; S5's opposite (conflict 1) | Adapted | card-flow.md 1: spend vs draw rule chosen |
| Definitions: cantrips are not card advantage; scry is not draw; tutors are not card advantage | In | card-flow.md 2; S-5 |
| Conditional and combat-tied draw category | In | S-5; card-flow.md 2 |
| Opponent-triggered draw stronger in multiplayer | In | card-flow.md 2 |
| Tutors replace redundancy; two on a budget; tutor for the finisher | In | card-flow.md 4 |
| Checklist 37/13/10/6/3/2/2/1/1 | In | mana-and-ramp.md 1; interaction-and-protection.md 1 |
| Ramp odds reproduce; land odds do not (conflict 3) | In | probability.md D |
| Computed table of one-of-k odds | In, recomputed for 7 + N | probability.md A; S-3.3 |
| Synergy over staples; multi-job cards; one plan; group by function | In | S-9; S-10; evaluation-and-cuts.md 1 |
| Diagnosis signs (one-land hands, empty hand by turn 6) | In | evaluation-and-cuts.md 6 |
| Redundancy snippet heuristics (2 to 4, 5 to 8, 8 to 12) | In as unverified | card-flow.md 6 |

### notes/04 interaction and protection
| Claim | Status | Where / why |
|---|---|---|
| Removal 8 to 10 floor; 8 to 12 incl. wipes; 3 to 5 must-answer spot | In | interaction-and-protection.md 1; S-6 |
| One-for-one trades lose in pods; two-for-one preferred; spread across types | In | interaction-and-protection.md 1 |
| Wipe counts 1 to 5 (conflict) | Adapted | 2 base; 0 to 2 creature decks; 3 to 5 control |
| One-sided, synergy, instant-speed wipes; bounce wipes' cost | In | interaction-and-protection.md 2 |
| Protection 5 to 7 (single source); layers by wipe type; shroud vs hexproof | In | interaction-and-protection.md 3 table; S-6 |
| Recursion 2 to 3; exile prevents recursion | In | card-flow.md 5 |
| Edicts weak against wide boards; target sacrifice outlets | In | win-routes.md 2 |
| Neutralizing commanders instead of destroying | In | interaction-and-protection.md 1 |
| Equipment popularity rank and the designer's remark on Greaves | Out | trivia, not a building rule |

### notes/05 multiplayer
| Claim | Status | Where / why |
|---|---|---|
| Threat assessment indicators and removal order | In | multiplayer-politics-and-threat.md 1; interaction-and-protection.md 1 |
| Politics conflicts (S2 vs S3: visibility, whom to pressure) | In with conflicts | multiplayer-politics-and-threat.md 2; win-routes.md 5 |
| Attack taxes push attacks elsewhere; payers still attack; punishment preferred by one source | In | win-routes.md 4 |
| Four finishing types; 2 to 3 routes; overrun example; one main plan plus fallback | In | win-routes.md 1; S-7 |
| Bracket 3 six turns; one big turn from earlier resources | In | multiplayer-politics-and-threat.md 3 |
| Commit when ahead; 60 % attempt now | In | win-routes.md 1 |
| Playgroup win shares (unverified) | In as unverified | win-routes.md 1 |
| Commander damage 18 (S2) | Out | unchecked; the skill uses 21 marked as a rules fact not re-checked in the notes |

### notes/06 combat archetypes
| Claim | Status | Where / why |
|---|---|---|
| Creature counts by archetype (aggro 30+, typal 30+, voltron 20 to 30, control conflict, combo 15 to 30, spellslinger 25 or fewer) | In | `archetypes.json` creature_count; archetypes.md |
| Evasion ranking (no method); menace, skulk, fear, daunt, stalking behaviour | In | win-routes.md 2 and 3 |
| Team-wide effects scale with the attack | In | S-8; win-routes.md 3 |
| Haste: removal before attack; one deck with six haste cards | In | S-8; win-routes.md 4 |
| Protection first for commander-plan decks; two-layer stack | In | voltron and combat profiles; win-routes.md 4 |
| Wipe recovery principles | In | interaction-and-protection.md 2, 4 |
| Uril aura list counts; typal Marisi counts; theme cap 75 % (2017) | In | archetypes.md voltron and typal |
| Failure modes list (self-hosing wraths, attack targets by die roll, colorless lands in 4 to 5 colors) | In | archetypes.md; mana-and-ramp.md 4; win-routes.md 4 |
| Owner's game notes (OG) | Out as content | blindness rule; covered by general principles (section 1) |

### notes/07 engine archetypes
| Claim | Status | Where / why |
|---|---|---|
| Ramp definitions differ (S1 lands only vs S2 rocks too) | In | mana-and-ramp.md 2 |
| 8 to 10 ramp on 40 lands; ramp never replaces lands; past five mana not ramp | In | mana-and-ramp.md 2 |
| Extra land drops, several lands per spell, land sacrifice that nets a land; count extra drops on their own line | In | mana-and-ramp.md 3; landfall profile |
| Counters roles (sources, doublers, proliferate, evasion) and traps | In | counters profile |
| Spellslinger needs (engine, payoffs, growing board, win condition); treasure as mana | In | spellslinger profile |
| Reanimator: enablers 3 MV or less; 8 to 12 targets; several revival spells; threats outside the graveyard | In | reanimator profile |
| Blink and aristocrats (unverified summaries) | In, marked unverified | profiles |
| Artifacts: not searched | Gap stated | artifacts profile marked weakly supported |

### notes/08 evaluation, testing, tools
| Claim | Status | Where / why |
|---|---|---|
| Judge by fit, role, replacement, mana, then playtest | In | evaluation-and-cuts.md 1 |
| Dead cards from 6 to 7 cards at 7+ MV | In | mana-and-ramp.md 5; big_mana profile |
| London mulligan details; free first mulligan in pods | In (free mulligan) | probability.md intro; full procedure Out (not a building rule) |
| Goldfishing limits; ten games cannot rank close lists | In | evaluation-and-cuts.md 5 |
| cEDH: compact combos, resilience, tutor reach | Adapted | win-routes.md 1 combos (general principles only, labelled cEDH) |
| Prior-art tools (Spellbook, XMage, Forge, MCP servers) | In | tools.md 4, 5 |
| 43-land baseline column; EDHREC-attributed 36 average | In as secondary | mana-and-ramp.md 1 |

### notes/09 EDHREC foundations
| Claim | Status | Where / why |
|---|---|---|
| Command Zone 2025 template: categories only, no numbers; "starting point" | In | tools.md 1; P-2 |
| 2019 land study (29 lands, too low); Burgess rule | In | mana-and-ramp.md 1 |
| Atraxa averages by bracket (lands 34 to 37; cheap spells rise with power) | In | mana-and-ramp.md 1, 5 |
| EDHREC rules of thumb (ramp 10, removal 10 / 5 to 7 / 15+, card advantage 12+, wipes 2, graveyard hate 1) | In | tools.md 1; profiles |
| Synergy, lift, inclusion definitions; averages describe behaviour, not quality; precon effect | In | S-13; tools.md 1 |
| JSON endpoints and fields | In | tools.md 1 |
| Bracket history (2025 launch, October 2025 update, February 2026 changes) | In via the project snapshot | S-12 |
| Organic vs inorganic combos | In | S-7; win-routes.md 1 |

### notes/10 EDHREC archetypes
| Claim | Status | Where / why |
|---|---|---|
| Sample list type counts for nine archetypes; landfall highest at 39 lands | In | profiles land_why |
| Landfall top cards and traps (payoff competition, entry-only value) | In as traps | landfall profile (card names kept out except as generic patterns) |
| Counters color ranking; one-source trap | In | counters profile |
| Spellslinger: one main plan with one or two side packages; read payoff types; stalled board | In | spellslinger profile |
| Tokens win routes; board-dependent payoffs; snippet ratio conflict | In | tokens profile |
| Voltron: protection as important as growth; chump blockers absorb hits | In | voltron profile |
| Pillowfort roles and weaknesses | In | pillowfort profile |
| Reanimator table-social claims; dead draws fix | In | reanimator profile |
| Blink balance and hosers | In | blink profile |
| Aristocrats three legs; free vs costed outlets | In | aristocrats profile |
| Assassins theme page commander and card lists | Out | blindness rule (owner's commander) and no building guidance in it |

### notes/11 community
| Claim | Status | Where / why |
|---|---|---|
| Workflow: plan, functional slots, staples, deck-specific, cut; final omission check | In | S-10; tools.md 1 |
| Bracket 3 medians from 1,285 lists | In | everywhere as the generic base |
| Simulation land bands by archetype | In | mana-and-ramp.md 1; probability.md D |
| Layering: cards two steps away become dead | In | P-3; evaluation-and-cuts.md 3 |
| Engine needs about ten synergy cards or many tutors (anecdote) | In as anecdote | card-flow.md 6 |
| Voltron: 8 to 12 rocks; equipment safer; protection before casting; reserve tutors for protection; finishers that hit several players | In | voltron profile |
| Mulligan judgement criteria | Out | play skill, not construction |
| Politics: never break deals; griefer cards draw battle lines | In | multiplayer-politics-and-threat.md 2 |
| Closing: name routes, add damage aloud, do not draw when lethal | In | multiplayer-politics-and-threat.md 3 |
| Thunderbowl testing; goldfish poll | In | evaluation-and-cuts.md 5 |

### notes/12 combat in multiplayer
| Claim | Status | Where / why |
|---|---|---|
| Defense toolkit: deathtouch, reach or flying blockers, punishers, taxes, density, vigilance | In | S-8; win-routes.md 4 table |
| Menace weak against wide boards; color-based evasion depends on the table | In | S-7; win-routes.md 2, 3 |
| Forced blocks, lures, goad, politics against big blockers | In | win-routes.md 2 |
| 120 total life; team-wide vs single-target closing | In | P-5; S-7; win-routes.md 1 |
| Each-player effects and their symmetric risk | In | win-routes.md 2 (non-combat routes); symmetric risk noted in interaction-and-protection.md 2 |
| Aggro ramp 10, curve 2.8 or lower, two-drop gaps (opinion) | In as opinion | combat profile; mana-and-ramp.md 5 |
| Haste snippets (team vs single-target) | In as unverified | win-routes.md 4 |
| Aggro mistakes in pods | In | win-routes.md 4 |
| Forum win ratios (25 %, 80 %) | Out | anecdotes without method |

### notes/13 ratio gaps (revision 2)
| Claim | Status | Where / why |
|---|---|---|
| K1 curve and land simulation (42 lands + Sol Ring, cut per extra rocks and cantrips, rocks pay only with a 4+ MV commander) | In | mana-and-ramp.md 1 and 2; SKILL S-4 |
| K2 regression 31.42 + 3.13 x MV - 0.28 x cheap, fitted on 95,143 sixty-card decks (earlier notes call them Commander decks: wrong) | In, corrected | mana-and-ramp.md 1; SKILL S-4; `meta.lean_low_land_rule` |
| K3 colored-source table for 99 cards, gold +1, partial sources | In | mana-and-ramp.md 4; SKILL S-4 colors |
| CZ-new template (38 / 12 / 10 or 12 / 12 / 6 / about 30; curve 9-18-14-10-4-4) and CZ-old | In | tools.md 1; archetypes.md generic base; SKILL P-2, S-4 |
| E1 EDHREC Bracket 3 averages by function for seven archetypes | In as community behaviour, never as target | archetypes.md table; profile `why` strings; SKILL S-13 |
| PG opening-hand data and mulligan frequencies; computed odds of 2 to 4 lands and of a keepable hand | In | probability.md C |
| Joint colors (computed here, Monte Carlo) | New | probability.md E2; SKILL S-4 |
| What the table holds (computed from the Bracket 3 medians) | New | multiplayer-politics-and-threat.md 6; SKILL S-6 |
| W1 to W3 written guides (voltron, spellslinger) | In as opinion | profile `why` strings |
| CZ-659 audio, Reddit threads, Card Kingdom | Out | blocked or not transcribed (note 13 gaps) |

## 3. Sanity check of the method on the three commander studies (not copied into the skill)
- A landfall commander with an end-step land animation: the method reads "land entries" as fuel, applies the landfall
  profile (38 to 40 lands, ramp 12 to 15, extra land drops 4 to 6, land recursion 2 to 4), flags the rules question on
  added card types (mana abilities, entry triggers), and sets dependence to enabler. That matches the study's sourced
  plans and its open rules question, and it would flag a list with generic ramp counts and few extra land drops.
- A three-color commander that copies spells cast while it attacks and makes combat-only mana: the method detects two
  archetypes and applies the spellslinger + combat hybrid (instants and flash only, draw 12 to 15, haste after recast,
  evasion, protection, defense while tapped, window-mana handling). The study notes that no read source covers defense
  while tapped or retention cards for it; the skill covers both by principle.
- A two-mana typal attacker with menace and a five-color kill on combat damage at 10 life: the method reads engine
  dependence, the combat profile with typal hybrid, flags menace as failing against the wide reference board, flags the
  single-player kill as a backup route, and requires haste, team evasion and defense while tapped. That matches the
  study's open questions (haste and wide boards undiscussed in its sources).

## 4. Known gaps and tensions (honest list)
1. **No measured function profile exists for any archetype.** Most plan-function counts in `archetypes.json` are [J]
   from the gate's odds classes. They need play evidence.
2. **No source counts** team evasion, defense while tapped (beyond about 4 vigilance creatures), combat draw, wipe
   insurance, mana sinks, counter payoffs, or protection beyond one 2021 source (5 to 7) and a voltron guide (8 to 10). Haste,
   land recursion, landfall payoffs, spellslinger draw and the counters roles now have community averages (notes/13 E1).
3. **Artifacts, enchantments and group hug** have no composition source; their profiles are marked weakly supported or
   unsupported.
4. **Karsten's primary articles** were read in revision 2 (notes/13 K1 to K3): resolved. What stays open: his models are
   goldfish, 7 turns, no interaction, and his land regression is not Commander data.
5. **The Command Zone's 2025 template numbers** were reached in revision 2 through two written summaries (notes/13 CZ-new);
   the episodes themselves were not heard and episode 659's per-strategy exceptions are unknown.
6. **Reddit and most forums** were not read (blocked); community consensus beyond the read articles is absent.
7. **No outcome data**: nothing read ties any deck-level ratio to win rates in pods (only opener-level land data, notes/13
   PG).
8. **Gate tension**: `scripts/plan_density.py` warns with generic numbers (lands 36 to 38, wipes 2, protection 3) that
   some profiles exceed on purpose (landfall 38 to 40 lands; tokens 0 to 1 wipes). The skill tells builders to keep the
   profile and write the reason; a later change could make the script read `archetypes.json` (not done; the script was
   not changed). Second tension, resolved inside the skill: the gate fails any declared function under 10 (early) or 6
   (late), while several sourced or judged needs are smaller (haste, defense while tapped, doublers, extra land drops).
   The skill splits functions into gate and support tiers (`archetypes.json` meta.tier); support lines are checked by the
   builder and reviewer, not by the script. A later script change could read the tier and check support lines too.
   Some payoff and outlet minimums were raised to 10 to meet the gate's early class (for example sacrifice outlets 10,
   inside the 7 to 12 range one unverified source gives); these are [J].
9. **Commander damage threshold** (21) is a rules fact not re-checked in the notes.
10. **L6 and L10 are partial** by nature (section 1).
11. **Rule 103.8c or 800.7** (no first-draw skip in multiplayer, basis of 7 + N): Karsten cites 800.7, earlier notes
    103.8c; neither was re-read in the current rules.

## 5. Revision 2 (2026-11-01)

Inputs: the adversarial audit of 2026-10-31 (accuracy, lesson coverage, blindness, usability, gaps, JSON), the new sourced
numbers of notes/13, and the feedback of a blind reviewer who used the skill on five decks. Method: the JSON is rebuilt by a
generator from the old file plus explicit overrides; the function tables of archetypes.md are generated from the JSON
between `<!-- BEGIN table:slug -->` markers, so the twins cannot drift (since revision 3 the table generator is
`scripts/gen_archetype_tables.py`, with `--check` and a test; the JSON build script of this revision stayed in the session
scratchpad and is not needed again: edit `archetypes.json` directly).

### What changed
- `archetypes.json` schema 3: top-level `meta` (shared rules, weights, commander-dependence classes, hybrid rule) and
  `archetypes.<slug>`; each profile has `base` (ONLY the five tag floors, each with min, target, why, source) and
  `functions` (every plan function with min, target, tier, needed_by, why, source). `base.removal` = spot answers;
  `base.protection` = commander protection by class; wipe insurance is a function. Both reference boards are gate-early
  functions in all 16 profiles. Sixteenth archetype `alternate_kill` added. Optional keys: `if_commander_is_payoff`,
  `if_commander_is_source`, `if_secondary_modifier`, `counts_inside`, `default_class`.
- `SKILL.md` (480 lines): outputs gain rules points to verify and the guide-line template; step 1 tax arithmetic and
  rules families; 3.1 source functions, support = repeatable, haste promotion test; 3.2 entries-per-turn budget and a row
  for threshold kills; 3.4 weights; 3.5 fit check for every profile; step 4 lands, ramp, colors and window costs rewritten
  on notes/13; step 5 draw floor stated once; step 6 removal defined once, wipes corrected, commander protection and wipe
  insurance separated, answers to opponents' commanders, what the table holds; step 7 closers only, boards; step 8
  toughness pass line; step 9 bad-when-drawn threshold; step 10 attack-first fill order; step 12 live Game Changer
  search and the combo wording; step 14 moved to the new `references/plan-file.md` with the path `decks/phase2/`; step 15
  red-flag definition of answers versus closers; step 16 reviewer additions.
- References: `mana-and-ramp.md` (Karsten K1 to K3, CZ-new, entries per turn, basic-fetching ramp, curve by role, window
  costs), `probability.md` (opening hands and mulligans, joint colors E2, repeatable-mins note), `archetypes.md` (generated
  tables, EDHREC behaviour table, leak rewrites, hybrids), `card-flow.md`, `interaction-and-protection.md`, `win-routes.md`,
  `multiplayer-politics-and-threat.md` (section 6), `evaluation-and-cuts.md`, `tools.md` (CZ-new, live Game Changer search),
  new `plan-file.md`. `role-players-and-upgrades.md` and the lead's sections of SKILL.md were left as written.

### Audit fixes applied (numbers are the audit's prioritized list)
Applied: 4 (path, closers only), 5 (reference boards in every profile), 6 (landfall ramp, entries per turn), 7 ([J] on the
spending extension), 8 (wipes), 9 (protection split, removal and draw defined once), 10 (support mins assume repeatable),
11 (already in), 12 (all mislabels A1 to A18 fixed or relabelled), 13 (play-report citations replaced, soft leaks rewritten
as families), 14 (land floors with the lean-low rule), 15 (the JSON half), 16 to 23 (table holds, tax arithmetic, answers to
commanders, MV by role, pip-by-turn procedure, basic-fetching ramp, keepable hands, diversity, fit check, fill order,
guide template, sacrificeable chump board). From section 4: haste promotion test, outputs order, multi-role counting
(stated as primary-tag counting), the reviewer additions for G1, G3 and G7, route cards as closers.
Skipped: 1, 2, 3 and 24 and the script half of 15 (all change `scripts/plan_density.py`, which another person edits: force
reference boards early, tutor tag check, odds with and without the commander, count only early and late `bad_when_drawn`,
`support` block, read the JSON through an `archetype` field, secondary tags in base counts, removal = spot answers). The
SKILL text already states the intended behaviour. Also skipped: the audit's split of `land_entries` into two functions
(`extra_land_drops` is now defined as the repeatable-engine line, 5 to 7, and the entries budget does the rest); the
tutor-pacing gap (no source, left as it was).

### [J] counts that became sourced (notes/13 section 6 plus the original source)
| Count | Old [J] | Now | Source |
|---|---|---|---|
| landfall land_entries | 10 to 14 | 12 to 16 | E1 lands onto the battlefield 16 (11 to 20) |
| landfall extra_land_drops | 4 to 6 | 5 to 7 | E1 7 (3 to 10) |
| landfall land_recursion | 2 to 4 | 3 to 5 | E1 6 (2 to 11) |
| landfall landfall_payoffs | 10 to 12 [J] | 10 to 12 sourced | E1 11.5 (5 to 21) |
| landfall ramp | 12 to 15 | 18 to 20 [J, owner signal] | at or above the top of the Bracket 3 IQR (notes/11 S15); E1 ramp tag 28.5; notes/09 conflict 2 |
| landfall land band | 38 to 40 | 38 to 40, lean 40 | E1 39.5; K1; K2 |
| spellslinger spell_density | 28 to 32 | 30 to 36 | E1 36 (31 to 43) |
| spellslinger draw | 12 to 15 | 12 to 18 | E1 draw tag 21, card advantage 25; the spend extension stays [J] |
| spellslinger cost_reducers | none | 2 to 4 (new) | E1 3 (1 to 8) |
| tokens token_makers | 12 to 15 | 15 to 20 | E1 regex 32 (13 to 35) |
| tokens token_payoffs | 6 to 8 | 6 to 8 | E1 anthem 6, team pump 4 |
| voltron equipment_auras | 10 to 15 | 12 to 16 | W1 15 to 20; snippets 12 to 18 |
| voltron protection (attack engine) | 5 to 8 | 6 to 8 | W1 8 to 10; E1 15.5 broad |
| voltron evasion, haste | 6 to 8, 2 to 3 | same, now sourced | E1 5.5, 2 |
| combat haste | 4 to 6 | 4 to 6, target 6 | E1 gives haste 4 + hasty 2 |
| counters counter_sources | 10 to 14 | 12 to 18 | E1 20.5 (3 to 46) |
| counters counter_doublers | 3 to 5 | 4 to 7 | E1 11 (0 to 25) |
| aristocrats fodder, sac_outlets | 12 to 15, 10 to 12 | 14 to 18, 10 to 14 | E1 token makers 17; outlets 18 (broad) |
| all ramp bases | 8 to 10 | 10 to 12 | CZ-new 10, 12 with a 4+ commander |
| all draw bases | 10 to 12 | 10 to 12 | CZ-new card advantage 12 |
| land bands outside landfall | 34 to 37 | 35 to 38 (34 to 36 spellslinger) | CZ-new 38; E1 34 to 36; lean-low rule |
Still [J] (no source): mana sinks, wipe insurance, combat team evasion (owner signal), defense while tapped (partly),
combat draw, counter payoffs, pillowfort deterrents, reanimator, blink, artifacts, enchantments, typal, control profile
numbers and every profile not sampled in E1.

### Corrections of earlier statements
- The Karsten land formula is a regression on 95,143 sixty-card tournament decks scaled to 99 cards, not Commander data
  (notes/02 S2, S12, S13 called them winning Commander decks).
- ScrollVault's 19 and 30 colored sources reproduce under Karsten's conditional definition.
- Rule numbering of the multiplayer first draw: 103.8c in earlier notes, 800.7 in Karsten; unverified either way.

### Blind reviewer feedback (items 1 to 3 handled by the lead, 4 to 16 here)
| Item | Handled in |
|---|---|
| 1 comparing lists; 2 commander-conditional pieces; 3 support line met by the commander | S-0b; S-3.4; role-players-and-upgrades.md (lead) |
| 4 joint colors | probability.md E2; S-4 |
| 5 alternate-kill commanders | `alternate_kill` profile; S-1; S-3.2 |
| 6 Game Changer check offline | S-12 live `is:gamechanger` search, no embedded list |
| 7 rules points to verify | output 1; S-1; S-15 item 10 |
| 8 haste promotion | S-3.1; win-routes.md 4 |
| 9 copied cantrips | S-3.4 weights; card-flow.md 2 |
| 10 payoff alternative for sources | `if_commander_is_source`; S-3.1 |
| 11 removal outnumbers plan pieces | S-15 red flag (answers versus closers) |
| 12 typal as a secondary | `if_secondary_modifier`; meta.hybrid |
| 13 window costs | S-4; mana-and-ramp.md 6 |
| 14 bad-when-drawn threshold | S-9; evaluation-and-cuts.md 3 |
| 15 through_wide_board counting | S-3.4 weights; win-routes.md 2 |
| 16 toughness threshold | S-8; win-routes.md 4 |

## 6. Revision 3 (2026-11-01): the gate reads the profiles

`scripts/plan_density.py` now reads `archetypes.json`; the plan file names its `archetype` (and `secondary`,
`secondary_role`, `commander_dependence`, `commander_mv`). What the audit's blocking and important script items became:

| Audit item | Done in the script |
|---|---|
| 1 (U3, G1) reference boards declared late | Always judged early; FAIL when declared late |
| 2 (G2) any card named a tutor | A tutor must carry the tag `tutor`, or FAIL; only tagged tutors count as pieces |
| 2 (G3) commander hides a short function | Pieces and odds reported without the commander; WARN when the function reaches its minimum only with it |
| 3 (U2) `never` counted as bad | Only `early` and `late` count |
| 15 (G4) profile minimums unchecked | Every gate function of the profile must be declared, with the larger of the class and the profile minimum, and not later than the profile says (the commander alternative excepted) |
| U1 | The skill already names `decks/phase2/` |
| U6, U7 | Floors come from the profile; `removal` is the spot-answer tag |
| U9 | Base floors count every tag of a card (primary and second) |
| 24 (support) | `support` block reported against the profile minimum, WARN only |
| G6 (one-card routes) | WARN when a route rests on one card and is not the commander |
| land band and base floors | The profile's, with `commander_dependence` overriding protection and `commander_mv` of 4 or more adding 2 to ramp; a hybrid takes the higher minimums and the band overlap |

Not done (reviewer work, listed in `references/plan-file.md`): G5 tag-versus-Scryfall-tags check, the claim that a route's
`axis` is honest, the half-of-the-secondary-serves-the-primary rule, and the half weights of `meta.weights`.

