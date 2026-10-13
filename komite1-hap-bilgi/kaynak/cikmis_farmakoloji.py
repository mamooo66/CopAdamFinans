# -*- coding: utf-8 -*-
"""Son 5 yılın (2021-22 → 2025-26) Kurul 1 FARMAKOLOJİ çıkmış soruları — 2026-27 PDF'i HENÜZ OLMAYAN dersler.

Bu konuların hap bilgi slaytları yok; ilgili dersin 2026-27 PDF'i Drive'da görünür olunca o PDF'ten yazılıp
desteye eklenecek (bolumler/fNN_*.py). Resmi cevap anahtarı yok: buradaki cevaplar PDF gelince o PDF ile
karşılaştırılmalı; "?" ile işaretlenenler şüpheli.
PDF'i olan derslerin soruları kendi bölüm modüllerinde (bolumler/) durur.

Q(yıl, soru_no, kök, cevap, not, n=kaç soruyu temsil ettiği, ref=sayıma girmeyen çapraz atıf)
"""

from yardim import Q

BEKLEYEN = {}

BEKLEYEN["immunmodulator"] = dict(
    baslik="İmmünmodülatörler", hoca="Prof. Dr. Akif Hakan Kurt", tarih="14 Ekim",
    sorular=[
        Q("25-26", 25, "İmmünomodülatör ilaçlar için yanlış olan?", "Mikofenolat mofetilin etki mekanizması siklofosfamide benzer",
          "Doğrular: siklosporin kalsinörini selektif inhibe eder · takrolimus karaciğer Tx'te tercih · sirolimus: hiperlipidemi, trombositopeni · azatioprin ameliyat günü başlanır"),
        Q("24-25", 34, "İmmünomodülatör ilaçlar için yanlış olan?", "Siklosporin otoimmün yanıtın GEÇ basamaklarını önler (doğrusu: erken)"),
        Q("23-24", 20, "İmmünomodülatör ilaçlar için yanlış olan?", "Azatioprin FOLAT antimetabolitidir (doğrusu: purin antimetaboliti)"),
        Q("22-23", 31, "İmmünomodülatör ilaçlar için yanlış olan?", "Sirolimus immünsüpresiflerden efikasitesi en yüksek olanıdır",
          "Doğrular: siklosporin erken basamak · IFN-α/β, IL-2 immünopotansiyalizasyon · takrolimus suda daha çözünür"),
    ],
)

BEKLEYEN["antianemik"] = dict(
    baslik="Antianemik İlaçlar", hoca="Doç. Dr. Oruç Yunusoğlu", tarih="9 Ekim",
    sorular=[
        Q("25-26", 35, "Eritropoietin (EPO) tedavisiyle ilgili doğru olan?", "Böbrekten salgılanan doğal hormonun rekombinant formudur",
          "? “Bazı anemilerde etkisiz olabilir” şıkkı da doğru görünüyor · yanlışlar: yıkımı artırır, karaciğerde sentez, hipotansiyon"),
        Q("24-25", 54, "Antianemik/hematopoetik ilaçlarla ilgili yanlış olan?", "B9 eksikliğinin belirgin sonucu pernisiyöz anemidir (pernisiyöz anemi B12)",
          "Doğrular: demir zehirlenmesinde deferoksamin · filgrastim G-CSF · epoetin sıklıkla hipertansiyon"),
        Q("22-23", 16, "Antianemik ilaçlarla ilgili doğru olmayan?", "Epoetin pahalı ve sık hipotansiyon yapar (doğrusu: hipertansiyon)"),
    ],
)

BEKLEYEN["makrolid"] = dict(
    baslik="Makrolidler ve Linkozamidler", hoca="Prof. Dr. Akif Hakan Kurt", tarih="19 Ekim",
    sorular=[
        Q("25-26", 32, "Makrolid antibiyotikler için yanlış olan?", "? (PDF gelince belirlenecek)",
          "Şıklar: spiramisin eritromisinden az etkili · klaritromisin aside dayanıklı, uzun etkili · azitromisin lejyonerde 1. sıra · roksitromisin GİS/hepatik yan etki az · telitromisin safrayla yavaş itrah"),
        Q("24-25", 41, "Makrolid antibiyotikler için doğru olan?", "Eritromisin, penisilin allerjisinde gram (+) cilt, yumuşak doku ve solunum yolu enfeksiyonlarında kullanılır",
          "Yanlışlar: spiramisin dağılımı iyi değil · klaritromisin aside dayanıksız · azitromisin CYP3A4 inhibe eder · roksitromisin daha az serum düzeyi"),
        Q("23-24", 26, "Makrolid antibiyotikler arasında yer ALMAYAN?", "Kuinupristin", "Eritromisin, klaritromisin, azitromisin, roksitromisin makrolid"),
        Q("22-23", 38, "Makrolid antibiyotikler arasında yer ALMAYAN?", "Kuinupristin"),
    ],
)

BEKLEYEN["betalaktam"] = dict(
    baslik="Beta Laktam Antibiyotikler", hoca="Prof. Dr. Akif Hakan Kurt", tarih="20 Ekim",
    sorular=[
        Q("25-26", 28, "β-laktamazlara dayanıklı OLMAYAN penisilin?", "Azlosilin", "Okloksasilin, nafsilin, flukloksasilin, metisilin dayanıklı"),
        Q("25-26", 29, "Sefalosporinler için yanlış olan?", "Sefazolin ve sefasetril alkolle disülfiram reaksiyonu yapar"),
        Q("24-25", 38, "Penisilinler için doğru olan?", "Metisiline dirençte vankomisin, teikoplanin ve bunların rifampinle kombinasyonu kullanılır",
          "Yanlışlar: amoksisilin daha fazla diyare · antistafilokok penisilinler β-laktamaza dayanıksız · aminopenisilinler dar spektrumlu"),
        Q("23-24", 23, "β-laktamazlara dayanıklı OLMAYAN penisilin?", "Karbenisilin"),
        Q("22-23", 34, "β-laktam antibiyotikler arasında yer ALMAYAN?", "Aminoglikozidler", "Monobaktam, sefalosporin, karbapenem, penisilin β-laktam"),
        Q("22-23", 35, "β-laktamazlara dayanıklı OLMAYAN penisilin?", "Karbenisilin"),
        Q("21-22", None, "Aztreonam özellikleri (eşleştirme)", "PBP-3'e bağlanır, dar spektrum (gram −), penisilin allerjisinde kullanılabilir, renal atılır, nefro/ototoksik değil",
          "Öğrenci hatırlamasından derlenmiş soru"),
    ],
)

BEKLEYEN["kinolon"] = dict(
    baslik="Kinolonlar", hoca="Prof. Dr. Akif Hakan Kurt", tarih="26 Ekim",
    sorular=[
        Q("25-26", 30, "Fluorokinolonlar için yanlış olan?", "Plazma proteinlerine bağlanma oranları yüksektir (doğrusu: düşük)"),
        Q("24-25", 39, "Fluorokinolonlar için yanlış olan?", "Streptococcus pneumoniae'de en çok tercih edilen ilaçlardır",
          "Doğrular: DNA giraz (topoizomeraz II) inhibisyonu, bakterisid · proteine bağlanma düşük · sükralfat/Ca/Zn/Fe şelat · nokardiya ve streptokoklara etkisiz"),
        Q("23-24", 24, "Fluorokinolonlar için yanlış olan?", "Ofloksasin karaciğerde en fazla metabolize edilen kinolondur"),
        Q("22-23", 36, "Fluorokinolonlar için yanlış olan?", "Ofloksasin karaciğerde en fazla metabolize edilen kinolondur"),
        Q("21-22", None, "Florokinolon için yanlış olan?", "“Dar spektrumludur”", "Öğrenci hatırlamasından derlenmiş soru"),
    ],
)

BEKLEYEN["aminoglikozid"] = dict(
    baslik="Aminoglikozidler", hoca="Prof. Dr. Akif Hakan Kurt", tarih="26 Ekim",
    sorular=[
        Q("25-26", 33, "Aminoglikozidler için yanlış olan?", "Oral kullanımda kanda terapötik seviyelere ulaşabilirler",
          "Doğrular: anaeroblara etkisiz · lipofilitesi düşük · tek başına yalnız idrar yolu infeksiyonunda · vestibüler/koklear toksisite"),
        Q("24-25", 42, "Aminoglikozidler için yanlış olan?", "Terapötik indeksleri geniştir (doğrusu: dar)"),
        Q("23-24", 27, "Aminoglikozidler için yanlış olan?", "Safra yolu ile itrah edilirler"),
        Q("22-23", 39, "Aminoglikozidler için yanlış olan?", "Plazma proteinlerine yüksek oranda bağlanırlar"),
        Q("21-22", None, "Aminoglikozidlerle ilgili doğru olan?", "Polar olduklarından en az lipofilik antibiyotiklerdir", "Öğrenci hatırlamasından derlenmiş soru"),
        Q("21-22", None, "Antipsödomonal ilaç?", "Aminoglikozid (amikasin, gentamisin, tobramisin)", "Öğrenci hatırlamasından derlenmiş soru"),
    ],
)

BEKLEYEN["antifungal"] = dict(
    baslik="Antifungal İlaçlar", hoca="Prof. Dr. Akif Hakan Kurt", tarih="27 Ekim",
    sorular=[
        Q("25-26", 31, "Triazol türevi antifungaller için doğru olan?", "Klotrimazol, Malassezia furfur ve Corynebacterium minutissimum'a etkilidir",
          "Yanlışlar: ketokonazol gebede · itrakonazol daha dar spektrum · flukonazol yiyecekten etkilenir · vorikonazol imidazol"),
        Q("24-25", 40, "Triazol türevi antifungaller için doğru olan?", "Flukonazol testosteron ve estradiol sentezini etkilemez"),
        Q("23-24", 25, "Triazollerin imidazollere üstünlüklerinden biri OLMAYAN?", "CYP2C19 ve CYP3A4 inhibisyonu yapmaz"),
        Q("22-23", 37, "Triazollerin imidazollere üstünlüklerinden biri OLMAYAN?", "Daha geniş spektrumludur"),
        Q("21-22", None, "Triazolün imidazole üstünlüklerinden olmayan?", "Daha geniş spektrumludur",
          "Üstünlükler: yavaş metabolize (uzun etki, uzun doz aralığı) · direkt toksisite az · endokrin yan etki yok · öğrenci hatırlaması"),
    ],
)

BEKLEYEN["antiviral"] = dict(
    baslik="Antiviral İlaçlar", hoca="Doç. Dr. Oruç Yunusoğlu", tarih="21 Ekim",
    sorular=[
        Q("25-26", 36, "Antiviraller için doğru olan?", "Asiklovir ön ilaçtır (prodrug), oral da kullanılır",
          "Yanlışlar: sakinavir RT inhibitörü · valasiklovir aktif · amantadin influenzaya etkisiz · asiklovir yalnız VZV"),
        Q("24-25", 50, "HIV'e etkili ters transkriptaz inhibitörü OLMAYAN?", "İdoksuridin", "Zidovudin, didanozin, zalsitabin, stavudin RT inhibitörü"),
        Q("23-24", 35, "Ön ilaç olmasına rağmen lokal olarak kullanılabilen?", "Asiklovir"),
        Q("22-23", 11, "Türkiye'de COVID-19 tedavisinde yaygın kullanılan?", "Favipiravir"),
        Q("21-22", None, "HBV tedavisinde kullanılmayan ilaç?", "(hatırlanmıyor)",
          "Kullanılanlar: interferon, adefovir, lamivudin, entekavir, telbivudin, tenofovir, emtrisitabin · öğrenci hatırlaması"),
    ],
)

BEKLEYEN["antimalaryal"] = dict(
    baslik="Antimalaryal ve Ektoparaziter İlaçlar", hoca="Doç. Dr. Oruç Yunusoğlu", tarih="22 Ekim",
    sorular=[
        Q("25-26", 37, "Antimalaryal/ektoparaziter ilaçlar için doğru olan?", "Klorokin antimalaryaldir; ayrıca antiinflamatuvar ve antiaritmik etki gösterir",
          "Yanlışlar: klorokin yalnız parenteral, birikmez · permetrin lindandan az etkili ve toksik · klorokin zayıf emilir"),
        Q("23-24", 37, "Antimalaryal olarak kullanılan?", "Kinin", "Tiasetazon, izoniazid, rifampisin, sikloserin antitüberküloz"),
        Q("22-23", 13, "Çinkonizm oluşturabilen?", "Kinin"),
        Q("21-22", None, "Antimalaryal ilaç?", "Klorokin / kinin", "Öğrenci hatırlamasından derlenmiş soru"),
    ],
)

BEKLEYEN["antistafilokoksik"] = dict(
    baslik="Antistafilokoksik ve Dar Spektrumlu Antianaerob İlaçlar", hoca="Doç. Dr. Oruç Yunusoğlu", tarih="22 Ekim",
    sorular=[
        Q("25-26", 16, "Glikopeptit sınıfı, sistemik enfeksiyonlarda parenteral kullanılan?", "Vankomisin", "Basitrasin, polimiksin B, neomisin, fidaksomisin değil"),
        Q("24-25", 51, "Kızarık boyun sendromu oluşturan?", "Vankomisin"),
    ],
)

BEKLEYEN["tuberkuloz"] = dict(
    baslik="Tüberküloz ve Lepra Tedavisinde Kullanılan İlaçlar", hoca="Doç. Dr. Oruç Yunusoğlu", tarih="23 Ekim",
    sorular=[
        Q("25-26", 15, "Antitüberküloz ilaç yan etkisi ve doğru uygulama?", "Streptomisin işitme kaybı yapabilir; kesilip etambutol kullanılabilir",
          "Yanlışlar: rifampisinin turuncu idrarı tedaviyi kestirmez · INH nöropatisinde piridoksin verilir · etambutol hepatotoksik değil"),
        Q("24-25", 46, "Hem kendisi hem pirazinamide dönüşerek etki eden antitüberküloz ilaç?", "Morfozinamid"),
        Q("23-24", 36, "İdrarı kırmızı veya turuncu yapan?", "Rifampisin"),
        Q("22-23", 12, "Optik nörit oluşturabilen?", "Etambutol"),
        Q("21-22", None, "Optik nöropati yapan antitüberküloz ilaç?", "Etambutol", "Öğrenci hatırlamasından derlenmiş soru"),
    ],
)
