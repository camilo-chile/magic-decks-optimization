# Owner's card review of the built decks (2026-11-14)

After playing and reading the four decks built on 2026-11-09, the owner flagged the cards below. He does NOT say each
choice was wrong; he says better cards seem to have left than came in, and he wants every one of these decisions
re-examined in the collection-only optimization (every deck, whatever the model).

**Rule for every builder and reviewer of the next optimization:** each card below that fits the deck's colors gets an
explicit verdict in the build notes (section "Owner's cards"): IN, or OUT with a written reason of weight that names the
card that does the job better and why (Oracle text, the deck's plan, 3-4 player pods). "Not enough slots" or "lower EDHREC
synergy" is not a reason by itself. A card the owner calls weak but that stays IN needs the same written reason.

Free copies today: `data/model/phase2/pool-<slug>.json` (`held_by`, `free_by_language`), from the decks as built.

## Cards he finds weak or doubtful (currently IN)

| Card | Deck now | His point |
|---|---|---|
| Merciless Harlequin ("Arlequín") | Ezio | He considers it very bad and is surprised it is in. |
| Waterbending Lesson | Azula (EN), Kilo (ES) | Waterbend taps creatures and artifacts to pay; does the deck have enough of them to use it well? |
| Evie Frye (owned, out) / Jacob Frye (in Ezio) | Ezio | Mixed: Evie is weak alone, but with Jacob (her partner) either one entering draws a card; if one is played, the other may be worth it. |

## Cards he was surprised to see OUT

| Card | Deck it was in (or fits) | His point |
|---|---|---|
| Torrential Gearhulk ("Mecatitán Torrencial") | Azula | His best Azula card before the optimization rounds; won him two games ("if I draw it, I win"): flash, copies itself, and recasts instants from the graveyard, which almost nothing else does. THE most surprising cut. |
| Frostcliff Siege | Azula | CONSTANT card draw; its replacement draws once. Second most surprising cut. |
| Aether Gale ("Vendaval del éter") | Azula | Clears the board without touching our creatures: a finishing blow with no blockers left. |
| Imprisoned in the Moon | Azula | Neutralizes a commander without changing its zone, so it cannot be recast. |
| Mana Leak | Azula (now in Ezio; a second copy is free) | Excellent counter; helped in every game he played it. |
| Mystical Teachings | Azula (in; a second copy is free) | Tutors the right instant at instant speed, or Torrential Gearhulk. |
| Return the Favor | Azula / Ezio | Protection, or copying a spell for more damage. |
| The Revelations of Ezio | Ezio | A removal plus a reanimation; slow, but he found it useful (he knows the deck no longer recurs creatures). |
| Lydia Frye | Ezio | Unblockable; dies to a double block of 1/1s, but useful in an assassin deck. |
| Tome of Legends | Ezio (colorless) | CONTINUOUS card draw. |
| Royal Assassin | Ezio | Kills repeatedly without attacking; draws a removal spell from an opponent. |
| Mortify | Ezio | One opponent's commander has protection from monocolored; Mortify is two colors and also hits enchantments. |
| Utter End ("Fin absoluto") | Ezio | Like Mortify, and it exiles. |
| Deadeye Navigator | Ezio | Re-triggers enter-the-battlefield effects (Adéwalé and others). He knows it was questioned before. |
| Commander's Sphere | Ezio (now only in Kilo; an English copy is free) | Any color of mana; he thinks it belongs in every deck that can play it, Ezio above all. |
| Hardened Scales | Toph | Toph lives on earthbend (+1/+1 counters); Scales is like an Ozolith for her. |
| Inscription of Abundance | Toph | Life gain, removal and pump in one card. |
| The Stasis Coffin | Toph | Total protection; can decide a game. The Toph cut that surprised him most. |
| Alibou, Ancient Witness | Toph | He liked it (his opinion; it is mana-expensive). |

## Multiple copies (owner, 2026-11-14, standing rule)

The rule covers the WHOLE collection, not only his three examples. On 2026-11-14 it held 309 non-basic cards with two or
more copies, 138 of them with three or more, and 64 played by a deck with spare copies in a binder: Fatal Push 1 of 3,
Evolving Wilds 1 of 5, Rampant Growth 1 of 4, Brainstorm, Entomb, Mana Leak, Mystical Teachings and Commander's Sphere 1
of 2, and others; the pools' `free_by_language` lists every one. The optimization runs deck by deck in series, and a card
one deck takes stays an option for every later deck while a copy is left. A strong staple with spare copies should be considered for every deck that can
play it, never left in one deck while its other copies sit in the binder.

## Cards left out with no written reason in iteration 3 (owner, 2026-11-15)

The next iteration must give each one a written verdict:
- Toph: Blossoming Tortoise (the most doubtful cut: a land returns every time it enters or attacks), Embodiment of Fury,
  Embodiment of Insight, Horrid Vigor.
- Ezio: Lion Vulture, Senu, Keen-Eyed Protector.
- Any white deck: Exorcise.

## Cards that fell between decks in iteration 3 (owner question, 2026-11-15)

The serial order (Azula, Ezio, Toph, Kilo) with each deck frozen after its build left good free copies in no deck. The next
iteration re-offers every card a later deck freed to the earlier decks, and checks `free_by_language` before writing "taken
by another deck" as a reason.
- Kolaghan's Command (1 EN, free): Azula left it "for Ezio" (build notes, "Not claimed, on purpose"); Ezio then cut it for a
  36th land, which became Secret Tunnel. An instant with two modes (2 damage, discard, raise dead, artifact kill) that Azula
  copies while attacking.
- Chromatic Lantern (2 EN; Ezio holds one, one free): Azula's cut log gives "Ezio's, or 3-mana rocks"; the first half was
  wrong (a second copy is free) and Azula's gate warns ramp 10 against the 12 its profile asks.
- Octopus Form (2 EN, both free; owner, 2026-11-15: "excellent protection"): Azula cut it for Chromatic Lantern on
  2026-11-15. The lead's own reading: the weakest call of that pair; the next iteration weighs Octopus Form back in Azula
  for a basic land (35 lands with 12 mana rocks and ramp). Ezio left it out (protection at 8, blue not always up in five
  colors); Kilo cannot play it (no Spanish copy).
