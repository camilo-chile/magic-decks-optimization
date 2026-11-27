# Pending purchases for the next iteration (2026-11-16)

Nothing is bought now (collection frozen). Everything below waits for the next iteration, which will include purchases and
is well in the future (owner, 2026-11-16). This is the list the next iteration starts from, with its own budget and stores
(`decks/phase2.json` `iteration`), live stock checks and the purchase rules of CLAUDE.md. Language: the bilingual decks take
English, Kilo takes Spanish only.

## 1. Loans and proxies (`restock.md`)

| Card | Language | Deck | Why |
|---|---|---|---|
| Arbaaz Mir (ACR) | EN | Toph | Lent from the owner's Standard deck on 2026-11-15; buying it returns the Standard copy |
| Ezio Auditore da Firenze (ACR 25) | EN | Ezio | Optional: the commander is a proxy and may stay one (his friends allow it) |

No other loan is open: the purchase of 2026-11-09 replaced every earlier loan (`loans.md`).

## 2. Tokens (`decks/reports/tokens-20261121.md`)

Rule (owner, 2026-11-16): each deck keeps its own token copies: at least 2 of a token when one game can make several of
it, 1 when it can make only one. Owned copies are shared out before buying. A surplus (owner, 2026-11-27) goes 2
per deck that makes the token, more when the deck makes many in a game; whatever is left stays stored.
Physical split on 2026-11-27: Clue Toph 4 (Tireless Tracker on every landfall) and Kilo 2; Incubator Kilo 2, the two Spanish
copies (the all-Spanish deck; the English copy stays stored); Copy 1 each to Azula, Ezio, Toph; Treasure 1 each to Azula and
Ezio (Toph's Tireless Provisioner takes Food until Treasures are bought).
Found by the owner on 2026-11-27 on the BACK faces of his double-faced tokens: he scanned each token by one face only, so
the export misses every back face (checked on Scryfall): Bird TEOC 3 (ES,
exact for Swan Song) to Azula, Thopter TEOC 16 (ES, exact for Hangarback Walker) to Kilo, Copy TTLA 2 (EN) to Azula,
Food TTLA 21 (EN) to Toph, a second Golem TEOC 14 (ES) to Kilo, a second Soldier TTLE 2 (EN)
to Toph; Insect TDSK 13 (black-green, flying) is not Springheart Nantuko's token and stays stored.
First step of the next iteration (owner, 2026-11-27): rescan the tokens recording BOTH faces of each card, then
recount the owned tokens (`scripts/token_needs.py`) before buying any: more back faces may cover this list.

| Token | Deck: copies (why) | Needed | Owned | To buy |
|---|---|---|---|---|
| Bird 2/2 blue, flying | Azula 2 (Swan Song, copied while Azula attacks) | 2 | 1 | 1 |
| Copy | Azula 2 (Helm of the Host each combat), Ezio 2 (Altaïr each attack), Toph 2 (Springheart Nantuko each landfall) | 6 | 4 | 2 |
| Treasure | Azula 2 (Storm-Kiln Artist, Big Score), Ezio 2 (Black Market Connections), Toph 2 (Tireless Provisioner) | 6 | 2 | 4 |
| Assassin 1/1 black, deathtouch and haste | Ezio 2 (Queen Marchesa each upkeep) | 2 | 0 | 2 |
| Assassin 1/1 black, menace | Ezio 2 (Aya of Alexandria, Ratonhnhaké꞉ton) | 2 | 1 | 1 |
| Shapeshifter 3/2 changeling | Ezio 2 (Black Market Connections each turn) | 2 | 1 | 1 |
| Bear 4/4 green | Toph 2 (The Earth King; Springheart Nantuko can copy it) | 2 | 1 | 1 |
| Food | Toph 2 (Tireless Provisioner) | 2 | 2 | 0 |
| Insect 1/1 green | Toph 2 (Springheart Nantuko) | 2 | 1 | 1 |
| Soldier 2/2 red | Toph 2 (Fire Nation Archers, repeatable) | 2 | 2 | 0 |
| Thopter 1/1 colorless artifact, flying | Kilo 2 (Hangarback Walker, one per counter) | 2 | 1 | 1 |
| Golem 9/9 colorless artifact | Kilo 2 (Titan Forge, repeatable) | 2 | 2 | 0 |
| Clue | Toph 2 (Tireless Tracker), Kilo 1 (Fateful Absence) | 3 | 6 | 0 |
| Incubator | Kilo 2 (Chrome Host Seedshark) | 2 | 3 | 0 |
| Beast 3/3 green | Toph 1 (Beast Within) | 1 | 1 | 0 |
| Human 1/1 white | Toph 1 (Stroke of Midnight) | 1 | 1 | 0 |
| Wrenn and Realmbreaker emblem | Toph 1 | 1 | 1 | 0 |

To buy: 14 tokens. Each must be the exact token of its card (name, type, P/T, colors, abilities), as always.

## 3. Full-art basics

Free full-art basics today (owned minus the copies the four decks hold; Scryfall `full_art` or borderless): Plains 10, Island 11,
Swamp 11, Mountain 11, Forest 13. The target stays 20 of each color in stock (CLAUDE.md; owner confirmed on 2026-11-16), so
the next purchase adds Plains 10, Island 9, Swamp 9, Mountain 9, Forest 7 (44 lands), full art only, NM to LP, EN/ES.

## 4. Staples a deck could play but has no free copy of

Candidates for the next optimization, not decisions: each deck still judges whether the card earns its slot. Owned copies
are all in decks or in the other language unless the row says so.

| Card | Owned | In | Copies to buy so every deck that fits can play it |
|---|---|---|---|
| Lightning Greaves | 0 | none | Azula, Ezio, Toph (EN), Kilo (ES): 4 |
| Counterspell | 0 | none | Azula, Ezio (EN), Kilo (ES): 3 |
| Fellwar Stone | 1 EN | Ezio | Azula, Toph (EN), Kilo (ES): 3 |
| Mind Stone | 1 ES | Azula | Ezio, Toph (EN), Kilo (ES): 3 |
| Commander's Sphere | 1 EN, 1 ES | Ezio, Kilo | Azula, Toph (EN): 2 |
| Path of Ancestry | 2 EN, 1 ES | Ezio, Kilo | Azula, Toph (EN): 1 (one EN copy is free for the other; it enters tapped) |
| Chromatic Lantern | 2 EN | Azula, Ezio | Toph (EN), Kilo (ES): 2 |
| Swiftfoot Boots | 2 EN | Azula, Ezio | Toph (EN), Kilo (ES): 2 |
| Mana Leak | 2 EN | Azula, Ezio | Kilo (ES): 1 |
| Octopus Form | 2 EN, both free | none | Kilo (ES): 1 (Azula and Ezio can take the free English copies) |
| Kolaghan's Command | 1 EN | Azula | Ezio (EN): 1 |

Sol Ring, Arcane Signet, Command Tower, Exotic Orchard and Swords to Plowshares are already in every deck that fits.

## 5. Cards the owner asked to evaluate in the next optimization

| Card | Deck | Owned | Why it is asked |
|---|---|---|---|
| Unleash Fury | Azula | 1 EN, free | Owner, 2026-11-27: cast while Azula attacks, the copy doubles her power twice (4 to 16) for the red mana firebending gives. Cut in iteration 2 as combat-only (`fire-lord-azula.build.md` section 8): it needs Azula unblocked, 16 is short of 21 commander damage, and the deck wins with copied instants. Weigh it against the weakest slot. |
