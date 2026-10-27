<!-- Written 2026-10-26 by an Opus 5.5 (high) review agent for the owner. Paths such as in/list-<deck>.txt and in/cards-facts.json refer to the review workspace: the lists are the final ones in decks/measured/, the card facts come from scripts/dashboard_cards.py. -->

# Toph, the First Metalbender: synergy review (2026-10-26)

Scope: the 100-card list in `in/list-toph.txt` (77 non-basic cards incl. the commander, 23 basics). Card text from
`in/cards-facts.json`; P/T and Wrenn's loyalty from the local Scryfall oracle bulk (`data/cache/oracle-cards-20261011...`);
combos from `in/guide.json` plus the local Commander Spellbook bulk (`data/cache/spellbook_variants_slim.jsonl.gz`),
filtered to variants whose every card is in this list (13 variants, listed under Orphan risk). Scryfall's API answered
HTTP 403 to WebFetch, so no Gatherer ruling could be spot-checked online; see Rules checks.

Headline: unlike the owner's Ezio complaint, this deck's combo pieces are mostly good on their own. The fair plan
(landfall drain to every opponent at once, with Toph turning every nontoken artifact into a land) is the real plan in a
3-4 player game; the infinite lines are a bonus that shows up in roughly 1 game in 3 by the time about 17 cards have been
seen (Monte Carlo below). The weak spots are a few low-impact filler cards, not orphan combo pieces.

## Verdict table

Stand-alone = value with no specific partner in hand (Toph on the battlefield is assumed for artifact cards, because the
commander is always available). Breadth = rough count of other cards in this list it works with.

| Card | Stand-alone | Needs exact partners? | Breadth | Verdict | Reason |
|---|---|---|---|---|---|
| Toph, the First Metalbender | high | no | ~45 (20 artifacts, all landfall and earthbend cards) | core | Every artifact is a land drop with landfall; free earthbend 2 each turn |
| Annie Joins Up | high | no | 9 legendary creatures | keep | 5-damage removal alone; doubles Tannuk, Arbaaz, Toph x3, Bumi, Haru |
| Arbaaz Mir | high | no | ~30 (20 artifacts, 11 legendaries) | core | 2-mana drain per artifact/legend; lifegain also untaps Ragost |
| Arcane Signet | medium | no | broad | keep | Turn-2 fixing rock |
| Ashaya, Soul of the Wild | high | no | ~20 | core | Huge body alone; makes every creature a landfall; piece of 3 Spellbook lines |
| Ba Sing Se | medium | no | ~8 earthbend payoffs | keep | Mana sink that earthbends every turn |
| Beast Within | high | no | - | keep | Answers any permanent at instant speed |
| Bender's Waterskin | medium | no | instants, Clues, Ragost | keep | Mana on every opponent's turn |
| Boros Locket | low | no | Ragost only | replace-candidate | 3 mana for one R/W mana; the draw mode costs 4 more and a tap |
| Brightglass Gearhulk | medium-high | no | 9 targets with MV 1 or less | keep | Two-card tutor + 4/4; {G}{G}{W}{W} is hard in a green-heavy base |
| Bumi, Unleashed | high | no | earthbend payoffs, Coating, Ashaya, Rogue's Passage | core | Earthbend 4 + 5/4 trample + extra combat alone; piece of 2 infinite lines |
| Chord of Calling | medium-high | no | ~17 creatures | core | Instant tutor; must not be used for Nantuko (enters unattached) |
| Chromatic Lantern | high | no | ~12 artifacts with no mana ability | core | With Toph turns Zuran Orb, Haystack, Ichor, Chalice-for-0 into rocks |
| Clifftop Retreat | medium | no | - | keep | Untapped dual from turn 2 |
| Collective Resistance | medium-high | no | - | keep | Protection (hexproof stops targeted exile) or artifact/enchantment removal |
| Command Tower | medium | no | - | keep | Fixing |
| Crop Rotation | medium | no | earthbent lands, Heaped Harvest, Ichor, Rogue's Passage | keep | 2-3 landfalls for {G}; cannot fetch artifacts |
| Cycle of Renewal | medium | no | earthbent lands, Harvest, Valakut | keep | Instant-speed land ramp and landfall burst |
| Earth Kingdom General | low-medium | Ashaya + Bombardment or Zuran Orb for the combo | ~8 (Ragost, Terrasymbiosis, Haru, counters) | watch | 4 mana for a 2/2 + earthbend 2; Blind Bandit does the same loop for 3 |
| Earthbender Ascension | medium-high | no | all landfall | keep | Ramp + earthbend + late trample counters |
| Everflowing Chalice | medium | no | Lantern, Wrenn, Guide, Cobra, Arbaaz, Ragost | keep | Free landfall with Toph; a 0-mana rock with a mana-granting card |
| Exotic Orchard | medium | no | - | keep | Fixing in multiplayer |
| Fateful Absence | high | no | - | keep | 2-mana instant removal |
| Fortified Village | medium | no | - | keep | Untapped dual early |
| Furycalm Snarl | medium | no | - | keep | Untapped dual early |
| Game Trail | medium | no | - | keep | Untapped dual early |
| Goblin Bombardment | high | no | earthbent lands, pingers, loopers | core | Repeatable reach alone (sac earthbent lands that return); wins with Ashaya + looper |
| Great Divide Guide | high | no | all artifacts, Allies, Ashaya | core | With Toph every artifact becomes a rock of any color |
| Hardened Scales | low-medium | no | ~10 earthbend/counter cards | watch | +1 counter per earthbend; small impact alone |
| Hardlight Containment | high | an artifact you control (20 in the list) | - | keep | 1-mana exile; Gearhulk can fetch it |
| Harrow | medium-high | no | earthbent lands, Harvest | keep | Instant ramp, up to 4 landfalls |
| Haru, Hidden Talent | low | Allies (6 others, incl. the commander) | 6 | replace-candidate | 2-mana 1/1 that earthbends 1 per Ally; no impact without a stream of Allies |
| Haystack | medium | no | - | keep | Repeatable protection for Toph/Ashaya/Bumi |
| Haywire Mite | medium | no | Gearhulk, Coating, earthbend, Ragost | keep | Cheap stax answer; earthbent it works twice |
| Heaped Harvest | high | no | Zuran Orb, Harrow, Crop Rotation, Cycle, Ragost, earthbend | core | With Toph 2 landfalls on cast and 1 per sacrifice |
| Hunter's Bow | medium-high | no | big creatures, earthbent lands | keep | Removal that is also a landfall; ward {2} after |
| Ichor Wellspring | medium | no | sac outlets, earthbend | keep | Cantrip x2; earthbent it draws on death and on return |
| Inscription of Abundance | medium-high | no | counters payoffs, big creatures | keep | Fight, counters (Terrasymbiosis draw) or all three |
| Liquimetal Coating | low | Toph + Bumi for the combo | 5 (Bumi, Collective Resistance, Origin, Haywire Mite, Ragost) | watch | Only real job is the Bumi line; fair uses are marginal |
| Lotus Cobra | high | no | all artifacts and landfall | core | Mana per artifact with Toph; piece of the Nantuko line |
| Nutrient Block | medium | no | Ragost, Zuran Orb, earthbend | keep | Indestructible fodder that draws |
| Origin of Metalbending | medium-high | no | - | keep | Removal or protection at instant speed |
| Path to Exile | high | no | - | keep | 1-mana exile |
| Planar Outburst | medium | no | earthbent lands, Ashaya | watch | One-sided only with Ashaya or a land-creature board; kills Toph and every engine otherwise |
| Ragost, Deft Gastronaut | high | no | every artifact incl. Treasures and Clues | core | 3 damage to each opponent per artifact; untaps on any turn you gained life |
| Rampant Growth | low-medium | no | landfall | watch | Redundant late; one of many land-ramp spells |
| Reckless Handling | medium | no | 20 artifacts | keep | Artifact tutor, but random discard can hit the tutored card |
| Redirect Lightning | medium | no | - | keep | 1-mana protection vs single-target removal |
| Rocky Rebuke | medium | a creature with power 3+ | big creatures | keep | One-sided bite; dead on an empty board |
| Rogue's Passage | high | no | Bumi, Ashaya | core | Bumi's line repeats it every combat |
| Rootbound Crag | medium | no | - | keep | Untapped dual |
| Rugged Prairie | medium | no | - | keep | {W}{W} for Gearhulk and Outburst |
| Rumble Arena | medium-high | no | earthbend | keep | Best earthbend target (vigilance) |
| Sabotender | high | no | all landfall | core | 2-mana drain per land; finisher for infinite landfall |
| Sakura-Tribe Elder | medium | no | landfall, Chord | keep | Ramp + chump |
| Seismic Sense | medium | no | creatures and lands | keep | Cheap dig; better late with many lands |
| Selesnya Signet | medium | no | - | keep | Fixing rock |
| Shared Roots | low-medium | no | Hardheaded Teacher | watch | Same as Rampant Growth; Lesson only matters with Hardheaded |
| Sol Ring | high | no | broad | core | Fast mana |
| Soul-Guide Lantern | low-medium | no | Ragost, Zuran Orb | watch | Graveyard hate that is often irrelevant; 1-mana landfall + slow cantrip |
| Springheart Nantuko | medium | Lotus Cobra or Tireless Provisioner + a land creature (Toph gives one free each turn) | ~8 | keep | Infinite landfall with one of two common partners; alone copies Tracker/Provisioner |
| Stroke of Midnight | high | no | - | keep | Instant removal for any nonland permanent |
| Sunpetal Grove | medium | no | - | keep | Untapped dual |
| Swords to Plowshares | high | no | - | keep | 1-mana exile |
| Talisman of Impulse | medium | no | - | keep | Turn-2 rock |
| Tannuk, Memorial Ensign | high | no | all landfall, Annie | core | Drain + card per turn |
| Terrasymbiosis | high | no | ~12 earthbend/counter cards | core | Draws 2 every turn from Toph's end-step earthbend alone |
| The Stasis Coffin | medium-high | Toph (always available) | Toph, Arbaaz, landfall | keep | Spellbook lock: protection from everything on every opponent's turn for {2}; returns each turn as a landfall |
| Tireless Provisioner | high | no | all landfall, Ragost | core | Treasure per land/artifact; Nantuko partner |
| Tireless Tracker | high | no | landfall, Ragost, Terrasymbiosis | core | Main card flow |
| Toph, Hardheaded Teacher | medium-high | no | every spell, Lessons, Terrasymbiosis | keep | Earthbend per spell + regrowth on entry |
| Toph, the Blind Bandit | medium-high | no | all earthbend | keep | Cheap growing threat; looper with Ashaya |
| True Ancestry | medium | something worth returning | - | keep | Regrowth of any permanent + Clue |
| Valakut Exploration | high | no | all landfall | core | Card advantage + drain |
| Wayfarer's Bauble | medium | no | landfall | keep | Turn-1 ramp, 2 landfalls with Toph |
| Wrenn and Realmbreaker | high | no | all artifacts, Nantuko | core | Every artifact a rock; +1 makes a protected land creature |
| Zuran Orb | medium | no for fair use; Ashaya + looper for combo | ~10 sac-value lands, Ragost | keep | Free landfall; instant-speed lifegain that untaps Ragost; land-destruction insurance |

Counts (77 rows, checked by script): core 20, keep 48, watch 7 (Earth Kingdom General, Hardened Scales, Liquimetal
Coating, Planar Outburst, Rampant Growth, Shared Roots, Soul-Guide Lantern; Reckless Handling is a borderline keep),
replace-candidate 2 (Boros Locket, Haru).

## Orphan risk

All 13 Spellbook variants fully inside this list (local bulk, status OK):

| Line | Spellbook variant(s) | Pieces from hand | Pieces dead alone? | Tutors that reach it |
|---|---|---|---|---|
| A. Ashaya + Bumi (infinite combats) | 539-7033 (in guide.json) | 2 (5 mana each) | none: both are strong alone | Chord (X=5), Seismic Sense |
| B. Ashaya + Blind Bandit or General + Bombardment or Zuran Orb | 539-5147-7085/-7037, 539-1315-7085/-7037 (in guide.json) | 3, with 2x2 alternatives | none: Bombardment, Blind Bandit good alone; Orb and General medium | Chord, Seismic Sense (creatures); Gearhulk, Reckless Handling (Orb) |
| C. Toph + Springheart Nantuko + Lotus Cobra or Tireless Provisioner | 3470-5702-6871, 3875-5702-6871 (+ generic "card that earthbends" variants 3470-5702--143, 3875-5702--143); NOT in guide.json | 2 (commander + land creature are free) | Nantuko medium alone; Cobra and Provisioner are core alone | Chord (Cobra, Provisioner only), Seismic Sense (all three) |
| D. Toph + Bumi + Liquimetal Coating | 662-6871-7033; NOT in guide.json | 2 | Coating is weak alone | Reckless Handling (Coating); Chord, Seismic (Bumi) |
| E. Toph + The Stasis Coffin (protection lock, not a win) | 4155-6871; NOT in guide.json | 1 | no | Reckless Handling |

Monte Carlo (40,000 draws, 99-card library, tutors treated as free wildcards that fetch one reachable piece, mana and
Seismic Sense misses ignored, so these are upper bounds):

| Cards seen | Any infinite line (A-D), no tutors | Any infinite line, with tutors | Line A | Line B | Line C | Line D |
|---|---|---|---|---|---|---|
| 12 (about turn 5) | 5 % | 19 % | 7 % | 4 % | 8 % | 7 % |
| 17 (about turn 9, or earlier with Tracker/Terrasymbiosis) | 11 % | 34 % | 14 % | 10 % | 15 % | 13 % |
| 22 | 19 % | 48 % | 22 % | 18 % | 23 % | 21 % |

Reading: in 3-4 player games the deck must win with drain plus combat most of the time, and it can: every piece of A, B
and C has stand-alone value. The only real orphan is **Liquimetal Coating** (line D), and second **Earth Kingdom General**
(the costlier of the two loopers). Line C is the most likely infinite and it was missing from the guide; it is now in the
win section and on the Nantuko, Cobra and Provisioner rows.

## Misplay corrections (the old guide or the natural play was wrong)

1. **Reckless Handling**: the old guide said cast it "with the hand almost empty". Wrong: the search goes to the hand
   first and then a card is discarded at random, so with an empty hand you discard the card you just found. Cast it with
   3 or more other cards in hand.
2. **Chord of Calling for Springheart Nantuko**: the proposal lists Chord as reaching Nantuko for line C. Chord puts it
   onto the battlefield as a creature, not attached (bestow only applies when cast for its bestow cost), so it cannot make
   copies of a land. With Nantuko in hand, Chord must fetch Lotus Cobra (X=2) or Tireless Provisioner (X=3).
3. **Tireless Provisioner, "choose Food for Ragost"**: wrong. Ragost makes every artifact you control a Food, tokens
   included, so a Treasure is also Ragost ammo and also a 3-life Food. With Ragost out, Treasure is strictly better.
4. **The Stasis Coffin "protects Toph"** (old commander and protect sections): wrong; it gives the player protection.
   The guide also missed the Spellbook line: earthbend the Coffin at your end step, pay {2}, exile it, it returns tapped
   (landfall, Arbaaz trigger) and untaps on your turn: protection from everything on every opponent's turn.
5. **Collective Resistance "does not save from exile"**: wrong for targeted exile (Swords, Path): hexproof in response
   makes them fizzle. It does not stop untargeted exile or sacrifice.
6. **Wrenn's −2 to get Ashaya back from the graveyard** (old graveyard section): wrong; −2 mills 3 and takes a permanent
   from those 3 only.
7. **Bumi needs to be unblocked**: he has trample, so trample-over damage triggers him; only a blocker with toughness
   at least his power stops him. Also, the "infinite mana" of line A is only usable at instant speed: Bumi gives extra
   combat phases, never an extra main phase.
8. **Earthbend targets**: Toph's end-step earthbend sets the target's base P/T to 0/0. Never earthbend Ashaya, Bumi or
   Gearhulk when they are lands (Ashaya's effect, or Toph for the artifact Gearhulk): Ashaya would become 0/0+2. Good
   targets: Rumble Arena (vigilance), Ichor Wellspring (draws on death and on return), Heaped Harvest (basic on sacrifice
   and on return), Nutrient Block (an indestructible creature), Haywire Mite (two uses), The Stasis Coffin (the lock), a
   Forest for Springheart Nantuko.
9. **Planar Outburst** kills Toph (a nonland creature) and every creature engine unless Ashaya is out; the old guide
   only said what survives.
10. **Seismic Sense and Crop Rotation cannot find artifacts**: Toph makes artifacts lands only on the battlefield.
    Seismic Sense still finds artifact creatures (Gearhulk, Haywire Mite) as creatures.
11. **Under-used engine**: Chromatic Lantern, Wrenn and Realmbreaker and Great Divide Guide grant "{T}: any color" to
    lands, so with Toph every artifact land taps for mana, including Zuran Orb and an unkicked Everflowing Chalice
    (cast for {0} = a free rock and a free landfall). Do not tap Haystack or Liquimetal Coating for mana when their own
    {T} ability may be needed.
12. **Ragost untaps on opponents' end steps too** ("each end step"): an instant-speed life gain (Zuran Orb sacrificing a
    land, a Food) in an opponent's turn lets Ragost fire once per turn around the table.
13. **Hardlight Containment placement**: never on Zuran Orb, Nutrient Block, an earthbent artifact or a Ragost target, and
    never on a permanent Liquimetal Coating made an artifact (the Aura is put into the graveyard at end of turn and the
    creature returns).
14. **Annie Joins Up + Tannuk**: the first landfall of the turn already draws (the ability resolves twice, the second
    resolution draws).

## Next-iteration candidates (jobs, not purchases)

| Weak card | Job the replacement must do | Extra synergy it should add |
|---|---|---|
| Boros Locket | A 0-2 mana artifact (more landfall per mana with Toph) that fixes or replaces itself | ETB/death value (draw, scry, ping) so Ragost and Zuran Orb sacrifices are card-neutral |
| Haru, Hidden Talent | A 2-mana creature useful with no partner: landfall or artifact-enters payoff, or a mana creature | Ideally also legendary (Annie, Arbaaz) or an artifact (Toph landfall) |
| Liquimetal Coating | Keep only while line D is wanted; otherwise an artifact that is good alone and still a combo piece with Bumi or Toph | Instant-speed or repeatable value; tutorable by Reckless Handling |
| Earth Kingdom General | A second looper only if it costs 3 or less, or a 4-drop that is strong without Ashaya | Counters/lifegain for Terrasymbiosis and Ragost |
| Soul-Guide Lantern | A cheap artifact with card flow; graveyard hate only if the playgroup reanimates | Ragost/Zuran fodder that draws |
| Rampant Growth or Shared Roots (one of them) | Instant-speed protection for Toph (vs exile, edict, wraths) or a draw engine | The list has 35 lands + 20 artifact lands + ~15 ramp cards; flood is likelier than screw |
| Hardened Scales (watch) | A 1-2 mana card that turns earthbend counters into cards or damage | Terrasymbiosis-like redundancy |

Structural gaps:
- **Protection for the commander** is thin against exile and sacrifice: Collective Resistance (targeted only), Redirect
  Lightning (single-target only), Haystack (needs {2} open). No blanket protection (Heroic Intervention-type effect) and no
  answer to an edict.
- **Mana density is high**: 35 lands, 20 artifact lands, about 15 more ramp pieces. Card flow rests on Tireless Tracker,
  Terrasymbiosis, Tannuk and Valakut Exploration; two of the low-impact ramp spells could become draw or protection.
- **Artifact wipes** remove a large part of the mana base at once; nothing in the list protects artifacts.
- **Win without combo** is healthy (Sabotender, Tannuk, Arbaaz Mir, Valakut, Ragost, Bombardment all hit every
  opponent), so new cards should feed that plan rather than add more exact combo pieces.
- **Curve** is fine (MV 0:2, 1:12, 2:25, 3:18, 4:4, 5:3 for the 64 nonland cards); {G}{G}{W}{W} on Gearhulk is the only
  awkward cost.

## Rules checks

Online rulings: the Scryfall API returned HTTP 403 to WebFetch on 2026-10-26, so no Gatherer ruling was fetched. Status
per point:

| Point | Used in | How verified |
|---|---|---|
| Nantuko's token copy of an earthbent land is a plain land (earthbend's type and P/T change is not copiable) and enters untapped | Nantuko, Forest, win section | Spellbook variants 3470-5702-6871 and 3875-5702-6871 (infinite landfall, land tokens); CR 707.2 (copiable values) from knowledge |
| Earthbend returns The Stasis Coffin when exiled as a cost | Coffin, protect section | Spellbook variant 4155-6871 ("protection from everything during opponents' turns, {2} each turn") |
| Liquimetal Coating makes Bumi an artifact, so a land with Toph (layer-4 dependency) | Bumi, Coating | Spellbook variant 662-6871-7033; CR 613.8 from knowledge |
| Earthbend on a creature that is a land (Ashaya, Gearhulk) sets base P/T 0/0 over its own P/T | Ashaya, Gearhulk, Toph | CR 613.4 (layer 7b after 7a) from knowledge; no ruling fetched |
| Mana abilities granted by Lantern/Wrenn/Guide work on artifact lands the turn they enter (noncreature, no summoning sickness) | Lantern, Chalice, Zuran Orb | CR 302.6 from knowledge; Toph's reminder text says the artifacts do not gain {T} mana abilities on their own |
| Chord of Calling puts Nantuko onto the battlefield unattached | Chord, Nantuko | Bestow rules (CR 702.103) from knowledge |
| Hexproof in response makes targeted exile fizzle | Collective Resistance | CR 608.2b from knowledge |
| An Aura on a permanent that stops being an artifact goes to the graveyard | Hardlight Containment | CR 303.4d / 704.5m from knowledge |
| Annie doubles Tannuk (second resolution draws) and Bumi (two untaps, two extra combats) | Annie, Tannuk | Oracle text; CR 603.2 from knowledge; Bumi double-combat unverified by ruling |
| Ragost makes Treasure and Clue tokens Foods; untaps on any end step | Ragost, Provisioner, Tracker | Oracle text ("Artifacts you control", "each end step") |
| Tokens are never lands under Toph | Toph, Provisioner | Oracle text ("Nontoken artifacts") |
| Cards exiled by Valakut on an opponent's turn stay until your end step | Valakut, STE, Cycle | Oracle text |
| Reckless Handling can discard the card it found | Reckless Handling | Oracle text (search to hand, then discard at random) |
| Protection from everything stops you targeting yourself (Inscription's life mode) | Inscription | CR 702.16 from knowledge |
| Commander dies while earthbent (Ashaya out): decline the command zone and let earthbend return it tapped, no tax | not used in the table | **unverified** (CR 903.9a timing with the leaves-the-battlefield trigger); left out of the playbook |
| An earthbent artifact after Toph leaves (still a 0/0 creature?) | not used | **unverified**; left out |
