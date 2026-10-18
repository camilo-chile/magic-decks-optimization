# Locked cards (mechanism kept, list empty since 2026-10-18)

`decks/locked.txt` holds the cards the owner wants to keep: each must be in **at least one** of the project's
Commander decks (any number of decks, not tied to its original deck). On 2026-10-18 the owner emptied the list:
no card is mandatory and the optimizer may adapt every deck freely. The mechanism stays for future restrictions:

- Add one `1 Card Name` line per card (English names, comments start with `#`).
- `scripts/check_list.py` then prints the locked cards each list holds and those that fit its color identity but are
  missing; `scripts/price_candidates.py` flags them in the pools (`locked: true`) and adds a "Locked held" column.
- The optimizer (Phase 8 step 3) must then cover every locked card in at least one deck (`allocation_model.locked_coverage`).
- Owned copies: one physical copy sits in one deck, so a card locked in two decks needs two copies.

The former list (32 cards: 10 only Toph can play, 8 only Azula can play, 13 free ones) and its color-identity table are
in version control history: `git show 323cf77:decks/locked.txt` and `git show 323cf77:decks/locked.md`.
