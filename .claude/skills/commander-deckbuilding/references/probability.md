# Probability tables for a 99-card singleton library

All tables are **computed** (hypergeometric, exact), not sourced claims. Computed 2026-10-31 for this skill; the same
method and matching values appear in notes/03 (section 3, "Computed") and notes/02 (section 2). Assumptions: 99-card
library, no mulligan, no scry, no extra draw, no tutor. Cards seen by your turn N in a multiplayer game = **7 + N**
(nobody skips the first draw in multiplayer: cited as Comprehensive Rules 103.8c in the gate review
`docs/research/phase2-gate-review-20261031.md` and as 800.7 by Karsten, notes/13 K1; neither number was re-read in the
current rules). In a duel the player on the play sees 6 + N.

Why these are conservative: the first mulligan is free in multiplayer (notes/11 S13; notes/08 S1), every draw spell
raises the cards seen, and tutors add effective pieces. Why they can be optimistic: a piece drawn is not a piece cast
(mana, colors, timing), and opponents remove pieces.

## A. At least one of k pieces, by your turn N

| k | T1 (8) | T2 (9) | T3 (10) | T4 (11) | T5 (12) | T6 (13) | T7 (14) | T9 (16) | T13 (20) |
|---|---|---|---|---|---|---|---|---|---|
| 1 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 16 | 20 |
| 2 | 16 | 17 | 19 | 21 | 23 | 25 | 26 | 30 | 36 |
| 3 | 23 | 25 | 28 | 30 | 32 | 35 | 37 | 41 | 50 |
| 4 | 29 | 32 | 35 | 38 | 41 | 44 | 46 | 51 | 60 |
| 5 | 35 | 39 | 42 | 45 | 48 | 51 | 54 | 59 | 68 |
| 6 | 41 | 44 | 48 | 52 | 55 | 58 | 61 | 66 | 75 |
| 7 | 46 | 50 | 54 | 57 | 61 | 64 | 67 | 72 | 81 |
| 8 | 50 | 55 | 59 | 62 | 66 | 69 | 72 | 77 | 85 |
| 9 | 55 | 59 | 63 | 67 | 70 | 73 | 76 | 81 | 88 |
| 10 | 59 | 63 | 67 | 71 | 74 | 77 | 80 | 84 | 91 |
| 11 | 62 | 67 | 71 | 75 | 78 | 81 | 83 | 87 | 93 |
| 12 | 66 | 70 | 74 | 78 | 81 | 83 | 86 | 90 | 94 |
| 13 | 69 | 73 | 77 | 81 | 83 | 86 | 88 | 91 | 96 |
| 14 | 72 | 76 | 80 | 83 | 86 | 88 | 90 | 93 | 97 |
| 15 | 75 | 79 | 82 | 85 | 88 | 90 | 92 | 94 | 97 |
| 16 | 77 | 81 | 84 | 87 | 90 | 91 | 93 | 95 | 98 |
| 18 | 81 | 85 | 88 | 90 | 92 | 94 | 95 | 97 | 99 |
| 20 | 85 | 88 | 91 | 93 | 94 | 96 | 97 | 98 | 99 |
| 24 | 90 | 93 | 95 | 96 | 97 | 98 | 99 | 99 | 100 |

Values in percent. Cross-check with a source: 14 ramp cards give 80 % and 20 give 90 % to see one by turn 3 with 10 cards
seen (notes/03 S1; reproduced in notes/03).

Reading the gate's classes (scripts/plan_density.py, judgment): early = 10 pieces judged at 12 cards (74.3 %); late = 6
pieces judged at 20 cards (75.2 %). Eight pieces, the "8x8" theme size (notes/01 S2), give only 66 % by turn 5: eight is
a theme size, not an every-game guarantee (notes/03 section 3).

## B. At least TWO of k pieces (for fuel that must recur)

| k | T1 (8) | T2 (9) | T3 (10) | T4 (11) | T5 (12) | T6 (13) | T7 (14) | T9 (16) | T13 (20) |
|---|---|---|---|---|---|---|---|---|---|
| 6 | 7 | 9 | 11 | 13 | 15 | 18 | 20 | 25 | 35 |
| 8 | 13 | 15 | 19 | 22 | 25 | 28 | 32 | 38 | 51 |
| 10 | 19 | 22 | 27 | 31 | 35 | 39 | 43 | 51 | 64 |
| 12 | 25 | 30 | 35 | 40 | 44 | 49 | 53 | 62 | 75 |
| 14 | 32 | 37 | 43 | 48 | 53 | 58 | 63 | 71 | 83 |
| 16 | 38 | 45 | 51 | 56 | 62 | 66 | 71 | 78 | 89 |
| 20 | 51 | 58 | 64 | 70 | 75 | 79 | 83 | 89 | 95 |
| 25 | 65 | 72 | 78 | 82 | 86 | 89 | 92 | 95 | 99 |
| 30 | 76 | 82 | 87 | 90 | 93 | 95 | 97 | 98 | 100 |

Use B when the plan needs the function more than once (two extra land drops, two haste sources for successive
attackers, two revival spells). A function that must fire "most turns" from turn 5 needs a count where B by turn 7 is
above about 70 % [J], or repeatable pieces (one permanent that works every turn counts as many one-shot pieces). The
mins of the profile's support lines (haste 4, defense while tapped 4, extra land drops 5) ASSUME repeatable permanents:
four one-shot pieces give only 9 % to see two by turn 7 (computed), so a one-shot effect counts half [J].

## C. Opening hand and mulligans

At least one of k specific cards in the opening seven: 6 → 36 %, 8 → 46 %, 10 → 54 %, 12 → 61 %, 14 → 67 %, 16 → 72 %,
20 → 81 %. A plan that must start on turn 2 or 3 cannot rely on its opening hand with fewer than about 14 pieces; it
needs the free mulligan, cheap selection, or redundancy.

**Lands in the opening seven** (computed, exact; "free redo" = the multiplayer free first mulligan, so 1 - (1 - p)^2 when
a hand is shipped for this reason):

| Lands | 2 to 4 lands in 7 | with a free redo | 3+ lands in 7 | keepable* per look | keepable* with a free redo |
|---|---|---|---|---|---|
| 34 | 71.9 % | 92.1 % | 45.3 % | | |
| 36 | 74.0 % | 93.3 % | 50.1 % | 64 to 69 % | 87 to 90 % |
| 38 | 75.5 % | 94.0 % | 54.8 % | 64 to 71 % | 87 to 91 % |
| 40 | 76.4 % | 94.4 % | 59.4 % | 67 % | 89 % |

*Keepable = 2 to 4 lands AND at least one spell of mana value 3 or less in the hand, with 22 to 30 such spells among the
nonland cards (computed here; the range is the number of cheap spells). A deck that keeps only 3+ land hands (landfall, big
mana) needs about 40 lands to make that keep more likely than not in one look. Keepable hands are a construction check
[J], not a play rule.

**Measured data** (Playgroup.gg, 173,016 opening hands from tracked games, updated 2026-10-31, "directional, not a
verdict"; opener lands confound deck build, mulligans and skill, notes/13 PG): win rate in 4 to 6 player games was 17 %
with 0 lands in the opener, 25 % with 1, 28 % with 2, 28 % with 3, 29 % with 4, 28 % with 5, 24 % with 6 and 26 % with 7,
so 2 to 5 lands sit within one point of each other and 0 to 1 or 6 lose 4 to 11 points. Of 1,591,235 finished games, 65 %
had no mulligan, 24 % one, 8 % two and 3 % three or more; 89 % of kept openers had 2 to 4 lands (average 2.96); the average
game lasted 8.76 rounds (median 9), which supports a 7-turn curve horizon. Karsten's modelled keep policies (a first seven
with 3 to 5 lands, or Sol Ring with 1 to 5 lands; after the free mulligan also 2-landers) are reasonable, not optimal.

## D. Lands

| Lands | 2 to 4 lands in 7 | 3+ lands by T3 (10) | 4+ by T4 (11) | 5+ by T5 (12) | 5+ lands in opening 7 (flood) |
|---|---|---|---|---|---|
| 33 | 70.7 | 71.3 | 53.3 | 36.3 | 3.9 |
| 34 | 71.9 | 73.7 | 56.3 | 39.4 | 4.5 |
| 35 | 73.1 | 75.9 | 59.2 | 42.5 | 5.1 |
| 36 | 74.0 | 78.0 | 62.1 | 45.6 | 5.8 |
| 37 | 74.8 | 80.0 | 64.9 | 48.8 | 6.6 |
| 38 | 75.5 | 81.9 | 67.6 | 51.9 | 7.4 |
| 39 | 76.0 | 83.6 | 70.2 | 55.0 | 8.3 |
| 40 | 76.4 | 85.3 | 72.6 | 58.0 | 9.2 |
| 41 | 76.6 | 86.8 | 75.0 | 61.0 | 10.2 |
| 42 | 76.7 | 88.2 | 77.2 | 63.9 | 11.3 |

These count lands only. Ramp raises the mana by turn N; it does not raise the land drops (ramp adds to land drops, never
replaces them, notes/03 S5). Source conflict: one checklist claims 36 lands give 90 % for three lands by turn 3 and 74 %
for four by turn 4 (notes/03 S1); recomputed without mulligans these are 78.0 % and 62.1 % (notes/03 conflict 3). Use
the computed values. A landfall deck that wants a land in hand for an extra drop on turns 4 to 6 reads the "5+ by T5"
column: the extra drop needs lands beyond the natural one. Karsten's land regression (31.42 + 3.13 x average MV - 0.28 x
cheap pieces) is fitted on 60-card tournament decks, not on these tables (`mana-and-ramp.md` section 1).

Simulated cast rates with ramp modelled (notes/11 S14, ScrollVault, 50,000 games per setup, London mulligan with the free
first mulligan, no draw spells or interaction): a midrange deck (MV 3.0, 10 ramp) reaches 95 %+ on-curve casting through
five mana at 36 to 37 lands; a four-rock midrange deck casts its five-drop on turn 5 in 88.4 % of games at 29 lands and
95.6 % at 37; a 7-drop on turn 7 is castable in 72.8 % of games at 37 lands and 84.0 % at 42 (battlecruiser).

## E. Colored sources (one color)

| Sources | 1+ by T1 (8) | 1+ by T3 (10) | 2+ by T2 (9) | 2+ by T4 (11) | 3+ by T5 (12) |
|---|---|---|---|---|---|
| 12 | 65.9 | 74.3 | 29.9 | 39.7 | 15.9 |
| 15 | 74.5 | 82.3 | 41.0 | 52.4 | 26.3 |
| 18 | 81.2 | 87.9 | 51.5 | 63.6 | 37.6 |
| 19 | 83.1 | 89.4 | 54.8 | 66.9 | 41.5 |
| 20 | 84.8 | 90.8 | 58.0 | 70.0 | 45.3 |
| 22 | 87.7 | 93.0 | 63.9 | 75.6 | 52.7 |
| 24 | 90.1 | 94.7 | 69.4 | 80.3 | 59.7 |
| 26 | 92.1 | 96.0 | 74.2 | 84.4 | 66.2 |
| 28 | 93.8 | 97.0 | 78.5 | 87.7 | 72.0 |
| 30 | 95.1 | 97.8 | 82.2 | 90.5 | 77.1 |
| 33 | 96.6 | 98.6 | 86.9 | 93.6 | 83.6 |
| 36 | 97.7 | 99.2 | 90.6 | 95.9 | 88.6 |

Sources count lands, rocks and dorks that make the color (notes/02 S5 cites a Commander FAQ that counts rocks and
dorks). Source conflict, now resolved: ScrollVault gives 19 sources for a single pip on turn 1 and 30 for a double pip on
turn 2 in 99 cards (notes/02 S5); under the assumptions of this table (no mulligan, no condition on land drops) 19 reaches
90 % only by turn 3 and 30 only by turn 4 (notes/02 conflict 4), but Karsten's own definition is conditional on having
drawn M lands by turn M after the free mulligan, and under it the same counts give 90 % and 91 % (notes/13 K3). His full
99-card table is in `mana-and-ramp.md` section 4: use it for the target, and this table for the odds at a given count.
Practical reading [J]: a color whose single pips you need on turns 2 to 3 wants about 18 to 20 sources; a color with
double pips on turn 4 wants about 22 to 30; a splash color needed late can sit near 12 to 15.

## E2. Several colors AT ONCE (joint chance)

Chance to have at least one source of EACH of c colors among the cards seen, when each color has s sources among the 38 lands
of a 99-card deck (rocks and dorks ignored, so conservative; sources of different colors overlap at random, as duals do;
Monte Carlo of 60,000 hands per cell, about +-0.3 points; computed for this skill). "Floor" is the product of the
single-color chances from table E.

| Colors c | Sources s per color | by T5 (12 cards) | floor | by T7 (14 cards) | floor |
|---|---|---|---|---|---|
| 2 | 14 | 75 % | 74 % | 82 % | 81 % |
| 2 | 18 | 86 % | 85 % | 91 % | 91 % |
| 2 | 22 | 93 % | 92 % | 96 % | 96 % |
| 3 | 14 | 67 % | 63 % | 75 % | 73 % |
| 3 | 18 | 81 % | 79 % | 88 % | 86 % |
| 3 | 22 | 90 % | 89 % | 94 % | 94 % |
| 4 | 14 | 60 % | 54 % | 70 % | 66 % |
| 4 | 18 | 77 % | 73 % | 84 % | 82 % |
| 4 | 22 | 88 % | 85 % | 93 % | 91 % |
| 5 | 14 | 54 % | 46 % | 65 % | 59 % |
| 5 | 18 | 73 % | 67 % | 82 % | 78 % |
| 5 | 22 | 85 % | 82 % | 91 % | 89 % |
| 5 | 26 | 93 % | 90 % | 96 % | 95 % |

Rule of thumb: multiply the single-color chances of table E; the real joint chance is higher by 0 to 7 points (the gap grows
with the number of colors and shrinks with more sources), so the product is a safe floor. Five colors at 18 sources each give
about 73 % by turn 5 and 82 % by turn 7, so roughly one game in four or five lacks one of the five colors in the early
turns. The table counts having each color once; it does not count the lands needed to cast other spells that turn.

## F. Small-sample warning for playtests

Ten games with five wins give a 95 % Wilson interval of about 24 % to 76 % (computed in notes/08). Ten games cannot rank
two close lists; log what each card did and when (notes/08 inference).
