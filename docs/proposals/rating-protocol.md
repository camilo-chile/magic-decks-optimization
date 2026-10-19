# Measurement protocol and decision log (v4)

Status: v4, 2026-10-13. The judge-panel protocol (v3) was removed on 2026-10-18 (it is in the git
history). Power is now measured with Commander Salt
(owner decision, 2026-10-13); see [power-scale.md](../power-scale.md) and
[commandersalt-adoption.md](commandersalt-adoption.md).

## How a deck is scored
1. **Layer A** (offline): `scripts/layer_a.py` writes `decks/<slug>.layer_a.json`. The floor must
   not exceed the deck's target bracket and nothing may be rejected.
2. **Host the list.** Since 2026-10-18 Claude creates the deck (unlisted, paste in list) in the
   owner's signed-in Moxfield (`camilochile`), one deck at a time, and submits the link to Commander Salt.
3. **Score.** Claude reads on the Salt deck page: power, bracket, salt, pillars, Manabase Quality, score
   drivers (caps and penalties), combos and the scoring version, and compares the hash of Salt's
   "Export list" with the hash of our file (they must be identical).
4. **Record.** The numbers go to `decks/proposals/measured.json` (one entry per list, with the hash, the
   Salt page id and the Moxfield id) and a short report in `decks/reports/`, stamped with the scoring version
   and the date. Scores from different versions are not compared.
5. **Decide.** The optimizer chooses one measured checkpoint per deck for each budget at parity, gated by
   Layer A; the final lists of each budget point are scored on the site before the owner chooses. No local
   surrogate model (it would be our own power scale again) and no expert judgment of power: the agents'
   estimates were 0.3 to 2.1 points too high for Toph and Alexios (`decks/reports/round2-measured-20261018.md`).

## Calibration (Phase 5)
- Dropped on 2026-10-14 (prior-art audit): the ablation ladder (the site already shows a dense
  measured spread of real lists).
- Done: the owner's Toph link scored twice on different days (2026-10-13 and 2026-10-14), identical
  on every number.
- Fixed points: the owner's two current decks (Toph 6.5, Azula 4.0) and the friend's Krenko (6.1).

## Decision log
| ID | Decision | Status |
|---|---|---|
| D1 | Y relative to each commander | Superseded: power is Commander Salt's absolute 1-10 |
| D2 | Goal: budget curve, 100,000 to 300,000 CLP in steps of 50,000, parity within 0.2 points, owner picks | **Kept** (points are Commander Salt power points) |
| D3 | Speed as a 5-level flag | Superseded: the site's speed and pillars |
| D4 | Pairwise judgments, Bradley-Terry | Superseded |
| D5 | Owned cards cost 0; one physical copy per deck; locked-cards file per deck, chosen in Phase 6 | **Kept** |
| D6 | Any legal English or Spanish printing and finish, condition near mint to lightly played, no proxies; budget counts checkout totals with shipping and fees; sleeves outside the budget | **Kept** |
| D7 | EDHREC, Archidekt and Moxfield are not scripted (terms) | **Kept**; Commander Salt is used by hand (D21) |
| D8 | The owner does not label decks | **Kept** |
| D9 | Stock verifier on Haiku 5.5, Sonnet 5.5 if it fails | **Kept** |
| D10 | Bracket-fit review by a panel | Superseded: Commander Salt's bracket rationale and Layer A |
| D11 | Ablation constant `9 - k/4` | Superseded: the rungs are measured, not labelled |
| D12 | The reference is drafted by Claude and accepted by criteria | **Changed**: accepted by Layer A, an independent card-by-card review and its Commander Salt score |
| D13 | Official ratings by a script, development ratings in chat | Superseded |
| D14 | Local `qwen3.8:27b` judge through Ollama | **Dropped**: no panel, no Ollama install |
| D15 | Wait for the 2026-10-12 rules announcement | Done (re-checked 2026-10-13) |
| D16 | Everything in CLP from the 7 stores in `data/stores.md`, no conversion, fewer stores preferred | **Kept** |
| D17 | Speed bands | Superseded |
| D18 | Language is a per-deck setting (es, en, both) | **Kept** |
| D19 | Power first: only official conditions of the target bracket limit a deck | **Kept** |
| D20 | Target bracket per deck; all three are 3 | **Kept** |
| D21 | Commander Salt is the yardstick, used by hand in the browser, no email, no scripting (2026-10-13) | **New** |

## Open items
| ID | Question | When |
|---|---|---|
| O1 | Whether the stores expose a product JSON, and each store's shipping rule and payment fees | Before Phase 7 |
| O2 | Which cards of Toph and Azula are locked | Phase 6, after their scores |
| O3 | Other decks of the owner | Closed 2026-10-12: out of scope until the project ends |
