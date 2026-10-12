Model ID: claude-opus-5-5

# Synergy research: Fire Lord Azula (Phase 3, 2026-10-11; revised 2026-10-12 after verification)

Sources (local only, no network): `data/cache/pool_fire-lord-azula.jsonl` (18,563 cards, Scryfall
oracle bulk `2026-10-11T21:01:56Z`), `data/cache/spellbook_fire-lord-azula.json` (94 variants),
`collect_manifest.json` (run `2026-10-11T23:09:01Z`). Rules: snapshot 2026-02-09 (beta), via
`docs/research/commander-brackets-rules-snapshot.md` and `docs/power-scale.md` v0.5. No prices.
The owner's current list was not used. Scryfall's `edhrec_rank` field (in the pool) was used only
to sort exploration lists, never as evidence. "Background knowledge, unverified" marks anything
not taken from these files. Scryfall rulings could not be fetched (the verifier got HTTP 403;
this researcher had no network access), so every rules reading stays **unverified**.
Independent review: `synergy-fire-lord-azula-2026-10-11-verification.md`; responses in §9.

## 1. Commander
| Field | Value (from the pool) |
|---|---|
| Name / cost / type | Fire Lord Azula, {1}{U}{B}{R}, Legendary Creature — Human Noble, 4/4 |
| Color identity | U B R (Grixis); `game_changer: false` |
| Oracle text | "Firebending 2 (Whenever this creature attacks, add {R}{R}. This mana lasts until end of combat.) / Whenever you cast a spell while Fire Lord Azula is attacking, copy that spell. You may choose new targets for the copy. (A copy of a permanent spell becomes a token.)" |

What it does:
- The copy window is only your own combat, from the moment she attacks until she leaves combat or
  combat ends. Firebending adds RR for that window.
- Every spell cast in that window is copied, and the copy is **mandatory** ("copy that spell"; no
  "may"). That covers:
  - instants;
  - flash permanents (copied as tokens);
  - sorceries, only with a flash enabler;
  - spells cast while another spell resolves, such as Electrodominance's free spell or Torrential
    Gearhulk's instant. Electrodominance can also put a sorcery into combat.
- Copies are not cast, so cast triggers (Guttersnipe, prowess) fire once, while magecraft ("cast or
  copy") fires twice.
- Rules background (CR 707.10, unverified): a copy keeps X and the chosen modes, may only change
  targets, pays no additional costs (discard, sacrifice, life), and sees 0 for "mana spent". So Big
  Score and Fire Covenant get a free copy, but a Memory Deluge copy looks at 0 cards.
- Copies of legendary permanent spells are legendary tokens. The legend rule leaves one body, but
  both ETB triggers still happen (Ertai Resurrected, Venser, Shaper Savant, Mithril Coat).

How it is usually played (background knowledge, unverified): a Grixis spellslinger that attacks
with Azula and keeps instants for combat, with equipment for haste and protection and flash
enablers for sorceries. Higher-power lists copy extra-turn spells and loop Narset's Reversal
(Bracket 4).

Weaknesses:
- She must attack and survive. She is a 4/4 with no evasion, haste or protection, and blockers or
  removal cast in response to the first spell turn the engine off.
- Her mana must be held through main phase 1.
- She is a 4-mana, 3-color commander with tax.
- Shroud equipment (Lightning Greaves, Whispersilk Cloak) also blocks your own targeting of her.
- The mandatory copy can backfire (Pact of Negation, Final Fortune; §5).

## 2. Archetypes
| # | Direction | Bracket fit |
|---|---|---|
| A | **Combat spellslinger (recommended primary)**. Instant removal, draw and Treasure spells cast in combat for 2-for-1s. Engines that count every copy (Archmage Emeritus, Storm-Kiln Artist, Professor Onyx). Haste, evasion and protection (Swiftfoot Boots, Brotherhood Regalia). Wins with drain, X burn and combat. | B3, comfortable |
| B | **Flash creatures / token copies** (sub-package of A). ETB flash creatures (Ertai Resurrected, Snapcaster Mage, Torrential Gearhulk) plus Leyline of Anticipation and Vedalken Orrery. Ghostly Flicker must stay out (§6). | B3, fine |
| C | **Fire Nation big combat** (budget or thematic). Fire Nation Palace, Zuko, Firebending Master, rituals, red-mana retention (Electro, Ashling, Birgi) and X finishers. Adding the speed package (§7: copy multipliers and damage multipliers) moves it toward medium speed risk. | B3; watch speed |
| D | **Extra turns / Reversal and Breach loops**. Time Warp-style spells copied for 2 turns; Narset's Reversal, Frantic Search, Underworld Breach, Snap with Dualcaster Mage. | **Bracket 4: excluded** |

Recommendation: A as the core, B as a 6-10 card package, C's mana pieces where the budget allows.

## 3. Candidate cards by role (212)
Tier legend:
- `core` / `strong` / `situational` / `budget alternative to <card>`.
- "Budget alternative" means a likely cheaper functional substitute. Prices are unknown until
  Phase 7.
- GC = Scryfall `game_changer` from the pool. Six candidates are Game Changers; a list may hold at
  most 3 (§4).
- The `core` set (13 cards) excludes the **speed package** (§7). Rows marked "(speed package)" move
  a build from low to medium speed risk.
- Combo partners that must never be added are named in the rows and in §5-§6.
#### Ramp and mana (24)
| Card | Tier | GC | Why it fits Azula |
|---|---|---|---|
| Sol Ring | core |  | 1-mana rock; Azula on turn 3; never with Hullbreaker Horror |
| Arcane Signet | core |  | Any Grixis color |
| Talisman of Dominance | strong |  | U/B untapped on turn 2 |
| Talisman of Creativity | strong |  | U/R untapped on turn 2 |
| Talisman of Indulgence | strong |  | B/R untapped on turn 2 |
| Dimir Signet | budget alternative to Talisman of Dominance |  | Filters into UB |
| Izzet Signet | budget alternative to Talisman of Creativity |  | Filters into UR |
| Rakdos Signet | budget alternative to Talisman of Indulgence |  | Filters into BR |
| Fellwar Stone | strong |  | 2-mana fixing in multiplayer |
| Commander's Sphere | budget alternative to Arcane Signet |  | Any Grixis color, but costs 3; sacrifice to draw |
| Mind Stone | situational |  | 2-mana rock that cycles itself late |
| Thought Vessel | situational |  | 2-mana rock; no maximum hand size for big draws |
| Mox Amber | situational |  | 0 mana; any color among your legendaries (Azula gives all three); never with Hullbreaker Horror |
| Dark Ritual | strong |  | Cast while Azula attacks: the copy adds BBB more (6 for 1) |
| Seething Song | strong |  | Copied in combat: 10 red for 3; never with Reiterate (loop) |
| Pyretic Ritual | budget alternative to Seething Song |  | RRR, doubled by the copy |
| Big Score | core |  | Copy skips the discard cost: 4 cards and 4 Treasures |
| Unexpected Windfall | strong |  | Same as Big Score; firebending RR pays the red |
| Deadly Dispute | strong |  | Copy needs no sacrifice: draw 4 and 2 Treasures |
| Black Market Connections | strong |  | Treasure, cards or a body every turn |
| Storm-Kiln Artist | core |  | Treasure per cast AND per copy; see the partner exclusions in §5 |
| Birgi, God of Storytelling // Harnfel, Horn of Bounty | strong |  | R per spell cast, kept through steps; never with Grinning Ignus |
| Goldspan Dragon | strong |  | Treasure on attack or when targeted; Treasures tap for 2 |
| Electro, Assaulting Battery | situational |  | Keeps unspent red mana; R per instant/sorcery cast |
#### Card advantage (20)
| Card | Tier | GC | Why it fits Azula |
|---|---|---|---|
| Archmage Emeritus | core |  | Draws on cast and on copy: 2 cards per instant in combat |
| Rhystic Study | strong | yes | Strongest passive draw; uses a Game Changer slot |
| Mystic Remora | strong |  | Cheap early draw engine |
| Phyrexian Arena | strong |  | Steady draw outside the combat plan |
| Archmage of Runes | strong |  | Instants/sorceries cost 1 less and draw on cast |
| Fact or Fiction | strong |  | Copy = a second 5-card split |
| Pull from Tomorrow | strong |  | X draw; the copy keeps X |
| Stroke of Genius | strong |  | X draw; the copy keeps X |
| Blue Sun's Zenith | budget alternative to Stroke of Genius |  | X draw, reshuffles itself |
| Dig Through Time | strong |  | Copy needs no delve: a second look at 7 |
| Commence the Endgame | strong |  | Can't be countered; copy draws 2 and amasses again |
| Village Rites | situational |  | Copy pays no sacrifice: 4 cards for B; needs a creature to sacrifice |
| Brainstorm | situational |  | With the copy: 4 new cards seen, put back the worst |
| Opt | situational |  | Cast plus copy: 2 cards and 2 magecraft triggers for U |
| Consider | situational |  | Cast plus copy: 2 cards and 2 magecraft triggers for U |
| Thrill of Possibility | budget alternative to Big Score |  | Copy skips the discard: 4 cards for one discard; no Treasures |
| Valakut Awakening // Valakut Stoneforge | situational |  | MDFC: land or hand refresh |
| Ledger Shredder | situational |  | Connives on each player's second spell |
| Faerie Mastermind | situational |  | Flash draw engine; the token copy doubles it |
| The One Ring | situational | yes | Protection turn plus growing draw; Game Changer slot |
#### Removal, targeted (27)
| Card | Tier | GC | Why it fits Azula |
|---|---|---|---|
| Deadly Rollick | core |  | Free while Azula is out; the copy exiles a second creature |
| Infernal Grasp | core |  | 2-mana instant kill; copy = 2-for-1 |
| Fire Covenant | core |  | Copy keeps X with no life paid: X damage divided twice |
| Go for the Throat | strong |  | Instant kill, doubled in combat |
| Terminate | strong |  | Instant kill, doubled in combat |
| Bedevil | strong |  | Artifact, creature or planeswalker; doubled |
| Hero's Downfall | strong |  | Creature or planeswalker; doubled |
| Fell the Profane // Fell Mire | strong |  | MDFC: removal or land |
| Snuff Out | strong |  | Free (4 life) with a Swamp; doubled |
| Bitter Triumph | strong |  | 2-mana creature/planeswalker kill |
| Withering Torment | strong |  | Creature or enchantment |
| Pongify | strong |  | 1-mana kill (leaves a 3/3); the copy kills a second creature |
| Rapid Hybridization | strong |  | Same as Pongify |
| Chaos Warp | strong |  | Answers any permanent type |
| Kolaghan's Command | strong |  | Two modes; the copy repeats them with new targets |
| Sheoldred's Edict | strong |  | Edict that beats hexproof; copy = second edict |
| Murderous Rider // Swift End | strong |  | Instant face is copied; creature cast later |
| Brazen Borrower // Petty Theft | strong |  | Tempo bounce plus a flash flyer |
| Ertai Resurrected | strong |  | Flash; the token copy gives a second counter/kill (legend rule keeps one body) |
| Heartless Act | budget alternative to Infernal Grasp |  | 2-mana instant kill |
| Doom Blade | budget alternative to Go for the Throat |  | 2-mana instant kill |
| Murder | budget alternative to Hero's Downfall |  | 3-mana instant kill |
| Abrade | situational |  | 3 damage to a creature or kill an artifact; doubled |
| Dismember | situational |  | -5/-5, payable with life |
| Lightning Bolt | situational |  | 1 mana; the copy adds 3 more damage to any target |
| Bonecrusher Giant // Stomp | situational |  | Stomp is copied; 4/3 body later |
| Untimely Malfunction | situational |  | Artifact kill, redirect or 'can't block' for 2 |
#### Counterspells and stack interaction (18)
| Card | Tier | GC | Why it fits Azula |
|---|---|---|---|
| Counterspell | core |  | UU hard counter |
| Arcane Denial | strong |  | 2-mana hard counter |
| Swan Song | strong |  | 1 mana; stops removal spells aimed at Azula |
| An Offer You Can't Refuse | strong |  | 1-mana noncreature counter |
| Mana Drain | strong |  | Counter plus mana next main phase |
| Fierce Guardianship | strong | yes | Free while Azula is out; Game Changer slot |
| Force of Negation | strong |  | Free on opponents' turns |
| Force of Will | situational | yes | Free counter; Game Changer slot |
| Negate | budget alternative to An Offer You Can't Refuse |  | 2-mana noncreature counter |
| Mana Leak | budget alternative to Counterspell |  | Soft counter |
| Delay | budget alternative to Counterspell |  | 2-mana tempo counter |
| Flusterstorm | situational |  | 1 mana; counters the instant/sorcery aimed at Azula |
| Prismari Command | strong |  | 2 modes (damage, loot, Treasure, artifact); the copy repeats them with new targets |
| Izzet Charm | situational |  | Soft counter, 2 damage or loot |
| Cryptic Command | situational |  | The copy repeats both modes (e.g. tap all opposing creatures + draw) |
| Mystic Confluence | situational |  | 5 mana; the copy repeats the same three modes |
| Sublime Epiphany | situational |  | Copy repeats the modes; never with Archaeomancer/Mnemonic Wall plus Storm-Kiln Artist (loop, §5) |
| Tishana's Tidebinder | situational |  | Flash; counters an ability (token copy counters another) |
#### Board wipes (9)
| Card | Tier | GC | Why it fits Azula |
|---|---|---|---|
| Toxic Deluge | core |  | Pick X of 3 or less to keep Azula (4/4) alive |
| Cyclonic Rift | strong | yes | One-sided instant reset; Game Changer slot |
| Damnation | strong |  | Clean 4-mana wrath |
| Delayed Blast Fireball | strong |  | One-sided 2 (5 if foretold) damage, instant |
| Blasphemous Act | situational |  | Cheap in crowded boards, but kills Azula too |
| Anger of the Gods | situational |  | 3 damage: spares Azula (toughness 4), kills 2-toughness engines |
| Ritual of Soot | situational |  | Mana value 3 or less: spares Azula (4), kills cheap engines |
| Crux of Fate | situational |  | 5-mana wrath (non-Dragon mode) |
| Massacre Wurm | situational |  | One-sided -2/-2 plus drain |
#### Protection (15)
| Card | Tier | GC | Why it fits Azula |
|---|---|---|---|
| Swiftfoot Boots | core |  | Haste and hexproof; no clash with your own targeting |
| Lightning Greaves | strong |  | Haste and shroud, equip 0; shroud also blocks your own targeting (Palace, Passage, equips, protection spells) |
| Deflecting Swat | core |  | Free while Azula is out; redirects removal |
| Brotherhood Regalia | strong |  | Ward 2 and unblockable; equip legendary for 1 |
| Whispersilk Cloak | strong |  | Unblockable; shroud (blocks your own targeting too) |
| Mithril Coat | strong |  | Flash; attaches to Azula (targets); indestructible |
| Bolt Bend | strong |  | Costs R with Azula's power 4: redirect |
| Malakir Rebirth // Malakir Mire | strong |  | MDFC: return-on-death or land |
| Champion's Helm | situational |  | Hexproof while equipped to a legendary creature |
| Slip Out the Back | situational |  | 1-mana phase out |
| Dive Down | situational |  | 1-mana hexproof |
| Undying Malice | situational |  | Returns Azula if she dies this turn |
| Fake Your Own Death | situational |  | Returns Azula plus a Treasure |
| Kaya's Ghostform | situational |  | Returns Azula once from death or exile |
| Spellskite | situational |  | Redirect magnet for removal |
#### Evasion, haste and combat (8)
| Card | Tier | GC | Why it fits Azula |
|---|---|---|---|
| Prowler's Helm | strong |  | Can't be blocked except by Walls |
| Key to the City | situational |  | Discard for unblockable; draws on untap |
| Expedite | situational |  | Haste precombat plus a draw (no copy before she attacks) |
| Sword of Feast and Famine | situational |  | Pro-black; combat damage untaps all lands for main phase 2 |
| Rising of the Day | situational |  | Haste; legendary creatures get +1/+0 |
| The Fire Crystal | situational |  | Red spells cost 1 less; haste |
| Great Train Heist | situational |  | Extra combat; copy adds another (review note) |
| Savage Beating | situational |  | Combat-only: double strike or extra combat (review note) |
#### Flash enablers: copy sorceries and creature spells in combat (9)
| Card | Tier | GC | Why it fits Azula |
|---|---|---|---|
| Leyline of Anticipation | strong |  | All spells have flash |
| Vedalken Orrery | strong |  | All spells have flash; never with extra-turn spells |
| Valley Floodcaller | strong |  | Flash 3-drop; noncreature spells have flash |
| High Fae Trickster | strong |  | Flash flyer; all spells have flash |
| Borne Upon a Wind | situational |  | Flash for one turn and draw |
| Quicken | situational |  | Next sorcery has flash; draw |
| Hypersonic Dragon | situational |  | Haste flyer; sorceries have flash |
| Scarring Memories | situational |  | Flash while Azula attacks; copy = double edict/discard/drain |
| Tidal Barracuda | situational |  | Flash for all; opponents can't cast on your turn (review flag) |
#### Engines and payoffs (23)
| Card | Tier | GC | Why it fits Azula |
|---|---|---|---|
| Veyran, Voice of Duality | strong |  | Azula's trigger fires twice on instants/sorceries; doubles magecraft (speed package) |
| Roaming Throne | strong |  | Name Human: Azula's copy and firebending triggers fire twice for every spell (speed package) |
| Harmonic Prodigy | strong |  | Doubles Shaman/Wizard triggers: Storm-Kiln, Archmage Emeritus, Veyran, Ashling, Guttersnipe |
| Strionic Resonator | strong |  | {2}: copy Azula's copy trigger once per turn |
| Twinning Staff | strong |  | Each Azula copy becomes two (speed package); never with Dramatic Reversal |
| Shaun, Father of Synths | strong |  | Attacking token copy of Azula adds a second copy trigger (speed package) |
| Helm of the Host | situational |  | Hasty non-legendary Azula token each combat: second firebending and copy trigger (speed package) |
| Return the Favor | situational |  | Copy Azula's trigger, or redirect removal |
| Sedgemoor Witch | strong |  | Pest per cast and per copy |
| Professor Onyx | strong |  | Drain 2 per cast and per copy |
| Ashling, Flame Dancer | strong |  | Keeps red mana; loot per cast/copy; 2nd resolution sweeps for 2 |
| Baral, Chief of Compliance | strong |  | Instants/sorceries cost 1 less; loot on counter |
| Goblin Electromancer | strong |  | Instants/sorceries cost 1 less |
| Guttersnipe | strong |  | 2 damage to each opponent per instant/sorcery cast |
| Young Pyromancer | situational |  | Token per instant/sorcery cast (cast only; copies add nothing) |
| Third Path Iconoclast | situational |  | Artifact token per noncreature spell (cast only) |
| Murmuring Mystic | situational |  | Flying token per instant/sorcery cast (cast only) |
| Ral, Storm Conduit | situational |  | Ping per cast and per copy |
| Kessig Flamebreather | budget alternative to Guttersnipe |  | 1 damage each opponent per noncreature spell (cast only) |
| Zuko, Firebending Master | situational |  | Experience per spell cast in combat grows its firebending |
| Fiery Emancipation | situational |  | Triples damage (raises speed risk) |
| Twinflame Tyrant | situational |  | Doubles damage to opponents (raises speed risk) |
| Kediss, Emberclaw Familiar | situational |  | Azula's combat damage hits each other opponent |
#### Win conditions (6)
| Card | Tier | GC | Why it fits Azula |
|---|---|---|---|
| Comet Storm | strong |  | Copy keeps X and the kicks: double spread (speed package) |
| Expansion // Explosion | strong |  | Explosion copy: X damage and X cards again |
| Electrodominance | situational |  | X damage plus a free spell, cast mid-resolution, that Azula also copies |
| Exsanguinate | situational |  | Sorcery; with flash the copy drains X again |
| Torment of Hailfire | situational |  | Sorcery; with flash the copy repeats X |
| Fireball | situational |  | Sorcery X burn; needs flash to be copied |
#### Utility, recursion and tutors (12)
| Card | Tier | GC | Why it fits Azula |
|---|---|---|---|
| Snapcaster Mage | strong |  | Flash; the token copy grants a second flashback |
| Torrential Gearhulk | strong |  | Flash; the token copy casts a second instant free (also copied) |
| Archaeomancer | situational |  | Rebuys a spell; never with Ghostly Flicker or Sublime Epiphany plus Storm-Kiln Artist |
| Mnemonic Wall | budget alternative to Archaeomancer |  | Same rebuy and same exclusions |
| Venser, Shaper Savant | situational |  | Flash bounce of a spell or permanent; copy bounces again (legend rule keeps one body) |
| Orcish Bowmasters | situational | yes | Flash; token copy pings again; Game Changer slot |
| Spellseeker | situational |  | Tutor an instant/sorcery of mana value 2 or less |
| Merchant Scroll | situational |  | Tutor a blue instant |
| Solve the Equation | situational |  | Tutor an instant or sorcery |
| Waterlogged Teachings // Inundated Archive | strong |  | MDFC: tutor an instant/flash card or UB land |
| Sink into Stupor // Soporific Springs | strong |  | MDFC: bounce a spell/permanent or land |
| Jwari Disruption // Jwari Ruins | situational |  | MDFC: soft counter or land |
#### Lands (41)
| Card | Tier | GC | Why it fits Azula |
|---|---|---|---|
| Command Tower | core |  | Any Grixis color |
| Exotic Orchard | strong |  | Usually any color in multiplayer |
| Watery Grave | strong |  | Untapped UB; Island Swamp types for verges/fetches |
| Steam Vents | strong |  | Untapped UR; Island Mountain types |
| Blood Crypt | strong |  | Untapped BR; Swamp Mountain types |
| Polluted Delta | strong |  | Fetches Island or Swamp (incl. shocks) |
| Scalding Tarn | strong |  | Fetches Island or Mountain |
| Bloodstained Mire | strong |  | Fetches Swamp or Mountain |
| Fabled Passage | budget alternative to Polluted Delta |  | Fetches a basic |
| Sulfur Falls | strong |  | Check land UR |
| Dragonskull Summit | strong |  | Check land BR |
| Drowned Catacomb | strong |  | Check land UB |
| Morphic Pool | strong |  | Untapped UB in multiplayer |
| Training Center | strong |  | Untapped UR in multiplayer |
| Luxury Suite | strong |  | Untapped BR in multiplayer |
| Shivan Reef | strong |  | Pain land UR |
| Underground River | strong |  | Pain land UB |
| Sulfurous Springs | strong |  | Pain land BR |
| Stormcarved Coast | strong |  | Slow land UR |
| Shipwreck Marsh | strong |  | Slow land UB |
| Haunted Ridge | strong |  | Slow land BR |
| Gloomlake Verge | strong |  | U always; B with an Island or Swamp |
| Riverpyre Verge | strong |  | R always; U with an Island or Mountain |
| Blazemire Verge | strong |  | B always; R with a Swamp or Mountain |
| Xander's Lounge | situational |  | Tapped tri-land with all three types; cycling |
| Crumbling Necropolis | budget alternative to Xander's Lounge |  | Tapped tri-land |
| Clearwater Pathway // Murkwater Pathway | situational |  | Untapped U or B |
| Riverglide Pathway // Lavaglide Pathway | situational |  | Untapped U or R |
| Blightstep Pathway // Searstep Pathway | situational |  | Untapped B or R |
| Temple of Deceit | budget alternative to Drowned Catacomb |  | Tapped UB with scry |
| Temple of Epiphany | budget alternative to Sulfur Falls |  | Tapped UR with scry |
| Temple of Malice | budget alternative to Dragonskull Summit |  | Tapped BR with scry |
| Rogue's Passage | strong |  | Makes Azula unblockable (targets) |
| Fire Nation Palace | strong |  | Azula gains firebending 4: +RRRR in combat (net +1 after {1}{R} and its own tap; targets) |
| Otawara, Soaring City | strong |  | Blue source with instant-speed bounce |
| Plaza of Heroes | situational |  | Any color for legendary spells; can give Azula hexproof and indestructible |
| Reliquary Tower | situational |  | No hand size limit for big draws |
| Emergence Zone | situational |  | One turn of flash from a land |
| Talon Gates of Madara | situational |  | Phases out Azula in response to removal |
| Shizo, Death's Storehouse | situational |  | Gives Azula fear (targets) |
| Mystic Sanctuary | situational |  | Puts an instant back on top |

Mana base notes:
- About 36-37 lands plus 8-10 rocks or Treasure makers.
- Blue is the heaviest color, then black. Red needs in combat are partly covered by firebending RR,
  but not in main phases.
- Prefer untapped duals: the shocks give the land types that the verges and fetches use.
- Off-color fetches (Flooded Strand, Misty Rainforest, Marsh Flats, Verdant Catacombs, Arid Mesa,
  Wooded Foothills) each find one Grixis type.
- Underground Sea, Volcanic Island and Badlands are in the pool. Hunch, unverified: they are likely
  far above budget.

## 4. Game Changers in the pool (36)
Bracket 3 allows at most 3 (Azula is not one). Hunch, unverified: Rhystic Study, Fierce
Guardianship, Force of Will and The One Ring are likely in the expensive tier, so the optimizer may
choose 0-3.

| Verdict | Cards | Reason |
|---|---|---|
| Worth a slot (pick up to 3) | Cyclonic Rift, Rhystic Study, Fierce Guardianship | Instant one-sided reset / best value engine / free protection while Azula is out |
| Alternates | The One Ring, Orcish Bowmasters, Force of Will | Draw plus a safe turn / flash body whose token copy pings twice / free counter |
| Legal, weak fit | Consecrated Sphinx, Bolas's Citadel, Opposition Agent | Sorcery-speed 6-drop / life-hungry, works outside combat / mostly a hoser |
| Legal, weak fit (tutors) | Demonic Tutor, Vampiric Tutor, Imperial Seal, Mystical Tutor, Gamble, Intuition, Gifts Ungiven | A GC slot is worth more as an engine; Wizards frames efficient tutors as Bracket 4 GCs |
| Avoid: combo | Underworld Breach, Thassa's Oracle, Ad Nauseam | Breach + Frantic Search + Azula is a Spellbook combo; Oracle and Ad Nauseam are combo finishers (background) |
| Avoid: lock or stax | Narset, Parter of Veils, Notion Thief, Tergrid, God of Fright // Tergrid's Lantern, Braids, Cabal Minion, Glacial Chasm, The Tabernacle at Pendrell Vale, Panoptic Mirror | Draw denial, sacrifice/discard locks, a free extra spell each upkeep (Mirror) |
| Avoid: fast mana | Ancient Tomb, Chrome Mox, Grim Monolith, Mana Vault, Mox Diamond, Lion's Eye Diamond, Mishra's Workshop, Jeska's Will | Wizards: fast mana is a Bracket 4 Game Changer pattern; raises speed risk |
| No fit | Necropotence, Field of the Dead | Bracket 4-style engine / no land-count plan |

## 5. Bracket 3 hazards (rules snapshot 2026-02-09, beta)
**Extra turns: decision for the owner, two readings.**
- Facts:
  - Azula's copy is mandatory, so one extra-turn spell cast while she attacks gives 2 extra turns.
  - 49 pool cards mention "extra turn". Three of them stop extra turns: Gerrard's Hourglass Pendant,
    Stranglehold, Ugin's Nexus.
  - Two are instants that need no flash enabler: Nexus of Fate, Final Fortune.
  - Extra-turn permanents with activated abilities are not copied unless the permanent spell is
    cast in combat: Time Sieve, Magistrate's Scepter, Sage of Hours.
- **Reading A (Wizards' text alone).** Wizards allows "low quantities", "not intended to be chained
  in succession or looped", and gives no number. One extra-turn card is a low quantity, so 1 card
  is allowed (Layer A floor 2) as long as it is never looped.
- **Reading B (project policy, conservative).** `power-scale.md` says a card multiplied by the
  commander counts as 2, and 2 or more is a policy reject. So 0 cards. One copied spell gives two
  successive turns, which arguably is also a "chain" (floor 4).
- Doc inconsistencies for the owner:
  - The power-scale table says "not chained" and drops "or looped".
  - Its "Spellbook tags 2+ as Ruthless" rationale does not cover a single copied card. Spellbook
    counts cards, so it would tag `C`.
- Either reading excludes 2 or more extra-turn cards and every loop.

**Two-card infinite combos** ("no intentional early-game two-card infinite combos"; project
convention: none reachable on turns 1-6). Exclude:
- **Azula + 2 cards** (Spellbook file, 22 buildable; §6): Narset's Reversal, Underworld Breach,
  Dualcaster Mage, Ghostly Flicker, Arcbond, plus Release to the Wind or Transcendent Dragon, and
  Reality Spasm or Errant, Street Artist.
- **Pairs with candidates**. Not in the local file: each is my oracle-text derivation plus the
  verifier's Spellbook API spot check. Phase 2 must confirm. Keep the partner out:

| Candidate | Partner(s) to exclude | Loop (oracle reading) |
|---|---|---|
| any magecraft payoff (Storm-Kiln Artist, Archmage Emeritus, Veyran, Voice of Duality, Professor Onyx, Sedgemoor Witch, Ral, Storm Conduit, Ashling, Flame Dancer) | Chain of Smog | Target yourself and copy it any number of times: every copy triggers magecraft (unbounded drain, pings, Treasures or cards) |
| Mox Amber, Sol Ring | Hullbreaker Horror (removed from the list) | Two cheap rocks bounce each other with each cast; Sol Ring + Mox Amber nets +2 mana per cycle |
| Twinning Staff | Dramatic Reversal, Narset's Reversal | Staff's {7} copy of Dramatic Reversal becomes 2 copies, so infinite mana once rocks make 4 or more |
| Birgi, God of Storytelling // Harnfel, Horn of Bounty | Grinning Ignus | Ignus bounce and recast is mana-neutral with Birgi: unbounded casts and ETBs |
| Storm-Kiln Artist | Haze of Rage; Reiterate (with Seething Song) | Buyback storm or buyback copy pays for itself with Treasures |
| Helm of the Host | Godo, Bandit Warlord | Infinite combats (commander-free) |

- **Commander-free pairs** (background knowledge, unverified; all in the pool; keep out):
  - Kiki-Jiki, Mirror Breaker or Splinter Twin + Pestermite / Deceiver Exarch / Zealous Conscripts
  - Dualcaster Mage + Twinflame / Heat Shimmer / Saw in Half
  - Isochron Scepter + Dramatic Reversal
  - Thassa's Oracle / Laboratory Maniac / Jace, Wielder of Mysteries + Demonic Consultation / Tainted Pact
  - Niv-Mizzet, Parun / Niv-Mizzet, the Firemind + Curiosity
  - Worldgorger Dragon + Animate Dead / Necromancy / Dance of the Dead
  - Sanguine Bond + Exquisite Blood

**Candidate-only chain** (oracle derivation, not in Spellbook; for the bracket-fit review).
- Pieces: Azula attacking + Storm-Kiln Artist + Archaeomancer (or Mnemonic Wall) + Sublime
  Epiphany.
- Cast Epiphany with the token-copy mode on Archaeomancer. Azula's copy re-targets Storm-Kiln, so
  it adds a Storm-Kiln each loop.
- The Archaeomancer token returns Epiphany. Treasures per loop are 2, 4, 6, 8 against a cost of 6,
  so about 12 mana starts unbounded mana and magecraft.
- Do not run all three pieces together.

**Mass land denial** (Wizards: four or more lands per player; "not in Brackets 1-3").
- Wizards' examples in this pool: Ruination, Sunder (an instant, so Azula would copy it), Winter
  Orb, Blood Moon.
- Also exclude: Magus of the Moon, Harbinger of the Seas, Zhao, the Moon Slayer, Back to Basics,
  Static Orb, Winter Moon, Storage Matrix, Rising Waters, Stasis, Tangle Wire, Contamination,
  Infernal Darkness, Curse of Marit Lage, Mana Vortex, Mana Breach, Overburden, Jokulhaups,
  Obliterate, Apocalypse, Worldfire, Decree of Annihilation, Wildfire, Destructive Force, Burning
  of Xinye, Devastation, Death Cloud, Devastating Dreams, Tectonic Break, Bend or Break, Epicenter,
  Thoughts of Ruin, Boom // Bust, Keldon Firebombers, Impending Disaster, Myojin of Infinite Rage,
  Boil, Boiling Seas, Pox.

**Stax, lock and control.** Wizards: Stax-style lock decks should "bracket up".
- Exclude:
  - Opposition, Smokestack, Arcane Laboratory, Trinisphere, Chalice of the Void, Imi Statue;
  - Mindslaver (controls a player's turn);
  - the lock GCs in §4.
- Review flags if used:
  - taxes and hosers: Sphere of Resistance, Thorn of Amethyst, Lodestone Golem, Defense Grid,
    God-Pharaoh's Statue, Null Rod, Cursed Totem, Damping Matrix, Torpor Orb, Mindlock Orb, Void
    Winnower;
  - cards that lock opponents out of your turn or hold them to sorcery speed: Tidal Barracuda,
    Conqueror's Flail, Teferi, Mage of Zhalfir.

**Tutors.** No bracket limit since 2025-10-21 (descriptive only). Non-GC tutors here: Merchant
Scroll, Solve the Equation, Spellseeker, Waterlogged Teachings. Suggest 3 or fewer (project
judgment).

**Mandatory-copy traps.**
- Pact of Negation copied creates two "pay {3}{U}{U} or lose" upkeep triggers.
- Final Fortune copied makes you lose at the end of the first extra turn.
- A Memory Deluge copy looks at 0 cards.

**Extra combats** (Great Train Heist, Savage Beating; copies add combats): Layer A treats them as a
review note, not a count.

## 6. Combos (Commander Spellbook file, 94 variants, all include Azula)
| Count | R | S | E | B | Total |
|---|---|---|---|---|---|
| Azula + 2 cards | 0 | 7 | 21 | 0 | 28 |
| Azula + 3 cards | 60 | 0 | 1 | 5 | 66 |
| Buildable in this pool | 48 | 7 | 16 | 0 | 71 |

- 23 variants are not buildable: 5 need Time Walk (tag `B`; banned and not in the pool) and 18 need
  off-identity cards.
- 65 variants produce "Infinite turns" plus "Lock".
- The file has no `speed` or `relevant` fields, so `manaValueNeeded` is the proxy used here; Phase 2
  `estimate-bracket` must confirm.
- The file covers only combos that include Azula. Candidate pairs without Azula are in §5.

| Buildable group | # | Tag | mv needed | Class | Why |
|---|---|---|---|---|---|
| Narset's Reversal + flash piece (Vedalken Orrery, Valley Floodcaller, Tidal Barracuda, Hypersonic Dragon) + extra-turn sorcery (Time Warp, Temporal Manipulation, Capture of Jingzhou, Temporal Mastery, Expropriate, Karn's Temporal Sundering, Beacon of Tomorrows, Alchemist's Gambit, Alrund's Epiphany, Walk the Aeons, Part the Waterveil, Twice Upon a Time // Unlikely Meeting); 4 x 12 | 48 | R | 5-9 | floor-4 trigger | Infinite turns and a lock |
| 11-2196-7089 Narset's Reversal + Frantic Search | 1 | S | 0 | floor-4 trigger | Infinite looting, near-infinite mana and storm |
| 11-5195-7089 Narset's Reversal + Storm-Kiln Artist | 1 | S | 0 | floor-4 trigger | Infinite Treasures and copies |
| 147-802-7089 Snap + Dualcaster Mage | 1 | S | 3 | floor-4 trigger | Infinite land untaps, ETB, storm |
| 1368-2196-7089 Underworld Breach + Frantic Search | 1 | S | 0 | floor-4 trigger | Infinite draw, near-infinite mana |
| 11-4276-7089 Narset's Reversal + Turnabout | 1 | S | 0 | floor-4 trigger | Infinite mana, storm, magecraft |
| 5067-7089-7269 Transcendent Dragon + Release to the Wind | 1 | S | 1 | floor-4 trigger | Infinite tokens, ETB, storm |
| 1357-4697-7089 Errant, Street Artist + Reality Spasm | 1 | S | 3 | floor-4 trigger | Infinite mana and magecraft |
| Ghostly Flicker + Archaeomancer / Pinnacle Monk // Mystic Peak / Ardent Elementalist / Scholar of the Ages / Mnemonic Wall / Shipwreck Dowser / Izzet Chronarch / Salvager of Secrets / Revolutionist / Donnie & April, Adorkable Duo / Zealous Lorecaster / Vampire Charmseeker / Scrivener / Possessed Skaab | 14 | E | 0 | floor-4 trigger | Spellbook tags it E (no built-in win). But it gives infinite mana, ETB and magecraft, which any magecraft payoff in §3 turns into a win |
| Bloodthirsty Conqueror + Arcbond | 1 | E | 1 | floor-4 candidate | A commander combo (Layer A reviews these as floor 4); infinite damage with heavy prerequisites; leave Arcbond out |
| Kiki-Jiki, Mirror Breaker + Blazing Firesinger // Seething Song + Hematite Talisman | 1 | E | 1 | floor-4 candidate | A commander combo. It uses the `prepare` card Blazing Firesinger // Seething Song, not the candidate Seething Song. Exclude Kiki-Jiki |
| **Fine for Bracket 3** | **0** | | | | No buildable variant is fine to assemble on purpose |

Safe halves (keep only while the partner is absent):
- Storm-Kiln Artist: without Narset's Reversal, Chain of Smog, Haze of Rage or Reiterate.
- Turnabout: without Narset's Reversal.
- Frantic Search: without Narset's Reversal and Underworld Breach.
- Snap: without Dualcaster Mage.
- The four flash pieces: without extra turns and Narset's Reversal.
- Archaeomancer, Mnemonic Wall and the other recursion creatures: without Ghostly Flicker (and not
  the §5 chain).
- Twinning Staff: without Dramatic Reversal.
- Birgi: without Grinning Ignus.
- Mox Amber and Sol Ring: without Hullbreaker Horror.

## 7. Speed profile (qualitative; the Monte Carlo script decides)
Speed package:
- copy multipliers: Veyran, Roaming Throne, Twinning Staff, Shaun, Helm of the Host;
- rituals: Dark Ritual, Seething Song;
- X burn: Comet Storm, Electrodominance;
- damage multipliers: Fiery Emancipation, Twinflame Tyrant.

| Build | Expected risk of lethal before own turn 7 | Drivers |
|---|---|---|
| `core` + `strong` minus the speed package (no combos, 0-1 extra turns, no fast-mana GCs) | **low** | Azula lands turn 3-4 and attacks turn 4-5; a typical combat copies 1-2 interaction or draw spells |
| Same plus the speed package | **medium** | Copy multipliers double every copied spell; rituals and X burn turn one combat into a large burst |
| Any extra-turn loop, Reversal or Breach loop, Ghostly Flicker loop, a §5 pair or chain, fast mana | high to very high | Bracket 4 by rule or intent |

## 8. Open questions and risks for Phase 4
1. **Extra turns, reading A or B (§5).** This is an owner decision, presented neutrally.
2. **Rules readings to verify.** Scryfall rulings were unreachable (HTTP 403), so these stay
   unverified:
   - (a) Does "don't lose unspent red mana" (Electro, Ashling) keep firebending mana?
   - (b) Shaun and Helm of the Host tokens: Shaun's token is not declared as an attacker, so it
     gives no firebending mana; its copy trigger should still work.
   - (c) Veyran, Roaming Throne and Harmonic Prodigy doubling Azula's and the engines' triggers
     (oracle text supports it).
   - (d) CR 707.10 for the copy rows.
3. **Phase 2 combo checks.** Run `find-my-combos` and `estimate-bracket` with Azula in
   `commanders`. They must confirm the §5 pairs (verifier API spot checks are not evidence) and
   search for new loops.
4. **Bracket-fit review rulings.** Copy multipliers plus land-untap spells or recursion creatures
   may form more chains like the §5 one. Extra combats (Great Train Heist, Savage Beating) and the
   Tidal Barracuda, Conqueror's Flail and Teferi, Mage of Zhalfir flags also need a ruling.
5. **Data quality.** The pool holds 48 Unfinity "Stickers" and 22 Attraction cards that Scryfall
   marks Commander-legal. Layer A should drop them.
6. **Rules re-check.** Re-check Game Changers after Wizards' announcement of 2026-10-12.
7. **Prices.** Prices are unknown, and the "budget" labels and expensive-tier hunches are
   unverified.

## 9. Response to verification
| Finding | Verdict | What changed / evidence |
|---|---|---|
| S1 Hullbreaker + Mox Amber / Sol Ring | confirmed (substance) | Oracle derivation: two cheap rocks bounce each other per cast, and Sol Ring + Mox Amber nets +2. Hullbreaker Horror removed; pairs added to §5 and the safe halves. The exact Spellbook 2-card shape was not reproducible offline |
| S2 Twinning Staff, Birgi, Veyran, Storm-Kiln partners | confirmed | Oracle derivations for Dramatic Reversal, Grinning Ignus, Chain of Smog, Haze of Rage, Reiterate + Seething Song. Chain of Smog combos with every magecraft engine. Added to §5, §6 and row notes |
| S3 Storm-Kiln + Archaeomancer + Sublime Epiphany chain | confirmed | My trace matches (Treasures 2k per loop vs cost 6). Named in §5; row notes on Epiphany and Archaeomancer |
| S4 Prismari Command "copy picks again" | confirmed | A copy keeps its modes (CR 707.10, unverified). Row fixed; Kolaghan's Command and Mystic Confluence aligned |
| S5 `core` vs §7 speed table | confirmed | Veyran and Comet Storm moved to `strong` and marked "(speed package)"; §7 defines the package; `core` is now 13 |
| S6 Lightning Greaves shroud anti-synergy | confirmed | Oracle "haste and shroud". Greaves moved to `strong` with a caveat; Swiftfoot Boots is now `core`; caveats on Whispersilk, the Palace, the Passage and Shizo |
| S7 omissions (20 items) | 19 confirmed, 1 disputed | Added 20 cards (item 8 is two cards): Roaming Throne, Helm of the Host, Strionic Resonator, Harmonic Prodigy, Village Rites, Thought Vessel, Mind Stone, Pongify, Rapid Hybridization, Abrade, Dismember, Opt, Consider, Faerie Mastermind, Flusterstorm, Expedite, Return the Favor, Cryptic Command, Plaza of Heroes, Sword of Feast and Famine. Net list change: 197 - 5 removed + 20 added = 212. **Disputed** Three Steps Ahead: its {3} token mode makes the §5 chain cost 4 instead of 6, so not added. Expedite: the "copy draws again" claim fails, because haste matters only before she attacks; the row is worded accordingly |
| S7 weak candidates | mostly confirmed | Removed Kozilek's Return (kills 2/2 engines: Storm-Kiln, Archmage Emeritus, Veyran, Guttersnipe are 2/2 in the pool), Evacuation, Insurrection, Najal, the Storm Runner; Blasphemous Act to `situational`. Kept Young Pyromancer, Murmuring Mystic and Kessig Flamebreather as cast-only tokens or pings (noted) |
| S7 "also worth a look" | partly disputed | Not added: Thousand-Year Storm, Galvanic Iteration, Double Vision (more copy multipliers, speed); Karlach, Fury of Avernus, Genji Glove (extra combats need a review ruling); Drown in Dreams, Brainsurge, Relic of Legends, Hall of the Bandit Lord (marginal over the listed cards); Conqueror's Flail added as a review flag |
| M1 Mox Amber text | confirmed | Row now says "any color among your legendaries" |
| M2 Thrill / Brainstorm / Palace arithmetic | confirmed, Palace partly disputed | Thrill: 4 cards for one discard; Brainstorm: 4 new cards seen. Palace: +RRRR for {1}{R} plus its own tap = net +1 (the verifier's +3 omits the activation cost); row fixed |
| M3 Mystic Confluence | confirmed | Row fixed |
| M4 legend rule | confirmed | Added to §1 and to the Ertai and Venser rows |
| M5 copy window | confirmed | §1 lists spells cast during resolution and Electrodominance's mid-combat sorcery |
| M6 budget pairs / labels | confirmed | Anger of the Gods, Ritual of Soot and Fireball are now `situational`; Commander's Sphere and Thrill notes added. The tier name is kept (the task brief requires it) with a legend note "price unknown" |
| M7 MLD / stax lists | confirmed | All names checked in the pool and added to §5 (the hosers as review flags) |
| M8 commander-free pairs | confirmed | Sanguine Bond + Exquisite Blood and Godo + Helm of the Host added; Birgi/Ignus and Hullbreaker in the §5 table |
| M9 Attractions | confirmed | 22 `Artifact — Attraction` rows (0 Contraptions found); §8.5 |
| M10 extra turns | confirmed | §5 rewritten as neutral readings A/B with the doc inconsistencies |
| M11 combo labels | confirmed | "unclear" changed to "floor-4 candidate" |
| M12 Kiki-Jiki variant card | confirmed | Clarified in §6 |

## Verification
All checks were read-only Python on `data/cache/` (run with `python -I`; helper scripts in the
session scratchpad under `azula/`, outside the repo). No network was used and no project file was
written except this report.

| Check | Command / script | Result |
|---|---|---|
| Pool integrity | `az_pool.py` | 18,563 rows, 18,563 unique names, 0 identity violations, 36 GCs, 48 Stickers, 22 Attractions |
| Spellbook summary | `sb_summary.py` plus a buildability script | 94 variants: R 60 / E 22 / S 7 / B 5; 28 with Azula + 2 cards, 66 with Azula + 3; 71 buildable; infinite-turn group 4 x 12 = 48 (asserted) |
| Candidate list | `az_validate.py` on the revised list | 212 cards, 0 duplicates, 0 missing, 0 identity violations, every budget-alternative target present; tiers core 13 / strong 100 / situational 79 / budget alternative 20 |
| Report re-parse | `az_final_check.py` parses this file's §3 tables | see the result line below |
| Game Changers | same script, §4 | 36/36 pool GCs named; 6 GC candidates |
| Other cited cards | same script, 206 names cited outside the tables | all in the pool and inside UBR. One deliberate non-pool name: Time Walk |

Final check result (`az_final_check.py` on this file, 2026-10-12):
- 212 rows parsed; 12 role headers sum to 212.
- **All names found in pool: yes. Color-identity violations: 0.**
- GC column matches the pool 212/212; budget-alternative targets 20/20 present.
- 36/36 pool GCs are in §4; 206/206 extra names are in the pool and in the text (after whitespace
  normalization).
- Leftover reverse-scan hits ("Island", "Mountain", "Exclude", "Redirect", "Breach", "Python",
  "Spellbook") are ordinary words that match card names, not citations.
- Length: 563 lines, above the ~450 target because of the verification additions.
