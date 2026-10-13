# Komite 1 Patoloji — Hap Bilgi + 5 Yılın Çıkmışları

BAİBÜ Tıp Dönem III, Hastalıkların Biyolojik Temeli Kurulu (I. Kurul, 2026-27) için ders ders ayrılmış hap
bilgi slaytları. Son 5 yılın (2021-22 → 2025-26) kurul sınavında çıkmış bilgiler kırmızı **ÇIKMIŞ**
etiketiyle (yıl/yıllar) işaretlenir. Her dersin sonunda o dersin çıkmış soruları (doğru cevap + çeldiriciler) yer alır.

**Kaynak kuralı:** Hap bilgiler yalnızca bu dönemin (2026-27) ders PDF'lerinden yazılır. Eski klasör,
geçmiş yılların notları ve kitaplar kullanılmaz. Bir dersin 2026-27 PDF'i gelmeden o ders desteye girmez.

- **`Komite1_Patoloji_Hap_Bilgi.pdf`** — 16:9 slayt PDF'i. Şu an tek ders var: Drive › Komite-1 › PDF ›
  Patoloji › 2026-2027(yeni) klasöründeki **1-PATOLOJİYE GİRİŞ** (Doç. Dr. S. E. Düzcü).
- `kaynak/` — PDF'in üretildiği kaynaklar
  - `icerik.py` — desteye giren dersler (yalnızca 2026-27 PDF'lerinden)
  - `cikmis_patoloji.py` — 21 dersin 108 çıkmış patoloji sorusu (cevaplı). Bu dersler 2026-27 PDF'i
    gelince desteye eklenecek; şimdilik desteye girmez.
  - `olustur.py` — içerikten `slaytlar.html` üretir; `stil.css`, `sigdir.js` — görünüm ve yazı boyutu sığdırma
  - `pdf.cjs` — Playwright/Chromium ile PDF'e basar
  - `fontlar/` — Inter yazı tipinden türetilmiş TTF'ler (SIL OFL 1.1, bkz. `fontlar/OFL.txt`)

Yeniden üretmek için:

```bash
cd komite1-patoloji/kaynak
python3 olustur.py && node pdf.cjs
```

Not: 2021-22 sınavının kitapçığı olmadığından o yılın soruları öğrencilerin hatırladıklarından derlenmiştir
(`21-22*`). Resmi cevap anahtarı yoktur. Bir ders desteye eklenirken o dersin sorularının cevapları
2026-27 PDF'iyle karşılaştırılır.
