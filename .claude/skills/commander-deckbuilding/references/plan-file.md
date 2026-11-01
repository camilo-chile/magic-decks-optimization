# The plan file for `scripts/plan_density.py`

Moved out of SKILL.md step 14 in revision 2 so the skill stays short. The script's docstring is the authority; this file
is the builder's reading of it. The file lives at `decks/phase2/<slug>.plan.json` next to the decklist `<slug>.txt`
(the script reads only that folder), is written from Oracle text BEFORE the last twenty cards are fixed, and is attacked
by a reviewer.

## Schema

```json
{
  "plan": "one sentence: engine + fuel + payoff + how it beats three opponents",
  "backup": "one sentence; reuses most plan pieces",
  "archetype": "slug in archetypes.json (step 2), or 'custom'",
  "secondary": "optional slug of a second archetype", "secondary_role": "plan|modifier",
  "commander_dependence": "engine|attack_engine|enabler|value (step 1)", "commander_mv": 4,
  "win_routes": {
    "route name": {"cards": ["..."], "axis": "combat|noncombat|alternate", "vs_three": "how it beats 3 opponents"}
  },
  "functions": {
    "through_wide_board": {"cards": ["..."], "needed_by": "early"},
    "through_big_creatures": {"cards": ["..."], "needed_by": "early"},
    "<function name>": {"cards": ["..."], "needed_by": "early|late"}
  },
  "support": {"<profile support line>": ["..."]},
  "tutors": {"tutor card": ["function it can fetch for"]},
  "tags": {"card": "engine|payoff|backup|ramp|draw|removal|wipe|tutor|protection|land|orphan", "card2": ["primary", "second"]},
  "bad_when_drawn": {"card": "early|late"}
}
```

- A route's `cards` hold its CLOSERS only. Routes may share the engine pieces that make them work (outside their card
  lists); two routes that share a card fail the gate.
- `bad_when_drawn` takes `early`, `late` or `never`; only `early` and `late` count toward the warning, so mark every card
  honestly. Cheap ramp counts as bad late only above the profile's ramp target.
- `tags` carry the primary tag first (it drives the tag table, the plan share and the orphan count). The base floors
  (ramp, draw, removal, wipe, protection) are counted on every tag of a card, so a card that really does two base jobs
  counts in both.

## What the gate enforces (summary)
The script applies the profile named in `archetype` (plus `secondary`: higher minimum of every shared function, overlap of
the land bands; `secondary_role: modifier` turns the secondary's own functions into support lines).
- FAIL:
  - the plan names no archetype, or one that is not in `archetypes.json` (`custom` is allowed and only warns);
  - every non-basic card has a tag;
  - every `gate` function of the profile is declared, with at least the larger of the class minimum (10 early, 6 late,
    counting the commander and the tutors) and the profile minimum;
  - `needed_by` is not later than the profile says. The only exception is the profile's commander alternative: when the
    commander itself is in the function's cards and the profile has `if_commander_is_payoff` or `if_commander_is_source`,
    the function may be late with that alternative's minimum;
  - the two reference-board functions exist and are judged early whatever `needed_by` says;
  - a card named in `tutors` also carries the tag `tutor`;
  - at least two disjoint routes, not all combat, every card in the list or command zone, each with `vs_three`;
  - at most 3 orphans, where every engine/payoff/backup card in no function and no route counts as an orphan.
- WARN:
  - a base floor of the profile (ramp, draw, removal as spot answers, wipes, protection) is not met, counted on every tag
    of a card, primary or second;
  - lands outside the profile's band;
  - a support line of the profile has fewer pieces than its minimum, or is not reported in the `support` block;
  - a function reaches its minimum only with the commander (it fails if the commander is removed);
  - a route rests on a single card;
  - more than 12 cards bad early or late (a `never` entry is not counted).
- `commander_dependence` replaces the profile's protection floor with the class's; `commander_mv` of 4 or more adds 2 to
  the ramp floor. **When your commander justifies a number outside a warning (for example 40 lands for landfall, 6 spot
  removal with 2 wipes, 1 wipe for tokens), keep it and write the reason in the profile table.**
- The report gives pieces and odds both with and without the commander and prints the support lines.
- Not enforced (the reviewer checks them): that a card's tag matches its Oracle text, that a route's `axis` is honest, that
  at least half of a secondary's pieces also serve the primary, that a tutor can really fetch what it is listed for, and the
  weights of `meta.weights` (commander-conditional or one-shot pieces count half).

## Honesty rules (gate review section f)
- Declare EVERY gate function the list leans on, including the ones that come out short. Drop a function only together
  with every card that exists for it. Support lines that come out short are reported in the profile table, never hidden.
- Declare the reference boards as `early`: they are early by definition, and a reviewer re-derives every `needed_by`.
- A card tagged engine, payoff or backup must sit in a declared function or win route, or the gate counts it as an
  orphan. For support-line cards: tag them by their safety role when they have one (haste-plus-hexproof equipment is
  protection; combat-damage draw is draw), or list them in the win route they enable, or promote the line.
- Declare the gate-tier functions of your profile under the names in `archetypes.json` (for example `land_entries`,
  `spell_density`, `token_makers`, `attackers`, `sac_outlets`): the script matches them by name and fails the plan when
  one is missing. Report the support lines (`haste`, `team_evasion`, `defense_while_tapped`, `extra_land_drops`...) in the
  `support` block, never as declared functions; promote one to a declared function only if the plan cannot work without
  it, and then it must reach 10 (early) or 6 (late).
- Tag by the job the card is in the deck for (primary), not by what makes the counts pass. A land tag only on lands. A
  tutor counts only for what it can really fetch.
- The commander needs no tag; it counts as a guaranteed piece of any function that lists it, so state the odds with and
  without it: an engine-dependent deck must reach the class min without the commander.
- Name dead clauses in the profile (they are not orphans: the card has another use).
- Run `python scripts/plan_density.py` and read `decks/reports/consistency-<slug>.md`. A PASS is a floor, not the goal.
- After editing `archetypes.json`, run `python scripts/gen_archetype_tables.py` so `references/archetypes.md` follows.
