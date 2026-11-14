# Champion addendum to the commander-deckbuilding skill (step 0 of the final rebuild, 2026-11-08)

Purpose: the owner's mandate (`docs/proposals/final-rebuild-brief-20261108.md`) asks that each deck be built as the best
Commander player in the world would build it, for an unknown 3 to 4 player table. This file checks the skill
(`.claude/skills/commander-deckbuilding/`) against what a world-class multiplayer and high-power/cEDH builder applies,
marks each item covered, thin or missing, and gives the distilled rule for every thin or missing item. It never weakens a
project rule: Bracket 3 RULES (at most 3 Game Changers, no mass land denial, no chained extra turns, no early two-card
infinite), the consistency gate as a floor, the language rules, no reversible cards.

Conventions: **[J]** = builder judgment (no source gives the number); a source ID names where a fact comes from. Article
facts were read through page extractions on 2026-11-08 (spot checks, not card evidence); card text is always re-read on
Scryfall or the Oracle cache before a card is counted. The commander-specific findings are in
`commanders/<slug>-primers-20261108.md` (Ezio, Azula, Toph, Kilo as `spanish-deck`).

## Sources (all read 2026-11-08)
| ID | Source | Author, date | URL |
|---|---|---|---|
| G1 | "Can I Keep This? How to Mulligan in cEDH" | Matt Sperling, TopDeck.gg, 2023-01-06 | https://topdeck.gg/articles/can-i-keep-this-how-to-mulligan-cedh |
| G2 | "How Many Lands Should You Play in cEDH?" | Sam Black, Commander's Herald, 2024-03-19 | https://commandersherald.com/how-many-lands-should-you-play-in-cedh |
| G3 | "EDHREC Guide to Interaction in cEDH" | Harvey McGuinness, EDHREC, 2026-01-13 | https://edhrec.com/guides/edhrec-guide-to-interaction-in-cedh |
| G4 | "A Beginner's Guide to cEDH" | Corey Williams, Commander's Herald, 2024-11-13 | https://commandersherald.com/?p=40871 |
| G5 | "How Many Counterspells Should You Run in Commander?" | DonSpider, Nerd Leagues, 2026-08-11 | https://www.nerdleagues.com/blog/how-many-counterspells-commander |
| G6 | "The Rise of Compact Combos" | Nerd Leagues, 2026-06-22 | https://nerdleagues.com/blog/the-rise-of-compact-combos |
| G7 | Tutors from real Commander game data (222,652 decks; win-rate lift vs same-commander decks without the card) | Playgroup.gg, computed 2026-11-05 | https://playgroup.gg/commander/tutors |
| G8 | Counterspells, same method | Playgroup.gg, computed 2026-11-05 | https://playgroup.gg/commander/counterspells |
| G9 | Board wipes, same method | Playgroup.gg, computed 2026-11-05 | https://playgroup.gg/commander/board-wipes |
| G10 | "How To Be New at Threat Assessment in Commander" | Roman Milan, EDHREC, 2026-01-13 | https://edhrec.com/articles/how-to-be-new-at-threat-assessment-in-commander |
| G11 | "The Problem With Politics In Commander" | Erik Tiernan, StarCityGames, 2016-07-18 | https://articles.starcitygames.com/articles/the-problem-with-politics-in-commander/ |
| G12 | Live Game Changer list (53 cards) | Scryfall API, 2026-11-08 | https://api.scryfall.com/cards/search?q=is:gamechanger |
| G13 | EDHREC Bracket 4 (`optimized`) and cEDH pages and average decks of the four commanders | EDHREC JSON, live 2026-11-08 | https://json.edhrec.com/pages/commanders/<slug>/<optimized or cedh>.json ; .../average-decks/<slug>/<optimized or cedh>.json |
| G14 | Snippets only (search results, pages not read; direction, not numbers to rely on): 3 to 6 tutors in a focused casual deck, 8 to 12+ in cEDH (a non-EDHREC guide); "the average blue cEDH deck has about twelve pieces of interaction" (Library of Leng); "cap tapped lands; most hands want an untapped turn-one play" (Geeky Domain) | various | search 2026-11-08 |
| Pn | The four primers: `commanders/*-primers-20261108.md` (EDHREC high-power article on Azula, Draftsim Azula and Kilo guides, DougY's cEDH Toph article, MTG Rocks Kilo combos, Commander Spellbook cache) | | see each file |

Best five: G1 (mulligans), G3 (interaction, by a cEDH writer), G7 to G9 (outcome data: the first win-rate evidence the
project has for card types), G2 (mana sources at high power), G13 (what B4 and cEDH lists of these exact commanders run).

## 1. Checklist and status (41 items: 18 covered, 16 thin, 7 missing)
| # | What a champion knows and applies | Status | Where in the skill / rule here |
|---|---|---|---|
| 1 | One plan plus a backup that reuses its pieces | Covered | P-1, S-2 |
| 2 | Every card does something alone and with many others (synergy density) | Covered | P-3, S-9 |
| 3 | Redundancy and diversity of key effects | Covered | card-flow 6 |
| 4 | Multi-role slots (more jobs per card) | Thin | R4 |
| 5 | Commander-centric versus commander-agnostic balance | Missing | R5 |
| 6 | Land count from curve and ramp | Covered | S-4, mana 1 |
| 7 | Colored sources (Karsten 99-card table), joint colors | Covered | mana 4, probability E2 |
| 8 | Total mana sources (lands + lasting ramp) | Thin | R8 |
| 9 | Fast mana that is not a Game Changer | Thin | R9 |
| 10 | The cost of tapped lands | Thin | R10 |
| 11 | Window mana and window costs | Covered | S-4, mana 6 |
| 12 | Curve by archetype and by role | Covered | S-4, mana 5 |
| 13 | Commander mana value, tax and recast arithmetic | Covered | S-1 |
| 14 | Lands and curve at Bracket 4 and cEDH power for these commanders | Thin | R14 |
| 15 | Engines versus one-shots, card-flow budget | Covered | S-3.2, card-flow 2 and 3 |
| 16 | Card advantage that scales with three opponents | Thin | R16 |
| 17 | Development before card advantage (timing) | Missing | R17 |
| 18 | Tutors: count against speed, targets, Game Changer cost | Thin | R18 |
| 19 | Cheap instant-speed answers (mana value and speed share) | Thin | R19 |
| 20 | Stack interaction and counterspell counts | Thin | R20 |
| 21 | Wipes as a reset button: which kind | Thin | R21 |
| 22 | Graveyard hate | Covered | S-6 |
| 23 | Commander protection in layers | Covered | S-6, interaction 3 |
| 24 | Protecting the turn you go for the win | Missing | R24 |
| 25 | Answers spread across permanent types | Covered | interaction 1 |
| 26 | Compact, deterministic win routes (how to score a route) | Thin | R26 |
| 27 | Two or more disjoint routes that beat three opponents | Covered | S-7 |
| 28 | Routes that do not share one failure point (hate, removal, a counter) | Missing | R28 |
| 29 | Threat assessment and what the table holds | Covered | multiplayer 1 and 6 |
| 30 | Archenemy timing and visibility | Thin | R30 |
| 31 | Politics (deals, griefer cards) | Covered | multiplayer 2 |
| 32 | Wipe recovery and not overextending | Thin | R32 |
| 33 | Mulligan and opening-hand standards | Missing | R33 |
| 34 | Game Changer slot choice | Thin | R34 |
| 35 | Efficiency over value (mana value caps, last-slot discipline) | Thin | R35 |
| 36 | High-power cards that are NOT Game Changers, considered for every slot | Missing | R36 |
| 37 | Which combos break Bracket 3 and which are welcome | Covered | S-12 (primers flag each commander's lines) |
| 38 | Goldfish and disrupted-goldfish protocol | Thin | R38 |
| 39 | Matchup thinking for an unknown table (a gauntlet) | Missing | R39 |
| 40 | Cut process and cut log | Covered | S-11, evaluation 4 |
| 41 | Real-game evidence over a score | Covered | P-6, S-0b, lessons L1 to L10 |

## 2. Rules for the thin and missing items
Each rule says what to do, the number, and its source. Write the result of each in the build notes.

**R4 Multi-role slots [J; skill notes/03 S5].** In the last 20 nonland slots, prefer the card that fills two functions the
profile counts (removal that draws, a creature that ramps and blocks, protection that gives haste). Report the number of
nonland cards that count in two or more functions; a champion list has many, a pile has few.

**R5 Commander-centric balance [G4; J].** cEDH writers call decks full of cards that are strong only with the commander
"too commander-centric" (G4). Count the nonland cards that do nothing useful with the commander gone. For an engine or
attack-engine commander keep that count at 12 or fewer, so the deck still functions for the turns the commander is dead
(table holds about 2.3 removal by turn 8, multiplayer 6). Bridge cards (role-players section 1) count here too.

**R8 Total mana sources [G2; G14 snippet; J].** cEDH decks run high-20s lands plus 40 to 50 mana producers in all, about
half of them lands (G2, Sam Black). For a Bracket 3 to 4 deck whose commander costs 3 to 4: lands + lasting ramp at or
above 46, with lands at least two thirds of that sum (more lands because these decks draw less early, G2), landfall decks
higher. Rituals do not count here (R9).

**R9 Fast mana that is not a Game Changer [G12, G13].** Fast mana is the strongest competitive lever the Bracket 3 rules
still allow, because most of it is NOT on the Game Changer list (G12: Chrome Mox, Mox Diamond, Mana Vault, Grim Monolith,
Ancient Tomb, Lion's Eye Diamond, Mishra's Workshop, Gaea's Cradle are; Sol Ring, Lotus Petal, Mox Amber, Mox Opal, Arcane
Signet, Fellwar Stone, Talismans, Signets, rituals are not). Rules: every deck runs Sol Ring and Arcane Signet; take Fellwar
Stone and the deck's Talismans before 3-mana rocks; Mox Amber only with 10+ legendary creatures or planeswalkers including
the commander; Mox Opal only with 15+ artifacts; Lotus Petal and rituals only when the deck spends the burst the same turn
(a combo turn, a commander window such as a combat that copies instants). Rituals copied by a copying commander net double
mana: count them as plan fuel, not ramp.

**R10 Tapped lands [G14 snippet; G13; skill mana 4; J].** Every high-power average list read (G13) is built from untapped
duals, shocks and fetches. Rule: at most 3 lands that always enter tapped; conditional lands count as tapped unless the
condition holds on turns 1 to 3 in most games; each tapped land must pay back (a third color the deck lacks, scry, a
landfall bonus). A deck that plans a two-drop on turn 2 and its commander on turn 3 should have zero tapped lands among the
lands it wants on turns 1 to 3. Commander Salt's manabase signal agrees (project pitfalls).

**R14 Lands and curve at higher power [G13, G2].** Average decks of these commanders: Bracket 4 lists run 33 to 35 lands
(Ezio 33, Azula 33, Toph 34, Kilo 35) and cEDH lists 26 to 29 with 14 to 22 artifacts of fast mana. The skill's lean-low rule
still decides (below 36 lands only with average MV under 2.8 and 10+ cheap ramp, draw or cantrip pieces); these numbers show
that a low-curve, fast-mana list can legitimately sit at 33 to 35, never that a Bracket 3 deck should copy cEDH land counts.
Higher curves and longer games need more lands (G2).

**R16 Card advantage that scales [skill card-flow 2; G13].** Draw that triggers on opponents' actions or counts opponents is
worth more at a four-player table: Rhystic Study (GC), Mystic Remora, Esper Sentinel, Smothering Tithe (GC, mana), monarch,
and in attacking decks draw on each player hit. Rule: a blue or white deck runs at least 2 such pieces when the pool has
them; prefer them over flat draw of the same mana. Mystic Remora and Esper Sentinel are not Game Changers (G12) and appear
in 78 to 92 % of the cEDH lists of these commanders (G13).

**R17 Development before card advantage [G1].** "Card advantage is usually a trap without development" (G1). Rule: the
draw cards that the deck casts on turns 2 and 3 must cost 2 or less or be engines; draw at 4+ mana must draw 3 or more or
repeat. In the mulligan section, a hand of draw without mana is a mulligan.

**R18 Tutors [G7; skill card-flow 4; G14 snippet; J].** Outcome data (G7, win-rate lift against same-commander decks without
the card): Urza's Saga +2.9 points, Demonic Tutor +1.4, Vampiric +1.2, Mystical +0.8, Enlightened +0.6, Diabolic Intent +1.9,
Grim Tutor +0.8. Tutors win games. Rules:
- Count: Bracket 3 median 4; a deck whose win needs one specific card runs tutors + copies of that effect so that
  P(see the piece or a tutor by turn 7) is 80 % or more: that is 10 cards with access (probability table A, 14 cards seen).
- Targets, in order: the finisher or the missing combo piece; the win-turn shield (R24); the engine only if the engine has
  no redundancy; an answer only if the tutor is instant.
- Prefer MV 2 or less, instant speed, and tutors that find more than one function. Tutors on G12 (Demonic, Vampiric,
  Imperial Seal, Mystical, Enlightened, Worldly, Gamble, Crop Rotation, Survival, Natural Order, Gifts, Intuition) use a
  Game Changer slot; non-GC tutors include Diabolic Intent, Grim Tutor, Solve the Equation, Mystical Teachings, Muddle the
  Mixture (transmute), Chord of Calling, Green Sun's Zenith, Finale of Devastation, Urza's Saga, Tezzeret the Seeker,
  Fabricate, Reckless Handling, Loyal Inventor, Entomb (check each on Scryfall).
- Project evidence: Azula's iteration-2 list lost four tutors and its win lines came together less often
  (`docs/research/real-power-iterations-20261108.md`). Never trade tutors to the win line for generic draw.

**R19 Cheap instant-speed answers [G3; real-power review; J].** Three mana is about the most a player should spend on
interaction (G3). High-power lists of these commanders run 7 to 16 interaction pieces, mostly at MV 1 to 2 (G13: Azula B4
about 12, Azula cEDH about 16; Ezio and Kilo B4 7 to 8; Toph B4 5 to 6, cEDH about 9; G14 snippet: about 12 in blue cEDH).
Rule: spot answers (removal + counters) at least 8, of which at least 5 cost 2 or less and at least 5 are instants or
flash; none above 3 mana unless it answers two or more permanents. Each deck holds at least 2 answers to artifacts and 2 to
enchantments (G10: under-represented), and at least 3 answers castable on an opponent's turn that stop a creature-based
combo or a lethal attack. Toph lost 3 of 7 cheap answers in iteration 2: restore them.

**R20 Stack interaction and counterspells [G5, G3, G8].** Counts (G5): blue midrange or spellslinger 4 to 6, value decks 2 to
4, control 8 to 10, combo 4 to 6 chosen to protect its own win (one-mana protection such as Swan Song or Flusterstorm over
catch-all counters); a deck that taps out through turn 6 runs 2 to 4. Soft "unless they pay" counters are early tempo only
(G5). Outcome lift (G8): Fierce Guardianship +2.7, Mana Drain +3.3, Stubborn Denial +3.4, An Offer You Can't Refuse +1.8,
Force of Negation +1.8, Swan Song +1.3, Arcane Denial +1.0, Counterspell +0.6. Free or commander-conditional free spells
(Fierce Guardianship, Deflecting Swat, Deadly Rollick) are the most efficient protection a commander deck has. Non-blue
stack tools: redirects (Deflecting Swat, Redirect Lightning), Pyroblast and Red Elemental Blast, Silence, Veil of Summer,
Grand Abolisher-type effects (G3).

**R21 Wipes as a reset button [G9; G3; skill interaction 2].** Lift (G9): Cyclonic Rift +2.9 (one-sided when overloaded),
The Meathook Massacre +2.4, Toxic Deluge +2.2 (choose X to keep your creatures), Delayed Blast Fireball +3.4 (one-sided),
Damn +0.9, Blasphemous Act +0.2, Farewell 0.0. Flexible and one-sided wipes win; symmetric "everything dies" wipes barely
move the result. Rule: wipes are chosen for asymmetry or control of X, cost 3 to 4 at most where possible (G3), and a board
deck plays a wipe only if it rebuilds faster than the table (R32).

**R24 The win-turn shield [G3, G5, G6].** Defensive counters "rarely stop an opponent's win; they make sure your own winning
spell resolves" (G3); combo decks pick counters to protect their win (G5). Rule: at least 3 pieces that protect the turn
you go for the win, castable that turn at MV 2 or less or free: counters, redirects, Silence or Grand Abolisher effects,
Veil of Summer, hexproof or phasing at instant speed, a haste-and-shroud equipment already on the commander. They may
double as commander protection; list them by name in the build notes and say how the deck sequences the win around them
(cast the shield first, keep mana for it, bait a counter with a lesser spell).

**R26 Compact routes [G6; skill win-routes 1].** Score every route on: cards needed (commander included), mana on the win
turn, tutors that find a missing piece, how many pieces do something alone, and how it fails (R28). G6's criteria: fewer
pieces, less mana, fewer dedicated slots, more tutor types that reach the pieces, resilience. Rule: the primary route
needs 3 cards or fewer including the commander, or is a repeatable board engine; the deck reaches it with 10+ access
cards (R18); a four-card line is a backup at most. A route whose pieces do nothing alone is a mini-combo (L7) and is cut.

**R28 Failure points [G1, G3; J].** For each route write its single failure points: the commander removed, a wipe, a
counterspell on the key spell, graveyard exile, artifact or enchantment removal, a tax or "can't search" piece. Rule: the
routes together must survive each of these at least once: no failure point is shared by every route; at least one route
works with the commander dead; at most one route depends on the graveyard.

**R30 Archenemy timing and visibility [G10, G11; skill multiplayer 1 and 2].** Visible engines and early aggression draw the
table's removal (G10); hiding does not work and visible deterrents help (G11). Construction rules [J]: (a) the commander or
the main engine comes down with protection ready (mana up or an equipment) from the turn the plan needs it; (b) the deck
has threats that do work at instant speed or from the hand (flash, instants, attack triggers) so it can stay
low-profile until the win turn; (c) at least 2 always-on deterrents in decks that attack (skill S-8 already counts defense
while tapped). Play rule for the guide: do not present a lethal threat one turn before you can protect it.

**R32 Wipe recovery [skill interaction 4; G9; J].** No source counts rebuild pieces. Rule: a board deck lists at least 4
pieces that rebuild after a wipe within one turn cycle (a cheap or hasty commander counts as 1, recursion, burst draw,
hasty threats, token makers that make 3+ bodies, team protection used before the wipe), and the play section says how many
threats to commit before a wipe (default: what wins in two turns, keep one threat in hand when two or more opponents can
wipe).

**R33 Mulligans and opening hands [G1, G2; skill probability C; notes/13 PG].** cEDH writers treat mulligan as the default
and ask "do I have a valid reason to keep?"; the reasons, ranked: hands that win or set up a win, then development (mana
and key permanents), then interaction, then card advantage; mana is the most common bottleneck; interaction-only hands are
shipped; slow development is a mulligan even with strong cards (G1). Free first mulligan in multiplayer: with 30 lands,
shipping 0 to 1 landers gives two lands by the five-card hand 97 % of the time (G2). Bracket 3 version [J]:
- Keep: 2 to 4 lands (3+ with no 1 to 2 mana ramp) AND a play by turn 2 or 3 AND either a plan piece or a way to find one
  (tutor, draw, the commander itself when it is the engine).
- Ship: 0 to 1 landers, 6+ landers, no play before turn 4, interaction-only hands, hands whose colors cannot cast the
  commander by its turn.
- Each build notes write the deck's keep checklist, its "keep almost any land-good hand with" cards (named), and the
  keepable share computed from probability C (87 to 91 % with the free redo at 36 to 40 lands).

**R34 Game Changer slots [G12, G7, G8, G9; skill P-7].** Fill all three. Rank candidates by marginal wins for THIS plan:
(1) a tutor that reaches the primary route or a card that IS the route; (2) win-turn shield or engine protection
(Fierce Guardianship +2.7 lift, Teferi's Protection); (3) a scaling engine (Rhystic Study, Necropotence, Smothering Tithe);
(4) fast mana (Ancient Tomb, Mana Vault, Chrome Mox); (5) a reset (Cyclonic Rift +2.9). A Game Changer that does a job a
non-GC already does in the list, or that the plan does not need, loses to one that adds a new capability. Count lands
(Ancient Tomb, Gaea's Cradle, Field of the Dead) and owned GCs before proposing buys; price each candidate and write its
gain, so the owner sees what each slot buys. Check the live list (G12, 53 cards on 2026-11-08).

**R35 Efficiency over value [G3, G4, G6; skill S-9].** cEDH flex slots go to card quality and mana efficiency (G4, G6).
Rules: interaction at MV 3 or less (R19); in the last 15 nonland slots, between two cards that do the job, take the lower
mana value unless the costlier one does a second counted job; every card at MV 5+ either wins the game, answers several
permanents, or refills 3+ cards (skill mana 5 already caps 6+ drops at 6 to 7).

**R36 High-power cards that are not Game Changers [G13, G12].** Consider these for every slot of the right colors; leaving
one out that the pool or a cheap buy offers needs a reason. From the B4 and cEDH lists of the four commanders: Deflecting
Swat, Snap, Frantic Search, Swan Song, Flusterstorm, Pact of Negation, Force of Negation, An Offer You Can't Refuse,
Counterspell, Mana Drain, Lightning Bolt, Deadly Rollick, Into the Flood Maw, Redirect Lightning, Pyroblast, Red Elemental
Blast, Silence, Veil of Summer, Grand Abolisher, Esper Sentinel, Mystic Remora, Big Score, Unexpected Windfall, Borne Upon a
Wind, Swords to Plowshares, Path to Exile, Lotus Petal, Mox Amber, Mox Opal, Fellwar Stone, Dark Ritual, Urza's Saga,
Walking Ballista, Lotus Cobra, Dryad of the Ilysian Grove, Freed from the Real. NOT for Bracket 3 despite being non-GC:
Thassa's Oracle with Demonic Consultation or Tainted Pact, Isochron Scepter with Dramatic Reversal, Magistrate's Scepter
loops (extra turns), when they can happen early (check with `scripts/check_phase2_bracket.py`).

**R38 Testing protocol [G1, G2, G4; skill evaluation 5; J].** Goldfish is the champion's minimum (G4: practise mulligans,
sequence plays, track turns and cards seen). Before handing a list over, write:
1. Hands: 20 random opening hands (a seeded shuffle of the list), each marked keep or ship with R33; report the keep rate
   with the free mulligan (target 85 % or more).
2. Goldfish: 5 games to turn 8; record the turn the commander lands, the turn the plan is online, the turn of the first
   lethal threat to the table.
3. Disrupted goldfish: 3 games with (a) the commander removed the first time it acts, (b) a wipe on turn 6, (c) the first
   win attempt countered; record how many turns the deck needs to threaten again.
4. Ten games cannot rank two close lists (skill evaluation 5): use these runs to find failures, not to prove a ranking.

**R39 Gauntlet for an unknown table [G1, G11; skill S-7; J].** "Test whether your deck can beat the pod" (G11) means every
seat. Write one paragraph per opponent type and the cards that win it: (1) fast combo that wins turns 5 to 7 (which
instant answers or counters stop it, R19, R20); (2) stax and taxes (cheap threats, artifact and enchantment answers);
(3) go-wide tokens (the skill's Board 1); (4) big creatures (Board 2); (5) control with counters and wipes (R24, R32,
threats at instant speed). A deck with no answer to (1) is not tournament-ready whatever its own speed.

## 3. Champion build procedure (the order of decisions, commander to 100th card)
1. **Read the commander and its primer**: Oracle and rulings (skill S-1), then `commanders/<slug>-primers-20261108.md`:
   the strongest known lines, engines, traps, and which lines break Bracket 3.
2. **Choose the win before the cards**: score the candidate routes (R26, R28), pick the primary route and a backup that
   reuses its pieces (P-1, S-2). Set the speed target: the turn the deck should threaten the table in a goldfish.
3. **Profile**: the archetype profile and function counts from the fuel (S-3), plus the champion lines: access to the
   primary route (R18: 10+ cards), win-turn shield (R24: 3+), cheap instant answers (R19: 8+, 5 at MV 2 or less),
   table-scaling draw (R16), rebuild pieces for board decks (R32: 4+).
4. **Mana**: lands from curve and ramp (S-4, R14), total mana sources (R8), colored sources (Karsten), tapped lands (R10),
   non-GC fast mana (R9).
5. **Game Changer slots** (R34): decide the three now, because they change the tutor and protection counts.
6. **Fill**: plan functions to min (best pieces, multi-role first, R4), attack lines for attacking decks (S-8), tutors and
   the win-turn shield, interaction suite (R19 to R21), card advantage (R16, R17), then role-players and R36 cards.
7. **Puzzle check**: for every card, "what does it do alone, on the turn I draw it, and with which five cards here does it
   combine?" Cards with no answer go to the cut log (S-9, S-11, R5).
8. **Rules and gate**: 100 cards, `python scripts/check_phase2_bracket.py decks/phase2/<slug>.txt` PASS, the plan file and
   `python scripts/plan_density.py` PASS with every WARN explained (S-14). Language and no-reversible checks.
9. **Test pass** (R33, R38, R39): hands, goldfish, disrupted goldfish, gauntlet, both reference boards (S-7).
10. **Final cut pass**: list the 10 weakest nonland cards by contribution in the games where drawn; for each, name the best
    unplayed candidate (owned or a cheap buy, R36) and swap when the candidate wins in this deck; log every cut with
    function, count after the cut and replacement (S-11). Then measure on Commander Salt as the second objective (P-6).
