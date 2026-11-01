# Interaction, protection and resilience in 3 to 4 player pods

Sources: notes in `docs/research/commander-deckbuilding/notes/`, mainly notes/04. No source read gives outcome data
(whether more removal or more wipes wins more games).

## 1. Removal

### Counts
| Figure | Scope | Source |
|---|---|---|
| floor 8 to 10 removal spells inside a 15 to 20 card interaction package | personal baseline, not split by archetype | notes/04 S2 |
| 8 to 12 including wipes; spot removal 5 to 8; wipes 2 to 4 | template | notes/04 S4 |
| about 10; aggressive decks 5 to 7; a long-game deck 15+ | EDHREC upgrade guide | notes/09 S17 |
| 3 to 5 spot answers for threats that must be answered | two sources | notes/04 S2, S4 |
| 6 targeted removal + 3 wipes | MTGGoldfish checklist | notes/03 S1 |
| Bracket 3 median: spot removal 5 (3 to 7), wipes 2 (1 to 4), counterspells 1 (0 to 3) | survey of 1,285 lists | notes/11 S15 |
| targeted disruption 12 (creature removal, counterspells, bounce, phasing, tappers, land destruction, targeted graveyard hate); mass disruption 6 | Command Zone 2025 template | notes/13 CZ-new |
| EDHREC Bracket 3 averages (Tagger removal tag): landfall 5.5, counters 6.5, voltron 8.5, tokens 10, combat 10.5, spellslinger 11, aristocrats 14.5 | community behaviour, broad tags | notes/13 E1 |

The totals use different definitions (whether wipes and counterspells count) and are not directly comparable (notes/04
conflict 2). Choice for Bracket 3: 8 to 10 total answers, of which 3 to 5 are flexible spot answers; adjust by archetype
in `archetypes.json`.

**One definition [J].** `removal` = SPOT answers: one target per card (destroy, exile, bounce used as an answer,
counterspell, steal, tap-lock, edict). Counterspells count here. Wipes are counted apart. Total answers = removal + wipes
(floor 8 to 10). Profile mins are spot-only (5 to 8), so a combat deck at 5 spot removal and 0 to 1 wipes is under the
generic total on purpose and writes the reason.

### Mix and quality
- In a four-player pod a one-for-one trade with one opponent leaves you and that player behind the two who spent nothing
  (notes/04 S2). You cannot rely on spot removal to solve your problems in multiplayer (notes/04 S3).
- Prefer two-for-one answers: creatures whose entry removes a permanent, planeswalkers that remove repeatedly, edicts that
  hit every opponent (notes/04 S2, S4).
- Spread answers across permanent types; creature-only removal leaves gaps against artifacts, enchantments and other
  noncreature threats (notes/04 S2, S4). Artifact and enchantment removal is under-represented in lists (notes/11 S6,
  opinion).
- Aim removal at what stops your deck or wins for them: the commander, a combo piece, a draw engine, a sacrifice outlet
  (notes/04 S4). Removal order: immediate danger, then engines, then cards that shut your strategy down (notes/05 S3).
- Edicts are excellent against single-creature decks and weak against wide boards (notes/04 S2; notes/04 section 5).
- Bounce is weaker in Commander; targeted discard is a poor fit (notes/04 S2).
- Commanders come back; neutralizing one (pacifism-style or transform effects) can beat destroying it (notes/04 S3).
- Combo decks use removal defensively, to stop the one card that stops them (notes/04 S4).
- Removal is a supporting role; keep 1 to 2 ready, not a hand full of it (notes/04 S3). A deck heavy in one-for-one
  answers with no way to get damage through loses: the missing piece is the threats, not the removal (notes/04
  inference).
  [J] Flag a list whose removal count exceeds its plan pieces.
- Removal can be a bargaining chip (notes/04 S2).

## 2. Board wipes

### Counts (conflict)
| Figure | Source |
|---|---|
| 3 to 5 for most decks; creature decks fewer, control more; about 10 too many (the range is for MOST decks, not for control) | notes/04 S1 (Draftsim 2025) |
| 1 to 2 for most decks | notes/04 S2 (same author, 2024) |
| 2 to 4 | notes/04 S4 |
| no more than 3 | notes/04 S5 |
| two is usually enough | notes/09 S17 |
| Bracket 3 median 2 (1 to 4) | notes/11 S15 |
| mass disruption 6 (wipes plus tax effects, artifact or enchantment sweepers, graveyard wipes) | notes/13 CZ-new |
| EDHREC Bracket 3 averages: landfall 1, counters 1, tokens 2, voltron 2, aristocrats 2, combat 2.5, spellslinger 3 | notes/13 E1 |

Choice: 2 as the generic base (median and two sources); 0 to 2 for creature and token decks, only one-sided or synergy
wipes [J; the 0 to 2 is not in the source, which says only "fewer"]; 3 to 5 for control and creature-light decks [J on the
exact range; the source says "more"]. Reason: symmetric wipes hit your own board, and creature decks that
stack wipes work against themselves (notes/04 S1; notes/06 S2 lists self-hosing wraths as a mistake).

### Kinds
- One-sided wipes (only opponents' permanents) are worth adding whenever possible except in control decks indifferent to
  their board; being hit by one is often game-losing (notes/04 S1).
- Synergy wipes act one-sided inside your deck (a conditional wipe your creatures never meet) (notes/04 S1).
- In multiplayer a wipe costs opponents more cards than you, even if you keep some creatures (notes/04 S1), but mass
  removal can push the table against you (notes/04 S3). Weigh both.
- Instant-speed wipes let you rebuild first; sorcery-speed ones let opponents rebuild first (notes/04 S1).
- Bounce wipes lose your own enter-the-battlefield value and let opponents recast commanders without tax (notes/04 S1).

## 3. Protection

### Counts
- 5 to 7 per deck in the text, 5 in the recap; protection varies more across decks than ramp, draw or removal (notes/04 S5,
  single source, 2021). Commander-dependent decks need more protection for the commander (notes/04 S5).
- The gate warns under 3 (judgment). The gate review proposes 4 commander-protection pieces when the commander is in a win
  route, and 2 wipe-insurance pieces (judgment).
- This skill separates two counts. **Commander protection** (profile key `base.protection`) follows commander dependence
  (SKILL.md step 1; `archetypes.json` `meta.commander_dependence`): engine 5 to 7, attack engine 6 to 10, enabler 3 to 4,
  value 2 to 3 [J]; the attack-engine range rests on a voltron guide's 8 to 10 protection spells (notes/13 W1, opinion)
  and on community averages that tag 10 (combat) to 15.5 (voltron) cards as protection with a broad tag (notes/13 E1).
  **Wipe insurance** (a separate support function of board-based plans) is 2 to 4 pieces [J]. Total protection =
  commander protection + wipe insurance; a card counts in both only if it does both jobs, and the actual commander's
  class overrides the profile's default.
- What the table holds, to size both: by turn 8 about 2.3 spot removal and 0.9 wipes have been seen across three
  opponents (`multiplayer-politics-and-threat.md` section 6).

### Layers: what stops what (notes/04 S1, S6)
| Threat | Stopped by | Not stopped by |
|---|---|---|
| Targeted removal | hexproof, shroud, ward (taxes), protection from a color [rules knowledge, not in the notes], counterspells | indestructible (exile, bounce, -X/-X still work) |
| Destroy wipes, damage | indestructible; damage prevention or protection against damage-based wipes | hexproof, shroud |
| Exile wipes | phasing | indestructible, hexproof |
| -X/-X wipes | phasing | indestructible |
| Mass bounce | nothing in place; rebuild | indestructible, protection |
| Sacrifice / edicts | more bodies, free outlets, recursion | hexproof, shroud, indestructible |

- Shroud also stops your own targeting; hexproof does not. For a deck that targets its own creatures, hexproof equipment is
  better (notes/04 S6).
- Equipment that grants haste plus hexproof or shroud combines haste with protection (notes/06 S15 card text; inference).
- A commander-dependent deck needs at least one answer per row it expects: targeted removal, destroy wipes, and exile or
  -X/-X (notes/04 inference). Protection spells that grant indestructible blank destroy wipes only (notes/04 S1).
- Counterspells double as protection and can stop a wipe aimed at your board (notes/04 S5; notes/05 S5).
- Opponents can pool removal to strip one layer of protection and then answer the threat (notes/06 S6).

## 4. Resilience and recovery
- Graveyard recursion 2 to 3 for a non-graveyard deck (notes/04 S5). Graveyard hate at least 1 (notes/09 S17; notes/03 S1).
  A deck with its own recursion wants hate it controls (a one-shot exile on demand, a repeatable effect it can turn off)
  rather than a symmetric static one [J].
- Exile answers deny opponents' recursion; graveyards feed other decks too (notes/04 S1, S3).
- Commanders return from wraths (notes/04 S3).
- Two plans against wipes for creature decks: indestructible creatures, or recursion and token production (notes/12 C3).
  Self-sacrificing creatures and free sacrifice outlets turn a wipe into value (notes/12 C1). Keep protection, recursion
  and draw in reserve rather than overcommitting (notes/12 C5 anecdote); do not go wide when the opponents' colors or
  archetypes point to sweepers (notes/12 C1).
- After a wrath, equipment and big threats let one or two creatures keep pressure (notes/12 C3).
- No source gives a rebuild count after a wipe (notes/04 gap).

## 5. Being the threat
- Build answers to being the table's target, not only answers to the table's cards: protection, counters, wipes (notes/05
  S3). Deterrent threats (cards that punish attacks or removal) make opponents weigh attacks (notes/05 S2).
- Cards that make you a target (big card-advantage engines, a huge single creature) draw removal; let others make the first
  big play (notes/06 S7).
