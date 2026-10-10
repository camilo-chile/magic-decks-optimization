# Power scale (v0.1 draft)

Status: draft. Thresholds marked TODO must be pinned against Wizards of the Coast's
official Commander Brackets page; secondary sources disagree on several of them.

## Notation `X.Y`
| Part | Meaning | Decided by |
|---|---|---|
| X (1-5) | Official Commander Bracket: the rules ceiling the deck stays under | Layer A, deterministic |
| Y (1-9) | Build quality inside that bracket. `X.1` = weakest, `X.9` = strongest possible without meeting Bracket X+1 conditions | Layer B, judge panel |

Order: 1.1 < 1.2 < ... < 1.9 < 2.1 < ... < 5.9.

`3.9` means: every slot is spent on the best cards allowed under Bracket 3 rules, with
strong synergy and fast, easy win conditions, without meeting any Bracket 4 condition.

## Important limit: not monotonic across brackets
X is a rules ceiling, not a win-rate ranking. A well-built `3.9` can beat a poorly built
`4.1`. Comparisons across a bracket boundary need an empirical measure (simulated pods);
this is an optional future addition, not part of v0.1.

## Layer A: deterministic gate (decides X)
Computed by code from Scryfall data and Commander Spellbook, never from memory:

| Check | Why it matters for the bracket |
|---|---|
| Format legality, 100 cards, color identity | Hard validity |
| Game Changers count | Main bracket driver (list changes over time) |
| Mass land denial | Excluded below Bracket 4 |
| Extra-turn chains | Excluded below Bracket 4 |
| Two-card infinite combos and the earliest turn they can fire | Timing limits per bracket |
| Tutor count | Consistency signal and bracket guidance |

Rules snapshot: TODO. Record the source URL, the date, and each threshold here before
the first rating. Every rating report cites this snapshot.

## Layer B: judge panel (decides Y)
- Judges are independent `deck-judge` agents. Each gets the decklist, this spec, the
  anchor decks and one lens: speed, resilience, interaction, mana, synergy.
- The panel mixes models, weighted toward the strongest (many Opus 5.5 and Sonnet 5.5,
  few of the others).
- Judges compare the deck with anchor decks of known level ("stronger or weaker than
  this one?") instead of inventing an absolute number.
- Aggregate with the median and report the spread. Add judges in rounds until the 95%
  interval is within the limit below. Debate only judges that disagree strongly, with
  evidence, never to reach consensus for its own sake.
- Judge weights come from agreement with the anchors (calibration), not uniform.
- Shared model bias is real: averaging reduces variance, not bias. Anchors and Layer A
  are what correct it.

## Acceptance of 3.9 (proposed defaults, tune with evals)
| Condition | Value |
|---|---|
| Layer A bracket | 3, with zero Bracket 4 conditions |
| Panel median of Y | at least 8.5 |
| 95% interval half-width | at most 0.5 |
| Test-retest | two independent runs differ by at most 0.5 |

## Anchors and evals
- `evals/anchors/` holds reference decks with an agreed level. TODO: choose them during
  the tooling research phase.
- Test-retest: rate the same deck twice with fresh judges; the method is only trusted if
  the results agree within tolerance.

## Changelog
- v0.1: initial draft.
