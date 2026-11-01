# Multiplayer: threat assessment, politics, pacing, Bracket 3 expectations

Sources: notes in `docs/research/commander-deckbuilding/notes/`, mainly notes/05, notes/11 and notes/12. Almost all of
this is opinion from experienced authors; no source reports a sample size. It shapes construction mainly through what a
deck must be able to survive and how visible it is.

## 1. Threat assessment (what the table will target)
- Threat assessment is ongoing: find the players and cards nearest to winning or to stopping you. Indicators: card
  advantage, mana, board presence (quality and quantity), combo potential, engines, life total; none decisive alone
  (notes/05 S3).
- Life total is the clock, not the score; engines, growing creatures and layers of protection are the real threats
  (notes/11 S6).
- A wide board one or two combats from lethal is a top removal priority; quality counts with quantity (notes/05 S4).
- Build-around threats keep coming back; keeping them off the table can matter more than anything else (notes/05 S3).
- Cards that make you the target (big card-advantage engines, a single huge creature) draw removal (notes/06 S7). A big
  voltron creature makes its controller the archenemy (notes/11 S16).
- With three opponents, the table gets about three answers for each card you draw (notes/05 S4, opinion). Section 6 turns
  this into counts.
- Construction consequence: a deck that will be the visible threat needs answers to being targeted (protection, counters,
  wipes), not only answers to the table's cards (notes/05 S3).

## 2. Politics
- How much politics matters is disputed: one author says threat evaluation decides games and politics adds little (notes/05
  S2); another treats politics as tactics on top of it (notes/05 S3).
- Visibility conflict: being seen as dangerous deters attacks and hiding strength makes you the easier target (notes/05 S2;
  notes/12 C1 density); talking down your threat makes opponents hold removal (notes/05 S3). Construction choice [J]:
  deterrents that are always on (deathtouch blockers, punishers) work whether or not you look dangerous.
- Never break a deal; word deals precisely; banding against an archenemy is a normal deal (notes/11 S7).
- Griefer cards (global locks, shuffle hazards, all-lands destruction) draw battle lines and the group gangs up (notes/11
  S8). Removing the same commander again and again is unfun in many groups (notes/11 S5).
- Opponents who see you profit from their creatures dying, or from reanimating their cards, stop cooperating (notes/10
  S8, S11).
- One-sided deterrents keep the table fighting each other; whole-table deterrents work against your own position
  (notes/12 C7, single forum source).

## 3. Pacing and closing
- Bracket 3 expects at least six turns before a game ends; Wizards says a seventh-turn ending is acceptable. These are
  expectations, not limits (notes/05 S1; `docs/research/commander-brackets-rules-snapshot.md`). An EDHREC author calls six
  optimistic (notes/09 S12).
- Bracket 3 wins arrive in one big turn from resources built earlier; Bracket 3 Game Changers tend to be card-advantage
  engines and game-enders (notes/05 S1).
- With four players each extra turn raises the chance another player wins; commit when ahead (notes/05 S4).
- Name the two or three real ways your deck ends games before the game; add up the damage out loud; count open mana before
  the kill; do not spend a turn on draw when you have lethal (notes/11 S17).
- Decide how to protect the board from a sweeper before an all-in attack (notes/05 S4).
- A deck should stabilize before it wins with its own plan (notes/12 C2, opinion).

## 4. What multiplayer does to construction (summary)
| Effect | Consequence | Source |
|---|---|---|
| Three opponents, 120 life | team-wide finishers; single-target kills are backups | notes/12 C3; notes/05 S3 |
| One-for-one trades lose ground | two-for-one answers, wipes that cost others more | notes/04 S2; notes/04 S1 |
| Several boards to get past | team evasion, evasion that ignores small blockers | notes/06 S3; notes/12 C10 |
| You attack one player and two can hit back | defense while tapped | notes/12 C1 C2 |
| The table can pool answers | layered protection | notes/06 S6 |
| Opponent-triggered draw scales | repeatable draw that counts opponents' actions is strong | notes/03 S3 |
| Free first mulligan | opening-hand odds better than the 1v1 math | notes/11 S13 |
| Removal is aimed at the leader and the visible engine | the engine needs redundancy or protection | notes/05 S3 |

## 5. Bracket 3 rules (construction)
From `docs/research/commander-brackets-rules-snapshot.md` (Wizards' beta system; snapshot 2026-02-09, checked current on
2026-10-31) and notes/01 S4 S5, notes/09 S10 to S15:
- Up to three Game Changers; one Game Changer makes a deck Bracket 3 at least; the list (53 cards after the February 2026
  revision) includes lands; Scryfall exposes it as `game_changer` and as the search `is:gamechanger`: check the LIVE list when
  you build, never a stored copy.
- No mass land denial.
- Extra turns in low quantity, not chained or looped.
- No intentional early-game two-card infinite combos (Wizards' test is whether it "tends to happen" in the first six turns;
  "not reachable in the first six turns" is the project's working convention); late-game infinite lines are
  allowed; three-card lines are not addressed by any bracket (notes/09 S15).
- Tutors have no bracket restriction of their own since the October 2025 update; the strongest are Game Changers.
- The system is in beta and still changing; cite the snapshot date with every bracket claim.
- Bracket labels have wide spread inside a bracket; turn expectations work as conversation rather than rules (notes/09
  S14).

## 6. What the table holds (computed)
Three opponents, each with a 99-card library, each having seen 7 + N cards by their turn N. Interaction counts are the
Bracket 3 medians (spot removal 5, wipes 2, counterspells 1; notes/11 S15), so the figures describe an AVERAGE Bracket 3
opponent; cards seen are not cards cast (mana, colors, timing), and tutors and draw spells raise them. Computed for this
skill (hypergeometric, opponents independent):

| By your turn | Cards each opponent has seen | Expected spot removal (all three) | Expected wipes | P(at least one wipe seen) | Expected counterspells | P(at least one spot removal seen) |
|---|---|---|---|---|---|---|
| 5 | 12 | 1.8 | 0.7 | 54 % | 0.36 | 86 % |
| 8 | 15 | 2.3 | 0.9 | 63 % | 0.45 | 92 % |
| 11 | 18 | 2.7 | 1.1 | 70 % | 0.55 | 95 % |

Uses [J]: (1) commander protection and wipe insurance stop being bare judgment: if the table aims its spot removal at the
visible engine, roughly one of the 2.3 seen by turn 8 lands on the commander, and a board plan faces a wipe in about two
games out of three; (2) the haste promotion test uses the
turn-8 removal figure as the expected number of recasts (`win-routes.md` section 4); (3) a kill that needs three resolutions
meets the same numbers three times. The medians describe sampled decks, not your pod: read the actual pod's colors first.
