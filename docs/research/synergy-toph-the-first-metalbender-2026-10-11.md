Model ID: claude-opus-5-5

# Synergy research: Toph, the First Metalbender (2026-10-11)

Phase 3 (synergy research), slug `toph-the-first-metalbender`. Independent of the owner's current list. Revised 2026-10-12 after an independent verification (`synergy-toph-the-first-metalbender-2026-10-11-verification.md`); changes are listed in the last section.

| Input | Value |
|---|---|
| Card pool | `data/cache/pool_toph-the-first-metalbender.jsonl`, 18,537 Commander-legal cards in R/G/W (Scryfall oracle bulk `updated_at` 2026-10-11T21:01:56Z, manifest run 2026-10-11T23:09:01Z) |
| Combos | `data/cache/spellbook_toph-the-first-metalbender.json`, 1,099 Commander Spellbook variants that contain Toph |
| Rules | Wizards snapshot of 2026-02-09 (beta), from `docs/research/commander-brackets-rules-snapshot.md`; re-check after 2026-10-12 |
| Not used | Network, EDHREC, prices, `data/raw/` |

Labels: **rules background** = Magic comprehensive-rules knowledge, not verifiable from the pool; **background knowledge, unverified** = community knowledge. All card facts below come from the pool's oracle text. The pool's `edhrec_rank` field (a Scryfall bulk field) was used only to sort search output, never as evidence.

## 1. Commander

> **Toph, the First Metalbender** {1}{R}{G}{W}, Legendary Creature — Human Warrior Ally, 3/3. `game_changer: false`.
> "Nontoken artifacts you control are lands in addition to their other types. (They don't gain the ability to {T} for mana.)
> At the beginning of your end step, earthbend 2. (Target land you control becomes a 0/0 creature with haste that's still a land. Put two +1/+1 counters on it. When it dies or is exiled, return it to the battlefield tapped.)"

Color identity: R, G, W.

| Effect | What it means in play |
|---|---|
| Artifacts are lands | Every nontoken artifact that enters is a land entering: landfall triggers on each cast (Spellbook descriptions treat it this way, e.g. variant 4300-5034-6871 lists "Infinite landfall triggers" from recasting Sol Ring). Land counts grow fast (Scute Swarm, Avenger of Zendikar, Greensleeves). |
| "Lands you control" effects reach artifacts | Chromatic Lantern, Joiner Adept, Wrenn and Realmbreaker give them "{T}: Add one mana of any color". Yavimaya, Urborg, Dryad of the Ilysian Grove and Prismatic Omen give them basic land types, so they tap for that color (rules background: basic land types carry intrinsic mana abilities). Every equipment and utility artifact becomes a mana source. |
| Only on the battlefield, only nontoken | Artifact cards in hand or graveyard are not lands: no extra land drops from them, no land recursion (Splendid Reclamation, Life from the Loam). Treasure, Clue and Food tokens are not lands. |
| End-step earthbend 2 | A free hasty 2/2 land creature (or +2 counters on an existing one) every turn. The returned-when-dies clause makes earthbended permanents reusable once per turn: self-sacrificing artifacts (Mind Stone, Burnished Hart, Wayfarer's Bauble), Solemn Simulacrum when it dies, and sacrificed lands such as Inventors' Fair (a repeatable artifact tutor), Urza's Saga, fetch lands and Myriad Landscape. It also makes creature wipes lopsided. |

How it is usually played (background knowledge, unverified): artifact-landfall value with "lands tap for mana" engines, a land-creature army, and, in high-power lists, earthbend-recursion loops. The 1,099 Spellbook variants confirm the loop potential (section 6).

| Weakness | Detail |
|---|---|
| Artifact removal is land destruction for you | Vandalblast overload, the artifact modes of Austere Command and Farewell hit your mana base. |
| Land hate hits artifacts | Single-target land removal can hit artifact-lands; Blood Moon, Magus of the Moon or Zhao (with a counter) make nonbasic lands Mountains, so your artifacts lose their abilities (rules background). |
| Land creatures are creatures | Wipes kill earthbended lands (they return tapped but lose counters and equipment). |
| Slow, unprotected commander | 4 MV, three colors, no evasion or built-in protection (Mithril Coat, Lightning Greaves and Swiftfoot Boots are candidates); the earthbend only happens at end step. |
| Earthbend versus Equipment | An earthbended Equipment becomes a creature and cannot stay attached; artifact creatures made lands are still summoning-sick for granted {T} mana abilities (both rules background, unverified: Scryfall rulings returned HTTP 403). |
| Symmetric land punishers | Ankh of Mishra and Zo-Zu the Punisher damage you for every artifact you cast. |
| Mandatory-loop trap | Caged Sun becomes a land and triggers itself forever: the game is a draw (Spellbook 5175-6871). |

## 2. Archetypes

| # | Archetype | Core idea | Bracket 3 fit |
|---|---|---|---|
| A | **Metal Landfall** (recommended primary) | Cheap artifacts as landfall triggers, lands-tap engines, landfall token makers, team-pump finish | Comfortable if the section 5 exclusions hold |
| B | Earthbend Army | Earthbend creatures, counter doublers, double strike for land creatures | Comfortable; best as a package inside A |
| C | Artifact count / equipment | Equipment on hasty land creatures, artifact-enters damage, 20-artifact Hellkite Tyrant | Comfortable, lower synergy ceiling |
| D | Earthbend recursion combo / lock | Sacrifice outlets plus earthbend recursion, Haru, Mindslaver, The Stasis Coffin, Candelabra | Drifts to Bracket 4: exclude |

**A. Metal Landfall.** Toph turns every rock, bauble and equipment into a land drop that does not use the land drop. Lotus Cobra refunds mana per artifact, Tireless Tracker draws per artifact, Scute Swarm and Avenger of Zendikar scale with land count, and Chromatic Lantern or Yavimaya turn non-mana artifacts into mana. The plan wins through a wide board plus Craterhoof Behemoth, Overwhelming Stampede or Omnath, all telegraphed and disruptable, which matches Wizards' Bracket 3 description. It needs no combo at all.

**B. Earthbend Army.** Toph earthbends every end step; the TLA earthbenders (Toph, Greatest Earthbender gives land creatures double strike; Bumi, Eclectic Earthbender adds two counters to each land creature) and counter enhancers (Hardened Scales and Kami of Whispered Hopes add one more; Branching Evolution and Doubling Season double) grow the land creatures. Inspiring Call and Terrasymbiosis turn the counters into cards. Strong synergy, but it is weak to wipes and to land hate, so it works best as 6-8 slots inside A.

**C. Artifact count.** Sword of the Animist, Sword of Fire and Ice, Sword of Feast and Famine, Blackblade Reforged, Skullclamp and artifact-enters damage (Reckless Fireweaver, Ingenious Artillerist) use the many artifacts. Fine in Bracket 3 but it duplicates A's artifact base with weaker payoffs.

**D. Recursion combo / lock.** 262 of the 400 in-identity Spellbook variants use one of 23 sacrifice outlets (Zuran Orb, Ashnod's Altar, Goblin Bombardment and others) with earthbend recursion; the one-card combos are a damage-proof lock (The Stasis Coffin), opponent control (Mindslaver) and infinite turns (Gonti's Aether Heart). A loop that Spellbook does not list (Emeria Shepherd, section 5) belongs here too. This is where the deck drifts to Bracket 4.

Rough slot shape for the Phase 4 reference (A with a B package; to be tuned there): about 34 real lands, 12-14 artifacts for ramp and landfall, 3-4 lands-tap engines, 8 landfall payoffs, 6 earthbend payoffs, 8 card advantage, 9-10 interaction, 3 wipes, 4 protection, 2-3 finishers.

## 3. Candidate cards by role

217 candidates (v2: 198 minus 5 removed plus 24 added after verification), all checked by script against the pool: names exact, color identity inside R/G/W, `game_changer` false for all (Game Changers are in section 4). Tiers: 21 core, 104 strong, 51 situational, 41 budget alternatives. Against Spellbook only: no subset of them, together with Toph, assembles any of the 1,099 Spellbook variants, with or without a template slot (section 6). That does not prove the list is combo-free: Spellbook missed the Emeria Shepherd loop (section 5), which is why Emeria Shepherd was removed; cards marked "B1 loop piece" are safe only while it stays out. Tiers are synergy judgments, not prices ("likely expensive" notes are unverified hunches).

#### 3.1 Ramp (each nontoken artifact is a landfall trigger) (39)
| Card | Tier | GC | Why it fits Toph |
|---|---|---|---|
| Sol Ring | core | no | 2 mana for 1; as a nontoken artifact it is a land under Toph, so casting it is a landfall trigger |
| Arcane Signet | core | no | Fixes all 3 colors; artifact = landfall trigger |
| Fellwar Stone | strong | no | 2-MV fixer; artifact = landfall trigger |
| Mind Stone | strong | no | Ramp, later sacrifice to draw; if earthbended, sacrificing it kills it and it returns tapped. B1 loop piece (section 5): safe only without Emeria Shepherd |
| Commander's Sphere | strong | no | Fixer that sacrifices itself to draw; earthbend recursion as Mind Stone. B1 loop piece (section 5): safe only without Emeria Shepherd |
| Everflowing Chalice | strong | no | Castable for 0 as a free landfall trigger or kicked as a big rock |
| Thran Dynamo | strong | no | 3 colorless; jumps from 4 to 8 mana |
| Talisman of Conviction | budget alternative to Fellwar Stone | no | R/W rock, 2 MV |
| Talisman of Impulse | budget alternative to Fellwar Stone | no | R/G rock, 2 MV |
| Talisman of Unity | budget alternative to Fellwar Stone | no | G/W rock, 2 MV |
| Boros Signet | budget alternative to Arcane Signet | no | Filter rock R/W |
| Gruul Signet | budget alternative to Arcane Signet | no | Filter rock R/G |
| Selesnya Signet | budget alternative to Arcane Signet | no | Filter rock G/W |
| Lotus Petal | situational | no | 0-MV artifact: free landfall trigger, then one mana. B1 loop piece (section 5): safe only without Emeria Shepherd |
| Wayfarer's Bauble | strong | no | 1-MV artifact (landfall) that fetches a basic (second landfall) |
| Burnished Hart | strong | no | Sacrifice: 2 basics; earthbended it is a land creature, dies and returns tapped to repeat |
| Solemn Simulacrum | core | no | ETB basic land, dies draw; when earthbended and killed it returns, repeating both |
| Mycosynth Wellspring | situational | no | Basic to hand on ETB and on going to graveyard; cheap artifact landfall |
| Lotus Cobra | core | no | Landfall: add one mana of any color; every artifact you cast refunds a mana |
| Tireless Provisioner | core | no | Landfall: Food or Treasure (tokens, so not lands under Toph: no loop) |
| Nissa, Resurgent Animist | strong | no | Landfall mana; second trigger each turn digs for an Elf or Elemental |
| Birds of Paradise | strong | no | 1-drop any-color mana |
| Llanowar Elves | budget alternative to Birds of Paradise | no | 1-drop G |
| Elvish Mystic | budget alternative to Birds of Paradise | no | 1-drop G |
| Sakura-Tribe Elder | strong | no | Sacrifice: basic land onto battlefield (landfall) |
| Nature's Lore | strong | no | Untapped Forest (fetches shocks/duals with Forest type) |
| Three Visits | strong | no | Same as Nature's Lore |
| Farseek | strong | no | Mountain or Plains card (shock/dual/triome) |
| Rampant Growth | budget alternative to Nature's Lore | no | Basic land tapped |
| Cultivate | budget alternative to Nature's Lore | no | 2 basics, one to battlefield |
| Kodama's Reach | budget alternative to Nature's Lore | no | Same as Cultivate |
| Exploration | situational | no | Extra land drop for real lands; artifacts cannot be played as lands (Toph only affects the battlefield) |
| Amulet of Vigor | situational | no | Earthbend returns lands tapped and many lands enter tapped: Amulet untaps them |
| Unwinding Clock | strong | no | Untaps all artifacts (your lands) in each other player's untap step |
| Sword of Feast and Famine | strong | no | On combat damage untap all lands you control, which under Toph is every artifact too |
| Thought Vessel | strong | no | 2-MV rock, no maximum hand size |
| Mox Amber | strong | no | 0-MV landfall trigger; taps for Toph's colors (Toph is legendary); speed note |
| Foundry Inspector | situational | no | Artifact spells cost {1} less: more artifacts, so more landfall, per turn |
| Harrow | strong | no | Instant; sacrifice a land (a spent or earthbended artifact-land, which returns) for two untapped basics |

#### 3.2 Mana engines (give lands, and so your artifacts, a mana ability) (9)
| Card | Tier | GC | Why it fits Toph |
|---|---|---|---|
| Chromatic Lantern | core | no | Lands you control tap for any color, so every nontoken artifact becomes a mana source |
| Dryad of the Ilysian Grove | core | no | Lands are every basic type: artifacts tap for any color (basic-type mana abilities, rules background); extra land drop; artifacts become Mountains for Valakut. B1 loop piece (section 5): safe only without Emeria Shepherd |
| Prismatic Omen | strong | no | Same land-type effect as Dryad for 2 mana. B1 loop piece (section 5): safe only without Emeria Shepherd |
| Joiner Adept | strong | no | Lands have '{T}: Add one mana of any color' on a 2-drop |
| Wrenn and Realmbreaker | strong | no | Same mana static plus +1 animate-land and card selection |
| Greenhouse // Rickety Gazebo | situational | no | Room: lands tap for any color; second door digs two permanents |
| Badgermole Cub | strong | no | ETB earthbend 1; whenever you tap a creature for mana add {G} (earthbended artifact lands with a mana ability are creatures) |
| Nissa, Who Shakes the World | strong | no | Forests add an extra {G} (with Yavimaya every artifact is a Forest); +1 animates and untaps a noncreature land with three counters |
| Dune Chanter | situational | no | Lands you control have '{T}: Add one mana of any color' (fifth lands-tap engine); mill for lands |

#### 3.3 Card advantage (17)
| Card | Tier | GC | Why it fits Toph |
|---|---|---|---|
| Tireless Tracker | core | no | Landfall: Clue; every artifact you cast is a Clue |
| Skullclamp | core | no | Draw 2 when a 1-toughness creature dies: Avenger Plants, Scute Swarm Insects, earthbend-1 lands (Badgermole Cub); Toph's earthbend 2 makes a 3/1 that survives |
| Valakut Exploration | strong | no | Landfall: exile top card, you may play it; artifacts make it fire often |
| Tannuk, Memorial Ensign | strong | no | Landfall: 1 damage to each opponent, draws on the second trigger each turn |
| Garruk's Uprising | strong | no | Trample for the land-creature army; draws with a power 4+ creature |
| Return of the Wildspeaker | strong | no | Draw equal to greatest power among non-Humans (land creatures) or +3/+3 to non-Humans |
| Inspiring Call | strong | no | Draw per creature with a +1/+1 counter (every earthbended land) and indestructible |
| Terrasymbiosis | strong | no | Draw when you put +1/+1 counters on a creature; Toph's end-step earthbend 2 can draw 2 each turn |
| Bitter Work | strong | no | Draw when attacking with power 4+; exhaust earthbend 4 |
| Sylvan Library | strong | no | Selection or life-for-cards every turn |
| Sensei's Divining Top | situational | no | Selection; its draw puts it on top of the library, so each recast is a new landfall trigger (no loop by itself) |
| Shamanic Revelation | strong | no | Draw one per creature; land-creature boards make it large |
| Harmonize | budget alternative to Shamanic Revelation | no | Draw three |
| Seer's Sundial | budget alternative to Tireless Tracker | no | Landfall: pay {2} to draw; itself an artifact |
| Ichor Wellspring | situational | no | Draws on enter and on leaving to graveyard; cheap artifact landfall |
| Sword of Fire and Ice | strong | no | Equipment for hasty land creatures: draw, 2 damage, protection |
| Mishra's Bauble | situational | no | 0-MV landfall trigger with a delayed draw; free self-sacrifice (B1-type piece) |

#### 3.4 Interaction and removal (23)
| Card | Tier | GC | Why it fits Toph |
|---|---|---|---|
| Swords to Plowshares | core | no | 1-mana creature exile |
| Path to Exile | strong | no | 1-mana creature exile |
| Chaos Warp | strong | no | Red answer to any permanent |
| Beast Within | strong | no | Instant answer to any permanent |
| Generous Gift | strong | no | Instant answer to any permanent |
| Stroke of Midnight | strong | no | Nonland permanent removal |
| Get Lost | strong | no | Creature, enchantment or planeswalker removal for 2 |
| Abrade | strong | no | 3 damage to a creature or destroy an artifact |
| Dispatch | budget alternative to Swords to Plowshares | no | Metalcraft exile; the deck runs many artifacts |
| Erode | budget alternative to Swords to Plowshares | no | Creature or planeswalker destruction for W |
| Nature's Claim | strong | no | 1-mana artifact/enchantment removal |
| Wear // Tear | budget alternative to Nature's Claim | no | Artifact and/or enchantment |
| Vandalblast | strong | no | Opponents' artifacts only (overload is one-sided, your artifact-lands survive) |
| Annie Joins Up | strong | no | 5 damage on ETB and legendary creature triggers twice: Toph earthbends twice per end step |
| Bridgeworks Battle // Tanglespan Bridgeworks | strong | no | Modal: fight spell or a land drop |
| Earth Rumble | situational | no | Earthbend 2, then up to one creature you control fights |
| Skyclave Apparition | strong | no | Exiles a nonland, nontoken permanent MV 4 or less |
| Deflecting Swat | strong | no | Free with a commander: redirect removal aimed at Toph |
| Krosan Grip | situational | no | Split-second artifact/enchantment removal |
| Reclamation Sage | situational | no | Artifact/enchantment removal on a body |
| Force of Vigor | strong | no | Up to two artifacts/enchantments, free on an opponent's turn |
| Rip Apart | strong | no | 3 damage to a creature/planeswalker or destroy an artifact/enchantment |
| Fateful Absence | strong | no | Instant creature/planeswalker removal for 2 |

#### 3.5 Board wipes (13)
| Card | Tier | GC | Why it fits Toph |
|---|---|---|---|
| Blasphemous Act | strong | no | Earthbended lands that die return tapped (reminder text), so creature wipes are lopsided |
| Austere Command | strong | no | Pick creature modes; avoid the artifact mode (your artifacts are your lands) |
| Wrath of God | strong | no | Earthbended lands return; Toph can be recast |
| Vanquish the Horde | strong | no | Cheap on big boards; same earthbend asymmetry |
| Hour of Revelation | strong | no | Destroys all nonland permanents: your nontoken artifacts are lands and survive |
| Ondu Inversion // Ondu Skyruins | strong | no | Same nonland asymmetry, and a land when not needed |
| Urza's Ruinous Blast | strong | no | Exiles nonland nonlegendary permanents: Toph (legendary) and your artifact-lands survive |
| Damning Verdict | situational | no | Spares creatures with counters (earthbended lands) |
| Delayed Blast Fireball | strong | no | One-sided 2 (or 5 from exile) damage to opponents and their creatures |
| Fumigate | budget alternative to Wrath of God | no | Wrath plus life |
| Planar Cleansing | strong | no | Destroys all nonland permanents: your artifact-lands survive (Toph dies) |
| Oblivion Stone | situational | no | Colorless nonland wipe; a fate counter saves Toph; earthbended and sacrificed it returns (repeatable wipe engine, review note) |
| Starstorm | situational | no | Instant X damage to each creature; earthbended lands return |

#### 3.6 Protection (12)
| Card | Tier | GC | Why it fits Toph |
|---|---|---|---|
| Heroic Intervention | core | no | All your permanents (artifact-lands included) gain hexproof and indestructible |
| Boros Charm | strong | no | Permanents indestructible, or 4 to face, or double strike |
| Flawless Maneuver | strong | no | Free with a commander: creatures indestructible |
| Akroma's Will | situational | no | Protection or a finisher (double strike, flying) with Toph out |
| Lightning Greaves | strong | no | Shroud/haste for Toph; equip 0 |
| Swiftfoot Boots | strong | no | Hexproof/haste for Toph |
| The Walls of Ba Sing Se | situational | no | Other permanents you control are indestructible |
| Earthshape | situational | no | Instant earthbend 3 plus hexproof/indestructible for smaller creatures and you |
| Tamiyo's Safekeeping | situational | no | One permanent hexproof and indestructible for 1 mana |
| Unbreakable Formation | budget alternative to Flawless Maneuver | no | Creatures indestructible, counters in main phase |
| Marwyn, the Preserver | situational | no | Lands you control have hexproof: covers all your artifacts |
| Mithril Coat | strong | no | Flash indestructible equipment that attaches to Toph on entry |

#### 3.7 Engines and payoffs: landfall and artifact-enters (22)
| Card | Tier | GC | Why it fits Toph |
|---|---|---|---|
| Scute Swarm | core | no | Six or more lands is trivial with artifact-lands: each landfall copies the Swarm |
| Felidar Retreat | core | no | Landfall: 2/2 or team counters + vigilance |
| Avenger of Zendikar | core | no | A Plant per land you control (artifacts count); landfall grows them |
| Ancient Greenwarden | core | no | Land-entering triggers (all your artifact casts) trigger twice |
| Panharmonicon | strong | no | Artifact entering triggers twice, and an artifact entering is a land entering |
| Omnath, Locus of Rage | strong | no | Landfall: 5/5 Elemental; Elemental deaths deal 3 |
| Rampaging Baloths | strong | no | Landfall: 4/4 Beast |
| Emeria Angel | strong | no | Landfall: 1/1 flier |
| Greensleeves, Maro-Sorcerer | strong | no | P/T = lands you control; landfall 3/3 |
| Evolution Sage | strong | no | Landfall: proliferate, grows every earthbended land |
| Bristly Bill, Spine Sower | strong | no | Landfall: +1/+1 counter; doubles counters on creatures |
| Toph, Earthbending Master | strong | no | Landfall: experience counter; earthbend X on attack |
| Reckless Fireweaver | strong | no | Artifact enters: 1 damage to each opponent |
| Ingenious Artillerist | strong | no | Artifacts enter: that much damage to each opponent |
| Weftstalker Ardent | situational | no | Creature or artifact enters: 1 damage to each opponent |
| Retreat to Kazandu | budget alternative to Felidar Retreat | no | Landfall: counter or 2 life |
| Zendikar's Roil | budget alternative to Rampaging Baloths | no | Landfall: 2/2 Elemental |
| Druid Class | budget alternative to Exploration | no | Landfall life, extra land drop, level 3 land creature |
| Mossborn Hydra | situational | no | Doubles its counters on each landfall |
| Moraug, Fury of Akoum | situational | no | Landfall in main phase = extra combat; strong speed driver (review note) |
| Admonition Angel | situational | no | Landfall: exile a nonland permanent while it lives |
| Geode Rager | situational | no | Landfall: goad each creature a target player controls |

#### 3.8 Engines and payoffs: earthbend and land creatures (20)
| Card | Tier | GC | Why it fits Toph |
|---|---|---|---|
| Toph, Greatest Earthbender | core | no | Land creatures you control have double strike; ETB earthbend X |
| Bumi, Eclectic Earthbender | strong | no | On attack, two +1/+1 counters on each land creature |
| Earthbender Ascension | strong | no | Earthbend 2, fetch a basic, landfall counters and trample |
| Badgermole | situational | no | Earthbend 2; countered creatures have trample |
| Earthbending Student | situational | no | Earthbend 2; land creatures have vigilance |
| Toph, the Blind Bandit | situational | no | Earthbend 2; power = counters on your lands |
| Hardened Scales | strong | no | Each earthbend adds one more counter |
| Kami of Whispered Hopes | strong | no | One more counter on any permanent; taps for X mana |
| Branching Evolution | strong | no | Doubles counters on creatures (earthbend counters land after the land becomes a creature) |
| Solid Ground | situational | no | Earthbend 3 and one more counter on any permanent |
| Ozolith, the Shattered Spire | budget alternative to Hardened Scales | no | Artifact (landfall) with the same +1 counter effect |
| Doubling Season | strong | no | Doubles earthbend counters and landfall tokens |
| Sylvan Awakening | situational | no | All lands (artifacts included) become 2/2 indestructible haste attackers |
| Kamahl's Will | situational | no | Instant land army; with commander also fight-removal |
| Embodiment of Insight | situational | no | Land creatures vigilance; landfall animates a land 3/3 haste |
| Rockalanche | situational | no | Earthbend X = Forests (all artifacts with Yavimaya) |
| Sword of the Animist | strong | no | Equipment (a land) for hasty land creatures; fetches a basic on attack |
| Cathars' Crusade | situational | no | Each creature entering (landfall tokens) puts a counter on each creature, land creatures included |
| Steel Overseer | situational | no | Counter on each artifact creature: earthbended artifacts qualify |
| Avatar Kyoshi, Earthbender | situational | no | Earthbend 8 and untap every combat; hexproof on your turn |

#### 3.9 Win conditions (8)
| Card | Tier | GC | Why it fits Toph |
|---|---|---|---|
| Craterhoof Behemoth | strong | no | Team pump by creature count after a wide earthbend/landfall board |
| Overwhelming Stampede | strong | no | Team pump by greatest power (countered land creatures) |
| Valakut, the Molten Pinnacle | situational | no | With Prismatic Omen/Dryad artifacts are Mountains: 3 damage per artifact entering after five other Mountains |
| Kessig Wolf Run | strong | no | Mana sink pump with trample |
| Beastmaster Ascension | budget alternative to Craterhoof Behemoth | no | +5/+5 after seven attacks |
| Zacama, Primal Calamity | situational | no | Untaps all lands (artifacts) on cast; repeatable removal |
| Moonshaker Cavalry | strong | no | Team flying and +X/+X by creature count |
| Blackblade Reforged | strong | no | +1/+1 per land you control (artifacts count); equip Toph for {3} |

#### 3.10 Utility (7)
| Card | Tier | GC | Why it fits Toph |
|---|---|---|---|
| Eternal Witness | strong | no | Regrowth any card |
| Sun Titan | strong | no | Returns MV 3 or less permanents (rocks, Baubles) = repeated landfall |
| Scrap Trawler | situational | no | Artifact chain recursion when artifacts die |
| Titania, Protector of Argoth | situational | no | Land to graveyard = 5/3; earthbended artifact-lands that die still trigger it (combo-adjacent with sac outlets) |
| Strionic Resonator | situational | no | Copy a landfall or Toph trigger |
| Expedition Map | situational | no | 1-MV landfall trigger; fetches Yavimaya, Valakut or Gavony Township |
| Tormod's Crypt | situational | no | 0-MV landfall trigger and graveyard hate; free self-sacrifice (B1-type piece) |

#### 3.11 Lands (47)
| Card | Tier | GC | Why it fits Toph |
|---|---|---|---|
| Command Tower | core | no | Three-color fixing |
| Exotic Orchard | strong | no | Fixing in multiplayer |
| Path of Ancestry | strong | no | Fixing; scry with Human/Warrior/Ally creatures (many earthbenders) |
| Jetmir's Garden | strong | no | RGW triome with basic types (fetchable) |
| Jungle Shrine | budget alternative to Jetmir's Garden | no | Tapped tri-land |
| Stomping Ground | core | no | Shock with Mountain Forest types (fetchable) |
| Sacred Foundry | core | no | Shock with Mountain Plains types |
| Temple Garden | core | no | Shock with Forest Plains types |
| Taiga | strong | no | Untapped dual with types (likely expensive tier, unverified hunch) |
| Plateau | strong | no | Same (likely expensive tier, unverified hunch) |
| Savannah | strong | no | Same (likely expensive tier, unverified hunch) |
| Wooded Foothills | strong | no | Fetch = two landfall triggers; earthbended and cracked it returns tapped (repeatable) |
| Arid Mesa | strong | no | Same as Wooded Foothills |
| Windswept Heath | strong | no | Same as Wooded Foothills |
| Fabled Passage | strong | no | Fetch a basic; two landfall triggers |
| Prismatic Vista | strong | no | Fetch a basic untapped |
| Evolving Wilds | budget alternative to Fabled Passage | no | Two landfall triggers |
| Terramorphic Expanse | budget alternative to Fabled Passage | no | Two landfall triggers |
| Myriad Landscape | budget alternative to Fabled Passage | no | Three landfall triggers; repeatable with Toph's earthbend |
| Rootbound Crag | budget alternative to Stomping Ground | no | Check land |
| Clifftop Retreat | budget alternative to Sacred Foundry | no | Check land |
| Sunpetal Grove | budget alternative to Temple Garden | no | Check land |
| Spire Garden | budget alternative to Stomping Ground | no | Untapped in multiplayer |
| Spectator Seating | budget alternative to Sacred Foundry | no | Untapped in multiplayer |
| Bountiful Promenade | budget alternative to Temple Garden | no | Untapped in multiplayer |
| Cinder Glade | budget alternative to Stomping Ground | no | Typed, fetchable |
| Canopy Vista | budget alternative to Temple Garden | no | Typed, fetchable |
| Rockfall Vale | budget alternative to Stomping Ground | no | Slow land R/G |
| Sundown Pass | budget alternative to Sacred Foundry | no | Slow land R/W |
| Overgrown Farmland | budget alternative to Temple Garden | no | Slow land G/W |
| Karplusan Forest | budget alternative to Stomping Ground | no | Pain land |
| Battlefield Forge | budget alternative to Sacred Foundry | no | Pain land |
| Brushland | budget alternative to Temple Garden | no | Pain land |
| Sheltered Thicket | situational | no | Typed, cycling |
| Slagwoods Bridge | situational | no | Indestructible artifact land: survives artifact wipes, counts for metalcraft |
| Rustvale Bridge | situational | no | Same, R/W |
| Thornglint Bridge | situational | no | Same, G/W |
| Yavimaya, Cradle of Growth | core | no | Each land is a Forest: every artifact you control taps for {G} (Forest mana ability, rules background) |
| Urborg, Tomb of Yawgmoth | strong | no | Each land is a Swamp: every artifact taps for {B} (spend on generic costs) |
| Ba Sing Se | strong | no | Repeatable earthbend 2 at sorcery speed |
| Inventors' Fair | strong | no | Artifact tutor land; repeatable every turn with Toph: earthbend it, sacrifice it (it dies and returns tapped) |
| Spire of Industry | strong | no | Any color with an artifact |
| Boseiju, Who Endures | strong | no | Channel removal on a land slot |
| Urza's Saga | situational | no | Constructs grow with artifact count; fetches a 0/1-cost artifact; if earthbended and killed it returns at chapter I |
| Reliquary Tower | situational | no | No hand limit for draw-heavy builds |
| Rogue's Passage | situational | no | Unblockable for a big land creature |
| Gavony Township | strong | no | Counter on each creature: grows land creatures and tokens; feeds Terrasymbiosis and Inspiring Call |

Mana base notes:
- Artifacts cannot be played as land drops, so keep about 33-35 real lands (background knowledge, unverified); the artifacts add land count for payoffs, not land drops.
- Prefer typed duals (shocks, original duals, Jetmir's Garden, Cinder Glade, Canopy Vista): fetchable by fetches, Nature's Lore, Three Visits and Farseek. Fetches give two landfall triggers.
- Run a few basics: Ba Sing Se enters untapped only with a basic land; Wayfarer's Bauble, Burnished Hart, Solemn Simulacrum and Sakura-Tribe Elder fetch basics.
- With a lands-tap engine out, colorless utility lands cost little, because every artifact taps for colored mana.
- Leave out the bounce lands (Gruul Turf, Selesnya Sanctuary, Boros Garrison, Arid Archway, Guildless Commons): harmless alone, but they are pieces of 60 Spellbook variants with Toph, Hardheaded Teacher (12 each).

## 4. Game Changers in the pool

30 Game Changers are in the pool (same 30 as the manifest). Bracket 3 allows up to 3; Toph is not one, and 0 is valid. Wizards describes Bracket 3 Game Changers as "value engines and game-ending spells" and Bracket 4 ones as "fast mana, snowballing engines, free disruption, tutors", so the value engines are preferred. Prices are unknown until Phase 7.

| Verdict | Game Changers | Why |
|---|---|---|
| Worth a slot (pick up to 3) | The One Ring, Smothering Tithe, Seedborn Muse, Field of the Dead, Teferi's Protection | The One Ring: card engine and cast-protection, indestructible artifact-land. Smothering Tithe: ramp (its Treasures are tokens, so no Toph loop). Seedborn Muse: untaps all your permanents (every artifact-land) in each other player's untap step. Field of the Dead: artifacts give "lands with different names" quickly, so most artifacts or lands entering make a 2/2. Teferi's Protection: phases out your whole board, including artifact-lands, against wipes |
| Possible, review needed | Aura Shards, Gaea's Cradle, Biorhythm | Aura Shards with landfall tokens repeatedly destroys artifacts/enchantments (value, but can feel like a lock against artifact decks). Gaea's Cradle is big mana with land creatures; its only Toph combo needs Candelabra of Tawnos (excluded). Biorhythm is a game-ending spell with a wide board |
| Avoid: fast mana (speed driver) | Ancient Tomb, Chrome Mox, Mox Diamond, Mana Vault, Grim Monolith, Mishra's Workshop | Wizards' Bracket 4 role. Mana Vault and Grim Monolith are Candelabra combo pieces in Spellbook |
| Avoid: tutors | Enlightened Tutor, Worldly Tutor, Gamble, Crop Rotation, Natural Order, Survival of the Fittest | Legal, but a GC slot is better spent on an engine; Natural Order into Craterhoof raises speed |
| Avoid: anti-synergy, stax or combo | Humility, Drannith Magistrate, Glacial Chasm, The Tabernacle at Pendrell Vale, Underworld Breach, Lion's Eye Diamond, Panoptic Mirror, Serra's Sanctum, Jeska's Will, Farewell | Humility makes land creatures 1/1 with no abilities; Glacial Chasm and Tabernacle are lock pieces; Lion's Eye Diamond is in a Spellbook combo with Haru and Retreat to Emeria; Farewell's artifact mode exiles your lands (creature mode only); the rest have little synergy |

## 5. Bracket 3 hazards (exclude)

Wizards wording used: mass land denial = cards that "regularly destroy, exile, and bounce other lands, keep lands tapped, or change what mana is produced by four or more lands per player without replacing them"; extra turns only in "low quantities", "not chained or looped"; no "intentional early-game two-card infinite combos"; stax-style lock decks should "bracket up". The project's Layer A treats any combo that uses the commander as a floor-4 candidate.

| Hazard | Cards in the pool | Reason |
|---|---|---|
| Unregistered commander loop (not in Spellbook) | **Emeria Shepherd** (removed from candidates). Pieces that stay as candidates: Prismatic Omen, Dryad of the Ilysian Grove, and any self-sacrificing artifact (Lotus Petal, Commander's Sphere, Mind Stone, Mishra's Bauble, Tormod's Crypt, Wayfarer's Bauble, Expedition Map, Burnished Hart, Oblivion Stone) | Unbounded mana, cards, landfall and artifact enters (steps below). Floor-4 candidate by project policy (commander combo), and Spellbook-based Layer A cannot see it |
| Mass land denial (non-exhaustive) | Armageddon, Ravages of War, Catastrophe, Jokulhaups, Obliterate, Wildfire, Ruination, Boom // Bust, Impending Disaster, Destructive Force, Keldon Firebombers, Tectonic Break, Planetary Annihilation, Global Ruin, Cataclysm, Cleansing, Fall of the Thran, Natural Balance, Restore Balance, Balancing Act, Devastation, Apocalypse, Decree of Annihilation, Worldfire, Worldslayer, Bearer of the Heavens, Myojin of Infinite Rage, Thoughts of Ruin, Bend or Break, Burning of Xinye, Epicenter, Ajani Vengeant (−7), Wake of Destruction, Price of Glory, Smokestack, Tectonic Instability, Quicksilver Fountain, Blood Moon, Magus of the Moon, Zhao, the Moon Slayer, Winter Orb, Static Orb, Hokori, Dust Drinker, Storm Cauldron, Mana Web, Hall of Gemstone | Wizards' definition (Armageddon, Ruination, Winter Orb, Blood Moon are its own examples); floor 4. Blood Moon effects and Tectonic Instability also cripple your own artifact-lands. Layer A curation should still scan the pool, not rely on this list |
| MLD by combo (Toph-specific) | Mycosynth Lattice; Nature's Revolt, Living Plane | Lattice makes all permanents artifacts, so an artifact wipe (Vandalblast overload, a candidate) destroys opponents' lands (also 37 in-identity Spellbook combos). Nature's Revolt and Living Plane make all lands creatures, so any creature wipe destroys opponents' lands |
| Borderline, review | Nature's Will | Taps a damaged player's lands after your combat damage; they untap in their own untap step, so it does not clearly "keep lands tapped". Not a candidate; flag if added |
| Extra turns | Gonti's Aether Heart, Ugin's Nexus, Magistrate's Scepter, Final Fortune, Last Chance, Warrior's Oath, Chance for Glory, Timesifter, Rise of the Eldrazi, Seedtime, Emrakul, the Promised End, Perch Protection | The first three are infinite-turn combos with Toph (floor 4). The rest are single extra turns (Layer A: 1 card = flag; 2+ = policy reject); Emrakul also controls an opponent's turn, Perch Protection gives the turn to an opponent |
| Two-card combos (commander not counted) | Candelabra of Tawnos, Argothian Elder, Ley Weaver, Springheart Nantuko, Bumi, Unleashed, Liquimetal Torque, Liquimetal Coating, Ashnod's Transmogrant, Silverskin Armor, Thran Forge, Transmogrifying Licid, Blossoming Tortoise, Battered Golem, Bootleggers' Stash | Each completes an infinite with Toph plus one common card (section 6). Excluding them keeps Lotus Cobra, Tireless Provisioner, Nissa, Resurgent Animist and the mana rocks safe |
| Loops with three or more pieces | Staff of Domination, Haru, Hidden Talent, Toph, Hardheaded Teacher, Maskwood Nexus, Meticulous Excavation, Aeon Engine, Magus of the Candelabra, Thousand-Year Elixir | Hubs of deterministic infinites, infinite turns or locks (section 6 gives the verdict per family). Staff of Domination loops with Yavimaya, Cradle of Growth or Urborg, Tomb of Yawgmoth plus a mana doubler; Magus of the Candelabra with Thousand-Year Elixir plus a doubler such as Nissa, Who Shakes the World (a candidate) |
| Sacrifice outlets (23, in 262 variants) | Zuran Orb, Goblin Bombardment, Altar of Dementia, Need for Speed, Lithatog, Thaumatog, Troubled Healer, Trenching Steed (16 each), Ashnod's Altar, Phyrexian Altar, Thermopod (15), Arcbound Ravager, Atog, Megatog, Extruder, Krark-Clan Grunt, Ravenous Intruder (10), Krark-Clan Ironworks (9), Spawning Pit (6), Grinding Station (5), Blasting Station, Sylvan Safekeeper (4), Oxidda Daredevil (1) | Earthbend recursion loops. Not two-card, but if one is wanted, check the final list with `find-my-combos` |
| Haru enablers that look harmless | Firdoch Core (22), Stonework Puma (22, an Ally), Stalactite Dagger (19), Three Tree Mascot (18), Barkform Harvester (18), Bloodline Pretender (18), Universal Automaton (14) | Fine while Haru, Hidden Talent and the outlets stay out; Firdoch Core and Three Tree Mascot read like plain mana rocks |
| Locks / opponent control | Mindslaver, The Stasis Coffin, Glacial Chasm, The Tabernacle at Pendrell Vale, Tangle Wire, Damping Sphere, Defense Grid, Torpor Orb, Cursed Totem | Mindslaver and The Stasis Coffin are one-card locks with Toph (section 6); the rest are stax pieces |
| Self-harm (not a bracket rule) | Caged Sun, Ankh of Mishra, Zo-Zu the Punisher | Draw by mandatory loop; damage to you per artifact |

**Emeria Shepherd loop, checked step by step from oracle text.** Setup: Toph; Prismatic Omen or Dryad of the Ilysian Grove ("Lands you control are every basic land type"); Emeria Shepherd ("Landfall — ... return target nonland permanent card from your graveyard to your hand. If that land is a Plains, you may return that nonland permanent card to the battlefield instead"); self-sacrificing artifacts in the graveyard (in the graveyard they are not lands, so they are legal "nonland permanent card" targets).
1. Any land enters; Shepherd returns artifact A (Lotus Petal) to the battlefield. A is a nontoken artifact, so a land (Toph), and a Plains (Omen).
2. A's entry triggers Shepherd, targeting B (Commander's Sphere). With three pieces, let it resolve while A is still on the battlefield, so the Plains check is plain; B enters and triggers Shepherd, targeting C (Mishra's Bauble). In response, sacrifice A (Petal: one mana).
3. C returns; its trigger targets A. In response, tap B for mana, then sacrifice it (draw). Repeat.

With only two pieces, the land must be sacrificed in response, and the "that land is a Plains" check then relies on last known information (rules background, unverified; Scryfall rulings returned HTTP 403). Each cycle gives at least one mana and one card, plus one landfall and one artifact enter per piece; Reckless Fireweaver, Ingenious Artillerist, Tannuk or Scute Swarm (candidates) turn it into a win. By Wizards' letter it is not a two-card combo; under project policy it is a commander combo (floor-4 candidate). Fix applied: Emeria Shepherd removed; the other pieces are marked "B1 loop piece" in section 3.

**Repeatable engines with Toph's earthbend** (no Layer A rule; note for the bracket-fit review and for tiers): a sacrificed earthbended land dies and returns tapped, so once per turn Inventors' Fair is an artifact tutor, Urza's Saga re-enters at chapter I and fetches a 0/1-cost artifact again, fetch lands and Myriad Landscape give an extra land and 2-3 landfall triggers, Burnished Hart, Wayfarer's Bauble and Expedition Map repeat, and Oblivion Stone repeats a one-sided nonland wipe (Toph dies each time unless it has a fate counter).

Tutors carry no bracket restriction since 2025-10-21. Non-GC tutors that fit (Green Sun's Zenith, Finale of Devastation, Chord of Calling, Eladamri's Call, Inventors' Fair, Urza's Saga) are descriptive statistics only, but each one makes the finishers more reliable (speed, section 7).

## 6. Combos (Commander Spellbook, all variants contain Toph)

The export has `bracketTag` and `manaValueNeeded` but no `relevant`, two-card or `speed` flags (those come only from `estimate-bracket`), so classification below uses the tag, the piece count and the description.

| Count by | Values |
|---|---|
| bracketTag, all 1,099 | E 991, S 57, R 46, P 3, B 2 |
| Pieces besides Toph (cards + template slots), all | 1: 4, 2: 90, 3: 717, 4: 288 |
| Color identity | R/G/W 400; R/G/W/U 169; B/R/G/W 365; five-color 165 (699 need colors Toph cannot use) |
| bracketTag, in-identity 400 | E 333, S 39, R 25, P 3 |
| Pieces besides Toph, in-identity | 1: 4, 2: 52, 3: 274, 4: 70 |
| Features, in-identity | Lock 26, Infinite turns 23, Infinite combat phases 7, Draw the game 2, control of an opponent 1 |

One-card combos (Toph + 1 card):

| Card | Tag | What Spellbook says | Mana | Verdict |
|---|---|---|---|---|
| The Stasis Coffin | S | Earthbend the Coffin at end step, pay {2}, tap and exile it, it returns; "protection from everything during your opponents' turns", "Prevent all damage that would be dealt to you", "Lock" | {2} each turn | **Unclear, recommend exclude.** Repeats every turn; opponents cannot target or damage you. It does not lock others out of their own turns, but Spellbook flags it `lock` (review flag in Layer A) and project policy reviews every commander combo as floor 4. Keeping it means arguing it in the bracket-fit review |
| Mindslaver | R | Earthbended Mindslaver is sacrificed, returns, repeat: "You control one opponent on each of their turns", "Lock" | 6 to cast, {4} each turn | **Floor-4 trigger, exclude.** Control of an opponent's turn every turn is a lock; tag R |
| Gonti's Aether Heart | R | Exile for an extra turn, earthbend returns it: "Infinite turns", "Lock" | 6 energy per turn | **Floor-4 trigger, exclude** (infinite-turn chain) |
| Caged Sun | R | Its own trigger is "a land's ability" under Toph: mandatory infinite loop, "Draw the game" | 0 | **Exclude** (not a win; ends the game in a draw) |

Two-card combos (Toph + 2 cards) relevant to an R/G/W build; all are floor-4 candidates under the project's two-card predicate (`relevant` unknown from the export; most need 0-4 mana):

| Family (in-identity variants) | Pieces | Result | Tag |
|---|---|---|---|
| Candelabra of Tawnos (24) | Candelabra + any rock or land making 2+ mana (Mana Vault, Grim Monolith, Basalt Monolith, Thran Dynamo, Everflowing Chalice, Gilded Lotus, Coveted Jewel, Gaea's Cradle, Serra's Sanctum, Lotus Field, Nykthos, Shrine to Nyx, ...) | Infinite mana | S/P/E |
| Untap-two-lands creature (15) | Argothian Elder or Ley Weaver + an artifact-maker (Liquimetal Torque, Liquimetal Coating, Ashnod's Transmogrant, Silverskin Armor, Thran Forge, Mycosynth Lattice, ...), or Ley Weaver + Marvin, Murderous Mimic (which copies its ability) | Infinite mana | S |
| Bumi, Unleashed (7) | Bumi, Unleashed + Liquimetal Torque, Liquimetal Coating, Mycosynth Lattice, Ashnod's Transmogrant, Silverskin Armor, Thran Forge or Transmogrifying Licid | Infinite combat phases | E (tagged low, but MV 0-2 and two cards) |
| Springheart Nantuko (4) | Nantuko + Lotus Cobra, Tireless Provisioner, Nissa, Resurgent Animist or Stone-Seeder Hierophant | Infinite landfall | S |
| Others (2) | Blossoming Tortoise + Basalt Monolith; Battered Golem + Bootleggers' Stash | Infinite mana / Treasures | S |
| Outside identity or banned | Meloku the Clouded Mirror (blue) + Sol Ring, Mana Vault or Grim Monolith; Overburden (blue) + 0-MV artifact creature; Mana Crypt, Tolarian Academy (tag B) | n/a | n/a |

The five in-identity families cover all 52 in-identity two-card variants (24 + 15 + 7 + 4 + 2).

Families with three or more pieces besides Toph (piece counts: Toph, Hardheaded Teacher's 70 have 4 pieces; Staff of Domination has 32 with 3 and 15 with 4; the rest 3). The verdict depends on the family: Wizards' two-card rule does not reach them, but extra turns must be "not chained or looped" and stax-style locks should "bracket up".

| Family (in-identity variants) | Pieces | Result | Verdict |
|---|---|---|---|
| Ugin's Nexus (21, tag R) | Ugin's Nexus + Meticulous Excavation + sacrifice outlet | Infinite turns | **Floor 4** (looped extra turns; power-scale: "any chain or infinite-turn combo -> floor 4") |
| Magistrate's Scepter (1, tag R) | Magistrate's Scepter + Rootpath Purifier + Earthcraft | Infinite turns | **Floor 4** (same rule) |
| Aeon Engine (1, tag S) | Aeon Engine + Wilderness Reclamation + Ba Sing Se | Lock: "Locks out all of your opponents but one" | **Bracket up** (stax-style lock) |
| Staff of Domination (32 with Yavimaya, Cradle of Growth or Urborg, Tomb of Yawgmoth) | One of those lands + Staff of Domination + a mana doubler (Wild Growth, Utopia Sprawl, Mirari's Wake, Nissa, Who Shakes the World, Zendikar Resurgent, Mana Reflection, ...) | Infinite mana, cards, life | Unclear by the letter; floor-4 candidate by project policy (commander combo) |
| Magus of the Candelabra (16, tag E) | Magus of the Candelabra + Thousand-Year Elixir + a mana doubler (Nissa, Who Shakes the World, ...) | Infinite mana | Same as Staff |
| Haru, Hidden Talent (159) | Haru, Hidden Talent + changeling, Ally or Maskwood Nexus + sacrifice outlet | Infinite landfall, death triggers | Same as Staff |
| Toph, Hardheaded Teacher (70) | Toph, Hardheaded Teacher + bounce land + 0-MV artifact + sacrifice outlet | Infinite landfall, death triggers | Same as Staff |
| Mycosynth Lattice (34 larger) | Mycosynth Lattice + earthbend-on-enter creature + sacrifice outlet | Infinite loops | Same as Staff (and MLD risk, section 5) |
| Emeria Shepherd (0: **not in Spellbook**) | Emeria Shepherd + Prismatic Omen or Dryad of the Ilysian Grove + two or three self-sacrificing artifacts | Infinite mana, cards, landfall | Same as Staff; found by the independent verification (section 5) |

Fine for Bracket 3: the recommended build needs no combo. Candidate list check, **against Spellbook only**: 0 variants fully assembled from the 217 candidates + Toph, 0 with one template slot; 8 cards are one card away from a candidate-only Spellbook combo (Springheart Nantuko x3, Candelabra of Tawnos x2, Meloku the Clouded Mirror x2, The Stasis Coffin, Mindslaver, Gonti's Aether Heart, Caged Sun, Staff of Domination), all excluded above. Spellbook is not complete (the Emeria Shepherd loop is missing), so this check is necessary but not sufficient. Combo-adjacent candidates, safe only while the excluded pieces stay out:

| Candidate | Excluded piece(s) it would combine with |
|---|---|
| Thran Dynamo, Everflowing Chalice | Candelabra of Tawnos |
| Lotus Cobra, Tireless Provisioner, Nissa, Resurgent Animist | Springheart Nantuko |
| Yavimaya, Cradle of Growth, Urborg, Tomb of Yawgmoth, Nissa, Who Shakes the World | Staff of Domination (+ doubler); Nissa also with Magus of the Candelabra + Thousand-Year Elixir |
| Everflowing Chalice, Lotus Petal, Mox Amber, Mishra's Bauble, Tormod's Crypt | Fill the "Artifact Castable for {0}" template of the Toph, Hardheaded Teacher loops |
| Badgermole Cub, Badgermole, Earthbending Student, Toph, the Blind Bandit, Toph, Greatest Earthbender, Bumi, Eclectic Earthbender | Fill the earthbend-on-enter templates of the Mycosynth Lattice loops |
| Doubling Season | Bootleggers' Stash + Clock of Omens |
| Ba Sing Se | Aeon Engine + Wilderness Reclamation |
| Mox Amber | Meloku the Clouded Mirror (blue, outside identity) |
| Prismatic Omen, Dryad of the Ilysian Grove, self-sacrificing artifacts | Emeria Shepherd |

## 7. Speed profile

Expectation for the recommended A+B build without fast-mana Game Changers: **low to medium** risk of threatening lethal before its own turn 7. Unverified until the Monte Carlo speed-risk script runs (it decides the flag). The base list has no rituals and no Game Changer fast mana, but it has many 0-2 MV artifacts and 1-2 MV mana creatures.

| Package | Effect on speed |
|---|---|
| Lotus Cobra + cheap artifacts (Mox Amber, Lotus Petal, Mishra's Bauble, Everflowing Chalice) + lands-tap engines | Big mana by turn 4-5; enables early 7-8 drops (main driver) |
| Scute Swarm, Ancient Greenwarden, Panharmonicon | Exponential token growth after six lands; can make a lethal board early |
| Valakut, the Molten Pinnacle + Prismatic Omen or Dryad of the Ilysian Grove | Every artifact entering is a Mountain entering: 3 damage each once five other Mountains exist; Ancient Greenwarden and Panharmonicon each add a trigger (up to 9 damage per artifact). Early non-combat kill |
| Sylvan Awakening, Kamahl's Will + Overwhelming Stampede, Craterhoof Behemoth or Moonshaker Cavalry | Every land and artifact attacks at once: one-turn alpha strike |
| Craterhoof Behemoth, Overwhelming Stampede, Moonshaker Cavalry, Toph, Greatest Earthbender | One-turn kills from a wide board (allowed: "one big turn") |
| Moraug, Fury of Akoum | Extra combats per artifact cast in main phase (review note, not a Wizards category) |
| Fast-mana Game Changers, tutors | Push toward **medium** or higher |
| Combo packages in sections 5-6, including the Emeria Shepherd loop | Would push to high or very high; excluded |

## 8. Open questions and risks for Phase 4

| # | Item |
|---|---|
| 1 | Rules-background claims to confirm with a rules source (Scryfall rulings returned HTTP 403, so all stay unverified): artifact entering = landfall under Toph (Spellbook descriptions agree); basic land types give artifact-lands mana abilities; Blood Moon removes artifact-land abilities; counter enhancers apply to earthbend counters; Valakut counts artifacts made Mountains by Prismatic Omen; an earthbended Equipment falls off; artifact creatures made lands stay summoning-sick for {T} mana; the two-piece Emeria Shepherd loop relies on last known information |
| 2 | The Spellbook file only holds combos that contain Toph. Two-card combos among the 99 without Toph are not covered: Layer A must run `find-my-combos` and `estimate-bracket` on the final list with Toph in `commanders` |
| 2b | Spellbook also misses some commander loops (Emeria Shepherd). Combo screening of the final list must include a manual check for recursion loops: any card that returns permanents from the graveyard to the battlefield on landfall or artifact entry, combined with self-sacrificing artifacts |
| 3 | No `relevant`, two-card or `speed` flags in the export; the floor-4 calls above are by piece count, tag and mana value only |
| 4 | Owner's deck contains The Stasis Coffin and Mindslaver: recommend not locking them in Phase 6 (Mindslaver is a clear floor-4 trigger; the Coffin needs a written bracket-fit decision) |
| 5 | Wizards' 2026-10-12 announcement may change the Game Changer list or bracket rules; re-check sections 4-5 |
| 6 | GC value versus budget is unknown until Phase 7 prices; low budget points may be best with 0 GCs |
| 7 | Community build patterns could not be verified (no EDHREC, no network); tiers are this report's judgment |
| 8 | Hour of Revelation, Ondu Inversion and Planar Cleansing kill Toph (not a land); Urza's Ruinous Blast spares it; Oblivion Stone spares it only with a fate counter. Graveyard hate is still thin (Tormod's Crypt only) |
| 9 | Many TLA cards (2025-11) have short play history; their tiers carry more uncertainty |

## Verification

Scripts in the session scratchpad, run with `python -I` on the local cache only. v1 scripts are in `...\scratchpad\`; the v2 revision scripts are in `...\scratchpad\toph\` (prefix `toph_`).

| Check | Command | Result |
|---|---|---|
| Spellbook totals | `sb_summary.py spellbook_toph-the-first-metalbender.json` | 1,099 variants; tags E 991, S 57, R 46, P 3, B 2; status OK 1,099 |
| In-identity subset, hubs | `sb_freq.py`, inline counts | 400 in R/G/W; hub counts as in sections 5-6 |
| One- and two-card lists | `sb_list.py ... 3 R,S,P,B`, `sb_list2.py ... 3 E` | 4 one-card, 52 in-identity two-card variants reviewed |
| Verification findings | `toph/toph_vcheck.py` | Magus of the Candelabra 16 variants, all 3 pieces, all with Thousand-Year Elixir; 23 sacrifice outlets in 262 variants (3 regex hits that are land costs, not outlets, removed by hand); Haru enablers as in section 5; Teacher variants all 4 pieces; Staff 32 x 3 + 15 x 4; bounce lands 5 x 12 = 60; Emeria Shepherd, Prismatic Omen, Dryad, Lotus Petal, Commander's Sphere, Mind Stone, Mishra's Bauble, Tormod's Crypt in 0 Toph variants |
| Oracle checks | `toph/toph_pool.py` on the B1 pieces, the 24 additions and 30 S3/S5 hazard names | 31/31 and 30/30 found; texts quoted in sections 3 and 5 |
| Candidates v2 | `toph/toph_validate_v2.py` | 217 listed; duplicates 0; missing from pool 0; color-identity violations 0; Game Changers among candidates 0; budget-alternative targets missing 0; Spellbook variants assembled from candidates 0 (0 with a template); Emeria Shepherd absent; loop screen: only Sun Titan and Titania, Protector of Argoth have triggered graveyard-to-battlefield text (both bounded: own enter/attack, or a land card on enter) |
| Tables | `toph/toph_gen_tables_v2.py` (tables generated from the validated list) | 217 rows |
| Hazard names (v1) | `pool.py` on 38 hazard names | 38/38 found in pool |
| Game Changers | pool filter `game_changer == true` | 30, same as manifest |
| Report names | `toph/toph_check_report_v2.py` (table names re-extracted from this file) | see last line of this section |
Final check (`toph/toph_check_report_v2.py`, run on this file before writing it): 217 section-3 cards re-extracted; all names found in pool: yes; color-identity violations: 0; duplicates: 0; Game Changers among candidates: 0; removed cards still listed: 0; 191 names cited in sections 4-6, 187 in pool with identity inside R/G/W, the other 4 outside Toph's identity or banned (Mana Crypt, Meloku the Clouded Mirror, Overburden, Tolarian Academy), as stated. Result: PASS.

## Response to verification

Each finding was re-checked against the pool oracle text and the Spellbook file (scripts `toph/toph_vcheck.py`, `toph/toph_validate_v2.py`), not accepted on trust.

| Finding | Status | What changed (or why disputed) |
|---|---|---|
| B1 Emeria Shepherd loop | **Confirmed** (stronger than reported) | Re-derived step by step from oracle text. With three self-sacrificing artifacts each Shepherd trigger resolves while its land is still on the battlefield, so the loop does not depend on last known information; the two-piece version does (rules background). Spellbook: 0 Toph variants with any piece. Emeria Shepherd removed; Prismatic Omen, Dryad of the Ilysian Grove, Lotus Petal, Commander's Sphere and Mind Stone marked "B1 loop piece"; hazard row and steps in section 5; family row in section 6; "0 combos" claim now says "against Spellbook only"; screening caveat added (section 8, item 2b); speed table updated |
| S1 Magus of the Candelabra | Confirmed | 16 in-identity variants, all 3 pieces, all with Thousand-Year Elixir. Moved from the two-card row to the 3+ piece row and table |
| S2 "allowed by the letter" contradiction | Confirmed | Section 6 now gives a verdict per family: Ugin's Nexus and Magistrate's Scepter floor 4 (looped extra turns), Aeon Engine bracket up (lock), the rest unclear by the letter and floor-4 candidates by policy |
| S3 MLD list incomplete | Confirmed, one item disputed | All 30 names verified in the pool. 24 added to the MLD row (now marked non-exhaustive); Nature's Revolt and Living Plane added as MLD by combo. Disputed: Nature's Will is not a clear MLD card (the tapped lands untap in their owner's untap step); listed as borderline, review |
| S4 Sacrifice outlets incomplete | Confirmed, one label corrected | 23 outlets in 262 variants, all now listed with counts; Haru enablers row added. Stonework Puma has no rules text: it is a Haru enabler because it is an Ally, not a changeling |
| S5 Extra-turn list incomplete | Confirmed | Seedtime, Emrakul, the Promised End and Perch Protection added |
| S6 Speed packages missing | Confirmed | Speed now "low to medium, unverified until the Monte Carlo run"; Valakut + Prismatic Omen/Dryad (up to 9 damage per artifact with Ancient Greenwarden and Panharmonicon), Sylvan Awakening/Kamahl's Will alpha strikes and the B1 loop added |
| S7 20 omissions and weak candidates | Confirmed, one item disputed | All 24 named cards verified and added with role and tier (section 3). Removed: Emeria Shepherd, Hellkite Tyrant, Azusa, Lost but Seeking, Organic Extinction, Darksteel Forge. Kept: Exploration (1 MV, still speeds real land drops; tier stays situational), Sensei's Divining Top (text fixed), Lotus Petal (marked B1 piece). Candidates 198 -> 217 |
| S8 Repeatable earthbend engines | Confirmed | Section 1 and a new paragraph in section 5; Inventors' Fair, Urza's Saga, fetch lands and Myriad Landscape rows updated. Own addition: an earthbended Oblivion Stone that is sacrificed dies and returns, making a repeatable one-sided nonland wipe (review note) |
| M1 Imprecise phrasings | Confirmed (all 8) | Nissa, Who Shakes the World ("noncreature land"), Earth Rumble (any creature you control), Sensei's Divining Top (no loop), counter "enhancers" instead of "doublers", one-card combos ("opponent control", no skipped turns), Solemn Simulacrum (reused when it dies), Darksteel Forge (removed), Marvin, Murderous Mimic in the Ley Weaver family |
| M2 Outlet count 262 | Confirmed | Oxidda Daredevil was missing; count now 262 |
| M3 "Three-card loops" heading | Confirmed | Renamed "Loops with three or more pieces"; piece counts stated in section 6 |
| M4 Bounce lands | Confirmed | Arid Archway and Guildless Commons added: 5 lands, 60 Teacher variants |
| M5 Combo-adjacent candidates | Confirmed | New table at the end of section 6 |
| M6 Rules gaps | Confirmed as rules background | Earthbended Equipment falls off; artifact creatures made lands stay summoning-sick for granted {T} mana. Added to section 1 weaknesses and section 8 item 1, marked unverified (Scryfall 403) |
| M7 Shorthand names | Partly applied | Combo and hazard tables now use full card names; narrative prose still uses short forms where unambiguous |
| M8 Tiers | Confirmed | Skullclamp reason rewritten (Avenger Plants, Scute Swarm Insects, earthbend-1 lands), still core; Tamiyo's Safekeeping moved from budget alternative to situational |
