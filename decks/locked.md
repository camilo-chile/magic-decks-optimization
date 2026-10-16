# Locked cards (Phase 6, O2)

Owner decision, 2026-10-16 (clarified the same day): every card in `locked.txt` must be in **at
least one** of the project's Commander decks, and may be in more than one. The rule applies to
every Commander deck the project has (three today; if a fourth is added, it applies to four). A
card is not tied to the deck it came from: it may move to another deck when that helps both,
replacing a card there. The owner may drop one on a strong recommendation.

Constraint for the optimizer (Phase 8): for every locked card, the number of decks that play it
is at least 1 (no upper bound other than the copies owned), each deck holds one copy per card
(singleton), a copy in two decks needs two physical copies (the ManaBox export in
`data/raw/ManaBox_Collection.csv` is the source; 2026-10-16: Redirect Lightning 2 copies, Toph and
Azula; Rogue's Passage 2, Toph and Azula; Swiftfoot Boots 1, Azula), and the card must fit the color
identity of each deck that plays it. Layer A of each deck is evaluated with the moved cards.

Identities: Toph R/G/W, Azula U/B/R, Alexios mono-red (Scryfall `color_identity`, 2026-10-16).

| Group | Cards | Fits |
|---|---|---|
| Toph only (green or R/W identity) | Ashaya, Soul of the Wild; Annie Joins Up; The Earth King; Terrasymbiosis; Bumi, Unleashed; Arbaaz Mir; Heaped Harvest; Seismic Tutelage; Wrenn and Realmbreaker; Inscription of Abundance | Toph (10 cards) |
| Azula only (blue or B/R identity) | Royal Assassin; Imprisoned in the Moon; Aether Gale; Torrential Gearhulk; Ozai, the Phoenix King; Octopus Form; Frostcliff Siege; Assassin Gauntlet | Azula (8 cards) |
| Red or colorless, free to move | Mindslaver; Redirect Lightning; Secret Tunnel; Deflecting Swat; The Stasis Coffin; Hidden Footblade; Rogue's Passage; Labyrinth Adversary; Bender's Waterskin; Swiftfoot Boots; Combustion Man; Electro, Assaulting Battery; Horizon Stone | Toph, Azula or Alexios (13 cards) |

Layer A on the lock sets (target Bracket 3, bulk `oracle-cards-20261011210156`): the Toph set is
floor 3 (Bumi, Unleashed with Ashaya is a late two-card combo; Mindslaver and The Stasis Coffin with
Toph are review notes), the Azula set floor 1, the 13 free cards in Alexios floor 1. All 32 are
Commander-legal and none is a Game Changer.

Names given by the owner in Spanish were resolved to: Vendaval del éter = Aether Gale, Mecatitán
torrencial = Torrential Gearhulk, Adversario del laberinto = Labyrinth Adversary, Guantelete del
asesino = Assassin Gauntlet, Inscripción de abundancia = Inscription of Abundance; "Wrenn" =
Wrenn and Realmbreaker (the one in his Toph list).
