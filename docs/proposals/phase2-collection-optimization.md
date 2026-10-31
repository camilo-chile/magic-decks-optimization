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
| 3 | Pools: every owned card legal in each commander's color identity, with Oracle text, copies by language and the decks that hold it; a table of the owned legendary creatures with the size of their Spanish pool | Claude | `scripts/build_pools.py` (written and tested; run on the three scanned decks, final run after the rest scan): `pool-<slug>.json` per deck and `legends.md` | pending the rest scan |
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

## Consistency gate (owner, 2026-10-30; revised after the Opus review of 2026-10-31)
Evidence (two games with one deck: a signal about what to look for, not proof; the gate applies to all four decks): he
played the Ezio list (Salt 7.7) twice in pods of 3 to 4 and lost both heavily to a friend's deck that Salt rates far lower.
His diagnosis: the list mixes many strategies, each with one to three support cards. A rough count on the Oracle text of the
Phase 1 list (regex, so approximate) agrees: reanimation 2 cards plus Winter Soldier conditionally (Restart Sequence, The
Revelations of Ezio); no vehicles for Adéwalé's Vehicle clause; equipment 2 (Assassin Gauntlet, Swiftfoot Boots) for Winter
Soldier's Equipment clause; blink or bounce 3; 24 creatures; one win route (Ezio's combat damage, menace the only evasion of the
commander). Salt measures the potential of ideal draws, not resilience in a pod with wide or bigger boards.

The gate for the four lists, before any Salt run, is `scripts/plan_density.py` reading `decks/phase2/<slug>.plan.json` (schema
in the script). Sources: the survey `docs/research/phase2-consistency-survey-20261031.md` (package size 8, base counts, odds);
everything else is judgment and says so in `GATE`. The adversarial review is `docs/research/phase2-gate-review-20261031.md`.
1. ONE primary plan, plus at most one backup that reuses most of its pieces.
2. Every non-basic card has a tag (a second one allowed): engine, payoff, backup, ramp, draw, removal, wipe, tutor, protection,
   land or orphan. Orphans, at most 3, are the declared ones PLUS every engine, payoff or backup card that sits in no function
   and no win route (so dropping a short function does not hide its cards).
3. Functions the plan leans on, each with "needed_by": EARLY functions (needed by turn 5, 12 cards seen) need 10 or more
   pieces; LATE ones (finishers, recursion, closing; judged at 20 cards) need 6 or more. The commander counts as a guaranteed
   piece of any function that lists it, and a tutor counts as a piece of the functions it can fetch for. Cards seen by turn T
   are 7 + T (no player skips the first draw in multiplayer; Comprehensive Rules 103.8c, recalled, not re-read).
4. Two reference-board functions are mandatory, with the same rule: a way through a wide board of small chump blockers
   (`through_wide_board`) and through creatures bigger than yours (`through_big_creatures`).
5. At least two win routes, disjoint, with a declared axis (combat, noncombat or alternate), at least one that does not need
   combat damage, every card in the list or the command zone, and a sentence on how each beats THREE opponents, not one.
6. Base health (warnings, sourced): lands 36 to 38, ramp 10 or more, draw 8 or more, removal 8 or more, wipes 2 or more,
   protection 3 or more (no source, judgment). Cards that are bad when drawn early, late or never are listed; warn over 12.
   `scripts/function_tags.py` gives an objective cross-check from Scryfall's oracle tags (`decks/reports/function-profile.md`).
7. Commander Salt only breaks ties among lists that pass.
A dead clause is not an orphan: Adéwalé's enter trigger works alone, but his Vehicle clause has no partner in the Ezio list; the
plan file must name such clauses.

Test on the list that failed (`docs/research/phase2-gate-test-ezio.plan.json`, report `phase2-gate-test-ezio-report.md`): the
revised gate FAILS it (through a wide board: 6 pieces; every route needs combat; four orphans; evasion, cheap Assassins, card
flow and any-color mana at 8 pieces). The first version of the gate failed it only on three density counts and could be passed by
editing the plan file; the changes above close those holes.

Not built yet (backlog from the review, in order of value): tag checks against the card's type line and the Scryfall tags once
`function_tags.py` has the whole cache; a mana report (tapped lands, colorless lands, sources per color); a goldfish and London
mulligan simulation (keepable hands, plan online by turn N); creature toughness and sweeper resilience; commander protection
as its own function. The deck builders are told to do these by hand until then.
