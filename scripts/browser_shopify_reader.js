// Phase 7: reads one Shopify store's singles collection from inside the owner's browser (Claude in
// Chrome, javascript_tool), keeping the cheapest available variant per card. Not run by the owner:
// Claude runs it by hand, one store per tab, because Shopify answers HTTP 429 to Python clients.
//
// Setup per tab (once): open the store's home page, then set window.name to the target names joined
// with "|" (lower case, front faces; `scripts/read_store_prices.py` -> targets_from_repo() prints them).
// window.name survives navigation between stores in the same tab.
//
// Run (set COLL to the collection path; see data/stores.md):
//   PayToWin /collections/mtg-singles-instock, Game of Magic /collections/mtg-todas-las-singles,
//   La Comarca /collections/magic-the-gathering-singles, Oasis /collections/mtg-singles-instock,
//   Piedra Bruja /collections/single-mtg, AFK Store /collections/singles-mtg
// Poll with: JSON.stringify({s:c.state,p:c.page,seen:c.seen,cards:Object.keys(c.best).length}) on window.__cr
// (a javascript_tool call times out after 45 s: sleep at most 40 s per call).
//
// Extract: build pipe lines `key|bucket|handle|variant|price|title_suffix` (see
// docs/research/phase7-handoff-2026-10-17.md), render them in the page body and read them with
// get_page_text, then save as data/prices/browser-<store>-<YYYYMMDD>.psv.
window.__cr = {state: 'running', page: 0, seen: 0, best: {}, err: null, r429: 0, t0: Date.now()};
(async (COLL) => {
  const cr = window.__cr;
  const names = new Set(window.name.split('|'));
  const bad = /heavily|damaged|moderately|japan|japon|franc|french|german|alem|ital|portug|korean|coreano|chinese|chino|russian|ruso|phyrexian/i;
  const skipT = /\bart (card|series)\b|\((japanese|japon[eé]s|french|german|italian|portuguese|korean|chinese|russian)\)|\bjapanese\b/i;
  const norm = s => s.toLowerCase().replace(/’/g, "'").trim();
  const FIN = new Set(['regular', 'foil', 'borderless', 'showcase', 'extended', 'etched', 'retro', 'full', 'art',
    'promo', 'surge', 'serialized', 'normal', 'non-foil', 'nonfoil']);
  try {
    for (let p = 1; p <= 600; p++) {
      let r;
      for (let k = 0; k < 4; k++) {
        r = await fetch(COLL + '/products.json?limit=250&page=' + p);
        if (r.status === 429) { cr.r429++; await new Promise(x => setTimeout(x, 60000)); continue; }
        break;
      }
      if (!r.ok) { cr.err = 'HTTP ' + r.status + ' page ' + p; break; }
      const prods = (await r.json()).products || [];
      cr.page = p; cr.seen += prods.length;
      for (const pr of prods) {
        if (/^(french|german|italian|portuguese|japanese|korean|russian|chinese)\s/i.test(pr.title) || skipT.test(pr.title)) continue;
        const clean = pr.title.replace(/^spanish\s+/i, '');
        const w = clean.split(' ');
        let key = null;
        for (let c = Math.min(9, w.length); c >= 1; c--) {
          const pre = w.slice(0, c).join(' ');
          if (names.has(norm(pre))) {
            const rest = clean.slice(pre.length).trim();
            const first = (rest.split(' ')[0] || '').toLowerCase().replace(/^\(/, '');
            if (!rest || '[(-—'.includes(rest[0]) || rest.startsWith('//') || FIN.has(first) || /^\d+$/.test(first)) key = norm(pre);
            break;
          }
        }
        if (!key) continue;
        for (const v of (pr.variants || [])) {
          if (!v.available || !(Number(v.price) > 0) || bad.test(v.title)) continue;
          const text = pr.title + ' ' + v.title;
          const foil = /foil/i.test(text) && !/non[- ]?foil|no foil/i.test(text);
          const es = /espa|spanish/i.test(text);
          const b = foil ? 'f' : (es ? 'nes' : 'nen');   // foil, Spanish, English
          const price = Number(v.price);
          const slot = cr.best[key] || (cr.best[key] = {});
          if (!slot[b] || price < slot[b][3]) slot[b] = [pr.title, pr.handle, v.title, price];
        }
      }
      if (prods.length < 250) break;
      await new Promise(x => setTimeout(x, 1200));
    }
    cr.state = cr.err ? 'error' : 'done';
  } catch (e) { cr.err = String(e); cr.state = 'error'; }
})('/collections/mtg-singles-instock');
