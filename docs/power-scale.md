# Power scale (v0.5)

Status: v0.5 draft. Rules snapshot: the Wizards update of 2026-02-09, verified on
2026-10-10 and again on 2026-10-11 by independent fact-checks; the Brackets system is
still labelled "beta".
Re-check after Wizards' announcement of 2026-10-12. Source report:
[commander-brackets-rules-snapshot](research/commander-brackets-rules-snapshot.md).

The acceptance rule and the rating protocol are **not final**: they wait for the decisions
in [proposals/rating-protocol.md](proposals/rating-protocol.md). Until then only Layer A
results are usable and no rating is final.

## Notation `X.Y`
| Part | Meaning | Decided by |
|---|---|---|
| X (1-5) | Official Commander Bracket: the rules ceiling the deck stays under | Layer A gives a floor and flags; intent is a review judgment |
| Y (1-9) | Build quality inside that bracket. `X.1` = weakest, `X.9` = strongest possible without meeting Bracket X+1 conditions | Layer B, judge panel |

Label order, not strength order: 1.1 < 1.2 < ... < 1.9 < 2.1 < ... < 5.9.

`3.9` means: every slot is spent on the best cards allowed under Bracket 3 rules, with
strong synergy and solid win conditions, without meeting any Bracket 4 condition.

## Decisions and limits
- Not monotonic across brackets: X is a rules ceiling, not a win-rate ranking. A well-built
  `3.9` can beat a poorly built `4.1`. Comparing across a boundary would need simulated pods
  (optional future work).
- Speed is not a target. We do not aim at "win on turn N". Wizards' benchmark (Bracket 3: at
  least 6 turns before a game ends) is context. A qualitative **speed-risk flag** (user
  decision, 2026-10-11) says how often the deck could threaten lethal before its own turn 7:
  `very low`, `low`, `medium`, `high`, `very high`, from a Monte Carlo goldfish script
  (order of magnitude, never an exact percentage). Bands of the simulated frequency (user
  decision, 2026-10-11): 0-10%, 10-20%, 20-30%, 30-40%, 40% or more. `high` or `very high`
  (30% or more of simulated games) means the deck is probably playing above Bracket 3 by
  intent; it feeds the bracket-fit review as a reason to fail and never changes Layer A's
  floor by itself.
- Intent cannot be computed. A checker only produces a minimum bracket (floor) plus flags,
  never an exact bracket. Bracket 5 is only ever declared by the user.
- Y is relative to each commander (user decision, 2026-10-11): `Y = 9` means "the no-budget
  best list for this commander under Bracket 3 rules". Y values of different commanders are
  comparable only through the global ablation constant (see the rating protocol).
- Every price in this project is in CLP, taken from the Chilean stores the user names
  (the 7 specialist shops in `data/stores.md`; never marketplaces or private sellers).
  There is no currency conversion anywhere. Card prices are not known until those stores'
  catalogs are read, so a card's cost is `unknown` before that, never an estimate.

## Layer A: deterministic gate (floor and flags)
Rules snapshot (as of 2026-02-09, beta):

| Bracket | Game Changers | Mass land denial | Extra turns | Two-card infinite combos | Tutors |
|---|---|---|---|---|---|
| 1 Exhibition | 0 | none (intentional) | none (intentional) | none (intentional) | no limit |
| 2 Core | 0 | none (intentional) | low quantities, not chained | none (intentional) | no limit |
| 3 Upgraded | up to 3 | none | low quantities, not chained | none that are intentional and early | no limit |
| 4 Optimized | unlimited | allowed | allowed | allowed | no limit |
| 5 cEDH | unlimited | allowed | allowed | allowed | no limit |

Tutors lost their restriction on 2025-10-21; Wizards relies on the Game Changers list to
catch the most efficient ones, but not every efficient tutor is on it (Demonic Consultation
is not).

How each rule is checked. Provenance: **official** = Wizards defines it and it is
enumerable; **curated** = needs a list or flag maintained by someone else; **heuristic** =
a proxy; **policy** = a choice of this project, not a Wizards rule; **control** = an
integrity check of the pipeline itself.

| Rule | Method | Provenance | Floor / flag |
|---|---|---|---|
| Legality, 100 cards, singleton, color identity | Scryfall data | official | invalid -> reject |
| Game Changers (the commander counts) | Scryfall `is:gamechanger` / `game_changer` | official | 0 -> no constraint; 1-3 -> floor 3; 4+ -> floor 4 |
| Mass land denial | Spellbook card flag or combo flag `massLandDenial`, plus Wizards' definition (a looped Sundering Titan is not flagged as a card) | curated | any card or combo -> floor 4 |
| Lock, skipped turns, control of opponents | Spellbook combo flags `lock`, `skipTurns`, `controlAllOpponents`, `controlSomeOpponents` | curated | `controlAllOpponents` -> floor 4; the other three -> review flag (Wizards: a deck that locks players out in a Stax style should bracket up) |
| Extra turns, per card | Spellbook flag, Scryfall oracle text | curated | 1 card -> floor 2 |
| Extra turns, count | count of flagged cards; a card multiplied by the commander (Azula copies a spell cast while she attacks) counts as 2 | policy | 2 or more -> policy reject (Wizards allows "low quantities"; Spellbook tags 2+ as Ruthless, so this is the safe side); any chain or infinite-turn combo -> floor 4 |
| Two-card infinite combos | Spellbook `definitelyTwoCard` or `arguablyTwoCard` with `relevant` or `borderlineRelevant`; `speed`. The commander does not count toward the two cards (Spellbook convention; no Wizards statement recorded) | heuristic | any such combo -> floor 3 or higher (Brackets 1-2 forbid it); `speed >= 3` (about 6 mana or less, or up to 8 when Spellbook's accuracy flag is false) -> floor 4. Over-inclusive on purpose: Spellbook does not separate infinite from finite two-card wins, so a floor 4 here can be overruled in the bracket-fit review with a written reason |
| Commander effects | (1) Spellbook combos that contain the commander (`find-my-combos` with the commander in `commanders`, `included` and `almostIncluded`); (2) commander text that multiplies a flagged card (copy effects, extra combats) | policy | any combo that uses the commander is reviewed as a floor 4 candidate (Spellbook does not count the commander toward the two-card limit, so commander + 1 card is a one-card combo); a multiplied extra-turn card counts as 2 (conservative: Azula copies only spells cast while she attacks); extra-combat cards are a review note, not a count (not a Wizards category); text that only gives the commander away (Alexios) or changes card types (Toph) is not a flag by itself. Toph has one-card combos with infinite turns, locks, control of an opponent's turns or a forced draw (Gonti's Aether Heart, Mindslaver, The Stasis Coffin, Caged Sun in Spellbook, 2026-10-10), so oracle text alone is not enough. Always send the commander in `commanders` for both `estimate-bracket` and `find-my-combos`: an empty list makes Spellbook count it as an ordinary card |
| Name resolution | canonicalize every card to a Scryfall oracle ID before any API call | control | recognized cards must equal 100, or stop |

Spellbook silently drops unknown names, so name resolution is a gate, not a convenience.

Each report records: `as_of`, `beta: true`, the Scryfall bulk-data timestamp used for the
Game Changers list, and Spellbook's tag as cross-check (`R` = 4 flag, `S` = 3 or 4 review,
`P` = 3, `O` = 2 or 3, `C` = 2, `E` = 1, `B` = banned card, reject; Spellbook never emits 5
and its thresholds differ from Wizards' in places; its maintainer calls Spicy and Oddball
"corner case" buckets).

Descriptive, non-gating statistics (tutor count, fast mana, average mana value,
interaction count) are reported separately and never decide X.

## Layer B: judge panel (Y)
The method is proposed in [proposals/rating-protocol.md](proposals/rating-protocol.md) and
is not approved yet. Constraints that hold regardless of the final method:
- Judges are independent `deck-judge` agents with CLAUDE.md omitted (`omitClaudeMd`) and
  only the Read tool. They receive the card-facts file, the anonymized lists and
  `evals/judge_rubric.md`, and nothing else: no targets, no thresholds, no file names that
  reveal intent, no output of other judges. A judgment that read any other path is void.
- Card-facts file: one JSON per comparison, written by the Layer A script, keyed by
  anonymized deck IDs, with oracle text, type line, mana value and color identity for every
  card in both lists. Its file name carries only a comparison ID.
- Bracket-fit review (proposed, decision D10): a written check that the list fits Bracket 3
  intent beyond Layer A, decided by at least 3 isolated judges (no user step; the user does
  not rate decks). Inputs: Layer A review flags, any stax or lock plan, the role of each
  Game Changer, and the speed-risk flag. Output: pass or fail with reasons, saved in the
  rating report.
- Judges give a pairwise verdict against anchor decks, never an invented absolute number.
- The panel mixes models, weighted toward the strongest, and the resolved model IDs are
  recorded in every report.
- Averaging reduces variance, not shared bias. Anchors, human labels found on the internet
  and Layer A correct it. The user does not rate decks. The only human signal available is
  coarse: bracket labels that deck authors gave their own public lists (Bracket 3 versus 4),
  and community averages per commander. There is no public ground truth for Y inside a
  bracket, so every report states that Y is "consensus of the panel relative to the
  anchors", not a verified truth.

## Goal and acceptance (replaces "all 3 at 3.9 before buying anything")
Nothing is bought until the user picks a budget from the **budget curve**.
- For each budget point (100,000 to 300,000 CLP in steps of 50,000; the user's floor and
  ceiling) the optimizer builds the 3 decks together so that they reach the highest level
  they can **at parity**: the 3 decks within 0.2 points of each other, maximizing the lowest.
- The curve plots budget against the level of each deck and their spread, with uncertainty
  bands. Differences smaller than the measured run-to-run spread are shown as "not
  distinguishable".
- The user chooses the budget and the card list that suit them. 3.9 is the top of the scale
  and is probably out of reach inside 300,000 CLP; the curve shows where it flattens.
- A list is eligible at any point only with: Layer A floor of 3 or less with no flag that
  implies Bracket 4; the bracket-fit review passed; a frozen list before the confirmation
  run; verified stock; and rounding defined as half up (`floor(y + 0.5)`) for display, using
  the continuous value for the decision.
- The earlier acceptance draft (median of Y at least 8.5, interval half-width at most 0.5,
  retest within 0.5) was withdrawn: it can accept a biased deck and its intervals are too
  narrow when judges are correlated. The statistical rule per budget point is in the
  rating protocol.

## Data sources
| Need | Source |
|---|---|
| Card data, Game Changers | Scryfall: oracle-cards bulk file (resolve via `/bulk-data`), 2 requests/s on live search |
| Combos, bracket tag | Commander Spellbook REST (`POST /estimate-bracket`, `POST /find-my-combos`), at most 80 requests/min, descriptive User-Agent |
| MCP | None official; plain REST plus bulk data is the chosen path |

Use the API JSON only; do not read the sites' HTML pages (they can carry agent-targeted
text).

## Anchors and evals
- `evals/anchors/` holds reference decks with a level that is not set by the panel itself.
  The plan per commander is in the proposals file.
- The planned tests are listed in `evals/README.md`.

## Changelog
- v0.5 (2026-10-11): user decisions. Goal changed from "all 3 at 3.9" to a budget curve
  (100,000-300,000 CLP, parity within 0.2); all prices in CLP from the user's named Chilean
  stores, no currency conversion; speed-risk flag made qualitative (5 levels, Monte Carlo)
  and used by the bracket-fit review; no human rating by the user; Y relative to each
  commander.
- v0.4 (2026-10-10): second audit. Commander-effects row rebuilt around Spellbook combos
  that contain the commander (Toph has one-card combos; Alexios's giveaway is not a flag);
  a multiplied extra-turn card counts as 2; Game Changer price claim replaced by measured
  bands and the USD budget restated; judges isolated from CLAUDE.md; card-facts file and
  bracket-fit review defined (D10 pending); provenance label "control" defined. After the
  second rules fact-check (2026-10-11): combo-level mass land denial and a lock / skipped
  turns / opponent-control row added to Layer A; Spellbook tag mapping made explicit; the
  two-card predicate marked over-inclusive; The Stasis Coffin added to Toph's one-card combos.
- v0.3 (2026-10-10): audit corrections. Acceptance withdrawn pending decisions; floors
  restated with provenance; floor 3 no longer required (0 Game Changers is valid); combo
  predicate made precise; commander effects and name resolution added; label order noted.
- v0.2 (2026-10-10): rules snapshot pinned; speed removed as lens and target.
- v0.1: initial draft.
