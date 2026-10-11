# Komite 1 Patoloji — Hap Bilgi + 5 Yılın Çıkmışları

BAİBÜ Tıp Dönem III, Hastalıkların Biyolojik Temeli Kurulu (I. Kurul, 2026-27) patoloji dersleri için
konu konu ayrılmış hap bilgi slaytları. Son 5 yılın (2021-22 → 2025-26) kurul sınavında çıkmış bilgiler
kırmızı **ÇIKMIŞ** etiketiyle (yıl/yıllar) işaretlidir; her başlığın sonunda o başlığın çıkmış soruları
(doğru cevap + çeldiriciler) yer alır.

- **`Komite1_Patoloji_Hap_Bilgi.pdf`** — 16:9 slayt PDF'i (112 sayfa, 22 başlık, 108 çıkmış soru)
- `kaynak/` — PDF'in üretildiği kaynaklar
  - `icerik.py`, `icerik2.py` — bölüm içerikleri ve çıkmış sorular; `icerik_ek.py` — özet listeler
  - `olustur.py` — içerikten `slaytlar.html` üretir; `stil.css`, `sigdir.js` — görünüm ve yazı boyutu sığdırma
  - `pdf.cjs` — Playwright/Chromium ile PDF'e basar
  - `fontlar/` — Inter yazı tipinden türetilmiş TTF'ler (SIL OFL 1.1, bkz. `fontlar/OFL.txt`)

Yeniden üretmek için:

```bash
cd komite1-patoloji/kaynak
python3 olustur.py && node pdf.cjs
```

Not: 2021-22 sınavının kitapçığı olmadığından o yılın soruları öğrencilerin hatırladıklarından derlenmiştir
(`21-22*`). Resmi cevap anahtarı olmayan sorular ders slaytları ve Robbins Temel Patoloji'ye göre cevaplanmıştır.
