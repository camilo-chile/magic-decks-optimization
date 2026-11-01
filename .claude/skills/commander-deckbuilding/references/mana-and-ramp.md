# Mana: lands, ramp, colors, curve, window mana and window costs

Sources are the notes in `docs/research/commander-deckbuilding/notes/` (file and source ID). Revision 2 added notes/13:
K1 K2 K3 = Frank Karsten's three TCGplayer articles (read in full), CZ-new = the Command Zone 2025 template (two written
summaries), CZ-old = the earlier template as quoted in 2022, E1 = EDHREC Bracket 3 average decks counted by function,
PG = Playgroup.gg opening-hand data. Probability tables are in `probability.md`.

## 1. Land count

### What the sources say

| Figure | Scope | Source |
|---|---|---|
| 38 | Command Zone 2025 template ("start at 38"; 3+ lands in the opening 7 about 55 %) | notes/13 CZ-new |
| 42 + Sol Ring, minus 1 land per 2 to 3 extra rocks, per 3 to 4 cheap cantrips, per 3 to 4 dorks; "try not to go below 37" for medium-power midrange | Karsten's goldfish simulation of mana spent over 7 turns, 99 cards | notes/13 K1 |
| 36 to 40 | casual Commander, most guides | notes/06 S8; notes/03 conflict 2; notes/11 S4 |
| 38 to 40 (most casual), 38 to 42 (typical casual), 40 to 44 (high average MV), 36 to 38 (low curve with card draw), 38 to 40 (five colors) | Playgroup bands | notes/02 S1 |
| cEDH 29 to 31; combo 33 to 35; midrange 36 to 37; battlecruiser 38 to 40; landfall 38 to 40 | ScrollVault simulation, cast rates | notes/02 S2; notes/11 S14 |
| Bracket 3 median 36 (middle half 34 to 37) | 1,285 self-declared Bracket 3 decks on Archidekt | notes/11 S15 |
| Bracket 3 averages: landfall 39.5 (38 to 46), spellslinger 35 (34 to 36), combat 35.5, tokens 35, voltron 35, aristocrats 35.5, counters 35 | EDHREC average decks, 54 commanders: community behaviour, not quality | notes/13 E1 |
| 35 (Bracket 3 average, Atraxa); 39 (the one landfall average read); 34 to 35 (sample lists of spellslinger, counters, tokens, aristocrats, voltron) | EDHREC | notes/09 S20; notes/10; notes/06 S11 |
| 37 with 36 as floor | MTGGoldfish checklist | notes/03 S1 |
| 43 baseline, range 36 to 46 | a 2026 column adapting Karsten's 60-card math | notes/08 S3 (secondary) |
| "just over 29" (2019 EDHREC average) | old average, judged too low | notes/09 S5 |
| No measured deck-level land count against win rate exists | Playgroup gives opener data only; Karsten: "hard to find data on a deck's performance" | notes/13 section 4 |

Karsten calls the community's 36 too low (notes/13 K1). Near the optimum the curve is flat: a deck one land off scored
99.96 % of optimal and a six-lands-for-six-threes swing about 98 % (K1), so lean to the safe side rather than agonize.

Formulas (cross-checks, not rules):
- **Karsten's regression, read in the primary** (notes/13 K2): lands = 31.42 + 3.13 × average MV of nonland cards − 0.28 ×
  cheap (MV 2 or less) draw-or-ramp pieces. CORRECTION to earlier notes: it comes from **95,143 sixty-card tournament decks**
  (MTG Melee and Magic Online, 2020 to 2022; R-squared 0.395), scaled to 99 cards and calibrated to the 42-land optimum of
  the simulation K1. It is **not Commander data**, and Karsten calls it "an imprecise back-of-the-envelope estimate". Worked
  examples: midrange (MV 3.0, 10 cheap pieces) 38.0; battlecruiser (3.5, 8) 40.1; landfall (3.0, 6) 39.1; spellslinger (2.5,
  20) 33.7. Adjust per card: efficient reliable ramp or one-mana cantrips cut a land per 2 to 3; fragile or inefficient
  ones (two-mana cantrips, dorks) one per 4 to 5.
- **Burgess rule of thumb**: lands = 31 + number of colors + commander's mana value, zero-cost rocks counted as lands
  (notes/09 S5).

### What to choose (Bracket 3, 3 to 4 players)
Start from the archetype's `land_band` in `archetypes.json`. Lean toward the higher end when: the curve averages above
3.2; the commander costs 5+; the deck wants lands in hand (extra land drops, landfall); the deck sacrifices lands. A band
below 36 is allowed only while BOTH hold: average MV under 2.8 AND 10+ cheap (MV 2 or less) ramp, draw or cantrip pieces;
write both numbers in the profile table [J]. Reason for leaning high in casual pods: missing land drops loses more games
than a little flood, and the named fixes for flood are utility lands and card advantage, while the named mistake is
cutting lands (notes/03 S1, S6). Every ramp piece is not a land: a turn-2 rock helps only if the third land arrives
(notes/03 S5). In the opening seven, 3+ lands is 55 % at 38 lands, 50 % at 36, 59 % at 40 (computed, `probability.md` D):
a deck that keeps only 3+ land hands wants about 40 lands.

## 2. Ramp

### Counts
- Command Zone 2025: 10, or **12 when the commander costs 4 or more**; rituals do not count; too much ramp at the cost of
  lands is counterproductive (notes/13 CZ-new). The 2022 template said 10 to 12 (notes/13 CZ-old).
- Karsten: rocks pay off only with a 4+ MV commander (7 to 9 Signet-type rocks plus Sol Ring for MV 4 to 6, none for MV 2
  to 3); a deck under 38 lands with more than nine rocks may do better swapping a rock for a land (notes/13 K1).
- About 10 for a generic deck (notes/02 S4 Draftsim; notes/09 S17 EDHREC guide; notes/12 C3 opinion: 10 to 12 for
  mid-power decks); 8 to 10 ramp spells on a 40-land base for a first deck (notes/07 S2).
- 13 in the MTGGoldfish checklist (notes/03 S1); Bracket 3 median 13, middle half 10 to 18, counting rocks, fast mana and
  rituals (notes/11 S15). EDHREC Bracket 3 averages by the (broad) ramp tag: landfall 28.5, tokens 17, aristocrats 17,
  counters 20, combat 13.5, spellslinger 13, voltron 10 (notes/13 E1).
- Big-mana commanders up to 15; the author has seen 20; his personal minimum is 7 (notes/09 S17).
- A landfall plan sits at or above the top of the Bracket 3 range (18+) [J, owner signal]. No EDHREC source gives a landfall
  total and the 2019 note says landfall decks run fewer rocks and more land ramp (notes/09 conflict 2).
- 14 ramp cards: 80 % to see one by turn 3; 20: 90 % (notes/03 S1, reproduced).
- Definitions differ: one source counts only spells that put lands onto the battlefield (notes/07 S1); others count
  land fetch, rocks and dorks (notes/07 S2); the Bracket 3 survey counts rituals too (notes/11 S15). Compare counts only
  under one definition. This skill counts anything that adds lasting mana or a land on the battlefield; rituals and
  one-shot bursts count only for a plan that spends the burst the same turn.

### Types (notes/02 S4)
Land ramp (onto the battlefield); mana creatures; rocks; treasure makers; extra land drops; land recursion; one-shot
bursts; cost reducers; mana doublers; temporary mana. Ramp that does a second job is preferred: a removal spell that
later becomes a mana outlet, a creature that blocks and is later sacrificed for a land, ramp that stocks the graveyard,
land recursion with extra land drops (notes/02 S4).

### Matching the type to the plan
| Plan | Prefer | Why |
|---|---|---|
| Landfall / lands | land ramp onto the battlefield; extra land drops; several lands per spell; land sacrifice that nets a land | each land entering is also fuel (notes/07 S1; notes/09 S5 landfall decks run fewer rocks and more land ramp; notes/11 S14 landfall preset uses land ramp in place of rocks) |
| Voltron / commander on turn 3 | 8 to 12 rocks | cast the commander early and hit land drops (notes/11 S16, opinion; notes/13 K1 for a 4+ commander) |
| Spellslinger | treasure from spells, cost reducers that work in the commander's window | treasure is the archetype's stated mana answer (notes/07 S4); rituals are same-turn only (notes/10 S7) |
| Aggro | cheap ramp, about 10, ahead of early draw | opinion (notes/12 C3) |
| Big mana | 12 to 15+ of any lasting type | notes/09 S17 |

### Timing and late ramp
- Ramp gains value once lands outnumber turns; past about five mana a spell is no longer really ramp (notes/07 S1).
- A card's value depends on the game stage: an early ramp card excels on turn 2 and is weak on turn 7 without a draw
  engine (notes/01 S6). Corollary [J]: a mana permanent whose output depends on what you pay when you cast it, or on a
  count that grows later (an X cost, counters it enters with, a party or devotion count), is a turn-2 to turn-3 card when
  small; cast late it often wastes the turn, unless the deck can grow it. Judge it for THIS deck's curve and mechanics.
- A mana permanent that is also plan fuel (it is a land entry, or an artifact or creature that a payoff counts) is counted
  in the fuel function; it counts in `ramp` only if the deck casts it by turn 3. Cast late it is not wasted: it still
  triggers its payoffs. Say which function carries it [J].
- Surplus: ramp that later becomes a card keeps its value; if the mana is not needed, even the best rock is close to dead
  after the opening hand (notes/07 S2). A ramp-heavy plan needs sinks.
- Sol Ring is the only card that survived correction in a 143-card screen of win-rate effects; its edge shrinks from
  +12.7 points in duels to +3.7 in four-player games (notes/02 S3). Editorial ranks of other rocks are opinion, not
  measurement (notes/02 conflict 5). Playgroup's per-card ramp lifts are small (a few tenths of a point to about 4 points,
  search summaries only, notes/13 section 4).

## 3. Extra land drops, land recursion and basic-fetching ramp (landfall plans)
- One land per turn is the normal limit. Extra land plays need a land in hand. Play the top card of the library first with
  top-of-library effects (notes/07 S1).
- Several lands per spell, land sacrifice that fetches two, and creatures that fetch a land on entering are the sourced
  mechanisms (notes/07 S1). Repeated entries: only one explicit case is sourced (a creature that searches again when it
  re-enters, notes/07 S1). Land recursion and "play lands from your graveyard" appear in snippets (notes/10 N3, N4) and in
  the community averages: a median of 7 extra-land-drop cards, 6 land-recursion cards and 16 lands put onto the battlefield
  in Bracket 3 landfall decks (notes/13 E1).
- Count extra land drops on their own line, not inside the ramp total (notes/07 inference).
- **Re-entry engines [J].** A free or cheap sacrifice outlet paired with a land (or a land that became a creature) that
  returns to hand or to the battlefield when it dies is a repeatable entry engine: each pair gives about one entry per
  outlet use. Count the pair under the repeatable engines of the entries-per-turn budget and name both cards.
- **Entries per turn [J].** Write the land entries per turn the deck can make at turns 4 to 8: 1 natural + repeatable
  permanents on the board (each adds one entry or one extra drop every turn) + one-shots spread over the turns (each adds
  one entry once). The aim for a landfall plan is 2 or more a turn. A repeatable engine counts for every turn it is out;
  a one-shot counts once, so 10 to 14 one-shots give only about one extra entry every 2 to 3 turns, and a fetch land
  gives two entries from one drop. With 7 repeatable engines only 61 % have one by turn 5 (`probability.md` A): the gap
  is filled by one-shots, so keep both kinds.
- Extra land drops create surplus mana: the deck needs payoffs and sinks for it (notes/07 inference from S1 and S2).
- **Basic-fetching ramp needs basics.** Spells that search for basic lands (or basic land types) find nothing in a base of
  nonbasic duals; keep at least about 8 basics of the types they fetch, and count a fetched dual as a bonus, not as the
  plan [J].

## 4. Colors, tapped lands, utility lands

### Karsten's colored-source table (notes/13 K3)
Sources (lands, rocks and dorks that make the color) needed in a **99-card deck with 41 lands** to cast a spell on curve,
read at turn = mana value. "Consistent" means at least **89 + M %** to have the needed sources by turn M, on the play,
CONDITIONAL on having drawn M lands by turn M, after the free multiplayer mulligan. C = one colored pip.

| Cost | Sources | Cost | Sources | Cost | Sources |
|---|---|---|---|---|---|
| C (turn 1) | 19 | 1CC | 28 | 4CC | 22 |
| 1C | 19 | 2CC | 26 | 5CC | 20 |
| 2C | 18 | 3CC | 23 | CCC | 36 |
| 3C | 16 | CC | 30 | 1CCC | 33 |
| 4C | 15 | 2CCC | 30 | 3CCC | 28 |
| 5C | 14 | 4CCC | 26 | CCCC / 1CCCC | 39 / 36 |

- A **gold card**: take each color's need from the table, then add 1 to each requirement.
- **Partial sources** (value per color): dork 0.5 (for MV 2+); Signet-type rock 0.75 (MV 3+); two-mana land ramp castable on
  turn 2 0.75 (MV 3+); three-mana ramp 0.5 (MV 5+); one-shot Treasure 0.25 each; a cheap cantrip about the land share of
  the deck, rounded down; scry 1 about 0.2, scry 2 about 0.3; only the first 10 draw effects count; any-color land
  ramp such as a fetch-type land 2/3 of each color in a 3+ color deck; Exotic Orchard-type 0.75; fetches that find duals
  count full. Turn 1 counts only untapped sources; from turn 2 all sources count.
- With a different land count scale by share (for example 18/25 of lands blue); 60-card tables move 2 to 5 sources for
  20, 25 or 30 lands. Tapped-land tolerance is given only for 60 cards (up to 3 in aggro with one-drops, up to 9 in
  midrange); no Commander number exists.
- The earlier conflict is resolved: ScrollVault's 19 and 30 do not reproduce unconditionally (83 % and 82 %, notes/02
  conflict 4) but reproduce at 90 % and 91 % under Karsten's conditional definition (notes/13 K3).

### Procedure [J]
1. List every colored card the plan casts on curve with its cost and the earliest turn it must be cast (the commander
   first). 2. For each color, take the strictest row from the table (a double pip on turn 2 needs 26 to 30). 3. Count the
   deck's sources per color with the partial weights, lands first. 4. Under the target: add duals or fixing, or move the
   demanding card later, or accept it as a late card. 5. For colors needed **at once** (a payment of several colors in one
   step), take the joint chance from `probability.md` E2, not the single-color table. A color needed late only can sit
   near 12 to 15 sources.
- Count the colored symbols in every casting cost; rebalance by cutting the heaviest cards of an over-weighted color
  (notes/11 S8).
- When a color keeps failing, swap colorless lands for colored sources; 4- and 5-color decks should probably skip
  colorless utility lands (notes/03 S6; notes/06 S2 lists colorless utility lands in 4 to 5 color decks as a mistake).
- Tapped lands cost one mana on the turn they enter; about 4 to 6 are tolerated in Commander (uncited) and each should pay
  you back (scry, a third color). Untapped sources early, tapped ones later (notes/02 S5).
- Lands that make no colored mana by default (or make it only under a condition) count as colorless sources until the
  condition holds most games [J].
- Utility lands go in last and give no colored-source credit (notes/02 S5).
- Modal double-faced lands are excluded in this project (no reversible cards); landcyclers are the transferable part of
  the "40 lands including MDFCs" advice (notes/03 conflict 2). One-mana basic landcyclers count as tapped lands (CZ-new).

## 5. Curve
- Commander curves usually peak at 3 to 4 (notes/01 S3, descriptive); the bulk should sit at 2 and 3 and each 5+ card
  should justify itself (notes/01 S2, prescriptive). Unresolved; for Bracket 3 lean to the 2-to-3 peak.
- Command Zone 2025 shape, cards by mana value: 1 MV 9; 2 MV 18 (the peak); 3 MV 14 to 15; 4 MV 10; 5 MV 4 to 5; 6+ MV 3 to
  5; five-plus only for game-defining cards, six-mana permanents avoided unless the deck reanimates (notes/13 CZ-new, two
  summaries differ slightly). Karsten's simulation also puts the bulk at 2, 3 and 4 and runs fewer cards at the
  commander's own mana value (notes/13 K1).
- Bracket 3 median average mana value 3.11, middle half 2.83 to 3.44 (notes/11 S15). EDHREC averages by archetype: 2.5 for
  spellslinger and voltron, 3.2 for landfall and combat (notes/13 E1). One-drops and instants rise with power (notes/09 S20).
- **Mana value by role** [J]: ramp mostly at MV 2 to 3 (past turn 3 it is not ramp, SKILL.md step 4), a few interaction
  pieces at MV 2 or less so the deck can answer on the opponent's turn, plays at MV 1 to 2 (ramp included) enough to fill
  turns 1 and 2, and at most 6 or 7 cards at MV 6+ (notes/08 S14: six or seven cards at 7+ MV leave many stuck in hand).
- Overloading on 4+ mana cards is a warning; a few 5 and 6 drops are fine (notes/06 S2).
- Aggro: low-ramp aggro needs an average of 2.8 or lower; only one- and two-drops leads to missed plays by turn 5;
  skipping two-drops leaves three dead turns (notes/12 C3, opinion).
- A costly commander may be cast rarely; the 99 must carry games (notes/01 S1).

## 6. Temporary mana, mana retention and window costs
- Unspent mana drains at the end of each step and phase (notes/02 section 4, summary level, not checked against the
  Comprehensive Rules).
- Some effects keep drained mana as colorless (pays generic costs only), some keep one color, some keep all mana
  (notes/02 section 4). Retention helps only when the deck makes mana it cannot spend in the window (notes/02 inference).
- Mana with its own duration ("lasts until end of combat") may not be kept by an effect that only stops mana from emptying
  at the end of a step or phase: read the keeper's text and the rulings. If that is unverified, score the keeper as half a
  bridge and put the rules point in the notes for the owner [J].
- Temporary mana is a ramp form (notes/02 S4). Treasure is permanent mana and does not solve a window problem (notes/07
  inference).
- Rule for the builder [J]: if the commander makes mana only during one step or phase (combat-only, end-step-only, made on
  opponents' turns), write what the deck can cast in that window (instants, flash, activated abilities, costs payable in that
  step) and whether any card keeps or converts the leftover. A card that solves that problem is a role-player for this
  commander; judge it by the mana it saves per turn, not by its general rating.
- **Window COSTS, the opposite problem** [J]. When the commander's payment (an activation, an alternative cost, a
  condition of its trigger) must be made inside a window, the window is a cost to budget, not a gift:
  1. Name the payment: how much mana, which colors and whether all must be paid at once.
  2. Count the sources that are UNTAPPED at that step, not the sources in play: mana spent in an earlier phase of the same
     turn is gone, so the plays that compete for the same mana (alternative costs, flash spells, equip, the commander's
     own activations) set how much is held back.
  3. The odds of having the right colors at once come from `probability.md` E2 (the joint-color table), and instant-speed
     fixing (any-color mana at instant speed, treasures held, untapped duals) raises them.
  4. If the payment is more than the turn can pay, the card is a once-per-game or once-in-a-while effect: count it that
     way in the plan (do not count it as a repeated trigger), or add cost reducers or window mana that pays for it.
  A card that makes the payment cheaper or fixes its colors at instant speed is a role-player for this commander.

## 7. Diagnosis (mana)
- Mulligans of one-land hands point to too few lands (notes/03 S6).
- When a color keeps failing: colored sources, not more lands (notes/03 S6).
- Hands full of 4+ drops: lower the curve (notes/03 S6 via section 5 inference).
- Key cards expensive: add ramp (notes/03 S1).
