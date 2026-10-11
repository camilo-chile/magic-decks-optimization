# Scan free with ManaBox, audit with Scryfall

*Independently fact-checked twice on 2026-10-10; the corrections from both checks are applied below. Google Play pages (download counts, review quotes, developer replies) could not be re-read in the second pass.*

As of 2026-10-10, the best free way to digitize this collection is to scan it with **ManaBox on the Android phone**, in separate Spanish and English piles. Then export ManaBox's **whole-collection CSV** and build the Python pipeline on its **`Scryfall ID`** column, checking every row against Scryfall. ManaBox is the only maintained free Android scanner with no documented card or scan cap whose CSV carries all of these on every row: a Scryfall UUID, set code, collector number, `Foil`, a lowercase `Language` code (`es`) and the binder or deck name. Delver Lens also scans for free, but its own changelog sets the free export limit at "<= 105" cards (v5.41, 2022; the delver.app pricing page says "up to 105 cards"); whether that is per export or cumulative is not documented. Dragon Shield, TCGplayer, EchoMTG and CardCastle each fail on caps, ads, accounts or non-English handling. Spanish cards are the hard part. Every Android scanner app that documents its method matches the card image (ManaBox: artwork), and **none documents detecting the printed language**; only the browser tool Natural Order claims to guess it (vendor claim). A Spanish card is saved in whatever language is selected, so you have to sort by language first and set the language once per pile. No independent accuracy benchmark exists for any app, for Spanish cards or any others. The only figure is one user's guess of "about 85%" for ManaBox. That makes a 100-card pilot mandatory before the full run, and 100 cards also fits Delver Lens's free export cap, so you get a free head-to-head. The main risks are:

- Losing the collection without a backup: three reports between August and October 2026, two of them about 10,000 cards or more.
- Wrong printings when reprints share the same art.
- Glare from sleeves.
- An unconfirmed free-tier limit of about five binders/lists.

The webcam is not needed, and the free desktop scanners are hobby projects with 0-5 GitHub stars (oracle_ii has not been updated since 2017). Your deck work needs the right *card* far more than the right *printing*, so most edition correction can be skipped. The whole job then takes roughly one working day (about 1.5 days if the pilot lands near the 20 s per card go threshold). That is a planning estimate, and the pilot will replace it with a measured one.

*Snapshot: all prices, limits, ratings and store data were read on 2026-10-10 unless another date is given. "Vendor claim" marks a statement by the product's own maker. "Competitor" marks scanyourmtg.com, which is run by Lotus Scan (an iOS-only rival scanner), and scrytics.com, which is run by Scrytics. Prices are US App Store prices in USD. Google Play prices in CLP were not read.*

## Two free Android scanners can handle 1,200 cards; four others cannot

Four camera scanners are realistic options on Android, and all four show activity in 2026:

| App | Downloads | Last Play update |
|---|---|---|
| ManaBox | 1M+ | 2026-09-23 |
| Delver Lens | 100K+ | 2026-10-05 (latest changelog entry: 7.04–7.05 on 2026-09-19) |
| MTG Scanner – Dragon Shield | 500K+ | 2026-09-16 |
| TCGplayer | 1M+ | 2026-10-01 |

Sources: [ManaBox on Play](https://play.google.com/store/apps/details?id=skilldevs.com.manabox&hl=en_US&gl=US); [Delver Lens on Play](https://play.google.com/store/apps/details?id=delverlab.delverlens&hl=en_US&gl=US); [Delver changelog](https://www.delverlab.com/); [Dragon Shield on Play](https://play.google.com/store/apps/details?id=pt.tscg.mtgmanager&hl=en_US&gl=US).

Most of them are ruled out by **free-tier terms, not by recognition quality**. EchoMTG caps free collections at 500 cards. CardCastle lets free users add unlimited cards but browse only the first 1,000 (its homepage says "Add up to 1,000 cards"). Dragon Shield's free tier got worse through 2026. Moxfield has no scanner (a mobile scanning app is only an open request on its feedback board), and a competitor's comparison lists Archidekt as having no built-in scanner. Both are import destinations only ([Moxfield feedback board](https://moxfield.nolt.io/1294); [competitor comparison](https://www.scanyourmtg.com/compare/archidekt-vs-moxfield/)). Lotus Scan, Lion's Eye and Helvault are iOS-only ([competitor list](https://www.scanyourmtg.com/best-mtg-scanner-app/)).

### Android scanner apps compared

| App | Free tier vs. ~1,200 cards + 2 decks | Paid price (US App Store) | Spanish handling | Speed evidence | Export for a Python pipeline | Verdict |
|---|---|---|---|---|---|---|
| **ManaBox** (SkillDevs) | No documented card or scan cap. Ads. One user (2026-09-28) reports "a combined total of 5 Binders, Lists (and I believe also Decks…)". A competitor says "5 decks free". There is no official number ([Play reviews](https://play.google.com/store/apps/details?id=skilldevs.com.manabox&hl=en_US&gl=US); [competitor](https://www.scanyourmtg.com/compare/manabox-vs-delver-lens/)). Cloud Sync is PRO-only. Users without sync get automatic daily backups to Google Drive ([FAQ](https://manabox.app/guides/general/faq)) | PRO US$2.49/month or US$22.99/year. "Remove ads" US$1.99. No lifetime option ([App Store](https://apps.apple.com/us/app/manabox-mtg/id1460407674); [FAQ](https://manabox.app/guides/general/faq)) | Identifies cards "based on their artwork". You set the language by hand in the scanner controls or by bulk edit. No auto-detection ([scanner guide](https://manabox.app/guides/scanner/getting-started/)). Search accepts Spanish names ([site](https://manabox.app/)) | No measured rate. Spanish users: "va super rápido" (2025-04-05), "muy pocos errores de detección" (2026-09-23) ([Play ES](https://play.google.com/store/apps/details?id=skilldevs.com.manabox&hl=es&gl=ES)). One user guesses "about 85% accurate" (2026-09-29) | Whole-collection CSV with `Scryfall ID`, `Set code`, `Collector number`, `Foil`, `Language`, `Binder Name`/`Binder Type`. No documented free export cap. Decks also export as text | **Recommended** |
| **Delver Lens** (Delver Lab) | No documented card or scan cap. Ad-free. Uses the free "lambda" model; Delver Lens has no advanced models. **Free export is limited to 105 cards**: the Delver Lens changelog (v5.41, 2022-05-01) reads "Increased free limit for exporting to <= 105" and delver.app's pricing table says "Text export: Up to 105 cards"; per export or cumulative is undocumented. Scanned images stored on the device only ([delver.app pricing](https://delver.app/); [changelog](https://www.delverlab.com/)) | US$4/month ([delver.app](https://delver.app/)). iOS "Delver Pro" US$4.99/month or US$49.99/year ([App Store](https://apps.apple.com/us/app/mtg-delver-tcg-scanner/id6504142186)) | "Recognition scans the full card". No statement on card languages ([Play](https://play.google.com/store/apps/details?id=delverlab.delverlens&hl=en_US&gl=US)). The Delver X FAQ says "Currently English only", without saying whether that means the interface or recognition ([delver.app](https://delver.app/)). Language is a per-card field | No measured rate. Users call it "so fast". v6.85 (2025-12-31) added "Faster recognition". A 2026-10-05 review, on update day: "Every card is plains" ([Play](https://play.google.com/store/apps/details?id=delverlab.delverlens&hl=en_US&gl=US)) | Per-list CSV using presets (Moxfield, Archidekt, Deckbox…) or custom columns. Language is blank for English ([real export](https://github.com/EchoMTG/mtg-csv-reader/blob/fa0e05e337f5b290b8d46c48e3d98526623113f2/example_datasets/delver/Delver_Test_Export_no_changes.csv)). The `.dlens` backup is a SQLite file that can only be decoded with the app's internal database ([parser](https://github.com/Jertzukka/dlensExporter/blob/e454031be293bef3451d8e1e2cf85505347cdf62/main.py)) | **Pilot challenger.** Full use needs ≤105-card lists or one paid month |
| **MTG Scanner – Dragon Shield** | Users report "an ad every 2 scans" (2026-07-14), a daily scan limit "like 5" (2026-08-28) and being pushed to a new "Sorted" app ([Play](https://play.google.com/store/apps/details?id=pt.tscg.mtgmanager&hl=en_US&gl=US)). A 100-card free cap is reported by a competitor ([competitor](https://www.scanyourmtg.com/best-mtg-scanner-app/)), but a developer reply on the sibling Pokemon app said in July 2021 that it "removed the card limit" ([Play](https://play.google.com/store/apps/details?id=pt.tscg.pokemanager&hl=en_US&gl=US)) | Premium US$3.99/month, US$39.99/year (also US$29.99) ([App Store](https://apps.apple.com/us/app/mtg-scanner-dragon-shield/id1460657155)) | Vendor claim: "scan cards in any language". No method or evidence given | No figure. "Almost all non-standard border & foiled cards fail to be recognized quickly" (2026-05-14) | CSV/text. **No Scryfall ID.** Language is a full word (`Spanish`). First line is `"sep=,"`. Some set codes are not Scryfall's ([parser](https://raw.githubusercontent.com/oflannabhra/transmute/main/src/transmute/formats/dragonshield.py); [format notes](https://github.com/cramt/progress-engine/blob/main/docs/research/collection-import-formats.md)) | Avoid |
| **TCGplayer** | Free. Collections require a TCGplayer account. No cap found ([App FAQ](https://help.tcgplayer.com/hc/en-us/articles/115009506407-TCGplayer-App-FAQ)) | Free | Wording from TCGplayer's seller-side Scan & Identify tool (for Pro sellers): non-English cards are identified "only if there is an English version of the card with the same artwork"; whether the consumer app's scanner shares this engine is undocumented. "Non-English black bordered cards" often come out as a more common variant or unidentified ([Scan & Identify FAQ](https://help.tcgplayer.com/hc/en-us/articles/27302442668695-Scan-Identify-FAQ)) | No figure | Export not confirmed | Avoid |
| **EchoMTG** | "Hard cap — 500 cards". "Scanner + bulk add" is listed under the paid Collector plan ([Plans](https://www.echomtg.com/plans/)) | Collector US$4/month | n/a | n/a | Free CSV import and export | Not viable for free |
| **CardCastle** | Free users are "limited to browsing the first 1,000 cards" and get one deck ([support](https://support.cardcastle.co/en/articles/2031522-what-is-the-difference-between-the-squire-and-knight-accounts)). The homepage instead says "Add up to 1,000 cards, Create 3 decks" ([cardcastle.co](https://cardcastle.co/)) | Knight US$9/month or US$90/year (2022 announcement, possibly outdated) ([pricing](https://support.cardcastle.co/en/articles/6234130-cardcastle-pricing-changes)) | n/a | n/a | n/a | Not viable for free |

The two survivors pinch in different places. ManaBox limits **containers** (binders, lists and probably decks) and shows ads. Delver Lens limits **getting data out**. For a Python pipeline the export limit is the one that matters: the 1,000 loose cards would have to be split into at least ten lists of 105 cards or fewer, each exported separately, assuming the cap is per export, not cumulative (undocumented). The alternative is paying US$4 for a month. A Delver user who switched from ManaBox on 2026-09-07 praised being able to "change the set of multiple cards at a time" ([Play](https://play.google.com/store/apps/details?id=delverlab.delverlens&hl=en_US&gl=US)). That is a real strength, but it does not offset the export limit at $0.

### Non-app and hybrid methods compared

| Method | Cost and limits | Spanish handling | Speed / accuracy evidence | Output | Role here |
|---|---|---|---|---|---|
| **Browser photo tools**: Scrycam, Natural Order | Scrycam: free "during early access", no login, photos deleted after 24 h ([Scrycam](https://scrycam.com/)). Natural Order: "no photo limits and no premium plan" (blog dated 2026-03-31) ([Natural Order](https://naturalorder.app/en/blog/scanner-binder-ia)) | Scrycam vendor claim: "Every English-language Magic printing in the Scryfall catalogue (over 113,000 cards)... and most non-English variants". Natural Order: multi-language OCR that guesses the language from characters like ñ, then searches Scryfall in that language | Scrycam vendor claim: ~97% correct names, ~7 s per photo. Natural Order vendor figure: ~40 s per 9-card page. Neither has been verified independently | Scrycam (vendor): CSV with set code, collector number, foil flag, quantity | Independent second read on the audit sample |
| **Windows webcam, open source**: jlelectroterra1-jpg/card-scanner, frnsys/oracle_ii | Free. card-scanner needs Python and ~500 MB of images; training takes about 1 h on an NVIDIA GPU. It has 0 stars and shows no license ([GitHub](https://github.com/jlelectroterra1-jpg/card-scanner)) | Non-English cards not addressed. The phone-browser version uses an English OCR model | card-scanner self-reports "200/200 cards" recognised at about 110-150 px tall. oracle_ii self-reports 25 misses in 1,045 cards (2.4%), says the set is "not guaranteed", and has "trouble with cards in sleeves" ([GitHub](https://github.com/frnsys/oracle_ii)) | card-scanner exports ManaBox CSV and decklist text | Experiment only |
| **LLM photo batch** (3×3 grids in a free chat app) | Free-tier quotas not checked | Can read Spanish text in principle. Untested | No benchmark exists. A production binder-scanner builder calls a pure vision-model pipeline "extremely slow and expensive" and sends fewer than 5% of cards to Gemini ([Natural Order](https://naturalorder.app/en/blog/scanner-binder-ia)) | A table that is unvalidated until every row is checked against Scryfall | Optional cross-check, mainly as a learning exercise |
| **Manual / text list** | Free | You type the language | No measured time. The tool's author finds both finding the card and picking its set and art tedious ([MTG-Bulk-Scan](https://github.com/JackTheTripperr/MTG-Bulk-Scan)) | ManaBox's documented deck *import* format, such as `3 Verdant Catacombs (MH2) 260` (the guide says only that export creates a text file that can be re-imported, so confirm the export layout in the pilot) ([deck guide](https://manabox.app/guides/decks/import-export/)) | Fallback for sleeved decks and scanner failures |

The webcam adds convenience, not accuracy. Delver's site says "USB webcams work on Android" and recommends at least 1080p at 10 fps ([delver.app](https://delver.app/)). That is the only documented way to use your webcam with a phone app, as a fixed overhead camera. A phone on a stand gives the same hands-free scanning with ManaBox. The desktop projects are hobby code (card-scanner's model training expects an NVIDIA GPU), and none of them claims Spanish support, so the webcam stays out of the critical path.

## Artwork matching finds Spanish cards but never records their language

ManaBox's documentation is explicit: "the scanner identifies cards based on their artwork". Language is a manual step: "Choose the correct set and language" in the bottom controls ([scanner guide](https://manabox.app/guides/scanner/getting-started/)). The Spanish FAQ repeats this: "El escáner detecta las cartas utilizando el arte" ([FAQ ES](https://manabox.app/guides/es/scanner/faq/)). On 2025-04-05 a Spanish reviewer listed "la detección automática de idioma" as the feature to add. The developer's reply did not address it ([Play ES](https://play.google.com/store/apps/details?id=skilldevs.com.manabox&hl=es&gl=ES)). A modern Spanish card shares its artwork with the English printing of the same set, so it should be **identified about as reliably as its English twin**. The language, though, is metadata you have to supply. TCGplayer states the same limit officially for its seller Scan & Identify tool, and adds that "non-English black bordered cards" often come out unidentified or as a more common variant ([TCGplayer FAQ](https://help.tcgplayer.com/hc/en-us/articles/27302442668695-Scan-Identify-FAQ)). Dragon Shield's "any language" claim is vendor copy with no method or evidence behind it. Delver documents nothing about language at scan time. No 2025–2026 review tested Spanish cards specifically. Reddit, where such threads would most likely be, was blocked for the research tools.

The difficult cases are old cards and cards whose art exists only in Spanish. Scryfall itself says its multilingual coverage of older sets is limited ([Scryfall languages](https://scryfall.com/docs/api/languages)). Combined with TCGplayer's warning about non-English black-bordered cards, this means any old or black-bordered Spanish cards belong in a **separate manual batch**. Any Spanish printing without an English art twin cannot be matched by artwork at all.

The export shows how Spanish rows will reach your pipeline. In three real ManaBox exports (only two are linked below), non-English rows carry three things: the **English `Name`**, a lowercase `Language` code, and a `Scryfall ID` that resolves to the printing's **English** record. A Lightning Bolt M11 row is repeated with `es`, `fr`, `de` and other codes, all under an ID that Scryfall returns as `lang: "en"`. A French Abundance C17 row also carries the English record's ID although Scryfall has a French record (`/cards/c17/145/fr` → "Abondance"), and the one Spanish row, Lightning Bolt M11, carries the English ID although `/cards/m11/149/es` exists ("Relámpago") ([MtgCsvHelper export](https://github.com/StepKie/MtgCsvHelper/blob/e8488c7c982bf4663d62e184cf23e34ce11e7b34/MtgCsvHelper/Resources/SampleCsvs/Tests/manabox-real-export.csv); [alg77 export](https://github.com/alg77/siteMagic/blob/HEAD/Decks/ManaBox_Collection.csv); [Scryfall c17/145/es](https://api.scryfall.com/cards/c17/145/es)). This behaviour is undocumented. A live check on 2026-10-10 found it on all 637 non-English rows (610 unique IDs) of three real exports, each resolving to `lang: "en"`. Only one of those rows is Spanish, so the pilot still has to confirm it for `es`.

On Scryfall's side, Spanish is `lang` = `es` (printed code `sp`) across **53,879 cards**. Non-English records add a `printed_name`, and double-faced cards carry it inside `card_faces[].printed_name` ([Scryfall languages](https://scryfall.com/docs/api/languages); [DFC example](https://api.scryfall.com/cards/search?q=set%3Amid+lang%3Aes+is%3Adfc&unique=prints)). **Spanish names do not resolve by exact lookup**: `/cards/named?exact=Contrahechizo` returns 404, and `/cards/collection` lists it as `not_found`. Searching by the Spanish name works only through `/cards/search` with `include_multilingual=true` (20 printings), while `!Counterspell lang:es` finds the same 20 by English name ([named lookup](https://api.scryfall.com/cards/named?exact=Contrahechizo); [multilingual search](https://api.scryfall.com/cards/search?q=Contrahechizo&include_multilingual=true&unique=prints)). The design rule follows directly. Never resolve by Spanish name. Resolve by ID or by set plus collector number, take the language from the `Language` column, and do deck logic on `oracle_id`, which every language and printing of a card shares.

## ManaBox wins on export and price, not on proven accuracy

There are five reasons for the recommendation:

1. **The free tier fits.** The collection needs only three containers: one "Loose" binder and two registered decks. That is within the reported five.
2. **The export is ready for the pipeline.** The `Scryfall ID` column removes fuzzy matching entirely. The header appears in several public real exports and in parsers in Python, Go, Ruby and Rust (a GitHub code-search count of "63 files" could not be reproduced without a login).
3. **The scanner has the controls this job needs** ([scanner guide](https://manabox.app/guides/scanner/getting-started/); [scanner FAQ](https://manabox.app/guides/scanner/faq/)):
   - "Lock" a set so only its versions are matched.
   - Turn Quick mode off so ambiguous versions need confirmation.
   - Bulk-edit language, foil and condition on scanned cards; the set is edited per card, so lock the set on set-sorted piles.
   - Three fixed price sounds (under 1, 1–10 and over 10 USD/EUR) that flag valuable cards as you scan.
4. **It is actively maintained.** iOS 4.2.1 shipped on 24 Sep, the developer answers reviews within days, and a desktop app for Windows/macOS/Linux has a beta promised "by the end of 2026 at the latest" (developer reply, 2026-10-09) ([App Store](https://apps.apple.com/us/app/manabox-mtg/id1460407674); [Play](https://play.google.com/store/apps/details?id=skilldevs.com.manabox&hl=en_US&gl=US)).
5. **The CSV doubles as a portable backup.** ManaBox's importer accepts `Scryfall ID` "as a replacement" for name plus set ([import/export guide](https://manabox.app/guides/collection/import-export/)).

The best case for Delver Lens is real: it is ad-free, has no container limit, offers more export presets and has a faster bulk set change. If you decide you need exact printings and the pilot shows Delver clearly ahead on Spanish cards, **one US$4 month** is the only paid exception worth considering, and only with the user's explicit approval (CLAUDE.md: free tools only). The recommendation does not rest on accuracy. Nobody has measured either app, and competitor-run "comparisons" publish no test method ([Scrytics](https://scrytics.com/blog/best-mtg-card-scanner-app-2026); [competitor](https://www.scanyourmtg.com/best-mtg-scanner-app/)).

| Risk | Evidence (dated) | Mitigation |
|---|---|---|
| **Losing the whole collection** | Users report losing "a 20k plus card collection" (2026-10-03) and "around 10,000 cards" (2026-08-26). A Spanish user wrote "Se pierden los datos si no tienes respaldo" (2026-08-22). The developer says the app sends reminders until backups are enabled ([Play US](https://play.google.com/store/apps/details?id=skilldevs.com.manabox&hl=en_US&gl=US); [Play ES](https://play.google.com/store/apps/details?id=skilldevs.com.manabox&hl=es&gl=ES)) | Turn on Google Drive auto-backup before scanning a single card. Export a CSV after every pile and copy it to the PC |
| **Wrong printing on same-art reprints** | Official: version detection fails when art is shared ([FAQ](https://manabox.app/guides/scanner/faq/)). A user found correcting 5,000 alphabetised cards "tedious" (2026-09-11) | Decide your precision target first (see the decisions table). Lock the set on set-sorted piles. Turn Quick mode off for valuable cards |
| **Language silently left at the default** | Language is manual only ([guide](https://manabox.app/guides/scanner/getting-started/)) | Scan language-sorted piles and bulk-set the language per pile. Run a pivot check in Python |
| **Black-framed, full-art, foil and sleeved cards** | "about 85% accurate… some black mana cards and full art cards don't scan well" (2026-09-29). "Do not even bother scanning cards in sleeves" (2026-08-26). Official: sleeves "should work, but glare… might prevent it" ([Play](https://play.google.com/store/apps/details?id=skilldevs.com.manabox&hl=en_US&gl=US); [guide](https://manabox.app/guides/scanner/getting-started/)) | White paper, diffuse light, a separate slow pile, manual search for failures, and a sleeve test in the pilot |
| **Free container cap** | One user reports 5 combined binders/lists. No official number | Use at most 4 containers. Read the paywall in the pilot. One PRO month costs US$2.49 but needs the user's explicit exception to the free-tools rule. After a lapse, "no data will be deleted" ([subscriptions](https://manabox.app/guides/general/subscriptions/)) |
| **Export header drift** | Title Case headers in 2023 versus `Set code` in 2026 ([TappedOut](https://tappedout.net/mtg-forum/tappedout/importing-csv-from-manabox)). New `Added`/`Signed`/`Proxy` columns reported ([format notes](https://github.com/cramt/progress-engine/blob/main/docs/research/collection-import-formats.md)). v4.2.1 exports the proxy/signed flags ([App Store](https://apps.apple.com/us/app/manabox-mtg/id1460407674)) | Match columns by name, case-insensitively, never by position |
| **Double counting deck cards** | The same Scryfall IDs appear in both deck and binder rows of one real export. Whether deck rows are separate copies is undocumented ([alg77 export](https://github.com/alg77/siteMagic/blob/HEAD/Decks/ManaBox_Collection.csv)) | Test with a 5-card deck in the pilot |
| **App regressions** | "One of the updates broke my ability to scan cards" (2025-06-22, 51 helpful votes). Delver's "Every card is plains" on its 2026-10-05 update day ([Play ManaBox](https://play.google.com/store/apps/details?id=skilldevs.com.manabox&hl=en_US&gl=US); [Play Delver](https://play.google.com/store/apps/details?id=delverlab.delverlens&hl=en_US&gl=US)) | Once the pilot passes, consider turning off Play auto-update for the app until the run ends (my suggestion) |

## A 100-card pilot measures Spanish accuracy before you scan 1,000 cards

The pilot is the cheapest information available, for three reasons:

- **It is the only way to get real numbers.** Scrytics, itself a vendor, argues that accuracy scores from different sources are not comparable without a shared benchmark, and recommends testing "at least one non-English printing" ([Scrytics](https://scrytics.com/blog/best-mtg-card-scanner-app-2026)).
- **100 cards fits the "up to 105 cards" free export cap** (Delver Lens changelog v5.41 and the delver.app pricing page), so both apps can be compared on identical cards at no cost.
- **100 cards is enough to tell "about 85%" from "about 95%".** At an accuracy near 85%, the 95% confidence interval on 100 cards is roughly ±7 percentage points (1.96·√(0.85·0.15/100) ≈ 0.07).

Build the pile from the strata below. Fill any stratum you lack with modern Spanish cards.

| Stratum | Cards | What it tests |
|---|---|---|
| Spanish, modern frame, mixed sets | 30 | The core case |
| Spanish copies of heavily reprinted staples (shared art) | 10 | Wrong printing |
| Spanish old-frame, including any black-bordered | 10 | The non-English black-border failure case |
| Spanish foils | 10 | Foil weak spot |
| Full-art, borderless, showcase or extended-art (any language) | 10 | Reported failures |
| Dark or black-framed cards | 10 | Reported failures |
| Double-faced, split or adventure cards | 5 | `Front // Back` naming |
| English modern controls | 15 | Baseline |
| **Total for both apps** | **100** | |
| Sleeve test: 20 cards from one deck, scanned sleeved and then unsleeved (ManaBox only) | 20 | How to handle the decks |

Run the pilot in this order:

1. **Write the ground truth by hand before any scanning.** Create a `pilot_truth.csv` with columns `slot, set_code, collector_number, language, foil, printed_name`, read directly off each card. For cards that print no collector number, record the set name. Keep the stack in slot order.
2. **ManaBox run.** Scan the stack into a temporary "Pilot" binder with Quick mode off. Set the language per sub-pile. Time the run with a stopwatch and tally every manual intervention. Export the CSV.
3. **Delver Lens run.** Repeat on the same cards. Export one list using a CSV preset that includes set code, number, language and foil, plus a Scryfall ID field if the app offers one (unverified).
4. **Optional Quick-mode run.** Rescan in ManaBox with Quick mode on, to price the speed-versus-accuracy trade-off.
5. **Compare in Python.** ManaBox **aggregates rows by printing**: in two real exports, quantities sum to more cards than rows (873 rows hold 1,227 cards in one, 219 rows hold 228 cards in the other); one report cites "7,835 rows → 8,704 physical cards" (unverified: GitHub code search needs a login). So compare the truth file and each export as multisets of `(set, collector_number, language, foil)`, not row by row. Report each metric per stratum.

The thresholds below are my proposals, not sourced figures:

| Metric | Definition | Proposed go threshold (ManaBox) |
|---|---|---|
| First-pass recognition | % recognised without a manual search | ≥ 90% overall |
| Card (oracle) accuracy | % with the right card before corrections | ≥ 95% on Spanish strata, excluding old-frame |
| Printing accuracy | % with the right set + collector number, Quick mode off | Report only. Use ≥ 85% if you choose printing-level precision |
| Language accuracy | % correct after the per-pile bulk edit | 100% |
| Foil accuracy | % with the correct finish | Report only |
| Time | Seconds per card, including corrections | ≤ 20 s (≈ 5.5 h per 1,000 cards) |
| Sleeve gap | Recognition with sleeves minus without | Sleeved scanning adds at most 1 failure on the 20 cards → scan the decks sleeved. At n = 20 one card is 5 points and the noise is about ±14 points, so this is a coarse test; use 50 cards for a finer one |

If ManaBox passes, proceed. If it fails and Delver passes with a clear lead on the Spanish strata, move to Delver with lists of 105 cards or fewer (a paid month needs the user's explicit exception to the free-tools rule). Any stratum that both apps fail goes to manual entry.

The pilot also settles the open questions that change the workflow:

| Open question | How to settle it in the pilot |
|---|---|
| ManaBox free container limit | Create the production containers first (Loose, Deck 1, Deck 2); only then probe the paywall with one or two throwaway containers and read its text |
| Does the scan language persist between scans? | Set Spanish, scan 10 cards, and check every row *before* any bulk edit |
| Are deck rows separate copies? | Scan 5 cards into a registered "Test deck" and 5 into "Pilot", export, and confirm the quantities sum to 10 with the right `Binder Type` |
| Exact header, and does `Scryfall ID` point to the English record for `es` rows? | Inspect the header, then call `GET /cards/{id}` for the `es` rows and record `lang` |
| How the export is delivered | Check whether export opens the Android share sheet or saves a file |
| Backups | Enable Google Drive backup and confirm the last-backup date updates the next day |
| Delver cap scope | After the 100-card export, try a second small list to see whether the cap is per export |

When the pilot is done, delete the Pilot binder and Test deck, freeing their container slots (whether deleting frees a slot is unverified). Then rescan those cards in the main run so the whole dataset comes from one consistent process.

## The full run: sort by language, scan on white paper, export a CSV after every pile

The workflow below combines ManaBox's official guidance with the process advice in the research. The step that matters most is sorting by language: without it, language correction is impossible to do at scale.

| # | Step | Exact action | Basis |
|---|---|---|---|
| 1 | Install and prepare | Install ManaBox from Google Play. On Wi-Fi, open the scanner once so it downloads its card database; after that "the scanner can work offline". In settings, **enable automatic Google Drive backup** | Developer replies ([Play](https://play.google.com/store/apps/details?id=skilldevs.com.manabox&hl=en_US&gl=US)); FAQ ([FAQ](https://manabox.app/guides/general/faq)) |
| 2 | Pilot | Run the pilot above. Do not proceed until it passes | Section above |
| 3 | Split by container | Physically separate Deck 1, Deck 2 and Loose. **Hand-count Loose** and write the total down | Count reconciliation |
| 4 | Split by language | Divide Loose into Spanish and English. Pull a "slow pile" out of both: foils, full-art/borderless/showcase, old or black-bordered Spanish cards, tokens, double-faced cards | Manual-only language; reported failure modes |
| 5 | Sort by set (optional) | **Only if you want exact printings:** sort each language pile by set symbol so that Lock Set applies | Lock Set ([FAQ](https://manabox.app/guides/scanner/faq/)) |
| 6 | Make piles | Piles of 100–250 cards. Put a sticky note on each with an ID (e.g. `ES-01`), the language and the hand count. Keep each pile in order until it has been validated | A competitor recommends 200–300-card sessions with a review after each ([competitor](https://www.scanyourmtg.com/best-mtg-scanner/large-collections/)) |
| 7 | Set up the station | Plain white printer paper. Even, diffuse light with no glare and no shadow, e.g. two lamps from opposite sides or indirect daylight. Phone on a stand at a fixed height. One card at a time, never overlapping | "Use a plain colored background with good contrast like a white sheet of paper"; avoid "glares… and shadows" and overlaps ([guide](https://manabox.app/guides/scanner/getting-started/)) |
| 8 | Set up containers | One **binder** "Loose" (binders hold owned cards; lists are for cards you track but don't own). One **registered deck** per Commander deck. At most 4 containers in total | [Collection guide](https://manabox.app/guides/collection/getting-started); [deck guide](https://manabox.app/guides/decks/collection-decks/) |
| 9 | Configure the scanner | Quick mode **on** for bulk if you only need the right card; **off** if you need exact printings or are scanning valuable cards. Lock the set on set-sorted piles. Language = Spanish for `ES` piles. Foil toggle on only for foil piles | [Guide](https://manabox.app/guides/scanner/getting-started/) |
| 10 | Scan a pile | Place a card, wait for detection, swap. (To scan the same card again, tap the scanner screen once, or set the copy count in the bottom controls; [guide](https://manabox.app/guides/scanner/getting-started/).) When the **over-10 sound** plays, set the card aside on an audit stack. Look up unrecognised cards by name (Spanish works) or set them aside | [FAQ](https://manabox.app/guides/scanner/faq/); [Search FAQ](https://www.manabox.app/guides/search/faq/) |
| 11 | Review the pile | In the scanned-cards overview, select all → bulk-set the language. Confirm the total equals the pile's hand count. Add the selection to "Loose" | Bulk edit and add-selection features ([App Store notes](https://apps.apple.com/us/app/manabox-mtg/id1460407674)) |
| 12 | Checkpoint | Export a CSV, either the scanner export or Collection tab → top-right menu → export. Send it to the PC as `YYYYMMDD_ES-01.csv`. Return the physical pile to storage only after the Python checks pass | [Import/export guide](https://manabox.app/guides/collection/import-export/) |
| 13 | Slow pile | Quick mode off. Foil toggle on for foils, with side light angled to move the glare. Enter failures manually | [Guide](https://manabox.app/guides/scanner/getting-started/); a competitor's foil-lighting advice |
| 14 | Decks | Follow the sleeve-test result: scan sleeved, or unsleeve 25 cards at a time, scan into the registered deck with Quick mode off, and resleeve immediately. Check that each deck totals 100. Export each deck as text (the export layout is undocumented; the import format looks like `3 Verdant Catacombs (MH2) 260`, so confirm it in the pilot), which also gives the project the text decklists it needs for both decks (Toph and Fire Lord Azula). Fallback: type the list and import it | [Deck guide](https://manabox.app/guides/decks/import-export/) |
| 15 | Final export | Collection tab → top-right menu → export the full-collection CSV, which "will include all card properties as well as the binder/list name". Also save a ManaBox backup file | [Import/export guide](https://manabox.app/guides/collection/import-export/) |
| 16 | Transfer to the PC | Any free route works: share to Google Drive; **Quick Share for Windows** (Windows 10 64-bit or later, Wi-Fi and Bluetooth on, location on the phone, within about 5 m, recipient accepts); email to yourself; or USB from the `Download` folder | [Quick Share](https://www.android.com/better-together/quick-share-app/) |
| 17 | Land the file safely | Keep the raw file untouched. **Never open-and-save it in Excel**: ManaBox itself recommends Google Sheets and notes that Excel needs extra setup for values containing commas. Read it with pandas, `dtype=str`, `encoding="utf-8"` | [Import/export guide](https://manabox.app/guides/collection/import-export/) |
| 18 | Validate and fix | Run the checks in the next section. Fix flagged rows in ManaBox, re-export, and repeat until the checks are clean | Next section |
| 19 | Take breaks | Stop every 2–3 hours. A competitor warns that after that, "you start accepting wrong identifications without noticing" | [Competitor](https://www.scanyourmtg.com/best-mtg-scanner/large-collections/) |

For time, the only rate available is a competitor's *assumed* 300 cards per hour, with no stated method ([competitor](https://www.scanyourmtg.com/best-mtg-scanner/large-collections/)). Using it:

| Stage | Estimate |
|---|---|
| Sorting | 1–1.5 h |
| Scanning 1,000 loose cards | ~3.5 h |
| Review | ~1 h |
| Decks | 1–2 h |
| **Total** | **roughly 6.5–8 h** |

Per-app rates attributed to the same competitor (ManaBox 150–250 cards per hour) would put scanning alone at 4–6.7 h. Those rates do appear on that page, as unverified "real-world estimates based on continuous scanning sessions" with no data behind them (Lotus 400-600, Delver 300-500, ManaBox 150-250, Dragon Shield 200-350, TCGplayer 100-200) ([competitor](https://www.scanyourmtg.com/best-mtg-scanner/bulk-scanning/)). Replace all of this with pilot seconds-per-card × 1,200. Choosing card-level precision removes step 5 and most of the set correction, and that is where large collections lose most of their time.

## Scryfall turns the raw export into a checked dataset

Two older real exports share this whole-collection header. 2026 whole-collection exports append `,Added` (an ISO-8601 timestamp), and third-party format notes report `Signed` and `Proxy` columns in October 2026 exports (not seen in a file). No official ManaBox page publishes the header, so treat it as observed, not guaranteed ([chayde export](https://github.com/chayde/mtg-deck-collection/blob/HEAD/ManaBox_Collection.csv); [alg77 export](https://github.com/alg77/siteMagic/blob/HEAD/Decks/ManaBox_Collection.csv)):

```text
Binder Name,Binder Type,Name,Set code,Set name,Collector number,Foil,Rarity,Quantity,ManaBox ID,Scryfall ID,Purchase price,Misprint,Altered,Condition,Language,Purchase price currency
```

Exports of a single binder leave out `Binder Name,Binder Type` ([MtgCsvHelper export](https://github.com/StepKie/MtgCsvHelper/blob/e8488c7c982bf4663d62e184cf23e34ce11e7b34/MtgCsvHelper/Resources/SampleCsvs/Tests/manabox-real-export.csv)). The values seen in real files are:

| Column | Values seen |
|---|---|
| `Foil` | `normal`, `foil`, `etched` |
| `Condition` | `near_mint`, `excellent`, `played`, `mint` |
| `Binder Type` | `binder` (both cited files), `deck` (alg77 only); `list` in a 2026-08 export (file not cited) |
| `Misprint`, `Altered` | `false` seen in every real file (`true` expected) |
| `Language` | `en, es, fr, de, it, pt, ja, ko, ru, zh_CN, zh_TW` |

Scryfall uses `zhs`/`zht` for Chinese, so map `zh_CN`→`zhs` and `zh_TW`→`zht`. All other codes pass through unchanged ([format notes](https://github.com/cramt/progress-engine/blob/main/docs/research/collection-import-formats.md); [Scryfall languages](https://scryfall.com/docs/api/languages)).

The Scryfall contract is strict, and the research checked it live on 2026-10-10:

- **`POST /cards/collection`** accepts at most **75 identifiers per request**. Sending 76 returned HTTP 400. The limit is **2 requests per second**. Missing cards come back in `not_found`, and the docs warn against relying on position ([collection docs](https://scryfall.com/docs/api/cards/collection)). For ~1,200 rows that is 16 requests, about 8 seconds.
- **Headers are required** by the API docs: `User-Agent` and `Accept` (`Accept: */*` is fine). The first fact-check saw HTTP 400 without them; the second could not reproduce it because curl sends default values. Python `urllib` sends no `Accept` by default, so set both explicitly.
- **Rate limits and caching.** A 429 response locks you out for 30 s. Data should be cached for at least 24 h ([rate limits](https://scryfall.com/docs/api/rate-limits)).
- **Bulk files are now gzipped JSONL** behind `jsonl_download_uri`, with no `download_uri` key. Compressed (`.jsonl.gz`) sizes on 2026-10-09: Default Cards 75.1 MB, Oracle Cards 23.5 MB, All Cards 377 MB; the uncompressed files are much larger. Default Cards holds English records, so offline `es` checks need All Cards. Bulk downloads are not rate-limited and are the better choice for repeated runs ([bulk docs](https://scryfall.com/docs/api/bulk-data); [live /bulk-data](https://api.scryfall.com/bulk-data)).
- **Quirks seen live:**
  - A `"lang":"es"` key added to a collection identifier is silently ignored.
  - Full `Front // Back` names come back `not_found` from `/cards/collection` but work with `/cards/named?exact=` ([named Fire // Ice](https://api.scryfall.com/cards/named?exact=Fire%20%2F%2F%20Ice)).
  - Reversible cards have no top-level `oracle_id` ([reversible example](https://api.scryfall.com/cards/search?q=layout%3Areversible_card&unique=prints)).
  - Promo collector numbers carry suffixes such as `40p` ([pdmu example](https://api.scryfall.com/cards/search?q=set%3Apdmu&unique=prints)).

| Check | Rule (Python) | Catches |
|---|---|---|
| Schema | Match headers by name, case-insensitively, after stripping. Require `Name`, `Set code`, `Collector number`, `Foil`, `Quantity`, `Scryfall ID`, `Language`, plus `Binder Name`/`Binder Type` in the full export. `Quantity` is an integer ≥ 1. `Scryfall ID` matches a UUID regex. `Binder Type` ∈ {binder, list, deck}. Strip `Binder Name` (a real export contains `"Plus One "`). Keep `Collector number` as a string | Header drift, trailing spaces, mangled suffixes |
| Resolution | Send `{"id": …}` in chunks of 75, at least 500 ms apart. `not_found` must be empty. Map results by returned `id`. If a card is unresolved, check `/migrations` ([docs](https://scryfall.com/docs/api/migrations)), then retry with `{set, collector_number}` | Stale or merged IDs |
| Printing consistency | The resolved `set` must equal the exported set code (lowercased) and `collector_number` must equal the exported value as an exact string (values such as `CN2-22` or `73★` exist; do not lowercase it) | Export bugs (cf. the 3.26.2 fix of 2026-02-09, "CSV export in the scanner not exporting the right card versions sometimes") |
| Counts | `groupby(["Binder Type","Binder Name"])["Quantity"].sum()`: each deck = 100, Loose = the hand count, and each checkpoint's increase = that pile's count. Sum `Quantity`, never count rows | Missed or doubled scans |
| Language | Pivot pile × `Language`; `ES` piles must be 100% `es`. For each `es` row, call `GET /cards/{set}/{number}/es` (10 per second). A 404 means "no Spanish record on Scryfall": send it to review, don't treat it as an error | Language left at the default |
| Finish | Map `Foil` `normal` to `nonfoil`, then require it ∈ the printing's `finishes` (nonfoil/foil/etched) | Wrong printing |
| Same-art ambiguity | Flag printings whose `illustration_id` is shared with other paper printings | Likely wrong printing (matters only at printing-level precision) |
| Deck legality | Exclude `layout` ∈ {token, double_faced_token, emblem, art_series}, `set_type` = memorabilia, and `oversized`. A real deck row held an oversized `OC17` commander, and Scryfall lists 205 oversized and 2,593 memorabilia prints as `legal` in Commander, so the explicit exclusion is required (token, emblem and art-series layouts are already `not_legal`). Require `legalities.commander` = legal, one copy per non-basic `oracle_id`, and colour identity within the commander's. List `game_changer` cards ([token/art examples](https://api.scryfall.com/cards/search?q=layout%3Aart_series&unique=prints)) | Stray tokens or oversized cards, duplicate scans |
| Duplicates | Flag the same (`Scryfall ID`, `Foil`, `Language`, `Condition`) appearing in both a deck and Loose, and Loose quantities you know are wrong | Double counting |
| Oracle key | `card.get("oracle_id") or card["card_faces"][0]["oracle_id"]` | Null keys on reversible cards |
| Audit | Check every row on the audit stack (over USD/EUR 10), plus about 10 random rows per pile (~100 in total). 2 or more errors of any kind in one pile's 10-row sample → re-review that pile (a proposal; it fires about 26% of the time at a true 10% error rate and 62% at 20%). Sample physical cards by position, not rows | Residual errors |

The audit size follows from sampling arithmetic. At a true error rate of 2–3%, estimating it within ±3 points at 95% confidence takes about **84-125 cards**, and within +/-2 points about 189-280 (n ≈ 1.96²·p(1−p)/e²). Self-reported error rates in the research run from 2.4% for a webcam hashing scanner to 10% for an OCR name reader ([oracle_ii](https://github.com/frnsys/oracle_ii); [mtgscan](https://fortierq.github.io/mtgscan-ocr-azure-flask-celery-socketio/)). So for planning, expect roughly **2–10% wrong rows** after a set-locked art scan with no review (cited self-reports 2.4–10%; one ManaBox user guesses about 85% accuracy). That is an inference from incomparable figures, not a measurement. With about 100 audited cards, 0, 1 or 2 errors give exact 95% upper bounds of 3.6%, 5.4% and 7.0%, and most of the errors should be printing or language, not the card itself. If you want an independent cross-check, re-read the 100 audit cards with Natural Order or Scrycam. Those tools read text and collector numbers rather than art, so they fail differently, and you can diff the two outputs on set + collector number + language.

## Unverified facts and the decisions that remain yours

| Could not be verified | Status as of 2026-10-10 | Resolve by |
|---|---|---|
| ManaBox free container limit | One user reports 5 combined binders/lists, maybe decks. A competitor says "5 decks". No official number; the subscriptions page implies creating binders is Pro-gated beyond an unpublished free allowance | Paywall in the pilot |
| A persistent default scan language in ManaBox | The docs describe only the per-card controls | Pilot |
| Whether ManaBox deck rows are separate copies | Shared IDs appear in deck and binder rows. Undocumented | Pilot test deck |
| The exact ManaBox export header | Known only from real exports and parsers. Casing drifted after 2023. `Added`/`Signed`/`Proxy` columns reported | First export |
| `Scryfall ID` = English record for `es` rows | Seen on 637 rows in 3 files (only 1 of them Spanish) | Pilot API call |
| ManaBox export delivery (share sheet or saved file) | Not checked | Pilot |
| Google Play / CLP prices | Only US App Store USD prices were read | The Play listing on your phone |
| Scope of Delver's 105-card free export cap | Applies to Delver Lens (changelog v5.41); per export or in total is unknown | Pilot |
| Delver's Spanish recognition and any Scryfall ID export field | Undocumented | Pilot |
| Delver's 2026-10-05 "every card is plains" regression | Two reviews (2026-01-06 and 2026-10-05) | Pilot on the current version |
| Dragon Shield's free limits and the "Sorted" migration | Conflicting reports; no announcement | Not needed |
| Accuracy of any app on Spanish cards; speed of any app | No independent data exists | Pilot |
| Accuracy loss from sleeves | No measured difference | Sleeve test |
| Scryfall's Spanish coverage of old sets | "Limited", not quantified | The 404 log in validation |
| Why `Front // Back` names fail in `/cards/collection` | Observed only | Resolve by ID |
| Free quotas of consumer LLM chat apps; long-term availability of Scrycam and Natural Order | Not checked; "early access"; vendor claims | Only if you use them |
| Community consensus | Reddit was blocked; the evidence is about 40 Play reviews per app | — |

| Decision | Options | Suggested default |
|---|---|---|
| Precision target | Card-level (`oracle_id`) or printing-level (set + collector number + foil) | Card-level for everything; printing-level only for the over-10 audit stack. Deck building and "owned cards first" need `oracle_id`; the printing only changes value |
| Scanner | ManaBox or Delver Lens | ManaBox, unless the pilot shows Delver clearly ahead on the Spanish strata |
| Spending | $0 only (CLAUDE.md: free tools only). Paid options (US$1.99 to remove ads; one PRO month at US$2.49 if the container cap bites; one Delver month at US$4 if Delver wins) need the user's explicit exception | $0 |
| Decks | Scan sleeved, unsleeve and scan, or type the list | Decided by the sleeve test |
| Foil and condition fields | Track or skip | Foil only at printing-level precision; skip condition |
| Audit threshold | USD/EUR 5 or 10 | 10, which matches ManaBox's top price sound |
| Where the CSV lives | Committed to the public repo, or git-ignored | Keep the raw file git-ignored; commit derived lists only if you want them public |
| Second-read experiment | None, Natural Order, Scrycam, or an LLM chat on 100 cards | Optional; run it on the audit sample |
| Webcam | Unused, a Delver USB overhead rig, or a desktop prototype | Unused |

## Conclusion

Recognising *which card* is largely solved for this collection. The open problem is the card's *metadata*: the language, which no scanner detects, and the printing, which art matching guesses when reprints share artwork. That moves the real work from the phone to the PC. A Scryfall ID plus a language column turns the leftover error into a data-validation job: counts, a language pivot, finish checks and a sampled audit. That is cheap to automate and repeatable each time the collection changes. Your deck goal needs card-level identity, not exact printings, so the costliest part of scanning (edition correction) is optional, and the collection can likely be done in about a day rather than a week.

Two consequences matter going forward. First, the CSV is both your interface and your insurance. ManaBox re-imports its own CSV by Scryfall ID, so a dated CSV on the PC protects you against the app-side losses reported in 2026, independently of any backup. Second, today's facts will move: ManaBox's desktop app (beta promised by the end of 2026), the pricing on both apps, and Scryfall's recent switch to gzipped JSONL bulk files can all change. Keep the pipeline matching columns by name and resolving by ID, and re-check the free-tier terms on the phone right before the full run.
