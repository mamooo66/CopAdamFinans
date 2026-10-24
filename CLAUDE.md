# Komite 1 AI Notları — devir notu (yeni oturum buradan başlar)

Bu repo BAİBÜ Tıp Dönem III, I. Kurul (Hastalıkların Biyolojik Temeli) için **Patoloji + Farmakoloji hap bilgi slayt
PDF'i** üretir. Sınav **30 Ekim 2026**. Her ders bir Python modülüdür; modüllerden HTML üretilir, HTML Playwright ile
16:9 PDF'e basılır. Son 5 yılın (2021-22 → 2025-26) kurul sorularında geçen bilgiler kırmızı **ÇIKMIŞ** rozetiyle
işaretlidir. Her dersin sonunda o dersin çıkmış soruları yer alır.

**Durum (15 Eki 2026):** `komite1-ai-notlari/Komite1_AI_Notlari_<Ders>.pdf` 501 slayttır.
- Patoloji: 15 ders, 81 soru.
- Farmakoloji: 19 ders, 83 soru.

Branch `claude/komite-1-patoloji-ozet-0s5dt7`. Kullanıcı istemedikçe PR açma.

## 1. Kullanıcının kuralları (çiğneme)
1. **Yalnızca bu dönemin (2026-27) ders PDF'leri kullanılır.** Kullanıcının talimatı: “Bu PDF'lerdeki bilgilerin
   dışına çıkma.” Eski klasör, geçmiş yıl notları, kitap ya da kendi bilginle slayt maddesi yazma. Kullanıcı bu yüzden
   bir kez çok kızdı.
2. Çıkmış sorunun doğru cevabı PDF'te yoksa soru yine konur. Cevabı kendi bilginle ver ve notu
   ` · (PDF'te geçmiyor)` ile bitir.
3. PDF'i gelmemiş ders desteye girmez. O dersin soruları `cikmis_*.py` dosyasında BEKLEYEN'de bekler.
4. Kullanıcıyla Türkçe ve kısa konuş. Resmi cevap anahtarı yok: emin olmadığın cevabı soru notunda belirt, kullanıcıya
   da sor.

## 2. Token tasarrufu
- **Okuma:** `olustur.py`, `stil.css`, `sigdir.js`, `pdf.cjs` ve `README.md`'yi okuma; kod bu dosyada anlatıldı.
  Repoyu tarama. Yalnız üzerinde çalıştığın modülü oku. Yeni modül yazarken örnek olarak
  `bolumler/f12_antikoagulan.py`'nin ilk ~40 satırı yeter.
- **PDF:** PDF'i Read ile açma; sayfalar resim olarak gelir ve çok pahalıdır. Önce `araclar/pdf_metin.py` ile metne
  çevir, sonra `.txt` dosyasını oku. Uzun metni parça parça oku.
- **Resimler:** Araç, metni çıkmayan sayfaları listeler. Bunlardan yalnız sınavlık tablo ya da sınıflama taşıyanlara
  `--resim N --dpi 70` ile bak. Ders başına en çok 3 resim.
- **Soru bankası:** Bankayı bütün okuma, soruyu kimliğiyle çek:
  `grep "2024-25 S31\." komite1-ai-notlari/sorular/farmakoloji_cikmis.md`
- **Derleme:** Denerken yalnız ilgili modülü derle (`--sadece`). Tam desteyi en sonda bir kez bas.
- **Alt ajan:** Birden çok ders birlikte gelirse ders başına bir alt ajan açabilirsin (ucuz model, ör. Sonnet). Ajana
  §1 ve §5'i, PDF metin dosyasının yolunu ve o dersin soru kimliklerini ver. Tek ders için ajan açma.
- **Bitirince:** Ders bitince commit + push yap, kullanıcıya 2-4 satırlık rapor ver.

## 3. Kurulum (kullanıcının bilgisayarında, bir kez)
```bash
git clone https://github.com/mamooo66/CopAdamFinans.git && cd CopAdamFinans
git checkout claude/komite-1-patoloji-ozet-0s5dt7
cd komite1-ai-notlari/kaynak
npm install && npx playwright install chromium   # PDF basmak için
pip install pymupdf                               # PDF → metin ve sayfa resmi
```
- **Gerekenler:** git, Python 3.8+, Node 18+.
- **Windows:** `python3` yerine `python` yaz. Türkçe çıktı bozulursa `set PYTHONUTF8=1`.
- **Klasörler:** Kullanıcının PDF'leri `komite1-ai-notlari/pdf/` altına, ara dosyalar `komite1-ai-notlari/calisma/`
  altına gider. İkisi de gitignore'da, commit edilmez.
- **Drive:** Ders PDF'lerinin Drive'daki yeri: Komite-1 › PDF › Patoloji | Farmakoloji › 2026-2027(yeni) ›
  <hoca klasörü>. Drive bağlayıcısı büyük PDF'te yalnız ilk ~80 sayfanın metnini verir; yerel dosyayı kullan.

## 4. Dosyalar
```
komite1-ai-notlari/
  Komite1_AI_Notlari_<Ders>.pdf      çıktı (commit edilir)
  sorular/patoloji_cikmis.md, farmakoloji_cikmis.md
      son 5 yılın kurul soruları, tam metin
      kimlik: "2025-26 S23" = kitapçıktaki soru no; "2021-22* H3" = kitapçık yok, hatırlanan soru
  kaynak/
    bolumler/pNN_*.py, fNN_*.py   her ders bir modül; sıra ve kod dosya adından gelir (f12_… → F12)
    cikmis_patoloji.py, cikmis_farmakoloji.py   BEKLEYEN: PDF'i gelmemiş derslerin soruları
    yardim.py      B, C, Q, YILLAR
    icerik.py      modülleri yükler
    olustur.py     → slaytlar.html
    pdf.cjs        → PDF
    araclar/       pdf_metin.py, denetle.py, sadakat.py
```

## 5. Modül biçimi
```python
# -*- coding: utf-8 -*-
"""Kaynak: Drive › Komite-1 › PDF › Farmakoloji › 2026-2027(yeni) › <Hoca> › <PDF adı>"""

from yardim import B, C, Q  # noqa: F401

BOLUM = dict(
    key="antianemik", baslik="Antianemik İlaçlar",
    hoca="Doç. Dr. Oruç Yunusoğlu", tarih="9 Ekim", saat="2 saat",          # saat isteğe bağlı
    kaynak="<PDF adı> · Doç. Dr. O. Yunusoğlu · 2026",
    ozet=["2-3 kısa madde: bu dersten ne soruldu, tekrar eden tuzaklar"],  # soru yoksa: "Son 5 yılda bu dersten soru çıkmadı."
    # eksik="…",                     # yalnız ders yarımsa: ayraçta turuncu uyarı kutusu çıkar
    slaytlar=[                       # her slayt = 2-5 karttan oluşan liste
        [C("Kart başlığı", [
            B("Madde; **anahtar terim** kalın", y="24-25 25-26", tuzak="“sınavdaki yanlış ifade” → YANLIŞ"),
            B("Alt madde", lvl=1),
        ]), C("…", [B("…")])],
    ],
    sorular=[                        # en yeni yıl önce
        Q("25-26", 35, "Kısa soru kökü?", "b) Doğru şık", "Çeldiriciler / PDF'teki dayanak"),
        Q("21-22", None, "Hatırlanan soru…", "Cevap", "…"),
    ],
)
```
- **`B(t, y=None, tuzak=None, g=None, lvl=0)`:**
  - `y`: bu bilginin sorulduğu yıllar, boşlukla ayrılmış. Kırmızı ÇIKMIŞ rozeti çıkarır; 3+ yılda ★ eklenir.
  - `tuzak`: bilginin sınavdaki yanlış hali.
  - `g`: gri etiket (şu an kullanılmıyor).
- **`Q(y, no, kok, cevap, not_=None, n=1, ref=False)`:**
  - Kök en çok 150, not en çok 170 karakter.
  - `ref=True`: soru başka bölümde sayılıyor, bu yalnız atıf kopyası. Notta “Soru Farmakoloji F04'te sayılır” gibi
    belirt.
- **Rozet:**
  - Sorunun doğru cevabını taşıyan maddeye o yılı yaz.
  - "Hangisi yanlıştır" sorusunda slayttaki doğru şıklara da yaz; yanlış şık, ilgili doğru maddenin `tuzak`'ı olur.
  - Yalnız slaytta olan bilgiye rozet koy.
- **Slayt yoğunluğu:**
  - Slayt başına ≈1300-1700 karakter (10-16 madde); madde en çok ~180 karakter. Taşarsa slaytı böl.
  - PDF'in terimlerini, sayılarını, listelerini, sınıflamalarını ve sırasını koru.
  - Başlık, teşekkür ve kaynak slaytlarını atla.

## 6. Komutlar (`komite1-ai-notlari/kaynak/` içinden)
```bash
python3 araclar/pdf_metin.py ../pdf/DERS.pdf --cikti ../calisma/ders.txt           # metin + metinsiz sayfa listesi
python3 araclar/pdf_metin.py ../pdf/DERS.pdf --sayfa 76- --cikti ../calisma/son.txt  # yalnız bir aralık
python3 araclar/pdf_metin.py ../pdf/DERS.pdf --resim 12 --dpi 70 --klasor ../calisma # tek sayfanın PNG'si
python3 olustur.py --sadece f20_antianemik --cikti ../calisma/t.html && node pdf.cjs --html ../calisma/t.html --olc
python3 araclar/denetle.py                                    # soru tekrarı, kayıp soru, rozet-soru tutarlılığı
python3 araclar/sadakat.py f20_antianemik ../calisma/ders.txt # PDF metniyle örtüşmeyen maddeler (uydurma kontrolü)
python3 olustur.py && node pdf.cjs                            # tam deste → ../Komite1_AI_Notlari_<Ders>.pdf
git add -A komite1-ai-notlari && git commit -m "…" && git push -u origin claude/komite-1-patoloji-ozet-0s5dt7
```
- `--olc` çıktısı "tüm slaytlar sığıyor (≥13px)" olmalı. "TAŞIYOR" ya da "13px altı" görürsen slaytı böl ya da kısalt.
- `--sadece` modülün **dosya adını** alır (`f05_uygulama`), `key`'ini değil.
- `denetle.py` çıktısı "HİÇBİR YERDE YOK: 0" olmalı ve "TEKRAR" satırı çıkmamalı.
- Ders ekledikten sonra baştaki sayfalara (kapak, içindekiler, dağılım tablosu, ders ayraçları) bak:
  `python3 araclar/pdf_metin.py ../Komite1_AI_Notlari_<Ders>.pdf --resim 1-6 --dpi 50 --klasor ../calisma`
  Ders sayısı arttıkça içindekiler ve ayraçtaki ders çipleri taşabilir; ayraçlar sığma ölçümüne girmez. Taşma varsa
  `stil.css`'te `.ders-ayrac .dv-cip` ve `.toc` boyutlarını küçült.

## 7. Yapılacaklar
### 7.1 Yarım kalan 3 patoloji dersi (Drive 80. sayfadan sonrasını vermedi)
| Modül | PDF (hoca: Selma Erdoğan Düzcü) | Desteye giren | Eklenecek |
|---|---|---|---|
| `p04_inflamasyon` | 3-AKUT VE KRONİK İNFLAMASYON (11,7 MB) | s.1-~79; son kart “Araşidonik asit metabolitleri / siklooksijenaz yolu” (TXA₂'de kesik) | AA metabolitlerinin devamı, diğer mediatörler, **kronik inflamasyon** |
| `p05_iyilesme` | 4-İYİLEŞME, TAMİR VE ONARIM (14,6 MB) | s.1-80; son kart “Doku onarımını etkileyen faktörler” | s.81-son |
| `p06_hemodinamik` | 5-HEMODİNAMİK BOZUKLUKLAR (9 MB) | s.1-80; son kart “Tromboz: Virchow triadı” | trombüsün devamı, DIC, emboli, infarktüs, şok |

Adımlar:
1. `--sayfa 76-` ile PDF'in son kısmının metnini çıkar.
2. Modülün son 1-2 slaytını oku. Kesilen yerden devam ederek yeni slaytları `slaytlar` listesinin sonuna ekle; eski
   slaytları yeniden yazma.
3. `eksik=` satırını sil. `ozet` kesiklikten söz ediliyorsa düzelt.
4. Aşağıdaki soruların cevabını yeni sayfalardan doğrula, notlarını düzelt ve ilgili maddeleri rozetle:
   - **p04:** 25-26 S69, S78 · 24-25 S72 · 23-24 S63, S64 · 22-23 S63, S74. Notlarındaki `_KESIK` ekini kaldır; hiç
     kalmazsa `_KESIK` tanımını da sil.
   - **p06:** 25-26 S71 · 24-25 S74. Notlarında "PDF 81+. slayt okunamadı" yazıyor.
5. `--olc` ve `denetle.py` çalıştır, commit et.

### 7.2 PDF'i gelmemiş dersler (yeni modül)
Bunların çoğu ileri tarihli; PDF'ler ders işlendikçe gelecek. Yeni dosya numarasını mevcutların sonuna ver
(Patoloji p16+, Farmakoloji f20+). Mevcut dosyaları yeniden numaralama: notlarda “F04'te / F19'da sayılır” atıfları var.

Sorular hazır: `cikmis_*.py` → `BEKLEYEN["<key>"]` (baslik, hoca, tarih ve Q kayıtları).

Adımlar:
1. PDF'i metne çevir.
2. Modülü yaz; başlık bilgilerini BEKLEYEN'den al.
3. Q kayıtlarını modüle taşı ve **her cevabı PDF'ten doğrula**. Farmakoloji cevapları önceki oturumun tahminidir,
   doğrulanmadı; 25-26 S32'nin cevabı "?" olarak duruyor.
4. Tam soru metni ve şıklar için `sorular/*.md`'de grep yap; ilgili maddeleri rozetle.
5. O anahtarı BEKLEYEN'den sil.
6. `--olc` ve `denetle.py` çalıştır, commit et.

| Ders (tarih) | BEKLEYEN key | Önerilen dosya | Soru |
|---|---|---|---|
| Pato · Tümöre karşı konak savunması, tümörün konağa etkileri, kanser tanısı (13 Eki) | konak | p16_konak | 3 |
| Pato · Tümör büyümesinin biyolojisi, anjiogenez, invazyon, metastaz (15 Eki) | buyume | p17_buyume | 3 |
| Pato · Dalak patolojisi (19 Eki) | dalak | p18_dalak | 1 |
| Pato · İmmün sistem patolojisi (20-22 Eki) | immun | p19_immun | 15 |
| Pato · İnfeksiyon hastalıklarının patolojisi (23, 26 Eki) | enf | p20_enfeksiyon | 4 |
| Farma · Antianemik ilaçlar (9 Eki) | antianemik | f20_antianemik | 3 |
| Farma · İmmünmodülatörler (14 Eki) | immunmodulator | f21_immunmodulator | 4 |
| Farma · Makrolidler ve linkozamidler (19 Eki) | makrolid | f22_makrolid | 4 |
| Farma · Beta laktam antibiyotikler (20 Eki) | betalaktam | f23_betalaktam | 7 |
| Farma · Antiviral ilaçlar (21 Eki) | antiviral | f24_antiviral | 5 |
| Farma · Antimalaryal ve ektoparaziter ilaçlar (22 Eki) | antimalaryal | f25_antimalaryal | 4 |
| Farma · Antistafilokoksik ve dar spektrumlu antianaerob ilaçlar (22 Eki) | antistafilokoksik | f26_antistafilokoksik | 2 |
| Farma · Tüberküloz ve lepra ilaçları (23 Eki) | tuberkuloz | f27_tuberkuloz | 5 |
| Farma · Kinolonlar (26 Eki) | kinolon | f28_kinolon | 5 |
| Farma · Aminoglikozidler (26 Eki) | aminoglikozid | f29_aminoglikozid | 6 |
| Farma · Antifungal ilaçlar (27 Eki) | antifungal | f30_antifungal | 5 |

### 7.3 Küçük eksikler (kullanıcı isterse)
- **`p09_neoplazi`** (PDF: 1-Neopl-isimlendirme-biyolojisi, Çetin Boran): Drive metni yalnız ~6 bin karakter geldi ve
  modül 7 slayt. PDF'in tamamının işlendiğini kontrol et.
- **`f09_etkilesim`** (PDF: 4-ilaç-ilaç etkileşimleri, Oruç Yunusoğlu): emilim ve dağılım etkileşimi slaytları
  resimdi; modülde yoklar.
- **Okunmamış resim sayfaları:** Metni çıkmadığı için okunmadılar; çoğu şema. Yalnız sınavlık bilgi varsa ekle.
  - F03: Tablo 5.2 (s.8) ve Tablo 5.1-B'deki aktivite işaretleri
  - F05: s.4, 34, 57
  - F06: s.3, 11-12, 21, 23-25, 30, 36, 50-53, 60
  - F12: s.18-20, 22, 24, 30
  - F13: s.10, 12, 14, 23
  - F14: s.20-21
  - F15: s.2, 4, 6, 8, 11, 14, 15
  - F17: s.10, 11, 13

### 7.4 Cevabı şüpheli sorular (resmi anahtar yok; kullanıcı anahtarı bulursa düzelt)
- **25-26 S23 (F12):** Kök "doğrudur" diyor ama PDF'e göre B-E doğru. Muhtemelen kök "yanlıştır"dı; o zaman cevap A
  (L-arjinin benzeri olan argatroban'dır, dabigatran değil).
- **25-26 S24 (F13):** PDF'e göre absiksimab da tirofiban da GP IIb/IIIa blokörü; iki şık doğru.
- **25-26 S26 (F16):** B seçildi (minosiklin en uzun etkili), ama E de PDF'e uyuyor.
- **23-24 S34 = 24-25 S49 (F15):** e (eritromisin) seçildi. PDF novobiosini DNA giraz altında gösteriyor, yani a da
  olabilir.
- **24-25 S55 (F18):** Cevap PDF'te yok. Borik asit seçildi; formaldehit de olabilir.
- **25-26 S13 (F09):** c seçildi (Sınıf IV'te de serum düzeyi takibi gerekebilir).
