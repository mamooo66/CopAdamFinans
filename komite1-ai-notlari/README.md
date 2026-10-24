# Komite 1 AI Notları (2026-27)

BAİBÜ Tıp Dönem III, Hastalıkların Biyolojik Temeli Kurulu (I. Kurul, sınav 30 Ekim 2026) için ders ders
ayrılmış ayrıntılı notlar. **Her ders ayrı PDF'tir**: `Komite1_AI_Notlari_Patoloji.pdf`, `…_Pediatri.pdf`,
`…_Aile_Hekimligi.pdf`, `…_Enfeksiyon.pdf`, `…_Farmakoloji.pdf`, `…_Dahiliye.pdf`, `…_Nukleer_Tip.pdf`.
Son 5 yılın (2021-22 → 2025-26) kurul sınavında çıkmış bilgiler kırmızı **ÇIKMIŞ** etiketiyle (yıl/yıllar)
işaretlenir. Her dersin sonunda o dersin çıkmış soruları (doğru cevap + çeldiriciler) yer alır.

**Kaynak kuralı:** Notlar yalnızca bu dönemin (2026-27) ders PDF'lerinden yazılır (Drive › Komite-1 › PDF ›
<Ders> › 2026-2027(yeni)). Eski klasör, geçmiş yılların notları ve kitaplar kullanılmaz. Bir dersin 2026-27 PDF'i
gelmeden o ders notlara girmez. Çıkmış sorunun cevabı PDF'te yoksa soru yine gösterilir ve “(PDF'te geçmiyor)” diye
işaretlenir.

- `sorular/<ders>_cikmis.md` — son 5 yılın kurul soruları (tam metin; kimlikle grep edilir)
- `kaynak/` — PDF'lerin üretildiği kaynaklar
  - `bolumler/<harf>NN_*.py` — her ders saati/konusu bir modül; harf: p Patoloji · c Pediatri · a Aile Hekimliği ·
    e Enfeksiyon · f Farmakoloji · d Dahiliye · n Nükleer Tıp; sıra dosya numarasına göre
  - `cikmis_<ders>.py` — PDF'i henüz gelmemiş derslerin çıkmış soruları (notlara girmez)
  - `yardim.py` — modüllerin yazım yardımcıları (madde, kart, soru); `icerik.py` — modülleri yükler
  - `olustur.py` — bir dersin HTML'ini üretir; `bas.py` — ders başına PDF basar; `stil.css`, `sigdir.js` — görünüm ve yazı boyutu sığdırma
  - `pdf.cjs` — Playwright/Chromium ile PDF'e basar (`--olc`: yalnızca sığma raporu)
  - `araclar/` — `pdf_metin.py` (ders PDF'i → sayfa işaretli metin, sayfa resmi, 9'lu önizleme panosu), `kapsam.py`
    (PDF'in modülde karşılığı olmayan sayfaları), `sadakat.py` (maddelerin PDF metniyle örtüşmesi), `denetle.py`
    (soru ve rozet denetimi)
  - `fontlar/` — Inter yazı tipinden türetilmiş TTF'ler (SIL OFL 1.1, bkz. `fontlar/OFL.txt`)

Yeni bir oturumda çalışmaya devam etmek için önce depo kökündeki `CLAUDE.md`'ye bakın (kurulum, kurallar,
yapılacaklar).

Yeniden üretmek için:

```bash
cd komite1-ai-notlari/kaynak
python3 bas.py              # bütün dersler
python3 bas.py patoloji     # tek ders
```

Tek bölümü denemek için: `python3 olustur.py --sadece p02_hasar --cikti ../calisma/t.html && node pdf.cjs --html ../calisma/t.html --olc`

Not: 2021-22 sınavının kitapçığı olmadığından o yılın soruları öğrencilerin hatırladıklarından derlenmiştir
(`21-22*`). Resmi cevap anahtarı yoktur.
