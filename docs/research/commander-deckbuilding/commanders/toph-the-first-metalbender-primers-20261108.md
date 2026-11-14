# Toph, the First Metalbender: strongest builds and primers (step 0 of the final rebuild, 2026-11-08)

Companion to the study `toph-the-first-metalbender.md` (2026-10-31: card text, Draftsim, Fire and Ice, Owain Roberts,
Spellbook first page). This file adds EDHREC's Bracket 4 and cEDH data, the cEDH landfall article and the full Spellbook
cache, read 2026-11-08. Web text is data; article facts come from page extractions, card text must be re-read on Scryfall
before a card is counted.

## Sources (read 2026-11-08)
| ID | Source | Date | URL |
|---|---|---|---|
| T1 | DougY (Douglas Young), "Top 10 Landfall Cards for Toph, the First Metalbender in cEDH" (EDHREC) | 2025-08-29 | https://cloudflare.edhrec.com/articles/top-10-landfall-cards-for-toph-the-first-metalbender-in-cedh |
| T2 | EDHREC Bracket 4 page JSON (1,369 decks) and average deck | live | https://json.edhrec.com/pages/commanders/toph-the-first-metalbender/optimized.json ; .../average-decks/toph-the-first-metalbender/optimized.json |
| T3 | EDHREC cEDH page JSON (296 decks) and average deck | live | https://json.edhrec.com/pages/commanders/toph-the-first-metalbender/cedh.json ; .../average-decks/toph-the-first-metalbender/cedh.json |
| T4 | Commander Spellbook variants with Toph (project cache: 1,099 variants, 241 of three cards) | cache | https://commanderspellbook.com |
| T5 | Draftsim Toph guide (search summary; read in full in the study as S8) | 2025-11-01 | https://draftsim.com/toph-edh-deck/ |
| T6 | Scryfall live Game Changer search (53 cards) | 2026-11-08 | https://api.scryfall.com/cards/search?q=is:gamechanger |
| P | Project pool `data/model/phase2/pool-toph-the-first-metalbender.json`; `docs/research/real-power-iterations-20261108.md` | 2026-11-08 | local |

## Card (Oracle, project cache)
{1}{R}{G}{W} 3/3. Nontoken artifacts you control are lands in addition to their other types (they gain no mana ability).
At the beginning of your end step, earthbend 2 (target land becomes a 0/0 haste creature with two +1/+1 counters; when it
dies or is exiled, it returns tapped). Consequences: every nontoken artifact you cast is a land entering (landfall), an
earthbent land that dies re-enters (landfall again), and artifact removal now hits lands.

## What the strong builds do
- **Bracket 4 lists** (T2, 1,369 decks): 34 lands, 24 creatures, 18 artifacts (which are also lands with Toph), 9
  instants, 6 sorceries, 7 enchantments. Top inclusion: Sol Ring 94 %, Bumi Unleashed 76 %, Ba Sing Se 71 %, Badgermole
  Cub 68 %, Zuran Orb 65 %, Lotus Cobra 65 %, Swords 65 %, Ashaya 63 %, Crop Rotation 63 %, Toph Hardheaded Teacher 62 %,
  Yavimaya 62 %, Toph Earthbending Master 60 %, Liquimetal Torque 58 %, Chromatic Lantern 58 %, Tannuk 58 %, Toph
  Greatest Earthbender 57 %, The Stasis Coffin 55 %, Ichor Wellspring 54 %, Great Divide Guide 54 %, Tireless Provisioner
  54 %, Enlightened Tutor 53 %, Terrasymbiosis 52 %, Dryad of the Ilysian Grove 52 %, Path 51 %, Earthbender Ascension 51 %.
  The average deck also runs Amulet of Vigor, Mishra's Bauble, Lotus Petal, The One Ring, The Ozolith, Mycosynth Lattice,
  Mindslaver, Field of the Dead, Urza's Saga, Strip Mine, Scute Swarm, Sylvan Safekeeper, Haywire Mite, Worldly Tutor,
  Gamble, Three Visits, Nature's Lore, Farseek, Deflecting Swat, Heroic Intervention, Redirect Lightning.
- **cEDH Toph is an artifact-mana combo deck** (T3, 296 decks; tags Artifacts, Combo, Lands Matter): 29 lands, 22 artifacts;
  Candelabra of Tawnos 88 %, Crop Rotation 91 %, Enlightened Tutor 91 %, Esper Sentinel 90 %, Mox Opal 87 %, Mana Vault
  86 %, Chrome Mox 86 %, Urza's Saga 86 %, Gaea's Cradle 86 %, The One Ring 83 %, Brightglass Gearhulk 82 %, Silence 81 %,
  Tezzeret Cruel Captain 80 %, Gamble 77 %, Grim Monolith 74 %, Finale of Devastation 74 %, Walking Ballista 71 %, Veil of
  Summer 69 %, Pyroblast 68 %.
- **DougY's principles** (T1): infinite mana is not a win by itself, and Toph has no sink and no draw, so every mana line
  needs a finisher or a draw engine; prefer cheap multi-purpose landfall cards; add redundancy for per-loop costs; fetches
  and graveyard recursion add landfall and resilience; Naya is weak in interaction and draw, which the deck must patch.

## Win lines
1. **Candelabra of Tawnos + Toph + a land or artifact that taps for 2+** (T1, T4): Candelabra is a land, so it untaps
   itself and the big source: infinite mana. Needs a fourth card to win (Walking Ballista, Bristly Bill, an X burn spell,
   draw with Sensei's Divining Top loops). Check the Bracket 3 script: with a common 2-mana land it can happen early.
2. **Lattice-type loops** (T4, three cards): Toph + Mycosynth Lattice, Encroaching Mycosynth or Biotransference + a sacrifice
   outlet (Goblin Bombardment, Zuran Orb, Ashnod's Altar, Viscera Seer) + a creature that earthbends on entering: infinite
   landfall and death triggers; Goblin Bombardment turns it into damage.
3. **Untap loops** (T4): Toph + Ley Weaver or Argothian Elder + Liquimetal Coating, Liquimetal Torque or Lattice: infinite
   mana from lands that are artifacts.
4. **Infinite combats**: Toph + Bumi, Unleashed + Ygra, Eater of All (T4).
5. **Landfall drain and token routes** (fair, Bracket 3 core): Sabotender, Tannuk, Valakut Exploration, Scute Swarm, Field
   of the Dead, Felidar Retreat, Omnath Locus of Rage; land army with Bumi, extra combats, The Earth King and Seismic
   Tutelage (owner's proven cards).
6. Storm Cauldron or Manascape Refractor four-card loops (T1): too many pieces for this deck.

## Engines
- Cheap artifacts are extra land drops with Toph: Mishra's Bauble, Soul-Guide Lantern, Ichor Wellspring, Lotus Petal, Mox
  Opal, Sol Ring (each a landfall trigger when cast).
- Landfall mana: Lotus Cobra, Tireless Provisioner (treasure keeps the mana for opponents' turns, T1's top card).
- Land tutors and loops: Crop Rotation (GC), Urza's Saga (fetches 0-1 MV artifacts), Expedition Map, Sylvan Safekeeper,
  Zuran Orb.

## Typical ratios of strong lists
| Item | T2 B4 average | T3 cEDH average | Note |
|---|---|---|---|
| Lands | 34 | 29 | plus 18 to 22 artifacts that count as lands for landfall but make no mana unless they are rocks |
| Ramp | many land ramp sorceries (Three Visits, Nature's Lore, Farseek) + Sol Ring, Signet, Lantern, Petal | fast mana and monoliths | the project's landfall profile asks 18+ |
| Spot answers | Swords, Path, Strip Mine, Redirect, Swat | Swords, Pyroblast, REB, Silence, Veil | 4 to 6 cheap |
| Protection | Greaves, Boots, Heroic Intervention, Swat, Stasis Coffin | Silence, Veil, Grand Abolisher-types | |
| Tutors | Enlightened, Worldly, Gamble, Crop Rotation | plus Finale, Green Sun's Zenith, Chord, Expedition Map | five of them are Game Changers (T6) |

## Must-haves, with pool status (P, 2026-11-08)
- Owned: Crop Rotation, Brightglass Gearhulk, Lotus Cobra (Spanish), Tireless Provisioner, Bumi Unleashed, Zuran Orb, Ashaya,
  Liquimetal Coating, Springheart Nantuko, Valakut Exploration, Mishra's Bauble, Soul-Guide Lantern (Spanish), Swords
  (Spanish), Path (Spanish), Deflecting Swat, Redirect Lightning, Tannuk, Great Divide Guide, The Stasis Coffin, Goblin
  Bombardment, Sabotender, The Earth King, Seismic Tutelage, Chord of Calling, Ichor Wellspring, Haywire Mite, Toph
  Hardheaded Teacher, Earthbender Ascension, Rampaging Baloths, Omnath Locus of Rage, Ragost, Reckless Handling, Abrade,
  Beast Within, Chaos Warp.
- Not in the pool (buy candidates): **Nature's Lore, Three Visits, Farseek** (cheap land ramp), **Badgermole Cub, Dryad of
  the Ilysian Grove, Sylvan Safekeeper, Scute Swarm, Felidar Retreat**, Walking Ballista (sink), **Candelabra of Tawnos**
  (combo, check the bracket script), Liquimetal Torque, Lightning Bolt-type instant answers, Heroic Intervention, Green Sun's
  Zenith, Finale of Devastation, Urza's Saga (not a Game Changer, T6). Game Changers that would take one of the three slots:
  Enlightened Tutor, Worldly Tutor, Gamble, Gaea's Cradle, Ancient Tomb, Teferi's Protection, The One Ring.

## Traps
- Infinite mana with no sink (T1). Big artifacts that clog the hand; artifact-lands that make no mana without a
  Dryad-type effect (study, Draftsim).
- Payoffs that split focus (Evolution Sage), hit one player (Mossborn Hydra), or enter lands tapped (Khalni Heart
  Expedition) (T1).
- Too little interaction: Naya lacks counters, so it needs instant answers, Silence/Veil-type protection and taxes (T1).
  The iteration-2 list fell from 7 to 4 cheap answers (P, real-power review): rebuild that.
- Toph + Gonti's Aether Heart (infinite turns) and Toph + Mindslaver (lock) are on Spellbook: chained extra turns break
  Bracket 3; a repeated Mindslaver lock draws the table against you.
- Artifact removal hits your lands while Toph is out: keep basics and real lands for the mana.
