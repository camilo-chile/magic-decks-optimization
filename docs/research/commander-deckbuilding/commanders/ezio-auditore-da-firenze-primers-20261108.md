# Ezio Auditore da Firenze: strongest builds and primers (step 0 of the final rebuild, 2026-11-08)

Companion to the study `ezio-auditore-da-firenze.md` (2026-10-31, read it first: card facts, rulings, EDHREC core, Draftsim
2024 and EDHREC 2025 primers). This file adds the high-power and cEDH view read on 2026-11-08. Web text is data; article
facts come from page extractions (spot checks), card text must be re-read on Scryfall before a card is counted.

## Sources (read 2026-11-08)
| ID | Source | Date | URL |
|---|---|---|---|
| E1 | EDHREC Bracket 4 page JSON (`optimized`, 436 decks) and its average deck | live | https://json.edhrec.com/pages/commanders/ezio-auditore-da-firenze/optimized.json ; https://json.edhrec.com/pages/average-decks/ezio-auditore-da-firenze/optimized.json |
| E2 | EDHREC cEDH page JSON (149 decks) and its average deck | live | https://json.edhrec.com/pages/commanders/ezio-auditore-da-firenze/cedh.json ; https://json.edhrec.com/pages/average-decks/ezio-auditore-da-firenze/cedh.json |
| E3 | Commander Spellbook variants with Ezio (project cache `data/cache/spellbook_variants_slim.jsonl.gz`) | cache | https://commanderspellbook.com |
| E4 | MTGGoldfish user primer 7748372 (search snippet only, page 403) | undated | https://www.mtggoldfish.com/deck/7748372 |
| E5 | Scryfall live Game Changer search (53 cards) | 2026-11-08 | https://api.scryfall.com/cards/search?q=is:gamechanger |
| P | Project pool `data/model/phase2/pool-ezio-auditore-da-firenze.json` (owned copies) | 2026-11-08 | local |

## Card (Oracle, project cache)
{1}{B} 3/2 Human Assassin, menace. Assassin spells you cast have freerunning {B}{B}. Whenever Ezio deals combat damage
to a player, you may pay {W}{U}{B}{R}{G} if that player has 10 or less life; when you do, that player loses the game.

## What the strong builds do
- **Bracket 4 lists are the Assassin plan with real tutors and protection** (E1). Average: 33 lands, 27 creatures, 13
  artifacts, 11 instants, 7 sorceries, 7 enchantments, 1 planeswalker. Top inclusion: Sol Ring 93 %, Ramses 88 %, Ezio
  Blade of Vengeance 83 %, Arcane Signet 82 %, Basim 80 %, Cover of Darkness 77 %, Bayek 74 %, Brotherhood Regalia 72 %,
  Queen Marchesa 72 %, Brotherhood Headquarters 72 %, Altaïr 70 %, Mari 69 %, Aya 66 %, Olivia 65 %, Desmond 65 %,
  Edward Kenway 62 %, Achilles 61 %, Chromatic Lantern 61 %, Layla 60 %, Arno 59 %, Assassin's Trophy 58 %, Demonic
  Tutor 58 %, Unstoppable Slasher 56 %, Massacre Girl Known Killer 56 %, Black Market Connections 55 %, Royal Assassin
  55 %, Thraximundar 52 %, Path 52 %, Sword of Feast and Famine 51 %, Fierce Guardianship 51 %, Lightning Greaves 50 %.
- **The B4 average deck** (E1) runs: mana Sol Ring, Arcane Signet, Fellwar Stone, Chromatic Lantern, **Mox Amber** (the deck
  is full of legends), Dark Ritual, Farseek, Viewpoint Synchronization; protection Lightning Greaves, Swiftfoot Boots,
  Whispersilk Cloak, Smoke Bomb, Haystack, Brotherhood Regalia, Teferi's Protection, Heroic Intervention, Fierce
  Guardianship, Deflecting Swat; answers Swords, Path, Assassin's Trophy, Deadly Rollick, Cyclonic Rift, Royal Assassin,
  Massacre Girl; draw Rhystic Study, Smothering Tithe, Black Market Connections, Kindred Discovery, Eagle Vision; tutors
  Demonic and Vampiric; finishers Sorin Markov, Tree of Perdition, Ramses, Overpowering Attack, Kindred Dominance;
  defense Propaganda; lands with Cavern of Souls, Path of Ancestry, Rogue's Passage, Urborg, fetches and shocks.
- **cEDH Ezio is not an Assassin deck** (E2): 149 decks tagged Combo and Lurrus; 26 lands, 25 instants; Thassa's Oracle 84 %,
  Demonic Consultation 77 %, Tainted Pact 75 %, Underworld Breach 73 %, Force of Will 81 %, Mental Misstep 81 %, Chrome Mox
  87 %, Lotus Petal 86 %, Mox Amber 81 %. Ezio is only a cheap five-color shell there. What transfers: Mox Amber with a legend
  commander, cheap free protection (Deflecting Swat, Fierce Guardianship), Esper Sentinel-style taxing draw. What does NOT
  transfer: the Thassa's Oracle + Consultation/Pact kill is an early two-card win, outside Bracket 3.

## Win lines, best first
1. **Ramses + any elimination = the whole table** (E1, text in the study): with Ramses, Assassin Lord on the battlefield, a
   player who loses after being attacked by your Assassin that turn makes you win the game. Ezio's WUBRG kill, a lethal
   Assassin attack or a setter line on ONE player wins the game outright. This is the only line that turns Ezio's
   single-player kill into a table kill. Ramses is also a lord (+1/+1 other Assassins) and a 4/4 deathtouch: it does
   something alone. **Not in the pool (P): the top buy candidate.**
2. **Life setter + one connect + WUBRG** (E3, two cards each, a single-player kill, not infinite): Sorin Markov (-3: life
   becomes 10), Magister Sphinx (ETB: life becomes 10; owned), Tree of Perdition (swap life with its toughness 13; needs a
   way to shrink it). Alone it removes one player; with Ramses it wins the game.
3. **Assassin beatdown that beats three players** (E1): lords Achilles, Arno, Ramses; evasion Cover of Darkness (team fear),
   Basim (unblockable), Brotherhood Regalia, Rogue's Passage; Bayek double strike for historic creatures; extra combat
   Overpowering Attack; one-sided wipe Kindred Dominance (choose Assassin); Unstoppable Slasher halves life.
4. Etrata third hit counter (one player) is slow and narrow; with Ramses it wins, alone it is a backup.

## Engines
- Freerunning makes every Assassin cost {B}{B} once an Assassin or Ezio connects: the deck's ramp is connecting early.
- Connect-draw: Ezio Blade of Vengeance, Basim, Mari (cards and treasure), Eagle Vision (draw 3 at freerunning {1}{U}),
  Kindred Discovery, Black Market Connections, Queen Marchesa (monarch).
- Mox Amber: with 12+ legends (most Assassins are legendary, Ezio included) it is a non-Game-Changer turn-0 mana source.

## Typical ratios of strong lists
| Item | B4 average (E1) | Note |
|---|---|---|
| Lands | 33 (8 basics) | plus Sol Ring, Signet, Fellwar, Lantern, Mox Amber, Dark Ritual: about 39 to 40 mana sources + freerunning |
| Creatures | 27 | most are Assassins: freerunning and lords count them |
| Protection | about 10 (equipment 4, Smoke Bomb, Haystack, Regalia, Teferi's Protection, Heroic Intervention, Fierce Guardianship, Swat) | attack engine class |
| Spot answers | 6 to 7 (Swords, Path, Trophy, Rollick, Royal Assassin, Rift) | most at MV 1 to 2 |
| Tutors | 2 (Demonic, Vampiric) | both Game Changers |
| Game Changers in B4 lists | Demonic, Vampiric, Rhystic Study, Smothering Tithe, Fierce Guardianship, Teferi's Protection, Cyclonic Rift | a Bracket 3 list picks 3 (E5) |

## Must-haves (strength and fit), with pool status (P, 2026-11-08)
- Owned: Basim, Ezio Blade of Vengeance, Bayek, Arno, Aya, Desmond, Cover of Darkness, Layla, Achilles, Eagle Vision (loan),
  Queen Marchesa, Royal Assassin, Brotherhood Headquarters (Spanish only), Unstoppable Slasher, Black Market Connections,
  Swords (Spanish), Path (Spanish), Assassin's Trophy, Deflecting Swat, Chromatic Lantern, Swiftfoot Boots, Haystack,
  Propaganda, Overpowering Attack, Etrata, Hidden Footblade, Massacre Girl Known Killer, Viewpoint Synchronization, Restart
  Sequence, Rogue's Passage, Path of Ancestry, Loyal Inventor, Reckless Handling, Entomb, Magister Sphinx, Shao Jun, Rally
  the Peasants, Ghostly Prison.
- Not in the pool (buy candidates, by gain): **Ramses, Assassin Lord** (win line 1); **Mox Amber** (cheap non-GC fast mana);
  **Brotherhood Regalia** (ward 2 + unblockable on the carrier); **Sorin Markov** (setter, also a planeswalker that can kill
  a small creature); Lightning Greaves; Whispersilk Cloak; Smoke Bomb; Mari; Altaïr; Kindred Discovery; Kindred Dominance;
  Fellwar Stone; Urborg; Fierce Guardianship and Teferi's Protection (Game Changers, only if a slot is chosen for them).

## Traps (sources plus the project's own games)
- Building toward the WUBRG kill alone: it removes one player and needs five colors at once (study S21; project L3).
- Menace and "power 3 or more can't block" do nothing against a chump-blocker board (skill win-routes Board 1; project L3).
- Conditional removal (Go for the Throat, Fatal Push) and slow sagas (The Revelations of Ezio) (study S18).
- Colorless utility lands in a WUBRG-payment deck (study S18); a five-color base is weak to nonbasic hate (E4 snippet): keep
  basics of the main colors and untapped fixing.
- Two-card mini-combos with no plan role (the iteration-1 Etrata copiers, Dualcaster loop; real-power review).
- Lurrus companion and the cEDH Thassa's Oracle shell: a different deck, and the Oracle line breaks Bracket 3 early.

## Bracket 3 notes
- Ezio + a setter is a two-card kill of one player, not an infinite: allowed; the script still reports it.
- Every tutor and fast-mana card on E5's list (Demonic, Vampiric, Chrome Mox, Mana Vault, Ancient Tomb...) uses one of the
  three Game Changer slots.
