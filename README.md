# magic-decks-optimization

Build one new Commander deck and upgrade two existing ones as high inside Bracket 3 as the
budget allows (measured with Commander Salt's power 1-10), using verified real stock in
Chilean stores. The result is a budget curve (100,000 to 300,000 CLP) and a dashboard; the
decks are kept at parity (within 0.2 power points) and the owner picks the budget.

| Deck | Commander | Goal |
|---|---|---|
| New | Alexios, Deimos of Kosmos | Build from scratch |
| Existing | Toph, the First Metalbender | Upgrade |
| Existing | Fire Lord Azula | Upgrade |

## Pipeline
| Phase | What happens | Depends on | Status |
|---|---|---|---|
| Base | Harness (CLAUDE.md, skills, agents, hooks, permissions), research reports, decisions, store list | none | Done (committed 2026-10-11) |
| 0 | Rules snapshot (Wizards' official conditions) | none | Done (2026-10-13). Wizards' official pages were checked after the 2026-10-12 announcement and the 2026-10-13 stream: Competitive Brawl only, no change to the Commander banned list, Brackets or Game Changers; Wizards said a Commander announcement is likely before the end of 2026, so the rules are re-checked at the 2026-11-30 announcement and in the Phase 11 freshness check |
| 1 | Digitize the 2 physical decks and the loose collection | Android phone and a free scanning app | In progress: Toph (10 Spanish cards) and Azula (9 Spanish cards) scanned, exported and validated on 2026-10-12; the inventory builder (`scripts/build_inventory.py`, 5 tests) is ready; the loose collection scan is pending (owner) |
| 2 | Layer A code and golden tests (name resolution, gate, Spellbook) and the card-facts file generator | Phase 1 export format, Phase 0 | Done on 2026-10-14: gate, local Spellbook matcher, curated hazards that follow the same early two-card rule as Spellbook combos (`scripts/layer_a.py`, `data/hazards.json`, 36 tests; 6 golden tests on the real decks, `tests/test_golden_decks.py`), the rules-freshness line (bulk date and Game Changers count against the pinned 53) on every run, and `scripts/check_candidates.py` for the candidate lists; the speed-risk flag was built and retired on 2026-10-13 (Commander Salt replaces it); the deck export validator has 7 tests; independent code review by Haiku 5.5 (26 findings, all 5 blocking fixed; `docs/research/code-review-phase2-*`) |
| 3 | Synergy research per commander (Scryfall and Commander Spellbook data; EDHREC excluded by its terms); can run in parallel with Phase 1 | Phase 0 | Done on 2026-10-12: 3 reports researched, cross-verified and rules-checked against the official rulings (`docs/research/synergy-*`); the open readings were then closed with the Comprehensive Rules text of 2026-09-25 (`docs/research/comprehensive-rules-check-2026-10-12.md`, one reader, not cross-verified) |
| 4 | Candidate menu per commander: real public lists from the Commander Salt commander page (read by hand, one deck at a time), each with its site score and gated by Layer A; plus the Upgrades Meta picks for the owner's two decks. Replaces the agent-built references, slot rankings and ablation ladders (audit of 2026-10-13) | Phase 2 | Done on 2026-10-14 for the first menu: 13 lists in `decks/candidates/` (Alexios 4, Toph 4, Azula 5), 8 pass Layer A at Bracket 3 (Alexios 2 at power 7.2-7.5, Toph 3 at 7.2-7.4, Azula 3 at 7.2-7.4); Meta Staples (Bracket 3 bin) for Toph and Azula. The agent-built Alexios reference is archived in `evals/anchors/` and not used |
| 5 | Repeatability on Commander Salt: the same list scored again on a later day (no ladder, no judge-panel validation, no Ollama) | Phase 4 | Done on 2026-10-14: the owner's Toph link scored 6.5 / bracket 3 / salt 72.4 / pillars 308-202-197-490 on 2026-10-13 and again the same on 2026-10-14 after Import and Refresh; the site's leaderboard rows were stale against deck pages (use the deck page) |
| 6 | Score Toph and Azula on Commander Salt through their ManaBox links (pilot); the owner then picks the cards he keeps | Phase 1 | Done on 2026-10-16: Toph power 6.5, bracket 3; Azula power 4.0, bracket 2 (site version 2026.4195; reports in `decks/reports/`); the owner's 32 must-keep cards (15 from Toph, 17 from Azula) are in `decks/locked.txt`: each must be in at least one of the project's Commander decks (any number of them), free to move between decks within color identity (`decks/locked.md`) |
| 7 | Feasibility: CLP prices, from the catalogs of the stores the owner names (price reading only; stock is verified later), of the cards in each candidate list, Meta pick and lock | Phases 1 and 4, and the store list | In progress (2026-10-16): store reconnaissance done (`docs/research/store-recon-2026-10-16.md`), 8 stores, all with a public JSON feed (Magic4Ever through its own API, found 2026-10-17); `scripts/read_store_prices.py` read Magic4Ever and CardNexus on 2026-10-17, the 6 Shopify stores blocked the Python client (HTTP 429) and are read in the owner's browser by Claude, then merged with `scripts/merge_prices.py` (offline tests for both) |
| 8 | Global allocation across the 3 decks and the budget curve (100,000-300,000 CLP, steps of 50,000, parity within 0.2): one list per deck chosen from the measured candidates and the owner's deck upgraded with Meta picks (PuLP), the final lists scored on Commander Salt; dashboard (Artifact) | Phases 6 and 7 | Pending |
| 9 | Choose stores and collect offers with verified real stock for the Phase 8 shortlist | Phase 8 | Pending (late) |
| 10 | Joint optimization (allocation plus purchase, at most the stores the owner lists, shipping); backtrack when stock fails (at most 5 rounds, each re-scored on Commander Salt) | Phase 9 | Pending |
| 11 | Rules freshness check, Commander Salt score of the frozen lists, stock re-check of the chosen offers within 24 h, pull list (owned cards to take out per deck), the optional token step (tokens and emblems the final decks create that the owner lacks, stock only in stores already in the plan, outside the budget, added only if the owner says yes), purchase by the user, reconciliation (bought versus planned, collection updated). If the score fails: back to Phase 8 once, then the D2 fallback | Phase 10 | Pending |

Status as of 2026-10-14.

## Constraints
- Budget: chosen by the owner from the curve, between 100,000 and 300,000 CLP, only for
  the cards (payment fees count if a store charges them); owned cards are free. Shipping is
  outside the budget (assumed 5,000 CLP per store, reported separately).
- Stores: the owner's 6 Chilean specialist shops in `data/stores.md` (the first 3 by default)
  plus up to 4 more at most, only with excellent reputation evidence, a public JSON stock feed
  and his OK; fewer stores preferred as a tie-break; all prices in CLP, no conversion.
- Free tools only: no paid apps or subscriptions (an exception needs the user's approval).
- Cards to buy: English or Spanish printings only, the cheaper one preferred; at the same price, Spanish.
- Collection: mixed Spanish and English cards; the 2 decks are sleeved; scanning is done
  from an Android phone.
- Every card to buy needs verified real stock at decision time.
- The user makes every purchase.

## Power scale
Since 2026-10-13 the yardstick is Commander Salt's: **power 1-10** (casual below 5, upgraded casual
5-6.49, mid 6.5-7.59, high 7.6-8.99, cEDH from 9) and its decimal bracket. The goal is the highest
power the budget buys for each deck, at parity, every deck above the 6.1 of the owner's friend's
deck. All three decks target Bracket 3; only Wizards' official conditions limit a deck (Layer A).
See [docs/proposals/commandersalt-adoption.md](docs/proposals/commandersalt-adoption.md); how it is measured is in [docs/power-scale.md](docs/power-scale.md).

## Research
| Report | Topic |
|---|---|
| [commander-brackets-rules-snapshot](docs/research/commander-brackets-rules-snapshot.md) | Official bracket rules, Game Changers, Commander Spellbook API, MCP landscape |
| [mtg-collection-scanning-on-android](docs/research/mtg-collection-scanning-on-android.md) | Free Android scanners, Spanish cards, export formats, pilot test, workflow |

## Credits
- Combo data and bracket tags: [Commander Spellbook](https://commanderspellbook.com), read
  from its published bulk file `variants.json.gz`.
- Card data and rulings: [Scryfall](https://scryfall.com) bulk data. Card text and the
  Comprehensive Rules are Wizards of the Coast's.

## Setup
The conda environment is created in conda's default location; only `requirements.txt`
lives in the repo.

```
conda create -n magic-decks python=3.12
conda activate magic-decks
pip install -r requirements.txt
```

## Working with Claude Code
Project rules live in [CLAUDE.md](CLAUDE.md). Skills (user-invoked): `rate-deck`,
`check-stock`, `build-deck`. Subagent: `stock-verifier`.

## Git hygiene
Commits must use the personal identity. After cloning, enable the repo hook (it is
bypassed by `git commit --no-verify`):

```
git config --local core.hooksPath .githooks
```

The hook that keeps Claude's git read-only is tested with
`sh evals/run_hook_cases.sh .claude/hooks/block-git-writes.sh evals/hook_cases.tsv`
(140 cases, expect `failures=0`).
