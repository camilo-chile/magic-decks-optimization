# Rating protocol (v3, decisions recorded)

Status: revised on 2026-10-11 after the user's answers to the second review. The goal and
the main policies are now decided (table at the end). Numeric thresholds below are
placeholders until Phase 5 measures the run-to-run spread, the censoring rate and the anchor
separation; none may be frozen before that.

## What the protocol must deliver
1. A **budget curve**: for each budget from 100,000 to 300,000 CLP (steps of 50,000), the 3
   decks built together at parity (within 0.2 points, maximizing the lowest), with their
   level and an uncertainty band.
2. An honest statement of what Y is: the consensus of a panel of language models relative
   to reference decks. The user does not rate decks and no public ground truth for Y inside a
   bracket exists.

## Why the old acceptance rule was withdrawn
| Problem | Evidence |
|---|---|
| Judges from the same provider make correlated errors, so a within-run interval is far too narrow | Kim et al., ICML 2025 ([arXiv 2506.07962](https://arxiv.org/abs/2506.07962)): correlated errors across 350+ LLMs, partly from shared providers and even among large accurate models from different providers. A May 2026 single-author preprint (v1, not peer reviewed) finds 9 judges from 7 families give about 2 independent votes, and its best single judge matched or beat the panel ([arXiv 2605.29800](https://arxiv.org/abs/2605.29800)) |
| Shared bias (leniency, self-preference, position bias) is invisible to variance checks | [Thakur et al.](https://arxiv.org/abs/2406.12624), [Panickssery et al.](https://arxiv.org/abs/2404.13076), [Zheng et al.](https://arxiv.org/abs/2306.05685), [Shi et al.](https://arxiv.org/abs/2406.07791) (position bias grows as the quality gap narrows). With a few ground-truth labels, debiasing a judge at most halves the labels needed when the judge is no more accurate than what it evaluates ([Dorner et al.](https://arxiv.org/abs/2410.13341), ICLR 2025) |
| A within-run interval misses run-level shared error, and a constant bias is invisible to variance checks | Analytic. Illustrated on the withdrawn absolute-score rule (judge SD 0.8, 0.5 grid clipped to [1, 9], within-run correlation 0 or 0.5, fixed panels of 6, 12 or 24, 400 trials): bootstrap half-width 0.22 to 0.34, yet two runs differed by more than 0.5 in 30 to 43% of trials; a 7.5 deck with a shared +1 bias is the same as an unbiased 8.5 deck, accepted 81% and 82% of the time. The new protocol has not been simulated |
| Judges had no card text and could read the target | Fixed: judges omit CLAUDE.md, have only Read, and acceptance runs use an isolated packet |
| Absolute `y_estimate` per lens is not a reliability statistic | Six lenses measure six constructs; their spread is the deck's profile, not error |

## The panel
8 judges, equal weight in the fit:

| Judges | Model | Note |
|---|---|---|
| 3 | Opus 5.5 | |
| 3 | Sonnet 5.5 | |
| 1 | Haiku 5.5 | Most likely to be dropped by qualification |
| 1 | Qwen3.8 27B, local | `qwen3.8:27b` in Ollama (Q4_K_M, about 17 GB, Apache 2.0; fits a 24 GB RTX 3090). A different family, so its errors correlate less with the rest. Called by the user-run runner through Ollama's local API |

Every judge must pass the qualification test (below); a judge that fails is dropped and
logged. The local model is never used where it is not measured to help; it is not a builder
or a stock verifier.

## Proposed protocol
1. **Frozen, hashed inputs.** Candidate list with names canonicalized to Scryfall oracle
   IDs; card-facts file; anchor ladder for the commander; `evals/judge_rubric.md`; frozen
   prompt templates and paraphrases (generated and hashed in Phase 5); resolved model IDs
   (for the local model, the Ollama digest); rules snapshot hash.
2. **Judgment unit.** One fresh context judges one ordered pair (candidate versus one
   anchor), random order, anonymized IDs, from a packet outside the repo (`A.txt`, `B.txt`,
   `facts.json`, `rubric.md`) with no CLAUDE.md loaded. Every Read path is logged and a
   judgment that read anything else is discarded. Output: winner A, B or tie, lens notes,
   unknowns, leaks. A judgment with non-empty `unknowns` or `leaks` is discarded and logged;
   a run with more than 10% discarded judgments is void.
3. **Run.** Each judge compares the candidate with every labelled anchor in both orders.
   Anchor-versus-anchor judgments are collected in at least R independent replicates per
   anchor set and model version, and each run uses a different replicate, so the anchors'
   placement error enters the between-run spread.
4. **Fit per run.** Bradley-Terry with ties (Davidson), by maximum likelihood, not Elo
   ([Boubdir et al.](https://arxiv.org/abs/2311.17295); [Chiang et al.](https://arxiv.org/abs/2403.04132);
   Davidson, JASA 65:317-328, 1970, reference not re-verified). Only labelled anchors (the
   Y = 9 reference and the ablation ladder) enter the order check and the mapping; community
   decks are unlabelled diagnostics. A run is valid only if the fitted strengths of the
   labelled anchors fall strictly as k rises (Kendall tau = 1), adjacent anchors differ by at
   least a minimum gap set in Phase 5, and the guard probes pass. Map the candidate's
   strength to Y by monotone piecewise-linear interpolation between labelled anchors. Above
   the top anchor record 9.0 and flag the run as censored; below the bottom anchor record the
   bottom label and flag it. If more than one run is censored, report "censored" and use
   `s_used = max(s, s_cal)`, where `s_cal` is the between-run SD measured in Phase 5. Never
   extrapolate.
5. **Repeat R runs**, fixed in advance. Each run uses fresh contexts, a paraphrased prompt
   and a new anchor order. Y is the mean of the run values, the spread `s` is their
   standard deviation, and the one-sided lower bound is `Y - t(0.90, R-1) * s / sqrt(R)`
   (margin 0.82 s for R = 4, 0.50 s for R = 8).
6. **Bracket-fit review** (see below) runs on every frozen candidate; it is a separate
   condition, not part of Y.
7. **Eligibility at a budget point.** Layer A floor 3 or less with no flag implying 4, the
   bracket-fit review passes, the list is frozen, and one fresh confirmation run gives a Y
   within the band of the first batch. The test panel (held-out paraphrases and ablation
   variants, frozen in Phase 5) rates each final list at most twice, and every submission
   is logged, including failures; all iteration uses the dev panel. A re-roll after changing
   one card counts as a new submission.
8. **Report** Y, s, R, J, the intraclass correlation of judge errors, the effective number
   of judges `J / (1 + (J - 1) * ICC_err)` (never more than `1 / ICC_err`), model IDs,
   hashes, censoring flags and per-lens diagnostics.
9. **Determinism.** Individual judge calls are not deterministic. Raw judgments are logged
   to JSONL and aggregation uses fixed seeds, so the same logs always give the same Y.

### Cost tiers (accuracy first, but the usage limit is real)
| Tier | Used for | What | Calls |
|---|---|---|---|
| 0 | Every candidate | Layer A (deterministic code) and the speed-risk simulation | none |
| 1 | Every budget point | Surrogate level `Y_hat` from the optimizer, computed from the ablation ranking (a script, not a model) | none |
| 2 | 2-3 checkpoints of the curve, during iteration | Reduced panel: J = 4 (2 Opus, 2 Sonnet), A = 5, P = 6, R = 2 | (R+1) * J * (2A+P) = 192 |
| 3 | The lists the user will actually consider | Full panel: J = 8, A = 7, P = 14, R = 4 | 1,120, of which 140 are local |

The runner writes each judgment to JSONL as it goes and resumes after an interruption, so a
usage limit only pauses it. Anchor sets add `J * A * (A - 1)` calls once per model version.

### What the numbers mean
| Quantity | Value |
|---|---|
| 95% two-sided half-width `t * s / sqrt(R)`, s = 0.3 | 0.48 (R = 4), 0.25 (R = 8) |
| same, s = 0.5 | 0.80 (R = 4), 0.42 (R = 8) |
| One-sided 90% lower-bound margin | 0.82 s (R = 4), 0.50 s (R = 8) |
| Level differences below the measured `s` | shown as "not distinguishable" on the curve |

Measure `s` in the evals before freezing any threshold.

## The budget curve
1. Inputs per budget B: owned cards at cost 0, CLP catalog prices of the user's stores,
   shipping per store as a fixed cost, the 7 stores in `data/stores.md` with their
   preference order as a tie-break.
2. The optimizer is an integer program (a solver), not a language model. It maximizes the
   lowest surrogate `Y_hat` over the 3 decks, then the sum, then minimizes cost, subject to
   the checkout total <= B (shipping included, which penalizes extra stores), verified
   stock, Layer A floor <= 3,
   each physical copy in one deck only, locked cards kept, and parity within 0.2.
3. Tier 2 or 3 ratings validate selected points; the curve shows the surrogate with the
   panel results as marked points.
4. The final output is a dashboard (an Artifact) with the curve, the three decks, the cards
   to buy per budget point, the store split and the evidence timestamps. A mock-up with
   example data comes only after real data exists.

## Anchors per commander
| Anchor | How it is made | Role |
|---|---|---|
| Y = 9 reference | A no-budget best Bracket 3 list drafted by Claude. Accepted by criteria, not by the user: passes Layer A and the bracket-fit review, and wins the panel comparison against the community's Bracket 3 average deck | Top of the scale |
| Ablation ladder | The reference with its best k non-land slots replaced, nested, for k in {2, 4, 6, 10, 20} (add 30 if the current decks fall below). Labels `Y = 9 - k/4`; the constant is fixed for all commanders before Phase 5 and never changed after a candidate is seen | Known order without any LLM; k = 2 sits at 8.5 and k = 4 at 8.0 |
| Community Bracket 3 average deck (EDHREC or similar) | Public data for the same commander (read through a cached script after reading the site's terms) | Unlabelled diagnostic |
| Community Bracket 4 average deck | Same | Known-answer probe of the bracket-fit review (judges must call it Bracket 4); never in the Y fit |
| Public decks with a bracket label by their authors | Moxfield, Archidekt and similar, where the author chose the bracket | Coarse human labels (Bracket 3 versus 4) for the probes; self-reported, so used for discrimination only, not for Y |

Ladder rules: best slots are ranked once by a fixed rule (Game Changers first, then by
community inclusion rate for that commander); each replacement is the card with the same
role tag that has the lowest inclusion rate and is not already in the list. No prices are
used for the ladder, so no currency enters here. The reference and all ablations share the
same mana-base rule (fixed in Phase 4), or lands enter the ranking. Phase 5 must show that
judges tell k = 0 from 2, and 2 from 4, at least 70% in both orders; otherwise the
thresholds widen to the smallest gap they resolve. The current Toph and Azula lists will
probably land below the k = 20 anchor; report "below 4" from a cheap check against that
anchor alone, or add the k = 30 anchor.

## Bracket-fit review
At least 3 isolated judges (not the user) each answer for the candidate alone: "Bracket 3 or
4 under Wizards' expectation text (snapshot 2026-02-09)?" with a checklist: (1) the role of
each Game Changer (Bracket 3: value engine or game-ending spell; Bracket 4: fast mana,
snowballing engine, free disruption, tutor); (2) the speed-risk flag; (3) stax, lock or
"tricked-out" patterns. Pass = a Bracket 3 majority in every run and a speed-risk flag
below `high`.

## Speed-risk simulation
A Monte Carlo goldfish script (`scripts/speed_risk.py`, to be written, run by the user):
shuffle the 100 cards, draw an opening hand with a fixed mulligan rule, play lands and mana
rocks, and count how often a known win line (Spellbook combos for the deck, or enough
commander damage or other burst the script models) is castable by turn 6. It reports a
frequency used only to place the deck in one of 5 bands (0-10%, 10-20%, 20-30%, 30-40%, 40% or more); it does not model opposing
interaction, so it is an upper-ish bound and an order of magnitude. Lines it cannot model
are listed as "not simulated".

## Guards against a judge that just agrees
Judges are qualified once per model version in Phase 5 on at least 40 known-answer items
(ablation gap k at least 10, both orders) and at least 20 order-swap pairs: pass at 90%
known-answer accuracy and 85% order consistency, a tie counting as wrong on known-answer
items, and consistency meaning the same deck (or a tie) in both orders. Per-run checks
catch only gross failure: per judge per run at least 8 of 10 known-answer items; a failing
judge's judgments are dropped and logged, and a run is void if fewer than J - 1 judges
remain. Placebo (the same deck under two IDs should tie), label-leak probe (the same deck
named `final_3.9` versus `deck_17`), discrimination slope and intra-run versus across-run
ICC are assessed over Phase 5, not per run. Context canary: asked to quote any project
goal, target or threshold it can see, a judge returns none. Debate settles only disputes
about card text and post-debate scores never enter the statistic. The builder and most
judges are the same model family, so build against a development panel and accept only with
a separate, frozen test panel; this reduces, but does not remove, shared misjudgments.

## Execution
- A user-run runner (`scripts/run_panel.py`, to be written) calls headless Claude Code once
  per judgment from an empty working directory with tools disabled, and the local judge
  through Ollama's HTTP API on localhost, using the frozen template (hash in
  `evals/protocol.yaml`). It writes raw responses to `evals/judgments/<rating-id>.jsonl`
  with model ID and prompt hash, then fits Bradley-Terry to `<rating-id>.fit.json`. Claude
  reads the fit and writes the report. In-session subagents are for development only.
- Installing Ollama and pulling the model is done by the user, step by step, manually.
- The offline Bradley-Terry fit and the optimizer are scripts the user runs (execution
  boundary in CLAUDE.md).

## Decisions
### Decided by the user (2026-10-11)
| ID | Decision |
|---|---|
| D1 | Y is relative to each commander |
| D2 | Goal is the budget curve at parity within 0.2 points, 100,000 to 300,000 CLP in steps of 50,000; the user then chooses |
| D3 | Speed is a qualitative 5-level risk flag from a Monte Carlo script (order of magnitude); `high` or more means probable Bracket 4 intent |
| D4 | Pairwise judgments, Bradley-Terry and several runs |
| D5 | Owned cards cost 0; one physical copy goes to one deck only; a locked-cards file per deck, chosen in Phase 6 after the current decks are rated |
| D6 | Any legal English or Spanish printing and finish, condition near mint to lightly played, no proxies, owned Spanish copies fine; budget counts checkout totals including shipping and any payment fees; sleeves and accessories outside the budget; no selling or trading |
| D7 | EDHREC data through a small cached script, after reading its terms (no MCP: none official, community ones abandoned) |
| D8 | The user does not label decks; internet sources and ablations replace human labels |
| D9 | Stock verifier on Haiku 5.5; if it does not give good results, move to Sonnet 5.5 (measured on about 20 cards of known state) |
| D10 | Bracket-fit review by the panel only |
| D14 | Any Anthropic model plus the local `qwen3.8:27b` as a judge, only if it passes qualification; Ollama, manual install |
| D15 | Wait for the 2026-10-12 rules announcement before Phase 4 |
| D16 | Everything in CLP from the 7 Chilean specialist stores in `data/stores.md` (preference order given); no conversion. No fixed store cap: shipping is a fixed cost per store inside the optimizer, and fewer stores are preferred; the first 3 are the default |
| D17 | Speed-risk bands: 0-10%, 10-20%, 20-30%, 30-40%, 40% or more (very low to very high); `high` or more fails the bracket-fit review |

### Set by default (the user may override)
| ID | Default |
|---|---|
| D11 | Ablation constant 1/4 and k in {2, 4, 6, 10, 20} |
| D12 | The Y = 9 reference is drafted by Claude and accepted by the criteria above |
| D13 | Official ratings run through the user-run script; development ratings in the chat |

### Still open
| ID | Question | When |
|---|---|---|
| O1 | Whether the stores expose a product JSON that a script can read, and each store's shipping rule and payment fees (read-only, from the stores' own pages; needs the owner's go-ahead) | Before Phase 7 |
| O2 | Which cards of Toph and Azula are locked (a step after the first rating, Phase 6) | Phase 6 |
