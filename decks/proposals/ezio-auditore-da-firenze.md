# Ezio Auditore da Firenze: purchase ladder, round 4 (Phase 8 step 2, 2026-10-19)

Main ladder: `decks/proposals/ezio-auditore-da-firenze.ladder.txt` (free base + 54 swaps). Black-core variant:
`decks/proposals/ezio-auditore-da-firenze.bcore.ladder.txt` (free base + 26 swaps, section at the end). Both checked with
`python -I -X utf8 scripts/ladder.py <file> --caps 0,15000,25000,35000,50000,75000,100000,150000`: every step valid
(0 INVALID; 100 cards, no reversible card, every purchase in stock, Layer A floor 3, 0 Game Changers). Prices:
`merged-20261019T1013Z.json` (a hint; stock is checked in Phase 9). Round 3 is in version control history. No power
numbers: the Commander Salt measurement replaces them.

## Why round 4 changes the plan
Round 3 measured (Salt 2026.4195): 6.4 at 24,827, 7.0 at 45,872, 6.9 at 70,872 (cap "sparse slow combo package"), 7.0 at
93,962, 7.1 at 141,322 CLP; Manabase Quality 94-96 %; pillars Consistency 289, Efficiency 191, Interaction 173,
Wincons 353 (baselines 100/100/140/200). Toph broke its plateau with 16 Layer-A-legal Spellbook variants, 10 tutors and a
lower average mana value. Round 4 therefore:
- keeps the mana that already gives about 94 % (12 cheap lands instead of 14, no later land purchases);
- moves the money from staples to **cheap win lines that share hubs**: 1 line in the free base, 3 at 15,000, 10 at 50,000,
  15 at 100,000 (round 3: 0 / 1 / 1 / 3 / 3);
- adds the tutors that reach them from 15,000 (Mystical Teachings, Reckless Handling) and four more at 150,000;
- lowers the average mana value of the nonland cards to 2.59 at the base and at most 2.81 (round 3: 3.06 to 3.14):
  the base drops the 5- to 8-drops (Eivor, Rakdos, Combustion Man, Decree of Pain) for owned 0- to 2-mana cards.

## Checkpoints to measure
| Cap CLP | Step | Cost CLP | Spellbook lines | Tutors that reach a line | What the block buys |
|---|---|---|---|---|---|
| 0 | 0 | 0 | 1: Deadeye + Intruder Alarm | Seismic Sense, Entomb + Restart Sequence (Deadeye) | owned cards only; average mana value 2.59 |
| 15,000 | 14 | 14,655 | 3: + Venser + Alarm, Etrata + Return the Favor + Camera | + Mystical Teachings (Venser, Return the Favor), Reckless Handling and Loyal Inventor (Camera), Adéwalé (Etrata) | Lantern, Orchard, Encampment, 4 B duals, Infernal Grasp |
| 25,000 | 31 | 24,751 | 3 | same | 6 more duals (MBQ near round 3's 94 %), Thorn, Ravenloft, Desmond, Winter Soldier, Etrata Deadly Fugitive, Nekrataal, Fateful Absence, Bitter Triumph, Mana Leak, Kolaghan's Command, Tome |
| 35,000 | 33 | 34,541 | 5: + Etrata + Strionic + Return the Favor / + Camera | + Reckless and Loyal Inventor reach Strionic | Strionic Resonator, Queen Marchesa |
| 50,000 | 39 | 48,951 | 10: + 3 Lithoform lines, Dualcaster + Starfall Invocation, Dualcaster + Ember Island Production | + Mystical Teachings reaches Dualcaster | Lithoform Engine, Dualcaster, Rakdos Signet, Stroke of Midnight, Everflowing Chalice |
| 75,000 | 43 | 74,151 | 13: + Kiki + Alarm, Kiki + Dualcaster + Return the Favor, Kiki + Bombardment + All-Fates Stalker | Kiki: Seismic Sense, Entomb | Kiki-Jiki, Goblin Bombardment, All-Fates Stalker, Sheoldred's Edict |
| 100,000 | 50 | 97,791 | 15: + Godo + Helm, Kiki + Helm | + Godo (Helm), Reckless and Loyal Inventor (Helm) | Godo, Helm, Counterspell, Talisman of Dominance, Phyrexian Arena, Whispersilk Cloak, Fellwar Stone |
| 150,000 | 54 | 148,011 | 15 | + Recruiter of the Guard (Kiki, Dualcaster, Venser), Idyllic Tutor (Intruder Alarm), Diabolic Intent (any) | Mari |

Stores: 5 at 15,000 (cardnexus, gameofmagic, magic4ever, oasis, paytowin), 6 from 25,000 (+ piedrabruja), 7 from 50,000
(+ lacomarca). Piedrabruja sells only the cheapest Thorn of the Black Rose (350; gameofmagic 570) and Frostboil Snarl (481;
cardnexus 490): dropping it adds 229 CLP and every checkpoint keeps its step.

## Strategy and engine
Black Assassin tempo with dense, cheap combo hubs. Ezio (2 mana, menace) and 1- to 2-mana Assassins connect early; then
every Assassin spell costs {B}{B} (freerunning), and with Roshan every creature is an Assassin (Kiki-Jiki, Godo, Dualcaster
included). Card flow comes from combat (Ezio, Blade of Vengeance, Tome, Etrata Deadly Fugitive, Mari) and from the crown
(Thorn, Queen, Ravenloft). The win lines share five hubs, so each new piece adds several lines: **Intruder Alarm** (owned),
**Etrata, the Silencer** with four copiers, **Dualcaster Mage**, **Kiki-Jiki** and **Helm of the Host**. The copiers
(Return the Favor, Camera, Strionic Resonator, Lithoform Engine) also copy Godo's, Helm's, Thorn's and Ravenloft's
triggers, so they are not dead outside the combo. Mari and Ravenloft put hit counters on the opponents' dead creatures,
which count toward Etrata's three-card kill.

## Win lines (exact cards; all checked by Layer A: floor 3, no early two-card line)
| # | Cards | From step | How it wins | Tutors that reach it | Layer A |
|---|---|---|---|---|---|
| 1 | Deadeye Navigator + Intruder Alarm | base | Blink loop; every entry untaps the mana creatures (Deathcap, any dork): infinite enters with any ETB Assassin | Seismic Sense, Entomb + Restart Sequence; Idyllic (Alarm) at 150k | 2 cards, 9 mana: floor 3 |
| 2 | Venser, Shaper Savant + Intruder Alarm | 3 | Venser loop (Spellbook) | Mystical Teachings, Seismic Sense, Recruiter of the Guard | 2 cards, 7 mana: floor 3, review note |
| 3-8 | Etrata, the Silencer + any two of Return the Favor, Peter Parker's Camera, Strionic Resonator, Lithoform Engine | 10 / 32 / 34 | Etrata connects (unblockable); the copies give three hit-counter exiles: that player loses | Adéwalé (Etrata); Reckless Handling and Loyal Inventor (Camera, Strionic, Lithoform); Mystical Teachings (Return the Favor) | 3 cards: no floor |
| 9 | Dualcaster Mage + Starfall Invocation (owned) | 35 | Spellbook copy loop (infinite enters and deaths) | Mystical Teachings, Recruiter of the Guard | 2 cards, 8 mana: floor 3, review note |
| 10 | Dualcaster Mage + Ember Island Production (owned) | 36 | Infinite token copies of Dualcaster | Mystical Teachings, Recruiter of the Guard | 2 cards, 8 mana: floor 3, review note |
| 11 | Kiki-Jiki + Intruder Alarm | 40 | Infinite hasty tokens of any non-legendary creature | Recruiter of the Guard, Seismic Sense, Entomb + Restart Sequence (cut at 44), Diabolic Intent | 2 cards, 8 mana: floor 3 |
| 12 | Kiki-Jiki + Dualcaster + Return the Favor | 40 | Spellbook loop, infinite hasty tokens | as 9 and 11 | 3 cards: no floor |
| 13 | Kiki-Jiki + Goblin Bombardment + All-Fates Stalker | 42 | Infinite damage (Spellbook) | Recruiter of the Guard (Kiki), Idyllic (Bombardment) | 3 cards: no floor |
| 14 | Godo + Helm of the Host | 45 | Godo fetches Helm; infinite combats | Godo, Reckless Handling, Loyal Inventor | 2 cards, 10 mana: floor 3 |
| 15 | Kiki-Jiki + Helm of the Host | 45 | Infinite token copies (Spellbook); with Bombardment, damage | as 11 and 14 | 2 cards, 9 mana: floor 3 |
| - | Ezio's own trigger | base | Whispersilk (step 49), Secret Tunnel or Etrata-style evasion; WUBRG at 10 life | Loyal Inventor (Whispersilk) | not a combo |

Kept out on purpose: Joo Dee, Xerex Strobe-Knight and Goblin Welder (early two-card loops with Intruder Alarm: floor 4),
Twinflame / Heat Shimmer (Dualcaster hazard: floor 4), Tree of Perdition (Ezio + Tree, 6 mana: floor 4), Narset's
Reversal with Return the Favor (floor 4). Hullbreaker Horror, Akki Battle Squad and Magister Sphinx would add one or two
lines each but cost 6-7 mana (efficiency); they are fallbacks.

## Mana base (main ladder)
Free base: 10 nonbasic (Command Tower, Brotherhood Headquarters, Concealed Courtyard, Woodland Cemetery, Hinterland Harbor,
Prairie Stream, filters Abstergo / Rumble Arena / White Lotus Hideout, Secret Tunnel) + 25 basics. Purchases (steps 1-20,
8,616 CLP with Lantern): Chromatic Lantern, Exotic Orchard, Survivors' Encampment, Drowned Catacomb, Dragonskull Summit,
Sunken Hollow, Smoldering Marsh, Isolated Chapel, Sulfur Falls, Clifftop Retreat, Fortified Village, Game Trail, Frostboil
Snarl. From 25,000: 35 lands, 22 nonbasic, 13 basics; every land enters untapped or conditionally untapped (check,
battle, reveal and fast lands), none always tapped. Colored symbols
(150,000): B 39 %, U 24 %, R 19 %, W 15 %, G 4 %; land and rock sources B 26, R 17, U 18, W 15, G 14. Expected
Manabase Quality: base 30-45 %, 15,000 60-80 %, 25,000 onward near the 94 % of round 3 (two fewer duals).

## Roles
| Role | Base (step 0) | 150,000 (step 54) |
|---|---|---|
| Lands | 35 (10 nonbasic) | 35 (22 nonbasic) |
| Ramp | 8: Sol Ring, Arcane Signet, Dimir and Boros Locket, Bender's Waterskin, Barrels, Deathcap, Rampant Growth | 8: Sol Ring, Arcane Signet, Chromatic Lantern, Talisman of Dominance, Rakdos Signet, Everflowing Chalice, Fellwar Stone, Deathcap |
| Card flow | 16 (Ezio Blade, Adéwalé, Coastal Piracy, Theater, Rooftop Bypass, Notion Rain, Brainstorm, Faithless Looting, Mishra's Bauble, Kaya and 6 small ones) | 11: Ezio Blade, Adéwalé, Thorn, Queen, Ravenloft, Etrata Deadly Fugitive, Mari, Phyrexian Arena, Tome, Brainstorm, Mishra's Bauble |
| Interaction | 20 (owned removal, Starfall Invocation) | 18: Trophy, Terminate, Utter End, Fatal Push, Infernal Grasp, Fateful Absence, Bitter Triumph, Stroke of Midnight, Sheoldred's Edict, Kolaghan's Command, Mana Leak, Counterspell, Venser, All-Fates Stalker, Royal Assassin, Haytham, Nekrataal, Starfall |
| Tutors | 5: Loyal Inventor, Entomb, Seismic Sense, Restart Sequence, Adéwalé | 10: + Mystical Teachings, Reckless Handling, Godo, Recruiter of the Guard, Idyllic Tutor, Diabolic Intent (Restart Sequence out) |
| Win lines (Spellbook, local bulk) | 1 | 15 |
| Combo pieces | Deadeye, Intruder Alarm, Starfall | 16 (Etrata, 4 copiers, Alarm, Deadeye, Venser, Dualcaster, Ember Island Production, Starfall, Kiki, Bombardment, All-Fates, Godo, Helm) |
| Creatures | 23 | 24 |
| Average mana value (nonland) | 2.59 | 2.81 |

## Fallback per swap (main ladder)
| Step | Buy | CLP | Fallback (CLP) |
|---|---|---|---|
| 1 | Chromatic Lantern | 600 | All-Fates Scroll (350) |
| 2 | Exotic Orchard | 500 | The Mycosynth Gardens (890) |
| 3 | Venser, Shaper Savant | 990 | Hullbreaker Horror (8,360; also an Alarm line) |
| 4 | Mystical Teachings | 450 | Solve the Equation (5,390; reaches Return the Favor only) |
| 5 | Survivors' Encampment | 450 (1 store) | Unclaimed Territory (350) |
| 6 | Drowned Catacomb | 1,190 | Darkwater Catacombs (790) |
| 7 | Dragonskull Summit | 1,190 | Haunted Ridge (1,990) |
| 8 | Etrata, the Silencer | 2,400 (1 store) | no equivalent: move Kiki-Jiki (step 40) up; the copiers still copy Ravenloft, Thorn, Godo |
| 9 | Return the Favor | 1,250 (2 stores) | move Strionic Resonator (step 32) up |
| 10 | Peter Parker's Camera | 2,600 (1 store) | move Lithoform Engine (step 34) up |
| 11 | Reckless Handling | 630 | keep Notion Rain; Loyal Inventor still reaches the copiers |
| 12 | Sunken Hollow | 790 | Underground River (1,990) |
| 13 | Smoldering Marsh | 915 | Shadowblood Ridge (590) |
| 14 | Infernal Grasp | 700 | Withering Torment (2,090) |
| 15 | Isolated Chapel | 500 | keep the Plains |
| 16 | Sulfur Falls | 500 | Shivan Reef (690) |
| 17 | Clifftop Retreat | 500 | Battlefield Forge (590) |
| 18 | Fortified Village | 500 | Canopy Vista (590) |
| 19 | Game Trail | 500 | Cinder Glade (790) |
| 20 | Frostboil Snarl | 481 | Frostboil at cardnexus (490) |
| 21 | Thorn of the Black Rose | 350 | Thorn at gameofmagic (570) |
| 22 | Ravenloft Adventurer | 890 | Hooded Assassin (200) |
| 23 | Fateful Absence | 490 | Generous Gift (1,560) |
| 24 | Winter Soldier, Icy Assassin | 490 | Reno and Rude (300) |
| 25 | Desmond Miles | 915 (1 store) | Guildsworn Prowler (500) |
| 26 | Etrata, Deadly Fugitive | 1,210 | Anhelo, the Painter (2,000) |
| 27 | Nekrataal | 400 | Hooded Assassin (200) |
| 28 | Tome of Legends | 490 | Mask of Memory (890) |
| 29 | Bitter Triumph | 490 | Withering Torment (2,090) |
| 30 | Mana Leak | 490 | Arcane Denial (2,840) |
| 31 | Kolaghan's Command | 900 | Rakdos Charm (890) |
| 32 | Strionic Resonator | 7,800 | move Lithoform Engine up (one line fewer) |
| 33 | Queen Marchesa | 1,990 | Agent of the Fates (900) |
| 34 | Lithoform Engine | 6,960 | Akki Battle Squad (5,840; Helm and Kiki lines later) |
| 35 | Dualcaster Mage | 6,200 (2 stores) | Akki Battle Squad (5,840) |
| 36 | Ember Island Production | owned | - |
| 37 | Rakdos Signet | 450 | Dimir Signet (300) |
| 38 | Stroke of Midnight | 300 | Generous Gift (1,560) |
| 39 | Everflowing Chalice | 500 | Talisman of Conviction (890) |
| 40 | Kiki-Jiki, Mirror Breaker | 18,500 (2 stores) | Akki Battle Squad (5,840; Akki + Helm line) |
| 41 | Goblin Bombardment | 4,200 | skip: Kiki + Alarm already wins in combat |
| 42 | All-Fates Stalker | 300 | skip (line 13 needs it) |
| 43 | Sheoldred's Edict | 2,200 | Dismember (4,150) |
| 44 | Godo, Bandit Warlord | 1,590 | Akki Battle Squad (5,840) |
| 45 | Helm of the Host | 7,490 | Brotherhood Regalia (9,960; no line) |
| 46 | Counterspell | 3,300 | Arcane Denial (2,840) |
| 47 | Talisman of Dominance | 2,290 | Talisman of Indulgence (2,490) |
| 48 | Phyrexian Arena | 4,190 | Fact or Fiction (300) |
| 49 | Whispersilk Cloak | 3,290 | Brotherhood Regalia (9,960) |
| 50 | Fellwar Stone | 1,490 | Dimir Signet (300) |
| 51 | Recruiter of the Guard | 8,300 (1 store) | Imperial Recruiter (14,700) |
| 52 | Mari, the Killing Quill | 7,700 | Virtus the Veiled (9,300) |
| 53 | Idyllic Tutor | 14,640 | Grim Tutor (28,990) |
| 54 | Diabolic Intent | 19,580 (2 stores) | Grim Tutor (28,990) |

## The three swaps that matter most
| Swap | CLP | Why |
|---|---|---|
| Venser, Shaper Savant (step 3) | 990 | A second Spellbook line with the owned Alarm for under 1,000 CLP, reached by Mystical Teachings; also flash interaction |
| Etrata + Return the Favor + Peter Parker's Camera (steps 8-10) | 6,250 | The cheapest three-card kill; with Strionic (7,800) and Lithoform (6,960) the same hub makes six lines |
| Kiki-Jiki, Mirror Breaker (step 40) | 18,500 | Three lines at once on hubs already in the list (Alarm, Dualcaster + Return the Favor, Bombardment + All-Fates), four with Helm |

## Owned cards another deck also wants
| Card | Copies owned | Also in | Substitute here (CLP) |
|---|---|---|---|
| Sol Ring | 2 | Azula, Toph | buy a third (1,900, magic4ever) |
| Arcane Signet | 2 | Azula, Toph | buy a third (890, cardnexus) |
| Command Tower | 2 | Azula, Toph | buy a third (500, oasis) |
| Entomb | 1 | Azula | second copy 22,400 (paytowin); cheaper: drop it, Diabolic Intent covers it at 150,000 |
| Loyal Inventor | 1 | Azula | second copy 700 (lacomarca) |

All five sit in both Ezio ladders (main and black-core). Shared purchases with Azula and Toph (Lantern, Orchard, the duals,
Dualcaster, Mystical Teachings, Counterspell, Imperial-style tutors) mostly have 3+ stores; the two-store ones are
Return the Favor, Dualcaster, Kiki-Jiki and Diabolic Intent.

## Wishlist (names the pool does not price)
| Card | Role | Would replace | Why |
|---|---|---|---|
| Tribute Mage | tutor on a body | Reckless Handling | finds Strionic Resonator (mana value 2), Talismans |
| Fabricate | tutor | Reckless Handling | any artifact: Camera, Strionic, Lithoform, Helm |
| Whir of Invention | tutor | Idyllic Tutor | instant artifact to the battlefield |
| Sorin Markov | win line | Deadeye Navigator | Ezio + Sorin (Spellbook, 8 mana, floor 3 with a note) |
| Feign Death | win line | Ember Island Production | Dualcaster + Bombardment + Feign Death (3 cards, 6 mana) |
| Scheming Symmetry | tutor | Diabolic Intent | 1-mana black tutor |
| Dark Petition | tutor | Grim Tutor (fallback, 28,990) | black tutor that refunds mana with spell mastery |
| Open the Armory | tutor | Idyllic Tutor | finds Helm or Whispersilk |

## Black-core variant (owner request, 2026-10-19)
File: `decks/proposals/ezio-auditore-da-firenze.bcore.ladder.txt` (free base + 26 swaps), checked with `ladder.py`:
every step valid, Layer A floor 3, 0 Game Changers.

**Second color: blue.** The Assassin core that does not need red is blue-black (Ezio, Blade of Vengeance, Adéwalé,
Etrata ×2, Lydia, Evie), the combo hubs that fit are blue or colorless (Intruder Alarm with Deadeye and Venser; Etrata
with the colorless copiers Camera, Strionic, Lithoform), and so are the tutors (Mystical Teachings, Loyal Inventor). Red
would bring Godo, Kiki-Jiki and Dualcaster, but those lines need Helm or Kiki (26,000 CLP together) and RRR.

Checkpoints:
| Cap CLP | Step | Cost CLP | Spellbook lines | Main additions |
|---|---|---|---|---|
| 0 | 0 | 0 | 1: Deadeye + Alarm | owned black-blue cards, owned tapped B-X duals |
| 15,000 | 18 | 14,625 | 2: + Venser + Alarm | Lantern, Orchard, Unclaimed Territory, Sunken Hollow, Venser, Mystical Teachings, Etrata, Camera, Thorn, Ravenloft, Nekrataal, Desmond, Etrata Deadly Fugitive, Infernal Grasp, Bitter Triumph, Tome, Reno and Rude, Hooded Assassin |
| 25,000 | 20 | 24,715 | 3: + Etrata + Strionic + Camera | Strionic Resonator, Talisman of Dominance |
| 35,000 | 23 | 34,065 | 5: + Etrata + Lithoform + Camera, Etrata + Strionic + Lithoform | Lithoform Engine, Fellwar Stone, Agent of the Fates |
| 50,000 | 26 | 49,205 | 6: + Ezio + Magister Sphinx | Magister Sphinx, Sheoldred's Edict, Withering Torment |

How the mana base works: 35 lands. Base: Swamp 12, Island 6; blue-black duals that enter tapped (Dismal Backwater,
Temple of Deceit, Serpent's Pass, Murky Sewer); black-and-X tapped duals only for the splash (Scoured Barrens W, Temple of
Malady G, Temple of Malice R, Thriving Moor any); untapped multi-color owned lands (Concealed Courtyard, Woodland
Cemetery); any-color sources (Command Tower, Path of Ancestry, filters Abstergo / Rumble Arena / White Lotus Hideout,
Brotherhood Headquarters for Assassins); Secret Tunnel. Purchases replace only the slowest pieces: Exotic Orchard for Path
of Ancestry, Sunken Hollow for Serpent's Pass, Unclaimed Territory for a Swamp, Chromatic Lantern, Talisman of Dominance
and Fellwar Stone for the 3-mana rocks. Lands that always enter tapped: 9 in the base, 8 from step 2, 7 from step 13.
Stores: 6 up to 35,000, 7 at 50,000 (+ lacomarca for Magister Sphinx); piedrabruja only for Thorn (350; gameofmagic 570,
every checkpoint keeps its step). White, red and green are never cast
regularly: they come from Lantern, Command Tower, Orchard, Arcane Signet, Fellwar, the filters and the three B-X duals,
which is enough for Ezio's late WUBRG payment.

Colored symbols: base B 83 %, U 17 %; 15,000 B 76 %, U 24 %; 50,000 B 73 %, U 25 %, W 1 % (Magister Sphinx, usually cast for
{B}{B} by freerunning). Black stays at or above 73 % at every step. Land and rock sources: B 30, U 19-20, W 9-10, R 8-9,
G 9-10, plus 1-2 lands that make any color for Assassin spells, plus Lantern from step 1.

What it gives up versus the five-color main list: every red and white card (Godo + Helm, the four Kiki lines, the two
Dualcaster lines, Return the Favor, Goblin Bombardment, Queen Marchesa, Haytham, Mortify, Utter End, Fateful Absence,
Stroke of Midnight, Kolaghan's Command, Assassin's Trophy); 6 Spellbook lines at 50,000 instead of 10; one tutor fewer
(no Reckless Handling); counterspells kept out to hold black above 65 %; 7 tapped lands, so the early turns are slower and
Manabase Quality will read lower (Salt penalizes tapped lands). What it gains: black and blue are cast on curve from 30
and 20 sources, the deck is cheaper at every checkpoint, and freerunning {B}{B} is always payable.

Fallbacks (black-core): Etrata, the Silencer and Camera (1 store each): move Strionic and Lithoform up (lines need two
copiers); Venser: Hullbreaker Horror (8,360); Magister Sphinx (2 stores): Mari (7,700, no line); Strionic: Lithoform
first; Thorn: gameofmagic (570); Desmond Miles (1 store): Guildsworn Prowler (500); Sunken Hollow: Darkwater Catacombs
(790); Unclaimed Territory: keep the Swamp; the rest as in the main table.
