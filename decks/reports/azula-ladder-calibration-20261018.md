# Azula ladder calibration on Commander Salt, 2026-10-18

Four checkpoints of the Opus 5.5 ladder (`decks/proposals/fire-lord-azula.ladder.txt`) were hosted on the owner's
Moxfield (unlisted) and scored by hand on Commander Salt, scoring version 2026.4195 (latest in the changelog on
2026-10-18). For each list the cards Salt scored (its "Export list") hash identically to our file (see
`decks/proposals/measured.json`). The agent's power figures were a judgment, written before any measurement.

| Ladder step | Cost CLP | Bracket | Power | Salt | Agent's expected power | Reading |
|---|---|---|---|---|---|---|
| owner's list (reference) | 0 | 2 | 4.0 | 33.6 | - | the deck before the project |
| 0 (free base) | 0 | 2 (core) | **4.9** | 41.9 | 4.6-5.2 | inside the band: a better list with the same cards |
| 17 | 24,505 | 3* (upgraded) | **6.1** | 52.0 | 5.8-6.4 | inside the band; ties the friend's 6.1 for about 25,000 CLP |
| 31 | 49,190 | 3* | **6.6** | 53.6 | not given | +0.5 for +24,700 CLP |
| 47 (end) | 148,760 | 3* | **7.4** | 67.7 | 6.6-7.1 | above the band; equals the best measured public lists (7.2-7.4 at 500,000 to 1,230,000 CLP) |

Findings:
- The ladder method works: the first purchases buy the most (steps 1-17 give +1.2 power for 24,505 CLP) and the
  agent's judgment was conservative at the top (7.4 against 6.6-7.1).
- Bracket 3* is Salt's mark for "near the upper edge of Bracket 3"; the lists pass Layer A (floor 1, 0 Game
  Changers). Keep watching the star on every checkpoint.
- The salt rating is noise below about 1 point (see `moxfield-validation-20261018.md`); parity is judged on power.
- Still unmeasured for the first optimizer pass: steps 38 and 41 (about 74,000 and 97,000 CLP) and, if the optimizer
  needs it, steps between 31 and 47.
