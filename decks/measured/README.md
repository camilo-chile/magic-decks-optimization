# Measured lists

The exact 100-card lists that were scored on Commander Salt (scoring 2026.4195), one file per entry of
`decks/proposals/measured.json`: `<deck slug>/<label>.txt`, the label being the key after the slash. The first 16 hex digits of
the SHA-256 of the sorted lines (commander included) equal that entry's `list_hash`. They feed `scripts/deck_stats.py` (the
statistics of the dashboard). Lists that no chart uses any more (rounds 1 and 2 of Toph and Azula) are not kept; they are in
version control history. Each new measured list is saved here when it is measured.
