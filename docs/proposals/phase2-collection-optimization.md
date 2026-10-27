# Phase 2 plan: four decks from the owned collection (2026-10-26)

Owner decisions of 2026-10-26: iteration 1 is closed; iteration 2 optimizes Toph, Ezio and Azula (bilingual) and a fourth
deck (Spanish cards only) from the cards he already owns. He wipes the collection and the decks and rescans everything
(basic lands and tokens included) into two binders, Spanish and English. The Standard cards are not scanned and never used.
Decks stay plain decklists, not registered in ManaBox, so no card counts twice. Claude chooses the fourth commander (the
Spanish "Counter Intelligence" precon is the base, a better commander is welcome). Quality criterion: broad synergy and
stand-alone value in 3 to 4 player pods next to the Commander Salt power (see `docs/research/phase2-play-review-20261026.md`).

| # | Step | Who | Tool or model | State |
|---|---|---|---|---|
| 1 | Wipe, rescan into the Spanish and English binders, export the CSV to `data/collection/ManaBox_Collection_<date>.csv` | Owner | ManaBox on the phone | pending |
| 2 | Build the inventory; read the problem list with him (scan errors: a card in the binder of the other language, unknown names, proxies, conditions) | Claude | `scripts/build_inventory.py` (updated and tested) | ready |
| 3 | Pools: every owned card legal in each commander's color identity, with Oracle text, copies by language and the decks that hold it; a table of the owned legendary creatures with the size of their Spanish pool | Claude | script to write after the scan (needs the real data) | pending step 2 |
| 4 | Choose the fourth commander and its base list from the Spanish collection (precon first) | Claude | Opus 5.5 high (judgment) | pending step 3 |
| 5 | Build the four lists: the Spanish deck first (it is the restricted one), then the others from what is left, one physical copy per deck; judge synergy, curve, interaction, card flow, protection and the plan for 3 to 4 players, not only combos | Claude | Opus 5.5 high, one agent per deck, checked with `scripts/assign_copies.py` | pending step 4 |
| 6 | Bracket 3 gate: Layer A, Game Changers, no reversible cards | Claude | `scripts/check_list.py`, `scripts/ladder.py` | ready |
| 7 | Commander Salt score of each list (Moxfield, one deck at a time, human pace) | Claude | Haiku 5.5 max in the browser, `rate-deck` skill | pending step 5 |
| 8 | Pull list by binder and deck, and the tokens each deck makes against the tokens he owns (exact tokens) | Claude | `scripts/assign_copies.py` (updated and tested) | ready |
| 9 | Dashboard: lists, statistics, the guide of each deck (how to use each card, written by Opus), images; English on his word | Claude | Opus 5.5 high for the guides, scripts for the rest | pending step 7 |
| 10 | Close: README, memory, one commit on his word | Claude | | pending |

Rules kept in the tools: a bilingual deck takes the English copy when a card is owned in both languages (Spanish when only
that exists); the Spanish deck takes Spanish copies only and is served first; a copy sits in one deck; the Ezio commander is a
proxy declared in `decks/phase2.json`; every shortage and every card shared by two decks is listed, never hidden.

No score target (owner, 2026-10-26): each of the three decks is improved as much as the collection allows, and the fourth is
the best deck the Spanish collection can make, commander included. Commander Salt is a measure to compare candidate lists,
never a target; the only gate is Bracket 3 (Layer A). The 7.0 yardstick of Phase 1 no longer applies.

Open decision for the owner: whether the optimizer may take any card out of the three current lists freely (the lock list
is empty, so by default yes).
