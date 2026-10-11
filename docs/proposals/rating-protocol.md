# Rating protocol (proposal v2, needs the user's decisions)

Status: draft proposal, revised on 2026-10-10 after a second independent review (method,
statistics, plan). Nothing here is in force until the user accepts it. It replaces the
acceptance rule of power-scale v0.2, which an earlier review found unsound. All numeric
thresholds below are placeholders until Phase 5 measures the run-to-run spread, the
censoring rate and the anchor separation; none may be frozen before that.

## Why the old acceptance rule was withdrawn
| Problem | Evidence |
|---|---|
| Judges from the same provider make correlated errors, so a within-run interval is far too narrow | Kim et al., ICML 2025 ([arXiv 2506.07962](https://arxiv.org/abs/2506.07962)): correlated errors across 350+ LLMs, partly from shared providers and even among large accurate models from different providers. A May 2026 single-author preprint (v1, not peer reviewed) finds 9 judges from 7 families give about 2 independent votes, and its best single judge matched or beat the panel ([arXiv 2605.29800](https://arxiv.org/abs/2605.29800)) |
| Shared bias (leniency, self-preference, position bias) is invisible to variance checks | [Thakur et al.](https://arxiv.org/abs/2406.12624), [Panickssery et al.](https://arxiv.org/abs/2404.13076), [Zheng et al.](https://arxiv.org/abs/2306.05685), [Shi et al.](https://arxiv.org/abs/2406.07791) (position bias grows as the quality gap narrows, so it is worst near a threshold). With a few ground-truth labels, debiasing a judge at most halves the labels needed when the judge is no more accurate than what it evaluates ([Dorner et al.](https://arxiv.org/abs/2410.13341), ICLR 2025) |
| A within-run interval misses run-level shared error, and a constant bias is invisible to variance checks | Analytic. Illustrated on the withdrawn absolute-score rule (judge SD 0.8, 0.5 grid clipped to [1, 9], within-run correlation 0 or 0.5, fixed panels of 6, 12 or 24, 400 trials): bootstrap half-width 0.22 to 0.34, yet two runs differed by more than 0.5 in 30 to 43% of trials; a 7.5 deck with a shared +1 bias is the same as an unbiased 8.5 deck, accepted 81% and 82% of the time. Optional stopping was not simulated and the new protocol has not been simulated |
| Judges had no card text and could read the target | The judge tools were Read, Grep and Glob over name-only lists, the spec held "3.9" and the thresholds, and custom subagents load CLAUDE.md. Fixed in v2: judges omit CLAUDE.md and have only Read, and acceptance runs use an isolated packet (step 2) |
| Absolute `y_estimate` per lens is not a reliability statistic | Six lenses measure six constructs; their spread is the deck's profile, not error |

## Proposed protocol
1. **Frozen, hashed inputs.** Candidate list with names canonicalized to Scryfall oracle
   IDs; card-facts file; anchor ladder for the commander; `evals/judge_rubric.md`; frozen
   prompt templates and their paraphrases (generated and hashed in Phase 5); resolved model
   IDs; rules snapshot hash.
2. **Judgment unit.** One fresh context judges one ordered pair (candidate versus one
   anchor), random order, anonymized IDs, from a packet outside the repo (`A.txt`, `B.txt`,
   `facts.json`, `rubric.md`) with no CLAUDE.md loaded. Every Read path is logged and a
   judgment that read anything else is discarded. Output: winner A, B or tie, lens notes,
   unknowns, leaks. A judgment with non-empty `unknowns` or `leaks` is discarded and logged;
   a run with more than 10% discarded judgments is void. In-session subagents are for
   development only; acceptance runs use the user-run runner (see Execution).
3. **Run.** J judges (composition = mixed models, weighted toward the strongest; every
   judgment has equal weight in the fit). Each compares the candidate with every labelled
   anchor in both orders. Anchor-versus-anchor judgments are collected in at least R
   independent replicates per anchor set and model version, and each run uses a different
   replicate, so the anchors' placement error enters the between-run spread.
4. **Fit per run.** Bradley-Terry with ties (Davidson), by maximum likelihood, not Elo
   ([Boubdir et al.](https://arxiv.org/abs/2311.17295); [Chiang et al.](https://arxiv.org/abs/2403.04132);
   Davidson, JASA 65:317-328, 1970, reference not re-verified). Only labelled anchors (the
   Y = 9 reference and the ablation ladder) enter the order check and the mapping; EDHREC
   decks are unlabelled diagnostics. A run is valid only if the fitted strengths of the
   labelled anchors fall strictly as k rises (Kendall tau = 1; with 5 labelled anchors
   tau >= 0.8 would allow one swapped pair and break a monotone mapping), adjacent anchors
   differ by at least a minimum gap set in Phase 5, and the guard probes pass. Map the
   candidate's strength to Y by monotone piecewise-linear interpolation between labelled
   anchors. Above the top anchor record 9.0 and flag the run as censored; below the bottom
   anchor record the bottom label and flag it. If more than one run is censored, report
   "censored" and use `s_used = max(s, s_cal)`, where `s_cal` is the between-run SD
   measured in Phase 5. Never extrapolate.
5. **Repeat R runs**, fixed in advance (start with 4). Each run uses fresh contexts, a
   paraphrased prompt and a new anchor order. Y is the mean of the run values, the spread
   `s` is their standard deviation, and the one-sided lower bound is
   `Y - t(0.90, R-1) * s / sqrt(R)` (margin 0.82 s for R = 4, 0.50 s for R = 8).
6. **Bracket-fit review** (see below) runs on the frozen candidate; it is a separate
   condition, not part of Y.
7. **Accept 3.9 only if** Layer A floor is 3 or less with no flag implying 4, the
   bracket-fit review passes, Y is at least 8.5 with a lower bound of at least 8.0, the
   list is frozen, and one fresh confirmation run gives Y at least 8.0. "Inconclusive" means
   Y at least 8.5 with a bound below 8.0; one pre-declared extra batch of R runs is allowed
   once, pooled with the first batch (2R runs, t(0.95, 2R-1)). The test panel (held-out
   paraphrases and ablation variants, frozen in Phase 5) rates each deck at most twice over
   the whole project, and every submission is logged, including failures; all iteration
   uses the dev panel. A re-roll after changing one card counts as a new submission.
8. **Report** Y, s, R, J, the intraclass correlation of judge errors, the effective number
   of judges `J / (1 + (J - 1) * ICC_err)` (never more than `1 / ICC_err`), model IDs,
   hashes, censoring flags and per-lens diagnostics.
9. **What "deterministic" means here.** Individual judge calls are not deterministic. Raw
   judgments are logged to JSONL and aggregation uses fixed seeds, so the same logs always
   give the same Y. The estimate converges as runs are added, but only to the panel's value,
   bias included; only anchors and human labels correct that. Y is "consensus deck quality
   as the panel perceives it", not a win rate.

### What the numbers mean
| Quantity | Value |
|---|---|
| 95% two-sided half-width `t * s / sqrt(R)`, s = 0.3 | 0.48 (R = 4), 0.25 (R = 8) |
| same, s = 0.5 | 0.80 (R = 4), 0.42 (R = 8) |
| One-sided 90% lower-bound margin | 0.82 s (R = 4), 0.50 s (R = 8) |
| s at which "bound >= 8.0" binds when Y = 8.5 | 0.61 (R = 4), 1.00 (R = 8) |
| P(accept) when the panel's true value is 8.5 | about 45% (so the effective pass mark is about 8.75) |
| P(a run is censored at 9) when the value is 8.75 and s = 0.5 | about 31% |

Measure `s` in the evals before freezing any threshold.

## Anchors per commander
| Anchor | How it is made | Role |
|---|---|---|
| Y = 9 reference | A no-budget best Bracket 3 list that passes the bracket-fit review; the user signs it off (D12) | Top of the scale |
| Ablation ladder | The reference with its best k non-land slots replaced, nested, for k in {2, 4, 6, 10, 20} (add 30 if the current decks must be placed). Labels `Y = 9 - k/4`; the constant is fixed for all commanders before Phase 5 and never changed after a candidate is seen (D11) | Known order without any LLM; k = 2 sits at 8.5 and k = 4 at 8.0 |
| EDHREC user-labelled Bracket 3 average deck | Public data for the same commander (D7) | Unlabelled diagnostic |
| EDHREC user-labelled Bracket 4 average deck | Same | Known-answer probe of the bracket-fit review (judges must call it Bracket 4); never a strength anchor, never in the Y fit |
| User labels | The user blind-labels 15 pairs (D8) | A human reference standard; cannot be replaced |

Ladder rules: best slots are ranked once by a fixed rule (Game Changers first, then by the
USD price of the cheapest legal printing from Scryfall `default-cards`), and the user signs
off the ranking with the reference. Each replacement is the cheapest card with the same role
tag that is not already in the list, and the user confirms each is a downgrade. The
reference and all ablations share a budget-capped mana base (rule fixed in Phase 4), or
lands enter the ranking; otherwise a no-budget three-color mana base pushes every budget
candidate down and can make 3.9 unreachable by construction. Phase 5 must show that judges
tell k = 0 from 2, and 2 from 4, at least 70% in both orders; otherwise the acceptance
thresholds widen to the smallest gap they resolve. Current Toph and Azula lists will
probably land below the k = 20 anchor; report "below 4" from a cheap check against that
anchor alone, or add the k = 30 anchor.

## Bracket-fit review (proposed, D10)
K at least 3 isolated judges, then the user, each answer for the candidate alone: "Bracket
3 or 4 under Wizards' expectation text (snapshot 2026-02-09)?" with a checklist: (1) the role
of each Game Changer (Bracket 3: value engine or game-ending spell; Bracket 4: fast mana,
snowballing engine, free disruption, tutor); (2) whether the deck tends to end the game, or
assemble a two-card combo, before its own turn 7; (3) stax, lock or "tricked-out" patterns.
Pass = a Bracket 3 majority in every run and the user agrees. Decision D3 (the informational
turn-7 flag) feeds item (2).

## Guards against a judge that just agrees
Judges are qualified once per model version in Phase 5 on at least 40 known-answer items
(ablation gap k at least 10, both orders) and at least 20 order-swap pairs: pass at 90%
known-answer accuracy and 85% order consistency, a tie counting as wrong on known-answer
items, and consistency meaning the same deck (or a tie) in both orders. Per-run checks catch
only gross failure: per judge per run at least 8 of 10 known-answer items; a failing judge's
judgments are dropped and logged, and a run is void if fewer than J - 1 judges remain.
Placebo (the same deck under two IDs should tie), label-leak probe (the same deck named
`final_3.9` versus `deck_17`), discrimination slope and intra-run versus across-run ICC are
assessed over Phase 5, not per run. Context canary: asked to quote any project goal, target
or threshold it can see, a judge returns none. Debate is used only to settle disputes about
card text and post-debate scores never enter the statistic. The builder and the judges are
the same model family, so build against a development panel and accept only with a
separate, frozen test panel; this reduces, but does not remove, shared misjudgments. The
Agent tool offers only Anthropic models, so "mixed models" does not mean mixed families.

## Execution
- A user-run runner (`scripts/run_panel.py`, to be written) calls headless Claude Code once
  per judgment from an empty working directory with tools disabled and the frozen
  template (hash in `evals/protocol.yaml`). It writes raw responses to
  `evals/judgments/<rating-id>.jsonl` with model ID and prompt hash, then fits
  Bradley-Terry to `<rating-id>.fit.json`. Claude reads the fit and writes the report.
- Calls per rating: `(R + 1) * J * (2A + P)` with A labelled anchors and P probe pairs
  per judge (J = 6, A = 7, P = 14, R = 4 gives 840), plus 672 for an extra batch, plus
  `J * A * (A - 1)` per anchor set (252). Roughly 17M input tokens per rating (estimate).
- A PostToolUse hook on the Agent tool could append each in-session judge's output to the
  JSONL deterministically; this is untested (to verify with the Claude Code docs).
- The offline Bradley-Terry fit is a script the user runs (execution boundary in
  CLAUDE.md), or the user lets Claude run it as a `pytest`-style offline step (D13).

## Decisions for the user
| ID | Decision | Recommended default |
|---|---|---|
| D1 | Is Y measured relative to each commander (Y = 9 is that commander's no-budget Bracket 3 reference)? Y is comparable across commanders only through the global ablation constant, read as "k-equivalent best slots" | Yes. Alexios's owner controls it only from their own upkeep until the next player's upkeep, since each player gains control at the beginning of their upkeep (oracle text); an absolute scale would mix commander strength with build quality (inference) |
| D2 | Project goal: replace "nothing is bought before all 3 are 3.9" with a purchase objective: maximize the minimum surrogate `Y_hat` over the 3 decks (surrogate from the ablation ranking, for example `9 - c * k_eq`, defined in Phase 8), tie-break by the sum, then by lowest cost; subject to checkout total <= 200,000 CLP, <= 3 stores, verified stock, Layer A floor <= 3 and a passing bracket-fit review. Acceptance: panel Y >= F for every deck, with F set by the user. If the optimum is below F: report the gap and offer a lower common floor, deferring one deck, or a second purchase window. The panel cannot score every candidate purchase set, which is why the optimizer uses the surrogate | Yes. The whole budget is about USD 204 (981.61 CLP/USD, 2026-10-09) for three decks, while 22 of the 51 Game Changers that fit our colors cost over USD 40 at their cheapest printing (Scryfall, 2026-10-10), so a budget-free ceiling can deadlock the project. Chilean CLP prices decide the real cost |
| D3 | Add an informational, non-gating flag "threatens lethal before its own turn 7"? | Yes: information for Y, and an input to the bracket-fit review; speed stays out of Y and out of the gate |
| D4 | Adopt the pairwise plus Bradley-Terry plus R-runs protocol above, with its gates, censoring and execution rules | Yes |
| D5 | "Owned cards first": owned cards cost 0 and act as a tie-breaker; a locked-cards file per deck (who writes it, and when, is open). Moves between decks are handled by the global allocation (each physical copy in at most one deck) with no extra cost term | Yes |
| D6 | Printing and budget policy: any legal English or Spanish printing and finish, condition near mint to lightly played, no proxies; budget = final checkout totals including shipping and any payment fees; sleeves and accessories outside the budget; no selling or trading. Are owned Spanish copies acceptable in the final decks? | Yes |
| D7 | May EDHREC's undocumented JSON endpoints be used (cached, rate-limited, as untrusted data)? Blocks the EDHREC anchors in Phase 4; the fallback is that the user copies the lists by hand | Decide in the synergy phase after reading its terms |
| D8 | Human labels: 15 pairs chosen by the protocol, not the builder: 10 candidate-versus-anchor pairs near the threshold and 5 known-order ablation pairs (these measure the user's own accuracy); decks the user owns are excluded. Pass: the panel majority agrees with the user on at least 12 of 15 non-tie pairs (agreements needed by number of non-tie pairs: 10 needs 9, 12 needs 10, 13 needs 10, 14 needs 11). Kappa is reported with its interval for information only (10 to 15 labels give about +-0.40 to 0.50; +-0.25 needs about 40) | Yes; the labels are a human reference standard, not ground truth |
| D9 | Stock verifier model: Sonnet instead of Haiku, because it reads untrusted pages in the user's real browser. Applied as `model: sonnet`; confirm, switch to Opus, or revert | Confirm Sonnet |
| D10 | Approve the bracket-fit review procedure above (K judges plus the user) and its place as a separate acceptance condition | Yes |
| D11 | The ablation constant `c` (default 1/4), the k values and whether anchors sit exactly at 8.5 and 8.0; fixed globally before Phase 5 | Yes, k in {2, 4, 6, 10, 20} |
| D12 | The Y = 9 reference: who builds it, the sign-off criteria, whether it must beat a human-built high-power Bracket 3 list, the budget-capped mana-base rule, and what happens if a candidate rates "at least 9" | Claude drafts, the user signs |
| D13 | How judges run: in-session subagents (development only) versus a user-run headless runner (acceptance); may Claude run the offline Bradley-Terry fit? | Runner for acceptance |
| D14 | The test panel's composition, the submission cap, and whether a cross-family free-tier judge is allowed under "free tools only" | Same-family only unless the user allows otherwise |
| D15 | Rules policy: "rules in force on the purchase date"? Hold Phase 4 until the re-check after the 2026-10-12 announcement? | Yes to both |
| D16 | Price model inputs for Phase 7: the exchange-rate source and date (Banco Central dólar observado), a CLP store multiplier from a price-only store sample, a shipping model, whether each MercadoLibre seller counts as one store, and pickup or shipping and which city | The user decides when Phase 7 starts |
