---
name: rate-deck
description: Rate a Commander decklist on the project's custom power scale X.Y. Use when asked to rate, evaluate or re-evaluate a deck's power level, or to confirm a deck is 3.9.
disable-model-invocation: true
argument-hint: [path-to-decklist]
---

Rate the deck at $ARGUMENTS following `docs/power-scale.md` (read it first).

1. Layer A (deterministic). Compute and list: legality, Game Changers count, mass land
   denial, extra-turn chains, two-card infinite combos with the earliest turn, tutor
   count, fast mana, average mana value, interaction count. Use Scryfall data and
   Commander Spellbook (`/estimate-bracket`); never rely on memory for card text. This
   decides X as a floor, with flags, never as an exact bracket. Cite the rules snapshot
   date from `docs/power-scale.md`.
2. Layer B (panel). Only after the user opts in to a workflow: show the planned agent
   count and model mix first. Judges are `deck-judge` agents with different lenses,
   independent from each other, compared against `evals/anchors/`. Aggregate with the
   median and report the spread; add judges in rounds until the interval limit in the
   spec is met.
3. Report a table: X, Y (median, spread, number of judges, models), gate evidence,
   weakest slots, and what would raise Y without crossing the bracket.
4. Save the report to `decks/reports/<deck>-<date>.md`.

Never present Y as more precise than the measured spread.
