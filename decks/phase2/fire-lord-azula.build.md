# Fire Lord Azula: Phase 2 build notes (2026-11-02)

Upgrade of the Phase 1 list he plays today (`decks/scanned/fire-lord-azula.txt`), checked against his original list
(`data/raw/Azula.txt`). Pool: `data/model/phase2/pool-fire-lord-azula.json` (516 cards). Language policy `both`.
Gate: `decks/reports/consistency-fire-lord-azula.md` PASS (0 failures, 2 support WARNs, reasons in section 9).
Bracket: `scripts/check_phase2_bracket.py` PASS (0 Game Changers; live Scryfall `is:gamechanger` search on 2026-11-01, 53 cards,
none in the list; no extra turns, no mass land denial, no two-card infinite in the list).

## 1. Commander reading and rules points

Fire Lord Azula {1}{U}{B}{R}, 4/4. Firebending 2: when she attacks, add {R}{R} that lasts until end of combat. Whenever you cast
a spell while she is attacking, copy it (new targets allowed; a copied permanent spell becomes a token).
- Rewards: spells cast in HER combat window (from declare attackers to end of combat). Fuel: instants and flash cards in hand
  when she attacks, and mana in that window. Each cast spends a card and the copy only doubles its effect, so the hand empties
  fastest of his decks (owner): draw is the first need after the window itself.
- Window mana: {R}{R} per attack, only red, gone at end of combat unless a keeper holds it (Horizon Stone, Electro, Ozai,
  The Last Agni Kai). Fire Nation Palace adds firebending 4 more ({R}x4) the turn it is activated.
- Wins: copied burn (one Comet Storm with two kicks hits all three opponents twice), copied draw and removal as two-for-ones,
  commander damage pumped by copied pumps, Helm of the Host copies of her. She does not kill by herself.
- Dies to: targeted removal (the visible engine), wipes, blocks by bigger creatures, being tapped and open on the crack-back.
- Dependence: ATTACK ENGINE. Her trigger needs her attacking; it does not need her to connect (chump blocks do not stop the
  copies). Protection class attack_engine (6 to 8). She costs 4, so a recast comes the next turn: haste on the recast decides
  whether that turn counts (haste promotion test, section 3).
- Dead clauses: none on the commander. Copies are not cast, so Electro's {R} and Thermo-Alchemist's untap trigger only on the
  original spell; magecraft (Archmage Emeritus, Storm-Kiln Artist) says "cast or copy" and triggers twice.

Rules points to verify (load-bearing):
| # | Point | Status | What falls if wrong |
|---|---|---|---|
| R1 | Horizon Stone keeps firebending mana. Firebending ruling (2025-10-02): "Until end of combat, you don't lose this mana as steps end"; at the end of combat the mana would be lost, so Horizon Stone's replacement ("if you would lose unspent mana, that mana becomes colorless instead") applies. Horizon Stone ruling (2020-11-10): you retain unspent mana as steps and phases end and may spend it in a future step, phase or turn. | Confirmed by reading both rulings; no single joint ruling exists. | Horizon Stone as the window keeper; the burn route's "X reaches 8 to 12". |
| R2 | With Horizon Stone, mana made in an opponent's end step survives into my turn (as colorless), so lands can be tapped twice per turn cycle for generic costs (X of Comet Storm, Electrodominance, Pull from Tomorrow; Insight Engine). | Confirmed by the same Horizon Stone ruling. | Same as R1. |
| R3 | Copies trigger magecraft (Archmage Emeritus, Storm-Kiln Artist): Oracle "Whenever you cast or copy". Electro and Thermo-Alchemist trigger on cast only (Azula ruling: the copy is not cast). | Confirmed (Oracle and Azula rulings). | Draw and treasure counts per combat. |
| R4 | A copy skips additional costs but keeps X and kicker paid for the original (Azula rulings): copied Big Score and Thrill of Possibility draw without discarding; copied Comet Storm keeps X and the number of kicks. | Confirmed (Azula rulings). | Half-weight draw of Big Score, Thrill, Abandon; Comet Storm math. |
| R5 | A copied permanent spell resolves as a token (Azula ruling): Dualcaster Mage and Torrential Gearhulk cast in combat give two ETBs; the Gearhulk's free cast from the graveyard is itself cast while she attacks, so it is copied too. | First half confirmed (ruling); the second half is rules knowledge (a cast is a cast), not checked in a ruling. | Payoff value of Gearhulk. |
| R6 | Fire Nation Palace on Azula: two firebending instances trigger separately (Azula ruling: "Multiple instances ... trigger separately"). | Confirmed. | Window mana on big turns. |
| R7 | Day of Black Sun with X=0 destroys every created token (a token that is not a copy has mana value 0). | Rules knowledge, not checked in a ruling. | Board 1 answer for {B}{B}. |
| R8 | A Helm of the Host token of Azula has her abilities and is nonlegendary; two attacking Azulas copy each spell twice and add {R}{R} each. | Rules knowledge (each Azula has its own trigger), not checked in a ruling. | Combat route scaling. |
| R9 | Electrodominance's free cast happens during resolution, ignoring timing, and is a cast while she attacks, so it is copied. | Rules knowledge, not checked in a ruling. | Value of Electrodominance in the route. |
| R10 | Deflecting Swat is free while I control a commander (Oracle). | Confirmed. | Free protection on a tapped-out turn. |

## 2. Plan and backup

- **Plan.** Azula attacks every turn (haste and hexproof from equipment, counterspells and redirects behind her); while she
  attacks she copies every instant and flash spell cast with her firebending mana and the cost reducers, so each draw, removal
  and burn spell is a two-for-one; Horizon Stone, Electro and Ozai keep the leftover window mana; she closes against all three
  opponents with copied multi-target X burn (Comet Storm, Electrodominance) and with combat by herself, Helm of the Host copies of
  her and Ozai.
- **Backup** (same pieces): when Azula is answered or the board stalls, Thermo-Alchemist pings every opponent on each instant,
  Comet Storm and Electrodominance are cast uncopied with the mana Horizon Stone stores, Archmage Emeritus, Storm-Kiln Artist and
  Black Market Connections keep the hand and the mana full, and Ozai attacks with haste.
- Archetype: `spellslinger` (primary) + `combat_attackers` as `modifier`. Reason for "modifier": the combat profile supplies
  the window's support lines (haste, defense while tapped, combat draw, wipe insurance, evasion), but its fuel function
  `attackers` (12 creatures) is a creature-beatdown plan this commander does not need: her trigger needs ONE attacker, herself,
  and does not need to connect (`win-routes.md` 4, "attack or connect"). This is the worked pattern "window-limited payoff +
  attackers" of `references/archetypes.md`: spell density counted only on instants and flash, the higher draw of the two
  profiles, haste after a recast, protection, defense while tapped.

## 3. Profile table

| Function | Tier | Min | Target | Actual | Reason |
|---|---|---|---|---|---|
| Lands | band | 36 | 36 | 36 | Overlap of spellslinger 34 to 36 and combat 36 to 38. Nominal average MV 2.62 (X at 0) would allow the lean-low rule, but the X spells, Horizon Stone and three colors for a 4-MV gold commander want the land. |
| Ramp (by turn 3) | base | 12 | 12 | 12 | 10 + 2 for a 4-MV commander. 10 primary (5 two-mana rocks or Sol Ring, Dimir Locket, Bender's Waterskin, 3 reducers) + Black Market Connections (treasure from turn 4) + Glamdring (reducer). Only Sol Ring, Arcane/Izzet/Dimir Signet, Mind Stone and Nightscape Familiar speed Azula herself (44 % to hold one by turn 2); the reducers pay for the window. |
| Draw (nets cards) | base | 12 | 18 | 13 tags, about 11.5 weighted + copied cantrips | Owner: the MOST draw of his decks. Spellslinger 12 to 18 [J spend extension]. Full: Archmage, BMC, Fact or Fiction, Pull from Tomorrow, Lion Vulture, Gleam of Death, Insight Engine. Half alone, full when copied: Big Score, Thrill, Thirst, Abandon Attachments. 0.75: Azula On the Hunt (Clue per attack). Half: Frostcliff Siege (Jeskai mode). Copied cantrips (Brainstorm, Expedite, Frantic Search) add half each while she is out. Phase 1 had 4 real pieces. 81 % to see one by turn 5. |
| Spot removal | base | 8 | 10 | 10 + 3 counters (second tag) + 1 graveyard hate | Instant removal is also window fuel: copied, one card answers two permanents and triggers magecraft twice. |
| Wipes | base | 2 | 3 | 2 | Day of Black Sun and Ritual of Soot both spare Azula (MV 4) and the 4-MV engines; X=0 Day of Black Sun kills every token. |
| Commander protection | base (attack_engine) | 6 | 8 | 8 | Swiftfoot Boots, Champion's Helm, Octopus Form, Deflecting Swat, Narset's Reversal, Swan Song, Negate, Undying Malice. Layers: hexproof (3), redirect or bounce of the spell (2), counters (2, also stop wipes), death return (1). Propaganda carries the protection tag but guards the player, not Azula; not counted here. 66 % to hold one by turn 5. |
| spell_density | gate | 30 | 36 | 31 | Only instants and flash count (the window). 31 = 27 instants + Dualcaster, Gearhulk, Amphibian Downpour, Hidden Footblade. 79 % to hold 3+ by turn 5. Below target: the slots went to draw engines and defense that work without Azula. |
| spell_payoffs | gate (commander payoff, late 6) | 6 | 8 | 8 + 2 tutors | Azula, Archmage, Storm-Kiln Artist, Dualcaster Mage, Electro, Torrential Gearhulk, Helm of the Host, Narset's Reversal; 7 without Azula (no WARN). |
| through_wide_board | gate | 10 | 12 | 10 + Mystical Teachings | Comet Storm, Electrodominance, Thermo-Alchemist, Day of Black Sun, Ritual of Soot, Rogue's Passage, Haunted Cloak, Frostcliff Siege, Ozai, Electro. |
| through_big_creatures | gate | 10 | 12 | 12 + Mystical Teachings | Terminate, Hero's Downfall, Go for the Throat, Chaos Warp, Imprisoned in the Moon, Amphibian Downpour, Snap, Lightning Strike, Electrodominance, Comet Storm, Rogue's Passage, Day of Black Sun. |
| window_mana (declared, bridge) | declared late | 6 | 8 | 10 + Loyal Inventor | Makes or keeps mana inside her combat: Horizon Stone, Electro, Ozai, The Last Agni Kai (keepers); Fire Nation Palace, Azula On the Hunt (more firebending); Storm-Kiln Artist, Big Score (treasure); Frantic Search, Snap (untap lands, twice when copied). |
| haste | support | 4 | 6 | 5 (4.5 weighted) | Promotion test says PROMOTE (attack-only engine, MV 4), but the pool holds only these five haste givers (Swiftfoot Boots, Haunted Cloak, Hidden Footblade, Frostcliff Siege in Temur mode, Expedite). Fit fallback (`win-routes.md` 4): haste stays support and commander protection sits at its target 8. Equipment stays on the table after she dies, so a recast is hasty for the equip cost. |
| team_evasion | support | 6 | 8 | 4 (WARN) | See section 9. |
| defense_while_tapped | support | 4 | 6 | 7 | Propaganda, Haunted Cloak (vigilance), Loyal Inventor (vigilance), Thermo-Alchemist (0/3 defender), Lion Vulture (flier that draws without attacking), Octopus Form (untaps her after damage), Bender's Waterskin (mana on their turns for instants). |
| combat_draw | support | 4 | 6 | 4 | Archmage (draws on each cast and copy in the window), Lion Vulture, Azula On the Hunt, Frostcliff Siege (Jeskai). |
| wipe_insurance | support | 2 | 3 | 3 | Undying Malice, Swan Song, Negate (counter the sorcery wipe); equipment survives wipes. |
| attackers | support (from the modifier) | 12 | 16 | 3 (WARN) | See section 9. |
| cost_reducers | support | 2 | 4 | 4 | Goblin Electromancer, Stormcatch Mentor, Nightscape Familiar, Glamdring (up to 4 less on Azula, 6 with Champion's Helm). |
| Graveyard hate | floor | 1 | 1 | 1 | Soul-Guide Lantern (one card, or every opponent's graveyard, or a card). Phase 1 had none. |
| Answers to commanders | floor | 2 | 3 | 3 | Imprisoned in the Moon, Amphibian Downpour (neutralize, no tax reset), Chaos Warp. |
| Tutors | info | | | 2 | Mystical Teachings (instant or flash: finishers, payoffs, protection, removal; copied it finds two) and Loyal Inventor (artifact to the top: Helm, Horizon Stone, Boots). The engine is redundant (31 window spells), so tutors are spent on finishers. |

Fit check (each card once): ramp 10 + draw 12 + removal 8 + wipes 2 + commander protection 6 + payoffs outside draw/protection 5
+ route closers outside payoffs 4 + haste/defense pieces in no other line 4 + tutors 2 + Horizon Stone 1 = 54 of 63 non-land
slots; 36 + 54 = 90 of 99. Spell density is met inside those lines (27 of the 31 are draw, removal or protection).

Answers versus closers (red flag check): spot removal 10 + counterspells 3 + wipes 2 = 15 against 14 closers (Azula, Archmage,
Storm-Kiln, Dualcaster, Electro, Gearhulk, Helm, Narset's Reversal, Comet Storm, Electrodominance, Thermo-Alchemist, Ozai,
Unleash Fury, Azula On the Hunt). Reason it stays: in this deck instant removal is the fuel the commander converts (copied, one
card is two answers, two Archmage draws and two Storm-Kiln treasures), and the three counterspells are primarily Azula's
protection. The red flag targets one-for-one answers without threats; these are two-for-ones that feed the engine.

## 4. The list by function (how to use each card; when it is bad to draw)

Commander: **Fire Lord Azula**. Cast turn 3 to 4; equip Boots or Cloak before attacking; attack every turn, then cast the
instants in the declare blockers step (blocks known) or after damage.

**Ramp (10)**
- Sol Ring: turn 1; with a Signet, Azula on turn 3. Never bad early; weak late (it still pays X).
- Arcane Signet: turn 2, fixes the third color for Azula. Bad late only as a topdeck.
- Izzet Signet: turn 2; filters into {U}{R} for the double-pip window spells. Same.
- Dimir Signet: turn 2; {U}{B} for Hero's Downfall and Day of Black Sun. Same.
- Mind Stone: turn 2; late, crack it for a card. Never dead.
- Dimir Locket: turn 3 when no 2-drop rock came; late, sacrifice for two cards with stored Horizon Stone mana. Bad on turn 3 if Azula is castable instead.
- Bender's Waterskin: turn 3; untaps on each opponent's turn, so it is an instant-speed source for counters and Pull from Tomorrow. Weak late.
- Goblin Electromancer: turn 2; every instant in the window costs 1 less, so firebending pays for more. Dies to pings; cast it before Azula.
- Stormcatch Mentor: turn 2; same discount, hasty prowess body that chips in. Same.
- Nightscape Familiar: turn 2; blue and red spells (Azula included) cost 1 less; regenerates to block. Keep {1}{B} up when a wipe is likely.

**Draw (12 primary + Frostcliff Siege)**
- Archmage Emeritus: the best engine: in her window each instant draws two (cast and copy). Cast it on a turn you can hold {1}{U} or a counter for it; bad as the only creature on turn 4 against a pinger.
- Black Market Connections: turn 3; pick draw plus Treasure every turn, the 3/2 Shapeshifter only when you need a blocker; watch life against aggro.
- Fact or Fiction: end of the opponent's turn before yours, or in the window (two piles twice). Never bad.
- Pull from Tomorrow: at the end of the last opponent's turn with all lands (Horizon Stone keeps the rest); copied in the window it draws 2X. Bad on turn 2 to 3.
- Big Score: cast in the window: the copy draws two and makes two Treasures without the discard (R4). Discard an extra land. Weak with an empty hand outside combat.
- Thrill of Possibility: in the window, discard one, draw four. Outside combat it is a loot.
- Thirst for Knowledge: discard a spare artifact (Signet, Lantern) to keep two cards; best copied. Weak with no artifact in hand.
- Abandon Attachments: cheap rummage that becomes +1 card copied; bin extra lands. Weak alone late.
- Lion Vulture: turn 4 to 5; draws at your end step whenever an opponent lost life (Azula's attack, Thermo-Alchemist, any burn); keep it home as a flying blocker.
- Glamdring, Foe-hammer // Gleam of Death: cast Gleam of Death (mill six, take every instant and sorcery, about 2 to 3 cards), later cast Glamdring from exile and equip Azula: her spells cost up to 4 less. Bad if you need the equipment now and the adventure is wasted.
- Azula, On the Hunt: a second attacker with firebending 2 (more window mana in the same combat) and a Clue each attack. Bad into a board of bigger untapped creatures.
- Insight Engine: turn 3 to 5; activate at the end of each opponent's turn with Horizon Stone or spare mana; draws 1, 2, 3... Bad when behind on board.
- Frostcliff Siege: choose Temur (team trample, haste) when Azula needs haste or the board is wide, Jeskai (draw on combat damage) when she is safe and connecting.

**Spell payoffs and engines (5 + Horizon Stone)**
- Storm-Kiln Artist: two Treasures per spell in the window; the Treasures pay the next instant or Pull from Tomorrow. Bad early before Azula, fragile.
- Dualcaster Mage: flash in the window: it copies an instant and Azula copies the Mage, so the token Mage copies it again (three copies). Out of combat, copy an opponent's removal at your own target.
- Electro, Assaulting Battery: keeps red mana (firebending stays red after combat), adds {R} per instant you cast; when he leaves, pay X to burn a player. Flying blocker.
- Torrential Gearhulk: flash it in the window: the token copy also recasts an instant from the graveyard, and both recasts are copied (R5). Bad before turn 6.
- Helm of the Host: equip Azula: each combat a hasty nonlegendary Azula, so every spell is copied twice and she survives spot removal. Bad early (4 + 5 mana); Loyal Inventor finds it.
- Horizon Stone (proven role-player, bridge): keeps all unspent mana as colorless (R1, R2): firebending leftovers pay main-phase X and next-turn spells; tap lands at the last opponent's end step to double the mana for X spells. Bad on turn 5 with no Azula in sight.

**Commander protection (8)**
- Swiftfoot Boots: equip before attacking: hexproof and haste for a recast. Never dead while Azula lives.
- Champion's Helm: hexproof on a legendary, +2/+2 (6/6 Azula beats most blockers, raises Glamdring's discount to 6).
- Octopus Form: one mana: hexproof in response to removal, or after combat damage to untap her as a blocker; copied, it can hit a second creature.
- Deflecting Swat: free with a commander out: send the removal to their creature. Hold it on the turn you tap out.
- Narset's Reversal: against an instant or sorcery aimed at Azula: return it to its owner and keep a copy for yourself (copied in the window, twice).
- Swan Song: one mana answer to removal, burn or a sorcery wipe; the 2/2 Bird it gives is a small price.
- Negate: counters removal spells and wipes; hold {1}{U} on the turn after a big attack.
- Undying Malice: in response to destroy or a wipe on Azula: she returns with a counter, without the commander tax.

**Removal (10) and graveyard hate**
- Terminate: kill the biggest blocker after blocks; copied, a second creature dies. Never dead.
- Hero's Downfall: same, also hits planeswalkers.
- Go for the Throat: same for nonartifact creatures; check for artifact creatures.
- Chaos Warp: the answer to any permanent (enchantment, artifact, commander); copied it hits two.
- Imprisoned in the Moon: lock an opposing commander for good (it stays on the battlefield as a land, no tax reset).
- Abrade: 3 damage to a creature or kill an artifact (the only cheap artifact answer beside Chaos Warp). Weak late against big bodies.
- Lightning Strike: 3 (6 copied) to a blocker or a player at low life.
- Snap: bounce a blocker or a token (token dies); it untaps two lands (four copied), so it pays for itself in the window.
- Amphibian Downpour: flash it in the window: storm plus Azula's copy turn several creatures into vanilla 1/1 frogs; ideal against commanders.
- The Last Agni Kai: Azula (4/4) fights a smaller creature; excess damage becomes {R}, and red mana stays until end of turn (keeps firebending for main phase 2). Do not let the copy make her take lethal damage. Bad late against big boards.
- Soul-Guide Lantern: exile a key card from a graveyard on entry, sacrifice to exile every opponent's graveyard against recursion, or crack it for a card.

**Wipes (2)**
- Day of Black Sun: X=0 for {B}{B} kills every token (R7); X=3 clears small creatures and spares Azula and the 4-MV engines.
- Ritual of Soot: kills everything at MV 3 or less; Azula, Archmage, Storm-Kiln, Lion Vulture survive.

**Finishers and routes (5)**
- Comet Storm: the main kill: X plus two kicks names all three opponents; cast in the window it is copied (2X each). Early it is removal for X=2 to 3.
- Electrodominance: X to a player or creature and a free spell from hand; copied, two X and two free spells.
- Ozai, the Phoenix King: haste 7/7 trample with firebending 4; keeps unspent mana as red; with six floating mana he flies and is indestructible. Bad before turn 6.
- Unleash Fury: on an unblocked Azula in the window: copied, her power doubles twice (16, 24 with Champion's Helm): 21 commander damage. Bad when she is not out.
- Thermo-Alchemist: turn 2; ping every opponent each time you cast an instant (it untaps); blocks small attackers.

**Haste, defense while tapped, evasion (5)**
- Propaganda (proven role-player): turn 3; every creature that attacks you costs {2}; they hit the other players while Azula is tapped. Never dead.
- Haunted Cloak: equip {1}: vigilance (Azula stays home as a blocker), trample, haste on a recast.
- Hidden Footblade: {R} flash equipment: haste on a recast, first strike when it enters; equip on the turn she returns.
- Expedite: one mana: haste on a recast Azula plus a card. Weak when she is already on the table.
- Rogue's Passage (land): {4}: Azula unblockable when Unleash Fury or commander damage matters.

**Tutors and selection (4)**
- Mystical Teachings: at the end of an opponent's turn, fetch the instant the game needs (Comet Storm to kill, Negate to protect, Terminate); in the window the copy fetches a second.
- Loyal Inventor: turn 3: put Helm of the Host, Horizon Stone or Swiftfoot Boots on top; vigilant 2/3 blocker.
- Frantic Search: in the window it untaps three lands (six copied) and loots; out of combat it fixes a hand with extra lands.
- Brainstorm: in the window draw six and put back four; with Mind Stone or a shuffle it nets cards. Weak alone.

**Lands (36)**: 7 Island, 5 Mountain, 5 Swamp; Command Tower, Exotic Orchard (any color the table has); check and reveal lands
that are untapped by turn 2 to 3 (Drowned Catacomb, Dragonskull Summit, Sulfur Falls, Choked Estuary, Foreboding Ruins, Frostboil
Snarl); Smoldering Marsh and Sunken Hollow (untapped with two basics); pain lands (Shivan Reef, Sulfurous Springs, Underground
River); filter lands (Cascade Bluffs, Sunken Ruins, Darkwater Catacombs, Shadowblood Ridge: they turn one mana into two colored,
the double pips); Fire Nation Palace ({1}{R}: firebending 4 on Azula the turn you go big); Rogue's Passage (unblockable).

## 5. Cut log (Phase 1 list he plays today)

Proven role-players (Horizon Stone, Propaganda) are both IN; none left out.

| Card out | Function it served | Count after the cut (min) | Replacement | Reason |
|---|---|---|---|---|
| Ember Island Production | none (combo with Dualcaster) | n/a | Pull from Tomorrow | L7: a mini-combo piece that waited all game; dead alone at 5 mana sorcery. |
| Entomb | none | n/a | Thrill of Possibility | No reanimation; Gearhulk targets are instants already in the graveyard. Orphan. |
| Goblin Bombardment | noncombat damage | burn route 3 closers | Thermo-Alchemist | 13 creatures and few tokens: no fodder. Thermo pings all three opponents per instant. |
| Godo, Bandit Warlord | tutor for Helm, extra combat | tutors 2 | Lion Vulture | 6-mana 3/3 dead alone most games; Loyal Inventor keeps the Helm tutor. Loses the late Godo + Helm infinite combats (legal, not a reason to keep a dead 6-drop). |
| Lo and Li, Twin Tutors | tutor (Lesson, Noble) | tutors 2 | Azula, On the Hunt | 5-mana 2/2 at sorcery speed; its best target is in the list now. |
| Reckless Handling | artifact tutor | tutors 2 | Horizon Stone | Sorcery with random discard; Loyal Inventor does the job. |
| Solve the Equation | tutor | tutors 2 | Insight Engine | Sorcery tutor outside the window; Mystical Teachings stays. |
| Banefire | finisher | burn route 3 (Comet Storm, Electrodominance, Thermo) | Unleash Fury | Single target at sorcery speed; one player per cast. |
| Mana Leak | counter | protection 8 (6) | Swan Song | Bad late (they pay 3); Swan Song costs 1 and counters removal and sorcery wipes. |
| Consider | cantrip | density 31 (30) | Thirst for Knowledge | Cantrip, not draw; the owner's need is draw that nets cards. |
| Opt | cantrip | density 31 (30) | Abandon Attachments | Same. |
| Ponder | cantrip (sorcery) | n/a | Soul-Guide Lantern | Not castable in the window; the list had no graveyard hate. |
| Heartless Act | removal | spot removal 10 (8) | Hidden Footblade | Removal surplus; answers already outnumber closers; haste was under min. |
| Fatal Push | removal | 10 (8) | Haunted Cloak | Bad late (MV 2, revolt only with a Treasure); Cloak gives haste, vigilance and trample. |
| Ultimate Price | removal | 10 (8) | Propaganda | Misses multicolored commanders; Propaganda is a proven role-player. |
| Aether Gale | one-sided bounce | wipes 2 (2) | Dimir Locket | 5-mana sorcery outside the window; Day of Black Sun X=0 handles tokens; ramp needed its 12th piece. |
| Redirect Lightning | protection | protection 8 (6) | Expedite | Protection at target with cheaper pieces; haste was under min. |
| Canyon Slough (land) | land | 36 | Smoldering Marsh (owed, counts as owned) | Always tapped; the Marsh enters untapped with two basics. |

Original-list cards reconsidered and left out: Coastal Piracy (draw needs connection, Lion Vulture does it without combat),
Malcolm, Fists of Flame, Cunning Maneuver, Run Amok, Fire Nation Attacks (window cards, lower value than the ones chosen),
It'll Quench Ya (soft counter), Zuko's Exile (5 mana), Firebender Ascension, Combustion Man, Koh, Zuko Exiled Prince, Cruel
Administrator (creature plan the commander does not need), Royal Assassin, Labyrinth Adversary, Commander's Sphere.

## 6. Loans

- Used: none. Propaganda and Hidden Footblade come from his own collection (free copies), not from the Standard binder.
- Proposal to evaluate (the list keeps its current card until he accepts): **Overpowering Attack** (loan candidate, class
  evaluate: no stock at Game of Magic Singles on 2026-10-31, the replacement waits for a restock). Need: a second combat
  window per turn; freerunning {2}{R} works with commander combat damage, so after Azula connects it untaps her and gives a new
  combat: a second firebending, a second round of copies. Replacement situation: no stock in the iteration's store, no price
  read. Fallback: the list as is; if accepted it replaces Brainstorm (the weakest window card).

## 7. Scarce copies (for `scripts/assign_copies.py`)

| Card | Copies | Who may want it | Where it adds most |
|---|---|---|---|
| Command Tower | 3 (1 en, 2 es) | Toph, Ezio, Azula, Spanish deck | Any 3-color deck equally; Azula takes the English copy; the Spanish deck is the one left without. |
| Hidden Footblade | 1 free (+1 loan, no stock) | Ezio (Assassin equipment), Azula | Ezio if he keeps an Assassin equipment theme; for Azula it is haste piece 4 of 5: without it haste drops to 3.5 (WARN), fallback Mechanical Glider (pool) for evasion. |
| Narset's Reversal, Swan Song, Negate | 1 each (Spanish only) | Azula, a blue Spanish deck | Azula: copied in the window and her protection layers. |
| Pull from Tomorrow, Thrill of Possibility, Thirst for Knowledge, Insight Engine, Mind Stone | 1 each (Spanish only) | Azula, a blue or red Spanish deck | Azula (her draw is the owner's top need). |
| Torrential Gearhulk, Helm of the Host | 1 each (Spanish only) | Azula, a Spanish deck | Azula (both double with her copies). |
| Soul-Guide Lantern | 2 (es; Toph holds 1) | Toph, Azula, Spanish deck | Toph and Azula, one each; the Spanish deck would need a third. |
| Propaganda | 2 free (+1 loan) | Azula, Ezio | One each; not scarce unless a third deck wants it. |

Cards I share with Ezio's current list hold two copies each (Brainstorm, Dualcaster Mage, Loyal Inventor, Mystical Teachings,
Swiftfoot Boots, Terminate, Dragonskull Summit, Drowned Catacomb, Frostboil Snarl, Sunken Hollow, Smoldering Marsh: Ezio the
English one, Azula the owed Spanish one), so they are not in conflict.

## 8. Purchase proposals (iteration 2: Game of Magic Singles only; owner update 2026-11-02: the Spanish deck may use up to 5,000 CLP of the 10,000, so Toph, Ezio and Azula share about 5,000; the lead verifies live stock and decides)

Ranked by impact on this deck. The list is complete without any of them (every card above is owned).

| Rank | Card | Need | Price hint | Plays instead of |
|---|---|---|---|---|
| 1 | Talisman of Dominance (or Indulgence, Creativity) | A 2-mana rock: Azula on turn 3 rises from 44 % to about 50 % with a T2 accelerant, and the 12th ramp piece stops being a 3-mana Locket that competes with her cast turn | No reading of a normal printing (only a borderless foil, 12,840 CLP, 2026-10-17); usually cheap, the lead checks | Dimir Locket |
| 2 | Arcane Denial | A 2-mana counter for ANY spell: protects Azula against creature-based removal and abilities' sources, and stops wipes; adds a window-castable card (density 31 to 32 if it replaces a non-instant) | 2,840 CLP NM (OTC, GoM reading 2026-10-17, old) | Brainstorm |

If the bilingual share cannot cover both, take rank 1 only; if it covers neither, nothing is lost (the list passes as it is).

## 9. WARN reasons and dead clauses

- **attackers 3 of 12** (support line from the modifier): Azula's trigger needs one attacker, herself; other attackers do not
  power the copies. The line counts the bodies that attack beside her (Azula On the Hunt, Ozai, Electro); Helm of the Host adds a
  token Azula every combat. Filling 12 would turn 9 window spells into creatures and cut the density the plan runs on.
- **team_evasion 4 of 6**: her engine triggers on attacking, not on connecting (`win-routes.md` 4: do not over-weight evasion for
  attack triggers). Evasion matters only for the commander-damage closer; Board 1 is beaten by noncombat burn and the token wipes
  instead. Pieces: Rogue's Passage, Haunted Cloak, Frostcliff Siege, Ozai. If he sees Azula chump-blocked every turn, Mechanical
  Glider (pool, 1 mana, flying) is the swap for Brainstorm.
- Dead clauses: Glamdring's discount needs an equipped creature (put it on Azula); Frostcliff Siege's two modes are exclusive
  (choose at entry); Black Market Connections' Shapeshifter is a blocker only; Ozai's flying needs six floating mana (Horizon Stone
  helps); The Last Agni Kai's mana needs excess damage (bonus only).

## 10. Reference boards

- **Board 1: eight sacrificeable 1/1s.** Day of Black Sun for X=0 ({B}{B}) or Ritual of Soot clears them; Comet Storm copied
  hits all three players over the board; Thermo-Alchemist pings past them; Rogue's Passage, Haunted Cloak or Frostcliff trample
  put Azula's damage through; Ozai flies with six floating mana. Chump blocks do not stop the copies, so the engine keeps
  drawing (Archmage) and making Treasures while they chump. Risk: pingers kill the 2-toughness engines (Archmage, Storm-Kiln,
  reducers); cast them after Azula's protection is up.
- **Board 2: two creatures bigger than Azula.** After blocks, one Terminate, Hero's Downfall or Go for the Throat cast in the
  window kills the blocker and its copy kills the second; Amphibian Downpour and Imprisoned in the Moon neutralize; Snap copied
  bounces both; Electrodominance and Comet Storm for X; Champion's Helm makes her 6/6; Rogue's Passage skips them.
- **One sweeper turn:** equipment, Horizon Stone, BMC, Propaganda, Insight Engine and Glamdring survive; Azula returns with Undying
  Malice or is recast with haste from the equipment left on the table; Swan Song and Negate counter the sorcery wipe; Ozai with
  six floating mana is indestructible.

## 11. Mana

- Colored sources (lands; rocks apart): blue 19 (7 Island + 12 nonbasic), black 18 (5 Swamp + 13), red 17 (5 Mountain + 12).
  Rocks: Arcane Signet and Bender's Waterskin (any), Izzet Signet (U R), Dimir Signet and Dimir Locket (U B). Karsten for a gold
  4-drop with one pip of each color: 16 + 1 = 17 per color: met. Red double pips (Comet Storm, Electrodominance, Dualcaster,
  Electro) are paid mostly by firebending {R}{R} in the window.
- Tapped lands: none always tapped (Canyon Slough out). Conditional: Smoldering Marsh and Sunken Hollow (two basics), Fire Nation
  Palace (a basic), three check lands, three reveal lands. Four filter lands need one mana of input.
- Curve (X at 0): MV1 8, MV2 25, MV3 18, MV4 9, MV5 1, MV6 2; average 2.62; 33 cards at MV 2 or less; three X spells scale up.
- Odds (99 cards, no mulligan): 2 to 4 lands in 7 cards 74 % per look, about 93 % with the free redo; 4 lands by turn 4 62 %;
  a ramp piece by turn 3 67 %; a repeatable draw engine by turn 5 48 %, any draw piece 81 %; a haste piece by turn 5 48 %
  (the first cast needs none); a protection piece by turn 5 66 %.

## 12. Open questions for the owner

1. Coastal Piracy or Lion Vulture: did Coastal Piracy draw for Azula in your games? I chose Lion Vulture (draws without needing
   to connect).
2. Godo + Helm of the Host (infinite combats, late and legal) is out because Godo is a dead 6-drop alone; do you want the line back
   instead of Brainstorm?
3. Overpowering Attack as a loan (section 6): accept or reject.
4. Do you see Azula chump-blocked often (team_evasion WARN)? If yes, Mechanical Glider goes in for Brainstorm.
