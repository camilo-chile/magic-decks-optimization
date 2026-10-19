# Evals

Tests of the data pipeline and of the Commander Salt scoring. Offline tests run with
`python tests/<file>.py` (pytest is not installed in the base interpreter). The judge-panel evals
of the earlier design were dropped on 2026-10-13 with the switch to Commander Salt.

| ID | Artifact | What it checks | Pass rule / status |
|---|---|---|---|
| E-0 | `evals/hook_cases.tsv` with `evals/run_hook_cases.sh` | The git-writes hook: 140 cases (read-only git allowed, state-changing spellings blocked) | 0 failures: `sh evals/run_hook_cases.sh .claude/hooks/block-git-writes.sh evals/hook_cases.tsv`. Passing |
| E-1 | `tests/test_layer_a.py` (37), `tests/test_golden_decks.py` (6) | Layer A: Game Changer counts, mass land denial, extra turns (up to 3, the 4th is floor 4), early and late two-card combos with the cards' own mana values, a finite combo, locks as notes, target bracket, singleton, identity, 100 cards, banned, front-face names, Spanish and unknown names, commander omitted; golden floors of the real Toph, Azula and Alexios lists | All green. Passing |
| E-2 | The rules-freshness line printed by `scripts/layer_a.py` on every run | Bulk date and Game Changers count against the pinned 53 (2026-10-13) | Prints a `STALE?` line when the count differs; the banned list and Spellbook schema are re-read by hand. Run at 2026-11-30 and in Phase 11 |
| E-4 | `tests/test_build_inventory.py` (5) | Owned-card inventory | Passing |
| E-5 | `tests/test_collect_research_data.py` (3), `tests/test_collect_spellbook_bulk.py` (3) | Bulk collector helpers | Passing |
| E-6 | `tests/test_read_store_prices.py` (10), `tests/test_merge_prices.py` (4) | Phase 7 price readers and the merge: language, condition and finish, art cards excluded, Spanish wins a price tie, newest good reading per store | Passing |
| E-7 | `tests/test_allocation_model.py` (6) | Phase 8 model: owned copies first, one physical copy per deck, basics free, no-stock reported, Spanish on ties, Japanese copies not usable, locked coverage | Passing |
| E-8 | Validator of a proposed list and JSON Schema for `data/stock/*.json` (planned, Phase 8 step 3 and Phase 9) | Layer A, identity, singleton, stock, shared copies, lock coverage; store, URL, variant, language, condition, price, quantity, evidence, UTC timestamp | A purchase list is rejected if any line fails or is stale |
| E-9 | Commander Salt repeatability (Phase 5, by hand) | The same list scored on two days agrees; the owner's two decks and the friend's Krenko deck as fixed points | Done 2026-10-14 for Toph (identical); recorded in `decks/reports/` |

The optimizer (`scripts/optimize_budget.py`, 5 offline tests in `tests/test_optimize_budget.py`) uses only the standard library: it enumerates the measured lists of each deck, so `pulp` is not needed (2026-10-19).
