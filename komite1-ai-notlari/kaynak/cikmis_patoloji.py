# -*- coding: utf-8 -*-
"""Son 5 yılın (2021-22 → 2025-26) Kurul 1 PATOLOJİ çıkmış soruları — konu konu, cevaplı.

Yalnızca çıkmış soru kitapçıklarından derlendi. Yalnızca 2026-27 PDF'i HENÜZ YÜKLENMEMİŞ dersler (dalak, immün sistem, infeksiyon patolojisi). Bu konuların hap bilgi slaytları yok:
ilgili dersin 2026-27 PDF'i Drive'da okunabilir olunca o PDF'ten yazılıp desteye eklenecek
(bolumler/pNN_*.py). Desteye girmeden önce her sorunun cevabı/notu o PDF ile karşılaştırılmalı.

Q(yıl, soru_no, kök, cevap, not, n=kaç soruyu temsil ettiği, ref=sayıma girmeyen çapraz atıf)
"""

from yardim import Q

BEKLEYEN = {}

# ---------------------------------------------------------------- dalak
BEKLEYEN['dalak'] = dict(
    baslik='Dalak Patolojisi',
    hoca='Dr. Öğr. Üyesi Songül Peltek Özer', tarih='19 Ekim',
    sorular=[
        Q('23-24', 70, 'Portal hipertansiyon ilişkili konjesyon varlığıyla karakterize splenomegali?', 'Splenik ven trombozu', 'Tüberküloz, ekinokok, Hodgkin lenfoma, amiloidoz değil'),
        Q('İÇ HAST.', None, 'İlişkili İç Hastalıkları çıkmışları (22-23 S44 · 23-24 S42 · 24-25 S8 · 25-26 S47)', "Aplastik anemide splenomegali görülmez · demir eksikliği anemisi masif splenomegali yapmaz · EMN'de splenomegali + servikal LAP", 'Patoloji sorusu değil; konu tekrarı için eklendi', ref=True),
    ],
)

# ---------------------------------------------------------------- immun
BEKLEYEN['immun'] = dict(
    baslik='İmmün Sistem Patolojisi',
    hoca='Dr. Öğr. Üyesi Songül Peltek Özer', tarih='20-22 Ekim',
    sorular=[
        Q('25-26', 63, '42 yaş erkek; yılın belli dönemlerinde artan göz kaşıntısı, gözyaşı, burun akıntısı — mekanizma?', 'Tip I hipersensitivite', 'Tip II, III, IV, otoimmünite değil'),
        Q('25-26', 64, 'AIDS hastalarında fırsatçı enfeksiyon etkenlerinden biri OLMAYAN?', 'Streptococcus pneumoniae', 'P. jirovecii, C. albicans, CMV, T. gondii fırsatçı'),
        Q('25-26', 65, 'Foxp3 geni hangi hücrelerin regülasyonunda önemli rol oynar?', 'T helper (CD4+ CD25+ regülatuvar T)', 'Eozinofil, makrofaj, mast hücresi, nötrofil değil'),
        Q('25-26', 66, "SCID, Bruton, DiGeorge, X'e bağlı lenfoproliferatif sendrom — hangileri lenfosit matürasyon defektidir?", 'Kitaba göre I, II, III — şıklarda yok; en uygun: d) I, II, III ve IV', '⚠ Cevap anahtarı yok; XLP genelde “aktivasyon defekti” sayılır — İmmün sistem PDF’i gelince kontrol edilecek'),
        Q('24-25', 88, 'Bir otoimmün hastalıkta inflamasyon nötrofilden zenginse rol alan lenfosit?', 'T-helper-17', 'Th1, Th2, NK, CTL değil'),
        Q('24-25', 89, 'Antikora bağımlı eritrosit yıkımı → hemolitik anemi; hipersensitivite tipi?', 'Tip II'),
        Q('24-25', 90, 'Fas mutasyonu olan kişide otoimmün hastalık gelişmesinin en olası mekanizması?', 'Otoreaktif lenfositler apoptoza uğratılamaz', 'Sinyal iletimi, süpresör gen, antikor sentezi, CTLA-4 aktivasyonu değil'),
        Q('23-24', 75, 'Enfeksiyonla ekspresyonu artarsa otoimmüniteye yatkınlık oluşturan hücre yüzey molekülü (reseptörü)?', 'CD28', 'CTLA4, CD3, AIRE, Foxp3 değil'),
        Q('23-24', 78, 'Yaygın vaskülitlerle seyreden tablo — hipersensitivite tipi?', 'Tip III'),
        Q('23-24', 79, 'IgM aşırı yüksek + immün yetmezlik; lenfosit gelişim bozukluğu?', 'CD40 mutasyonu (hiper-IgM sendromu)', 'Btk, 22q11 delesyonu, ADA, MHC II ekspresyon bozukluğu değil'),
        Q('22-23', 79, 'Doğal immünitenin komponenti olan hücre?', 'NK hücreleri', 'CD8 CTL, B lenfosit, CD4 Th = edinsel (dendritik hücre derste APC olarak edinsel başlıkta)'),
        Q('22-23', 80, 'Santral immün toleransta görev alan?', 'AIRE', 'IPEX, PD-1, CTLA-4, FAS = periferik tolerans'),
        Q('22-23', 81, 'Yanlış olan?', '“Miks konnektif doku hastalığı diğer otoimmün hastalıklara göre tedaviye daha dirençlidir”', "Doğrular: SLE tip III · RF anti-IgG · Scl-70 SSc tanı koydurucu · RA'da anti-sitrüllinlenmiş peptid"),
        Q('22-23', 82, 'T lenfosit diferansiasyon yolundaki mutasyon/eksiklikle oluşan immün yetmezlik?', 'Şiddetli kombine immün yetmezlik (SCID)', 'Hiper-IgM, CVID, Bruton, Chediak-Higashi değil'),
        Q('21-22', None, 'Tip 3 hipersensitivite örneği?', 'Vaskülit / SLE', 'Öğrenci hatırlamasından derlenmiş soru'),
    ],
)

# ---------------------------------------------------------------- enf
BEKLEYEN['enf'] = dict(
    baslik='İnfeksiyon Hastalıklarının Patolojisi (Bakteri, Virüs, Mantar, Parazit)',
    hoca='Dr. Öğr. Üyesi Songül Peltek Özer', tarih='23 ve 26 Ekim',
    sorular=[
        Q('24-25', 82, 'Akut apandisit etyolojisinde rol oynayabilen enfeksiyon ajanı?', 'Enterobius vermicularis', 'HSV, HPV, E. histolytica, molluskum kontagiozum değil'),
        Q('23-24', 82, 'Vücutta mononükleer inflamasyona yol açan bakteri?', 'Treponema pallidum', 'S. aureus, grup A streptokok, C. perfringens, C. jejuni → süpüratif/nekrotizan'),
        Q('22-23', 83, 'Hangisi bakteriyel bir hastalık DEĞİLDİR?', 'Tinea versikolor (Malassezia — mantar)', 'İmpetigo, erizipel, kızıl, psödomembranöz enterokolit bakteriyel'),
        Q('25-26', 64, '(AIDS fırsatçı enfeksiyonları — bkz. Bölüm 21)', 'Fırsatçı olmayan: S. pneumoniae', ref=True),
        Q('21-22', None, 'Pnömokok pnömonisi · Kronik hepatit yapmayan ajan · COVID-19 akciğer patolojisi evreleri', 'Süpüratif, lober tutulum · HAV/HEV kronikleşmez (HBV/HCV yapar) · eksüdatif faz (DAH)', 'Öğrenci hatırlamasından; şıklar tam bilinmiyor', n=3),
    ],
)
