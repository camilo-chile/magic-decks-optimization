# Evals

Tests of the rating method and of the data pipeline. Nothing here is implemented yet; this
is the plan, sized to what the project needs. Offline tests use cached API responses so
they are repeatable.

| ID | Artifact | What it checks | Pass rule |
|---|---|---|---|
| E-1 | `tests/test_layer_a.py` with JSON fixtures | Game Changer count 0/3/4 and a commander that is one; mass land denial; extra turns 1 / 2 and Azula plus one extra-turn instant (Nexus of Fate, Final Fortune) counting as 2; a slow versus a fast two-card combo; commander plus one card (Toph with Gonti's Aether Heart, Mindslaver or Caged Sun) as a floor 4 candidate; Azula + Snap + Dualcaster Mage as a commander-plus-two combo; Alexios producing no commander flag; a combo-level mass land denial flag and lock / skipped-turn / opponent-control flags (Toph with The Stasis Coffin); the commander omitted from `commanders` being caught as a pipeline error; singleton; color identity (Boros Reckoner rejected and Flame Javelin accepted in mono-red); 100 cards; banned; front-face names (Tergrid, God of Fright) resolve to one oracle ID and count as a Game Changer; Spanish and unknown names fail loudly | All green; recognized count equals 100 |
| E-0 | `evals/hook_cases.tsv` with `evals/run_hook_cases.sh` | The git-writes hook: 140 cases (read-only git allowed, state-changing spellings blocked, accepted false positives) | 0 failures: `sh evals/run_hook_cases.sh .claude/hooks/block-git-writes.sh evals/hook_cases.tsv` |
| E-2 | `scripts/rules_freshness.py` | Hash of the Game Changers list and count, banned list, Spellbook schema version and resolved model IDs against the pinned snapshot | Prints `OK` or `STALE: <what>` |
| E-3 | `evals/judge_suite/` | Ablation-ladder ordering; order swap; placebo; label leak; known-answer accuracy; card-text hallucination audit; ICC and effective judges; false-accept and true-accept rates | Tau = 1 on the labelled anchors; judge qualification on at least 40 known-answer items and 20 order-swap pairs (90% and 85%); false accept at most 5% and true accept at least 80% from a user-run simulation fed with the measured run-level spread, checked on held-out ablation variants (k = 1 should accept; k = 4 and 6 should reject) |
| E-4 | `evals/human_labels.csv` | The user's blind labels of 15 pairs chosen by the protocol (10 near the threshold, 5 known-order ablations) against the panel | Panel majority agrees on at least 12 of 15 non-tie pairs; kappa is reported with its interval for information only |
| E-5 | `scripts/bt_fit.py` and tests | Recovers known strengths from synthetic pairs; handles ties; refuses to extrapolate | Within tolerance on synthetic data |
| E-6 | `scripts/optimize_purchase.py` and tests | At most 3 stores; shipping; quantities; English/Spanish only; condition floor; total including fees within budget; infeasible gives a clear report | Constraints asserted on toy store data |
| E-7 | `scripts/allocate_collection.py` and tests | No physical copy in two decks; singleton per deck; basic lands; locked cards respected | Asserted |
| E-8 | `evals/protocol.yaml` and `evals/judgments/*.jsonl` | Pre-registered runs, judges, models, prompt hash, thresholds, stopping rule, seeds; raw judgment log | A rating refuses to run if the protocol hash changed since calibration |
| E-9 | JSON Schema for `data/stock/*.json` | Store, URL, variant, language, condition, price, quantity, evidence, UTC timestamp | A purchase list is rejected if any line fails or is stale |

Dependencies to add when this code is written: `numpy`, `scipy` (or `choix`), `pulp`;
pin versions at that point.
