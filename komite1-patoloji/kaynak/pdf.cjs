// slaytlar.html -> PDF (Playwright + Chromium). Kullanım: node pdf.cjs [çıktı.pdf]
const path = require('path');
const { chromium } = require('playwright');

(async () => {
  const dir = __dirname;
  const html = path.join(dir, 'slaytlar.html');
  const out = process.argv[2] || path.join(dir, '..', 'Komite1_Patoloji_Hap_Bilgi.pdf');
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1280, height: 720 } });
  await page.goto('file://' + html, { waitUntil: 'load' });
  await page.waitForFunction(() => window.__hazir === true, null, { timeout: 60000 });
  await page.emulateMedia({ media: 'print' });
  const rapor = await page.evaluate(() => window.__sigdir());
  const ilk = await page.evaluate(() => window.__rapor);
  const hepsi = {};
  for (const r of [...ilk, ...rapor]) hepsi[r.sayfa] = r;
  const liste = Object.values(hepsi).sort((a, b) => a.sayfa - b.sayfa);
  for (const r of liste) {
    console.log(`sayfa ${r.sayfa}: yazı ${r.fs}px${r.tasma ? '  <<< HÂLÂ TAŞIYOR' : ''}`);
  }
  await page.pdf({ path: out, width: '1280px', height: '720px', printBackground: true, preferCSSPageSize: true });
  await browser.close();
  console.log('PDF:', out);
})();
