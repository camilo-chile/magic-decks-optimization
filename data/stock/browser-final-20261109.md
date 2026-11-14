# Browser read of the final purchase, 2026-11-09

- UTC time of this write: 2026-11-09T10:33Z. Part 1 reads: GoM about 10:05-10:20Z (start not logged), PayToWin 10:20:48-10:26:15Z.
- Method: `scripts/browser_shopify_lookup.js` in a store tab (window.name = names, polled `window.__wl`), then Part 2 by `fetch()` from the store tab (suggest.json, then products/<handle>.js, 1.5 s pause). No HTTP 429 was met, so no line is UNVERIFIED. Damaged variants are excluded from every pick below.
- Files: `data/prices/browser-gameofmagic-20261109-final.psv` (30 lines), `data/prices/browser-paytowin-20261109-final.psv` (64 lines). Checksums computed in the page: GoM h=823590, PayToWin h=521357. A Python re-check was not possible in this session (no shell tool), so the copies are unverified by Python.

## Part 1: names read

| Store | Names read | Found (at least one available variant) | Not found |
|---|---|---|---|
| Game of Magic Singles | 31 | 20 | 11 |
| PayToWin | 35 | 32 | 3 |

Names with no available variant:
- Game of Magic Singles: Shred Memory, Turnabout, Golgari Signet, Altaïr Ibn-La'Ahad, Eivor Battle-Ready, Prologue to Phyresis, Tribute Mage, Trophy Mage, Ramses Assassin Lord, Diabolic Tutor, Fellwar Stone.
- PayToWin: Altaïr Ibn-La'Ahad, Radiant Summit, Prologue to Phyresis.

## Part 2a: the named cards, every available variant (Damaged excluded)

### Ramses, Assassin Lord
| Store | Variant | Price CLP |
|---|---|---|
| GoM | none (DMU Commander 0/10; Foil Etched 0/5) | - |
| PayToWin | Lightly Played (English), DMU Commander, 1 of 30 | 3100 |

### Diabolic Tutor
| Store | Variant | Price CLP |
|---|---|---|
| GoM | none in the 10 suggestions (Odyssey, Secret Lair 1592 and variants, Tenth Edition, Oversized, SL Retro: all 0 available) | - |
| PayToWin | Magic 2012, Heavily Played | 1600 |
| PayToWin | Magic 2014, Lightly Played | 1800 |
| PayToWin | Magic 2011, Moderately Played | 1800 |
| PayToWin | Kaladesh, Lightly Played | 2000 |
| PayToWin | WPN 2024, Lightly Played Foil | 2400 |
| PayToWin | Conspiracy: Take the Crown, Lightly Played | 2500 |
| PayToWin | Magic 2010, Moderately Played | 2700 |
| PayToWin | Magic 2010, Lightly Played | 2900 |
| PayToWin | Magic 2012, Lightly Played Foil Spanish | 7900 |
| PayToWin | Conspiracy: Take the Crown, Near Mint Foil | 6300 |
| PayToWin | Odyssey, Lightly Played Foil | 62600 |

### Prologue to Phyresis, Counterspell, Flux Channeler, Tribute Mage, Trophy Mage
| Card | Store | Cheapest available (any language) | Cheapest SPANISH |
|---|---|---|---|
| Prologue to Phyresis | GoM | none (Phyrexia: All Will Be One, 0/11) | no Spanish |
| Prologue to Phyresis | PayToWin | not found | no Spanish |
| Counterspell | GoM | Near Mint 7480 (MH2 Borderless) | Near Mint Foil Espanol 16000 (Retro Release, DMR); no non-foil Spanish in the hits |
| Counterspell | PayToWin | Near Mint 3000 (Retro, DMR) | Near Mint 4300 (MH2); LP Spanish 5100 (7th Ed.), MP Spanish 4700 (7th Ed.) |
| Flux Channeler | GoM | Near Mint 4640 (WotS) | no Spanish |
| Flux Channeler | PayToWin | Moderately Played 4200 (WotS); LP 4600 | no Spanish |
| Tribute Mage | GoM | not found in the 10 suggestions | not found |
| Tribute Mage | PayToWin | Lightly Played 1440 (MH); LP Foil 3500 and 4600; NM Foil 3100 (Secret Lair) | no Spanish |
| Trophy Mage | GoM | not found | not found |
| Trophy Mage | PayToWin | Near Mint 1560 (Aether Revolt) | Moderately Played 1700 (Aether Revolt Promos, Game Day) |

### Shred Memory and Turnabout
| Card | Store | Variant | Price CLP |
|---|---|---|---|
| Shred Memory | GoM | none | - |
| Shred Memory | PayToWin | Moderately Played Spanish (RAV CoG), cheapest | 1500 |
| Shred Memory | PayToWin | Lightly Played Spanish (RAV CoG) | 1600 |
| Turnabout | GoM | none | - |
| Turnabout | PayToWin | Near Mint (DMR), cheapest; Near Mint Foil and Retro DMR also 1560 | 1560 |
| Turnabout | PayToWin | Near Mint (Urza's Saga) | 2300 |

## Part 2b: Mountain (268) Full Art, PayToWin

- "Mountain (268) (Full Art) [Battle for Zendikar]": 4 of 30 available.
- Lightly Played Spanish at 900: STILL AVAILABLE.
- Cheapest available in that product: Moderately Played (English) 825. Other available: Near Mint 975, Near Mint Foil 1300.
- GoM: not searched (not requested).

## Part 2c: tokens

| Needed token | Store | Title, set | Variant | Price CLP | Available |
|---|---|---|---|---|---|
| Assassin 1/1 black menace (AC version) | GoM | Assassin Token [Assassin's Creed Tokens] | Near Mint | 570 | yes (1 of 5) |
| Assassin 1/1 black menace (AC version) | GoM | Human Rogue Token [Assassin's Creed Tokens] (other token) | Near Mint | 570 | yes |
| Assassin 1/1 black menace (AC version) | PayToWin | none in the 10 suggestions | - | - | - |
| Assassin deathtouch and haste (OTJ or CTTC) | GoM | Assassin Token [Conspiracy: Take the Crown Tokens] | - | - | no (0 of 5) |
| Assassin deathtouch and haste (OTJ or CTTC) | GoM | OTJ: none in the suggestions | - | - | - |
| Assassin deathtouch and haste (OTJ or CTTC) | PayToWin | CTTC and OTJ: none in the suggestions | - | - | - |
| Assassin, Return to Ravnica (not on the wanted list) | PayToWin | Assassin Token [Return to Ravnica Tokens] | Lightly Played | 900 | yes (1 of 15) |
| Bird 2/2 blue flying | GoM | no 2/2 blue bird confirmed; Bird tokens listed at 570 each: Ravnica Remastered (wrong per owner), Commander Masters DFC, Innistrad MH, DMU (wrong per owner), Commander Masters Insect DFC, Commander Masters Treasure//Bird DFC | Near Mint | 570 | yes |
| Bird 2/2 blue flying | PayToWin | Bird Token [Return to Ravnica Tokens] (wrong per owner); Bird (002)//Saproling (016) [Commander 2016] (Japanese, excluded); Human Warrior//Bird DFC [Kaldheim] | NM / LP / NM Foil | 900 to 975 | yes |

Token notes: the Shopify JSON gives set, rarity and "Token Creature" tags, but NO power, toughness or colour. The 1/1 versus 2/2 and colour checks cannot be made from store data; the Assassin AC token is taken from its set name only. The OTJ and CTTC Assassin tokens are not confirmed in both stores.

## Summary of unfound or unavailable names
- Game of Magic Singles: 11 names not found, plus Ramses, Diabolic Tutor, Prologue, Tribute Mage, Trophy Mage, Turnabout, Shred Memory with no available variant (see Part 1).
- PayToWin: Altaïr Ibn-La'Ahad, Radiant Summit, Prologue to Phyresis.
