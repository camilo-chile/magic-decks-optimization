# Card flow: draw, selection, tutors, recursion

Sources: notes in `docs/research/commander-deckbuilding/notes/`. Odds tables: `probability.md`.

## 1. Draw counts

| Figure | Scope | Source |
|---|---|---|
| 10 effective draw pieces | baseline for a 99-card list | notes/03 S1, S2 (minimum), S3 (for a commander that does not draw) |
| 12+ card advantage | EDHREC upgrade guide | notes/09 S17 |
| 12 card advantage (cards that net two or more; cantrips do not count) | Command Zone 2025 template | notes/13 CZ-new |
| 15 to 20 | a commander built around DRAWING cards | notes/03 S2 |
| EDHREC Bracket 3 spellslinger averages: draw tag 21 (15 to 27, cantrips included), card advantage tag 25; all-deck median 10 | community behaviour | notes/13 E1, notes/11 S15 |
| 15 as default, 10 for a card-advantage commander | conflicts with the line above | notes/03 S5 (conflict 1) |
| Bracket 3 median 10, middle half 7 to 13 | counts engines and cards drawing 2+ | notes/11 S15 |
| 8x8 default 8; its beginner section 10 to 12 | template | notes/01 S2 |
| about 10, "standard"; one draw a turn is not enough | structure article | notes/04 S5 |
| 11 in one voltron list; 3 in one typal list | samples | notes/06 S11, S12 |

**Conflict and choice.** Two Draftsim articles point opposite ways on the commander's effect (notes/03 conflict 1): one
says a draw-built commander needs MORE draw (15 to 20), the other that a card-advantage commander needs LESS. They
describe different commanders. Rule used here [J; neither article speaks of commanders that spend cards, and the
extension is the skill's own]: a commander that **spends** cards each turn (casts spells, discards, sacrifices cards)
raises the draw need; a commander that **draws** by itself lowers it. Default floor 10 for everyone else; a profile goes
lower (voltron 8) only with a written reason.

Higher curves and opponents who outdraw the table call for more draw (notes/03 S2). The mana base should keep pace with
draw (notes/03 S2). With heavy tutoring, the best 5 draw pieces can be enough (notes/03 S1); at Bracket 3 tutoring is
moderate (median 4 tutors, notes/11 S15), so keep 10.

## 2. What counts as draw
- Card draw is any effect that draws; card advantage is a net gain. Instant and sorcery cantrips net no card; permanent
  cantrips do (notes/03 S2). Do not count cantrips as draw (notes/03 SN8, snippet). In a spellslinger deck cantrips are
  fuel (spell_density), not draw.
- Scry and surveil do not draw ("virtual advantage"); looting is not classified by the sources (notes/03 S2). Treat them as
  selection: they find the plan's cards; they do not refill a hand.
- Tutors are one-for-one, not card advantage (notes/03 S2). Count them on their own line.
- Repeatable sources rank first, then multi-card bursts, then cantrips and draw-on-enter; every type stays useful (notes/03
  S2).
- **Plan-tied and conditional draw** (draw when a creature connects, X spells) is a named category that pays off mid to
  late game (notes/03 S2). It counts when the deck meets the condition most turns. In a deck that connects reliably, a
  cheap combat-tied draw card is often the best draw it can run [J, consistent with notes/03 S4: fit can outweigh
  efficiency]. Weight [J]: full when the condition is met most turns; half when it is met in about half the turns; zero
  when it is almost never met.
- **Copied cantrips.** A cantrip is fuel, not draw. When the commander copies the spells you cast and the copy draws, the
  copy nets a card: count such a cantrip as HALF a draw piece in the card-flow budget while the commander is out (the
  same half weight as conditional draw, because the commander may be absent), and never in the `draw` tag [J].
- **Copies that skip additional costs or untap lands [J].** A copy is not cast, so it skips additional costs: a copied
  "discard a card, then draw" or "sacrifice, then draw" spell nets the card without the cost (count it as a draw piece at
  the half weight), and a copied mana-producing or untapping spell nets mana. Name such cases in the profile.
- Opponent-triggered draw is much stronger in multiplayer (repeatable, several cards per turn cycle); wheel effects hand
  opponents cards (notes/03 S3).

## 3. The card-flow budget [J]
Write for the plan's peak turns (usually 4 to 8):
- **Spent per turn cycle**: cards cast or discarded by the plan (a spellslinger that casts two spells in its window spends
  two; a landfall deck spends a land and a spell; an attacker deck spends one threat and one trick).
- **Gained per turn cycle**: 1 natural draw + repeatable engines on board + plan-tied draw at its realistic rate.
- If spent minus gained is above 1, the hand runs out in two or three turns. Signs: an empty hand by turn 6 (notes/03 S6),
  running out of action late (notes/03 S6). Fix by more repeatable draw, cheaper fuel, or cards that are worth two cards.
- Draw that does not move the plan forward gives the table time to find answers (notes/11 S17: value trap; do not spend a
  turn on draw when you have lethal).

## 4. Tutors
- They replace redundancy: each finds one card, so the list can cut backups (notes/03 S1). Two flexible tutors on a budget;
  more with a bigger budget (notes/03 S1). Bracket 3 median 4, middle half 2 to 7 (notes/11 S15).
- Tutors have no bracket restriction of their own since 2025-10-21; five of them are Game Changers (notes/01 S5;
  `docs/research/commander-brackets-rules-snapshot.md`).
- Use [inference, notes/03]: tutor for the single payoff, finisher or protection piece; the engine should already be in the
  list with redundancy so the plan does not depend on one tutor. Voltron: reserve tutor slots for protection (notes/11 S16).
- In the plan file, list each tutor with the functions it can fetch for: the gate counts it as a piece of each.
- Heavy tutoring makes games repetitive and tempts combo-only builds (notes/03 SN2, SN3; notes/11 X11, opinions).

## 5. Recursion
- 2 to 3 graveyard recursion effects for a deck that is not graveyard-based, counted apart from draw, because the graveyard
  may be empty early or exiled (notes/04 S5); graveyard plans run more. The MTGGoldfish checklist runs 2 (notes/03 S1).
- A deck that runs 3+ wipes, or expects them, needs more rebuild than the baseline (notes/04 inference).
- Exile answers prevent recursion; if the deck itself recurs, its own exile effects remove its targets too (notes/04
  inference).

## 6. Redundancy
- Redundancy per function is the main consistency lever (notes/03 section 3; notes/08 S12 [cEDH, general principle]:
  resilience comes from redundancy, tutor access, protection, graveyard recovery, and pieces that keep value apart from the
  combo).
- Count distinct cards per function and per turn; 60-card "four copies" logic does not carry over to singleton (notes/03).
- **Diversity** [J]. Redundancy counts different cards; diversity asks whether they fail together. When a critical function
  sits in one card type or zone (all haste on equipment, all recursion from the graveyard, all protection in one color), a
  single hate card or wipe type switches it off. Keep no more than about half of a critical function in one type or zone.
- Snippet heuristics (unverified): 2 to 4 backups for support roles, 5 to 8 for regular roles, 8 to 12 for plan-critical
  functions (notes/03 SN10). Consistent with the gate's 10 for early functions.
- An engine card needs about ten cards that work with it, or many tutors, or it should be left out (notes/11 S4, one
  commenter's anecdote).
