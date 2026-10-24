// Her slaytın gövde yazı boyutunu kutuya sığan en büyük değere ayarlar (ikili arama).
// Üst sınır .govde[data-max] (px), alt sınır 11px. Rapor window.__rapor'da.
(function () {
  function tasiyor(g) {
    if (g.scrollHeight > g.clientHeight + 1 || g.scrollWidth > g.clientWidth + 1) return true;
    for (const s of g.querySelectorAll(':scope > .sut')) {
      if (s.scrollHeight > s.clientHeight + 1) return true;
    }
    return false;
  }
  function ayarla(g) {
    const enAz = 11;
    const enCok = parseFloat(g.dataset.max || '17');
    let alt = enAz, ust = enCok;
    g.style.fontSize = ust + 'px';
    if (!tasiyor(g)) return ust;
    for (let i = 0; i < 9; i++) {
      const orta = (alt + ust) / 2;
      g.style.fontSize = orta + 'px';
      if (tasiyor(g)) ust = orta; else alt = orta;
    }
    const fs = Math.floor(alt * 4) / 4;
    g.style.fontSize = fs + 'px';
    return fs;
  }
  window.__sigdir = function () {
    const rapor = [];
    document.querySelectorAll('.slide').forEach(function (sl, i) {
      const g = sl.querySelector('.govde');
      if (!g) return;
      const fs = ayarla(g);
      rapor.push({ sayfa: i + 1, fs: fs, tasma: tasiyor(g) });
    });
    return rapor;
  };
  function calistir() {
    window.__rapor = window.__sigdir();
    window.__hazir = true;
  }
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(calistir);
  else calistir();
})();
