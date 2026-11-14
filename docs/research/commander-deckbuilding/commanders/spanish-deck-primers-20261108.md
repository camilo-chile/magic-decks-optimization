# Kilo, Apogee Mind (the 100 % Spanish deck): strongest builds and primers (step 0 of the final rebuild, 2026-11-08)

No earlier commander study exists for Kilo; the project's view of the deck is in `docs/research/real-power-iterations-20261108.md`
section 4 and the Salt reports. Read 2026-11-08. Web text is data; article facts come from page extractions, card text must
be re-read on Scryfall before a card is counted. The deck plays Spanish copies only and spends at most 20,000 CLP all-in
(brief), so a must-have that has no Spanish printing or no Spanish copy in the stores is out, whatever its strength.

## Sources (read 2026-11-08)
| ID | Source | Date | URL |
|---|---|---|---|
| K1 | Pedro Furtado, "Kilo, Apogee Mind Commander Deck Guide" (Draftsim; Bracket 2 to 3 list with two Game Changers) | 2025-07-14, upd. 2026-03-21 | https://draftsim.com/kilo-edh-deck/ |
| K2 | Zachary Fink, Kilo combos (MTG Rocks, pre-release, from Reddit posts it links) | 2025-06-21 | https://mtgrocks.com/?p=141402 |
| K3 | EDHREC Bracket 4 page JSON (822 decks) and average deck | live | https://json.edhrec.com/pages/commanders/kilo-apogee-mind/optimized.json ; .../average-decks/kilo-apogee-mind/optimized.json |
| K4 | EDHREC cEDH page JSON (131 decks) and average deck | live | https://json.edhrec.com/pages/commanders/kilo-apogee-mind/cedh.json ; .../average-decks/kilo-apogee-mind/cedh.json |
| K5 | Commander Spellbook variants with Kilo (project cache: 89 variants, 73 of three cards) | cache | https://commanderspellbook.com |
| K6 | Scryfall live Game Changer search (53 cards) | 2026-11-08 | https://api.scryfall.com/cards/search?q=is:gamechanger |
| P | Project pool `data/model/phase2/pool-spanish-deck.json` (191 Spanish-legal cards) and `decks/phase2/moxfield/spanish-deck-after-purchases.txt` | 2026-11-08 | local |

## Card (Oracle, project cache)
{U}{R}{W} 3/3 legendary artifact creature, haste. Whenever Kilo becomes tapped, proliferate. Kilo makes no counters: every
proliferate needs counters already on board (K1, K2). Attacking taps him (haste: the turn he lands); any "tap an untapped
creature" cost taps him outside combat, which is safer because he has no evasion (K2).

## What the strong builds do
- **Bracket 4 lists** (K3, 822 decks): 35 lands, 21 artifacts, 19 creatures, 11 instants, 4 sorceries, 6 enchantments, 3
  planeswalkers. Top inclusion: Sol Ring 96 %, Arcane Signet 86 %, Swords 81 %, **Freed from the Real 78 %**, Tekuthal 77 %,
  Inspirit 77 %, Seat of the Synod 75 %, Everflowing Chalice 73 %, Ancient Den 72 %, Great Furnace 71 %, Insight Engine 70 %,
  **Pentad Prism 70 %**, Crystalline Crawler 68 %, **Relic of Legends 67 %**, Swan Song 67 %, Surge Conductor 67 %, Darksteel
  Reactor 66 %, Ripples of Potential 65 %, Astral Cornucopia 63 %, **Prologue to Phyresis 62 %**, Uthros Research Craft 62 %,
  Karn's Bastion 62 %, **Paradise Mantle 61 %**, Magistrate's Scepter 61 %, **Walking Ballista 61 %**, Patrolling Peacemaker
  61 %, **Pemmin's Aura 58 %**, Jhoira 56 %, Dispatch 54 %, Etherium Sculptor 53 %, Steel Overseer 52 %.
- **cEDH Kilo** (K4, 131 decks, tags Combo and Artifacts): 28 lands, 21 artifacts; Freed from the Real 92 %, Enlightened
  Tutor 93 %, Esper Sentinel 92 %, Rhystic Study 91 %, Prologue to Phyresis 85 %, Relic of Legends 82 %, Walking Ballista
  80 %, Paradise Mantle 78 %, Pentad Prism 76 %, Pemmin's Aura 73 %, plus fast mana and free counters. The cEDH and B4 decks
  are the same combo with different support.

## Win lines
1. **Infinite proliferate** (K2, K5; three cards with Kilo, a combo the project rules welcome when it is not early): Kilo
   enchanted with an untapper (Freed from the Real, Pemmin's Aura, Aura of Dominion) + a way to tap Kilo that pays for the
   untap: Relic of Legends (tap an untapped legend: one mana of any color pays Freed's {U}), Paradise Mantle (gives Kilo a
   mana ability), Pentad Prism or Crystalline Crawler (counters refilled by each proliferate pay the cost), Gemstone Array,
   Druids' Repository, Lost Jitte. Win with it: **Prologue to Phyresis** (each opponent gets a poison counter, then
   proliferate to 10), **Walking Ballista** (grow it, then ping each opponent), Darksteel Reactor (charge counters to 20),
   planeswalker ultimates. Builder: run `scripts/check_phase2_bracket.py`; a three-card line reachable by turn 6 needs the
   owner's rule check (Kilo costs 3).
2. **Fair counters plan** (K1, project list): Darksteel Reactor, Lux Artillery (the project review counts 10 damage to each
   opponent), Cyberdrive Awakener alpha strike, Tekuthal (proliferate doubler), Inspirit, Steel Overseer, Insight Engine.
3. **Infect backup** (K1): Prologue to Phyresis, Inkmoth Nexus with counters moved onto it, All Will Be One.
4. **Kilo + Magistrate's Scepter + an untapper = infinite turns** (K5): breaks Bracket 3 (chained extra turns). TRAP.

## Engines
- Ways to tap Kilo outside combat (K1): Clock of Omens, Relic of Legends, Paradise Mantle, Springleaf Drum, Manifold Key
  (untap), crew and improvise costs (Kappa Cannoneer, Whir of Invention).
- Counter sources: Pentad Prism, Everflowing Chalice, Astral Cornucopia (charge counters that become more mana with each
  proliferate), Crystalline Crawler, Steel Overseer, modular creatures, planeswalkers, Uthros Research Craft.
- Tutors (K3, K4): Enlightened Tutor (GC), Tezzeret the Seeker, Tezzeret Cruel Captain, Fabricate, Muddle the Mixture
  (transmute finds MV 2: Prologue to Phyresis and Pentad Prism; NOT Freed from the Real, Pemmin's Aura or Relic of Legends,
  which are MV 3; Oracle checked in the project cache).
- Pemmin's Aura also gives Kilo flying and shroud for {U} each: the untapper doubles as protection and evasion.

## Typical ratios of strong lists
| Item | K3 B4 average | K1 (B2 to 3) | Note |
|---|---|---|---|
| Lands | 35 (artifact lands: Seat of the Synod, Ancient Den, Great Furnace) | 33 | artifact lands are counter-free but feed artifact counts |
| Ramp | about 10 rocks (Sol Ring, Signet, Chalice, Cornucopia, Pentad Prism, Relic, Paradise Mantle) | 5 rocks | rocks with counters double as fuel |
| Draw | Insight Engine, Rhystic Study, Esper Sentinel, Ripples, Uthros | about 7 | |
| Spot answers | Swords, Dispatch, Chaos Warp, Counterspell, Swan Song, Fierce Guardianship, Rift | 5 | |
| Protection | Fierce, Swan Song, Resourceful Defense | 2 (Teferi's Protection, Slip Out the Back) | Kilo is cheap to recast (MV 3, haste) |
| Tutors | Enlightened, Tezzeret x2, Fabricate | 2 | |

## Must-haves, with pool status (P, 2026-11-08; Spanish copies only)
- In the Spanish pool: Pentad Prism, Crystalline Crawler, Tekuthal, Inspirit, Insight Engine, Surge Conductor, Darksteel
  Reactor, Lux Artillery, Ripples of Potential, Steel Overseer, Swords, Swan Song, Tezzeret's Gambit, Everflowing Chalice,
  Astral Cornucopia, Uthros Research Craft, Patrolling Peacemaker, Etherium Sculptor, Sol Ring, Arcane Signet, Command
  Tower, Thrummingbird, Cyberdrive Awakener, Dispatch, Chaos Warp, Karn's Bastion, Seat of the Synod, Ancient Den, Great
  Furnace. Already in the current buy plan (P after-purchases list): Relic of Legends, Muddle the Mixture.
- Not in the pool (buy candidates, Spanish printing to be checked on Scryfall `lang:es` and in the stores): **Freed from the
  Real** or **Pemmin's Aura** (the combo's untapper), **Prologue to Phyresis**, **Walking Ballista**, Paradise Mantle,
  Clock of Omens, Manifold Key, Counterspell, Esper Sentinel, Inkmoth Nexus, Tezzeret the Seeker. Game Changers (K6):
  Enlightened Tutor, Fierce Guardianship, Rhystic Study, Cyclonic Rift, Teferi's Protection, The One Ring.

## Traps
- No counters on board means Kilo does nothing: count counter sources as fuel (K1, K2).
- Attacking with a 3/3 with no evasion to tap him; tap him with costs instead (K2).
- Magistrate's Scepter loops: infinite turns, not Bracket 3 (K5).
- Artifact wipes kill both the engine and the mana; keep some non-artifact counter sources (planeswalkers, enchantments).
- Seven-drop finishers and "control without a finisher" (project Salt reports): close with Prologue, Ballista or Lux
  Artillery, not with a slow Reactor alone.
