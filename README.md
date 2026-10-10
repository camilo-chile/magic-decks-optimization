# magic-decks-optimization

Build one new Commander deck and upgrade two existing ones to the top of Bracket 3 ("3.9"
on a custom power scale), within a budget, using verified real stock in Chilean stores.

| Deck | Commander | Goal |
|---|---|---|
| New | Alexios, Deimos of Kosmos | Build from scratch |
| Existing | Toph, the First Metalbender | Upgrade |
| Existing | Fire Lord Azula | Upgrade |

Budget: 200,000 CLP total, at most 3 stores, owned cards first.

## Power scale
`X.Y`: X is the official Commander Bracket (1-5), Y is build quality inside it (1-9).
`3.9` is the strongest deck that still meets every Bracket 3 condition. Details and rating
method: [docs/power-scale.md](docs/power-scale.md).

## Setup
The conda environment is created in conda's default location; only `requirements.txt`
lives in the repo.

```
conda create -n magic-decks python=3.12
conda activate magic-decks
pip install -r requirements.txt
```

## Working with Claude Code
Project rules live in [CLAUDE.md](CLAUDE.md). Skills: `rate-deck`, `check-stock`,
`build-deck`. Subagents: `deck-judge`, `stock-verifier`.

## Git hygiene
Commits must use the personal identity. After cloning, enable the repo hook:

```
git config --local core.hooksPath .githooks
```
