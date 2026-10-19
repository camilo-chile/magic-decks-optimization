// Phase 8: prices a short list of card names in one Shopify store from inside the owner's browser (Claude in
// Chrome, javascript_tool): one /search/suggest.json request per name, then the matching product's .js (variants,
// prices in cents). For the wishlists (decks/proposals/*.md): the full-collection reader
// (scripts/browser_shopify_reader.js) cannot reach the cheap tail of the 25,000-product stores, a per-name search can.
// Not run by the owner: Claude runs it by hand, one store per tab (Shopify answers HTTP 429 to Python clients),
// one request per second at most.
//
// Setup per tab (once): open the store's home page and set window.name to the names joined with "|" (lower case,
// front faces; `scripts/read_store_prices.py` -> new_names(targets_from_repo()) lists the unpriced ones).
// Run this file, then poll JSON.stringify({s:w.state,d:w.done,t:w.total,e:w.err}) on window.__wl (a javascript_tool
// call times out after 45 s: sleep at most 40 s per call). When state is "done", read window.__wl.lines (pipe lines
// `key|bucket|handle|variant|price|title_suffix`, as in browser_shopify_reader.js) and save them under the header
//   #STORE <id> fetched_at=<UTC> source=browser seen=<names> FORMAT key|bucket|handle|variant|price|title_suffix
// as data/prices/browser-<store>-<YYYYMMDD>-wishlist.psv; scripts/merge_prices.py adds those cards to the store's
// earlier reading. Buckets: nen English, nes Spanish, f foil (the cheapest available variant of each).
// A javascript_tool result is cut at about 900 characters: for the full lines, split them into chunks of at most
// 760 characters in the page (window.__chunks), read one chunk per call (a browser_batch of calls works) and check
// the copy with a checksum of the joined lines (h = (h * 31 + charCode) % 1000003) computed in the page and again in
// Python before saving. window.__wl.sum is a short `card:cheapest non-foil price` summary for a quick estimate.
// Do not POST the lines to a local server: Chrome holds a request from a public page to localhost for a permission.
window.__wl = {state: 'running', done: 0, total: 0, lines: [], err: null, t0: Date.now()};
void (async () => {
  const wl = window.__wl;
  const names = window.name.split('|').filter(Boolean);
  wl.total = names.length;
  const bad = /heavily|damaged|moderately|japan|japon|franc|french|german|alem|ital|portug|korean|coreano|chinese|chino|russian|ruso|phyrexian/i;
  const skipT = /\bart (card|series)\b|\((japanese|japon[eé]s|french|german|italian|portuguese|korean|chinese|russian)\)|\bjapanese\b/i;
  const FIN = new Set(['regular', 'foil', 'borderless', 'showcase', 'extended', 'etched', 'retro', 'full', 'art',
    'promo', 'surge', 'serialized', 'normal', 'non-foil', 'nonfoil']);
  const norm = s => s.toLowerCase().replace(/’/g, "'").trim();
  const sleep = ms => new Promise(x => setTimeout(x, ms));
  const get = async url => {
    for (let k = 0; k < 4; k++) {
      const r = await fetch(url);
      if (r.status === 429) { await sleep(30000); continue; }
      return r;
    }
    throw new Error('HTTP 429 four times');
  };
  const best = {};
  for (const name of names) {
    try {
      const r = await get('/search/suggest.json?q=' + encodeURIComponent(name) + '&resources[type]=product&resources[limit]=10');
      const prods = ((await r.json()).resources || {}).results?.products || [];
      for (const pr of prods) {
        if (/^(french|german|italian|portuguese|japanese|korean|russian|chinese)\s/i.test(pr.title) || skipT.test(pr.title)) continue;
        const clean = pr.title.replace(/^spanish\s+/i, '');
        if (norm(clean.slice(0, name.length)) !== name) continue;       // the title must start with the card name
        const rest = clean.slice(name.length).trim();
        const first = (rest.split(' ')[0] || '').toLowerCase().replace(/^\(/, '');
        if (rest && !('[(-—'.includes(rest[0]) || rest.startsWith('//') || FIN.has(first) || /^\d+$/.test(first))) continue;
        await sleep(1000);
        const pj = await (await get('/products/' + pr.handle + '.js')).json();
        for (const v of (pj.variants || [])) {
          const price = Number(v.price) / 100;
          if (!v.available || !(price > 0) || bad.test(v.title)) continue;
          const text = pr.title + ' ' + v.title;
          const foil = /foil/i.test(text) && !/non[- ]?foil|no foil/i.test(text);
          const es = /espa|spanish/i.test(text);
          const b = foil ? 'f' : (es ? 'nes' : 'nen');
          const variant = es && !/espa|spanish/i.test(v.title) ? v.title + ' Spanish' : v.title;
          const slot = best[name] || (best[name] = {});
          if (!slot[b] || price < slot[b][3]) slot[b] = [rest, pr.handle, variant, price];
        }
      }
    } catch (e) { wl.err = (wl.err ? wl.err + '; ' : '') + name + ': ' + e.message; }
    wl.done++;
    await sleep(1000);
  }
  for (const [key, buckets] of Object.entries(best)) {
    for (const [b, [suffix, handle, variant, price]] of Object.entries(buckets)) {
      wl.lines.push([key, b, handle, variant, price, suffix].join('|'));
    }
  }
  const cheapest = {};
  for (const l of wl.lines) {
    const [k, b, , , p] = l.split('|');
    if (b !== 'f') (cheapest[k] = cheapest[k] || []).push(Number(p));
  }
  wl.sum = Object.entries(cheapest).map(([k, a]) => k.slice(0, 20) + ':' + Math.min(...a)).join('; ');
  wl.state = 'done';
})();
