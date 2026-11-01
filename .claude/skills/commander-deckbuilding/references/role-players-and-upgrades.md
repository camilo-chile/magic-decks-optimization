# Role-players, bridge cards, timed ramp and upgrade mode

Builder judgment throughout [J], written after a blind test in which a reviewer following the rest of the skill read the
functions of real decks correctly but misjudged single cards: it called a resource keeper an orphan, rejected a
counters multiplier for its one bad use with the commander, and counted a slow scaling rock as ramp. The tests below
exist to catch those three errors.

## 1. Bridge cards

A bridge card does little in a generic deck and a lot with one commander, because it keeps, converts or unlocks
something that commander produces every turn. Judge it with the commander on the battlefield.

| Family | What the commander produces or lacks | Bridge examples (patterns, not a card list) |
|---|---|---|
| Window keepers | Mana that empties at the end of a step or phase (combat-only mana, end-step mana, mana made on opponents' turns) | Permanents that stop mana from emptying, that turn spent or unspent mana into counters, cards or treasure, cost reducers that let the window pay for more |
| Leaving-resource keepers | Tokens or creatures that are exiled or sacrificed at end of turn; cards exiled "until end of turn" | Effects that make the tokens stay, sacrifice outlets that pay you for them, ways to cast or keep the exiled cards |
| Bottleneck breakers | A color, card type or timing the commander needs and the deck barely has (a payment in many colors during combat, a sorcery-speed limit, a trigger that needs a permanent type) | Any-color fixing that works in that window, flash enablers, type-changing effects that supply the missing type |
| Multipliers of the main action | The action the deck repeats every turn (attacking, a land entering, a spell cast, a counter placed) | Doublers and copiers of that trigger; auras or equipment that grow when the creature performs the action |

**The test.** (1) What does the commander produce or need every turn? (2) How much of it is wasted or blocked each turn
without this card? (3) How many turns of the game does the card work? A bridge that saves a large share of the
commander's output for most of the game outranks a generic staple doing a job the deck already covers. Count it in the
function it unlocks. List it as "bridge" in the profile so a reviewer does not flag it as an orphan.

**The only keeper.** If the pool has no other card that does a window-keeper or bottleneck-breaker job, a cut needs a
replacement that does the same job; a cheaper source of the same mana does not replace a keeper. When the owner reports the
keeper winning games, the report outranks a per-turn arithmetic, which cannot see the turns the mana was kept for a spell.

**Bad use is not the card.** Before rejecting a card because one way of using it fails with the commander (for example an
aura that would be lost when the commander's mechanic returns or changes a permanent), check the other targets and
timings. Write the use that works ("put it on a creature that is not affected by the commander's mechanic").

## 2. The role-player test (every cut from an owner's list)

Answer in the cut log for each card that leaves:
1. Did the owner report it winning or nearly winning games? If yes it is a proven role-player: keep it, or write why it
   goes, for the owner to review.
2. Is it a bridge card (section 1) for this commander?
3. Which function does it serve, and what is that function's count after the cut against its min?
4. Which card replaces it, and does the replacement do the same job in the same window and turn?
5. Is the reason anything other than a score, an inclusion rate or "a better rated staple"? Those alone never justify a
   cut.

## 3. Timed ramp

1. For each mana card, write its realistic cast turn in this deck. Start from the curve: what the deck wants to cast on
   turns 2, 3 and 4 (the commander's own cast turn comes first). A 2-mana rock in a deck that wants a 3-drop on turn 3
   is cast on turn 2. A 3-mana rock competing with the commander on turn 3 is often cast on turn 4 or later.
2. Count it in `ramp` only if that turn is 3 or earlier. Cards cast later go into "late mana" and must have another use
   (draw, a body, a sink, a synergy) or be cut.
3. Scaling cards (X costs, enters with counters equal to mana spent): their value is the size the deck can afford on
   the turn they come down. One cast on turn 5 for two mana of output is a turn spent on mana; keep it only if the deck
   uses what it leaves (proliferate, artifact or creature synergies).
4. Commander cast turn: ramp exists to cast the commander and then to cast the next plays without skipping a turn. Check
   that the turn-1-to-3 ramp count gives good odds (probability.md) of casting the commander one turn early.

## 4. Upgrade mode and comparing two versions

- Start from the owner's list and his play notes. Diagnose with the profile before choosing cards.
- The fewest changes that close the gaps win; keep his engine.
- When two versions are compared, report for each: fuel and mana by turn 5; the route that beats three opponents and its
  odds; protection of the engine; the functions behind the owner's losses. Then state which failure is worse for this
  commander and why. Do not call the version that stumbles less "better" if it cannot close games, nor the reverse.
- A review proposes additions from the deck's own pool by default. Cards from another deck's pool or from outside the
  collection are named as such, so the lead can check copies and loans.
- A review that recommends cutting a card the owner reports as proven must say what the deck loses and what replaces it.

## 5. Weights that the gate does not see

- Commander-conditional pieces [J]: weight = 0.5 + 0.5 x min(1, commander-protection pieces / protection min) for an engine
  commander (full at min, half at none), so one protection card moves the count a little, not by half the function. Take a
  further discount for pieces the deck casts before the commander is usually out (its mana value or one turn later): they
  count for their other jobs only until then. The weight is also 0.5 when the commander is not an engine.
- One-shot effects in a support line count half against a repeatable permanent that does the same job every turn.
- A pinger or 1-damage effect counts half against a wide board of chump blockers; team effects and scaling damage count
  full.
