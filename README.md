# magic-decks-optimization

Build one new Commander deck and upgrade two existing ones as high inside Bracket 3 as the
budget allows ("3.9" is the top of a custom power scale), using verified real stock in
Chilean stores. The result is a budget curve (100,000 to 300,000 CLP) and a dashboard; the
decks are kept at parity (within 0.2 points) and the owner picks the budget.

| Deck | Commander | Goal |
|---|---|---|
| New | Alexios, Deimos of Kosmos | Build from scratch |
| Existing | Toph, the First Metalbender | Upgrade |
| Existing | Fire Lord Azula | Upgrade |

## Pipeline
| Phase | What happens | Depends on | Status |
|---|---|---|---|
| Base | Harness (CLAUDE.md, skills, agents, hooks, permissions), research reports, decisions, store list | none | Done (committed 2026-10-11) |
| 0 | Rules snapshot and draft power scale | none | Done (2026-10-13). Wizards' official pages were checked after the 2026-10-12 announcement and the 2026-10-13 stream: Competitive Brawl only, no change to the Commander banned list, Brackets or Game Changers; Wizards said a Commander announcement is likely before the end of 2026, so the rules are re-checked at the 2026-11-30 announcement and in the Phase 11 freshness check |
| 1 | Digitize the 2 physical decks and the loose collection | Android phone and a free scanning app | In progress: Toph (10 Spanish cards) and Azula (9 Spanish cards) scanned, exported and validated on 2026-10-12; the inventory builder (`scripts/build_inventory.py`, 5 tests) is ready; the loose collection scan is pending (owner) |
| 2 | Layer A code and golden tests (name resolution, gate, Spellbook) and the card-facts file generator | Phase 1 export format, Phase 0 | Done on 2026-10-12: gate, local Spellbook matcher, curated hazards (`scripts/layer_a.py`, `data/hazards.json`, 35 tests; 6 golden tests on the real decks, `tests/test_golden_decks.py`) and speed flag (`scripts/speed_risk.py`, 9 tests); the deck export validator has 7 tests; independent code review by Haiku 5.5 (26 findings, all 5 blocking fixed; `docs/research/code-review-phase2-*`) |
| 3 | Synergy research per commander (Scryfall and Commander Spellbook data; EDHREC excluded by its terms); can run in parallel with Phase 1 | Phase 0 | Done on 2026-10-12: 3 reports researched, cross-verified and rules-checked against the official rulings (`docs/research/synergy-*`); the open readings were then closed with the Comprehensive Rules text of 2026-09-25 (`docs/research/comprehensive-rules-check-2026-10-12.md`, one reader, not cross-verified) |
| 4 | Reference builds and anchor ladders per commander; accepted by the criteria of D12, not by the user | Phases 2 and 3, decisions D7, D10-D12, the rules re-check after 2026-10-12 | In progress (2026-10-12): pilot on Alexios done: reference built with no caps of its own (Sonnet 5.5 high), independently reviewed (Haiku 5.5 xhigh, PASS WITH FIXES, fixes applied; `docs/research/review-alexios-reference-2026-10-12.md`), anchors under `evals/anchors/`; the ablation ladder script `scripts/build_ablation_ladder.py` (5 tests) waits to be run; Toph and Azula follow |
| 5 | Calibrate on Commander Salt (replaces the judge-panel validation; no Ollama): score the reference and its ablation rungs, check the order and the stability | Phases 2 and 4 | Pending |
| 6 | Score Toph and Azula on Commander Salt through their ManaBox links (pilot); the owner then picks the cards of each deck to lock | Phase 1 | Pending |
| 7 | Feasibility: price the reference lists minus owned cards, in CLP, from the catalogs of the stores the owner names (price reading only; stock is verified later) | Phases 1 and 4, and the store list | Pending |
| 8 | Global allocation across the 3 decks and the budget curve (100,000-300,000 CLP, steps of 50,000, parity within 0.2); candidate and swap lists; dashboard | Phases 6 and 7 | Pending |
| 9 | Choose stores and collect offers with verified real stock for the Phase 8 shortlist | Phase 8 | Pending (late) |
| 10 | Joint optimization (allocation plus purchase, at most the stores the owner lists, shipping); backtrack when stock fails (at most 5 rounds, each re-rated with a reduced rule) | Phase 9 | Pending |
| 11 | Rules freshness check, test-panel rating of the frozen lists, stock re-check of the chosen offers within 24 h, pull list (owned cards to take out per deck), purchase by the user, reconciliation (bought versus planned, collection updated). If the rating fails: back to Phase 8 once, then the D2 fallback | Phase 10 | Pending |

Status as of 2026-10-12.

## Constraints
- Budget: chosen by the owner from the curve, between 100,000 and 300,000 CLP, only for
  cards and shipping (payment fees count if a store charges them); owned cards are free.
- Stores: the 7 Chilean specialist shops in `data/stores.md`, the first 3 by default; fewer
  stores are preferred because of shipping; all prices in CLP, no conversion.
- Free tools only: no paid apps or subscriptions (an exception needs the user's approval).
- Cards to buy: English or Spanish printings only, the cheaper one preferred.
- Collection: mixed Spanish and English cards; the 2 decks are sleeved; scanning is done
  from an Android phone.
- Every card to buy needs verified real stock at decision time.
- The user makes every purchase.

## Power scale
Since 2026-10-13 the yardstick is Commander Salt's: **power 1-10** (casual below 5, upgraded casual
5-6.49, mid 6.5-7.59, high 7.6-8.99, cEDH from 9) and its decimal bracket. The goal is the highest
power the budget buys for each deck, at parity, every deck above the 6.1 of the owner's friend's
deck. All three decks target Bracket 3; only Wizards' official conditions limit a deck (Layer A).
See [docs/proposals/commandersalt-adoption.md](docs/proposals/commandersalt-adoption.md); the older
scale is in [docs/power-scale.md](docs/power-scale.md) (superseded).

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
`check-stock`, `build-deck`. Subagents: `deck-judge`, `stock-verifier`.

## Git hygiene
Commits must use the personal identity. After cloning, enable the repo hook (it is
bypassed by `git commit --no-verify`):

```
git config --local core.hooksPath .githooks
```

The hook that keeps Claude's git read-only is tested with
`sh evals/run_hook_cases.sh .claude/hooks/block-git-writes.sh evals/hook_cases.tsv`
(140 cases, expect `failures=0`).
