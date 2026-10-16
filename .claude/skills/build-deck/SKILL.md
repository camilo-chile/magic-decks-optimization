---
name: build-deck
description: Plan the build or upgrade of a Commander deck under the project's power scale, budget and verified-stock constraints. Use when asked to build, upgrade or re-plan a deck.
disable-model-invocation: true
argument-hint: "[commander-name]"
---

Plan the deck for $ARGUMENTS. Respect every hard constraint in `CLAUDE.md`. Plan first.

0. Gate. Read the pipeline in `README.md` and name the current phase. This skill starts at
   Phase 8 and needs Phases 6 and 7 done. Step 5 belongs to Phases 9-10; steps 6 and 7 to
   Phase 11. If a needed phase is not done, say which and stop.
1. Inputs: the current decklist (if any), the validated collection dataset, the locked
   cards file `decks/locked.txt` (each card in at least one of the project's decks, see `decks/locked.md`) and the Phase 8
   allocation (per-deck swap list and budget share). Never plan one deck against "the
   budget left"; that is greedy and order-dependent.
2. Candidates come from Commander Salt, not from Claude's judgment: the measured lists in
   `decks/candidates/<slug>/` (real public lists with their site score) and, for an upgrade, the
   Upgrades Meta picks (`meta-staples-bracket3.md`, or the Upgrades tab at the deck's bin).
   Prefer a measured list that passes Layer A; take a pick only when it is not already in the
   deck. Treat owned cards as cost 0, but allocate physical copies across the 3 decks globally:
   one copy can sit in only one deck. Justify each purchase by the site's per-card contribution
   or inclusion rate, and note when a swap makes the list "unmeasured" until it is scored.
3. Gate: apply the Layer A checks from `docs/power-scale.md` through the user-run script
   outputs. Drop anything that implies a Bracket 4 condition.
4. Present the plan (cards, roles, estimated cost, candidate stores) and ask "execute now?".
   Stop here. Nothing below runs without the user's go-ahead.
5. Stock: ask the user to run `/check-stock` on the shortlist. When stock fails, re-plan
   with substitutes and recompute the totals. At most 5 substitution rounds, then stop and
   report what blocks the plan.
6. Scoring: write the frozen candidate to `decks/<commander-slug>.txt`, ask the user for a
   ManaBox link of it, then run `/rate-deck <commander-slug>` (Commander Salt power and bracket)
   and continue once the report exists.
7. Deliver: the shopping list grouped by store, the total cost in CLP including shipping,
   and the evidence timestamps. Then the optional tokens: list the tokens and emblems the final
   decks create, ask the owner which he already has, check stock for the missing ones only in
   stores already in the plan, show them as a separate optional block outside the budget and
   ask whether to add them.

A `/goal` re-runs Claude after each turn and a small fast model judges the condition from
the transcript only. There is no turn-limit option: put the bound in the condition (for
example "or stop after 20 turns"). A goal never changes permissions and never authorizes
stock checks, script runs or purchases; `/check-stock` and `/rate-deck` can only be started
by the user.
