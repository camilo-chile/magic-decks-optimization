# Power scale (v0.9)

> **Superseded on 2026-10-13 (owner decision).** The power yardstick is now Commander Salt's:
> power 1-10 with its bands, and its decimal bracket (see `docs/proposals/commandersalt-adoption.md`).
> The `X.Y` scale, the Layer B judge panel, the ablation-ladder labels and the local Ollama judge
> described below are historical. Layer A (official conditions of the target bracket, offline)
> stays as the pre-gate for the optimizer.

Status: v0.8.2 draft. Rules snapshot: the Wizards update of 2026-02-09, verified on
2026-10-10 and again on 2026-10-11 by independent fact-checks; the Brackets system is
still labelled "beta".
Checked on 2026-10-13 against Wizards' own pages: the 2026-10-12 Banned and Restricted
announcement changes Competitive Brawl only (Commander: no changes; no Brackets or Game
Changers item), and the Commander page still says Brackets are in beta with up to three Game
Changers at Bracket 3. A Commander announcement is expected before the end of 2026; re-check
at the 2026-11-30 Banned and Restricted announcement and in the Phase 11 freshness check. Source report:
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
`4.9` means the same under Bracket 4 rules (no card limits): the best list for the commander
that is not a metagame-tuned cEDH list. That edge is judged by the panel, never computed, and
Bracket 5 is only ever declared by the user.

## Decisions and limits
- **Power first (user decision, 2026-10-12).** The decks are for casual games with friends and
  the goal is the strongest, most consistent list the chosen budget buys. The only limits are
  Wizards' official conditions of each deck's **target bracket** (Game Changers, mass land
  denial, extra turns, early two-card infinite combos at Bracket 3; none at Bracket 4) and
  Commander legality. A rule that is only this project's own, and that lowers power, is not
  allowed. All three decks target Bracket 3; a deck may be given another target in `TARGET_BRACKET`
  (`scripts/layer_a.py`).
- Not monotonic across brackets: X is a rules ceiling, not a win-rate ranking. A well-built
  `3.9` can beat a poorly built `4.1`. Comparing across a boundary would need simulated pods
  (optional future work).
- Speed is not a target. We do not aim at "win on turn N". Wizards' benchmark (Bracket 3: at
  least 6 turns before a game ends) is context. A qualitative **speed-risk flag** (user
  decision, 2026-10-11) says how often the deck could threaten lethal before its own turn 7:
  `very low`, `low`, `medium`, `high`, `very high`, from a Monte Carlo goldfish script
  (order of magnitude, never an exact percentage). Bands of the simulated frequency (user
  decision, 2026-10-11): 0-10%, 10-20%, 20-30%, 30-40%, 40% or more. The level is
  **reported only** (user decision, 2026-10-12): it is context for the bracket-fit review
  judges, never a pass or fail by itself, and never changes Layer A's floor. Reason: a
  commander can be a fast clock on its own (Alexios, Deimos of Kosmos is `very high` with 63
  blank cards next to it), so an absolute threshold would fail the commander, not the deck.
  The model grows and rotates such a commander at every upkeep but does not model equipment,
  removal or blockers, so for a gear deck it is a floor of the real speed.
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

**Spellbook data source (v0.7, user decision 2026-10-12).** Wherever a row below says
`find-my-combos`, `estimate-bracket` or a Spellbook flag, read it as matched **locally**
against Commander Spellbook's published bulk file (`variants.json.gz`, fetched by
`scripts/collect_spellbook_bulk.py`; its API documentation asks clients not to export the
dataset through the API). `estimate-bracket` stays an optional cross-check. The bulk file
has `bracketTag`, produced features ("Mass Land Denial", "Lock", "Infinite turns" and
others), `manaNeeded` / `manaValueNeeded` and the card list, but not the API's `relevant`,
`speed` or `definitelyTwoCard` fields, so: a two-card combo is a variant with exactly two
cards (the commander not counted) and no template requirement; speed is judged from
`manaValueNeeded`, using 8 or less (the looser end of the two-card row, because the
accuracy flag is not in the file). A variant that uses the commander is a floor-4
candidate whatever its size, as the commander-effects row says. A variant with template
requirements ("any creature with persist") cannot be resolved offline and is listed for
review when it has a winning, infinite, mass land denial, lock or control feature. Spellbook's
own tag is a cross-check: a variant tagged R that the predicates leave under floor 4 is
listed for review. Combos Spellbook does not list (the Toph
Emeria Shepherd loop, the Azula self-copy loop) are covered by a curated hazard list
built from the Phase 3 reports, not by Spellbook.

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
| Extra turns, count | count of flagged cards; a card multiplied by the commander (Azula copies a spell cast while she attacks) counts as 1 card, with a review note because it gives two consecutive extra turns (user decision, 2026-10-12) | curated | Wizards: "low quantities, not chained or looped". Read as at most 3 cards (the 4th sets floor 4; 2 and 3 are a review note, no rejection); any chain or infinite-turn combo -> floor 4 |
| Two-card infinite combos | Spellbook bulk variants with 2 cards or fewer, the commander counted as a card, whose features are infinite or win the game; the "early" test uses the mana to assemble the combo: the larger of `manaValueNeeded` and the mana values of the cards (`manaValueNeeded` is the mana beyond the pieces and is 0 for most combos of permanents: median ratio 0.0 to the pieces' total over 108,039 variants, measured 2026-10-12) | heuristic | Wizards bans intentional **early-game** two-card infinite combos at Bracket 3. Early = mana to assemble of 6 or less (Spellbook's speed >= 3) -> floor 4. 7 or 8 (the bulk file has no accuracy flag) -> floor 3 with a review note. 9 or more -> floor 3 (Brackets 1-2 forbid any). Finite two-card value combos and combos of 3 or more cards set no floor |
| Commander effects | (1) Spellbook combos that contain the commander, counted as one of the cards; (2) commander text that multiplies a flagged card (copy effects, extra combats) | policy | a combo of the commander plus one card is a two-card combo and follows the row above; locks, skipped turns and control of an opponent's turns are review notes, not floors (Wizards' text names none of them); a multiplied extra-turn card counts as 1 card with a review note (user decision, 2026-10-12; Azula copies only spells cast while she attacks, and the official rulings confirm one copied extra-turn spell gives two extra turns); extra-combat cards are a review note, not a count (not a Wizards category); text that only gives the commander away (Alexios) or changes card types (Toph) is not a flag by itself. Always send the commander in `commanders` for any Spellbook estimator call: an empty list makes Spellbook count it as an ordinary card |
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
- Bracket-fit review (decision D10, restated 2026-10-12): a written, report-only note from at
  least 3 isolated judges on whether the list reads as its target bracket by Wizards' text. It
  is context for the user and never a pass or fail: only Layer A's official conditions block a
  list. Inputs: Layer A review flags, the role of each Game Changer and the speed-risk flag.
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
- A list is eligible at any point only with: Layer A floor at or below the deck's target
  bracket and no rejection; a frozen list before the confirmation run; verified stock; and
  rounding defined as half up (`floor(y + 0.5)`) for display, using the continuous value for
  the decision. The bracket-fit review and the speed flag are reported, not gates.
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
- v0.9 (2026-10-13): owner decision: Commander Salt's power and bracket replace this scale and
  Layer B. Layer A stays. See the banner above.
- v0.8.2 (2026-10-12): user decision: all three decks target Bracket 3 again. Toph's current
  list measures floor 3 with the official conditions, so it does not need Bracket 4.
- v0.8.1 (2026-10-12): the "early" test counts the mana values of the two cards as well as
  Spellbook's `manaValueNeeded` (code review item F-13 closed with data). Toph's current list
  drops from floor 4 to 3: Bumi + Ashaya cost 14 mana together.
- v0.8 (2026-10-12): user decision, power first. Only official conditions of the target
  bracket limit a deck. Per-deck target bracket (Toph 4, Alexios 3, Azula 3); the extra-turn
  rejection at 2 cards is gone (floor 4 from the 4th card); two-card combos count the
  commander and need to be infinite and early (mana value needed 6 or less); control of a
  turn and locks are review notes; the speed flag and the bracket-fit review are reported,
  not gates. The Alexios reference must be rebuilt without the caps of its first draft.
- v0.7 (2026-10-12): user decision: Spellbook combos are matched locally against its
  published bulk file instead of `find-my-combos`; two-card and speed predicates restated
  for the fields the bulk file has; a curated hazard list covers combos Spellbook lacks.
- v0.6 (2026-10-12): user decision: the extra-turn count policy is relaxed. A card
  multiplied by the commander (Azula) counts as 1 card, not 2, so one extra-turn card is
  allowed in any deck; 2 or more cards, chains and infinite-turn combos keep their outcomes.
  Reason given: the decks are for casual games and the goal is maximum power inside
  Bracket 3; the bracket-fit review still sees the two consecutive turns as a review note.
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
