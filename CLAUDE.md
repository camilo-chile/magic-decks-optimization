# magic-decks-optimization

Build 1 new Commander deck and upgrade 2 existing ones, all to the top of Bracket 3
("3.9" on our custom power scale), within a purchase budget, using verified real
stock in Chilean stores. The project is also a vehicle for learning modern AI tooling.

## Decks
| Role | Commander |
|---|---|
| NEW (user owns only the commander card) | Alexios, Deimos of Kosmos |
| UPGRADE | Toph, the First Metalbender |
| UPGRADE | Fire Lord Azula |

## Hard constraints
- Target: all 3 decks at 3.9 (spec: `docs/power-scale.md`). Never meet Bracket 4 conditions.
- Budget: 200,000 CLP in total for all purchases, max 3 Chilean stores, owned cards first.
- Every card to buy must have verified stock > 0 at decision time. If stock fails, re-plan
  (backtrack). Never leave an unverified card in a final list.
- Nothing is bought before the 3 final lists are rated 3.9.

## Working agreement (read first)
- Chat language with the user: Spanish. Everything else (code, comments, identifiers,
  commits, docs, reports, this file): English.
- Be extremely concise. Short answers; tables and bullet lists over paragraphs.
- Plan first and resolve open questions. When the plan looks closed, ask "execute now?"
  unless the user already said to go ahead. Do not rush. Read-only research is always fine.
- The user runs project code himself. Use conda, never venv. The conda env lives in conda's
  default envs directory; the repo only holds `requirements.txt`. You may write and test
  code, but hand over the run command.
- Never `git commit` or `git push` (denied in settings). Propose a commit message; the user
  commits from the VS Code UI.
- Git identity for this repo: camilo-chile / camiloy.94@gmail.com. Never the work or
  university email. `.githooks/pre-commit` enforces it for every commit, UI included.
- Prefer UI steps over terminal commands when giving instructions.
- Tooling policy: official MCP > community MCP > custom MCP (last resort). For simple public
  APIs consider a skill plus the API before any MCP.
- Teaching: the user leads an AI team and wants to learn new tools. When a Claude Code or AI
  feature fits the moment, suggest it proactively in one or two lines, with why it matters
  for his work.
- Never state that a read, extraction or verification is complete without a check
  (counts, a control phrase).
- Do not use `/effort ultracode`. Run a workflow only when the user asks for one.

## Layout
| Path | Purpose |
|---|---|
| `docs/power-scale.md` | Source of truth for the X.Y power scale |
| `decks/` | Decklists (`1 Card Name` per line) and rating reports |
| `data/raw/` | Private inputs such as the collection export (git-ignored) |
| `scripts/` | Python the user runs himself |
| `evals/` | Anchor decks and reliability tests of the rating method |
| `.claude/skills/` | `rate-deck`, `check-stock`, `build-deck` |
| `.claude/agents/` | `deck-judge`, `stock-verifier` |
| `.githooks/pre-commit` | Blocks commits made with a non-personal git email |

## Known facts and pitfalls
- ManaBox deck links are JS-rendered and cannot be fetched; use a text export.
- Static HTML or search snippets are not evidence of stock. See the `check-stock` skill.
- Bracket rules change over time; always cite the date of the rules snapshot used.
- Speed ("win by turn N") is not a goal or a gate in this project; only bracket rules and
  budget bound a deck. Only Game Changers are an exact bracket count; the rest is intent.
- Use the Scryfall and Commander Spellbook JSON APIs only; do not read their HTML pages.
