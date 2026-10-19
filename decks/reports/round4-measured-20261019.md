# Round-4 ladders measured on Commander Salt, 2026-10-19

Azula and Ezio were rebuilt after the round-3 plateau (Salt's ceiling "wincon combos with no tutors", Wincons pillar 219 and 353 against
Toph's 1,654): more Layer-A-legal Spellbook win lines, tutors that reach them, a lower average mana value, lands only as far as
Manabase Quality needs. Every list was hosted unlisted on the owner's Moxfield and scored by hand on Commander Salt, scoring
version 2026.4195; the cards Salt scored (its "Export list") hash identically to our file in every case (`decks/proposals/measured.json`
keeps the hash, the Salt page id and the Moxfield id; the lists are in `decks/measured/`). Prices: `merged-20261019T1013Z.json`
(140 new names read on 2026-10-19). "WotC" is Wizards' own bracket as the Salt page reports it; "Salt bracket" is Commander Salt's.

| Deck | Step | Cost CLP | Power | Salt | Manabase Quality | Salt bracket | WotC | Pillars C / E / I / W | Ceiling |
|---|---|---|---|---|---|---|---|---|---|
| Azula | 0 | 0 | 4.9 | 44.0 | 63 % | 2 | - | 237 / 341 / 301 / 72 | -1.60 stall shell, no clear win path |
| Azula | 15 | 14,406 | 6.0 | 40.3 | 96 % | 3* | - | 249 / 356 / 293 / 83 | -0.70 stall shell |
| Azula | 18 | 24,921 | 7.0 | 50.5 | 96 % | 3* | - | 236 / 360 / 291 / 212 | -0.26 sparse, slow combo package |
| Azula | 24 | 34,721 | 6.9 | 58.3 | 96 % | 3* | - | 241 / 384 / 279 / 292 | -0.93 wincon combos with no tutors |
| Azula | **27** | **49,191** | **8.4** | 66.1 | 95 % | 4* | 3 | 256 / 381 / 265 / 477 | none |
| Azula | 35 | 74,041 | 8.4 | 67.0 | 95 % | 4* | 3 | 246 / 379 / 225 / 745 | none |
| Azula | 40 | 98,561 | 8.4 | 82.8 | 95 % | 4* | 3 | 251 / 367 / 221 / 1,501 | none |
| Azula | 44 | 147,811 | 8.3 | 104.5 | 95 % | 4* | 3 | 259 / 357 / 204 / 2,147 | none |
| Ezio | 0 | 0 | 4.1 | 57.0 | 43 % | 2 | 2 | 279 / 128 / 152 / 31 | none |
| Ezio | 14 | 14,655 | 5.3 | 58.9 | 55 % | 3* | 2 | 262 / 136 / 171 / 135 | none |
| Ezio | 31 | 24,751 | 5.8 | 51.9 | 97 % | 3* | 2 | 291 / 150 / 188 / 163 | none |
| Ezio | 33 | 34,541 | 6.8 | 52.7 | 97 % | 3* | 2 | 285 / 150 / 186 / 290 | none |
| Ezio | **39** | **48,951** | **7.4** | 59.6 | 97 % | 3* | 2 | 267 / 159 / 194 / 429 | none |
| Ezio | 43 | 74,151 | 6.2 | 72.0 | 97 % | 3* | 2 | 257 / 163 / 199 / 503 | none |
| Ezio | 50 | 97,791 | 6.4 | 83.2 | 97 % | 3 | 3 | 252 / 179 / 213 / 603 | none |
| Ezio | 54 | 148,011 | 6.3 | 84.4 | 97 % | 3 | 3 | 284 / 190 / 198 / 622 | none |
| Ezio black-core | 0 | 0 | 4.1 | 62.3 | 10 % | 2 | 2 | 257 / 112 / 155 / 51 | none |
| Ezio black-core | 18 | 14,625 | 4.7 | 64.4 | 21 % | 2 | 2 | 250 / 133 / 171 / 63 | none |
| Ezio black-core | 26 | 49,205 | 5.3 | 70.7 | 21 % | 3 | 3 | 222 / 157 / 159 / 492 | none |

## Reading
- **Azula: the plateau was a missing win line.** The step that added Godo + Helm of the Host and Solve the Equation (step 24 to 27, with
  Reckless Handling and Loyal Inventor to find the Helm) took power from 6.9 to 8.4 for about 14,000 CLP more, the structural ceiling
  disappeared and the Wincons pillar went from 292 to 477 (2,147 by step 44). More money after step 27 added nothing (8.4, 8.4, 8.3).
  Commander Salt's own bracket is 4* from step 27 on ("outperforms its WotC bracket"); Wizards' criteria and Layer A give Bracket 3.
  If the owner wants Salt's bracket at 3* or below, step 18 (24,921 CLP) scores 7.0.
- **Ezio: one good list, then it gets worse.** Step 39 (48,951 CLP) scores 7.4 (round 3: 7.0 at 45,872); the lists that add Kiki-Jiki,
  Goblin Bombardment, Godo and Helm score 6.2 to 6.4 although Salt's score and Wincons pillar grow: more Spellbook lines are not more
  power on Salt. WotC bracket 2 up to step 43.
- **The black-core test fails on Salt.** Black at least 73 % of the symbols, blue as the only regular second color, the others only through
  any-color sources, tapped black-and-X duals: 5.3 at 49,205 CLP against 7.4 for the five-color list at 48,951. Manabase Quality is
  21 % against 97 % (six lands always tapped, four conditionally), and it gives up Godo, Kiki-Jiki, Dualcaster and Queen Marchesa. It casts
  the {B}{B} freerunning costs a little more often (32 black sources against 27), which Salt's power does not reward.
- **Budget curve (no parity rule, `decks/reports/budget-curve.md`):** 100,000 CLP: Ezio 39 + Azula 27 + Toph free base (98,142 CLP,
  7.4 / 8.4 / 7.1); 150,000: Toph step 21 (147,284 CLP, 7.4 / 8.4 / 7.4); 200,000: Toph step 30 (195,679 CLP, 7.4 / 8.4 / 7.5); above that nothing
  more is offered. The checkpoints between (Azula 15, 24; Ezio 14, 31, 33, 43, 50, 54; black-core 0, 18, 26) are measured but dominated.
- Not measured: the black-core steps 20 and 23 (they sit between measured steps 18 and 26).
