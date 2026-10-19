# Purchase order of the 200,000 CLP plan (20261019T1542Z)

From the live stock check `20261019T1542Z.json` (`scripts/plan_purchase.py`), 6 stores chosen by the owner's rules of 2026-10-19: stock first, fewer stores, the cards at risk are secured first. Live prices of the stock check; the plan priced them a few hours earlier.

91 copies of 70 distinct cards; total 184,342 CLP; shipping assumed 30,000 CLP (outside the budget).

## How to buy

1. Fill every cart first, the A cards of each store first. A cart shows the quantity limit of a card without paying: where it says fewer than the plan needs, stop and tell me.
2. Pay store by store in the order below (the riskiest first). If a card of a store fails when you pay, use its fallback (the price difference is in the table); a card with no fallback means stop and re-plan before paying anything else.

| Order | Store | Cards | A cards | Subtotal CLP |
|---|---|---|---|---|
| 1 | gameofmagic | 11 | 4 | 31,102 |
| 2 | paytowin | 7 | 2 | 58,600 |
| 3 | lacomarca | 3 | 1 | 23,950 |
| 4 | magic4ever | 13 | 6 | 17,850 |
| 5 | cardnexus | 29 | 10 | 44,830 |
| 6 | oasis | 7 | 3 | 8,010 |

## 1. gameofmagic (31,102 CLP)

| Class | Card | Qty | Unit CLP | Stock shown | Why | Fallback inside the set |
|---|---|---|---|---|---|---|
| A | Goblin Bombardment | 2 | 3,960 | ? | quantity not shown | paytowin 4,200 (+480) |
| A | Game Trail | 2 | 915 | ? | single source, quantity not shown | none |
| A | Smoldering Marsh | 2 | 915 | ? | single source, quantity not shown | none |
| A | Desmond Miles | 1 | 915 | ? | single source | none |
| B | Lithoform Engine | 1 | 7,000 | ? | - | cardnexus 8,090 (+1,090) |
| B | Brightglass Gearhulk | 1 | 6,920 | ? | - | paytowin 9,100 (+2,180) |
| B | Return the Favor | 1 | 1,250 | ? | - | cardnexus 1,390 (+140) |
| B | Etrata, Deadly Fugitive | 1 | 1,210 | ? | - | lacomarca 3,600 (+2,390) |
| B | Glamdring, Foe-hammer // Gleam of Death | 1 | 915 | ? | - | magic4ever 1,100 (+185) |
| B | Talisman of Impulse | 1 | 742 | ? | - | oasis 15,650 (+14,908) |
| B | Thorn of the Black Rose | 1 | 570 | ? | - | lacomarca 650 (+80) |

## 2. paytowin (58,600 CLP)

| Class | Card | Qty | Unit CLP | Stock shown | Why | Fallback inside the set |
|---|---|---|---|---|---|---|
| A | Dragonskull Summit | 2 | 2,400 | ? | single source, quantity not shown | none |
| A | Etrata, the Silencer | 1 | 2,400 | ? | single source | none |
| B | Entomb | 1 | 22,200 | ? | - | cardnexus 22,990 (+790) |
| B | Springheart Nantuko | 1 | 10,400 | ? | - | lacomarca 12,800 (+2,400) |
| B | Chord of Calling | 1 | 8,100 | ? | - | gameofmagic 8,720 (+620) |
| B | Lotus Cobra | 1 | 7,700 | ? | - | cardnexus 8,090 (+390) |
| B | Narset's Reversal | 1 | 3,000 | ? | - | lacomarca 4,800 (+1,800) |

## 3. lacomarca (23,950 CLP)

| Class | Card | Qty | Unit CLP | Stock shown | Why | Fallback inside the set |
|---|---|---|---|---|---|---|
| A | Dualcaster Mage | 2 | 6,200 | ? | quantity not shown | paytowin 17,400 (+22,400) |
| B | Magister Sphinx | 1 | 10,850 | ? | - | paytowin 18,700 (+7,850) |
| B | Loyal Inventor | 1 | 700 | ? | - | gameofmagic 742 (+42) |

## 4. magic4ever (17,850 CLP)

| Class | Card | Qty | Unit CLP | Stock shown | Why | Fallback inside the set |
|---|---|---|---|---|---|---|
| A | Strionic Resonator | 1 | 7,700 | 1 | thin stock | paytowin 7,800 (+100) |
| A | Sol Ring | 1 | 1,900 | 1 | thin stock | oasis 2,220 (+320) |
| A | Chromatic Lantern | 2 | 600 | 2 | single source, thin stock | none |
| A | Rugged Prairie | 1 | 500 | 1 | thin stock | cardnexus 690 (+190) |
| A | Nekrataal | 1 | 400 | 1 | thin stock | paytowin 1,560 (+1,160) |
| A | Rakdos Signet | 1 | 400 | 1 | thin stock | paytowin 1,560 (+1,160) |
| B | Exotic Orchard | 3 | 500 | 38 | - | cardnexus 590 (+270) |
| B | Clifftop Retreat | 2 | 500 | 7 | - | cardnexus 690 (+380) |
| B | Fortified Village | 2 | 500 | 3 | - | cardnexus 590 (+180) |
| B | Sulfur Falls | 2 | 500 | 3 | - | cardnexus 590 (+180) |
| B | Isolated Chapel | 1 | 500 | 4 | - | cardnexus 690 (+190) |
| B | Nightscape Familiar | 1 | 450 | 2 | - | lacomarca 750 (+300) |
| B | Fact or Fiction | 1 | 300 | 5 | - | cardnexus 490 (+190) |

## 5. cardnexus (44,830 CLP)

| Class | Card | Qty | Unit CLP | Stock shown | Why | Fallback inside the set |
|---|---|---|---|---|---|---|
| A | Helm of the Host | 1 | 7,490 | 1 | thin stock | gameofmagic 7,690 (+200) |
| A | Queen Marchesa | 1 | 1,990 | 1 | thin stock | gameofmagic 2,480 (+490) |
| A | Sunken Hollow | 2 | 690 | 2 | thin stock | gameofmagic 2,360 (+3,340) |
| A | Fateful Absence | 2 | 490 | 2 | thin stock | magic4ever 500 (+20) |
| A | Frostboil Snarl | 2 | 490 | 2 | thin stock | gameofmagic 915 (+850) |
| A | Mana Leak | 2 | 490 | 2 | thin stock | lacomarca 550 (+120) |
| A | Darkwater Catacombs | 1 | 790 | 1 | thin stock | oasis 900 (+110) |
| A | Shadowblood Ridge | 1 | 590 | 1 | thin stock | paytowin 2,400 (+1,810) |
| A | Bitter Triumph | 1 | 490 | 1 | thin stock | lacomarca 1,200 (+710) |
| A | Liquimetal Coating | 1 | 490 | 1 | thin stock | oasis 630 (+140) |
| B | Solve the Equation | 1 | 5,390 | 4 | - | lacomarca 6,250 (+860) |
| B | Storm-Kiln Artist | 1 | 3,590 | 2 | - | lacomarca 4,150 (+560) |
| B | Drowned Catacomb | 2 | 1,190 | 3 | - | lacomarca 4,300 (+6,220) |
| B | Underground River | 1 | 1,990 | 2 | - | magic4ever 3,500 (+1,510) |
| B | Sulfurous Springs | 1 | 1,790 | 3 | - | gameofmagic 3,250 (+1,460) |
| B | Reckless Handling | 3 | 590 | 4 | - | oasis 630 (+120) |
| B | Godo, Bandit Warlord | 1 | 1,590 | 6 | - | lacomarca 1,900 (+310) |
| B | Sunken Ruins | 1 | 1,490 | 3 | - | paytowin 14,200 (+12,710) |
| B | Stroke of Midnight | 2 | 690 | 3 | - | paytowin 1,560 (+1,740) |
| B | Venser, Shaper Savant | 1 | 990 | 2 | - | magic4ever 1,200 (+210) |
| B | Arcane Signet | 1 | 890 | 4 | - | gameofmagic 1,000 (+110) |
| B | Ravenloft Adventurer | 1 | 890 | 3 | - | oasis 1,500 (+610) |
| B | Sakura-Tribe Elder | 1 | 890 | 6 | - | paytowin 900 (+10) |
| B | Shivan Reef | 1 | 690 | 4 | - | gameofmagic 915 (+225) |
| B | Soul-Guide Lantern | 1 | 690 | 2 | - | lacomarca 700 (+10) |
| B | Stormcatch Mentor | 1 | 690 | 5 | - | paytowin 6,700 (+6,010) |
| B | Furycalm Snarl | 1 | 590 | 5 | - | gameofmagic 915 (+325) |
| B | Tome of Legends | 1 | 490 | 2 | - | magic4ever 500 (+10) |
| B | Winter Soldier, Icy Assassin | 1 | 490 | 4 | - | magic4ever 500 (+10) |

## 6. oasis (8,010 CLP)

| Class | Card | Qty | Unit CLP | Stock shown | Why | Fallback inside the set |
|---|---|---|---|---|---|---|
| A | Everflowing Chalice | 2 | 500 | ? | quantity not shown | lacomarca 650 (+300) |
| A | Mystical Teachings | 2 | 450 | ? | quantity not shown | lacomarca 500 (+100) |
| A | Survivors' Encampment | 1 | 450 | ? | single source | none |
| B | Tireless Provisioner | 1 | 3,560 | ? | - | paytowin 3,700 (+140) |
| B | Kolaghan's Command | 1 | 900 | ? | - | paytowin 2,400 (+1,500) |
| B | Infernal Grasp | 1 | 700 | ? | - | cardnexus 890 (+190) |
| B | Command Tower | 1 | 500 | ? | - | gameofmagic 570 (+70) |
