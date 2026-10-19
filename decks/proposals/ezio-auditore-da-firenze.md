# Ezio Auditore da Firenze: purchase ladder (Phase 8 step 2, round 1, 2026-10-19)

Ladder: `decks/proposals/ezio-auditore-da-firenze.ladder.txt` (free base + 52 swaps). Checked with
`python -I -X utf8 scripts/ladder.py decks/proposals/ezio-auditore-da-firenze.ladder.txt`: all 53 steps valid (0 INVALID;
100 cards, no reversible card, every purchase with stock > 0, Layer A floor 1 at the base and 3 from step 7, 0 to 2 Game
Changers, 0 extra-turn cards). Prices: `merged-20261019T0300Z.json` (a hint; stock is checked in Phase 9). No power numbers
here: the Commander Salt measurement replaces them.

Layer A note for the main assistant: `check_list.py` prints "commander not recognized" because Ezio is not in
`COMMANDERS` (`scripts/collect_research_data.py`); the target falls back to the default Bracket 3, which is correct, but
commander-specific hazards cannot be attached to Ezio until the slug is added.

## Checkpoints to measure
| Cap CLP | Step | Cost CLP | Stores | Win lines (Spellbook, floor 3) | Tutors that reach them | Main additions |
|---|---|---|---|---|---|---|
| 0 | 0 | 0 | none | none | - | owned Assassin core, 20 interaction, 13 card-advantage pieces |
| 25,000 | 24 | 24,827 | cardnexus, gameofmagic, lacomarca, magic4ever, oasis, piedrabruja | Godo + Helm | Godo, Loyal Inventor, Reckless Handling, Entomb (+ 3 reanimators), Seismic Sense | 16 untapped lands, Chromatic Lantern, monarch x2, initiative |
| 50,000 | 39 | 49,047 | + paytowin | same | same 5 | Bayek, Whispersilk Cloak, Counterspell, Kolaghan's Command, Etrata, Arena, FoF, Tome |
| 75,000 | 43 | 74,047 | same 7 | + Kiki + Intruder Alarm, Kiki + Helm (+ Bombardment) | Kiki: Seismic Sense, Entomb; Alarm: none yet | Kiki-Jiki, Goblin Bombardment, Sheoldred's Edict |
| 100,000 | 46 | 98,587 | same 7 | same 3 | + Imperial Recruiter (Kiki) | Mari, Shivan Reef |
| 150,000 | 50 | 148,797 | same 7 | same 3 | + Gamble (Game Changer 1) | Cover of Darkness, Plaza of Heroes, Underground River |
| 200,000 | 52 | 198,267 | same 7 | same 3 | + Enlightened Tutor (Game Changer 2; Alarm, Helm) | Basim |

Store consolidation: piedrabruja only sells the cheapest Thorn of the Black Rose (350; lacomarca 650) and Frostboil Snarl
(482; cardnexus 490). Dropping it adds 308 CLP: the 25,000 checkpoint then becomes step 23 (24,735, without Nekrataal); the
others keep their step. Shipping (outside the budget): 6 stores at 25,000, 7 from 50,000.

## Strategy and engine
Five-color Assassin tempo, black at the core (80 % of the base's colored pips are B, U or R; B alone 48 %; G and W are
splashes). Ezio is
a 2-mana menace attacker: once he or any Assassin connects, every Assassin spell costs {B}{B} (freerunning).
**Roshan, Hidden Magister** makes every creature an Assassin, so Godo, Kiki-Jiki and the 5-drops also cost {B}{B}, every
creature is paid by Brotherhood Headquarters, and **Ezio, Blade of Vengeance**, Arno Dorian, Mari and Cover of Darkness
apply to the whole team. Card advantage comes from combat (Ezio Blade, Coastal Piracy, Tome, Etrata, Mari), from the crown
(Thorn, Queen Marchesa, Ravenloft's initiative) and from cheap freerunning spells (Eagle Vision, Chain Assassination).

How it wins:
| Line | Cards | From | How | Tutors | Layer A |
|---|---|---|---|---|---|
| A | Godo, Bandit Warlord + Helm of the Host | step 7 | Godo enters and puts Helm onto the battlefield; equip Helm to Godo ({5}); each combat a hasty token Godo enters, attacks for the first time and adds another combat: infinite combats | Godo (Helm), Loyal Inventor and Reckless Handling (Helm), Entomb then Restart Sequence / What Must Be Done / Revelations III (Godo), Seismic Sense, Gamble, Enlightened | 2 cards, 10 mana: floor 3 |
| B | Kiki-Jiki + Intruder Alarm (owned) | step 41 | Kiki copies any non-legendary creature; the token's entry untaps Kiki: infinite hasty tokens, any time | Imperial Recruiter, Seismic Sense, Entomb + Restart Sequence (Kiki), Gamble, Enlightened (Alarm) | 2 cards, 8 mana: floor 3 (late) |
| C | Kiki-Jiki + Helm + Goblin Bombardment | step 42 | Token Kiki (non-legendary) copies itself without end; Bombardment turns each into 1 damage | as A and B | 3 cards: no floor |
| D | Ezio's own trigger | base | Unblockable Ezio (Whispersilk, Secret Tunnel, Assassin Gauntlet tapping a board) hits a player at 10 or less and pays WUBRG; Bayek gives two damage steps | Loyal Inventor (Whispersilk) | not a combo |

Kept out on purpose: Joo Dee, Xerex Strobe-Knight, Goblin Welder and Deadeye Navigator (each is a two-card loop with
Intruder Alarm, the first three early: floor 4); Dualcaster Mage + Ember Island Production (Azula buys Dualcaster, sold by
only 2 stores); Tree of Perdition (Spellbook: Ezio + Tree, 6 mana: floor 4).

## Mana base plan
- Free base: 10 nonbasic (Command Tower, Brotherhood Headquarters, Concealed Courtyard, Woodland Cemetery, Hinterland
  Harbor, Prairie Stream, filters Abstergo / Rumble Arena / White Lotus Hideout, Secret Tunnel) + 25 basics (10/5/4/3/3).
  No owned tapped land is used (Path of Ancestry, Thriving lands, temples, gain lands all stay out).
- 25,000: 15 purchases for 10,087 CLP: Exotic Orchard, Survivors' Encampment, Chromatic Lantern and 12 cheap duals that
  enter untapped (check: Drowned Catacomb, Dragonskull Summit, Sulfur Falls, Clifftop Retreat; battle: Sunken Hollow,
  Smoldering Marsh, Canopy Vista, Cinder Glade; reveal: Fortified Village, Game Trail, Furycalm Snarl, Frostboil Snarl).
  35 lands = 24 nonbasic + 11 basics (Swamp 6, Island 2, Mountain/Plains/Forest 1); every land enters untapped or
  conditionally untapped; land sources per color B 15, U 11, R 12, W 10, G 10 (+3 filters each), plus Lantern.
- Later: colorless filters become untapped duals (Battlefield Forge 50k, Shivan Reef 100k, Underground River 150k) and
  Plaza of Heroes (150k). No shocks or fetches: past about 80 % the main assistant's measurements show little gain.

Expected Manabase Quality (estimates; Salt measures it): base 30-45 %; 25,000 70-90 %; 50,000 and 75,000 75-95 %;
100,000 80-100 %; 150,000 and 200,000 85-100 %. Five colors on basics is the weakest point of the free base.

## Roles
| Role | Base (step 0) | 25,000 (step 24) | End (step 52) |
|---|---|---|---|
| Lands | 35 (10 nonbasic) | 35 (24 nonbasic, 0 tapped) | 35 (25 nonbasic) |
| Ramp and fixing | 8: Sol Ring, Arcane Signet, Dimir and Boros Locket, Bender's Waterskin, Barrels, Deathcap Cultivator, Rampant Growth | 8 (Lantern for Boros Locket) | 7: Sol Ring, Arcane Signet, Chromatic Lantern, Talisman of Dominance, Fellwar Stone, Deathcap Cultivator, Rampant Growth |
| Card advantage | 13 | 15 (+ Thorn, Queen, Ravenloft, Eagle Vision) | 16: Ezio Blade, Coastal Piracy, Theater, Phyrexian Arena, Tome, FoF, Eagle Vision, Thorn, Queen, Ravenloft, Etrata, Mari, Basim, Adéwalé, Evie, Kaya |
| Interaction | 20 (8 cheap instants, Royal Assassin, Haytham, Rooftop Assassin, Decree of Pain, What Must Be Done) | 20 (Infernal Grasp, Nekrataal in) | 20: Trophy, Mortify, Utter End, Murder, Terminate, Chaos Warp, Infernal Grasp, Fateful Absence, Chain Assassination, Sheoldred's Edict, Kolaghan's Command, Counterspell, Kaya, Revelations, Royal Assassin, Rooftop Assassin, Haytham, Nekrataal, Vraska, What Must Be Done |
| Tutors (Spellbook-line reach) | 0 lines | 5 for line A | 9: Godo, Loyal Inventor, Reckless Handling, Entomb, Seismic Sense, Imperial Recruiter, Gamble, Enlightened Tutor, Adéwalé (with Roshan) |
| Win conditions | Ezio trigger, Assassin Gauntlet, Arno | + line A | lines A-D, Bayek, Whispersilk, Cover of Darkness |
| Creatures | 30 | 29 | 24 |
| Average mana value (nonland) | 3.06 | 3.06 | 2.98 |

Curve (nonland cards, MV 1 / 2 / 3 / 4 / 5 / 6+): base 6/14/24/14/4/2; 25,000 5/15/22/16/5/1; end 5/19/19/15/5/1.
Salt counts printed mana value; five cards are cheaper here through freerunning (Eagle Vision 5 -> 2, Chain
Assassination, Restart Sequence and Petty Larceny 4 -> 2, Merciless Harlequin 3 -> 2), and with Roshan out every creature
costs BB after a hit.

## Fallback per swap (if stock fails)
| Step | Buy | CLP | Fallback (CLP) |
|---|---|---|---|
| 1 | Exotic Orchard | 500 | The Mycosynth Gardens (890) |
| 2 | Chromatic Lantern | 600 | All-Fates Scroll (350; fixes itself only) |
| 3 | Drowned Catacomb | 1,190 | Underground River (1,990; move step 50 up) |
| 4 | Dragonskull Summit | 1,190 | Sulfurous Springs (2,090) |
| 5 | Survivors' Encampment | 450 (1 store) | The Mycosynth Gardens (890) |
| 6 | Godo, Bandit Warlord | 1,590 | Godo at lacomarca (1,900); else Akki Battle Squad (5,840; Akki + Helm is also infinite combats, no self-tutor) |
| 7 | Helm of the Host | 7,490 | move Kiki-Jiki + Intruder Alarm (18,600) up; Godo then fetches Whispersilk |
| 8 | Reckless Handling | 630 | Master Piandao (owned; Equipment from the top 4 on attack) |
| 9 | Sunken Hollow | 790 | Darkwater Catacombs (790) |
| 10 | Smoldering Marsh | 915 | Haunted Ridge (1,990) |
| 11 | Sulfur Falls | 500 | Shivan Reef (690; move step 46 up) |
| 12 | Clifftop Retreat | 500 | Rugged Prairie (500) |
| 13 | Fortified Village | 500 | Razorverge Thicket (915) |
| 14 | Game Trail | 500 | Rockfall Vale (1,190) |
| 15 | Furycalm Snarl | 590 | Battlefield Forge (590; move step 39 up) |
| 16 | Frostboil Snarl | 482 | Frostboil at cardnexus (490); else Stormcarved Coast (3,750) |
| 17 | Canopy Vista | 590 | Overgrown Farmland (1,820) |
| 18 | Cinder Glade | 790 | Karplusan Forest (1,600) |
| 19 | Thorn of the Black Rose | 350 | Thorn at lacomarca (650); else Hooded Assassin (200) |
| 20 | Ravenloft Adventurer | 890 | Phyrexian Arena (4,190; move step 31 up) |
| 21 | Infernal Grasp | 700 | Bitter Triumph (490) |
| 22 | Eagle Vision | 700 (1 store) | Fact or Fiction (300; move step 32 up) |
| 23 | Queen Marchesa | 1,990 | Xira, the Golden Sting (1,700) |
| 24 | Nekrataal | 400 (1 store) | Serpent Assassin (300) |
| 25 | Bayek of Siwa | 1,700 (1 store) | Kelsien, the Plague (3,600) |
| 26 | Whispersilk Cloak | 3,290 | Aqueous Form (690) |
| 27 | Talisman of Dominance | 2,290 | Rakdos Signet (450) |
| 28 | Counterspell | 3,300 | Arcane Denial (2,840) |
| 29 | Kolaghan's Command | 900 | Rakdos Charm (890) |
| 30 | Etrata, Deadly Fugitive | 3,600 (1 store) | Anhelo, the Painter (2,000) |
| 31 | Phyrexian Arena | 4,190 | Memory Deluge (490) |
| 32 | Fact or Fiction | 300 | Memory Deluge (490) |
| 33 | Tome of Legends | 490 | Mask of Memory (890) |
| 34 | Winter Soldier, Icy Assassin | 490 | Reno and Rude (300) |
| 35 | Fateful Absence | 490 | Stroke of Midnight (300) |
| 36 | Vraska, the Cutting Glare | 800 (1 store) | Big Game Hunter (750) |
| 37 | Fellwar Stone | 1,490 | Everflowing Chalice (500) |
| 38 | Chain Assassination | 300 | Bitter Triumph (490) |
| 39 | Battlefield Forge | 590 | Rugged Prairie (500) |
| 40 | Kiki-Jiki, Mirror Breaker | 18,600 (2 stores) | Kiki at lacomarca (25,550); else Akki Battle Squad (5,840; second Helm line) |
| 41 | Intruder Alarm | owned | - |
| 42 | Goblin Bombardment | 4,200 | skip: Kiki + Alarm already wins in combat |
| 43 | Sheoldred's Edict | 2,200 | Dismember (4,150) |
| 44 | Imperial Recruiter | 14,700 | Formidable Speaker (23,320) |
| 45 | Mari, the Killing Quill | 9,150 (1 store) | Virtus the Veiled (9,300) |
| 46 | Shivan Reef | 690 | keep White Lotus Hideout |
| 47 | Gamble | 28,050 (2 stores; Toph also buys it) | Gamble at paytowin (33,900) |
| 48 | Cover of Darkness | 12,490 (1 store) | Brotherhood Regalia (9,960) |
| 49 | Plaza of Heroes | 7,680 | City of Brass (15,990) |
| 50 | Underground River | 1,990 | Sunken Ruins (1,790) |
| 51 | Enlightened Tutor | 38,480 | Brotherhood Regalia (9,960) and keep Bender's Waterskin |
| 52 | Basim Ibn Ishaq | 10,990 (1 store) | Edward Kenway (11,990) |

## The three swaps that matter most
| Swap | CLP | Why |
|---|---|---|
| Chromatic Lantern (step 2) with the 14 lands of steps 1-18 | 10,087 in all | Five colors on 25 basics is the free base's weakest pillar; Manabase Quality was worth +1.4 for 7,155 CLP on Azula |
| Helm of the Host (step 7, with Godo at step 6) | 9,080 for both | The first win line, found five ways (Godo fetches Helm himself); Helm also copies Ezio or Queen every combat |
| Kiki-Jiki, Mirror Breaker (step 40) | 18,600 | Two more win lines with the owned Intruder Alarm and the same Helm; copies the ETB Assassins (Thorn, Ravenloft, Nekrataal) the rest of the time |

## Owned cards another deck also wants
| Card | Copies owned | Also in | Substitute here (CLP) |
|---|---|---|---|
| Sol Ring | 2 | Azula, Toph | buy a third (1,900, magic4ever) |
| Arcane Signet | 2 | Azula, Toph | buy a third (890, cardnexus) |
| Command Tower | 2 | Azula, Toph | buy a third (500, oasis) |

Third copies: 3,290 CLP in all, outside this ladder's numbers (ladder.py prices each deck alone). Shared but with enough
copies: Bender's Waterskin (3), Chaos Warp (2), Terminate (2), Murder (4), Fatal Push (3), It'll Quench Ya! (3), Swiftfoot
Boots (2), Rumble Arena (2), Seismic Sense (2), Rampant Growth (4), Barrels (3), Boros Locket (2).

Purchases the other ladders also make (a second copy may cost the next offer): 27 cards, all with 3+ stores except
Talisman of Dominance (2 stores, next 2,690) and Gamble (2 stores, next 33,900); Kolaghan's Command has 3.

## Ranking rationale (no absolute numbers)
- **0**: coherent Assassin core and plenty of interaction, but five colors on 25 basics, three colorless filters and no
  combo: expect the lowest Manabase Quality of the ladder; the biggest single jump should be 0 -> 25,000.
- **25,000**: the whole cheap mana base (no tapped land), Lantern, line A with five tutors, two monarch cards and the
  initiative. Should rank well above the base; the main risk is "too slow for its pieces" (Godo 6, Helm 4 + equip 5).
- **50,000**: no new line; better interaction (Counterspell, Kolaghan's Command, Fateful Absence, Chain Assassination,
  Vraska), more card flow (Arena, FoF, Tome, Etrata) and Ezio's own kill (Whispersilk, Bayek). Smaller step than 25,000.
- **75,000**: lines B and C arrive; Intruder Alarm has no tutor until 150,000, so a "combo with no tutors" cap may appear here.
- **100,000**: Imperial Recruiter reaches Kiki and Mari gives the team deathtouch and card draw: should clear that cap.
- **150,000**: Gamble reaches every piece; Cover of Darkness makes the team evasive; low power per CLP from here.
- **200,000**: Enlightened Tutor (Alarm, Helm) and Basim; the lowest power per CLP of the ladder.

## Assassins still without a price (PayToWin, Game of Magic, Oasis being read)
Not used in the ladder. When priced: **Ramses, Assassin Lord** first (Assassins +1/+1; "if a player who was attacked by
your Assassin loses, you win": Ezio's WUBRG kill becomes a game win; not in Spellbook and not infinite, so Layer A gives
no floor, but check it by hand), then **Achilles Davenport** (anthem, freerunning UB; for Winter Soldier), **Desmond Miles**
(2-drop; for Vraska), **Olivia** and **Aya** (for Theater or Kaya), Altaïr and Layla (low priority).

## Data issue
`Savannah` has a best offer of 975 at paytowin, but the matched product is "Savannah Lions (Retro)" (match "exact"): a
false match in `merged-20261019T0300Z.json`. Not used here; the matcher should be fixed before any deck relies on it.

## Wishlist (not in the pool; do not build on them)
| Card | Role | Would replace | Why |
|---|---|---|---|
| Diabolic Intent | tutor | Gamble (28,050) | 2-mana black tutor to hand, no Game Changer, no random discard |
| Grim Tutor | tutor | Enlightened Tutor (38,480) | 3-mana black tutor for any piece |
| Exquisite Blood | win line | Kiki-Jiki (18,600) | with the owned Enduring Tenacity: two-card infinite drain at 9 mana (floor 3), all black |
| Magister Sphinx | win line | Rakdos, the Muscle | Spellbook: Ezio + Sphinx (9 mana, floor 3) sets a player to 10 for Ezio's trigger; BB with Roshan |
| Stoneforge Mystic | tutor | Reckless Handling | 2-mana Helm or Whispersilk tutor on a body, no random discard |
| Steelshaper's Gift | tutor | Enlightened Tutor | 1-mana Equipment tutor (Helm, Whispersilk) |
| Idyllic Tutor | tutor | Enlightened Tutor | finds Intruder Alarm, Exquisite Blood, Cover of Darkness or Arena |
| Recruiter of the Guard | tutor | Imperial Recruiter (14,700) | finds Kiki-Jiki (toughness 2), Nekrataal, Thorn |
| Isolated Chapel | W/B land | a Plains | the pool has no buyable untapped W/B dual |
| Llanowar Wastes | B/G land | a Forest | the pool has no buyable untapped B/G dual |
| Unclaimed Territory | any color for Assassins | a Swamp | a second Brotherhood Headquarters |
| Talisman of Hierarchy | W/B rock | Bender's Waterskin | 2-mana rock for a missing pair |
| Golgari Signet | B/G rock | Barrels of Blasting Jelly | 2-mana rock for a missing pair |
