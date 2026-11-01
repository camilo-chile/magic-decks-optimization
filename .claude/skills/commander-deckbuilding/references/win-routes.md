# Win routes, the reference boards, and attacking decks

Sources: notes in `docs/research/commander-deckbuilding/notes/`, mainly notes/05, notes/06 and notes/12. Most of this
material is opinion or card-level reasoning; no source measures win rates by route or by evasion type in pods.

## 1. Routes against three opponents

- Finishing types: combat, combo, drain, overrun (notes/05 S4). Extra combats and commander damage are not covered by that
  source.
- Each deck has 2 to 3 finishing routes; name them before play (notes/05 S4, opinion). One main plan with one credible
  fallback (notes/05 S12, snippet). These overlap.
- Three opponents at 40 life are 120 life against 20 in a duel (notes/12 C3).
- **Team-wide versus single-target** [inference and owner signal, notes/05 section 3; notes/12 section 4]: an overrun, a drain to each opponent,
  or damage to each opponent removes several players per resolution; a kill that removes one player per trigger needs one
  resolution per opponent. An overrun that kills two opponents and leaves the third at 4 is a win next turn (notes/05 S4).
  So the single-target kill is a backup route; the main route should reach the whole table.
- Unverified win shares (Playgroup snippet, about 645,000 games): about half of decided multiplayer wins by combat, a fifth
  by non-combat effects such as drain, about 8 % each by combo and by commander damage (notes/05 S8). Direction only.
- Each route should finish with little setup; a finisher that is easy to disrupt stalls (notes/03 S1). Carry several big
  finishers, since one counterspell stops a lone win condition (notes/03 S5).
- Value alone seldom ends games (notes/03 S5); extra card draw alone will not finish (notes/05 S12, snippet).
- Bracket 3 wins come in one big turn funded by resources built earlier (notes/05 S1). When ahead, add up the damage, pick
  the turn and commit; a roughly 60 % attempt now can beat waiting for 90 % in a four-player pod, because each extra turn
  is another player's chance to win (notes/05 S4, opinion).
- The gate also asks that at least one route does not need combat damage, and that each route's cards are disjoint
  (judgment, `scripts/plan_density.py`). In a combat deck, the non-combat route can be a small package that the main
  engine already reaches (for example drain or damage on each attack or each token entering) [J].

### Combos at Bracket 3
- Bracket 3 bars intentional early-game two-card infinite combos (Wizards' test: it "tends to happen" in the first six turns;
  "not reachable in the first six turns" is the project's working convention); late-game lines are
  allowed; three-card lines are not mentioned by any bracket (notes/09 S15; `docs/research/commander-brackets-rules-snapshot.md`).
- Organic combos use cards the deck wants anyway; inorganic combos are added only for the win (notes/09 S15). Consistency in
  assembling the pieces matters more than the combo's raw power (notes/09 S15).
- Compact lines (few cards, little mana) assemble more often; resilience comes from redundancy, tutor access, protection,
  graveyard recovery and pieces that keep value apart from the combo (notes/08 S12, cEDH source, general principle).
- Rule for this skill: a combo piece must do something useful in the plan on its own. A card whose only role is to complete
  a two-card combo is a dead draw in most games (project rule; consistent with notes/11 S3 layering).

## 2. The two reference boards

The gate requires two functions, `through_wide_board` and `through_big_creatures` (judgment, from the gate review). Test
every list against both.

### Board 1: eight or more small chump blockers, some of them sacrificeable
| Works | Why | Source |
|---|---|---|
| Flying or unblockable attackers (unless the tokens fly) | blockers cannot reach | notes/06 S3 |
| "Creatures can't block" or falter effects (team-wide) | covers the whole attack with one card | notes/06 S3 (bedlam, falter) |
| "Power 2 or less can't block" (daunt-type) | aimed exactly at token boards | notes/06 S3 (keyword text unverified) |
| Trample on a large attacker | excess damage passes a chump | notes/06 S3; notes/12 C4 |
| Flanking, deathtouch plus first strike, pingers | kill small blockers | notes/06 S3 (flanking); [J] for pingers. A single 1-damage ping on a small body does not clear eight chump blockers: it counts half; team effects and scaling damage count full (role-players-and-upgrades.md 5) |
| One-sided wipes, damage-based wipes that spare your board | clear the tokens | notes/04 S1; notes/12 C1 C9 |
| Non-combat damage or drain to each opponent | ignores blockers | notes/12 C14 |
| Attack caps on THEM (two attackers per turn) | defensive, against their wide counterattack | notes/05 S5 |

| Fails | Why | Source |
|---|---|---|
| Menace | needs two blockers; token and typal decks double-block easily | notes/12 C10 |
| "Can't be blocked by creatures with power 3 or greater" (nimble; skulk is the relative version) | stops big blockers, not 1/1s | notes/06 S3 |
| Fear and intimidate | depend on the blockers' colors; artifact creatures always block | notes/12 C11 |
| Stalking ("can't be blocked by more than one") | stops gang blocks, not a single chump | notes/06 S3 |
| Single-target removal | the board has too many bodies; edicts hit a token | notes/04 S2; notes/04 section 5 |

Sacrifice outlets turn the defender's chump blockers into removal of your attackers or into value; the attacker's side of
that exchange is not analysed by any source (notes/12 inference). A sacrificeable chump board therefore also removes the
attackers with low toughness that run into it: with a sacrifice outlet or a sweeper-like block, count your attackers of
toughness 2 or less as removable [J].

### Board 2: two or more creatures bigger than yours
| Works | Source |
|---|---|
| Removal on the few high-impact blockers first (quality over quantity) | inference, notes/05 section 4, untested; threat quality from notes/05 S3 |
| Deathtouch attackers or blockers (nobody trades a big creature into it) | notes/12 C1 C2 |
| Flying, unblockable, "can't be blocked by power 3+" (nimble-type; skulk is the relative version) | notes/06 S3 |
| Forced blocks and lures, pump plus trample, first strike | notes/12 C4 |
| Goad: make their big creatures attack someone else | notes/12 C8 C12 |
| Politics: ask others not to block, point to a bigger threat | notes/12 C12 |
| Non-combat routes | notes/12 C14 |

## 3. Evasion in multiplayer

Ranking of evasion types one-on-one, no method stated: unblockable, flying, trample, protection, deathtouch, shadow,
menace, intimidate, fear, daunt, flanking, "can't be blocked by", stalking, nimble, burrowing, falter and bedlam, skulk
(notes/06 S3). No source tests evasion in pods. What changes in a pod:
- Menace weakens as opponents add creatures (notes/12 C10).
- Color-based evasion is weaker with more colors at the table; artifact creatures always block it (notes/12 C11).
- Team-wide effects scale with the size of the attack: one card covers every attacker (notes/06 inference).
- Protection is one of the best ways to sneak creatures past blockers (notes/06 S3).

## 4. Attacking decks

**Attack or connect? Read the trigger first [J].** An engine that triggers on ATTACKING ("whenever it attacks", "while it
attacks") is not stopped by blockers: evasion matters only for the combat route and for keeping the attackers alive, and
the engine needs haste, protection and defense while tapped. An engine that triggers on COMBAT DAMAGE needs to connect:
evasion past the pod's blockers is part of the engine. Do not over-weight evasion for the first kind.

### Haste
- Opponents are strongly motivated to remove an attacking commander before it attacks; haste lets it attack at once
  and repeatedly (notes/06 S4).
- One sourced Commander deck runs six haste cards (notes/06 S4). One data point, not a target. No expert count exists.
- Two kinds (snippet, unverified): team haste for a wide board; single-target haste with protection for one or two key
  creatures (notes/12 U1). Haste equipment carries hexproof or shroud (notes/06 S15).
- A creature with no haste must survive a full turn cycle before it attacks; fragile creatures often do not [J].
- Haste is the weak spot of goad defenses (notes/05 S5).
- **Promotion test (support line or gate function)** [J]. The first cast of any commander loses its first turn whatever
  the deck does; haste decides the turns lost AFTER a removal. A recast of an attack-only engine loses one engine turn plus
  the tax, and roughly one of the 2.3 spot removal the table has seen by turn 8 is aimed at a visible engine
  (`multiplayer-politics-and-threat.md` section 6), so expect about one recast. Promote haste to a gate function (10
  pieces, early) when the commander is an attack-only engine AND either (a) it costs 4 or less, so it returns on the next
  turn and haste decides whether that turn counts, or (b) the plan needs the commander's trigger on three or more of turns
  4 to 8. Keep it a support line (4 to 6) when the commander also acts without attacking, costs 5 or more (the recast turn
  is spent on mana anyway), or can protect itself. "Acts without attacking" includes a static clause, a trigger on
  spells cast, and a trigger on other creatures attacking or connecting.
- **Fit fallback [J].** If the promoted haste line (10 pieces) cannot sit in the non-land slots next to the plan's own gate
  functions (the fit check, SKILL step 3.5), do not drop the other gate functions: keep haste at 4 to 6 as a support line
  and put the difference into commander protection at its target, because keeping the engine alive is cheaper than
  re-hasting it. Write the choice in the profile table.

### Protecting attackers
- A commander-plan deck ranks protection first; cheap hexproof and indestructible effects are central (notes/06 S9).
- A protection stack covers two threats: targeted removal (hexproof, shroud) and damage or destruction (indestructible,
  protection) (notes/06 inference). Add phasing for exile wipes (notes/04 S1).
- A wipe plus an indestructible commander clears the way (notes/06 S9).
- No source covers protecting attackers against multi-blocks or sacrifice (notes/12 gap): that is what evasion, first
  strike, deathtouch and pump are for [J].
- Toughness profile [J]: count attackers with toughness 2 or less. Many of them mean the board dies to pingers, small
  wipes and any block. No source counts this; it is a cheap check the gate review proposes. Pass line [J]: at most a
  third of the attackers and route cards have toughness 2 or less; between a third and a half, name the protection that
  covers them; above a half, fix it (tougher bodies, pump, team protection).

### Defense while tapped
No source counts defensive pieces for an attacking deck (notes/05 gap; notes/12 gap). The sourced tools:
| Tool | Source | Note |
|---|---|---|
| Vigilance | notes/12 C1 C2 | attacking does not tap; tap-to-destroy effects miss it |
| Deathtouch blockers, ideally with flying or reach | notes/12 C1 C2 | deterrent; nobody trades a big creature into it |
| Cheap high-toughness flying or reach blockers kept home | notes/12 C2 | rule of thumb against fast decks: 3 mana or less, 7 to 8 toughness |
| Attack taxes (Ghostly Prison-style) | notes/05 S5; notes/12 C2 | push attacks to other players; opponents who can pay still attack; can make you a hate magnet for efficiency (notes/12 C7) |
| Punishment effects (destroy a creature that hits you; damage when attacked) | notes/05 S5; notes/12 C2 | one source prefers them to taxes |
| Indestructible or punishing blockers | notes/12 C2 | players avoid pointless attacks |
| Board density | notes/12 C1 | opponents judge attacks by how many creatures you appear to have; density stops working after you attack |
| Mana held for instant responses; some creatures kept home | notes/12 C5 | forum opinion |
| Fog, goad | notes/10 S13 | pillowfort tools |

Inference used here: taxes stop only attackers who cannot pay, so a deck that relies on taxes still needs its own blockers
or vigilance for the biggest attacker (notes/05 inference; notes/12 inference). Target 4 to 6 pieces for a deck that taps
its board every turn [J]. Conflict: one source calls extra defensive turns a top cause of squandered advantages (notes/05
S4), while a board left tapped and open after attacking invites the crack-back (notes/12 C1: density stops deterring once
you have attacked; notes/05 conflict 5). The two fit if
defense comes from permanents that also attack or that cost nothing to keep (vigilance, deathtouch, taxes), not from turns
spent holding back [J].

### Common mistakes of aggro and typal decks in pods (notes/12 section 6; notes/06 section 7)
- Attacking the player who becomes the table's target with nothing behind; attacking early and drawing fire.
- A curve with too few early plays; going wide into a likely sweeper.
- Picking attack targets without a threat read; self-hosing wraths; cutting removal for an all-out attack (notes/06 S2).
- Chip damage versus focus: sources disagree (notes/12 conflict 3).
- Aggro needs its own Commander approach; cheap creatures alone are not enough (notes/12 C3).

## 5. Choosing whom to attack (play, not build)
Sources disagree (notes/05 conflicts 2 and 3; notes/12 conflict 2): pressure the leader before they attack you (notes/12
C13); ally with the trailing player against the leader (notes/05 S3); from strength, remove weaker players first (notes/05
S2). Common ground: do not pile onto a threat that is already answered, and track the next threat in turn order (notes/05
S3; notes/11 S5).
