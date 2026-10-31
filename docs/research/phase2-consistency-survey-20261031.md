# Survey for the consistency gate (read 2026-10-31)

Prior-art survey required by the project rule before building the gate (`docs/proposals/phase2-collection-optimization.md`). Two
Haiku 5.5 @ max readers (web) plus one direct API check. Page facts come from the agents' reports (WebFetch summaries) and are
dated; anything not sourced is marked unverified. EDHREC, Archidekt and Moxfield were not queried by automation.

## 1. Deckbuilding templates (counts per 100-card Commander deck)
| Source (date) | Lands | Ramp | Draw | Removal and wipes |
|---|---|---|---|---|
| Nerd Leagues, the 8x8 method (2026-08-03) | 36 to 38 | 8 to 12 | 10 to 12 | 8 to 10, 2 to 3 of them wipes |
| ScrollVault, medians of 6,532 Archidekt decks at Bracket 3 (2026-09-07; owner-set brackets, text matching) | 36 | 13 | 10 | 5 spot removal + 2 wipes |
| EDHLab (2026-04-28) | 37 floor, precons 37 to 39 | | | |
| MTGGoldfish (2017-05-05) | 37 to 40 | about 10 to 13 (derived) | "some" | "some" |
| Draftsim (2025-07-11) | | | | 3 to 5 wipes |
| CoolStuffInc (2026-04-27) | 43 (a Karsten adaptation, secondhand) | | | |
Where they disagree: lands 36 to 38 against 43; wipes 2 (ScrollVault) against 3 to 5 (Draftsim). Draw agrees at 10. No source
gives protection or win-condition counts. The Command Zone template counts and Frank Karsten's Commander articles were not found
(unverified): the numbers above are from secondary sources.

## 2. Plan density and redundancy
- The 8x8 method: eight themes of eight cards each. That is the only numeric rule for a package, and it supports the draft
  threshold of 8 pieces per function of the plan.
- Redundancy: 2 to 3 distinct cards per key job and 3 to 4 in singleton (a low-confidence blog); backups must be different
  cards (Star City Games 2012). No source counts tutors, recursion, evasion or sacrifice outlets.
- One copy of a card is in the opening hand only 7.1 % of the time: a single-copy must-have is not a plan.
- Wizards' Brackets update (2025-10-21): Bracket 3 asks for no Game Changer count; third parties say up to 3 (unverified on the
  Wizards page; the project's Layer A already pins its own snapshot).

## 3. Probability (99-card library, at least one of k copies in n cards seen)
The agent's table uses n = 6 + turn on the play and 7 + turn on the draw (the two-player convention). In a multiplayer game no
player skips the first draw (Comprehensive Rules 103.8c, recalled, not re-read), so every seat sees 7 + turn; `plan_density.py`
uses 7 + turn (12 cards by turn 5, 16 by turn 9, 20 by turn 13). The table below keeps the agent's labels.
| n | k=1 | 2 | 3 | 4 | 8 | 12 |
|---|---|---|---|---|---|---|
| 7 (opening hand) | 7.1 % | 13.7 % | 19.9 % | 25.8 % | | |
| 11 (turn 5 on the play) | 11.1 % | 21.1 % | 30.0 % | 38.1 % | 62 % | 78 % |
| 15 (turn 9 on the play) | | 28 % | | 49 % | 75 % | 88 % |
Formula 1 - C(99-k, n) / C(99, n) (hypergeometric, Wikipedia). The agent's table and the project's `plan_density.py` agree
(k=2, n=11: 21.1 %). No published 99-card table was found; the 8 and 12 columns come from the project's own function.

## 4. Pods
Guides agree on: a threat assessment on the biggest board, removal held until the threat aims at you, politics, and at least
one non-combat or evasive route (alternate win conditions are situational). No source gives numbers for wide boards or evasion.
The owner's own games (two with Ezio) are the only data on that.

## 5. Tools a script may use
| Tool | Verdict |
|---|---|
| Scryfall oracle tags (`otag:`) | **Yes, with a proper User-Agent and Accept header.** The agents got 403 from WebFetch; a Python request with the headers answered (checked 2026-10-31: `otag:ramp` 2,323 cards). Existing slugs: ramp, mana-rock, mana-dork, draw, card-advantage, removal, spot-removal, creature-removal, board-wipe (= sweeper), tutor, reanimate, reanimate-creature, recursion, blink (= flicker), bounce, protection, protects-creature, evasion, gives-evasion, gives-flying, gives-menace, sacrifice-outlet, mill-self, discard-outlet, counterspell, extra-combat, anthem, gives-haste, lure, fog, win-condition (70). No slug found for equipment, vehicles, token makers or goad (HTTP 404 on the names tried). Scryfall FAQ: under 10 requests per second, relevant User-Agent, Accept header, never retry a 429 in a loop (a 429 did stop one run of ours: the script now saves each tag and stops). Built: `scripts/function_tags.py` |
| Commander Spellbook REST | Yes (already used) |
| EDHREC, Archidekt, Moxfield | No: terms bar automated use (EDHREC 2024-08-06, Archidekt 2018-09-07, Moxfield §4c read 2026-10-18) |
| MTGGoldfish | No API; terms silent on automation, personal use only |
| EDHTop16 | Public GraphQL, cEDH only, terms bar excessive automated requests: not useful here |
| digitalkw EDH Power Calculator | Web form, formula hidden |
| Open-source simulators (Fozefy hand-simulator MIT 2020, Manabase GPL-2.0 2015, others stale or Rust or Java) | Nothing maintained that counts plan pieces; the hypergeometric function is three lines, so it is built (`plan_density.py`) |

Gap that remains and is built: nothing existing measures a list against its OWN declared plan (pieces per function,
orphans, independent win routes). `scripts/plan_density.py` does, with Scryfall tags as an objective cross-check.

Note: this survey's agent read the terms pages of four deck hosts (Archidekt, EDHREC, MTGGoldfish, EDHTop16) because the prompt
asked for it, against the earlier rule "do not read other deck hosts' terms" (CLAUDE.md, about Moxfield and its neighbors;
EDHREC and Archidekt were already read on 2026-10-11 and 12). Public pages only, nothing else happened; the rule stays.
