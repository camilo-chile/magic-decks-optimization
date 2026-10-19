# Budget curve (measured points only)

Generated 2026-10-19 by `scripts/optimize_budget.py` from `decks/proposals/measured.json` (Commander Salt 2026.4195, measured 2026-10-19). One measured list per deck, the highest sum of powers within the budget (no parity rule since 2026-10-19); every deck should reach 7.0. Costs are cards only (shipping outside the budget).

| Budget | ezio-auditore-da-firenze | fire-lord-azula | toph-the-first-metalbender | Total | Unspent | Sum | Weakest | Gap | All >= 7.0 |
|---|---|---|---|---|---|---|---|---|---|
| 100,000 | round4-step39 (48,951; 7.4) | round4-step27 (49,191; 8.4) | round2-step0 (0; 7.1) | 98,142 | 1,858 | 22.9 | 7.1 | 1.3 | yes |
| 150,000 | round4-step39 (48,951; 7.4) | round4-step27 (49,191; 8.4) | round3-step21 (49,142; 7.4) | 147,284 | 2,716 | 23.2 | 7.4 | 1.0 | yes |
| 200,000 | round4-step39 (48,951; 7.4) | round4-step27 (49,191; 8.4) | round3-step30 (97,537; 7.5) | 195,679 | 4,321 | 23.3 | 7.4 | 1.0 | yes |
| 250,000 | round4-step39 (48,951; 7.4) | round4-step27 (49,191; 8.4) | round3-step30 (97,537; 7.5) | 195,679 | 54,321 | 23.3 | 7.4 | 1.0 | yes |
| 300,000 | round4-step39 (48,951; 7.4) | round4-step27 (49,191; 8.4) | round3-step30 (97,537; 7.5) | 195,679 | 104,321 | 23.3 | 7.4 | 1.0 | yes |

Power change of each deck from one budget to the next:

- ezio-auditore-da-firenze: 150,000: +0.0, 200,000: +0.0, 250,000: +0.0, 300,000: +0.0
- fire-lord-azula: 150,000: +0.0, 200,000: +0.0, 250,000: +0.0, 300,000: +0.0
- toph-the-first-metalbender: 150,000: +0.3, 200,000: +0.1, 250,000: +0.0, 300,000: +0.0

Best buys first (power gained per 10,000 CLP between two measured points of the same deck):

| Deck | From | To | Extra CLP | Power | Per 10,000 CLP |
|---|---|---|---|---|---|
| ezio-auditore-da-firenze | round4-step14 (14,655) | round3-step24 (24,827) | 10,172 | +1.1 | +1.08 |
| fire-lord-azula | round4-step15 (14,406) | round4-step18 (24,921) | 10,515 | +1.0 | +0.95 |
| ezio-auditore-da-firenze | round4-step0 (0) | round4-step14 (14,655) | 14,655 | +1.2 | +0.82 |
| fire-lord-azula | round4-step0 (0) | round4-step15 (14,406) | 14,406 | +1.1 | +0.76 |
| fire-lord-azula | round4-step18 (24,921) | round4-step27 (49,191) | 24,270 | +1.4 | +0.58 |
| ezio-auditore-da-firenze | round4-step33 (34,541) | round4-step39 (48,951) | 14,410 | +0.6 | +0.42 |
| ezio-auditore-da-firenze | round3-step24 (24,827) | round4-step33 (34,541) | 9,714 | +0.4 | +0.41 |
| toph-the-first-metalbender | round3-step11 (24,152) | round3-step21 (49,142) | 24,990 | +0.2 | +0.08 |
| toph-the-first-metalbender | round2-step0 (0) | round3-step11 (24,152) | 24,152 | +0.1 | +0.04 |
| toph-the-first-metalbender | round3-step21 (49,142) | round3-step30 (97,537) | 48,395 | +0.1 | +0.02 |

Measured points used per deck (cost CLP; power):

- ezio-auditore-da-firenze: round4-step0 (0; 4.1), round4-step14 (14,655; 5.3), round4-step31 (24,751; 5.8), round3-step24 (24,827; 6.4), round4-step33 (34,541; 6.8), round3-step39 (45,872; 7.0), round4-step39 (48,951; 7.4)
- fire-lord-azula: round4-step0 (0; 4.9), round4-step15 (14,406; 6.0), round3-step23 (24,882; 6.8), round4-step18 (24,921; 7.0), round4-step27 (49,191; 8.4)
- toph-the-first-metalbender: round2-step0 (0; 7.1), round3-step11 (24,152; 7.2), round3-step21 (49,142; 7.4), round3-step30 (97,537; 7.5)
