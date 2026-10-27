<!-- Written 2026-10-26 by an Opus 5.5 (high) review agent for the owner. Paths such as in/list-<deck>.txt and in/cards-facts.json refer to the review workspace: the lists are the final ones in decks/measured/, the card facts come from scripts/dashboard_cards.py. -->

# Fire Lord Azula: synergy review (2026-10-26)

List reviewed: `in/list-azula.txt`. It hashes to the same card set as `decks/measured/fire-lord-azula/round4-step27.txt`
(Commander Salt 8.4, scoring version 2026.4195, round 4 step 27, 49,191 CLP). Card text: `in/cards-facts.json`. Power and
toughness come from the local Scryfall oracle bulk (`data/cache/oracle-cards-20261011210156.jsonl.gz`), read-only. Combos:
`in/guide.json` plus the local Commander Spellbook bulk (`data/cache/spellbook_variants_slim.jsonl.gz`), which has exactly
**6** variants fully inside this list (guide.json shows only 5; see "Guide errors").

Shape: 36 lands (17 basics), 6 rocks, 12 creatures in the library plus Azula, 28 instants, 9 sorceries (counting Gleam of
Death), 5 enchantments. Azula copies only what is **cast while she attacks**: the 28 instants plus the flash cards
(Dualcaster Mage, Torrential Gearhulk, Amphibian Downpour). The 9 sorceries and the other permanents never get copied
unless Electrodominance casts them for free.

## Verdict table

Breadth = how many other cards of this list it works with in practice (not counting "any instant" for Azula herself).

| Card | Stand-alone | Needs exact partners? | Breadth | Verdict | Reason |
|---|---|---|---|---|---|
| Fire Lord Azula | high | no | ~31 (every instant and flash card) | core | The engine; every instant is a 2-for-1 in her combat |
| Abrade | medium | no | 2 (Azula, Dualcaster) | keep | Artifact mode matters in 4-player pods; copy keeps the mode |
| Aether Gale | medium | no | 4 (Electrodominance, Treasures, ETB creatures to reuse) | watch | 5-mana sorcery, never copied in combat; strong one-sided reset but slow |
| Amphibian Downpour | medium | no | many (storm counts every spell, Azula adds one) | keep | Flash answer to commanders that does not send them to the command zone |
| Arcane Signet | medium | no | - | keep | T2 fixing for a 3-color commander |
| Archmage Emeritus | high | no | ~35 (every instant/sorcery, copies included) | core | Two cards per spell in Azula's combat; mandatory draws in loops |
| Banefire | low-medium | Electro or Ozai to be big | 3 (Electro, Ozai, The Last Agni Kai) | watch | Sorcery: Azula never copies it; Comet Storm does the same job better here |
| Bender's Waterskin | medium | no | 5 (flash cards, counters) | keep | 3-mana rock, but gives mana on every opponent's turn in a 4-player pod |
| Big Score | high | no | 5 (Azula, Storm-Kiln, Fatal Push, Gearhulk, Glamdring) | core | In combat: discard 1, draw 4, 4 Treasures |
| Black Market Connections | medium-high | no | 6 (Loyal Inventor, Godo, Lo and Li, Bombardment, Fatal Push, Storm-Kiln) | keep | Changeling token = Assassin, Samurai and Noble: quietly fixes three other cards |
| Brainstorm | medium | no | 3 (Azula, Loyal Inventor, shuffle effects) | keep | Better in combat (+2 cards net twice) |
| Cascade Bluffs | land | no | - | keep | Filter for {U}{U} / {R}{R} |
| Champion's Helm | medium | no | 4 (Azula, Glamdring, Ozai, Godo) | keep | Second hexproof source; +2 power raises Glamdring's discount |
| Chaos Warp | high | no | 1 | keep | Only instant answer to an enchantment |
| Choked Estuary | land | no | - | keep | |
| Comet Storm | high | no | 8 (Azula, Glamdring, reducers, every infinite-mana line) | core | The only multi-target finisher; copied it hits each target for 2X |
| Command Tower | land | no | - | core | |
| Consider | medium | no | 3 (Gearhulk, Electro, Storm-Kiln) | keep | Reducers do not discount it (no generic cost) |
| Darkwater Catacombs | land | no | - | keep | Needs another source |
| Day of Black Sun | medium | no | 1 | watch | Kills your reducers, Dualcaster, Electro and Inventor; redundant with Ritual of Soot |
| Deflecting Swat | high | no | 1 (Azula makes it free) | core | Free while Azula is out; offensive redirect, not only protection |
| Dimir Signet | medium | no | - | keep | |
| Dragonskull Summit | land | no | - | keep | |
| Drowned Catacomb | land | no | - | keep | |
| Dualcaster Mage | medium-high | no (alone it copies your best instant or an opponent's spell) | 4 combos + every big instant | core | Hub of 4 Spellbook lines and useful alone; Azula copies it too |
| Electro, Assaulting Battery | medium | no | 6 (Ozai, Banefire, Bombardment, Snap, Agni Kai, cheap instants) | keep | Red-mana battery and a reach finisher when it leaves |
| Electrodominance | high | no | 6 (Azula, sorceries it casts at instant speed) | core | Free-casts a sorcery in Azula's combat so she copies it |
| Ember Island Production | low-medium | Dualcaster Mage for the combo, plus a payoff to win that turn | 8 (Azula, Gearhulk, Godo, Storm-Kiln, Archmage, Lo and Li, Inventor, Electrodominance) | watch | 5-mana sorcery, never copied; the combo needs 8 mana and a payoff (Bombardment, Storm-Kiln + Comet Storm, Siege) |
| Entomb | low | Torrential Gearhulk or Mystical Teachings | 2 | replace-candidate | No reanimation in the list; also a 22,400 CLP card shared with Ezio |
| Exotic Orchard | land | no | - | keep | |
| Fact or Fiction | medium-high | no | 3 (Azula, Gearhulk, reducers) | keep | |
| Fatal Push | low-medium | revolt enablers for MV 3-4 | 6 (Treasures, Mind Stone, Snap) | watch | Narrow in Commander: most threats cost 5+ |
| Fire Nation Palace | land | no | 2 (Azula, Ozai) | keep | Turns main-phase mana into combat mana |
| Foreboding Ruins | land | no | - | keep | |
| Frantic Search | high | no | 5 (Azula, Reversal, reducers, Gearhulk, Electro) | core | Free spell; nets mana when copied |
| Frostboil Snarl | land | no | - | keep | |
| Frostcliff Siege | low | its old partner (Sword of Hearth and Home) is not in the list | 3 (Ember tokens, Godo, Azula haste) | replace-candidate | Orphan of a dropped line; Temur haste is its only real job |
| Glamdring, Foe-hammer // Gleam of Death | high | no | ~30 (every instant/sorcery, Champion's Helm, Ozai) | core | 4 generic off every spell on Azula, X included |
| Go for the Throat | high | no | 2 | keep | |
| Goblin Bombardment | medium | no | 8 (tokens, Electro, Malice value loops, 2 combos) | keep | Good alone, but no card in the list can tutor it |
| Goblin Electromancer | medium-high | no | ~25 | keep | |
| Godo, Bandit Warlord | medium | no (it fetches Helm itself) | 5 (Helm, Boots, Shapeshifter, Octopus Form, Undying Malice) | keep | Self-tutoring 2-card win; weak point: must survive one turn cycle and costs 6 + 5 |
| Heartless Act | medium-high | no | 2 | keep | |
| Helm of the Host | high | no | 4 (Godo, Azula, Gearhulk, Lo and Li) | core | Win with Godo; growing army of Azulas without him |
| Hero's Downfall | medium-high | no | 1 | keep | |
| Imprisoned in the Moon | high | no | 0 | keep | Handles commanders permanently |
| Izzet Signet | medium | no | - | keep | |
| Lightning Strike | medium | no | 2 | keep | Reach to face when copied |
| Lo and Li, Twin Tutors | low | Ozai or a Lesson as the target | 3 targets (Ozai, Octopus Form, Redirect Lightning) | replace-candidate | 5 mana for a narrow tutor; cannot find Azula (not in the library) |
| Loyal Inventor | medium | no | 6 (Helm/Godo, Boots, Glamdring, Gearhulk, BMC token, cantrips) | keep | Top-of-library unless the changeling token is out |
| Mana Leak | low-medium | no | 1 | watch | Opponents pay {3} after turn 5 |
| Mind Stone | medium | no | 1 (Fatal Push revolt) | keep | |
| Mystical Teachings | high | no | ~12 targets | core | Finds 5 different combo pieces |
| Narset's Reversal | high | no | 3 combos + any spell on the stack | core | Best flexible card of the deck |
| Negate | medium-high | no | 1 | keep | |
| Nightscape Familiar | medium | no | ~30 (blue or red spells incl. creatures) | keep | Also discounts Dualcaster, Godo, Gearhulk |
| Octopus Form | high | no | 3 (Azula, Godo extra combat, Lo and Li) | keep | |
| Opt | medium | no | 3 | keep | |
| Ozai, the Phoenix King | medium-high | no | 5 (Azula, Banefire, Glamdring, Agni Kai, Electro) | keep | Hasty 7/7 and the mana battery Banefire wants |
| Ponder | medium | no | 1 | watch | Sorcery: never copied in combat |
| Reckless Handling | medium | no | 4 (Helm, Boots, Glamdring, Gearhulk) | keep | Random discard can hit the tutored card (see misplays) |
| Redirect Lightning | medium | no | 2 (Lo and Li, Azula) | keep | Second redirect after Swat |
| Ritual of Soot | medium | no | 1 | watch | Same issue as Day of Black Sun |
| Rogue's Passage | low-medium | no | 2 | watch | Colorless land; Azula does not need to connect |
| Shadowblood Ridge | land | no | - | keep | |
| Shivan Reef | land | no | - | keep | |
| Smoldering Marsh | land | no | - | keep | |
| Snap | high | no | 6 (Dualcaster combo, Electro, Gearhulk, Inventor, Lo and Li, Azula) | core | Free tempo; bounces enemy commanders |
| Sol Ring | high | no | - | core | |
| Solve the Equation | medium-high | no | ~10 targets | core | Main-phase tutor for any instant or sorcery |
| Storm-Kiln Artist | high | no | ~35 | core | Two Treasures per spell in Azula's combat |
| Stormcatch Mentor | medium | no | ~25 | keep | |
| Sulfur Falls | land | no | - | keep | |
| Sulfurous Springs | land | no | - | keep | |
| Sunken Hollow | land | no | - | keep | |
| Sunken Ruins | land | no | - | keep | |
| Swiftfoot Boots | high | no | 3 (Azula, Godo, tutors) | core | |
| Terminate | high | no | 2 | keep | |
| The Last Agni Kai | low | a big creature of yours (Ozai, Gearhulk, Azula with Champion's Helm) | 3 | replace-candidate | 12 creatures, most 1/1-2/2; the Azula copy makes her fight twice |
| Torrential Gearhulk | high | no | ~20 instants | core | |
| Ultimate Price | low-medium | no | 1 | watch | Misses multicolor commanders and colorless creatures |
| Underground River | land | no | - | keep | |
| Undying Malice | medium | no | 7 (Azula, Bombardment, Dualcaster, Gearhulk, Lo and Li, Godo, Inventor) | keep | |

Totals (83 non-basic cards, counted): core 19, keep 50, watch 10, replace-candidate 4 (Entomb, Frostcliff Siege, Lo and
Li, The Last Agni Kai). Ember Island Production sits on the boundary between watch and replace; it stays "watch" because
it is a Spellbook line and clones Azula.

## Orphan risk

Monte Carlo (40,000 draws, read-only script in the scratchpad `work/sim.py`): probability that the pieces of each line are
in the cards seen, counting each tutor once (Mystical Teachings, Solve the Equation) and ignoring mana and removal. In a
3-4 player game you see about 13 cards by your turn 5 and about 16 by turn 6-7 (7 + draws + a few cantrips).

| Line (Spellbook) | Cards | With tutors, 13 / 16 / 20 seen | Without tutors, 16 seen | Pieces dead alone |
|---|---|---|---|---|
| Godo + Helm of the Host | 1 in practice (Godo fetches Helm) | 13 % / 16 % / 20 % | 16 % | none: Helm is good on Azula; Godo is a 6-mana 3/3 tutor |
| Azula + Snap + Dualcaster Mage | 2 + Azula | 7 % / 10 % / 16 % | 2 % | none |
| Azula + Narset's Reversal + Frantic Search | 2 + Azula | 8 % / 12 % / 18 % | 2 % | none |
| Azula + Narset's Reversal + Storm-Kiln Artist | 2 + Azula | 4 % / 7 % / 10 % | 3 % | none |
| Dualcaster Mage + Ember Island Production | 2 (+ a payoff to win that turn) | 6 % / 9 % / 13 % | 3 % | Ember Island is weak alone (5-mana sorcery clone) |
| Dualcaster Mage + Goblin Bombardment + Undying Malice | 3 | 1 % / 1 % / 3 % | 0 % | none, but Bombardment has no tutor: this line is mostly on paper |
| Any of the six | | 29 % / 37 % / 49 % | 24 % | |

Reading:
- In about 6 of 10 games the deck reaches turn 6 without a complete line. The fair plan (Azula copying instants, Comet
  Storm, Electrodominance, Helm on Azula) wins those games; the playbook now says so.
- The good news for the owner's lens: unlike the Ezio list, almost every combo piece here is useful alone. Snap, Narset's
  Reversal, Frantic Search, Storm-Kiln Artist, Dualcaster Mage, Undying Malice and Goblin Bombardment all have stand-alone
  jobs. The only genuinely conditional pieces are **Ember Island Production** (needs 8 mana and Dualcaster for the
  combo, and a payoff to win the same turn) and **Godo** (needs to survive a turn and 11 mana over two turns).
- Owner's doubt 6 applied here (Dualcaster Mage + Ember Island Production, both in this list):
  - Dualcaster alone: an instant copy of the best spell on the stack (your Comet Storm keeps X; your removal or draw; an
    opponent's tutor or draw becomes yours). Cast during Azula's attack, Azula copies the Mage, so two Mages make two
    copies. It is also a piece of the Snap and Bombardment lines. It is never dead.
  - Ember Island alone: a 4/4 non-legendary clone. Best targets: Azula (a second copier from the next turn), Torrential
    Gearhulk (another free instant), Godo (fetches another Equipment, or Helm if still missing), Storm-Kiln Artist or
    Archmage Emeritus (double triggers). Medium value for 5 mana at sorcery speed. Electrodominance with X 5+ can cast it
    in Azula's combat so Azula copies it (two clones).
  - Together: infinite 4/4 Dualcaster tokens without haste (8 mana). It wins the same turn only with Goblin Bombardment,
    with Storm-Kiln Artist (each copy of Ember Island is a magecraft trigger: infinite Treasures, then Comet Storm with
    huge X and kicker), or with Frostcliff Siege on Temur (haste). With Archmage Emeritus out, every copy draws: stop
    before the library runs out. Without a payoff, it is a huge board that wins next turn unless a sweeper answers.
- Narset's Reversal + Frantic Search is **library-bound** (Spellbook says "near-infinite"): each loop draws 4 cards
  (both Frantic Search copies resolve), so with about 60 cards in the library you get about 15 loops, about +1 mana each
  (5 mana spent, 6 lands untapped), plus whatever Electro or Storm-Kiln adds. It digs the whole deck for Comet Storm; it
  is not infinite.

## Misplay corrections

Errors in the previous guide (`in/playbook-azula.json`) and natural misplays:

1. **Reckless Handling** (old: "cast it with the hand almost empty"): wrong. The discard happens after the tutored card
   is in your hand, at random, so with an empty hand you always lose the card you fetched. Cast it with 3+ other
   expendable cards (with 4 others the risk is 1 in 5).
2. **Lo and Li** (old: "Fire Lord Azula if she was removed"): wrong. Lo and Li searches the library; a removed Azula
   goes to the command zone (or graveyard/exile). Its real targets are Ozai, Octopus Form and Redirect Lightning.
3. **Loyal Inventor** (old: "you have no Assassins"): partly wrong. Black Market Connections' Shapeshifter token has
   changeling, so it is an Assassin; with it on the battlefield the artifact goes to your hand. Also: Inventor and
   Reckless Handling can fetch Torrential Gearhulk (an artifact creature).
4. **Opt and Consider "cheap with your reducers"**: wrong. Reducers only take off generic mana; {U} spells do not get
   cheaper. The same for Brainstorm and Narset's Reversal ({U}{U}).
5. **Narset's Reversal loops**: the natural line (Azula's copy of Reversal targets the spell) breaks the loop: the copy
   returns the spell to your hand and the original Reversal loses its target. The copy of Reversal must target the
   **original Reversal**; that copy then makes a second Reversal copy aimed at the spell. Now written in the card row.
6. **Undying Malice on Azula**: when she dies, do not move her to the command zone, or she will not return. If she dies
   while attacking she comes back tapped and out of combat, so the copy window ends. It does nothing for tokens and
   nothing against exile.
7. **Frostcliff Siege** (old: "Jeskai if you have several attackers"): here Temur is almost always right (haste for
   Azula, Godo and Ember tokens). Jeskai draws only on combat damage, and Azula does not need to connect.
8. **Godo's extra combat** does not untap Azula (Godo untaps only itself and Samurai). Azula attacks again only with
   Octopus Form. The Shapeshifter token (a Samurai) does untap.
9. **Deflecting Swat** is offence, not only protection: send the removal to another opponent's creature, or a
   counterspell to another spell.
10. **Electrodominance**: its free cast ignores sorcery timing (Gatherer ruling, quoted from memory, see Rules checks),
    and that cast triggers Azula. In combat it turns Ember Island Production, Aether Gale or Ritual of Soot into copied
    spells. Never use it on Banefire (X = 0).
11. **The Last Agni Kai in Azula's combat**: the copy is a second fight; if Azula is the fighter both times, she takes both
    damages. Use Ozai or Gearhulk.
12. **Abrade, Heartless Act**: the copy keeps the mode chosen for the original; only targets change.
13. **Comet Storm/Electrodominance in the graveyard**: Torrential Gearhulk casts them with X = 0; do not Entomb or discard
    them as Gearhulk targets.
14. **Mana Leak late**: in a 4-player pod after turn 5 the target almost always pays {3}; spend it early or use Negate.
15. **Swiftfoot Boots on turn 4** (old curve: "cast Azula (4), equip Boots (1)"): that needs 5 mana and Boots already on
    the battlefield; the curve section now says so.
16. **Brainstorm, Opt, Ponder after Loyal Inventor**: do not shuffle (Ponder) or bin the artifact (Consider surveil, Opt
    scry to the bottom).

## Guide errors (`in/guide.json`, Azula rows)

- The Spellbook bulk lists 6 variants inside this list; guide.json omits **Dualcaster Mage + Ember Island Production**
  (mana {4}{U}{U}{R}{R}, infinite creature tokens and magecraft).
- Combo 2 (Dualcaster + Azula + Snap) ends with "finish with Guttersnipe, Black Waltz No. 3 or Electro": Guttersnipe and
  Black Waltz No. 3 are not in this list (they were in steps 35+). In this list the finishers are Comet Storm (infinite
  land mana in the same combat), Amphibian Downpour (storm) and Electro (bounce it with a Snap copy and pay X; once,
  since Electro has no flash to recast in combat). Goblin Bombardment does not combine with this loop: the token Mage's
  Snap copy must bounce a creature that is still there when it resolves (normally the token itself).
- Combo 4 says "infinite draw" in the Spanish title; it is near-infinite and bounded by the library.
- Combo 5 does not say which spell the copy of Reversal targets; see misplay 5.

## Next-iteration candidates (jobs, not purchases)

| Weak card | The job its replacement must do | Extra synergy to look for |
|---|---|---|
| Entomb | A cheap instant that finds a combo piece **to hand** | Instant speed so Azula copies it (two tutors); finds Dualcaster Mage or Narset's Reversal |
| Lo and Li, Twin Tutors | A tutor of 3 mana or less that reaches the lines, or a creature that is good alone | Ideally a creature tutor for Dualcaster Mage / Storm-Kiln Artist (both untutorable by sorcery tutors) or a tutor for Goblin Bombardment |
| Frostcliff Siege | Haste or a second payoff for the token lines | Something that makes Ember/Dualcaster tokens or Helm tokens lethal the same turn (damage per creature entering or per spell), so Ember Island Production stops needing Bombardment |
| The Last Agni Kai | Cheap instant removal that does not need your own creature | Instant, so the Azula copy is a real 2-for-1 |
| Ultimate Price / Fatal Push | Unconditional cheap instant removal, or an instant that hits enchantments | The deck has only Chaos Warp and Aether Gale against enchantments |
| Mana Leak | A counter that stays good late (hard counter or protection) | Instant; protects Azula's key combat |
| Ponder | An instant cantrip | Copied by Azula; triggers Electro, Storm-Kiln, Archmage in combat |
| Banefire (optional) | A second instant multi-target finisher | Copyable in combat; Comet Storm is the only one now |
| One of Ritual of Soot / Day of Black Sun | Keep one sweeper; the other slot to an instant answer or a sweeper that spares your 2-drops | The pod's go-wide decks (Krenko) justify one sweeper, not two that kill your own engine |
| Ember Island Production (only if the line is cut) | A cheaper flash or instant combo piece with Dualcaster Mage | Castable in Azula's combat |

Structural gaps:
- **Sorcery load**: 9 sorceries are never copied by Azula. Turning 2-3 of them (Ponder, one sweeper, Banefire) into
  instants raises what every combat does.
- **Goblin Bombardment has no tutor**, so the Dualcaster + Bombardment + Undying Malice line is about 1 % by turn 6. A
  second sac outlet or a tutor that reaches enchantments would make it real; or accept it as a bonus line.
- **Win without the exact combo in multiplayer**: Comet Storm is the only instant that hits every opponent. Helm on
  Azula and Godo + Helm are the table-wide wins. A second "each opponent" payoff that scales with spells cast or copied
  would turn the many copied cantrips into damage.
- **Creature density**: 12 creatures in the library, mostly 1/1-2/2. Agni Kai and Bombardment fodder suffer; the
  sweepers kill 6 of them.
- **Enchantment interaction**: only Chaos Warp (instant) and Aether Gale (sorcery bounce).
- **Graveyard hate**: none (Salt's 2026-10-13 report flagged the same).
- **Life**: 4 painlands, Black Market Connections and Redirect Lightning; lifelink only via Lo and Li.

## Rules checks

Scryfall API spot checks were attempted with WebFetch and returned HTTP 403, so no Gatherer ruling could be fetched this
session. Each item is marked with its basis.

| # | Statement used | Basis | Status |
|---|---|---|---|
| 1 | Copies are not cast: they do not trigger Azula, Electro or storm again; magecraft triggers on copies | Oracle text (Archmage, Storm-Kiln say "cast or copy"); CR 707.10 from memory | verified (Oracle) / CR not fetched |
| 2 | A copy keeps X, the kicker count and the chosen mode; only targets may change | CR 707.10 from memory; Spellbook loops rely on it | well-known, not fetched |
| 3 | A copy of a permanent spell becomes a token (Dualcaster, Gearhulk, Amphibian Downpour copies) | Azula's reminder text | verified (Oracle) |
| 4 | Copies of Big Score do not require the discard (additional costs are paid only on casting) | CR 707.10 / 601.2 from memory | well-known, not fetched |
| 5 | Casting "without paying its mana cost" (Gearhulk, Electrodominance) sets X = 0; additional costs (Big Score discard) are still paid | CR 107.3, 118.9 from memory | well-known, not fetched |
| 6 | Electrodominance's free cast happens during resolution and ignores sorcery timing; that cast triggers Azula | Gatherer ruling remembered for Electrodominance; "Whenever you cast a spell" | well-known, not fetched |
| 7 | Aether Gale needs six legal targets to be cast | "six target" in Oracle; CR 601.2c from memory | well-known, not fetched |
| 8 | Changeling token is every creature type: Assassin (Loyal Inventor), Samurai (Godo), Noble (Lo and Li) | CR 702.73 from memory; Oracle of the three cards | well-known, not fetched |
| 9 | Reckless Handling's random discard can hit the tutored card | Oracle order: "put it into your hand, shuffle, then discard a card at random" | verified (Oracle) |
| 10 | A dead commander may stay in the graveyard (the owner chooses), so Undying Malice returns it | CR 903.9a from memory (optional move) | well-known, not fetched |
| 11 | A creature returned by Undying Malice is a new object, not attacking | CR 400.7, 506.4 from memory | well-known, not fetched |
| 12 | Bounced or tucked enemy commanders: owner may move them to the command zone; recasting from there pays tax again | CR 903.9b, 903.8 from memory | well-known, not fetched |
| 13 | Narset's Reversal: Azula's copy may target the original Reversal (a spell cannot target only itself) | CR 115.5 from memory; consistent with the Spellbook loop | derived, not fetched |
| 14 | Narset's Reversal + Frantic Search loop: about +1 mana and 4 draws per loop; library-bound | Oracle arithmetic; Spellbook features say "near-infinite" | derived + Spellbook |
| 15 | Dualcaster + Ember Island Production with Storm-Kiln Artist gives infinite Treasures | Spellbook features "Infinite magecraft triggers" + Storm-Kiln Oracle | derived, Spellbook-backed |
| 16 | Godo + Helm of the Host: every token is a new object, so its "first time each turn" attack trigger fires | Spellbook variant (infinite combat phases) | verified (Spellbook) |
| 17 | Godo's untap affects only Godo and Samurai; Azula stays tapped unless untapped (Octopus Form) | Oracle | verified (Oracle) |
| 18 | Helm of the Host / Ember Island tokens of Azula are non-legendary; each has its own copy trigger | Oracle of Helm and Ember Island | verified (Oracle) |
| 19 | Glamdring reduces generic mana only, X included | CR 601.2f from memory | well-known, not fetched |
| 20 | Nightscape Familiar discounts multicolor spells that are blue or red, creatures included (Azula, Ozai, Dualcaster, Godo, Gearhulk) | Oracle "Blue spells and red spells" | verified (Oracle) |
| 21 | Fatal Push revolt is met by sacrificing a Treasure or Mind Stone, or bouncing your own creature | Oracle "a permanent left the battlefield under your control" | verified (Oracle) |
| 22 | Storm counts spells cast by every player this turn | CR 702.40 from memory | well-known, not fetched |
| 23 | Firebending mana with Electro or Ozai: whether the {R}{R} that "lasts until end of combat" survives into main phase 2 | Interaction of a duration with Electro's "don't lose red mana" and Ozai's replacement | **unverified**: left out of the table; the table only claims mana from lands/rocks is kept |
| 24 | The Snap loop gives no Bombardment damage (the token's Snap copy must bounce a creature that survives to resolution) | Oracle arithmetic | derived |
