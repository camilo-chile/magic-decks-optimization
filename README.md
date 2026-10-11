# magic-decks-optimization

Build one new Commander deck and upgrade two existing ones to the top of Bracket 3 ("3.9"
on a custom power scale), within a budget, using verified real stock in Chilean stores.

| Deck | Commander | Goal |
|---|---|---|
| New | Alexios, Deimos of Kosmos | Build from scratch |
| Existing | Toph, the First Metalbender | Upgrade |
| Existing | Fire Lord Azula | Upgrade |

## Pipeline
| Phase | What happens | Depends on | Status |
|---|---|---|---|
| 0 | Rules snapshot and draft power scale | none | Done (re-check after the 2026-10-12 Wizards announcement) |
| 1 | Digitize the 2 physical decks and the loose collection | Android phone and a free scanning app | In progress: tooling research done, 100-card pilot next |
| 2 | Layer A code and golden tests (name resolution, gate, Spellbook) and the card-facts file generator | Phase 1 export format, Phase 0 | Pending |
| 3 | Synergy research per commander (EDHREC, Scryfall, Commander Spellbook); can run in parallel with Phase 1 | Phase 0 | Pending |
| 4 | Reference builds and anchor ladders per commander; the user signs off each reference | Phases 2 and 3, decisions D7, D10-D12, the rules re-check after 2026-10-12 | Pending |
| 5 | Validate the rating method with evals and freeze the protocol | Phases 2 and 4, approved protocol | Pending |
| 6 | Rate Toph and Azula on the scale | Phases 1, 2 and 5 | Pending |
| 7 | Feasibility: price the reference lists minus owned cards (price model: cheapest legal EN/ES printing in USD, a dated exchange rate, a CLP store multiplier, a shipping model; decision D16) | Phases 1 and 4 | Pending |
| 8 | Global allocation across the 3 decks; candidate and swap lists | Phases 6 and 7 | Pending |
| 9 | Choose stores and collect offers with verified real stock for the Phase 8 shortlist | Phase 8 | Pending (late) |
| 10 | Joint optimization (allocation plus purchase, at most 3 stores, shipping); backtrack when stock fails (at most 5 rounds, each re-rated with a reduced rule) | Phase 9 | Pending |
| 11 | Rules freshness check, test-panel rating of the frozen lists, stock re-check of the chosen offers within 24 h, pull list (owned cards to take out per deck), purchase by the user, reconciliation (bought versus planned, collection updated). If the rating fails: back to Phase 8 once, then the D2 fallback | Phase 10 | Pending |

Status as of 2026-10-10.

## Constraints
- Budget: 200,000 CLP in total, only for cards and shipping (payment fees count if a store
  charges them at checkout, decision D6 pending); max 3 stores; owned cards first.
- Free tools only: no paid apps or subscriptions (an exception needs the user's approval).
- Cards to buy: English or Spanish printings only, the cheaper one preferred.
- Collection: mixed Spanish and English cards; the 2 decks are sleeved; scanning is done
  from an Android phone.
- Every card to buy needs verified real stock at decision time.
- The user makes every purchase.

## Power scale
`X.Y`: X is the official Commander Bracket (1-5), Y is build quality inside it (1-9).
`3.9` is the strongest deck that still meets every Bracket 3 condition. Details and rating
method: [docs/power-scale.md](docs/power-scale.md). Open design decisions:
[docs/proposals/rating-protocol.md](docs/proposals/rating-protocol.md).

## Research
| Report | Topic |
|---|---|
| [commander-brackets-rules-snapshot](docs/research/commander-brackets-rules-snapshot.md) | Official bracket rules, Game Changers, Commander Spellbook API, MCP landscape |
| [mtg-collection-scanning-on-android](docs/research/mtg-collection-scanning-on-android.md) | Free Android scanners, Spanish cards, export formats, pilot test, workflow |

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
