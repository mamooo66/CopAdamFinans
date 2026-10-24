// slaytlar.html -> PDF (Playwright + Chromium).
// Kullanım: node pdf.cjs [--html slaytlar.html] [--pdf çıktı.pdf] [--olc]
//   --olc : PDF basmadan yalnızca her slaytın sığan yazı boyutunu ve taşmayı raporlar.
const path = require('path');
const { pathToFileURL } = require('url');
const { chromium } = require('playwright');

function arg(ad) {
  const i = process.argv.indexOf(ad);
  return i > -1 ? process.argv[i + 1] : null;
}

(async () => {
  const dir = __dirname;
  const html = path.resolve(arg('--html') || path.join(dir, 'slaytlar.html'));
  const out = path.resolve(arg('--pdf') || path.join(dir, '..', 'calisma', 'slaytlar.pdf'));
  const sadeceOlc = process.argv.includes('--olc');
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1280, height: 720 } });
  await page.goto(pathToFileURL(html).href, { waitUntil: 'load' });
  await page.waitForFunction(() => window.__hazir === true, null, { timeout: 60000 });
  await page.emulateMedia({ media: 'print' });
  const rapor = await page.evaluate(() => window.__sigdir());
  let sorun = 0;
  for (const r of rapor) {
    const kucuk = r.fs < 13;
    if (kucuk || r.tasma) sorun++;
    console.log(`sayfa ${r.sayfa}: yazı ${r.fs}px${r.tasma ? '  <<< TAŞIYOR' : ''}${kucuk && !r.tasma ? '  <<< 13px altı: slaytı böl' : ''}`);
  }
  console.log(sorun ? `${sorun} slaytta sorun var` : 'tüm slaytlar sığıyor (≥13px)');
  if (!sadeceOlc) {
    await page.pdf({ path: out, width: '1280px', height: '720px', printBackground: true, preferCSSPageSize: true });
    console.log('PDF:', out);
  }
  await browser.close();
})();
