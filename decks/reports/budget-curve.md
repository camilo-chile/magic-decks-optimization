# Budget curve (measured points only)

Generated 2026-10-19 by `scripts/optimize_budget.py` from `decks/proposals/measured.json` (Commander Salt 2026.4195, measured 2026-10-19). One measured list per deck, the highest sum of powers within the budget (no parity rule since 2026-10-19); every deck should reach 7.0. Costs are cards only (shipping outside the budget).

| Budget | ezio-auditore-da-firenze | fire-lord-azula | toph-the-first-metalbender | Total | Unspent | Sum | Weakest | Gap | All >= 7.0 |
|---|---|---|---|---|---|---|---|---|---|
| 100,000 | round3-step39 (45,872; 7.0) | round3-step34 (49,592; 7.1) | round2-step0 (0; 7.1) | 95,464 | 4,536 | 21.2 | 7.0 | 0.1 | yes |
| 150,000 | round3-step39 (45,872; 7.0) | round3-step34 (49,592; 7.1) | round3-step21 (49,142; 7.4) | 144,606 | 5,394 | 21.5 | 7.0 | 0.4 | yes |
| 200,000 | round3-step39 (45,872; 7.0) | round3-step34 (49,592; 7.1) | round3-step30 (97,537; 7.5) | 193,001 | 6,999 | 21.6 | 7.0 | 0.5 | yes |
| 250,000 | round3-step50 (141,322; 7.1) | round3-step34 (49,592; 7.1) | round3-step21 (49,142; 7.4) | 240,056 | 9,944 | 21.6 | 7.1 | 0.3 | yes |
| 300,000 | round3-step50 (141,322; 7.1) | round3-step34 (49,592; 7.1) | round3-step30 (97,537; 7.5) | 288,451 | 11,549 | 21.7 | 7.1 | 0.4 | yes |

Power change of each deck from one budget to the next:

- ezio-auditore-da-firenze: 150,000: +0.0, 200,000: +0.0, 250,000: +0.1, 300,000: +0.0
- fire-lord-azula: 150,000: +0.0, 200,000: +0.0, 250,000: +0.0, 300,000: +0.0
- toph-the-first-metalbender: 150,000: +0.3, 200,000: +0.1, 250,000: -0.1, 300,000: +0.1

Best buys first (power gained per 10,000 CLP between two measured points of the same deck):

| Deck | From | To | Extra CLP | Power | Per 10,000 CLP |
|---|---|---|---|---|---|
| ezio-auditore-da-firenze | round3-step24 (24,827) | round3-step39 (45,872) | 21,045 | +0.6 | +0.28 |
| fire-lord-azula | round3-step23 (24,882) | round3-step34 (49,592) | 24,710 | +0.3 | +0.12 |
| toph-the-first-metalbender | round3-step11 (24,152) | round3-step21 (49,142) | 24,990 | +0.2 | +0.08 |
| toph-the-first-metalbender | round2-step0 (0) | round3-step11 (24,152) | 24,152 | +0.1 | +0.04 |
| toph-the-first-metalbender | round3-step21 (49,142) | round3-step30 (97,537) | 48,395 | +0.1 | +0.02 |
| ezio-auditore-da-firenze | round3-step39 (45,872) | round3-step50 (141,322) | 95,450 | +0.1 | +0.01 |
| fire-lord-azula | round3-step34 (49,592) | round3-step53 (148,712) | 99,120 | +0.1 | +0.01 |

Measured points used per deck (cost CLP; power):

- ezio-auditore-da-firenze: round3-step24 (24,827; 6.4), round3-step39 (45,872; 7.0), round3-step50 (141,322; 7.1)
- fire-lord-azula: round3-step23 (24,882; 6.8), round3-step34 (49,592; 7.1), round3-step53 (148,712; 7.2)
- toph-the-first-metalbender: round2-step0 (0; 7.1), round3-step11 (24,152; 7.2), round3-step21 (49,142; 7.4), round3-step30 (97,537; 7.5)
