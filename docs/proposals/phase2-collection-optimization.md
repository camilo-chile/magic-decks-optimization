# Phase 2 plan: four decks from the owned collection (2026-10-26)

Owner decisions of 2026-10-26: iteration 1 is closed; iteration 2 optimizes Toph, Ezio and Azula (bilingual) and a fourth
deck (Spanish cards only) from the cards he already owns. He wipes the collection and the decks and rescans everything
(basic lands and tokens included) into two binders, Spanish and English. The Standard cards are not scanned and never used.
Decks stay plain decklists, not registered in ManaBox, so no card counts twice. Claude chooses the fourth commander (the
Spanish "Counter Intelligence" precon is the base, a better commander is welcome). Quality criterion: broad synergy and
stand-alone value in 3 to 4 player pods next to the Commander Salt power (see `docs/research/phase2-play-review-20261026.md`).

| # | Step | Who | Tool or model | State |
|---|---|---|---|---|
| 1 | Wipe, then rescan by stages into the Spanish and English binders (owner, 2026-10-30): Ezio, Azula, Toph, the rest; after each stage export one full CSV of both binders to `data/collection/ManaBox_Collection_<date>_<stage>.csv` | Owner | ManaBox on the phone | Ezio export on its way |
| 1b | Which deck holds each physical card: the rows new against the previous export belong to the stage's deck; exact printing, finish, language, condition and proxy kept; the scanned deck is written as a Moxfield-style text and compared with its planned list | Claude | `scripts/collection_stages.py` (written and tested; first real run with the Ezio export) | ready |
| 2 | Build the inventory; read the problem list with him (scan errors: a card in the binder of the other language, unknown names, proxies, conditions) | Claude | `scripts/build_inventory.py` (updated and tested; reads the newest, most complete export) | ready |
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

## Consistency gate (owner, 2026-10-30)
Evidence (two games with one deck: a signal about what to look for, not proof; the gate applies to all four decks): he
played the Ezio list (Salt 7.7) twice in pods of 3 to 4 and lost both heavily to a friend's deck that Salt rates far lower. His diagnosis: the list mixes many strategies, each with one to three support cards. A rough count on the
Oracle text of the Phase 1 list (regex, so approximate) agrees: reanimation 2 cards plus Winter Soldier conditionally
(Restart Sequence, The Revelations of Ezio); vehicles 0 besides Adéwalé itself, whose recursion asks for one; equipment 2
(Assassin Gauntlet, Swiftfoot Boots) for Winter Soldier; blink or bounce 3 (Deadeye Navigator, Kaya, Venser) for the
enter-the-battlefield effects of Adéwalé; 24 creatures; one win route (Ezio's combat damage with menace as the only evasion
of the commander). Chance of seeing at least one of k pieces in the first 15 cards of 99: k=2 28 %, k=4 49 %, k=8 75 %,
k=12 88 %. Salt measures the potential of ideal draws, not resilience in a pod with wide or bigger boards.

The gate for the four lists, before any Salt run (the numbers are a first draft to calibrate; a prior-art survey of
Commander building templates and hypergeometric tools goes first, per the prior-art rule):
1. ONE primary plan, plus at most one backup that reuses most of its pieces; named in the rationale file of the list.
2. Every one of the 100 cards is tagged: plan engine, plan payoff, backup, ramp, draw, removal or interaction, protection,
   land, or ORPHAN (useful only if a specific partner appears). Orphans: at most 3.
3. Density: each function the plan needs (enabler, payoff, recursion, evasion, a way through blockers) has at least 8 pieces
   (about 75 % to see one by 15 cards), or the plan does not use that function. A card whose effect needs a package that the
   list cannot supply (Adéwalé with no vehicles or blink) is an orphan.
4. At least two independent ways to win, and an answer to wide boards (chump blockers) and to bigger creatures: evasion,
   removal, sweepers, or a non-combat route. Combat damage alone is not a plan in a 3 to 4 player pod.
5. Base health: ramp, card flow, interaction and protection at the usual counts of the community templates (to confirm in
   the survey), so the plan is not the only thing the list does.
6. Commander Salt only breaks ties among lists that pass.
`scripts/plan_density.py` (to write with the first list) reads the tags and computes the odds; Opus 5.5 high reviews the tags.
