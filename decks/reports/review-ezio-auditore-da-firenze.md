# Adversarial review: ezio-auditore-da-firenze (Phase 2, round 2 list, 2026-11-02)

Reviewer: Opus 5.5 (high). Inputs: `decks/phase2/ezio-auditore-da-firenze.txt`, Oracle text from
`data/model/phase2/pool-ezio-auditore-da-firenze.json` and the Scryfall API (commander text and rulings, read 2026-11-02),
then `ezio-auditore-da-firenze.plan.json`, `.build.md`, `decks/reports/consistency-ezio-auditore-da-firenze.md`,
`decks/phase2/owner-decisions.md` (three rounds; binding), `data/model/phase2/assignment.json` (final).
Scripts run: `scripts/plan_density.py` (PASS, 0 failures, 2 warnings) and `scripts/check_phase2_bracket.py` (PASS, floor 1,
0 Game Changers). Live Scryfall `is:gamechanger` search on 2026-11-02: 53 cards, none in the list.
Odds: hypergeometric, 99-card library, cards seen by turn N = 7 + N, no mulligan, no extra draw (skill `probability.md`).
Simulations (Monte Carlo, 20,000 to 40,000 games) are mine and are labelled as such.

## 1. Independent reading (written before opening the plan file and the build notes)

**Commander.** Ezio Auditore da Firenze, {1}{B}, 3/2 menace Human Assassin, color identity WUBRG (the kill cost). "Assassin
spells you cast have freerunning {B}{B}." "Whenever Ezio deals combat damage to a player, you may pay {W}{U}{B}{R}{G} if
that player has 10 or less life. When you do, that player loses the game." Rulings 2024-07-05: the life check is made when
the trigger resolves, the kill is a reflexive trigger that ignores later life changes; freerunning stays on for the turn
once an Assassin or a commander connected.
- Rewards: Assassins connecting (any Assassin hit turns on freerunning; the {B}{B} grant needs Ezio on the battlefield) and
  Ezio himself connecting with a player at 10 or less while five colors are untapped in the combat damage step.
- Fuel: attackers that connect every turn; opponents' life brought to 10 by everything else; WUBRG held in the window,
  competing with precombat casts and post-combat freerunning.
- Kill: one player per Ezio hit, Ezio attacks one player per combat: three opponents need three Ezio hits on three turns
  after ~90 life of team damage. Single-target, so a backup-style route; the main load is team damage.
- Dies to: everything (toughness 2); menace loses to two chump blockers that also kill him; tapped and open on the
  crack-back. Recast cost 2, 4, 6: cheap, but each recast without haste loses the attack turn.
- Dependence: attack engine for the kill, enabler for freerunning. Protection class attack_engine (6 to 8).
- Commander dead clauses: none; freerunning {B}{B} saves nothing on the 1- and 2-drop Assassins (only a color swap).

**Archetype and plan.** combat_attackers (primary) + alternate_kill (secondary, the kill triggers on combat) with an
Assassin typal modifier (22 Assassins in the 99). Plan: cheap Assassins with individual and team evasion connect from
turn 2 or 3, combat-tied draw refills, team pump (Arno, Achilles, Bayek, Rally) and Unstoppable Slasher push the table to
10, Ezio removes players one per hit; attack taxes and deathtouch bodies hold the crack-back.

**My recount from Oracle text** (weights per skill 3.4: one-shot half in support lines, conditional half):

| Function | Cards | Raw | Weighted (mine) |
|---|---|---|---|
| Attackers | Ezio, Initiate, Hookblade Veteran, Aven, Desmond, Spy, Winter Soldier, Slasher, Shao Jun, Rato, Jacob, Lydia, Achilles, Arno, Marchesa, Etrata S, Layla, Ezio BoV, Bayek | 18 + Ezio | 18 |
| Through 8 chump blockers | Cover of Darkness (team fear; red goblins cannot block), Secret Tunnel (2 creatures, {4}, repeatable), Hookblade, Glider Staff, Haunted Cloak (trample, partial), Assassin Gauntlet (one swing, one opponent), Mephitic Vapors (one sweep, symmetric), Spy, Etrata S (one hit per cast: she shuffles away), Rato (one hit: loses unblockable after its first damage), Aven, Shao Jun, Initiate ({1} flying), Hookblade Veteran; not counted by the builder: Evie (repeatable, needs a creature discard), Enter the Avatar State, Thopteryx (flier), Bleeding Effect (conditional) | 14 + 4 | about 11.5 to 13 |
| Of which pass EZIO himself (the kill) | Cover, Hookblade, Glider Staff, Secret Tunnel, Evie, Enter the Avatar State, Gauntlet, Haunted Cloak (trample damage triggers him), Loyal Inventor (fetches the Equipment) | 9 | 70 % by turn 5 |
| Team evasion (support) | Cover (repeatable, team); Secret Tunnel, Gauntlet, Vapors, Bleeding Effect partial | 5 | about 3 |
| Through two bigger creatures | 7 spot spells, Haytham (one per opponent), Royal Assassin, Revelations I, Etrata S, Hidden Blade, deathtouch bodies (Etrata DF, Slasher, Arno, Thorn, Marchesa, Ezio BoV), Initiate, Lydia, fliers, Glider Staff (airbend) | 17+ | 15+ |
| Haste | Swiftfoot Boots, Haunted Cloak, Boros Guildmage (repeatable {1}{R}), Queen Marchesa (self only); Loyal Inventor fetches Boots or Cloak; Bleeding Effect only with Marchesa in the yard | 4 | 3.5; Ezio after a recast: 3 granters + Inventor = 41 % by turn 5, 46 % by turn 7 |
| Commander protection | Swiftfoot Boots, Gold-Forged Thopteryx (ward {2} on every legend), Haystack, Octopus Form, Enter the Avatar State, Get Out | 6 | 6 (55 % by turn 5); Kaya's 0 is sorcery speed, not protection |
| Wipe insurance | Haystack (one creature), Get Out (two), Restart Sequence, Revelations III, Layla, Winter Soldier and Slasher self-return, Jacob | 5+ | ok; no team-wide save (no Heroic Intervention or Teferi's Protection in the pool) |
| Defense while tapped | Propaganda, Ghostly Prison, Royal Assassin, Winter Soldier and Haunted Cloak (vigilance), Etrata DF and Thorn (deathtouch home), Thopteryx | 8 | 8 |
| Net draw | Coastal Piracy, Ezio BoV, Eagle Vision, Theater of Horrors, Layla (full); Thorn, Marchesa, Kaya, Etrata DF (cloaks), Jacob, Evie's Jacob fetch, Boros Locket (half); Evie's loot is selection, not draw | 11 tags | about 8.5 |
| Spot removal | Swords, Infernal Grasp, Terminate, Assassin's Trophy, Mortify, Utter End, Bitter Triumph, Haytham, Royal Assassin | 9 | 9 (answers 10 with the wipe, under the closers) |
| Wipe | Mephitic Vapors (-1/-1 to all; also kills my Initiate, Aven, Evie, Deathcap, Royal Assassin, Rato and Marchesa tokens) | 1 | 1 |
| Ramp | Sol Ring, Arcane Signet, Rakdos Signet, Deathcap (needs {G}: 67 % by turn 2), Chromatic Lantern, Boros Locket, Bender's Waterskin (three 3-drops compete with 22 three-drops) | 7 | about 4 on time; the 3-drop rocks are kill fixers more than ramp |
| Non-combat damage | Shao Jun (1 to each opponent per two untapped artifacts; 14 artifacts in the list), Vindictive Warden ({3}: 1 to each), Kaya (-1: 2 to each, 5 loyalty), Theater ({3}{R}: 1 to one) | 4 | a top-off, not a kill: about 2 to 4 per opponent per turn once two are out |

**Lands and colors.** 36 lands (23 nonbasic, 13 basic: 9 Swamp, 1 of each other) + 7 rocks or dorks. Land sources (any-color
and filter lands included, Brotherhood HQ counted though it cannot pay the kill): B 24, W 15, U 15, R 14, G 11. Pips on the
nonland cards: B 30, U 21, W 18, R 6, G 2. **Tapped early** (my reading): Path, Command Bridge, Jungle Shrine always; Abandoned
Campground, Raucous Carnival, Murky Sewer until a player is at 13; Sunken Hollow, Smoldering Marsh, Prairie Stream until two
basics (13 basics in 36 lands); Clifftop Retreat (enablers: Mountain, Plains, Prairie Stream, Smoldering Marsh = 4),
Sulfur Falls (5), Hinterland Harbor (4) are tapped most of the early game. About 12 lands, against the 4 to 6 tolerated
(skill step 4, notes/02 S5). Command Bridge played on turn 1 is sacrificed (it cannot tap itself); later it taps another
permanent. Curve (63 nonland + Ezio): MV1 6, MV2 21, MV3 22, MV4 12, MV5 3, average 2.77.

**My simulations.**
- Early tempo (40,000 games, greedy land order): Ezio castable on turn 2: 72 % (78 % if every land entered untapped);
  three untapped mana on turn 3: 64 to 67 % (78 % if all untapped); about 1.2 tapped lands played by turn 4.
- Kill payment WUBRG at once (20,000 games, optimistic: Exotic Orchard any color, every rock drawn is cast, nothing else
  spent that turn): 33 % turn 5, 46 % turn 6, 55 % turn 7, 63 % turn 8, 76 % turn 10. The builder's conservative run
  (39 / 55 / 67 % at turns 6 / 8 / 10) brackets mine.

**How it loses.**
- To a wipe: the board of 1- to 3-toughness bodies dies; Haystack saves one, Get Out two, the Equipment stay; rebuild with
  Ezio (4) + Boots or Cloak, Restart Sequence, Revelations III, Winter Soldier, Slasher's return; no team-wide save.
  Two wipes by turn 9 leave it out of cards (net draw about 8.5).
- To 8 sacrificeable 1/1s: if Cover of Darkness is missing (12 % to have it by turn 5), Ezio is double-blocked and dies
  (menace, toughness 2); the deck then needs one of the 9 Ezio passes per kill turn, and the x/1s die to the goblin
  deck's pings. Taxes make the goblin swing cost 2 per goblin per tax.
- To two bigger creatures: least likely loss: 9 spot answers + Haytham's three exiles + deathtouch everywhere.
- To a removal-heavy table: Ezio recast without haste (54 % to lack any haste piece by turn 7) wastes the turn; the kill
  needs three such turns.

## 2. Differences with the builder

| Item | Builder | Mine | Effect |
|---|---|---|---|
| Net draw | 11 tags, "about 9.5 weighted" | about 8.5: Evie's loot is selection (skill step 5); Jacob needs graveyard Assassins; the draw base counts Evie and the monarch cards in full | Draw is under the base min 10 and the gate cannot see it (finding I3) |
| Tapped lands | "3 always + 3 until 13 life + 4 battle lands; check lands mostly untapped" | 3 battle lands, not 4; 3 of the 7 check lands (Clifftop, Sulfur Falls, Hinterland) have 4 or 5 enablers in 36 lands and are tapped most of the early game: about 12 tapped early | -11 to -14 points on 3 mana by turn 3 (finding I1) |
| Haste follow-up | "next swap is Expedite for Octopus Form" (build section 12) | Expedite's only copy is in `fire-lord-azula.txt` | The stated fallback does not exist (finding I2) |
| condition_enablers | late, via `if_commander_is_source`, 8 cards + Ezio | Ezio is the kill (payoff), not the source of life loss; the real enablers are the 18 attackers | Substance passes either way; declaration is mislabeled (M1) |
| through_wide_board | 15 full pieces | about 11.5 to 13 weighted: Rato and Etrata S pass once per cast, Gauntlet and Vapors are one-shots, Cloak passes 2 of 3 damage; Evie, Avatar State and Thopteryx not listed | Still above 10 |
| Kaya as protection | not counted | agree (sorcery speed) | none |
| Haste promotion | stays support: the freerunning grant acts without attacking | defensible [J]; but the profile asks that one haste source reach the commander after a recast, and only 3 granters do | finding I2 |
| Toughness | 8 of 22 at 2 or less (36 %) | 7 of 19 attackers (37 %), plus Royal Assassin, Deathcap, Guildmage at home | agree: between a third and a half, covered in writing |
| Protection, removal, wipe, defense, routes, Board 2 | as written | agree | none |

## 3. Findings

No BLOCKING finding: no broken rule, no plan-level error, the gate passes honestly at the gate's level. The IMPORTANT items are
where this list still loses games or Salt points.

### IMPORTANT

**I1. The mana base plays like a 5-color control deck under an aggro curve.**
- Failure: about 12 of 36 lands enter tapped in turns 1 to 4 for a deck with 27 one- and two-drops and a 2-mana commander.
- Evidence: my simulation: three untapped mana on turn 3 in 64 to 67 % of games against 78 % with untapped lands; Ezio on
  turn 2 in 72 % against 78 %. Clifftop Retreat (4 enablers), Sulfur Falls (5), Hinterland Harbor (4) are counted as
  "mostly untapped" in build section 11; three battle lands need two of only 13 basics; Command Bridge is a lost land on
  turn 1 and a lost mana on any other turn. Commander Salt's Manabase Quality is the measured lever that moves 2- to
  3-color decks most (CLAUDE.md, Azula 5.5 to 6.9 for untapped duals), so this costs Salt too.
- Fix [J]: (a) guide line: never play Command Bridge on turn 1; play the always-tapped lands on turns 1 and 4+; (b) Command
  Bridge -> Swamp gives +2.5 points on 3 mana by turn 3 (simulation) for one fewer any-color kill source (Chromatic Lantern
  and the 9 payment enablers carry the kill); (c) in the 5,000 CLP envelope shared with Toph and Azula, an untapped dual or
  2-mana Talisman beats Rogue's Passage (proposal 4) for this deck. The owner decides the trade between kill colors and
  tempo; the slow lands (Campground, Carnival, Sewer) turn untapped exactly when the kill is on, so they are the right
  tapped lands to keep. Partly sourced (tapped-land tolerance notes/02 S5; Salt fact in CLAUDE.md), rest [J].

**I2. Haste sits at the floor and its declared next step is a card the deck cannot have.**
- Failure: L3 (no haste was a cause of the Phase 1 losses) is met only at the minimum, and the minimum counts Queen
  Marchesa's haste on herself. A recast Ezio gets haste only from Swiftfoot Boots, Haunted Cloak or Boros Guildmage
  (+ Loyal Inventor fetching an Equipment).
- Evidence: 4 cards: 41 % by turn 5, 46 % by turn 7; build section 12 names Expedite as the next haste swap, but the
  only copy is in `fire-lord-azula.txt`. The pool's free haste cards are self-haste bodies (Skyknight Legionnaire, Malcolm,
  Treetop Freedom Fighters), none gives haste to Ezio.
- Fix: (a) correct the build note; (b) the Standard-binder Hidden Footblade (`loan_candidates`, class "evaluate", no stock at
  Game of Magic Singles on 2026-10-31) is the only owned haste granter left: a loan proposal to evaluate with a fallback
  (Octopus Form or Hookblade Veteran stays), owner decides; (c) or a haste Equipment from the envelope, live stock first.
  [J] + owner signal L3; skill step 8 ("haste must reach it after a recast").

**I3. Card flow is under the base and the tags hide it.**
- Failure: an attacking deck that spends its hand on 1- to 3-drops needs the refill (combat_attackers draw min 10).
- Evidence: net draw about 8.5 (section 1); the gate reads 11 because Evie (loot), Thorn, Marchesa, Kaya, Etrata DF and Jacob
  are tagged in full. Two wipes by turn 9 empty the hand.
- Fix [J], owned and free: **Bleeding Effect -> Lion Vulture** (English copy, in no Phase 2 list). Lion Vulture is a
  4-mana flier (passes Board 1) that draws a card and grows every end step in which an opponent lost life, which this deck
  causes almost every turn (combat, Shao Jun, Vindictive Warden, Theater, Kaya): the condition is the deck's own main action
  (skill 3.4). The owner's "slow" signal came from Azula, where the condition was met 2 or 3 times; Azula's builder left it
  out, so there is no copy conflict. Bleeding Effect is the weakest card in the list: 4 mana, nothing on board alone, its
  flying needs one of 2 creature cards (Aven, Thopteryx) in a graveyard the deck does not fill (L7). After the swap:
  draw about 9.5, through_wide_board 16, team_evasion 4 (the profile floor when the pool lacks 6), defense_while_tapped 9.

**I4. Team evasion is one card; the kill attacker's own passes are what carry Board 1.**
- Failure: against the goblin board the only repeatable team effect is Cover of Darkness (12 % by turn 5, 20 % by turn 13),
  removed by any enchantment answer; the WARN is honest, but the plan's sentence "carry Ezio past any board" overstates it.
- Evidence: Ezio-specific passes: Cover, Hookblade, Glider Staff, Secret Tunnel, Evie, Enter the Avatar State, Gauntlet,
  Haunted Cloak, Loyal Inventor = 9 (70 % by turn 5, 80 % by turn 7); Ezio needs one per kill turn, three kill turns.
- Fix [J], owned and free: **Hookblade Veteran -> Angelic Intervention** (English copy, in no list). Instant {1}{W}:
  protection from a color counters the removal aimed at Ezio AND makes him unblockable by creatures of that color on the
  kill turn (protection from red against red goblins). Commander protection 6 -> 7, Ezio passes 9 -> 10; attackers 18 -> 17,
  through_wide_board stays at or above 15. Guide note: its +1/+1 counter turns off Unstoppable Slasher's return, never cast
  it on Slasher. Hookblade Veteran is a 1-power body marked bad late.

**I5. The non-combat route is a top-off, not a route.**
- Failure: all three routes depend on combat in practice; a table that stops attacks (fogs, taxes of its own, a blocker
  wall that also flies) leaves the deck without a kill.
- Evidence: Shao Jun, Vindictive Warden, Kaya: 3 cards, 37 % to see one by turn 7, 50 % by turn 13; output about 2 to 4
  damage to each opponent per turn with two of them out, from 40 life that is 10+ turns. The gate counts the route because
  its cards hit every opponent; the plan's own wording ("closes a table that combat already put low") is honest.
- Fix: no owned card fixes it without a second plan; keep the route as written, and state in the plan that the deck is
  all-in on combat (the owner's pod blocks, it does not fog). [J]

**I6. Salt power may drop significantly against the Phase 1 7.7, and the list is unmeasured.**
- Evidence: round 1 removed every tutor but Loyal Inventor (Entomb, Reckless Handling, Mystical Teachings), most cheap
  interaction (Fatal Push, Murder, Mana Leak, Kolaghan's Command, Chaos Warp, Fateful Absence, Stroke of Midnight) and the
  cantrips, and round 2 added three tapped lands (I1). These are the levers Salt reads.
- Swaps that raise Salt without hurting consistency (all owned, English, in no Phase 2 list): Lion Vulture (I3), Angelic
  Intervention (I4), **Bitter Triumph -> Kolaghan's Command** (instant 2-for-1, adds the third artifact answer and a
  recursion mode; removal stays 9), **Mana Leak** as the interim wrath answer until Arcane Denial arrives (for Get Out only
  if the owner prefers a counter over the two-creature bounce). Measure on Salt with and without them before spending the
  envelope. [J]

### MINOR

- **M1.** `condition_enablers` is declared late via `if_commander_is_source`, but Ezio does not make opponents lose life,
  he kills them; the real enablers are the attackers (18, early). Redeclare early with the attackers, or write why. The gate
  result does not change.
- **M2.** Tag honesty: Propaganda, Ghostly Prison, Boros Guildmage and Bleeding Effect are tagged `engine` while they sit only
  in support lines (defense, haste); Evie Frye is tagged `draw` for a loot. This inflates "plan cards 34 of 63". Tag them
  `protection`/`defense` and Evie `engine` (Board 1 pass) or `tutor` (Jacob).
- **M3.** Build section 11: "4 battle lands" (there are 3) and "check lands mostly untapped" (3 of 7 are not).
- **M4.** Coastal Piracy (proven role-player) costs {U}{U}: about 15 blue sources give 52 % for two by turn 4 and 62 % by
  turn 6; the guide's "turn 4 or 5" is optimistic. Guide: cast it when UU is up; Chromatic Lantern or Arcane Signet first.
- **M5.** Mephitic Vapors is marked "never" bad when drawn, but it kills 5 of my own bodies (Initiate, Aven, Evie, Deathcap,
  Royal Assassin) and my Assassin tokens: bad when my board is x/1-heavy without Achilles. Mark it, or keep the guide line.
- **M6.** Purchase envelope (owner, third round: 5,000 CLP for Toph, Azula and Ezio together): Ezio's first two proposals
  take about 3,600 CLP (72 %) with prices from the 2026-10-17 reading; live stock is still required. The free swaps in I3,
  I4 and I6 reduce what Ezio must buy to the wrath counter and the mana (I1).
- **M7.** Ratonhnhaké꞉ton's Equipment return and Etrata the Silencer's hit-counter loss clause are near-dead (named by the
  builder); both cards are kept for their live text. No action.

## 4. Lessons checklist (`docs/research/phase2-owner-lessons-20261031.md`)

| Lesson | Covered? | Evidence |
|---|---|---|
| L1 one plan | Yes | Reanimation, copy and Sphinx packages gone; no undeclared 1-to-3-card package left (monarch is 2 deathtouch bodies, each useful alone; Equipment is 6 + Winter Soldier + Rato) |
| L2 ratios follow the plan | Partly | Attackers 18, Board 1 15, defense 10 are plan-sized; haste and protection sit at the floor, draw under it (I2, I3) |
| L3 attack lines | Partly | Haste 4 (floor, Boots, Cloak, Guildmage, Marchesa self); team evasion 1 repeatable card + 14 individual passes (Cover of Darkness in); protection 6 (floor); defense while tapped 10 (Propaganda, Ghostly Prison, Royal Assassin, vigilance) |
| L4 dependence | Yes | attack_engine, protection min 6 met |
| L5 card by turn | Partly | Everflowing Chalice gone; Boros Locket and two other 3-mana rocks cast on turn 3 against 22 three-drops are kill fixers, written as such |
| L6 proven role-players | Yes | Eagle Vision (loan), Cover of Darkness (loan), Propaganda, Coastal Piracy all in |
| L7 dead clauses | Mostly | Winter Soldier's clause live (6 Equipment); Haytham's Knight clause, Etrata S's hit counters, Rato's Equipment return named; Bleeding Effect is close to a card that does nothing alone (I3) |
| L8 both boards | Yes | Build section 10; Board 2 strong; Board 1 rests on Cover plus 9 Ezio passes (I4) |
| L9 Salt not the measure | Yes | No cut by score; round-2 loans were the owner's decisions |
| L10 guide by use | Yes | Build section 4 says how to use every card; add the guide notes from I1, I4, M4 |

## 5. Rules checklist

| Rule | Result |
|---|---|
| Pool and copies | 100 cards, every card assigned with `given = qty`, no missing (`assignment.json`, problems: none) |
| Language (bilingual, English when owned in both) | Spanish picks are Spanish-only cards or copies whose English print went to another deck; assignment is final |
| Proxy commander | Declared (`proxy_commander`), in `restock.md` |
| Loans | Eagle Vision, Bayek, Layla (automatic) and Cover of Darkness, Unstoppable Slasher, Achilles Davenport (evaluate, accepted by the owner 2026-11-02): all in `borrowed` and `restock.md`; none of them in another deck |
| Owed card | Smoldering Marsh (MSC, Spanish) counted as owned, per `pending_owned` |
| Purchases | Arcane Denial, Mind Stone, a Talisman, Rogue's Passage: proposals only, none in the list, one store (Game of Magic Singles), live stock still to verify; see M6 for the envelope |
| Scarce copies | Named in build section 7; the Expedite fallback ignored that Azula holds the only copy (I2) |
| Bracket 3 | 0 Game Changers (live search, 53 cards), no extra turns, no mass land denial, no reversible card, 0 Spellbook combos inside the list; no card held back for power |

## 6. Verdict

**PASS (ship to Salt).** One declared plan, every gate function above its class, both reference boards answered, rules clean,
the owner's lessons fixed at least to the floor. Before or alongside the Salt measurement, I recommend the three owned,
free swaps that raise consistency and likely Salt together: Bleeding Effect -> Lion Vulture, Hookblade Veteran -> Angelic
Intervention, Bitter Triumph -> Kolaghan's Command; and the guide notes for the tapped lands, Command Bridge and Coastal
Piracy. Owner decisions: the haste loan (Hidden Footblade, evaluate class) or a haste purchase; kill colors versus tempo in
the mana base (Command Bridge -> Swamp, an untapped dual instead of Rogue's Passage).

## Round 3 re-review (2026-11-04)

Scope: the round-3 list committed as 21674e6. Against the round-2 list I reviewed, six swaps: Bleeding Effect -> Lion Vulture,
Hookblade Veteran -> Angelic Intervention, Bitter Triumph -> Kolaghan's Command, Vindictive Warden -> Hidden Footblade
(loan), Command Bridge -> Swamp, Murky Sewer -> Island (checked by a line diff, 99 + commander). Scripts rerun on
2026-11-04: `plan_density.py` PASS (0 failures; warnings team_evasion 4 of 6, ramp 7 of 10; team_finishers 6 of 6);
`check_phase2_bracket.py` PASS (floor 1, 0 Game Changers, 0 review items); live Scryfall `is:gamechanger` search: 53 cards,
none in the list.

### Recount from Oracle text (round 3)

| Function | Round 2 | Round 3 (mine) | Evidence |
|---|---|---|---|
| Haste reaching a recast Ezio | 3 granters + Inventor (41 % by T5) | 4 granters + Inventor = 5 pieces: 48 % by T5, 54 % by T7; 5 with Marchesa's own | Swiftfoot Boots, Haunted Cloak, Hidden Footblade ({R}, flash), Boros Guildmage; Loyal Inventor fetches the three Equipment |
| Team evasion (support) | 5 (about 3) | 4 = the profile floor; one repeatable team card (Cover of Darkness) | Cover, Secret Tunnel, Assassin Gauntlet (one swing), Mephitic Vapors (one sweep) |
| Passes for EZIO himself on Board 1 | 9 (70 % by T5) | 10 (74 % by T5) | + Angelic Intervention (protection from red: red goblins cannot block him) |
| Commander protection | 6 | 7 (61 % by T5) | + Angelic Intervention |
| Net draw | about 8.5 | about 9.5 | + Lion Vulture (2/2 flier; draws every end step an opponent lost life, which this deck causes most turns) |
| Spot removal | 9 | 9; unconditional creature kills 6 + Haytham + Royal Assassin | Kolaghan's Command kills only toughness 2 or less, but adds the third artifact answer and a recursion mode |
| Through two bigger creatures | 17 | 16 real (the plan lists 17) | Hidden Footblade's first strike +1/+0 does not beat a bigger blocker; it is a haste card |
| Team finishers / non-combat route | 7 / 3 cards | 6 (at the minimum) / 2 cards (Shao Jun, Kaya): 26 % by T7, 36 % by T13 | Vindictive Warden cut |
| Mana, my simulation (40,000 games) | 3 untapped mana on T3 64 to 67 %; about 1.2 tapped lands by T4 | 71 % (78 % if all untapped); about 1.0 tapped lands by T4; Ezio on T2 72 % (unchanged) | 15 basics now: Sulfur Falls 6 enablers, Hinterland 5, Clifftop still 4 |
| WUBRG at once (my optimistic run) | 63 % by T8 | 60 % by T8 (builder's conservative 51 %) | Green lands: 7 + 2 filters; Chromatic Lantern and Loyal Inventor carry it |

Copies and loans: every new card is a free English copy in `assignment.json` (Lion Vulture TLE 232, Angelic Intervention MOM 5,
Kolaghan's Command M3C 268, Swamp TLA/ACR, Island ACR 104); 100 cards, no missing, no problems. Hidden Footblade is the
Standard-binder copy (`loan from the Standard decks`), accepted by the owner on 2026-11-02 (fourth round), in `borrowed`
(8 entries: Eagle Vision, the proxy Ezio, Bayek, Layla, Cover of Darkness, Unstoppable Slasher, Achilles, Hidden Footblade)
and in `restock.md`. Azula plays the free Footblade copy: two physical copies, so "one loan card in one deck" holds.

### Round-2 items: status

| Item | Status |
|---|---|
| I1 mana tempo | Partly closed: 3 mana on T3 up to 71 %; Clifftop Retreat (4 enablers) and Jungle Shrine are the tapped lands left to fix by purchase (R3-3) |
| I2 haste | Closed in the list (5); the build text is stale (R3-4) |
| I3 draw | Mostly closed (about 9.5) |
| I4 team evasion | Mitigated (Ezio passes 10, protection 7); still one repeatable team card, at the floor 4 the pool allows |
| I5 non-combat route | Worse: 2 cards (R3-2); accepted as a top-off, written as such in the plan |
| I6 Salt | Swaps applied; the list is still unmeasured |
| M1 condition_enablers | Closed (declared early, 21 pieces) |
| M2 tags | Evie fixed; the attack taxes stay `engine` with a written reason (no defense tag in the schema): accepted |
| M3, M4 build text | Open (R3-4) |
| M5 Vapors | Closed (bad late) |

### Findings (round 3)

No BLOCKING finding.

**R3-1 IMPORTANT (owner confirms). Boros Guildmage and Unstoppable Slasher are both in, against the literal owner decision.**
The 2026-11-02 decision says "Unstoppable Slasher (replaces Boros Guildmage)". Guildmage came back in round 2 in the slot of
the free Hidden Footblade (given to Azula), and now that the loaned Footblade is back, the builder cut Vindictive Warden instead
of Guildmage. The build notes record this as history, not as a departure from a decision. On the merits keeping both is right
[J, owner lesson L3]: haste 5 with four granters for a recast Ezio, against 4 (the floor) and three granters; Warden's {3} per
1 damage was the weakest route card. Concrete swap only if the owner holds to the literal decision: Boros Guildmage -> Vindictive
Warden (haste 4, team_finishers 7, non-combat route 3 cards). Recommendation: keep the list, and write the reason in the build
notes for the owner to confirm.

**R3-2 IMPORTANT. Team finishers sit exactly at the minimum (6), and the non-combat route is two cards.**
Arno, Achilles, Bayek, Rally, Shao Jun, Kaya: 55 % by T5, 75 % by T13; one miscount or one future cut fails the gate.
Shao Jun + Kaya: 36 % to see either by T13. Concrete swap if margin is wanted: Restart Sequence -> Vindictive Warden
(team_finishers 7, route 3 cards; wipe_insurance 6 -> 5, min 2; Restart Sequence is marked bad early) [J]. Otherwise leave
it, and cut none of the six without a replacement.

**R3-3 IMPORTANT. The purchase wishes are not in the best order for this deck.** Price hints from the Game of Magic Singles
readings of 2026-10-17 to 19 (`data/prices/browser-gameofmagic-*.psv`), stale; live stock before buying. Ranked by impact
per CLP for Ezio:
1. **Golgari Signet** (about 570 CLP) for Boros Locket: a turn-2 rock instead of a turn-3 one in a deck with 22 three-drops,
   and it makes {B}{G}: green is the kill's thinnest color (7 green lands) and black pays freerunning. Better here than
   Mind Stone (742, colorless).
2. **Battlefield Forge** (about 915) for Clifftop Retreat: same colors, untapped every turn; Clifftop has 4 enablers and stays
   tapped most early turns. Helps tempo and Salt's Manabase Quality.
3. **Arcane Denial** (about 2,840) for Get Out: the only hard answer to a wrath; worth it, but the most CLP per point.
4. **Llanowar Wastes** (about 1,600) for Jungle Shrine: an untapped green source; next if money remains.
5. Mind Stone (742) and Rogue's Passage (742) last: colorless; Secret Tunnel already gives unblockable.

Envelope (5,000 CLP for Toph, Azula and Ezio): with Azula buying only Soul-Guide Lantern (about 742), items 1 to 3 cost about
4,325 and the total about 5,067: slightly over, with nothing for Toph (whose rank 1, Eladamri's Call, has no reading). Ezio's
fair share is items 1 and 2 (about 1,485), plus Arcane Denial only if Toph's wishes fit in what is left. The lead decides.

**R3-4 MINOR. Stale build text.** Section 11 still says "4 battle lands", "13 basics", "Check lands mostly untapped
(9 Swamps)"; section 5 keeps "Expedite (next haste add)" and section 12 Q2 "Haste sits at the minimum (4)... Expedite for
Octopus Form" (Expedite is Azula's; haste is 5); the profile table shows commander protection "Actual 6" (it is 7),
wipe_insurance 5 (the plan has 6, with Kolaghan's Command), payment_enablers 9 (it is 8); section 12 Q1 still asks for Arcane
Denial and Mind Stone; the Coastal Piracy guide still says "turn 4 or 5" ({U}{U}: about 50 % by T4). Fix: edit the text; no
list change.

**R3-5 MINOR. Hidden Footblade is listed in through_big_creatures.** Its first strike and +1/+0 do not get past a bigger
creature; through_big_creatures is 16 without it (still above 10). Fix: remove it from that function in the plan file.

**R3-6 Salt.** The round-3 swaps should raise Salt (an instant 2-for-1, a protection spell, a draw engine, fewer tapped
lands); measure the list now. Further Salt-raising buys that keep the gate are R3-3 items 1, 2 and 4 (untapped mana).

### Verdict (round 3)

**PASS (ship to Salt).** The list fixes the round-2 IMPORTANT items it could fix from the collection. Still open: the owner's
confirmation of Guildmage plus Slasher (R3-1), the thin margin of the late finishers (R3-2), the order of the purchase wishes
(R3-3) and stale text (R3-4, R3-5).
