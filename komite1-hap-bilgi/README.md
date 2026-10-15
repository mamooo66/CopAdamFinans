# Komite 1 Hap Bilgi — Patoloji + Farmakoloji (2026-27)

BAİBÜ Tıp Dönem III, Hastalıkların Biyolojik Temeli Kurulu (I. Kurul, sınav 30 Ekim 2026) için ders ders ayrılmış
hap bilgi slaytları. Son 5 yılın (2021-22 → 2025-26) kurul sınavında çıkmış bilgiler kırmızı **ÇIKMIŞ** etiketiyle
(yıl/yıllar) işaretlenir. Her dersin sonunda o dersin çıkmış soruları (doğru cevap + çeldiriciler) yer alır.

**Kaynak kuralı:** Hap bilgiler yalnızca bu dönemin (2026-27) ders PDF'lerinden yazılır
(Drive › Komite-1 › PDF › Patoloji / Farmakoloji › 2026-2027(yeni)). Eski klasör, geçmiş yılların notları ve
kitaplar kullanılmaz. Bir dersin 2026-27 PDF'i gelmeden o ders desteye girmez. Çıkmış sorunun cevabı PDF'te yoksa
soru yine gösterilir ve “(PDF'te geçmiyor)” diye işaretlenir.

- **`Komite1_Patoloji_Farmakoloji_Hap_Bilgi.pdf`** — 16:9 slayt PDF'i
- `sorular/` — son 5 yılın kurul soruları (tam metin; kimlikle grep edilir)
- `kaynak/` — PDF'in üretildiği kaynaklar
  - `bolumler/pNN_*.py` (Patoloji), `bolumler/fNN_*.py` (Farmakoloji) — her ders bir modül; sıra dosya numarasına göre
  - `yardim.py` — modüllerin yazım yardımcıları (madde, kart, soru); `icerik.py` — modülleri yükler
  - `cikmis_patoloji.py`, `cikmis_farmakoloji.py` — PDF'i henüz gelmemiş derslerin çıkmış soruları (desteye girmez)
  - `olustur.py` — `slaytlar.html` üretir; `stil.css`, `sigdir.js` — görünüm ve yazı boyutu sığdırma
  - `pdf.cjs` — Playwright/Chromium ile PDF'e basar (`--olc`: yalnızca sığma raporu)
  - `araclar/` — `pdf_metin.py` (ders PDF'i → sayfa işaretli metin / sayfa resmi), `denetle.py` (soru ve rozet denetimi), `sadakat.py` (maddelerin PDF metniyle örtüşmesi)
  - `fontlar/` — Inter yazı tipinden türetilmiş TTF'ler (SIL OFL 1.1, bkz. `fontlar/OFL.txt`)

Yeni bir oturumda çalışmaya devam etmek için önce depo kökündeki `CLAUDE.md`'ye bakın (kurulum, kurallar,
yapılacaklar).

Yeniden üretmek için:

```bash
cd komite1-hap-bilgi/kaynak
python3 olustur.py && node pdf.cjs
```

Tek bölümü denemek için: `python3 olustur.py --sadece p02_hasar --cikti ../calisma/t.html && node pdf.cjs --html ../calisma/t.html --olc`

Not: 2021-22 sınavının kitapçığı olmadığından o yılın soruları öğrencilerin hatırladıklarından derlenmiştir
(`21-22*`). Resmi cevap anahtarı yoktur.
