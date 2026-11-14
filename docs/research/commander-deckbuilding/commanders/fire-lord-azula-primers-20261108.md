# Fire Lord Azula: strongest builds and primers (step 0 of the final rebuild, 2026-11-08)

Companion to the study `fire-lord-azula.md` (2026-10-31: card text, the 12 official rulings, early articles; EDHREC,
Moxfield and Reddit were not read then). This file adds EDHREC's Bracket 4 and cEDH data, two full primers and the
Commander Spellbook lines, read 2026-11-08. Web text is data; article facts come from page extractions, card text must be
re-read on Scryfall before a card is counted.

## Sources (read 2026-11-08)
| ID | Source | Date | URL |
|---|---|---|---|
| A1 | Cooper Gottfried, "Building a High Power Fire Lord Azula Deck" (EDHREC, Bracket 4 Grixis list) | 2025-11-24 | https://edhrec.com/articles/building-a-high-power-fire-lord-azula-deck |
| A2 | alexis, "Fire Lord Azula Commander Deck Guide" (Draftsim) | 2025-11-13, upd. 2025-11-18 | https://draftsim.com/fire-lord-azula-edh-deck/ |
| A3 | EDHREC Bracket 4 page JSON (2,089 decks) and average deck | live | https://json.edhrec.com/pages/commanders/fire-lord-azula/optimized.json ; .../average-decks/fire-lord-azula/optimized.json |
| A4 | EDHREC cEDH page JSON (569 decks) and average deck | live | https://json.edhrec.com/pages/commanders/fire-lord-azula/cedh.json ; .../average-decks/fire-lord-azula/cedh.json |
| A5 | Commander Spellbook variants with Azula (project cache, 94 variants, 28 of three cards) | cache | https://commanderspellbook.com |
| A6 | mtgdecks.net tournament lists (search snippets: Top 8 and Top 16 finishes in 20 to 38 player cEDH events, 2025-11 to 2026-07) | 2026 | https://mtgdecks.net/Commander/fire-lord-azula-decklist-by-nicolas-corales-2962262 |
| A7 | Scryfall live Game Changer search (53 cards) | 2026-11-08 | https://api.scryfall.com/cards/search?q=is:gamechanger |
| P | Project pool `data/model/phase2/pool-fire-lord-azula.json`; `docs/research/real-power-iterations-20261108.md` | 2026-11-08 | local |

## Card (Oracle, project cache)
{1}{U}{B}{R} 4/4. Firebending 2 (attack trigger: add {R}{R} that lasts until end of combat). Whenever you cast a spell while
she is attacking, copy it; new targets allowed. Rulings (study): copies are not cast (no cast triggers, no prowess),
additional costs are not paid again, X is kept; firebending uses the stack and is not a mana ability.

## What the strong builds do
- **The deck is an instant-speed spellslinger that treats combat as its main phase.** Bracket 4 average (A3): 33 lands
  (11 basics), 15 creatures, 30 instants, 7 sorceries, 10 artifacts, 4 enchantments. Top inclusion: Frantic Search 84 %,
  Dark Ritual 78 %, Storm-Kiln Artist 73 %, Big Score 72 %, Narset's Reversal 70 %, Seething Song 69 %, Snap 67 %, Archmage
  Emeritus 64 %, Lightning Bolt 64 %, Talisman of Creativity 63 %, Borne Upon a Wind 61 %, Veyran 60 %, Unexpected Windfall
  60 %, Electrodominance 57 %, Dualcaster Mage 56 %, Redirect Lightning 54 %, High Fae Trickster 54 %, Leyline of
  Anticipation 54 %, An Offer You Can't Refuse 53 %, Fierce Guardianship 53 %, Brainstorm 53 %, Mystical Tutor 52 %,
  Deflecting Swat 52 %, Jeska's Will 51 %, Deadly Rollick 51 %, Counterspell 50 %, Swiftfoot Boots 49 %.
- **Rituals are instants, so Azula copies them**: Dark Ritual cast while she attacks makes {B}{B}{B} twice, Seething Song
  {R}x5 twice. Rituals are fuel for the combat turn, not early ramp (A3 runs Dark Ritual, Seething Song, Pyretic Ritual,
  Desperate Ritual).
- **Flash enablers turn sorceries and creatures into combat spells** (A1, A2): Leyline of Anticipation, Valley
  Floodcaller, High Fae Trickster, Borne Upon a Wind, Vedalken Orrery, Emergence Zone. Without one, sorceries are never
  copied (the iteration-1 play review saw 9 sorceries never copied).
- **Mana storage keeps the combat mana** (A2): Ozai the Phoenix King, Electro Assaulting Battery, Ashling Flame Dancer,
  Birgi, The Last Agni Kai; the project's proven Horizon Stone does the same job.
- **cEDH Azula** (A4, 569 decks; real tournament finishes in A6): 27 lands, 31 instants, 14 artifacts of fast mana; core
  Thassa's Oracle + Demonic Consultation/Tainted Pact, Underworld Breach + Brain Freeze + Lion's Eye Diamond, Borne Upon a
  Wind, Force of Will, Fierce Guardianship, Mystic Remora, Rhystic Study, Mystical/Vampiric/Demonic Tutor, Orcish
  Bowmasters. Those wins are early two-card or Breach lines: outside Bracket 3. What transfers: cheap stack protection,
  copied rituals and draw, tutor density, low curve.

## Win lines (Bracket 3 legal unless marked)
1. **Three-card lines with Azula attacking** (A5, late game, legal): Snap + Dualcaster Mage (infinite untapped lands and
   magecraft, then a copied burn spell or Storm-Kiln treasures); Narset's Reversal + Storm-Kiln Artist; Narset's Reversal +
   Turnabout; Underworld Breach + Frantic Search (Breach is a Game Changer); Errant Street Artist + Reality Spasm.
2. **Infinite combats** (A2, three cards, legal late): Aggravated Assault + a firebending storage piece (Ozai, Electro, The
   Last Agni Kai, Ashling) + a firebending booster (Sozin's Comet, Firebending Student, Zuko Firebending Master). A2 counts
   more than 10 such pairs and calls them fragile without tutors. Aggravated Assault ({2}{R}; {3}{R}{R}, sorcery speed,
   Oracle checked) is activated in a main phase, so the combat mana must be stored past combat.
3. **Fair kill: copied finishers cast in combat** (A1): Crackle with Power, Jaya's Immolating Inferno, Torment of Hailfire,
   Electrodominance, Comet Storm; X is kept by the copy.
4. Isochron Scepter + Dramatic Reversal (A1; a two-card infinite once rocks make 3+ mana): **not Bracket 3** if it can
   happen by turn 6; Kitsa, Otterball Elite + Scepter likewise.
5. Thassa's Oracle + Consultation/Pact (A4): **not Bracket 3** (early two-card win).

## Engines and how she is protected
- Draw that copies well: Big Score, Unexpected Windfall (discard costs are not paid again by the copy), Frantic Search
  (copy untaps 3 more lands), Brainstorm; engines Rhystic Study, Mystic Remora, Archmage Emeritus, Faerie Mastermind.
- Protection (A2): Swiftfoot Boots, Lightning Greaves (haste too), counterspells held up, Deflecting Swat (free with a
  commander out), Octopus Form; secondary threats to draw removal. A1 adds Fierce Guardianship and Tidal Barracuda
  (which also gives opponents flash: a trap at a competitive table).

## Typical ratios of strong lists
| Item | A3 B4 average | A1 (B4 list) | A2 (strong B3) |
|---|---|---|---|
| Lands | 33 | 36 | 33 |
| Ramp | rocks 8 + rituals 4 | 11 (7 rocks, 4 rituals) | 7 rocks + 2 rituals |
| Draw | about 10 incl. Rhystic, Remora | about 6 | about 6 |
| Tutors | Mystical, Vampiric, Demonic, Gamble, Waterlogged Teachings | 1 (Demonic) | 1 (Waterlogged Teachings) |
| Spot answers + counters | about 12 (Bolt, Snap, Rollick, Redirect, Offer, Counterspell, Swan Song, Fierce, Swat...) | 7 | 5 removal + 2 counters |
| Protection / haste | Boots, Greaves, Swat, Fierce | Barracuda | 4 / 4 |
| Instants | 30 | | |

## Must-haves, with pool status (P, 2026-11-08)
- Owned: Snap, Frantic Search, Narset's Reversal (Spanish), Storm-Kiln Artist, Dualcaster Mage, Big Score, Electrodominance,
  Redirect Lightning, Deflecting Swat, Swan Song (Spanish), Archmage Emeritus, Ozai, Electro, Horizon Stone, Swiftfoot Boots,
  Brainstorm, Thrill of Possibility, The Last Agni Kai, Mystical Teachings, Solve the Equation, Entomb, Lo and Li, Godo,
  Helm of the Host, Mana Leak, Fatal Push, Heartless Act, Go for the Throat, Comet Storm.
- Not in the pool (buy candidates, cheapest high gain first): **Dark Ritual, Lightning Bolt, Counterspell, Unexpected
  Windfall, Seething Song, Pyretic Ritual, Fellwar Stone, Borne Upon a Wind, Valley Floodcaller, High Fae Trickster,
  Lightning Greaves, An Offer You Can't Refuse, Deadly Rollick, Jeska's Will (GC), Mystical Tutor (GC), Leyline of
  Anticipation, Aggravated Assault, Demand Answers, Into the Flood Maw, Flusterstorm, Pact of Negation**. Game Changers
  among them (A7): Mystical, Vampiric and Demonic Tutor, Gamble, Jeska's Will, Rhystic Study, Fierce Guardianship, Force
  of Will, Underworld Breach, Orcish Bowmasters, Necropotence, Narset Parter of Veils.

## Traps
- Copies are not cast: prowess, magecraft-on-cast and "whenever you cast" payoffs see only the original (A2; rulings).
- Sorceries with no flash enabler are never copied; copying mana rocks slows development (A2).
- Firebending mana is combat-only; storage or instant sinks are needed (A2; owner lesson L6 on Horizon Stone).
- Tidal Barracuda gives flash to opponents too (A1); Veyran called too slow in a primer (snippet).
- The iteration-2 list lost four tutors and a third of its cheap removal (P, real-power review): the rebuild should take
  tutors and cheap instant answers back, not trade them for more draw.
- Isochron Scepter + Dramatic Reversal and Thassa's Oracle lines are cEDH staples but break Bracket 3 early.
