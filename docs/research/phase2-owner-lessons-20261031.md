# Owner lessons for building the Phase 2 decks (2026-10-31)

Source: the owner's messages of 2026-10-26, 2026-10-30 and 2026-10-31, his two games with the Phase 1 Ezio list, his earlier
games with his own Toph and Azula lists, and the comparison of those original lists (ManaBox export of 2026-10-18) with the
Phase 1 finals. This is signal from few games, not proof, but it is the only real-game evidence the project has. Every deck
builder reads it; a builder that goes against one of these lessons writes the reason, and the owner reviews it.

| # | Lesson (owner) | Evidence | What the builder must do |
|---|---|---|---|
| L1 | One consistent, solid, robust strategy; never a mix of plans with one to three support cards each | Ezio (Salt 7.7) lost two games heavily to a deck Salt rates far lower; 2 reanimation spells for a graveyard plan, no vehicles for a vehicle clause, about 2 equipment for an equipment clause | Pass the consistency gate (`scripts/plan_density.py`) |
| L2 | The ratios follow the strategy, not a template: having far more of something than another deck can be right | Toph (landfall, rarely attacks) needs an "absurd" amount of ramp and ways to make lands enter again and again, ideally several per turn, and needs no haste; Azula (casts instants) empties her hand fastest and needs the most draw; Ezio and Azula (win by attacking) need haste, evasion and protection | Write the deck's archetype profile (what each function must reach for THIS plan) before choosing cards; the generic template is only a floor for safety functions |
| L3 | Decks that win by attacking must make the damage connect, keep their creatures alive, attack early (haste) and defend while tapped | Ezio: no creature had haste and nothing gave it; menace did nothing against 8 chump-blocking goblins; fragile creatures; wide open after attacking. Team evasion (Cover of Darkness: creatures of the chosen type have fear) and attack taxes or vigilance (Propaganda) were missing | Combat decks declare and fill: team evasion or ways past a wide board, ways past bigger creatures, haste enablers, protection for attackers and commander, defense while tapped |
| L4 | Commander dependence differs by deck | Ezio and Azula need their commander attacking every turn; Toph lives on landfall and its commander matters less | The protection count follows the dependence on the commander |
| L5 | A card's value depends on this deck's curve and mechanics, not on being a "staple" | Everflowing Chalice in Ezio: cast on turn 5 for two counters, two colorless mana for the rest of the game, the turn wasted; the same rock is good in a proliferate deck | Judge every card in the context of the plan, the curve and the turn it will be cast |
| L6 | The cards that won his games were cut by a score-driven builder | Cut from his Toph by Phase 1: The Earth King ("if it resolved, I won"; fetches basics when power 4+ creatures attack) and Seismic Tutelage (doubles the +1/+1 counters of the enchanted creature when it attacks: "almost a win condition" for a counters deck). Cut from his Azula: Horizon Stone (keeps the firebending mana that empties at end of combat) and Propaganda. Never included in Ezio: Eagle Vision (draw three, freerunning {1}{U}: "the best draw card for Ezio") and Cover of Darkness (team fear for Assassins; not available, see below) | Proven role-players are strong priors: to leave one out, write why; cards that make the plan work are judged by the plan, never by the Salt score |
| L7 | Dead clauses and mini-combos rot in hand | Adéwalé's vehicle clause with no vehicles; Winter Soldier's equipment clause with about two equipment; Ember Island Production waiting for Dualcaster Mage all game | Name every dead clause; no card whose only use is a two-card combo |
| L8 | The pod produces two reference boards | One opponent with 8 or more 1/1 goblins that sacrifice themselves; the others with two or more big creatures | Every list states how it wins through each board |
| L9 | Commander Salt is not the measure of a good deck | Ezio 7.7 lost to a lower-rated deck | Salt only breaks ties between lists that pass the gate and the review |
| L10 | The guide says how to USE each card in this deck | Play review of 2026-10-26 | Guides by card, as in Phase 1 |

## Constraints that shape the lessons in Phase 2
- No purchases: only owned cards. Eagle Vision and Cover of Darkness sit in the binder of his Standard decks ("Assassin's
  Creed"), which the rules of 2026-10-26 exclude. Owner's answer (2026-10-31): one English Eagle Vision (ACR 17) may go to Ezio
  as a loan, to be replaced at the next purchase (`decks/phase2.json` "borrowed", `decks/phase2/restock.md`); Cover of
  Darkness may NOT be taken, so Ezio's team evasion must come from other owned cards. Propaganda: 2 copies outside that binder
  in the 2026-10-18 export.
- The cards cut by Phase 1 from his original lists are still owned (they reach the pools when he scans the rest of the
  collection), so the builders reconsider them, starting with the landfall engines and payoffs of Toph.

## Appendix: what Phase 1 changed in his own lists (2026-10-18 export against the scanned Phase 1 finals)
Toph: 45 cards cut, 42 added.
- Cut: Aang, Air Nomad; Airbender's Reversal; Appa, Steadfast Guardian; Avatar Destiny; Awakening of Vitu-Ghazi; Badgermole;
  Banefire; Barrels of Blasting Jelly; Bitter Work; Blasphemous Act; Blossoming Tortoise; Bumi, Eclectic Earthbender;
  Cabaretti Courtyard; Darksteel Citadel; Deflecting Swat; Druid Class; Elemental Teachings; Evolving Wilds; Horrid Vigor;
  Hour of Revelation; Jungle Shrine; Karn's Sylex; Meteor Sword; Mindslaver; Moraug, Fury of Akoum; Mycosynth Wellspring;
  Omnath, Locus of Rage; Rockalanche; Roiling Regrowth; Rustvale Bridge; Sandbenders' Storm; Secret Tunnel; Seismic Tutelage;
  Slagwoods Bridge; Solemn Simulacrum; Stocking the Pantry; Terramorphic Expanse; The Boulder, Ready to Rumble; The Cave of
  Two Lovers; The Earth King; Thornglint Bridge; Titania, Nature's Force; Titania, Protector of Argoth; Urza's Cave; Vibrant
  Cityscape.
- Added: Arcane Signet; Beast Within; Bender's Waterskin; Boros Locket; Brightglass Gearhulk; Chord of Calling; Chromatic
  Lantern; Clifftop Retreat; Earth Kingdom General; Everflowing Chalice; Exotic Orchard; Fateful Absence; Fortified Village;
  Furycalm Snarl; Game Trail; Goblin Bombardment; Great Divide Guide; Hardlight Containment; Haru, Hidden Talent; Haystack;
  Hunter's Bow; Liquimetal Coating; Lotus Cobra; Ragost, Deft Gastronaut; Rampant Growth; Reckless Handling; Rocky Rebuke;
  Rugged Prairie; Rumble Arena; Sabotender; Sakura-Tribe Elder; Seismic Sense; Selesnya Signet; Shared Roots; Sol Ring;
  Soul-Guide Lantern; Springheart Nantuko; Stroke of Midnight; Talisman of Impulse; Tireless Provisioner; Valakut Exploration;
  Zuran Orb.

Azula: 40 cards cut, 49 added (the counts differ because some cards changed copies).
- Cut: Abstergo Entertainment; Artful Takedown; Assassin Gauntlet; Azula Always Lies; Azula, on the Hunt; Coastal Piracy;
  Combustion Man; Commander's Sphere; Cruel Administrator; Cunning Maneuver; Dragonfly Swarm; Evolving Wilds; Fire Nation
  Attacks; Fire Nation Sentinels; Fire Sages; Firebender Ascension; Fists of Flame; Hidden Footblade; Horizon Stone; It'll
  Quench Ya!; Koh, the Face Stealer; Labyrinth Adversary; Lion Vulture; Malcolm, the Eyes; Most Valuable Slayer; North Pole
  Patrol; Path of Ancestry; Propaganda; Royal Assassin; Run Amok; Solstice Revelations; Terramorphic Expanse; Thermo-Alchemist;
  Thrill of Possibility; Unexplained Disappearance; Unleash Fury; Vibrant Cityscape; Waterbender Ascension; Zuko's Exile;
  Zuko, Exiled Prince.
- Added: Banefire; Black Market Connections; Brainstorm; Canyon Slough; Champion's Helm; Consider; Darkwater Catacombs;
  Deflecting Swat; Dragonskull Summit; Drowned Catacomb; Dualcaster Mage; Ember Island Production; Entomb; Exotic Orchard; Fact
  or Fiction; Fatal Push; Frantic Search; Frostboil Snarl; Glamdring, Foe-Hammer; Go for the Throat; Goblin Bombardment; Godo,
  Bandit Warlord; Heartless Act; Helm of the Host; Lightning Strike; Lo and Li, Twin Tutors; Loyal Inventor; Mana Leak; Mind
  Stone; Mystical Teachings; Narset's Reversal; Negate; Nightscape Familiar; Opt; Ponder; Reckless Handling; Ritual of Soot;
  Shadowblood Ridge; Shivan Reef; Solve the Equation; Storm-Kiln Artist; Stormcatch Mentor; Sulfur Falls; Sulfurous Springs;
  Sunken Hollow; Sunken Ruins; The Last Agni Kai; Ultimate Price; Underground River.

Ezio was a new deck in Phase 1 (no original list to compare).
