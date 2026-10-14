# Candidate lists (Phase 4)

Real public lists copied by hand from Commander Salt deck pages ("Export list", one deck at a time,
2026-10-14), one file per list: `decks/candidates/<commander-slug>/<first 8 hex of the site id>.txt`.
They replace the agent-built reference lists (decision of 2026-10-14, see
`docs/research/audit-prior-art-2026-10-13.md`). Each is a candidate end state, a measured
(list, power) point; the optimizer (Phase 8) prices what the owner is missing from it.

Numbers come from the deck's own page on the day it was read, never from the leaderboard (the
leaderboard rows are stale: one deck showed 7.7 there and 6.9 on its page). Scoring version of the
site: 2026.4195. "Report" is the date printed in the page's field report, the best evidence of when
the score was computed. Layer A is `scripts/check_candidates.py` (target Bracket 3, rules snapshot
2026-02-09, bulk `oracle-cards-20261011210156`); the result is in `gate-report.json` once the owner
runs the script.

## Alexios, Deimos of Kosmos
| File | Deck (site title) | Power | Site bracket | Salt | Report | Layer A | Notes |
|---|---|---|---|---|---|---|---|
| `ec03cc3a` | Alexios, Deimos of Kosmos | 7.5 | 3 | 96.5 | 2026-10-07 | floor 3, 2 Game Changers (Gamble, Jeska's Will) | Late two-card Godo + Helm of the Host; stax names (review); best measured list that passes |
| `91a1a44e` | alexios b3 | 7.2 | 3 | 127.5 | 2026-10-03 | floor 3, 2 Game Changers | No combos flagged; stax names (review) |
| `f4b8cc3a` | [Bracket 3] Alexios, Brainless Fight-Machine | 8.0 | 4* | 125.0 | 2026-04-29 (older scoring) | floor 4 | Sword of Feast and Famine + Aggravated Assault is early; removing Aggravated Assault clears it. 3 Game Changers |
| `40b377d5` | Exporting Deimocracy | 8.9 | 4* | 135.2 | 2026-10-09 | floor 4 | Three early combos with Aggravated Assault; remove it (and review Helm of the Host pairs) |

Read, not saved (not Layer-A-tested, listed for the record): 2735a898 (7.5, site bracket 4: Blood
Moon, Aggravated Assault, Mana Vault), 869b65d5 (7.1, site bracket 4: Blood Moon, Winter Orb),
02ebb008 (8.2, site bracket 4: Winter Orb, Aggravated Assault, Helm), aeaac627 (8.3, site bracket 4:
Blood Moon, Aggravated Assault), 14640aa6 (6.9, site bracket 3), 5d19fb77 (6.9, site bracket 3*).

## Toph, the First Metalbender
| File | Deck (site title) | Power | Site bracket | Salt | Report | Layer A | Notes |
|---|---|---|---|---|---|---|---|
| `9354c58f` | Toph | 7.4 | 3* | 43.9 | 2026-10-01 | floor 1, 0 Game Changers | Only review notes (Mindslaver, The Stasis Coffin with Toph) |
| `46892532` | Toph, The 1st Metal bender | 7.3 | 3 | 70.4 | 2026-10-04 | floor 3, 0 Game Changers | Bumi, Unleashed + Ashaya is late (14 mana) |
| `0f65b61d` | [B3] Toph, the First Metalbender | 7.2 | 3 | 93.5 | 2026-10-04 | floor 3, 2 Game Changers (Crop Rotation, Field of the Dead) | Bumi + Ashaya late |
| `dce02411` | Toph, the First Metalbender | 7.3 | 3 | 89.0 | 2026-10-10 | rejected: Earth Rumble is not Commander-legal | Swap that card; otherwise floor 3, 1 Game Changer |

The owner's own list is power 6.5 (bracket 3, salt 72.4), so these four are +0.7 to +0.9.

## Fire Lord Azula
| File | Deck (site title) | Power | Site bracket | Salt | Report | Layer A | Notes |
|---|---|---|---|---|---|---|---|
| `963a6e62` | Flash Fire Lord | 7.4 | 3 | 79.4 | 2026-10-08 | floor 3, 3 Game Changers (Cyclonic Rift, Orcish Bowmasters, Vampiric Tutor) | Return the Favor + a magecraft payoff + Azula is a three-piece loop (no floor 4 under the early two-card rule; read it by hand) |
| `0653e6b7` | Shotgun Azula | 7.2 | 3* | 59.1 | 2026-10-13 | floor 3, 0 Game Changers | Hullbreaker Horror with two rocks costs 8 (borderline, check by hand); cheapest list |
| `c80d8207` | Dime Lindura | 7.3 | 3 | 84.2 | 2026-10-03 | floor 3 with review, 3 Game Changers (Jeska's Will, Orcish Bowmasters, The One Ring) | Nexus of Fate under Azula gives two extra turns and returns itself: chain candidate to check by hand before using it |
| `886804b8` | Azula win or wiff | 7.4 | 3* | 104.0 | 2026-10-12 | floor 4 | Dramatic Reversal + Isochron Scepter (4 mana) and + Lithoform Engine: remove Dramatic Reversal |
| `291c57b5` | Azula | 7.4 | 3 | 120.9 | 2026-09-30 | floor 4, 3 Game Changers (Ancient Tomb, Demonic Tutor, Fierce Guardianship) | Narset's Reversal + Reverberate is early: remove one |

The owner's own list is power 4.0 (bracket 2, salt 33.8), so the passing lists are +3.2 to +3.4.

## Upgrade picks (Upgrades tab, Meta, Staples, Bracket 3 bin, 2026-10-14)
`toph-the-first-metalbender/meta-staples-bracket3.md` and `fire-lord-azula/meta-staples-bracket3.md`:
the 100 cards each owner deck lacks, ordered by how many real Bracket 3 decks of that commander play
them. Not filtered by Wizards' conditions or by Commander legality: run Layer A on any list built
from them.

## How a list was captured
Deck page, "Export list" copies the 100 cards; the header values were read from the same page.
The site page was left unchanged (no import, no refresh of other people's decks).
