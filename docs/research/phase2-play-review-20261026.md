# Play review of the three final decks (2026-10-26)

Why: the owner played the Ezio deck and asked (1) for a guide that says how to USE each card in its deck, not what the card
says, and (2) whether some cards really lack synergy or he simply played them wrong. He does not want a deck full of
"exact and inflexible" mini-combos that leave dead cards in hand in 3 to 4 player pods; broad synergy and stand-alone value
count next to the Commander Salt score (rule saved in memory, `feedback-synergy-over-salt`). Nothing was removed: the
findings feed the Phase 2 optimization (4 decks from the owned collection).

Method: three Opus 5.5 (high) agents, one per deck, each over the exact final list, the Oracle text of every card
(`scripts/dashboard_cards.py`), the Spellbook-verified combos and the Commander Salt reports; rulings read from Scryfall
where the API answered (Ezio agent; the other two got HTTP 403 and marked those points as unverified). The main session
checked the output (100 cards per deck, names, quantities, mana-cost notation, no card outside the deck, Oracle spot
checks) and corrected two statements before publishing. Full reports: `play-review-ezio-20261026.md`,
`play-review-azula-20261026.md`, `play-review-toph-20261026.md` (verdict table, orphan risk, misplay corrections, rules
checks, next-iteration jobs). The guide that the dashboard shows is `data/model/dashboard/playbook-<deck>.json`.

## The owner's seven doubts (Ezio deck)

| Card | Owner's reading | Verdict | What the card really does here |
|---|---|---|---|
| Winter Soldier, Icy Assassin | Equipment card, useless here | Partly right: only 2 Equipment (Swiftfoot Boots, Assassin Gauntlet) | Fair 2-mana menace Assassin that turns on freerunning on turn 3, vigilance, comes back from the graveyard for {3}{W}{B}. Watch: a 2-drop that also draws or protects would do more |
| Deadeye Navigator | 5 mana, protects once, 4 per turn | Wrong: it costs {4}{U}{U} (6) and each protection costs {1}{U} on the one creature | Ruling 2017-03-14: the pair breaks and the soulbond trigger re-pairs at once. Best partners: Etrata the Silencer (blink in response to her trigger), Magister Sphinx, Adewale, Loyal Inventor, Nekrataal. Does not stop a wrath |
| Roshan, Hidden Magister | 80-90 % already Assassins | Partly wrong: 17 of 24 creatures (71 %); the 7 others include Sphinx (7) and Deadeye (6) | With Roshan, Sphinx costs {B}{B} after a hit, Revelations III / Jacob Frye / Adewale can use it, and library, hand and graveyard creatures count as Assassins |
| Adewale, Breaker of Chains | Only works on entering, no Vehicles | Right about the Vehicle text, wrong about the card | The enter trigger is the job: reveal 6, take an Assassin (about 70 %, 84 % with Roshan); cast for {B}{B} after a hit it is a 2-for-1 |
| Nekrataal | Costly for a removal, spends one of 2 reanimations | Mostly right | Replace candidate: 12 other removal spells, most cheaper and instant. Never spend Entomb or Restart Sequence on it |
| Dualcaster Mage + Ember Island Production | Combo needs both; other synergy? | Mage is useful alone; Ember Island is the weak half | The loop has no winning payoff in the Ezio list (only Desmond Miles with Roshan, derived). Mage copies Restart Sequence (two reanimations), removal, Teachings; Ember Island copies Sphinx, Ezio, Blade of Vengeance, Etrata |
| Etrata, the Silencer | Dead weight without the combination | Partly right about the autowin, wrong that she is dead | Unblockable removal; stays on the battlefield if the player has no creatures; blink or bounce her in response to her trigger; Ravenloft Adventurer turns every opposing death into a hit counter |

## Weakest cards found (replace or watch candidates, as jobs for the next iteration)

- Ezio: Intruder Alarm (no working line), Nekrataal, Everflowing Chalice, Dimir Locket; then Fatal Push, Mana Leak,
  Faithless Looting, Tome of Legends, Ember Island Production, Winter Soldier and four lands that enter tapped or make
  only colorless mana. Structural gaps: finishing more than one player, wrath insurance, one more evasion effect.
- Azula: Entomb, Lo and Li, Frostcliff Siege (its partner card left the list), The Last Agni Kai; watch Ember Island
  Production, Ultimate Price, Fatal Push, Mana Leak, Ponder, Banefire and carrying two sweepers. 9 sorceries are never
  copied by Azula. A complete combo by turn 6 happens in about 4 of 10 games.
- Toph: Boros Locket and Haru as replace candidates, Liquimetal Coating the only real orphan piece; watch Earth Kingdom
  General, Soul-Guide Lantern, Rampant Growth or Shared Roots, Hardened Scales. Any infinite line comes together in at
  most 34 % of games with tutors; the deck mostly wins by landfall drain.

## Errors of the old guide that were fixed

Reckless Handling "with an almost empty hand" (the random discard can hit the card just fetched); Lo and Li cannot find
Azula; Loyal Inventor puts the artifact in hand when Black Market Connections' Shapeshifter (an Assassin) is in play;
cost reducers do not make Opt or Consider cheaper; Narset's Reversal loops must target the original Reversal; Chord of
Calling puts Springheart Nantuko in unattached; The Stasis Coffin protects the player, not Toph; Provisioner should make
Treasures (Ragost makes them Food); earthbending Ashaya, Bumi or Gearhulk leaves them 0/0; Brotherhood Headquarters cannot
pay Ezio's {W}{U}{B}{R}{G}. The combo guide (`guide.json`) gained the missing Spellbook lines (Azula: Dualcaster Mage +
Ember Island Production; Toph: Springheart Nantuko with Lotus Cobra or Tireless Provisioner, and The Stasis Coffin) and
lost finishers that are not in the Azula list (Guttersnipe, Black Waltz No. 3).
