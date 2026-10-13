# Evals

Tests of the data pipeline and of the Commander Salt scoring. Offline tests run with
`python tests/<file>.py` (pytest is not installed in the base interpreter). The judge-panel evals
of the earlier design were dropped on 2026-10-13 with the switch to Commander Salt.

| ID | Artifact | What it checks | Pass rule / status |
|---|---|---|---|
| E-0 | `evals/hook_cases.tsv` with `evals/run_hook_cases.sh` | The git-writes hook: 140 cases (read-only git allowed, state-changing spellings blocked) | 0 failures: `sh evals/run_hook_cases.sh .claude/hooks/block-git-writes.sh evals/hook_cases.tsv`. Passing |
| E-1 | `tests/test_layer_a.py` (35), `tests/test_golden_decks.py` (6) | Layer A: Game Changer counts, mass land denial, extra turns (up to 3, the 4th is floor 4), early and late two-card combos with the cards' own mana values, a finite combo, locks as notes, target bracket, singleton, identity, 100 cards, banned, front-face names, Spanish and unknown names, commander omitted; golden floors of the real Toph, Azula and Alexios lists | All green. Passing |
| E-2 | `scripts/rules_freshness.py` (planned) | Game Changers list and count, banned list and Spellbook schema against the pinned snapshot | Prints `OK` or `STALE: <what>`. Run at 2026-11-30 and in Phase 11 |
| E-3 | `tests/test_validate_deck_export.py` (7) | The ManaBox deck export validator: totals, singleton, foil marker, binder isolation, languages, text against CSV | Passing |
| E-4 | `tests/test_build_inventory.py` (5), `tests/test_build_ablation_ladder.py` (5) | Owned-card inventory; the nested ablation rungs | Passing |
| E-5 | `tests/test_collect_*.py` | Bulk collectors and the rulings reader | Passing |
| E-6 | `scripts/optimize_purchase.py` and tests (planned) | Shipping as a fixed cost per store (no store cap), preference order as tie-break; quantities; English or Spanish only; condition floor; total with fees within budget; infeasible gives a clear report | Constraints asserted on toy store data |
| E-7 | `scripts/allocate_collection.py` and tests (planned) | No physical copy in two decks; singleton per deck; basic lands; locked cards respected | Asserted |
| E-8 | JSON Schema for `data/stock/*.json` (planned) | Store, URL, variant, language, condition, price, quantity, evidence, UTC timestamp | A purchase list is rejected if any line fails or is stale |
| E-9 | Commander Salt calibration (Phase 5, by hand) | Power falls as the 5 ablation rungs replace more of the best cards; the same list scored twice agrees; the owner's two decks and the friend's Krenko deck as fixed points | Recorded in `decks/reports/`, stamped with the site's scoring version |

Dependencies to add when the optimizer is written: `numpy`, `scipy`, `pulp`; pin versions then.
