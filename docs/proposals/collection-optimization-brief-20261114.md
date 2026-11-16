# Collection-only optimization brief (Phase 2 step 10, 2026-11-14)

Iteration 3 (owner, 2026-11-14). Iteration 1 was the first purchase. Iteration 2 was the decks of the 2026-11-09
purchase. Iteration 3 is this collection-only optimization: Fable 5.2 high builds each deck, Opus 5.5 high reviews it,
and the main session applies the fixes.

Owner's mandate, 2026-11-14:
- Optimize each deck as much as possible, as the greatest Commander champion would, from the owned collection ONLY.
  - No purchases, no loans, no exchanges: the collection is frozen as scanned on 2026-11-13 (`decks/phase2.json`
    `collection_frozen`).
  - Both binders, Spanish and English, are available in full.
- The goal is the strongest decks, nothing else. The model runs without any handicap.
  - A comparison with earlier runs is a side note only.
  - Use all the project's knowledge and the whole internet.
- Order, in series, one deck at a time. Azula goes first, as the Fable 5.2 trial (owner's OK given). Toph, Ezio and Kilo
  follow later, each on the owner's go.

## Flow per deck

1. A builder optimizes the deck. It starts from the deck as built today, `decks/phase2/<slug>.txt`, and may change
   anything, up to a full rebuild.
2. An independent reviewer tries to beat the list.
3. At most one round of fixes.
4. The list is final.

The lead then runs these checks and fixes the pinned copies:
- the gate;
- the bracket check;
- `scripts/assign_copies.py`.

The lead also writes the swap list for the owner: which cards leave the deck, and which come in, from which binder or
from which deck.

## Cards available

- The deck's pool, `data/model/phase2/pool-<slug>.json`: every owned card in the deck's colors, with the Oracle text.
  - `copies` and `by_language`: how many copies the owner has, and in which languages.
  - `held_by`: where each copy sits TODAY, from the decks as built (`free` = in a binder).
  - `free_by_language`: the copies in a binder, per language.
  - `printings`, plus EDHREC numbers when EDHREC knows the card.
- The current holders also appear in `data/model/phase2/assignment.json` and the newest `decks/reports/pull-list-*.md`.
- Copies, the owner's rule of 2026-11-14:
  - One physical copy sits in one deck.
  - Free copies come first.
  - A copy now in a deck not yet optimized in this step may be claimed. The builder writes why it adds more here and
    what that deck loses; that deck is re-optimized later and sees what is left.
  - A scarce copy (no free copy left) goes to the deck where it adds the MOST value (owner, 2026-11-14). A later deck may
    contest a copy held by a deck already optimized in this step. It writes the comparison: what the card does in
    each deck, and the fallback of the deck that would lose it. The lead (Opus 5.5 high) decides, and the losing deck
    takes its written fallback. Example: Azula took Black Market Connections from Ezio, with Tome of Legends as its
    fallback.
  - A card with several copies stays an option for every later deck while a copy is left. Strong staples with spare
    copies belong in every deck that can play them; never leave copies idle in the binder when they would improve a
    deck.
- Language:
  - A bilingual deck takes the English copy when both languages are free, and otherwise the copy that is free.
  - Kilo takes Spanish copies only.

## The owner's card review (mandatory)

`decks/phase2/owner-card-review-20261114.md`: cards he finds weak, and cards he was surprised to see cut. Every card
there that fits the deck's colors gets a written verdict in the build notes: IN, or OUT with a reason of weight. Use the
same section in every deck.

## Knowledge to apply

Everything listed in `docs/proposals/final-rebuild-brief-20261108.md`, section "Knowledge to apply":
- the skill and its references;
- the champion addendum;
- the primers;
- the owner's lessons and the play reviews;
- the EDHREC, Spellbook and Oracle caches;
- the internet.

Also:
- the final review of the previous list, `decks/reports/final-review-<slug>-20261108.md`;
- the earlier lists in version control, to learn from and not to copy. For Azula, `decks/measured/fire-lord-azula/`
  holds the iteration-1 lists that he won games with (Torrential Gearhulk, Frostcliff Siege, Mystical Teachings).

## Rules (unchanged)

- Bracket 3 RULES only: at most 3 Game Changers, no mass land denial, no chained extra turns, no EARLY two-card
  infinite combo. `python scripts/check_phase2_bracket.py decks/phase2/<slug>.txt` must say PASS.
- Power target: Bracket 3 OR HIGHER. Bracket 4 and 5 cards are welcome in every slot, and legal combos are always welcome.
- No reversible cards (transform, modal double-faced, meld, flip). Commander-legal only.
- The consistency gate is a floor: `python scripts/plan_density.py` must PASS. Write a reason for every WARN, and never
  relabel cards to pass.
- Commander Salt floors are secondary: Azula 7.0, Toph 7.0, Ezio 6.5, Kilo 4.5. Salt is not measured in this step.

## What the builder writes (overwrite; the previous versions stay in version control)

- `decks/phase2/<slug>.txt`: exactly 100 cards (Kilo too), under `// Commander` and `// Main`.
- `decks/phase2/<slug>.plan.json`: the plan file for the gate, written from the Oracle texts.
- `decks/phase2/<slug>.build.md`, with these sections:
  1. The profile: plan, backup plan, speed, win lines, how the deck beats three opponents, and what it fears.
  2. The puzzle: each card's role and its main synergies, grouped by function.
  3. The curve table and the ratios, each with its reason.
  4. The interaction plan and the protection plan.
  5. The mulligan, and the play pattern for turns 1 to 5, 6 to 9 and late.
  6. The owner's cards: the verdict for each card of the review, with its reason.
  7. Copies:
     - every card whose free copies run short;
     - every copy claimed from another deck, with the reason and what that deck loses;
     - the language of each card that is not the default.
  8. The changes against the deck as built today. OUT is the list of cards going back to a binder. IN is the list of
     cards coming in, with the binder or deck each comes from. Give a reason for each change.
  9. A real-power estimate on the 1-10 scale, with a range and a confidence, against the deck as built today.
  10. Knowledge used: for each source below, what it demands of this deck and how the list answers it (owner,
      2026-11-14, after a build whose notes cited few sources):
      - the skill and `archetypes.json`;
      - the champion addendum, its 41 items;
      - the mana study, `notes/02-mana.md` and `notes/13-ratio-gaps.md`: lands, colored sources per pip, untapped lands;
      - the other research notes;
      - the primers;
      - the owner's lessons, play reviews and gate review (section f);
      - the previous final review and the iteration-1 lists;
      - the owner's card review;
      - the web sources read, with their URLs.
      The lead never tells a builder to save tokens or to skip web research.
- No commit, and no edits to other decks' files.

## What the reviewer writes

`decks/reports/collection-review-<slug>-20261114.md`. The reviewer is an independent champion who tries to beat the
list, using the same pool, rules and knowledge. It covers:
- the rules: run both scripts and count 100 cards;
- every slot: is it the best available piece? Check the free copies in the pool, and the owner's cards above all;
- the curve and the ratios;
- the copies claimed from other decks;
- a verdict: ACCEPT, or FIX with an exact change list, ranked.

After at most one round of fixes, the list is final.
