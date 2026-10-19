# Round-2 ladders measured on Commander Salt, 2026-10-18

Lists hosted on the owner's Moxfield (unlisted), scored by hand on Commander Salt, scoring version 2026.4195. For every
list the cards Salt scored (its "Export list") hash identically to our file (`decks/proposals/measured.json` keeps the
hash, the Salt page id and the Moxfield id). The "judged" column is the expert agent's own estimate, written before any
measurement.

| Deck | Ladder step | Cost CLP | Judged | Measured | Bracket | Manabase Quality | What Salt says |
|---|---|---|---|---|---|---|---|
| Azula | round 1, step 17 | 24,505 | 5.8-6.4 | 6.1 | 3* | 53 % | - |
| Azula | round 1, step 31 | 49,190 | - | 6.6 | 3* | 68 % | - |
| Azula | round 1, step 47 | 148,760 | 6.6-7.1 | 7.4 | 3* | - | - |
| Azula | round 2, step 24 | 48,905 | 6.7-7.0 | **5.5** | 3* | 32 % | pillars fine; weak mana base |
| Azula | round 2, step 24 + 9 cheap duals | 56,060 | - | **6.9** | 3* | 70 % | +1.4 power for 7,155 CLP |
| Toph | round 2, step 0 (free) | 0 | 7.0 | **7.1** | 3 | 52 % | cap -0.27: wincon combos with no tutors |
| Toph | round 2, step 10 | 10,590 | 7.5 | 6.9 | 3 | 69 % | cap -1.18: wincon combos with no tutors |
| Toph | round 2, step 22 | 24,610 | 7.8 | 6.9 | 3 | 68 % | cap -0.50 and "too slow for its pieces" |
| Toph | round 2, step 36 | 146,240 | 8.1 | 7.5 | 3 | 93 % | "too slow for its pieces" (capped, major) |
| Alexios | round 2, step 19 | 24,822 | 5.9-6.5 | **4.1** | 3 | 97 % | Interaction 117 (84 % of baseline); incidental combos (major) |
| Alexios | round 2, step 39 | 97,602 | 6.8-7.3 | 5.9 | 3 | 98 % | cap -0.41: sparse, slow combo package; tutors would fix it |
| Alexios | round 2, step 48 | 197,392 | 7.2-7.7 | 6.8 | 3 | 98 % | cap -0.11; high-quality manabase boost |

Reading:
- The agents' power judgments are not reliable for Toph and Alexios (off by 0.3 to 2.1 points, always high); only
  measured points count for the budget curve.
- Azula's power responds strongly to the mana base (Salt's Manabase Quality) and to nothing else that was changed.
- Toph is already about 7.1 for free (the owner's list was 6.5): the purchases add little (+0.4 for 146,240 CLP), and the
  caps Salt applies are about tutors for the combo wincons and a deck that is slow for the pieces it plays. A fast,
  cheap package and a tutor could be worth more than lands.
- Alexios is a weaker deck: 4.1 at about 25,000 CLP and 6.8 at about 197,000 CLP. Salt's own Bracket 3 staples for it
  (`decks/candidates/alexios-deimos-of-kosmos/meta-staples-bracket3.md`) are equipment, cost reducers and red
  rituals; the agent's ladder is a Helm of the Host plan that Salt rates as sparse and slow.
- Parity within 0.2 across the three decks at each budget will be set by the weakest curve (Alexios), so the budget
  that matters most is what Alexios needs to reach 6.8 or more.
