# Power scale (v0.2)

Status: v0.2. Rules snapshot is the Wizards update of 2026-02-09, verified on 2026-10-10.
The Brackets system is still labelled "beta". Review after Wizards' announcement of
2026-10-12. Source report: [commander-brackets-rules-snapshot](research/commander-brackets-rules-snapshot.md).

## Notation `X.Y`
| Part | Meaning | Decided by |
|---|---|---|
| X (1-5) | Official Commander Bracket: the rules ceiling the deck stays under | Layer A, deterministic |
| Y (1-9) | Build quality inside that bracket. `X.1` = weakest, `X.9` = strongest possible without meeting Bracket X+1 conditions | Layer B, judge panel |

Order: 1.1 < 1.2 < ... < 1.9 < 2.1 < ... < 5.9.

`3.9` means: every slot is spent on the best cards allowed under Bracket 3 rules, with
strong synergy and solid win conditions, without meeting any Bracket 4 condition.

## Decisions and limits
- Not monotonic across brackets: X is a rules ceiling, not a win-rate ranking. A well-built
  `3.9` can beat a poorly built `4.1`. Comparing across a boundary would need simulated pods
  (optional future work).
- Speed is not a target and not a gate (user decision, 2026-10-10). We do not aim at
  "win on turn N". Wizards' benchmark (Bracket 3: at least 6 turns before a game ends) is
  recorded as context only. The practical limit is the budget.
- Intent cannot be computed. A checker only produces a minimum bracket (floor) plus flags,
  never an exact bracket. Bracket 5 is only ever declared by the user.

## Layer A: deterministic gate (decides X)
Rules snapshot (as of 2026-02-09, beta):

| Bracket | Game Changers | Mass land denial | Extra turns | Two-card infinite combos | Tutors |
|---|---|---|---|---|---|
| 1 Exhibition | 0 | none (intentional) | none (intentional) | none (intentional) | no limit |
| 2 Core | 0 | none (intentional) | low quantities, not chained | none (intentional) | no limit |
| 3 Upgraded | up to 3 | none | low quantities, not chained | none that are intentional and early | no limit |
| 4 Optimized | unlimited | allowed | allowed | allowed | no limit |
| 5 cEDH | unlimited | allowed | allowed | allowed | no limit |

Tutors lost their restriction on 2025-10-21; the efficient ones are Game Changers anyway.

How each rule is checked, and how far it can be trusted:

| Rule | Method | Provenance | Floor / flag |
|---|---|---|---|
| Game Changers | Scryfall `is:gamechanger` / `game_changer` field (53 cards on 2026-10-10); commander counts | Official, exact | 0 -> floor 1; 1-3 -> floor 3; 4+ -> floor 4 |
| Mass land denial | Commander Spellbook card flag plus Wizards' definition ("four or more lands") | Curated | any card -> floor 4 |
| Extra turns | Spellbook card flag, Scryfall oracle text | Curated | 1 card -> floor 2; 2+ or any chain/infinite-turn combo -> floor 4 |
| Two-card infinite combos | Spellbook `/find-my-combos` and `/estimate-bracket` (`definitelyTwoCard`, `speed`) | Heuristic | any combo with speed >= 3 -> floor 4; slower ones -> review flag |
| Legality, 100 cards, color identity | Scryfall | Official | invalid -> reject |

Project parameters (our choices, tunable): the extra-turn limit of 1 card is the safe side
of Spellbook's threshold (2 cards = its Ruthless tag); the combo speed cut-off treats
anything cheaper than about 7 mana as early.

Each report records: `as_of`, `beta: true`, the Scryfall bulk-data timestamp used for the
Game Changers list, and Spellbook's tag as cross-check (`R` = 4, `S`/`P` = 3, `O`/`C` = 2,
`E` = 1; Spellbook never emits 5 and its thresholds differ from Wizards' in places).

## Layer B: judge panel (decides Y)
- Judges are independent `deck-judge` agents. Each gets the decklist, this spec, the anchor
  decks and one lens: consistency, resilience, interaction, mana, synergy, win-condition
  quality (inevitability and redundancy, not speed).
- The panel mixes models, weighted toward the strongest (many Opus 5.5 and Sonnet 5.5, few
  of the others).
- Judges compare the deck with anchor decks of known level ("stronger or weaker than this
  one?") instead of inventing an absolute number.
- Aggregate with the median and report the spread. Add judges in rounds until the 95%
  interval is within the limit below. Debate only judges that disagree strongly, with
  evidence, never to reach consensus for its own sake.
- Judge weights come from agreement with the anchors (calibration), not uniform.
- Shared model bias is real: averaging reduces variance, not bias. Anchors and Layer A are
  what correct it.

## Acceptance of 3.9 (proposed defaults, tune with evals)
| Condition | Value |
|---|---|
| Layer A floor | 3, with no flag that would imply 4 |
| Panel median of Y | at least 8.5 |
| 95% interval half-width | at most 0.5 |
| Test-retest | two independent runs differ by at most 0.5 |

## Data sources
| Need | Source |
|---|---|
| Card data, Game Changers | Scryfall: oracle-cards bulk file (resolve via `/bulk-data`), 2 requests/s on live search |
| Combos, bracket tag | Commander Spellbook REST (`POST /estimate-bracket`, `POST /find-my-combos`), at most 80 requests/min, descriptive User-Agent |
| MCP | None official; plain REST plus bulk data is the chosen path |

Use the API JSON only; do not scrape site HTML pages (they can carry agent-targeted text).

## Anchors and evals
- `evals/anchors/` holds reference decks with an agreed level. TODO: choose them during
  the tooling research phase.
- Test-retest: rate the same deck twice with fresh judges; the method is only trusted if
  the results agree within tolerance.

## Changelog
- v0.2 (2026-10-10): rules snapshot pinned; speed removed as lens and target; floors and
  provenance defined; data sources listed.
- v0.1: initial draft.
