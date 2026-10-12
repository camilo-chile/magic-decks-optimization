Model ID: claude-opus-5-5

# Synergy research: Alexios, Deimos of Kosmos (2026-10-11, revised 2026-10-12)

Phase 3 (synergy research), NEW deck: the owner has only the commander card. Revised on 2026-10-12 after the independent verification `synergy-alexios-deimos-of-kosmos-2026-10-11-verification.md`. The response to each finding is the last section.

| Input | Value |
|---|---|
| Card pool | `data/cache/pool_alexios-deimos-of-kosmos.jsonl`: 7,552 Commander-legal cards with identity R or colorless, from the Scryfall oracle bulk file updated 2026-10-11T21:01:56Z |
| Combos | `data/cache/spellbook_alexios-deimos-of-kosmos.json`: **0 variants** (`count: null`), query `card="Alexios, Deimos of Kosmos"`, run 2026-10-11T23:09:01Z |
| Combo cross-check (revision) | Local copy of the Spellbook bulk file `variants.json.gz` (timestamp 2026-10-10T03:11:56Z, version 7.1.9, 114,450 variants), left in the session scratchpad by an earlier session and read offline as data. It was not re-downloaded and its provenance was not re-verified |
| Rules | Snapshot of the 2026-02-09 Wizards update (beta). The 2026-10-12 announcement has not been checked (no network) |
| Not used | Network, EDHREC, prices. Scryfall's `edhrec_rank` field from the local bulk file was read only as a global popularity hint |

## 1. Commander

| Field | Value (from the pool) |
|---|---|
| Name | Alexios, Deimos of Kosmos |
| Cost / MV | {3}{R} / 4 |
| Type | Legendary Creature — Human Berserker, 4/4 |
| Color identity | R (mono-red) |
| Game Changer | no (`game_changer: false`) |

Oracle text (exact):

> Trample
> Alexios attacks each combat if able, can't be sacrificed, and can't attack its owner.
> At the beginning of each player's upkeep, that player gains control of Alexios, untaps it, and puts a +1/+1 counter on it. It gains haste until end of turn.

**What it does**
- Every player controls Alexios on their own turn, and it must attack. It can never attack you (its owner), so on opponents' turns it hits your other opponents; the active opponent picks the target.
- It gets a +1/+1 counter at every upkeep (+4 per round in a 4-player pod) and attacks 4 times per round. It is a self-propelled commander-damage clock that needs no mana from you after it is cast.
- It can't be sacrificed (edicts miss), and the counters stay when control changes.

**How it is usually played** (background knowledge, unverified; no community source was read): a "pass the bomb" politics deck built from goad, symmetric damage (group slug) and equipment that rewards its owner.

**Weaknesses**
- No defense for you: it is tapped from attacking every turn and never blocks for you.
- "Can't attack its owner" protects only you, not your planeswalkers (Chandra, Jeska, Ugin). Assault Suit closes that gap ("can't attack you or planeswalkers you control").
- Opponents choose its target on their turns and can stop the forced attack by tapping it for a cost first (crew, convoke) (rules reading).
- Removal sends it to the command zone and it loses its counters and auras; commander tax rises. Deathtouch or first-strike blockers and fogs blunt it.
- Abilities granted to it, and lifelink, help whoever controls it. Hexproof or shroud gear also stops you from targeting it on opponents' turns (Rogue's Passage, Bolt Bend, Magnetic Theft), and ward makes you pay.
- Mono-red card draw is thin: impulse draw, wheels and equipment triggers have to cover it.

**Rules readings this report relies on.** Scryfall rulings could not be fetched (HTTP 403 for the verifier; this research had no network access), and no Comprehensive Rules text was read. **R1, R2, R4 and R6 therefore remain unverified.** R3 and R7 were confirmed by the verifier from the card text and logic, and R5 and R8 were corrected in this revision.

| # | Reading | Status | Consequence |
|---|---|---|---|
| R1 | Equipment stays attached when the creature changes control. Its own triggered abilities ("Whenever equipped creature…, you draw") belong to the Equipment's controller | **Unverified** (consistent with the card wording) | Swords, Mask of Memory, Sword of the Animist and similar pay **you** on every player's turn. This is the core synergy |
| R2 | A quoted ability granted to the creature (`has "Whenever this creature…"`) belongs to whoever controls the creature | **Unverified** | The Reaver Cleaver, Diamond Pick-Axe, Sticky Fingers, Vibranium Strike Gauntlets, Guild Artisan and Popular Entertainer pay the opponent on that opponent's turn |
| R3 | An "Enchant creature you control" Aura goes to the graveyard when an opponent gains control; plain "Enchant creature" Auras stay attached | Confirmed from text | Super State, Pain for All and Breath of Fury fall off; Shiny Impetus and The Sound of Drums stay |
| R4 | Commander damage is counted per commander, whoever controls it | **Unverified** | Hits on opponents' turns count toward 21 |
| R5 | A token created "tapped and attacking" under a non-active player's control enters the battlefield but does not attack | Rule unverified; consequence corrected | Andúril and Captain's Claws tokens enter **tapped**, so they can't block that turn. Moonsilver Spear's Angel enters untapped and is the real blocker source |
| R6 | "Your commander" triggers (Tome of Legends) fire while an opponent controls Alexios | **Unverified** | Tome of Legends counts every attack |
| R7 | Alexios is still controlled by the previous player when each upkeep begins | Confirmed from logic | Granted "at the beginning of your upkeep" triggers (Tavern Brawler) never fire. Edge case: an effect that hands Alexios back before your upkeep (Homeward Path) lets it fire |
| R8 | Legend rule | Corrected | Kiki-Jiki can't target Alexios. Heat Shimmer, Twinflame, Molten Duplication and Blade of Selves copies die to the legend rule. **Non-legendary copies** come from Helm of the Host, Tempestra, Dame of Games, Delina, Wild Mage and Hall of Mirrors (an Attraction). Mirror Box, Mirror Gallery and Hall of Echoes switch the legend rule off, so any copy effect plus one of them needs a combo check in Phase 4 |

## 2. Archetypes

| # | Archetype | Key package (pool cards) | Bracket 3 fit | Speed |
|---|---|---|---|---|
| A | **Equipment hand-off (recommended primary)** | Sword of Fire and Ice, Sword of the Animist, Mask of Memory, Tome of Legends, Shiny Impetus, Commander's Plate, Brotherhood Regalia, Komainu Battle Armor | Comfortable, with the combo exclusions in section 6 | Medium to high (the commander is the clock) |
| B | Goad politics | Disrupt Decorum, Vengeful Ancestor, Agitator Ant, Rite of the Raging Storm, Slicer, Hired Muscle, Death Kiss | Comfortable | Medium |
| C | Damage-doubler group slug | Dictate of the Twin Gods, Furnace of Rath, Jeska, Thrice Reborn, The Sound of Drums, Spectacular Showdown, Kediss, wheels | Within the rules, but speed risk is high | High |
| D | Helm army and extra combats | Helm of the Host, Relentless Assault, Seize the Day, Overpowering Attack, Genji Glove | Drifts toward 4: Helm goes infinite with 10 mono-red partners, and combats get chained | Very high |

- **A, equipment hand-off.** Equip on your turn and the gear stays on as Alexios travels (R1, unverified). Every Sword, Mask, Lens or Spear trigger then fires up to 4 times per round for you, with no extra mana. This turns Alexios's forced attacks into ramp (Sword of the Animist, Shiny Impetus), cards (Mask, Sword of Fire and Ice, Tome) and removal (Argentum Armor, Jitte). Protection and evasion gear (Commander's Plate, Brotherhood Regalia, Boots, Champion's Helm, Mithril Coat) keeps the engine running. Equipment tutors (Reckless Handling, Maximus, Knight Apparent) improve consistency. It is the most consistent plan and the one that best fits "strong synergy and card quality" for Bracket 3.
- **B, goad politics.** Opponents are pushed to attack each other while Alexios never hits you. It is slower and grindy and has the lowest speed risk. Its best pieces (Komainu Battle Armor, Disrupt Decorum, Vengeful Ancestor) add defense to A.
- **C, damage doublers.** Symmetric doublers are lopsided here because Alexios's damage always goes to opponents. Stacking them makes the clock very fast (section 7). Use it only as a light layer (1 or 2 multipliers).
- **D, Helm army and extra combats.** Each Helm token is another Alexios that is passed around and grows, but Helm is a combo hub (section 6), and stacked extra combats raise the speed risk sharply. Not recommended for Bracket 3.

**Recommendation:** A as the primary plan, with B's goad and protection pieces and at most 1 or 2 damage multipliers from C. Spectacular Showdown is the default single multiplier. Decide the multiplier cap in Phase 4 (section 8).

## 3. Candidate cards by role

220 candidates in 10 roles, every name checked by script against the pool (see Verification). Tiers: 15 core, 83 strong, 95 situational, 27 budget alternatives. This revision added 28 cards and dropped 3 that help opponents (Fumiko the Lowblood, Ellie, Brick Master and Goblin Spymaster, now in the hazards).

A "budget alternative" is a functional substitute only: no price is known before Phase 7, so "cheaper" is an unverified guess. GC = Game Changer flag from the pool. A local Spellbook bulk check found **no Spellbook combo made only of candidates**, but 45 two-card combos pair a candidate with a non-candidate, and all 45 partners are excluded in section 5.

Suggested skeleton for the Phase 4 reference build (a starting point only): 36 lands, about 10 ramp, 10 card advantage, 8 interaction, 3 wipes, 6 protection, 16 equipment and payoffs, 2 tutors, 4 goad, 3 finishers, plus 1 flex slot.

### Ramp (31)

| Card | GC | Tier | Why it fits Alexios |
|---|---|---|---|
| Sol Ring |  | core | Fastest rock; Alexios on turn 2 or 3 |
| Arcane Signet |  | core | Two-mana rock, always red here |
| Fellwar Stone |  | strong | Two-mana rock (any color an opponent's land makes) |
| Mind Stone |  | strong | Two-mana rock that cashes in for a card late |
| Thought Vessel |  | strong | Two-mana rock plus no hand size limit for Tome/Mask draws |
| Prismatic Lens |  | budget alternative to Arcane Signet | Two-mana rock |
| Coldsteel Heart |  | budget alternative to Arcane Signet | Two-mana rock (enters tapped) |
| Fire Diamond |  | budget alternative to Arcane Signet | Two-mana red rock |
| Commander's Sphere |  | situational | Three-mana rock that cycles itself |
| Thran Dynamo |  | strong | Three colorless; pays equip costs |
| Worn Powerstone |  | budget alternative to Thran Dynamo | Two colorless (enters tapped) |
| Everflowing Chalice |  | situational | Scalable rock |
| Ruby Medallion |  | situational | Cuts red spells by 1; equipment are colorless, so weaker here |
| Sword of the Animist |  | core | Its trigger is yours: a basic land on every Alexios attack, every player's turn |
| Bitterthorn, Nissa's Animus |  | budget alternative to Sword of the Animist | Same land-per-attack trigger; equip {3} |
| Sceptre of Eternal Glory |  | strong | Taps for three with three Mountains |
| Explorer's Scope |  | situational | Land drop on every Alexios attack, only if the top card is a land |
| Shiny Impetus |  | core | Aura stays when Alexios changes hands; you get a Treasure on every attack |
| Curse of Opulence |  | strong | Gold whenever the cursed player is attacked; the attacking opponent gets Gold too |
| Pip-Boy 3000 |  | strong | On every attack: untap two lands, a +1/+1 counter, or loot |
| Goldvein Pick |  | budget alternative to Shiny Impetus | Treasure per Alexios hit on any turn |
| Prying Blade |  | budget alternative to Shiny Impetus | Treasure per Alexios hit on any turn |
| Solemn Simulacrum |  | strong | Land plus a card; blocker |
| Burnished Hart |  | budget alternative to Solemn Simulacrum | Two lands for 3+3 |
| Wayfarer's Bauble |  | situational | Cheap land ramp |
| Jeska's Will | yes | core | Game Changer: mana burst plus 3 cards (both modes when you control Alexios) |
| Ancient Tomb | yes | situational | Game Changer: fast colorless mana; only if a GC slot is free |
| Big Score |  | strong | Instant: two cards and two Treasures |
| Unexpected Windfall |  | strong | Instant: two cards and two Treasures |
| Pirate's Pillage |  | budget alternative to Unexpected Windfall | Sorcery version |
| Seize the Spoils |  | budget alternative to Big Score | Two cards and one Treasure |

### Card advantage (34)

| Card | GC | Tier | Why it fits Alexios |
|---|---|---|---|
| The One Ring | yes | strong | Game Changer: protection turn plus a growing draw engine |
| Tome of Legends |  | core | Page counter whenever your commander attacks, under any controller |
| Furious Rise |  | strong | Card each of your end steps while you control 4-power Alexios |
| Endless Atlas |  | strong | Draw engine that is always on in a Mountain base |
| Strength-Testing Hammer |  | situational | Draw on attack if Alexios has the greatest power |
| Dream-Thief's Bandana |  | situational | Steal the victim's top card on each hit |
| Glamdring |  | situational | Free instant or sorcery from hand on each hit |
| Mask of Memory |  | strong | Draw 2, discard 1 per Alexios hit; the trigger is yours on every turn |
| Rogue's Gloves |  | budget alternative to Mask of Memory | Draw a card per Alexios hit |
| Infiltration Lens |  | strong | Draw 2 whenever Alexios is blocked (chump blocks are common) |
| Buster Sword |  | strong | Draw plus a free spell from hand on each hit, even on opponents' turns |
| Zephyr Boots |  | strong | Flying evasion plus loot per hit |
| Paleontologist's Pick-Axe // Dinosaur Headdress |  | situational | Loot on every attack |
| Court of Embereth |  | strong | Monarch; Alexios can't attack you, so the crown is safer |
| Emberwilde Captain |  | strong | Monarch plus punishes players who attack you |
| Crimson Fleet Commodore |  | budget alternative to Emberwilde Captain | Monarch on a trampler |
| Trailblazer's Torch |  | strong | Initiative; on Alexios it hurts every blocker |
| Loot Dispute |  | situational | Initiative plus Treasures |
| Caves of Chaos Adventurer |  | situational | Initiative on a body |
| Light Up the Stage |  | strong | Spectacle {R} after Alexios hits on your turn |
| Reckless Impulse |  | situational | Impulse draw 2 |
| Wrenn's Resolve |  | situational | Impulse draw 2 |
| Valakut Exploration |  | situational | Landfall card flow; pairs with Sword of the Animist |
| Outpost Siege |  | strong | Khans: an extra card every upkeep |
| Fable of the Mirror-Breaker // Reflection of Kiki-Jiki |  | strong | Treasure and filtering; combo hub with Combat Celebrant (kept excluded) |
| Seasoned Pyromancer |  | strong | Filters dead cards into tokens |
| Chandra, Torch of Defiance |  | strong | Card or mana each turn; Alexios can still attack your planeswalkers |
| Faithless Looting |  | situational | Cheap filtering |
| Wheel of Fortune |  | situational | Refill; group-slug variant only |
| Reforge the Soul |  | situational | Refill; miracle {1}{R} |
| Magus of the Wheel |  | situational | Repeatable wheel on a body |
| Will of the Jeskai |  | situational | Wheel to five plus flashback when you control Alexios |
| Professional Face-Breaker |  | situational | Treasures and impulse draws on your own turn only |
| Monastery Raid |  | situational | Freerunning: cheap impulse draw after Alexios connects |

### Interaction / removal (21)

| Card | GC | Tier | Why it fits Alexios |
|---|---|---|---|
| Chaos Warp |  | core | Red's catch-all answer to any permanent |
| Vandalblast |  | core | One artifact, or all of opponents' artifacts |
| Abrade |  | strong | Instant: 3 to a creature or kill an artifact |
| Lightning Bolt |  | strong | Efficient instant removal |
| Untimely Malfunction |  | strong | Artifact kill, redirect, or no-block on any turn |
| Wild Magic Surge |  | strong | Instant kill of any opponent permanent; they get a random permanent of a shared type |
| Flame Slash |  | situational | 4 damage to a creature for {R}; sorcery |
| Fiery Confluence |  | strong | Flexible: sweep small creatures, burn, or artifacts |
| Tibalt's Trickery |  | situational | Red's only hard counter |
| Pyroblast |  | situational | Answers blue spells and permanents |
| Red Elemental Blast |  | budget alternative to Pyroblast | Answers blue spells and permanents |
| Meteor Golem |  | situational | Colorless removal of any nonland permanent |
| Ugin, the Ineffable |  | strong | Removal plus card flow |
| Fury |  | strong | Free evoke removal or a double striker |
| Trumpeting Carnosaur |  | strong | Discover 5 or discard for removal |
| Umezawa's Jitte |  | strong | Counters on every Alexios hit; spend them as removal |
| Argentum Armor |  | strong | Destroy a permanent on every Alexios attack, every turn |
| Ultima Weapon |  | situational | +7/+7 and kills a creature per attack |
| Sword of Sinew and Steel |  | situational | Kills an artifact and a planeswalker per hit |
| Inferno Titan |  | situational | Repeatable burn |
| Brash Taunter |  | situational | Indestructible defense that punishes |

### Board wipes (15)

| Card | GC | Tier | Why it fits Alexios |
|---|---|---|---|
| Blasphemous Act |  | core | Cheap sweeper; Alexios survives at 14+ toughness |
| All Is Dust |  | strong | Colored permanents are sacrificed; Alexios can't be, and colorless gear stays |
| Chain Reaction |  | strong | Scales with board size; Alexios usually survives |
| Anger of the Gods |  | strong | Exiles small creatures |
| Storm's Wrath |  | strong | 4 to each creature and planeswalker |
| Mizzium Mortars |  | strong | Spot removal or a one-sided overload |
| Delayed Blast Fireball |  | strong | One-sided; 5 damage if foretold |
| Hour of Devastation |  | situational | Hits indestructible boards |
| Burn Down the House |  | situational | 5-damage sweep or tokens |
| Brotherhood's End |  | situational | Small creatures or cheap artifacts |
| Spiteful Banditry |  | situational | Scalable sweep plus Treasures |
| Star of Extinction |  | situational | 20 damage to each creature |
| Slagstorm |  | budget alternative to Anger of the Gods | 3 to each creature |
| Sweltering Suns |  | budget alternative to Anger of the Gods | 3 to each creature; cycles |
| Kozilek's Return |  | situational | Instant-speed sweep of small creatures |

### Protection (20)

| Card | GC | Tier | Why it fits Alexios |
|---|---|---|---|
| Swiftfoot Boots |  | core | Hexproof plus haste; hexproof also blocks your own targeting on opponents' turns |
| Commander's Plate |  | core | +3/+3 and protection from white, blue, black and green |
| Brotherhood Regalia |  | strong | Unblockable plus ward {2}; equip legendary {1} |
| Lavaspur Boots |  | budget alternative to Swiftfoot Boots | Haste plus ward {1}; equip {1} |
| Thran Power Suit |  | situational | +1/+1 per attached gear plus ward {2} |
| Not of This World |  | situational | Free counter for 7-power Alexios on your turn |
| Assault Suit |  | situational | Stops Alexios attacking your planeswalkers; +2/+2 |
| Champion's Helm |  | strong | +2/+2 and hexproof on a legendary creature |
| Mithril Coat |  | strong | Flash indestructible, auto-attaches to a legendary creature |
| Darksteel Plate |  | budget alternative to Mithril Coat | Indestructible |
| Whispersilk Cloak |  | strong | Unblockable every turn; shroud blocks later equips |
| Hammer of Nazahn |  | strong | Auto-attaches new equipment; indestructible |
| Lightning Greaves |  | situational | Shroud stops you equipping more gear |
| Leather Armor |  | situational | Ward {1} for equip {0}; no haste |
| Kaldra Compleat |  | situational | Indestructible +5/+5 package; expensive equip |
| Deflecting Swat |  | strong | Free redirect on your turn (you control a commander then) |
| Bolt Bend |  | strong | Costs {R} on your turn (you control 4-power Alexios) |
| Redirect Lightning |  | budget alternative to Deflecting Swat | One-mana redirect |
| Return the Favor |  | situational | Redirect or copy |
| Shadowspear |  | situational | Trample plus removes hexproof/indestructible; lifelink helps whoever controls Alexios |

### Engines / payoffs (53)

| Card | GC | Tier | Why it fits Alexios |
|---|---|---|---|
| Sword of Fire and Ice |  | core | Ping plus a card on every Alexios hit, every turn |
| The Spear of Leonidas |  | strong | Each attack: double strike, a Horse token, or loot |
| Mjölnir, Storm Hammer |  | situational | Each attack stuns a creature and burns each opponent |
| Bloodforged Battle-Axe |  | situational | Copies itself on every hit; re-equip costs {2} each |
| Hero's Blade |  | situational | +3/+2; attaches free when Alexios enters |
| Tempestra, Dame of Games |  | situational | Non-legendary Alexios copy; its sacrifice clause can't remove it |
| Delina, Wild Mage |  | situational | Temporary non-legendary Alexios copies on your attacks |
| Sword of Feast and Famine |  | strong | Untap your lands on every hit (instant-speed mana on opponents' turns) |
| Sword of War and Peace |  | strong | Extra damage equal to the victim's hand on every hit |
| Sword of Truth and Justice |  | strong | Each hit: proliferate adds a counter to Alexios (two on your turn) |
| Sword of Hearth and Home |  | situational | Ramp plus a blink of your own creature per hit |
| Sword of Light and Shadow |  | situational | Recursion plus life per hit |
| Sword of Body and Mind |  | situational | Wolf token plus mill 10 per hit |
| Sword of Wealth and Power |  | situational | Treasure per hit; copies an instant |
| Sword of Once and Future |  | situational | Surveil plus free cheap spell from graveyard per hit |
| Sword of Forge and Frontier |  | situational | Impulse 2 per hit; best on your own turn |
| Sword of Hours |  | budget alternative to Sword of Truth and Justice | Extra +1/+1 counter on every attack |
| Armory of Iroas |  | budget alternative to Sword of Truth and Justice | Extra +1/+1 counter on every attack |
| Komainu Battle Armor |  | strong | Each hit goads the victim's whole board away from you |
| Quietus Spike |  | strong | Deathtouch plus trample; each hit halves a life total |
| Scytheclaw |  | budget alternative to Quietus Spike | Each hit halves a life total |
| Blackblade Reforged |  | strong | +1/+1 per land for equip {3} on a legend |
| Leyline Axe |  | strong | Double strike plus trample; may start on the battlefield |
| Fireshrieker |  | budget alternative to Leyline Axe | Double strike |
| Lizard Blades |  | budget alternative to Leyline Axe | Double strike, reconfigure {2} |
| Embercleave |  | strong | Flash double strike plus trample |
| Two-Handed Axe // Sweeping Cleave |  | strong | Doubles Alexios's power on every attack |
| Mjölnir, Hammer of Thor |  | strong | Doubles all its damage; equip worthy {1} (Alexios qualifies) |
| The Sound of Drums |  | strong | Aura stays on: double combat damage; returns to hand |
| Spectacular Showdown |  | core | Default single multiplier: a permanent double strike counter for 2 mana |
| Helm of the Host |  | strong | Non-legendary hasty Alexios copy each of your combats; combo hub with 10 partners, see section 6 |
| Moonsilver Spear |  | strong | An untapped 4/4 flying Angel for you on every Alexios attack (a real blocker) |
| Andúril, Flame of the West |  | strong | Two 1/1 fliers for you on every attack (they enter tapped) |
| Captain's Claws |  | budget alternative to Andúril, Flame of the West | A tapped 1/1 for you on every attack |
| Grafted Wargear |  | strong | +3/+2 for equip {0}; its sacrifice clause can't hit Alexios |
| Bonesplitter |  | budget alternative to Grafted Wargear | +2/+0 for equip {1} |
| Trusty Machete |  | budget alternative to Grafted Wargear | +2/+1 for equip {2} |
| Colossus Hammer |  | situational | +10/+10; equip {8} |
| Excalibur, Sword of Eden |  | situational | +10/+0, equip legendary {2}; cheaper with many artifacts |
| Genji Glove |  | situational | Double strike; the active player gets an extra combat, but only Alexios is untapped |
| Basilisk Collar |  | situational | Deathtouch plus trample beats chump blocks; lifelink helps whoever controls Alexios |
| Jeska, Thrice Reborn |  | strong | 0: triple Alexios's damage to your opponents until your next turn; low loyalty |
| Kediss, Emberclaw Familiar |  | strong | On your turn Alexios's hit also hits each other opponent; never with Grafted Exoskeleton |
| Death Kiss |  | strong | Doubles power when an opponent's creature attacks another opponent |
| Dictate of the Twin Gods |  | strong | Doubles all damage; Alexios never hits you |
| Furnace of Rath |  | budget alternative to Dictate of the Twin Gods | Doubles all damage |
| Fiery Emancipation |  | situational | Triples only sources you control (your turn) |
| Twinflame Tyrant |  | situational | Doubles only sources you control |
| Bitter Feud |  | situational | Doubles damage between two chosen players |
| Curse of Bloodletting |  | situational | Doubles damage to one player |
| Brass Squire |  | situational | Free equip moves on your turn |
| Armory Automaton |  | situational | Backup body that grabs all equipment |
| Strionic Resonator |  | situational | Copies one of your Sword/Spear/Armor triggers |

### Goad / politics (10)

| Card | GC | Tier | Why it fits Alexios |
|---|---|---|---|
| Disrupt Decorum |  | strong | Goad everything: opponents must attack each other |
| Slicer, Hired Muscle // Slicer, High-Speed Antagonist |  | strong | Second pass-the-bomb threat: goaded double striker |
| Fast Forward |  | situational | Second mass goad; cheaper after you attack |
| Vengeful Ancestor |  | strong | Repeatable goad; goaded attackers ping their controllers |
| Agitator Ant |  | strong | Your end step: each player may add two counters to a creature, which is then goaded |
| Rite of the Raging Storm |  | strong | Each player gets a 5/1 that can't attack you, like Alexios |
| Bothersome Quasit |  | situational | Noncreature spells goad; goaded creatures can't block |
| Baeloth Barrityl, Entertainer |  | situational | Goads smaller creatures; Treasures when goaded ones die |
| Geode Rager |  | situational | Landfall goads a whole board; pairs with Sword of the Animist |
| Kazuul, Tyrant of the Cliffs |  | situational | Taxes attacks against you |

### Win conditions / finishers (6)

| Card | GC | Tier | Why it fits Alexios |
|---|---|---|---|
| Court of Ire |  | situational | Monarch plus 7 damage each upkeep |
| Comet Storm |  | situational | Instant X burn finisher |
| Crackle with Power |  | situational | X burn finisher |
| Overpowering Attack |  | situational | Extra combat; freerunning {2}{R} after Alexios connects (speed driver) |
| Relentless Assault |  | situational | Extra combat (speed driver) |
| Seize the Day |  | situational | Extra combat with flashback (speed driver) |

### Utility / tutors (5)

| Card | GC | Tier | Why it fits Alexios |
|---|---|---|---|
| Reckless Handling |  | strong | Tutors any artifact (a Sword, Helm or Plate); random discard |
| Maximus, Knight Apparent |  | strong | Tutors a 2-mana Equipment (Boots, Animist, Mask, Jitte, Blackblade) |
| Tezzeret, Cruel Captain |  | situational | Tutors a 0-1 mana artifact (Sol Ring, Commander's Plate) |
| Imperial Recruiter |  | situational | Finds Komainu Battle Armor or Lizard Blades |
| Magnetic Theft |  | situational | Instant equip onto Alexios on any turn |

### Lands (25)

| Card | GC | Tier | Why it fits Alexios |
|---|---|---|---|
| Mountain |  | core | Bulk of the mana base; feeds Sword of the Animist and Blackblade |
| Rogue's Passage |  | core | Unblockable Alexios on any turn, unless hexproof or shroud gear is on it |
| War Room |  | strong | Card draw for 1 life (one color) |
| Bonders' Enclave |  | strong | Draw when you control a 4-power creature (Alexios on your turn) |
| Castle Embereth |  | strong | Untapped red source and a pump |
| Sokenzan, Crucible of Defiance |  | strong | Red source that channels into blockers |
| Myriad Landscape |  | strong | Fetches two Mountains |
| Throne of the High City |  | strong | Late monarch from a land slot |
| Valakut Awakening // Valakut Stoneforge |  | strong | Modal land or hand refresh |
| Shatterskull Smashing // Shatterskull, the Hammer Pass |  | strong | Modal land or removal |
| Command Beacon |  | situational | Rescues Alexios from high commander tax |
| Sanctum of Eternity |  | situational | Saves Alexios on your turn |
| Reliquary Tower |  | situational | No hand limit |
| Mines of Moria |  | situational | Untapped with a legend; late Treasures |
| Arena of Glory |  | situational | Haste for Alexios the turn it lands |
| Den of the Bugbear |  | situational | Creature land |
| Spikefield Hazard // Spikefield Cave |  | situational | Modal land or ping |
| Urza's Saga |  | situational | Constructs; fetches Sol Ring, Commander's Plate or Bonesplitter |
| Temple of the False God |  | situational | Late ramp land |
| Maze of Ith |  | situational | Defense against non-Alexios attackers |
| The Lonely Mountain |  | situational | Mountain that makes Dwarves; untapped with equipment |
| Dwarven Mine |  | situational | Mountain that makes a 1/1 |
| Inventors' Fair |  | situational | Artifact tutor with 3+ artifacts |
| Buried Ruin |  | situational | Returns a destroyed key artifact |
| Karn's Bastion |  | situational | Proliferates Alexios's counters on any turn |


**Mana base notes**
- Mono-red: about 36 lands including 2 or 3 modal double-faced cards, mostly Mountains. Sword of the Animist, Bitterthorn, Myriad Landscape, Solemn Simulacrum and Burnished Hart fetch basics. Blackblade Reforged scales with land count, and Sceptre of Eternal Glory and Endless Atlas want three or more Mountains.
- RRR appears on Furnace of Rath and Fiery Emancipation and on the overload costs of Mizzium Mortars and Spectacular Showdown. Otherwise colored demands are light, so about 8 to 10 colorless utility lands are affordable.
- Equip costs are the real mana sink, which favors rocks that make colorless mana in volume (Sol Ring, Thran Dynamo, Sceptre of Eternal Glory).
- Skip fetch lands, Command Tower, Exotic Orchard and Path of Ancestry: in mono-red they are at best a Mountain.

## 4. Game Changers in the pool (15)

Flags are from the 2026-10-11 bulk file; the 2026-10-12 announcement is not reflected (re-check before Phase 4). Bracket 3 allows up to 3 (the commander is not one). Recommendation: **2** (Jeska's Will and The One Ring), and a third only if the optimizer shows real value.

| Card | Verdict | Reason |
|---|---|---|
| Jeska's Will | Worth a slot | Both modes on your turn (you control Alexios): mana plus 3 cards; the best ramp and card advantage in mono-red. Spellbook pairs it with Reiterate (excluded) |
| The One Ring | Worth a slot | Draw engine plus one turn of protection. Spellbook lock combos with Umbilicus, Blood Clock and Obelisk of Undoing (all excluded) |
| Ancient Tomb | Optional third | Fast mana: casts Alexios a turn earlier and raises the speed risk; Wizards lists fast mana under Bracket 4 Game Changers |
| Gamble | Avoid | Tutor with a random discard; this deck has no single card it must find |
| Mana Vault, Grim Monolith, Chrome Mox, Mox Diamond | Avoid | Fast mana: speeds up an already fast clock, which fits the Bracket 4 profile |
| Lion's Eye Diamond, Underworld Breach | Avoid | Combo engines |
| The Tabernacle at Pendrell Vale, Glacial Chasm | Avoid | Lock pieces |
| Field of the Dead | Avoid | Needs 7 or more lands with different names; a Mountain-heavy base rarely gets there |
| Mishra's Workshop | Avoid | Its mana only casts artifacts |
| Panoptic Mirror | Avoid | Repeat-spell engine; an extra-turn risk if it imprints one |

## 5. Bracket 3 hazards

Rules snapshot wording (2026-02-09 beta): mass land denial is cards that "regularly destroy, exile, and bounce other lands, keep lands tapped, or change what mana is produced by four or more lands per player without replacing them". Extra turns must be in "low quantities, not chained or looped". No "intentional *early-game* two-card infinite combos", and "if a combo could frequently come up, it's not the best fit for that bracket". Stax-style lock decks should "bracket up".

**Tutors** have had no restriction since 2025-10-21. The pool has many of them: 65 non-land tutors by this report's regex (the verifier counted 56 with a different regex). The equipment and artifact tutors are now candidates (Reckless Handling, Maximus, Knight Apparent, Tezzeret, Cruel Captain, Imperial Recruiter, Urza's Saga, Inventors' Fair).

Project policy: 1 extra-turn card sets floor 2, and 2 or more is a reject. Opponent control is a review flag (`controlSomeOpponents`).

**The list is not exhaustive.** Layer A must still rely on Spellbook's card flags (`massLandDenial`, `extraTurn`) and on `find-my-combos` / `estimate-bracket` run on the final list. All 131 names below were checked by script: present in the pool, none in the candidate list.

| Group | Pool cards to exclude | Reason |
|---|---|---|
| Mass land denial (37) | Blood Moon, Magus of the Moon, Ruination, From the Ashes (it replaces lands with basics: borderline), Wildfire, Destructive Force, Jokulhaups, Obliterate, Decree of Annihilation, Impending Disaster, Boom // Bust, Keldon Firebombers, Tectonic Break, Thoughts of Ruin, Epicenter, Burning of Xinye, Planetary Annihilation, Apocalypse, Worldfire, Worldslayer, Bend or Break, Devastating Dreams, Tectonic Hellion, Winter Orb, Static Orb, Price of Glory, Zhao, the Moon Slayer, Myojin of Infinite Rage, Quicksilver Fountain, Winter Moon, Rumbling Crescendo, Wake of Destruction, Boil, Boiling Seas, Flashfires, Curse of Marit Lage, Raiding Party | Destroy, sacrifice, keep tapped or change the mana of 4 or more lands per player. Blood Moon and Winter Orb are Wizards' examples. Worldslayer on a creature that attacks every turn wipes the board every turn |
| Land destruction below the threshold (5) | Scorched Earth, Orcish Settlers, Ember Swallower, Rain of Salt, Lavaball Trap | Fewer than 4 lands per player (or scales with X): a judgment call; avoid |
| Stax / lock (13) | Tangle Wire, Smokestack, Trinisphere, Sphere of Resistance, Thorn of Amethyst, War's Toll, Mana Web, Tectonic Instability, Ensnaring Bridge, The Tabernacle at Pendrell Vale, Glacial Chasm, Stranglehold, Silent Arbiter | Taxes, tap-downs and attack locks. Ensnaring Bridge also stops Alexios. Stranglehold and Silent Arbiter are mild (a review flag) |
| Extra turns (10) | Final Fortune, Last Chance, Warrior's Oath, Rise of the Eldrazi, Magistrate's Scepter, Gonti's Aether Heart, Timesifter, Panoptic Mirror, Emrakul, the Promised End (also controls an opponent's turn), Ugin's Nexus | Each extra turn is another Alexios attack. Recommend 0 |
| Opponent control (2) | Mindslaver, The Dominion Bracelet | "You control target player during that player's next turn": a review flag under the Lock / control row |
| Combo pieces (25) | See section 6 | Two-card infinite combats, tokens or mana |
| Spellbook partners of candidates (24) | Grafted Exoskeleton, Emrakul, the Exigent Doom, Umbilicus, Blood Clock, Obelisk of Undoing, Expedited Inheritance, Spiteful Sliver, Pyromancer's Goggles, Dawnsire, Sunstar Dreadnought, Toralf, God of Fury // Toralf's Hammer, Heartless Hidetsugu, Repercussion, Fall of Cair Andros, Bronze Bombshell, Barbarian Outcast, Aetherflux Reservoir, Wrathful Red Dragon, Lurebound Scarecrow, Phyrexian Devourer, Crackdown Construct, Reiterate, Goblin Sharpshooter, Mycosynth Lattice, Sands of Time | Each forms a two-card Spellbook combo with a candidate (section 6). They must never be added while that candidate is in the list |
| Helps opponents (3) | Fumiko the Lowblood, Ellie, Brick Master, Goblin Spymaster | Forced attacks or permanent tokens that can be turned on you |
| Rules traps or redundant (12) | Super State, Pain for All, Breath of Fury (R3); The Reaver Cleaver, Diamond Pick-Axe, Sticky Fingers, Vibranium Strike Gauntlets, Guild Artisan, Popular Entertainer (R2); Tavern Brawler (R7); Blade of Selves (R8); Hexplate Wallbreaker (it untaps all of the active opponent's attackers for an extra combat) | Do not work as hoped, or help opponents |

Extra combats are not a Wizards category (power scale: a review note, not a count). They are listed only as situational finishers; keep them at 2 or fewer (section 7). Genji Glove stays situational: unlike Hexplate Wallbreaker, it untaps only Alexios.

## 6. Combos

**Spellbook file:** 0 variants, `count: null`. The empty result is real: the verifier's live API check shows Alexios with `variantCount: 0`, and the local bulk copy also has 0 variants naming Alexios. The query covers only combos that contain Alexios, so the other 99 cards must still be checked with `find-my-combos` / `estimate-bracket` on the final list (Phase 2 gate). Alexios's give-away text is not a flag by itself (power scale).

**Bulk cross-check:**
- 2,999 commander-legal mono-red or colorless variants.
- **0** whose card pieces are all candidates.
- 45 two-card variants that pair a candidate with a non-candidate; all 45 partners are now excluded.

**Class rule** (power scale): any intentional two-card infinite floors at 3; it floors at 4 when Spellbook `speed >= 3` (about 6 mana or less, or up to 8 only when Spellbook's accuracy flag is false). Speed is shown as a range derived from the bulk field `manaValueNeeded`, because the accuracy flag is hidden.

| # | Cards (Spellbook ID) | Loop | Spellbook tag; speed | Class (power scale) | Action |
|---|---|---|---|---|---|
| 1 | Helm of the Host + Combat Celebrant (1692-2105), Godo, Bandit Warlord (1692-4251), Port Razer (1548-1692), Scourge of the Throne (1405-1692), Akki Battle Squad (1692-4367), Fear of Missing Out (1692-6188), Kiki-Jiki, Mirror Breaker (618-1692), Breath of Fury (1692-3259); plus Bloodthirster and Raphael, Tag Team Tough (oracle text only, not in Spellbook) | A fresh hasty token copy each combat retriggers "first time each turn" or "deals combat damage" extra combats | S (FOMO: R); speed 5–6 | **Floor-4 trigger** | Keep Helm only with all 10 partners excluded |
| 2 | Sword of Feast and Famine + Aggravated Assault (900-3750) (+ Alexios or any creature that connects) | Hit, untap lands, pay {3}{R}{R}, another combat | S; 5–6 | **Floor-4 trigger** | Exclude Aggravated Assault |
| 3 | Neheb, the Eternal + Aggravated Assault (3750-4945) | Postcombat mana pays for the next combat | S; 5–6 | **Floor-4 trigger** | Exclude both |
| 4 | Dualcaster Mage + Twinflame (147-1235), Heat Shimmer (147-2959), Molten Duplication (147-5487) | Infinite hasty copies | S; 3–4 | **Floor-4 trigger** | Exclude all four |
| 5 | Kiki-Jiki + Zealous Conscripts (618-1537) or Combat Celebrant (618-2105); Splinter Twin + Zealous Conscripts (1537-4702) | Copy untaps the copier | R; 5–6 | **Floor-4 trigger** | Exclude all |
| 6 | Fable of the Mirror-Breaker // Reflection of Kiki-Jiki (candidate) + Combat Celebrant (2105-3337--140, needs a mana-dork template); Fable + Zealous Conscripts + Panharmonicon (1537-2397-3337) | Reflection copies Celebrant each combat | E; 5–6 | Floor 3 or more (two cards plus a template) | Fable stays a candidate only while Celebrant and Conscripts stay excluded |
| 7 | Metalworker + Staff of Domination (578-2645), with 3 artifact cards in hand | Staff ({3}: untap a creature, {1}: untap itself) beats Metalworker's 6 mana | S; 5–6 | **Floor-4 trigger** | Exclude both (high risk in an artifact deck) |
| 8 | Kediss, Emberclaw Familiar (candidate) + Grafted Exoskeleton (2822-3681) | Infect commander damage copied to each opponent | S; 5–6; "Each opponent loses the game" | **Floor-4 trigger** (it uses the commander) | Grafted Exoskeleton excluded; it would also turn every Alexios hit into 10+ poison |
| 9 | Basalt Monolith + Rings of Brighthearth (4131-4235) or Forsaken Monument (4131-4547) | Infinite colorless mana | R; 4–6 | **Floor-4 trigger** | Exclude Basalt and partners |
| 10 | Hellkite Charger + Sword of Feast and Famine (900-3398) | Infinite combats | S; 5–6 | **Floor-4 trigger** | Exclude Charger |

- **Other two-card partners of candidates** (all excluded, section 5): The One Ring (3 lock pieces), Sanctum of Eternity (Emrakul, the Exigent Doom), Blasphemous Act and Star of Extinction (Expedited Inheritance and 5 damage loops), Return the Favor (Pyromancer's Goggles), Brash Taunter (2), Twinflame Tyrant, Bitter Feud and Curse of Bloodletting (Heartless Hidetsugu), Assault Suit (4 "draw the game" loops), Lightning Greaves and Grafted Wargear (Crackdown Construct), Jeska's Will (Reiterate), Quietus Spike and Basilisk Collar (Goblin Sharpshooter), Vandalblast (Mycosynth Lattice: mass land denial), Strionic Resonator (Sands of Time), Delina (Kiki-Jiki, Port Razer), Sword of Hearth and Home (Akki Battle Squad), Outpost Siege (Worldfire).
- **For the bracket-fit review (not two-card):** Sword of Feast and Famine + Sword of Hearth and Home + Ardent Elementalist + Seize the Day or Relentless Assault (900-1550-2239-2481 / -2489, tag E) gives infinite combats. Three of its pieces are candidates; Ardent Elementalist is not.

## 7. Speed profile

**Qualitative expectation: high in a pure goldfish, medium in real games.** This cannot be settled without the Monte Carlo script (section 8).

- **The commander alone is the clock.** Cast on your turn 4 in a 4-player pod (no haste, so no attack that turn), never blocked or removed, it attacks 11 times before your turn 7 with power 5, 6, …, 15, for **110 damage** to opponents. That is at least 37 to one opponent, so it kills one by commander damage even if the damage is spread (arithmetic confirmed by the verifier).
- **Real-game brakes:** removal and commander tax, chump blocks (trample only loses the blocker's toughness), and opponents spreading damage on their own turns.

| Package that drives speed | Cards | Effect |
|---|---|---|
| Fast mana | Sol Ring, two-mana rocks, Ancient Tomb (GC), Mana Vault and others (avoid) | Alexios on turn 2 or 3 adds a whole round of attacks |
| Haste enablers | Swiftfoot Boots, Lavaspur Boots, Arena of Glory, Lightning Greaves | An extra attack on the turn it is cast |
| Damage multipliers | Spectacular Showdown, Leyline Axe, Embercleave, Fireshrieker, Lizard Blades, The Spear of Leonidas (double strike mode), Two-Handed Axe, Mjölnir, Hammer of Thor, The Sound of Drums, Dictate of the Twin Gods, Furnace of Rath, Jeska, Thrice Reborn, Death Kiss, Kediss | Each one roughly doubles the damage of every hit, on every turn |
| Life-total shortcuts | Quietus Spike, Scytheclaw, Sword of War and Peace | Shorten kills on high life totals |
| Extra combats | Relentless Assault, Seize the Day, Overpowering Attack, Genji Glove | More hits per turn |

Guidance for Phase 4: favor value, evasion and protection equipment over multipliers. Cap multipliers at 1 or 2 (Spectacular Showdown by default) and extra combats at 2 or fewer until the Monte Carlo says otherwise.

## 8. Open questions and risks for Phase 4

1. **Speed-risk model (decision needed).** A goldfish that ignores opponents will flag Alexios "high" or "very high" from the commander alone. The script must define "threaten lethal" (one opponent or the whole table) and model opponents' removal, chump blocks and target choice on their turns.
2. **Multiplier and extra-combat cap** for the reference list, and how it affects parity with Toph and Azula (Y is relative to each commander).
3. **Helm of the Host:** keep it with the combo-1 partners hard-excluded, or drop it? Bloodthirster + Helm and Raphael + Helm are absent from Spellbook (plausible from text only).
4. **Rules readings R1, R2, R4 and R6 are unverified.** Scryfall rulings returned HTTP 403 and no Comprehensive Rules text was read. R1 (equipment triggers pay the owner) carries the whole primary archetype; confirm it before Phase 4 sign-off.
5. **Spellbook:** the empty Alexios result is confirmed (closed). The other 99 cards still need `find-my-combos` / `estimate-bracket` on the final list; the bulk copy used here is from 2026-10-10 and lacks the `relevant` and two-card flags and the exact speed.
6. **Game Changers:** the 2026-10-12 announcement is today; re-check the 15 pool flags (not done, no network).
7. **Copy effects plus legend-rule removers** (Mirror Box, Mirror Gallery, Hall of Echoes) need a combo check if both are ever proposed.
8. **No prices:** budget alternatives are functional substitutes only.
9. **Community play patterns** are unverified background knowledge; EDHREC was not used by its terms.
10. Not covered: printings and languages (English or Spanish only), and stock (Phases 7 and 9). The verifier noted the collection script may have been edited after its run; re-run it if the cache is reused.

## Verification

Helper scripts are in the session scratchpad. The revision's scripts are in `…/scratchpad/alexios/` (all named `alexios_*`; the original run used `…/scratchpad/alexios_research/`). They are read-only on `data/cache/` and on the local Spellbook bulk copy, run with `python -I` in the `magic-decks` conda env. No network, no package installs, no git writes.

| Step | Command / script | Result |
|---|---|---|
| Pool summary | inline Python over the pool file | 7,552 cards; identity R: 4,801, colorless: 2,751; 15 Game Changers; 0 duplicate names; Alexios `game_changer: false` |
| Spellbook file | read `spellbook_alexios-deimos-of-kosmos.json` | `variants: []`, `count: null` (0 combos) |
| Theme searches | `alexios_q.py <regex>` and `alexios_names.py` (exact-name text dump) | Source of every candidate and hazard; card facts quoted from oracle text only; all cards cited by the verifier re-read |
| Tutor and land-denial scans | inline Python regex over the pool | 65 non-land tutors; 45 land-denial text matches, read one by one (added Curse of Marit Lage and Raiding Party) |
| Candidate validation | `alexios_validate.py` (exact-name lookup) | 220 entries, 220 unique; missing from pool **0**; color-identity violations **0**; duplicates **0**; budget-alternative targets unresolved **0**; Game Changers listed 3 (Jeska's Will, Ancient Tomb, The One Ring) |
| Hazard validation | `alexios_validate.py` | 131 hazard names; missing from pool **0**; overlap with candidates **0** |
| Spellbook bulk cross-check | `alexios_sb_bulk.py`, `alexios_sb_pairs.py` on the local `variants.json.gz` (2026-10-10, 114,450 variants) | All 14 variant IDs cited by the verifier found; 10 oracle-derived pairs confirmed as two-card combos (Breach + LED needs a third card; Bloodthirster and Raphael + Helm absent); 0 variants naming Alexios; 0 variants made only of candidates; 45 two-card variants touching a candidate, with **0** partners left outside the hazard list |
| Speed arithmetic | inline Python | Unanswered Alexios cast on turn 4: 11 attacks before your turn 7, power 5–15, total **110** |
| Report check | `alexios_assemble.py` (re-reads this file) | Candidate rows 220 = data 220; row names not in pool **0**; color-identity violations **0** (rows, hazards and extra cited names); all 131 hazard names and all 15 pool Game Changers named; hazard group counts match the data |

**Summary:** 220 candidate cards listed; all names found in the pool: **yes**; color-identity violations: **0**.

## Response to verification

Each finding was re-checked against the pool oracle text and, for combos, against the local Spellbook bulk copy (section 6). Result: 25 findings confirmed (2 of them only in part), 0 fully disputed, plus 3 extra findings from this re-check.

| Finding | Confirmed / disputed | What changed (or why disputed, with evidence) |
|---|---|---|
| S1 Helm partners incomplete | Confirmed | Bulk has 1405-1692 (Scourge of the Throne) and 1692-4367 (Akki Battle Squad), both tag S. Both added to combo pieces; combo 1 now names all 10 partners |
| S2 Fable + Combat Celebrant | Confirmed | Bulk 2105-3337--140 (needs a mana-dork template, since Reflection costs {1} per copy) and 1537-2397-3337. Added as combo 6; the Fable note now says it is a combo hub |
| S3 Metalworker + Staff of Domination | Confirmed | Bulk 578-2645. Oracle: Staff "{3}, {T}: Untap target creature" and "{1}: Untap this artifact" (4 mana per loop) against Metalworker's 6 mana with 3 artifact cards in hand. Both excluded; combo 7 |
| S4 Missing mass land denial | Confirmed | Added Myojin of Infinite Rage, Quicksilver Fountain, Winter Moon, Rumbling Crescendo, Wake of Destruction, Boil, Boiling Seas and Flashfires (37 in total). Scorched Earth, Orcish Settlers and Ember Swallower went to a new "below threshold" group. The list is now stated as non-exhaustive, with Layer A relying on Spellbook card flags. Spellbook's own card flags could not be read offline (the bulk file has no card flags) |
| S5 Missing extra turns / opponent control | Confirmed | Emrakul, the Promised End and Ugin's Nexus added to extra turns (10). New "Opponent control" group: Mindslaver and The Dominion Bracelet |
| S6 Tutor statement false | Confirmed | This report's regex finds 65 non-land tutors (the verifier found 56). The sentence is rewritten, and the equipment tutors are now candidates |
| S7 R5 / Andúril / Captain's Claws | Confirmed | Oracle: "create two tapped 1/1…" and "tapped and attacking". The R5 consequence and both notes are fixed; Moonsilver Spear is named as the untapped blocker source |
| S8 R8 "only Helm" | Confirmed | Oracle of Tempestra, Delina and Hall of Mirrors ("isn't / not legendary"); Mirror Box, Mirror Gallery and Hall of Echoes switch the legend rule off. R8 rewritten; Tempestra and Delina added as situational; open question 7 |
| S9 Twenty omissions | Confirmed | All 20 re-read in the pool and added with tier and role, plus 5 of the "also worth a look" cards. All Is Dust: Alexios "can't be sacrificed" and colorless gear survives (Board wipes, strong) |
| S10 Power-scale threshold misquoted | Confirmed | The class rule is restated (speed >= 3: about 6 mana or less, or up to 8 only with the accuracy flag false). The combo table now gives the Spellbook tag and a speed range from `manaValueNeeded`; all flagged pairs reach speed 3 or more |
| M1 Blasphemous Act | Confirmed | 13 damage kills toughness 13, so the note now says 14+ |
| M2 Agitator Ant | Confirmed | Note now reads "your end step, each player may" |
| M3 Curse of Opulence | Confirmed | Note now says the attacking opponent gets Gold too |
| M4 Sol Ring | Confirmed | "Alexios on turn 2 or 3" |
| M5 Sword of Truth and Justice | Confirmed | The counter goes on your own creature on opponents' turns; the proliferate adds 1 to Alexios (2 on your turn) |
| M6 Wild Magic Surge | Confirmed | Replacement-permanent downside added |
| M7 RRR costs | Confirmed | Overloads of Mizzium Mortars and Spectacular Showdown added |
| M8 Assault Suit reason | Confirmed | Oracle: "can't attack you or planeswalkers you control". Moved from traps to Protection (situational); its 4 Spellbook "draw the game" partners are excluded. Vibranium Strike Gauntlets (R2) took its trap slot |
| M9 Genji Glove vs Hexplate Wallbreaker | Partly disputed | Genji "untap it" (only Alexios) versus Hexplate "untap each attacking creature" (all of the opponent's attackers): the risks differ. Genji stays situational, with the reason now stated in both places |
| M10 Shroud tiers / anti-synergy | Partly confirmed | Anti-synergy note added to the Swiftfoot Boots and Rogue's Passage rows and to the weaknesses. Tiers kept: Whispersilk Cloak adds "can't be blocked" on every turn, while Greaves adds only haste |
| M11 Showdown in core vs cap | Confirmed | Named as the default single multiplier (sections 2 and 7 and its row) |
| M12 Weak budget pairs | Confirmed | Bitterthorn and Lavaspur Boots are now the budget alternatives; Explorer's Scope, Leather Armor and Flame Slash moved to situational |
| M13 Weak candidates | Confirmed | Ellie, Fumiko and Goblin Spymaster dropped to "Helps opponents". Twinflame Tyrant and Fiery Emancipation were already situational with "your turn only" notes and are kept |
| M14 Four-card combo | Confirmed | Bulk 900-1550-2239-2481 / -2489 (tag E). Listed for the bracket-fit review in section 6 |
| M15 Rules snapshot re-check | Confirmed | Not possible offline; section 4 note and open question 6 |
| Extra: Spellbook partners of candidates | New (this re-check) | 45 two-card variants pair a candidate with a non-candidate. Notable: Kediss + Grafted Exoskeleton (2822-3681, "Each opponent loses the game"; the pool confirms that Exoskeleton grants infect). 24 partners added as a hazard group, and the Kediss note warns against it |
| Extra: more mass land denial | New | Curse of Marit Lage ("Islands don't untap") and Raiding Party (destroys unchosen Plains) added. Rain of Salt and Lavaball Trap went to "below threshold" |
| Extra: Sceptre of Eternal Glory | New | "Add three mana… if you control three or more lands with the same name": ramp, strong |

