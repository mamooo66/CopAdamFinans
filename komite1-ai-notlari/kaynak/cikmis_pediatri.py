# -*- coding: utf-8 -*-
"""Son 5 yılın (2021-22 → 2025-26) Kurul 1 PEDİATRİ çıkmış soruları — ders ders, cevaplı (kitapçıklardan).

Resmi cevap anahtarı yok; cevaplar ders PDF'i gelince o PDF ile doğrulanır. Bir dersin 2026-27 PDF'i gelince
o dersin notları bolumler/cNN_*.py olarak yazılır, soruları oraya taşınır ve anahtar buradan silinir.

Not: 2023-24 kitapçığında 1-3. sorular tek kayıtta (S3) birleşik çıktı; burada 1, 2, 3 numaralı üç ayrı soru olarak
ilgili derslere konuldu.
"""

from yardim import Q

BEKLEYEN = {}

# ---------------------------------------------------------------- giris
BEKLEYEN['giris'] = dict(
    baslik='Pediatriye Giriş ve Öykü',
    hoca='Prof. Dr. Halil İbrahim Atasoy', tarih='21 Eylül',
    sorular=[
        Q("25-26", 3, "Ateş yükselirken ekstremite uçlarının soğuk, bazen benekli mor olmasının nedeni?", "c) Vazokonstriksiyon",
          "Ayar noktası yükselince ısı kaybı azaltılır (deri damarları daralır, titreme) · gövde terlemesi, ateş düşürücü, etkenin yok olması değil"),
        Q("23-24", 2, "Infant döneminde ateşi hangi yöntemle ölçmek daha doğru ve uygundur?", "b) Frontal bölgeden infrared yöntem ile",
          "Kitapçıkta S3 kaydının içinde (2. soru) · cıvalı timpanik, termokromik, ağızdan termistör uygunsuz (cevap belirsiz)"),
        Q("22-23", 7, "Hangi muayene bulgusu çocuğu nöromotor gelişim açısından endişelendirir?", "d) 18 aylıkken anlamlı kelimesi olmayan hasta",
          "Normal: 2 ay Moro · 7 ay destekli oturma · 12 ay elden tutularak yürüme · 24 ay 2 kelimeli cümle"),
        Q("21-22", None, "Pediatride anamnez almanın hedeflerinden biri?", "Ebeveynin üzerinde durduğu konuyu önemsemek",
          "Hatırlanan soru; hatırlama kesin değil, şıklar yok (cevap belirsiz)"),
    ])

# ---------------------------------------------------------------- iskelet
BEKLEYEN['iskelet'] = dict(
    baslik='İskelet Sistemi Muayenesi',
    hoca='Dr. Öğr. Üyesi Emre Çapkınoğlu', tarih='22 Eylül',
    sorular=[
        Q("25-26", 12, "Çocuklarda kas iskelet sistemi muayenesiyle ilgili hangisi YANLIŞTIR?",
          "d) Pes kavus ayak arkı yüksekliğinin azalması, club foot ayak bileği eversiyonudur",
          "Pes kavus: ark yüksekliği ARTAR; club foot (ekinovarus): inversiyon · baş geride kalması hipotoni, Erb, hemihipertrofi, Galeazzi doğru"),
        Q("24-25", 63, "Yenidoğanda dizler farklı yükseklikte, bacak iç yüzü katlantıları asimetrik, tek tarafta abdüksiyon kısıtlı: tanı?",
          "c) Doğuştan kalça çıkıklığı", "Galeazzi, abdüksiyon kısıtlılığı, katlantı asimetrisi · Beckwith-Wiedemann, hemihipertrofi, genu valgum, pes ekinovarus değil"),
        Q("24-25", 64, "Omurga muayenesiyle ilgili I-IV numaralı ifadelerden hangileri doğrudur?", "e) I, II, III, IV",
          "I baş-boyun-sakrum hizası · II skapula çıkıntısı, iliak kret farkı · III öne eğilme (Adams) · IV yandan duruş (kifoz/lordoz) (cevap belirsiz)"),
        Q("23-24", 11, "Spina bifida ile ilgili hangi ifade doğrudur?", "a) Vertebral arkusların birleşmeyerek açık kalmasıdır",
          "b) blok vertebra · c) skolyoz · d) torakal kifoz · e) lomber lordoz artışı tanımlarıdır"),
        Q("22-23", 2, "Adölesanda (özellikle kızda) skolyoz muayenesinde hangi yöntem/bulgu uygulanır?", "e) Hepsi",
          "Omuz yüksekliği farkı, pelvik eğim, gövdenin yana kayması ve Adams testi birlikte değerlendirilir"),
        Q("21-22", None, "Skolyoz testi?", "Adams (öne eğilme) testi", "Hatırlanan soru"),
    ])

# ---------------------------------------------------------------- solunum
BEKLEYEN['solunum'] = dict(
    baslik='Solunum Sistemi Muayenesi',
    hoca='Prof. Dr. Mervan Bekdaş', tarih='23 Eylül',
    sorular=[
        Q("24-25", 59, "Hangisinde çomak parmak görülmez?", "d) Astım",
          "Çomak parmak: siyanotik kalp hastalığı, akciğer kanseri, akciğer apsesi, enfektif endokardit"),
        Q("24-25", 60, "Solunum sistemi belirti ve bulgularıyla ilgili hangisi doğrudur?",
          "c) Yenidoğanda asimetrik göğüs ekspansiyonu diyafragma hernisinin işareti olabilir",
          "Takipne eşiği yaşa göre değişir · apne 5 sn değil (≥20 sn) · pektus ekskavatum sendromlara eşlik edebilir · oskültasyon tek başına yetmez"),
    ])

# ---------------------------------------------------------------- urogenital
BEKLEYEN['urogenital'] = dict(
    baslik='Ürogenital Sistem Muayenesi',
    hoca='Prof. Dr. Aslı Çelebi Tayfur', tarih='28 Eylül',
    sorular=[
        Q("25-26", 7, "Erkek çocuklarda kriptorşidizm (inmemiş testis) ile ilgili hangisi doğrudur?", "c) Tek veya iki taraflı saptanabilir",
          "Prepisyumun geri çekilememesi fimozistir · yalnız travmaya bağlı değil · üretra kapanması değil · hipospadiasla birlikte seyretmesi genel değil"),
        Q("24-25", 67, "Çocuklarda fimozis tanımı?", "b) Prepisyumun, glans penis tepesine uyan açıklığın darlığı nedeniyle çekilememesi",
          "Hipospadias (a, e), hidrosel (c), meatal stenoz (d) tanımları çeldirici"),
        Q("24-25", 68, "Çocuklarda epispadias tanımı?", "e) Üretra dış measının (kız/erkek) pubik kemiğe olması gerekenden daha yakın üst kısma açılması",
          "Testis torsiyonu (a) · varikosel (b) · hidrosel (c) · kriptorşidizm (d)"),
        Q("23-24", 9, "Çocuklarda fimozis tanımı için hangisi uygundur?", "c) Prepisyumun, glans penis tepesine uyan açıklığın darlığı nedeniyle geriye çekilememesi",
          "Epispadias (a), meatal darlık (b), hipospadias (d), hidrosel (e) tanımları çeldirici"),
        Q("23-24", 10, "Çocuklarda epispadias tanımı için hangisi uygundur?", "a) Üretra dış measının (kız/erkek) pubik kemiğe olması gerekenden daha yakın üst kısma açılması",
          "Hipospadias (b) · hidrosel (c) · varikosel (d) · meatal darlık (e)"),
        Q("22-23", 4, "Çocuklarda fimozis tanımı için hangisi uygundur?", "b) Prepisyumun, glans penis tepesine uyan açıklığın darlığı nedeniyle geriye çekilememesi",
          "Epispadias (a), meatal darlık (c), hidrosel (d), hipospadias (e) tanımları çeldirici"),
    ])

# ---------------------------------------------------------------- dolasim
BEKLEYEN['dolasim'] = dict(
    baslik='Dolaşım Sistemi Muayenesi',
    hoca='Prof. Dr. Halil İbrahim Atasoy', tarih='29 Eylül',
    sorular=[
        Q("25-26", 1, "Dolaşım muayenesinde oskültasyon sırasında hastaya genellikle verilebilecek pozisyon?", "c) Oturur haldeki pozisyon",
          "Sol yan yatış (b) mitral için özel pozisyon; yüz üstü, baş aşağı pozisyonlar uygunsuz (cevap belirsiz)"),
        Q("24-25", 57, "Palpasyonda suprasternal çentikte tril hissedilmesi hangi patolojiye işaret eder?", "a) Pulmoner darlık",
          "Suprasternal tril: aort/pulmoner darlık, PDA, koarktasyon · triküspit yetmezliği, aort yetmezliği, mitral darlık, VSD değil"),
        Q("23-24", 1, "Oskültasyonda hastayı oturur ve öne eğilir halde dinlemek hangi üfürümü daha iyi duyurur?", "c) Aort yetmezliği",
          "Mitral darlığı sol yan yatışta dinlenir · kitapçıkta S3 kaydının içinde (1. soru)"),
        Q("22-23", 1, "Çocuklarda perküsyon tekniği neden tercih edilmez?", "b) Bebeklerin prekordiyal bölgesi küçük olduğundan",
          "Korku, aile tepkisi, zaman kısıtı, fibrilasyon riski gerekçe değildir"),
        Q("21-22", None, "Kalp yetmezliği olan çocukta hangi muayene adımı yapılmaz?", "Perküsyon", "Hatırlanan soru"),
    ])

# ---------------------------------------------------------------- gis
BEKLEYEN['gis'] = dict(
    baslik='Gastrointestinal Sistem Muayenesi',
    hoca='Doç. Dr. Meyri Arzu Yoldaş', tarih='30 Eylül',
    sorular=[
        Q("25-26", 11, "Sağ alt kadranda palpasyonda ağrı, rebound ve defans hangisinin lehinedir?", "a) Akut apandisit",
          "Kolesistit, pankreatit, perforasyon, irritabl barsak sendromu değil"),
        Q("24-25", 65, "Çocuklarda GİS muayenesinin doğru sıralaması?", "d) 4,3,1,2 (inspeksiyon, oskültasyon, palpasyon, perküsyon)",
          "Oskültasyon palpasyon ve perküsyondan önce yapılır (barsak sesleri bozulmasın)"),
        Q("24-25", 66, "GİS muayenesi ile ilgili hangisi doğrudur?", "c) Pilor stenozunda beslenme sonrası mide lojunda peristaltik dalgalar görülebilir",
          "Peritonitte hasta hareketsiz · barsak sesleri periton irritasyonu/hipopotasemide AZALIR · palpasyona ağrısız bölgeden başlanır"),
        Q("23-24", 4, "Çocuklarda GİS muayenesiyle ilgili hangisi doğrudur?", "e) Batın muayenesine inspeksiyonla başlanır, oskültasyonla devam edilir",
          "Perküsyon/palpasyonla başlanmaz · palpasyona ağrılı bölgeden değil, ağrısız bölgeden başlanır"),
        Q("23-24", 5, "Traube aralığında matite alınan çocukta hangisi öncelikle DÜŞÜNÜLMEMELİDİR?", "a) Sol akciğerde pnömotoraks",
          "Pnömotoraks hiperrezonans verir · matite: splenomegali, dolu mide, sol plevral sıvı, perikardit"),
    ])

# ---------------------------------------------------------------- yd_ozellik
BEKLEYEN['yd_ozellik'] = dict(
    baslik='Yenidoğanın Özellikleri',
    hoca='Prof. Dr. Mustafa Dilek', tarih='8 Ekim',
    sorular=[
        Q("21-22", None, "Hangisi yanlıştır? (yenidoğan dolaşımı)", "Doğumdan sonra duktus arteriozus açık kalır",
          "Hatırlanan soru; duktus arteriozus doğumdan sonra fizyolojik olarak kapanır"),
    ])

# ---------------------------------------------------------------- tuberkuloz
BEKLEYEN['tuberkuloz'] = dict(
    baslik='Çocuklarda Tüberküloz',
    hoca='Prof. Dr. Halil İbrahim Atasoy', tarih='12 Ekim',
    sorular=[
        Q("25-26", 2, "Ehrlich-Ziehl-Neelsen boyası için tüberküloz tanısında genellikle kullanılan örnek?", "d) Açlık mide suyu örneği",
          "Çocuk balgam çıkaramaz, yutulan balgam mide suyunda aranır · boğaz sürüntüsü, kan, idrar, doku değil"),
        Q("24-25", 58, "DSÖ önerilerine göre OLASI (probable) tüberküloz için hangi bulgu doğru kabul edilir?", "b) Akciğer grafisi bulguları saptanır",
          "Basilin gösterilmesi (e) kesin TB'dir · PPD <10-15 mm, biyopsi bulgusu yok, tedaviye yanıt yok olası TB'yi desteklemez"),
        Q("23-24", 3, "Plevral effüzyonda TB basilinin dolaylı gösterilmesi, yaygın ulaşılırlık açısından hangi yöntemle yapılır?", "c) Biyokimyasal yöntem",
          "ADA (adenozin deaminaz) ölçümü · kitapçıkta S3 kaydının içinde (3. soru)"),
        Q("22-23", 3, "BACTEC sistemi (2 haftada basil gösterir) hangi yönteme uyar?", "a) Radyometrik yöntem",
          "Luminometrik, biyokimyasal, kültür, immünometrik yöntemler farklı"),
        Q("21-22", None, "4 yaşında, TB hastasıyla temas eden çocukta tedavi?", "6-12 ay izoniazid", "Hatırlanan soru (koruyucu tedavi)"),
    ])

# ---------------------------------------------------------------- sepsis
BEKLEYEN['sepsis'] = dict(
    baslik='Çocuklarda Sepsis ve Septik Şok',
    hoca='Prof. Dr. Mervan Bekdaş', tarih='14 Ekim',
    sorular=[
        Q("25-26", 8, "1 yaşında ateşli bebekte (TA 60/40, nabız 160, laktat 5.2) hipotansiyonun temel nedeni?", "b) Artmış kapiller geçirgenlik ve vazodilatasyon",
          "Sepsiste distributif/sıcak şok · kontraktilite artışı, renal vazokonstriksiyon, periferik vazokonstriksiyon, pulmoner emboli değil"),
        Q("22-23", 5, "Hangisi sistemik inflamatuvar yanıt sendromu (SIRS) bileşeni DEĞİLDİR?", "c) Bradipne",
          "SIRS: ateş/hipotermi, taşikardi, takipne, lökosit değişikliği, immatür nötrofil >%10 · bradikardi yalnız <1 yaşta ölçüt (b de olabilir; cevap belirsiz)"),
    ])

# ---------------------------------------------------------------- usye
BEKLEYEN['usye'] = dict(
    baslik='Üst Solunum Yolu İnfeksiyonları ve Krup',
    hoca='Doç. Dr. Meyri Arzu Yoldaş', tarih='19 Ekim',
    sorular=[
        Q("25-26", 10, "Ani nefes darlığı, ses kısıklığı, havlar öksürük; boyun grafisinde “kalem ucu” görünümü en çok hangi hastalıkta görülür?", "b) Akut larenjit (krup)",
          "Epiglottitte başparmak belirtisi · bronşiolit, peritonsiller apse değil · laringotrakeit de krup spektrumu, kitapçık adlandırması “akut larenjit (krup)”"),
        Q("24-25", 61, "A grubu beta hemolitik streptokok tonsillofarenjitinin nonsüpüratif komplikasyonu?", "e) Akut romatizmal ateş",
          "Erizipel, sinüzit, peritonsiller abse, septik artrit süpüratif/lokal komplikasyonlar · diğer nonsüpüratif: post-streptokoksik GN"),
        Q("24-25", 62, "3 yaşında ateş, havlar öksürük, ses kısıklığı, stridor; grafide farinkste “kalem ucu”: en olası tanı?", "e) Krup (akut larenjit)",
          "Epiglottit, peritonsiller abse, tonsillofarenjit, yabancı cisim aspirasyonu değil"),
        Q("23-24", 12, "Çocuklarda akut epiglotitin en sık nedeni?", "c) H. influenzae tip B", "S. pneumoniae, rinovirüs, N. meningitidis, parainfluenza değil"),
        Q("21-22", None, "Akut otitis mediada en sık etken?", "Streptococcus pneumoniae", "Hatırlanan soru"),
    ])

# ---------------------------------------------------------------- intrauterin
BEKLEYEN['intrauterin'] = dict(
    baslik='İntrauterin Enfeksiyonlar',
    hoca='Prof. Dr. Mustafa Dilek', tarih='19 Ekim',
    sorular=[
        Q("22-23", 10, "İntrauterin geçirildiğinde sikatrisyel deri lezyonu, katarakt-koryoretinit, mikrosefali, ekstremite hipoplazisi yapan etken?", "d) Varisella zoster",
          "Konjenital varisella sendromu · rubella katarakt, sağırlık, PDA; CMV periventriküler kalsifikasyon; toksoplazma hidrosefali"),
        Q("21-22", None, "Koryoretinit, hidrosefali, serebral kalsifikasyonla gelen yenidoğan?", "Konjenital toksoplazmoz", "Hatırlanan soru"),
    ])

# ---------------------------------------------------------------- bogmaca_tetanoz
BEKLEYEN['bogmaca_tetanoz'] = dict(
    baslik='Boğmaca ve Tetanoz',
    hoca='Prof. Dr. Mervan Bekdaş', tarih='20 Ekim',
    sorular=[
        Q("25-26", 9, "Boğmaca ile ilgili hangisi YANLIŞTIR?", "e) Bordet-Gengou ekimi altın standarttır ve antibiyotik başladıktan sonra da yüksek oranda pozitif kalır",
          "Antibiyotikle kültür hızla negatifleşir · doğru: bağışıklık ömür boyu değil, en bulaştırıcı dönem kataral dönem, <3 ayda apne, trakeal sitotoksin"),
        Q("23-24", 6, "2 yaşında, 2 haftadır geceleri kentöz öksürük, morarma, öksürük sonrası kusma, ateşsiz: tanı? (olgu S6-8)", "c) Boğmaca",
          "Ateş ve ishal yok, postnazal akıntı ve patolojik solunum sesi yok · tüberküloz, difteri, nazofarenjit, emboli değil"),
        Q("23-24", 7, "Bu tablonun (boğmaca) patogenezinde rol alan toksinlerden hangisi DEĞİLDİR? (olgu S6-8)", "c) Nöraminidaz",
          "Boğmaca toksinleri: pertussis toksin, adenilat siklaz toksini, trakeal sitotoksin, dermonekrotik toksin"),
        Q("23-24", 8, "Bu tabloda (boğmaca) beklenen laboratuvar bulgusu? (olgu S6-8)", "a) Lenfositoz", "Lökositozla birlikte lenfositoz; nötropeni, eozinofili, bazofili, anemi beklenmez"),
        Q("22-23", 8, "Hangisi boğmaca tanısında kullanılan bulgulardan biri DEĞİLDİR?", "b) Yüksek eritrosit sedimentasyon hızı",
          "Tipik öksürük nöbetleri, lenfosit artışı, Bordet-Gengou'da üreme, anti-pertussis IgG artışı tanıda kullanılır"),
    ])

# ---------------------------------------------------------------- kabakulak_difteri
BEKLEYEN['kabakulak_difteri'] = dict(
    baslik='Kabakulak ve Difteri',
    hoca='Prof. Dr. Mervan Bekdaş', tarih='20 Ekim',
    sorular=[
        Q("22-23", 6, "Kabakulak enfeksiyonu için hangisi doğrudur?", "e) Hiçbiri",
          "Yalnız çocuk, yalnız parotis, yalnız kanda virüs, yalnız tek taraf ifadeleri yanlış: erişkini, diğer bezleri, orşiti, menenjiti etkiler"),
        Q("21-22", None, "Toksini var, psödomembran yapar, damlacıkla bulaşır: hangisi?", "Difteri", "Hatırlanan soru"),
    ])

# ---------------------------------------------------------------- dokuntulu
BEKLEYEN['dokuntulu'] = dict(
    baslik='Döküntülü Hastalıklar',
    hoca='Prof. Dr. Mustafa Dilek', tarih='21 Ekim',
    sorular=[
        Q("25-26", 4, "1 yaşında 3 gün 40°C ateş, ateş düşünce gövdede makülopapüler döküntü, genel durum iyi: tanı?", "c) Roseola infantum (6. hastalık)",
          "Kızamık, eritema infeksiyozum (5.), kızıl, kızamıkçık değil · önce yüksek ateş, ateş düşünce döküntü"),
        Q("25-26", 5, "4 yaşında 6 gün antibiyotiğe yanıtsız ateş, nonpürülan konjonktivit, çilek dil, el-ayak ödemi: kritik uzun vadeli komplikasyon?", "e) Koroner arter anevrizmaları",
          "Kawasaki hastalığı · post-streptokoksik GN, SSPE, akut romatizmal ateş, Stevens-Johnson değil"),
        Q("22-23", 9, "Tokatlanmış yüz görünümü ve 5. hastalığın etkeni?", "b) Parvovirus (B19)",
          "HSV, varisella zoster, HHV-6 (roseola), CMV değil"),
        Q("21-22", None, "Çilek dil hangi hastalıkta görülür?", "Kızıl", "Hatırlanan soru"),
        Q("21-22", None, "Ellerde ve ayaklarda veziküler döküntü yapan hastalık için hangisi doğrudur?", "En sık yaz aylarında görülür",
          "Hatırlanan soru: el-ayak-ağız hastalığı (Coxsackie) · yanlış şık: en çok yetişkinlerde (aslında çocuklarda)"),
    ])

# ---------------------------------------------------------------- programda_yok
BEKLEYEN['programda_yok'] = dict(
    baslik='Bu yılın programında karşılığı olmayan konu',
    hoca='—', tarih='—',
    sorular=[
        Q("25-26", 6, "Hücresel immün yanıtta CD8+ T lenfositlerin (sitotoksik T) temel görevi?", "d) Virüsle enfekte veya tümörleşmiş hücreleri doğrudan öldürmek",
          "Fagositoz makrofaj; hızlı doğal yanıt NK/nötrofil; plazma hücresi/antikor B lenfosit; B aktivasyonu CD4+ T yardımcı"),
    ])
