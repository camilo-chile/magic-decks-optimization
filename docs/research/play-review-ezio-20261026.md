<!-- Written 2026-10-26 by an Opus 5.5 (high) review agent for the owner. Paths such as in/list-<deck>.txt and in/cards-facts.json refer to the review workspace: the lists are the final ones in decks/measured/, the card facts come from scripts/dashboard_cards.py. -->

# Ezio Auditore da Firenze: synergy review (2026-10-26)

Deck: `in/list-ezio.txt` (100 cards, Salt round 5 step 40, 7.7). Card text: `in/cards-facts.json`. Rulings: Scryfall API
(`/cards/<id>/rulings`, official Gatherer rulings), read 2026-10-26, saved in `opus/rulings/`. Power/toughness: local Scryfall
bulk `data/cache/oracle-cards-20261011210156.jsonl.gz`. Combos: `in/guide.json` (Spellbook verified) or marked "derived, not
Spellbook". Odds are rough hypergeometric estimates (20 cards seen from 99, about turn 8 to 9 in a 4-player game).

Key facts used throughout:
- 24 creatures (commander included), 17 Assassins. The 7 non-Assassins: Magister Sphinx, Deadeye Navigator, Dualcaster Mage,
  Venser, Haytham Kenway, Loyal Inventor, Deathcap Cultivator.
- Freerunning {B}{B} needs combat damage to a player this turn by an Assassin or a commander; it then lasts the rest of the turn
  (ruling on Ezio and Restart Sequence). So almost every Assassin should be cast in the second main phase.
- Ezio's kill checks "10 or less" when its trigger resolves, after all combat damage (Ezio ruling). A player at 13 dies to Ezio
  alone (3 power), at 15 with Arno Dorian.

## Owner doubts

### 1. Winter Soldier, Icy Assassin: "a card for an equipment deck"
**Partly right.** Oracle: "{W}{B}, 2/2, vigilance, menace; +2/+0 for each Equipment attached; {3}{W}{B}: return this card from
your graveyard to the battlefield with a finality counter, then you may attach an Equipment you control." The deck has only 2
Equipment (Swiftfoot Boots, Assassin Gauntlet), so the equipment bonus is a minor upside, not a plan. Its real job is a 2-mana
Assassin with menace that connects on turn 3 to switch on freerunning, keeps blocking thanks to vigilance (useful when you hold
the monarch or the initiative), and comes back by itself from the graveyard after a wrath or a discard (Faithless Looting,
Bitter Triumph, Evie Frye), moving an Equipment onto itself for free.
**Consequence:** keep for now, verdict "watch". It is a fair 2-drop with no special synergy. In the next iteration a 2-mana
Assassin that also draws, protects or evades better would do the same job and more.

### 2. Deadeye Navigator: "5 mana, then 4 per turn, it only protects once"
**Wrong on the numbers and on the pairing.** Oracle: mana cost {4}{U}{U} (6 mana, not 5). While paired, each of the two creatures
has "{1}{U}: Exile this creature, then return it to the battlefield under your control." You blink only the creature you want
({1}{U}), not both. Official ruling (2017-03-14): "the pair will immediately be broken, and then the card will be returned to the
battlefield. Deadeye Navigator's soulbond ability triggers when that card enters the battlefield and the pair can then be
reunited." So the pair re-forms at once and the protection repeats for {1}{U} each time. With Ezio, when he is exiled you
choose to leave him in exile (instead of the command zone) and he comes back. If you blink him during an opponent's turn he can
attack on your turn; in your own turn he comes back summoning sick.
Limits that are real: it does not dodge wraths (the creature comes back before the wrath resolves); 6 mana is slow (with Roshan
it is an Assassin and costs {B}{B} after a hit); it protects only its partner.
**Consequence:** keep. Its best partners are not Ezio but Etrata, the Silencer (blink her in response to her trigger and she
is not shuffled away, ruling on Etrata), Magister Sphinx (each {1}{U} sets another player to 10), Adéwalé and Loyal Inventor
(a repeatable tutor), Nekrataal (a repeatable kill). To switch partners, blink Deadeye itself.

### 3. Roshan, Hidden Magister: "80-90 % of my creatures are already Assassins"
**Partly wrong.** 17 of 24 creatures (71 %) are Assassins; the 7 that are not include the two most expensive cards of the deck,
Magister Sphinx (7) and Deadeye Navigator (6). Oracle: "Other creatures you control are Assassins... The same is true for creature
spells you control and creature cards you own that aren't on the battlefield. Face-down creatures you control have menace.
Whenever a permanent you control is turned face up, you draw a card and you lose 1 life." What it really changes:
- Freerunning {B}{B} (from Ezio) for the 7 non-Assassins: Magister Sphinx goes from {4}{W}{U}{B} to {B}{B} after a hit; Deadeye
  from 6 to {B}{B}; Dualcaster, Venser, Haytham, Loyal Inventor too. Brotherhood Headquarters can pay any color for all of them.
- Graveyard and library cards become Assassins: The Revelations of Ezio chapter III and Jacob Frye can then use Magister Sphinx
  (otherwise they cannot); Adéwalé's reveal can take any creature, Sphinx included (hit rate from about 70 % to about 84 %);
  Desmond Miles counts every creature card in the graveyard.
- Lydia Frye, Ezio, Blade of Vengeance and Etrata, Deadly Fugitive trigger on any creature, Arno's +2/+0 reaches all creatures.
- Face-down creatures (Etrata, Deadly Fugitive's cloaks, a disguised Arno) get menace and draw a card when turned up.
He is right that the static text is redundant for most creatures; Roshan's value concentrates on the Sphinx line.
**Consequence:** keep. Play it when the Sphinx line or the graveyard plan is live; as a plain 4-mana 4/4 it is only average.

### 4. Adéwalé, Breaker of Chains: "it only works when it enters, I have no Vehicles"
**Right about the second ability, wrong about the card.** The Vehicle text (return from graveyard when a Vehicle hits) does
nothing here. The enter trigger is the job: reveal 6, take an Assassin (about 70 % hit with about 15 other Assassins in the
library; about 84 % with Roshan out, when any creature counts). Cast for {B}{B} after a hit, it is a 2-mana 2-for-1. It is a 4/1,
so it dies to everything, and it chains well with Deadeye Navigator, Strionic Resonator, Lithoform Engine, Ember Island
Production, Kaya's 0, Restart Sequence and Revelations III.
**Consequence:** keep. Never pay full price ({1}{U}{B}) before combat unless the hand is empty of plays.

### 5. Nekrataal: "expensive for just a removal; spending 1 of my 2 reanimations on it?"
**Mostly right.** Oracle: {2}{B}{B}, 2/1 first strike, enters: destroy target nonartifact, nonblack creature. In a 3-4 player pod
many key creatures are black or artifacts. The deck already has 12 removal spells, most cheaper and at instant speed (Fatal Push,
Infernal Grasp, Bitter Triumph, Terminate, Fateful Absence, Murder, Mortify, Assassin's Trophy, Stroke of Midnight, Utter End,
Chaos Warp, Kolaghan's Command) plus Royal Assassin, Haytham, Revelations chapter I and Starfall. Recursion is a bit wider than "2"
(Restart Sequence and Revelations III return to the battlefield; Jacob Frye can cast a copy from the graveyard; Kolaghan's Command
returns it to hand; Starfall's gift), but it is still wrong to spend Entomb or Restart Sequence on Nekrataal when Magister Sphinx,
Ezio, Blade of Vengeance or Etrata are options. Its only edge: as an Assassin it costs {B}{B} after a hit, and Deadeye, Strionic
or Ember Island repeat the kill.
**Consequence:** replace-candidate. The job a replacement must do: cheap instant-speed removal that hits any creature (or any
permanent), or a creature whose entry removes anything and is itself an Assassin.

### 6. Dualcaster Mage + Ember Island Production: "do they do anything apart?"
**Yes, but less than the combo suggests, and the combo does not win here by itself.** The Spellbook line (guide.json, combo 5)
makes infinite Dualcaster tokens, 4/4, no haste. This deck has no "whenever a creature enters" payoff that wins. Derived, not
Spellbook: with Roshan and Desmond Miles already on the battlefield, every token is an Assassin and Desmond gets +1/+0 per token,
so Desmond (menace) attacks for any amount that turn; otherwise you attack with the army next turn (weak to a wrath).
Dualcaster Mage alone (flash, "copy target instant or sorcery spell", any controller, ruling 2016-06-08): copy Restart Sequence
(two reanimations; after a hit both cost {1}{B} and {B}{B} with Roshan), any removal, Mystical Teachings, Kolaghan's Command
(same two modes), Entomb; or copy an opponent's spell: their removal aimed at their own creature, their draw, their tutor (the
copy is yours, so "you" means you). It cannot copy Magister Sphinx (a creature spell), only instants and sorceries.
Ember Island Production alone ({3}{U}{U} sorcery): a non-legendary 4/4 token copy whose enter abilities trigger (ruling): Magister
Sphinx (another player to 10), Ezio himself (a second Ezio with the kill trigger, attacks next turn), Ezio, Blade of Vengeance
(double draw), Etrata, the Silencer, Adéwalé, Loyal Inventor, Haytham. Note: Dualcaster can copy Ember Island Production without
the loop, giving two tokens.
**Consequence:** Dualcaster keep (flexible instant-speed card). Ember Island watch: a 5-mana sorcery that needs a good creature
already on the battlefield. For Azula the answer must be checked by that deck's agent.

### 7. Etrata, the Silencer: "dead weight without the two exact cards in a 3-4 player game"
**Partly right about the autowin, wrong that she is dead.** Oracle: {2}{U}{B}, 3/5, can't be blocked; on combat damage to a player:
exile target creature that player controls with a hit counter; that player loses if they own 3 or more exiled cards with hit
counters; then Etrata's owner shuffles Etrata into their library. Without the combo:
1. Removal on an unblockable body: every hit exiles that player's best nontoken creature (beats indestructible and recursion; a
   commander goes back to the command zone with more tax) and also triggers freerunning, Coastal Piracy, Ezio, Blade of
   Vengeance and Jacob Frye.
2. She is not always shuffled away. Ruling (2018-10-05): "If the player controls no creatures, Etrata's ability doesn't resolve.
   Etrata remains on the battlefield." Attack the opponent with no creatures and she stays as a 3/5 unblockable attacker.
3. Ruling (2018-10-05): "If Etrata leaves the battlefield while its triggered ability is on the stack, it remains in its new
   zone." Respond to her trigger with Deadeye Navigator ({1}{U}, she returns to the battlefield) or Venser (she returns to your
   hand): the exile still happens and she is not shuffled.
4. Hit counters accumulate. Ravenloft Adventurer: "If a creature an opponent controls would die, instead exile it and put a hit
   counter on it", so every kill (removal, deathtouch blocks, Starfall Invocation) adds counters for Etrata. Once a player owns 2
   such cards, a single Etrata hit wins against that player. With one copier (Strionic Resonator, Lithoform Engine or Return the
   Favor) two hits are enough.
5. Tokens do not count (ruling), and an opponent with no nontoken creatures cannot be killed this way.
**Consequence:** keep. Play her as removal plus evasion, aim her at the right player, and use the copiers when they happen to
be there.

## Verdict table

Stand-alone: value with no specific partner. Breadth: rough count of other cards in this list it works with.

| Card | Stand-alone | Needs exact partners? | Breadth | Verdict | Reason |
|---|---|---|---|---|---|
| Ezio Auditore da Firenze | high | kill needs a player at 10 or less + {W}{U}{B}{R}{G} | very high | core | 2-mana menace freerunning enabler; kill counts combat damage first |
| Abstergo Entertainment | medium | no | medium (Entomb, Sphinx, Lithoform, Strionic) | keep | utility land, but exiling all graveyards fights Restart, Revelations, Jacob |
| Adéwalé, Breaker of Chains | medium | no | high (Roshan, Deadeye, Strionic, Lithoform, Ember Island, Kaya) | keep | 2-for-1 Assassin dig; Vehicle text dead; 4/1 body |
| Arcane Signet | medium | no | broad | keep | 2-mana any-color rock |
| Arno Dorian | high | no | high (all Assassins, Roshan) | core | anthem; disguise + Roshan draws |
| Assassin Gauntlet | high | no | high (Royal Assassin, Revelations I, Strionic, Winter Soldier) | core | taps one opponent's whole board before combat |
| Assassin's Trophy | high | no | n/a | keep | cheap instant answer to any permanent |
| Bitter Triumph | high | no | medium (Sphinx, Winter Soldier discards) | keep | 2-mana instant kill |
| Brainstorm | medium | wants shuffles | medium | watch | few shuffle effects; fine with surveil |
| Brotherhood Headquarters | medium | no | medium (Roshan, Restart) | keep | cannot pay Ezio's {W}{U}{B}{R}{G} |
| Chaos Warp | medium | no | n/a | keep | catch-all answer |
| Chromatic Lantern | high | no | high (kill payment, colorless lands) | core | fixes the five-color kill |
| Clifftop Retreat | medium | no | low | keep | often enters tapped (few Mountains/Plains) |
| Coastal Piracy | high | no | high (every attacker) | core | multiplayer draw engine |
| Command Tower | high | no | broad | core | any color |
| Concealed Courtyard | medium | no | low | keep | untapped early only |
| Deadeye Navigator | medium | an ETB partner | high (~10 ETB creatures + Etrata) | keep | owner's cost wrong; repeatable blink; 6 mana |
| Deathcap Cultivator | medium | no | low | keep | turn-2 dork, green source |
| Desmond Miles | high | no | high (Assassins, Roshan, surveil) | core | best 2-drop; loop payoff with Roshan |
| Dimir Locket | low | no | low | replace-candidate | slow rock, weak late draw |
| Dragonskull Summit | high | no | low | keep | untapped with Swamps |
| Drowned Catacomb | high | no | low | keep | untapped with Swamps |
| Dualcaster Mage | medium | combo needs Ember Island + payoff | medium (Restart, removal, Teachings, K-Command) | keep | flexible flash copy |
| Ember Island Production | medium-low | a good creature on board | medium (Sphinx, Ezio, Blade, Etrata) | watch | 5-mana sorcery value |
| Entomb | medium | a recursion piece | medium (Restart, K-Command, Abstergo, Roshan+Revelations/Jacob) | keep | only Sphinx is the right target |
| Etrata, Deadly Fugitive | medium | no | high (any Assassin hit, Roshan) | keep | card/board advantage per hit |
| Etrata, the Silencer | medium | autowin: 2 of 3 copiers + 3 creatures | medium-high (Ravenloft, Deadeye, Venser, copiers) | keep | removal + evasion; see doubt 7 |
| Everflowing Chalice | low | no | low | replace-candidate | colorless 2-mana rock in a {B}{B} five-color deck |
| Evie Frye | medium | no | medium (Jacob, Sphinx discard) | keep | tutors Jacob, loot, unblockable |
| Exotic Orchard | medium | no | low | keep | fixing in 4-player pods |
| Ezio, Blade of Vengeance | high | no | high | core | main draw engine |
| Faithless Looting | low-medium | Sphinx + Restart | low | watch | card disadvantage; only for the graveyard line |
| Fatal Push | low-medium | revolt (Bauble, Locket, Deadeye, Kaya, Etrata) | low | watch | MV 2 or less without revolt |
| Fateful Absence | high | no | n/a | keep | 2-mana instant kill |
| Fortified Village | low | reveal Forest/Plains/Prairie Stream | low | watch | usually tapped |
| Frostboil Snarl | medium | no | low | keep | 5 cards reveal it |
| Game Trail | low | reveal Mountain/Forest/Smoldering Marsh | low | watch | usually tapped |
| Haytham Kenway | high | no | medium (Strionic, Lithoform) | keep | one exile per opponent; not an Assassin; anti-synergy with blink/bounce |
| Hinterland Harbor | medium | no | low | keep | often tapped early |
| Infernal Grasp | high | no | n/a | core | best removal |
| Intruder Alarm | low (anti-synergy) | none works here | low | replace-candidate | no creature mana for a combo; stops your attackers untapping |
| Isolated Chapel | high | no | low | keep | untapped with Swamps |
| Jacob Frye | high | no | high (Restart, Assassins in yard, Roshan + Sphinx) | core | graveyard engine on every hit |
| Kaya, Ghost Assassin | medium | no | medium | keep | discard/draw, drain, temporary removal |
| Kolaghan's Command | high | no | medium | keep | flexible instant, recursion to hand |
| Lithoform Engine | medium-high | no | high | keep | copies triggers, spells, permanent spells |
| Loyal Inventor | high | an Assassin in play (easy) | high | core | tutors Sphinx or a copier |
| Lydia Frye | medium | no | medium | keep | evasion vs big blockers, surveil |
| Magister Sphinx | medium | Ezio (always available) | very high | core | the main win; many copy and recursion routes |
| Mana Leak | low-medium | no | low | watch | soft counter, weak late |
| Mishra's Bauble | low-medium | no | low (Fatal Push, Deathcap) | watch | free cantrip |
| Mortify | high | no | n/a | keep | creature or enchantment |
| Murder | high | no | n/a | keep | plain kill |
| Mystical Teachings | medium | no | medium (Return the Favor, Dualcaster, Venser, removal) | keep | slow but flexible tutor |
| Nekrataal | low-medium | no | medium (Deadeye, Strionic, Ember Island) | replace-candidate | conditional, sorcery-speed, redundant removal |
| Prairie Stream | medium | no | low | keep | typed dual |
| Queen Marchesa | high | no | medium (Thorn) | keep | haste, monarch, token recovery |
| Rakdos Signet | medium | no | low | keep | 2-mana rock |
| Rampant Growth | medium | no | low | keep | ramp + fixing |
| Ravenloft Adventurer | medium | no | medium (Etrata, removal, Starfall) | keep | makes Etrata a real multiplayer wincon |
| Reckless Handling | medium | no | medium | keep | artifact tutor; random discard |
| Restart Sequence | high | no | high | core | best recursion |
| Return the Favor | medium | no | medium (Sphinx, Etrata, removal) | keep | copy or redirect |
| Roshan, Hidden Magister | medium | no | high (Sphinx, Revelations, Jacob, Adéwalé, Deadeye, cloaks) | keep | key to the cheap Sphinx line |
| Royal Assassin | medium | no | medium (Gauntlet, Revelations) | keep | kills tapped creatures each turn |
| Rumble Arena | low-medium | no | low | watch | colorless, filter costs a land |
| Secret Tunnel | medium | no | medium | keep | double unblockable for the kill turn |
| Seismic Sense | medium | no | medium | keep | late creature tutor |
| Smoldering Marsh | medium | no | low | keep | typed dual |
| Sol Ring | high | no | broad | core | fast mana |
| Starfall Invocation | medium | no | medium (Ravenloft, gift on Sphinx) | keep | own wrath in a creature deck: situational |
| Strionic Resonator | high | no | very high | core | copies ~20 triggers in the list |
| Stroke of Midnight | medium | no | n/a | keep | any nonland permanent |
| Sulfur Falls | medium | no | low | keep | 5 cards enable it |
| Sunken Hollow | medium | no | low | keep | typed dual |
| Survivors' Encampment | medium | no | medium | keep | any color by tapping a creature |
| Swiftfoot Boots | high | no | medium | core | protects Ezio |
| Terminate | high | no | n/a | keep | cheap kill |
| The Revelations of Ezio | high | Roshan for Sphinx | high | keep | kill, pump, reanimate |
| Theater of Horrors | high | no | high | core | card advantage in an attacking deck |
| Thorn of the Black Rose | medium | no | medium | keep | monarch is risky in 4-player pods |
| Tome of Legends | low-medium | Ezio attacking | low | watch | slow, depends on Ezio surviving |
| Utter End | high | no | n/a | keep | exile any nonland permanent |
| Venser, Shaper Savant | high | no | high | keep | protection, tempo, saves Etrata |
| White Lotus Hideout | low-medium | no | low | watch | colorless, filter costs a land |
| Winter Soldier, Icy Assassin | medium | no | low-medium | watch | fair 2-drop; equipment text minor |
| Woodland Cemetery | high | no | low | keep | untapped with Swamps |

Weakest in this deck: Intruder Alarm, Nekrataal, Everflowing Chalice, Dimir Locket, then Fatal Push, Mana Leak, Faithless
Looting, Tome of Legends, Ember Island Production, Winter Soldier, and the lands Fortified Village, Game Trail, Rumble Arena,
White Lotus Hideout.

## Orphan risk

| Mini-combo | Pieces | Odds together (20 cards seen) | Dead alone? |
|---|---|---|---|
| Ezio + Magister Sphinx | 1 (Ezio is always available) + {W}{U}{B}{R}{G} + a connection | Sphinx or one of its 4 tutors (Loyal Inventor, Reckless Handling, Entomb, Seismic Sense): about 68 % | No. Sphinx alone is a 7-mana 5/5 flier; every other route (Roshan, Restart, Revelations, Jacob, copies) widens it |
| Etrata + 2 of {Lithoform, Strionic, Return the Favor} | 3 + an opponent with 3 nontoken, noncommander creatures | about 2 % naturally; maybe 5-10 % with tutors (Adéwalé, Loyal Inventor, Reckless Handling, Mystical Teachings) | No: each copier has 10+ other uses; Etrata is removal + evasion (doubt 7) |
| Dualcaster Mage + Ember Island Production | 2, plus Roshan + Desmond for an immediate win | about 4 % for the pair; under 1 % with the payoff | Partly: Dualcaster flexible; Ember Island needs a good creature |
| Intruder Alarm + Venser or Deadeye | needs repeatable creature mana the deck does not have | no working line in this list | Yes: Intruder Alarm is dead or harmful |
| Royal Assassin / Revelations I + tapped creatures | Gauntlet or opponents' last attackers | high | No |

Conclusion: the deck has one reliable line (Sphinx + Ezio) with wide support, one line that is now much more flexible than the
owner thought (Etrata with Ravenloft and the blink/bounce tricks), one weak two-card loop with no payoff, and one dead card
(Intruder Alarm).

## Misplay corrections

1. Casting Assassins before combat at full price. After any Assassin or Ezio connects, Assassin spells cost {B}{B} for the rest
   of the turn. Before combat cast only Assassin Gauntlet, Queen Marchesa (haste) or what changes combat.
2. Entomb on Nekrataal, or Entomb with no recursion in hand. Entomb is for Magister Sphinx, used when Restart Sequence (or
   Roshan + Revelations/Jacob, or Kolaghan's Command/Abstergo to hand) is ready.
3. Revelations III or Jacob Frye on Magister Sphinx without Roshan: not legal (Sphinx is not an Assassin). Restart Sequence works
   without Roshan.
4. Paying Ezio's {W}{U}{B}{R}{G} with Brotherhood Headquarters: its colored mana is only for Assassin spells, freerunning spells
   and activating abilities of Assassin sources; a cost paid while a trigger resolves is none of these.
5. Holding Etrata, the Silencer for the exact combo. Use her as removal; attack an opponent with no creatures to keep her;
   blink (Deadeye) or bounce (Venser) her in response to her trigger.
6. Sparing opposing creatures "for Etrata" while Ravenloft Adventurer is out: with it, killing them adds hit counters.
7. Deadeye Navigator: blink only the creature that needs it; the pair re-forms. Leave Ezio in exile, not the command zone.
8. Magister Sphinx on a player below 10 raises them to 10. Aim it at someone above 10 whom Ezio can hit; aim it at yourself when
   you are low.
9. Ezio's kill: count the combat damage of the same combat. A player at 13 is already in range of Ezio alone.
10. Kaya's 0 on Ezio: he returns at your upkeep summoning sick and loses that turn's attack. Use it on an opposing blocker, on
    Kaya herself, or on Adéwalé to repeat his entry.
11. Haytham Kenway: blinking or bouncing him returns every creature he exiled.
12. Royal Assassin: use it on your turn against creatures that attacked during the last round (they stay tapped until their
    controller's untap step), right after Assassin Gauntlet, or after attackers are declared on an opponent's turn.
13. Reckless Handling: the random discard can hit the card you just fetched; cast it with a near-empty hand.
14. Monarch (Thorn, Queen) and initiative (Ravenloft): drop them when you can defend them, or you feed the table.
15. Starfall Invocation: promise the gift almost always; returning Magister Sphinx re-triggers it.
16. Mana Leak: strongest early; late it is a 2-mana tax.
17. Jacob Frye + Roshan + Ezio (derived, not Spellbook): when Ezio and Jacob both trigger on combat damage, put Ezio's trigger
    on the stack first and Jacob's on top; Jacob casts a copy of Magister Sphinx from the graveyard for {B}{B} (freerunning),
    the token sets that player to 10, then Ezio's trigger resolves and checks the life: a same-turn kill with {B}{B} + {W}{U}{B}{R}{G}.

## Next-iteration candidates (jobs, not purchases)

| Weak card | Job the replacement must do | Extra synergy wanted |
|---|---|---|
| Intruder Alarm | protection or card advantage at 3 mana: e.g. team protection against a wrath, or evasion for the whole team on the kill turn | works with many Assassins attacking |
| Nekrataal | 1-2 mana instant removal for any creature, or an Assassin creature whose entry removes any permanent | repeatable by Deadeye/Strionic if it is a creature |
| Everflowing Chalice | 2-mana rock that makes black or any color | helps {B}{B} and {W}{U}{B}{R}{G} |
| Dimir Locket | same as above, or a cheap repeatable draw engine | triggers on Assassin hits |
| Fatal Push | unconditional cheap removal or a protective instant for Ezio | |
| Mana Leak | hard protection on the kill turn (counter or protective instant) | |
| Faithless Looting / Tome of Legends | a tutor or draw engine (Salt's ceiling note in round 5: "no fast mana, tutors or draw engine") | finds Sphinx or draws per hit |
| Ember Island Production | a cheaper way to repeat an enter trigger (Sphinx, Adéwalé, Loyal Inventor) | |
| Winter Soldier | a 2-mana evasive Assassin that also draws, loots or protects | |
| Fortified Village, Game Trail, Rumble Arena, White Lotus Hideout | lands that enter untapped with two colors or any color | fewer colorless sources (6 of 35 lands make colorless by default) |

Structural gaps:
- Multiplayer finish: every kill line removes one player at a time. A card that hurts all opponents at once (group drain, extra
  combat, team evasion) or another repeatable "life becomes 10" route would close games after the first kill.
- Wrath insurance: only Swiftfoot Boots (one creature) and recursion. A team-protection effect would help a deck that commits
  creatures every turn.
- Interaction vs card flow: 12 removal spells + 6 other removal pieces (Royal Assassin, Haytham, Nekrataal, Revelations I, Kaya, Etrata) + a wrath is heavy one-for-one in a 4-player pod; trade 2-3 of
  the weakest for card advantage or tutors.
- Evasion on the kill turn: Secret Tunnel, Assassin Gauntlet, Evie Frye, menace. One more reliable "can't be blocked" effect
  for Ezio would raise the Sphinx line's conversion.
- Mana: 8 Swamps carry the {B}{B}; the single Forest, Plains and Mountain make the reveal lands (Fortified Village, Game Trail)
  enter tapped most of the time.

## Rules checks

| Statement | How verified |
|---|---|
| Deadeye: blinked creature re-pairs on return | Ruling 2017-03-14 (Scryfall rulings), verified |
| Commander exiled by Deadeye may stay in exile and return | Commander rule (owner may move it to the command zone; optional), well known; not ruling-checked |
| A creature returned during an opponent's turn can attack on your next turn; returned at your upkeep it cannot | Summoning-sickness rule (control since the start of your turn), well known |
| Etrata, the Silencer stays if the player has no creatures | Ruling 2018-10-05, verified |
| Etrata not shuffled if she leaves while her trigger is on the stack | Ruling 2018-10-05, verified |
| Tokens exiled by Etrata do not count | Ruling 2018-10-05, verified |
| Exiled commander may go to the command zone, so no hit card stays in exile | Commander rule, well known; the Etrata ruling covers the owner's own commander only |
| Ravenloft replacement applies when it dies in the same wrath | By analogy to the Kalitas, Traitor of Ghet ruling ("If Kalitas dies at the same time as creatures your opponents control, those creature cards will be exiled"), verified analog; no Ravenloft-specific ruling |
| Taking the initiative again ventures again | Ravenloft ruling 2022-06-10, verified |
| Ezio's check at resolution; reflexive kill | Ezio ruling 2024-07-05, verified |
| Freerunning available the rest of the turn | Ezio and Restart Sequence rulings, verified |
| Brotherhood Headquarters cannot pay Ezio's {W}{U}{B}{R}{G} | Card text (spells and activated abilities only); ruling covers only freerunning spells; high confidence, not ruling-checked |
| Roshan affects library, hand and graveyard creature cards | Oracle text ("creature cards you own that aren't on the battlefield"); no ruling |
| Jacob Frye: cast the copy during resolution | Jacob ruling 2024-07-05, verified |
| Jacob Frye's copy may be cast for freerunning {B}{B} | Derived: the ruling says you pay the spell's costs; alternative costs are allowed when not cast "without paying". Unverified by a ruling |
| Ordering Jacob's trigger above Ezio's | Basic trigger-ordering rule, well known |
| Etrata, Deadly Fugitive can turn up noncreature permanents; instants/sorceries are exiled and cast | Etrata, Deadly Fugitive ruling 2024-02-02 (only instants and sorceries cannot be turned up), verified by inference |
| Ember Island token copies trigger enter abilities, not legendary | Ember Island ruling 2025-10-02 + Oracle, verified |
| Dualcaster copies any instant/sorcery, any controller; "you" = copy's controller | Dualcaster rulings 2016-06-08, verified |
| Lithoform/Strionic copy of Haytham's entry exiles more creatures, all linked | Lithoform ruling 2020-09-25 (Fiend Hunter example), verified |
| Return the Favor redirect must change the target if possible | Return the Favor ruling 2024-04-12, verified |
| Survivors' Encampment can tap a summoning-sick creature | Ruling 2017-07-14, verified |
| Venser bouncing Ezio to hand; cast from hand pays no tax | Commander rules (tax counts casts from the command zone; owner may choose hand), well known |
| Dualcaster + Desmond + Roshan payoff for the loop | Derived, not Spellbook: Roshan makes the tokens Assassins; Desmond's +1/+0 per other Assassin you control |

## Validation of the playbook file

`out/ezio.playbook.json`: parses; 92 rows, names and order equal to `in/playbook-ezio.json`; basic-land qty unchanged
(8 Swamp, 2 Island, 1 Forest, 1 Mountain, 1 Plains); total 100 cards; no empty `play.es`; 10 sections with the same id/order;
no bare mana costs (regex check). Role changes: Queen Marchesa win to draw (monarch card draw), Winter Soldier win to engine.
