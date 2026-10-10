---
name: build-deck
description: Build or upgrade one Commander deck under the project's power scale, budget and verified-stock constraints. Use when asked to build, upgrade or re-plan a deck.
disable-model-invocation: true
argument-hint: [commander-name]
---

Plan the deck for $ARGUMENTS. Respect every hard constraint in `CLAUDE.md`.

1. Inputs: current decklist (if any), the user's collection export in `data/raw/`, the
   remaining budget across all 3 decks.
2. Candidates: pick cards by role (ramp, draw, interaction, win conditions, synergy
   engine). Prefer owned cards; justify each purchase by the weakest slot it replaces.
3. Gate: run the Layer A checks from `docs/power-scale.md`; drop anything that would
   meet a Bracket 4 condition.
4. Stock: run the `check-stock` skill on every card to buy. Re-plan with substitutes when
   stock fails (backtracking); count total stores and cost again after each change.
5. Rate with `rate-deck`. Iterate until the deck reaches 3.9 or the budget is exhausted.
6. Deliver: final list in `decks/`, shopping list grouped by store, total cost in CLP,
   and the evidence timestamps.

Long iteration loops are a good fit for a `/goal` with a measurable end state and a turn
limit.
