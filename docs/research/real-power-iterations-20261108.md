# Real power before and after iteration 2 (2026-11-08)

Informative only. Question (owner): Commander Salt measures the potential of ideal draws; iteration 2 rebuilt the decks
consistency-first and Salt went down for three of them. How big is the jump in REAL power, in a real 3 to 4 player pod?

Scale used: 4 = precon, 6 = upgraded deck, 7-8 = high power, 9-10 = cEDH. Estimates are judgment over the actual cards, not
a measurement. No deck file was edited; nothing was committed.

## Sources

| Deck | Before (file, how chosen) | After |
|---|---|---|
| Azula | `decks/measured/fire-lord-azula/round4-step27.txt` (Salt 8.4). The 200,000 CLP plan in `decks/reports/budget-curve.md` names round4-step27; its SHA-256 prefix matches `list_hash` 66717523bb43e4c7 in `decks/proposals/measured.json`. Steps 35 and 40 also read 8.4 but were not the bought plan. Its cards match the play review (Entomb, Lo and Li, The Last Agni Kai) | `decks/phase2/moxfield/fire-lord-azula-after-purchases.txt` (Salt 7.3, v3 section of `decks/reports/salt-fire-lord-azula-v2-20261107.md`) |
| Toph | `decks/measured/toph-the-first-metalbender/round3-step21.txt` (Salt 7.4; 200k plan; hash 16764d25098421dd matches). Step 32 also read 7.4 but was not the plan | `decks/phase2/moxfield/toph-the-first-metalbender-after-purchases.txt` (Salt 7.0, v3 section) |
| Ezio | `decks/measured/ezio-auditore-da-firenze/round5-step40.txt` (Salt 7.7; 200k plan; hash d24a5cd0c975a892 matches; cards match the list the owner played, `docs/research/play-review-ezio-20261026.md`) | `decks/phase2/moxfield/ezio-auditore-da-firenze-after-purchases.txt` (Salt 6.7, v4 section) |
| Kilo | Official precon Counter Intelligence (EOC, commander Inspirit, Flagship Vessel), from MTGJSON `CounterIntelligence_EOC.json` (100 cards, checked), Salt 3.8 (`decks/reports/salt-spanish-deck-20261107.md`) | `decks/phase2/moxfield/spanish-deck-after-purchases.txt` (Salt 4.6, v3 section of `salt-spanish-deck-v2-20261107.md`) |

Also read: `decks/phase2/<slug>.plan.json` and the consistency reports (`decks/reports/consistency-<slug>.md`, all four
PASS), `docs/research/phase2-play-review-20261026.md` and the three per-deck play reviews of 2026-10-26.

## Method

- One script (scratchpad, not in the repo) recounted both lists of each pair the same way: Oracle text from
  `data/cache/oracle-cards-20261011210156.jsonl.gz` and the Scryfall Tagger tags of `data/cache/oracle-tags.json` (ramp,
  draw/card advantage, tutor, removal, counterspell, board wipe, protection, recursion, gives haste, gives evasion, extra
  combat); lands, tapped lands (always tapped vs conditional), average mana value of the nonland cards and the curve.
  Tagger tags are broad (for example "tutor" includes land fetching), so the counts compare like with like but are not the
  builders' function counts; the real tutors are named by hand below.
- `scripts/plan_density.py` was not run on the iteration-1 lists: it needs a plan file per list and writing one after the
  fact would be my own reading of an old plan, not a fair gate. The iteration-1 play reviews (2026-10-26) already did that
  job for the three old lists and are cited instead.
- Odds of at least one of k cards by turn 5 (12 cards seen of 99): 1 = 12 %, 2 = 23 %, 3 = 32 %, 4 = 41 %, 6 = 55 %,
  8 = 66 %, 10 = 74 %, 14 = 86 %, 20 = 94 %.

## 1. Fire Lord Azula (Salt 8.4 → 7.3)

70 of the card names are shared; 16 out, 16 in. Out: Entomb, Lo and Li, Loyal Inventor, Reckless Handling (four tutors),
Consider, Ponder, Mana Leak, Heartless Act, Ultimate Price, Imprisoned in the Moon, Aether Gale, Redirect Lightning,
Banefire, Goblin Bombardment, Ember Island Production, The Last Agni Kai. In: Hidden Footblade, Haunted Cloak (haste),
Propaganda, Horizon Stone, Thermo-Alchemist, Overpowering Attack, Zuko, Azula On the Hunt, Narset Parter of Veils, Pull from
Tomorrow, Thrill of Possibility, Abandon Attachments, Waterbending Lesson, Fists of Flame, Cunning Maneuver, Soul-Guide Lantern.

| Rubric | Before (round4-step27) | After |
|---|---|---|
| Plan coherence | Spellslinger with Azula plus six exact lines; play review: Frostcliff Siege orphan, Lo and Li and Entomb weak, 9 sorceries never copied | One declared plan (Azula attacks, copies instants) with a backup; gate PASS, 0 declared orphans |
| Ramp (tag) | 14 | 15 (+Horizon Stone, Zuko and Azula On the Hunt firebending) |
| Draw / advantage (tag) | 12 | 20 |
| Real tutors | 7: Mystical Teachings, Solve the Equation, Godo (Helm), Entomb, Lo and Li, Loyal Inventor, Reckless Handling | 3: Mystical Teachings, Solve the Equation, Godo |
| Win lines | Godo + Helm; Azula + Dualcaster + Snap; Azula + Frantic Search + Narset's Reversal; Azula + Reversal + Storm-Kiln; Dualcaster + Ember Island; Comet Storm; any line by turn 6 about 24-37 % (play review) | The same four Spellbook lines (Salt lists them), Comet Storm, Electrodominance, Thermo-Alchemist pings, Overpowering Attack extra combat. Fewer tutors: lines a little less often |
| Haste for Azula | Swiftfoot Boots, Frostcliff Siege (2: 23 % by turn 5) | + Hidden Footblade, Haunted Cloak (4: 41 %) |
| Removal (tag) / cheap instant interaction | 20 / 14 | 13 / 10 |
| Counters / wipes | 3 / 2 | 2 / 2 |
| Protection | Boots, Champion's Helm, Octopus Form, Undying Malice (+ counters) | Same 4, plus Propaganda as defense while she is tapped |
| Mana | 36 lands, 3 tapped + 6 conditional, avg MV 2.60, 36 cards at MV ≤ 2 | 36 lands, same base, avg MV 2.71, 33 at MV ≤ 2 |
| Goldfish | Fair kill turn 7-9; combo kill turn 5-6 in about 1 game in 4 | Fair kill turn 7-8 (haste and window mana); combo kill turn 6 a bit rarer |
| One wipe / one removal on Azula | Weak on board, strong in hand (instants); Azula needed a turn cycle to attack | Same hand resilience; with haste equipment she attacks the turn she lands, so removal costs one attack less often |

Real power: before 7.0-7.5, after 7.2-7.7. Confidence: medium-low (no games with the new list).

Plain words: the new Azula attacks the turn she comes down far more often (twice the haste), refills her hand much better
(20 draw pieces against 12) and keeps her mana between turns, so the fair game of copying instants actually happens in more
games. What it gave up is real: four tutors and about a third of its cheap removal. The jump is small, +0.2 to +0.3, not a
new tier. Salt's 8.4 was the old list's six combo lines and seven tutors seen as ideal draws (Salt itself flagged it Bracket
4 and "kitchen-sink wincon"); the play review showed those lines came together by turn 6 in only about a quarter of games.
Salt's drop to 7.3 is almost all its "no tutors for the wincon combos" penalty (-0.45); in a real pod that matters less than
Salt says, so I rate the new list above its Salt and the old one below its Salt.

## 2. Toph, the First Metalbender (Salt 7.4 → 7.0)

60 names shared; 20 out, 23 in. Out: Arbaaz Mir, five rocks (Chromatic Lantern, Everflowing Chalice, Boros Locket, Selesnya
Signet, Bender's Waterskin), Liquimetal Coating, Hardened Scales, Haywire Mite, Hunter's Bow, Haru, Earth Kingdom General,
Wrenn and Realmbreaker, Fateful Absence, Rocky Rebuke, Inscription of Abundance, Redirect Lightning, Nutrient Block,
Soul-Guide Lantern, Rumble Arena. In: The Earth King, Seismic Tutelage, Rampaging Baloths, Druid Class, Explore, Wood Elves,
Cultivate, Roiling Regrowth, Solemn Simulacrum, Burnished Hart, four fetch-style lands (Evolving Wilds, Terramorphic
Expanse, Myriad Landscape, Vibrant Cityscape) plus Cabaretti Courtyard, Battlefield Forge, Secret Tunnel, Hakoda, Aang's
Iceberg, Generous Gift, Water Tribe Rallier, Stocking the Pantry, Drannith Magistrate.

| Rubric | Before (round3-step21) | After |
|---|---|---|
| Plan coherence | Landfall drain was the real plan (play review), diluted by a Bumi + Liquimetal line, counters package and rocks; 1 real orphan (Liquimetal Coating), several low-impact fillers | One plan: 2 to 4 land entries per turn, each one 1 damage to every opponent; backup land army. Gate PASS; 1 declared orphan (Drannith Magistrate). The plan text still names Arbaaz Mir, which left the list |
| Ramp (tag) | 22 (many rocks that are landfall only with Toph out) | 25, most of them land entries that work without Toph |
| Draw (tag) | 12 | 13 (+Stocking the Pantry, Rallier) |
| Tutors (real ones) | Chord of Calling, Brightglass Gearhulk, Reckless Handling, Crop Rotation, land tutors | Same core plus Water Tribe Rallier and more land tutors; Salt still sees "no tutors for the combos" (-0.34) |
| Win lines | Landfall drain (Tannuk, Sabotender, Arbaaz, Valakut), Ragost + Bombardment, Ashaya loops, Bumi + Liquimetal; any infinite by turn 9 about 34 % | Landfall drain (one payoff fewer), Ragost + Bombardment, land army with The Earth King, Seismic Tutelage, Baloths, Bumi; Ashaya + Bumi, Cobra + Nantuko. More fuel for the same payoffs |
| Removal (tag) / cheap instant | 15 / 7 | 12 / 4 |
| Wipes / counters | 1 / 0 | 1 / 0 |
| Protection | 7 (Hunter's Bow, Wrenn among them) | 7, now with Hakoda (team indestructible), Aang's Iceberg (flash exile) |
| Mana | 35 lands, 3 tapped + 4 conditional, avg MV 2.30, 39 at MV ≤ 2 | 38 lands, 4 tapped + 4 conditional, avg MV 2.61, 30 at MV ≤ 2 |
| Goldfish | Drain kill turn 8-10 | Drain or army kill turn 7-9 |
| One wipe / removal on Toph | Earthbent lands return; rocks lose their landfall when Toph dies | Land entries keep working without Toph; Hakoda can blank a wipe; lands return |

Real power: before 6.6-7.1, after 7.0-7.4. Confidence: medium.

Plain words: the old deck's best games were the landfall drain, but many of its "land drops" were rocks that only counted
while Toph lived. The new deck puts real lands onto the battlefield every turn with or without Toph, has a second way to
win (a land army that fetches more lands when it attacks) and survives a wipe better. It is slower to start (higher curve,
fewer one- and two-drops) and has fewer cheap answers, so it is weaker against a fast combo player. Net +0.3 to +0.4. Salt
penalizes it as "too slow for its pieces" and "combos with no tutors"; in a real pod the redundancy of the drain matters
more than tutoring a two-card combo, so I put it at or a little above its Salt.

## 3. Ezio Auditore da Firenze (Salt 7.7 → 6.7)

The biggest rebuild: 38 names out, 36 in. Out: the mini-combo and value pieces the owner doubted (Etrata's copiers
Strionic Resonator, Lithoform Engine, Return the Favor; Dualcaster Mage + Ember Island Production; Intruder Alarm; Deadeye
Navigator; Nekrataal; Royal Assassin; Venser; Adéwalé; Winter Soldier; Ravenloft Adventurer), cheap spells (Brainstorm,
Faithless Looting, Fatal Push, Bitter Triumph, Fateful Absence, Murder, Mystical Teachings, Seismic Sense) and five tapped or
colorless lands. In: Assassin lords and finishers (Achilles Davenport, Bayek of Siwa, Rally the Peasants, Unstoppable
Slasher, Shao Jun, Layla Hassan, Ratonhnhaké꞉ton, Brotherhood Spy, Merciless Harlequin, Lion Vulture), evasion and haste
(Hookblade, Glider Staff, Cover of Darkness, Haunted Cloak, Hidden Footblade, Rogue's Passage), protection (Angelic
Intervention, Enter the Avatar State, Gold-Forged Thopteryx, Haystack), defense (Propaganda, Ghostly Prison), wipes
(Mephitic Vapors, What Must Be Done), Swords to Plowshares, Get Out, Eagle Vision.

| Rubric | Before (round5-step40, the list that lost twice) | After |
|---|---|---|
| Plan coherence | Several plans: Ezio + Sphinx, Etrata autowin (about 2 % by turn 9), Dualcaster loop with no payoff, Intruder Alarm (no line, anti-synergy); play review: many pieces dead alone, gaps in finishing more than one player, wrath insurance, evasion | One plan: evasive Assassins connect from turn 2-3, freerunning makes them cheap, Sphinx + Ezio removes one player, team damage the rest. Gate PASS, 0 orphans |
| Ramp (tag) | 8 | 7 (Salt: "only 6 ramp cards" for a WUBRG trigger) |
| Draw (tag) | 17 | 14 (Eagle Vision, Harlequin, Lion Vulture; hit-based) |
| Real tutors to Sphinx | Loyal Inventor, Reckless Handling, Entomb, Seismic Sense: about 68 % to see Sphinx or a tutor by turn 9 (play review); Mystical Teachings for instants | Loyal Inventor, Reckless Handling, Entomb, plus recursion (Restart Sequence, What Must Be Done, Kaya): about 60 % |
| Win lines | Ezio + Sphinx (one player); Etrata on paper; no team finisher | Ezio + Sphinx; Assassin beatdown with two lords, Bayek double strike, Slasher halving life, Rally; Shao Jun and Kaya pings to each opponent |
| Evasion givers / haste | 3 / 1 | 8 / 4 |
| Removal (tag) / cheap instant | 20 / 7 | 14 / 6 |
| Wipes | 1 (Starfall Invocation) | 2 (Mephitic Vapors, What Must Be Done; What Must Be Done can instead return a historic card) |
| Protection | 3 | 6, plus ward 2 on legends, Slasher returns |
| Mana | 35 lands, 3 tapped + 11 conditional, avg MV 2.88, 26 at MV ≤ 2 | 36 lands, 1 tapped + 12 conditional, avg MV 2.94, 24 at MV ≤ 2; green sources 12 → 9 (the WUBRG trigger is a little harder) |
| Goldfish | First elimination turn 7-9 if Sphinx shows up, otherwise a slow value game | First elimination turn 6-8; table kill turn 8-10 |
| One wipe / removal on Ezio | Weak: few protection pieces, combo pieces stranded in hand | Better: 6 protection pieces, Propaganda and Ghostly Prison while tapped, and the team still wins without Ezio |

Real power: before 6.0-6.5, after 6.6-7.1. Confidence: medium-low (the "before" is anchored on two lost games, a tiny sample).

Plain words: the old Ezio held cards that only worked together and lost to a deck Salt rated far lower. The new Ezio starts
attacking on turn 2 or 3 with creatures that cannot be blocked well, gets cheaper Assassins and cards from every hit, and
has a way to finish the other two players after Sphinx removes one. It also defends itself while tapped. This is the
clearest real jump of the three, about +0.6. Salt went DOWN 1.0 because it valued the old list's combo count and tutors
(and called it Bracket 4); the new list's 6.7 on Salt is close to my estimate, while the old 7.7 was well above what it
showed in play.

## 4. Kilo (precon Counter Intelligence 3.8 → 4.6)

The commander changes (Inspirit in the precon, Kilo in the Spanish deck); 71 names shared. Out: Alibou, Angel of the Ruins,
Chain Reaction, Cloud Key, Depthshaker Titan, Etherium Sculptor, Gavel of the Righteous, Golem Foundry, Hangarback Walker,
Mindless Automaton, Pull from Tomorrow, Threefold Thunderhulk, Thrummingbird, Wake the Past, The Mycosynth Gardens and eight
tapped lands. In: Swiftfoot Boots, Relic of Legends, Commander's Sphere, Talisman of Conviction, Prophetic Prism, North Pole
Patrol, Katara, Reckless Fireweaver, Meticulous Excavation, Barrels of Blasting Jelly, Generous Gift, Swords to Plowshares,
Muddle the Mixture, Volt Charge, Tranquilize, Airbending Lesson, Waterbending Lesson, Sandbenders' Storm.

| Rubric | Before (precon) | After |
|---|---|---|
| Plan coherence | Precon: artifacts and counters around Inspirit's station, several expensive top-end cards | One plan: Kilo taps every turn to proliferate the counters of about 22 artifacts; Darksteel Reactor and Lux Artillery close. Gate PASS (one function reaches its minimum only with Kilo) |
| Ramp (tag) | 8 | 12 |
| Draw (tag) | 13 | 16 |
| Tutors | Angel of the Ruins (plainscycling) | Muddle the Mixture (transmute, MV 2); none for the finishers |
| Win lines | Darksteel Reactor, combat with big artifacts; Salt: "control without a finisher" | Darksteel Reactor funnel, Lux Artillery (10 to each opponent), Cyberdrive Awakener alpha strike, a three-card Crawler + Lux + Excavation loop |
| Removal (tag) / cheap instant | 9 / 3 | 12 / 4 |
| Wipes / counters | 3 / 1 | 2 / 2 |
| Protection | 2 | 4 (Boots, Airbending Lesson) |
| Mana | 40 lands, 11 tapped + 4 conditional, avg MV 3.34, 20 at MV ≤ 2, 6 cards at MV 7+ | 37 lands, 4 tapped + 4 conditional, avg MV 2.98, 23 at MV ≤ 2, 2 at MV 7+ |
| Goldfish | Turn 11-13+ | Turn 9-11 (Reactor plus proliferate; Lux Artillery a turn or two later) |
| One wipe / removal on Kilo | Inspirit gives other artifacts hexproof and indestructible once stationed | Kilo at MV 3 with haste is cheap to recast; counters spread over artifacts survive a creature wipe; an artifact wipe still ruins it |

Real power: before 4.0-4.5, after 4.8-5.3. Confidence: medium.

Plain words: the precon plays a land tapped every other turn and tops out with expensive cards. The Spanish deck plays on
curve, ramps harder, answers more threats and actually has a finisher that hits the whole table (Lux Artillery) next to the
slow Reactor. It is a well-tuned upgraded precon, not a high-power deck: no tutors for the finishers and slow, visible win
conditions. Jump about +0.8, close to Salt's +0.8; I put both lists a few tenths above Salt because Salt's "control without
a finisher" penalty undercounts Lux Artillery and the artifact alpha strike in a real game.

## Summary

| Deck | Salt before → after | Real power before → after | Jump | Main reason | Confidence |
|---|---|---|---|---|---|
| Azula | 8.4 → 7.3 | 7.0-7.5 → 7.2-7.7 | +0.2 to +0.3 | Twice the haste and much more draw make the fair game happen; four tutors and cheap removal lost | medium-low |
| Toph | 7.4 → 7.0 | 6.6-7.1 → 7.0-7.4 | +0.3 to +0.4 | Real land entries every turn with or without Toph, second win route, better vs wipes; slower curve, fewer answers | medium |
| Ezio | 7.7 → 6.7 | 6.0-6.5 → 6.6-7.1 | about +0.6 | One evasive Assassin plan that connects from turn 2-3 and finishes the whole table, protected; dead mini-combos gone | medium-low |
| Kilo | 3.8 → 4.6 | 4.0-4.5 → 4.8-5.3 | about +0.8 | Lower curve, untapped mana, more ramp and answers, a table-wide finisher | medium |

Honest reading: iteration 2 made every deck more consistent, but only Ezio and Kilo are clearly stronger in real play.
Azula and Toph are modest gains (a few tenths) that would be hard to feel in a handful of games; Azula's gain could even be
zero if the lost tutors matter more than I think. None of the three upgraded decks moved into a new tier: they are all in
the high-power band (about 6.6 to 7.7), Ezio at its low end. Where Salt went down it was mostly Salt's own combo and tutor
counting (penalties of -0.34 to -0.45 for "combos with no tutors"), which overrated the old lists' ideal draws.

Biggest levers left, from this recount: Azula and Ezio would gain most from one or two cheap tutors back (Ezio: also ramp for
WUBRG); Toph from two or three cheap instant answers; Kilo from any tutor that reaches Darksteel Reactor or Lux Artillery.
