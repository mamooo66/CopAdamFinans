# -*- coding: utf-8 -*-
"""Son 5 yılın (2021-22 → 2025-26) Kurul 1 PATOLOJİ çıkmış soruları — konu konu, cevaplı.

Yalnızca çıkmış soru kitapçıklarından derlendi. Bu konuların hap bilgi slaytları HENÜZ YOK:
ilgili dersin 2026-27 PDF'i Drive'da okunabilir olunca o PDF'ten yazılıp desteye eklenecek
(icerik.py · BOLUMLER). Desteye girmeden önce her sorunun cevabı/notu o PDF ile karşılaştırılmalı.

Q(yıl, soru_no, kök, cevap, not, n=kaç soruyu temsil ettiği, ref=sayıma girmeyen çapraz atıf)
"""

from icerik import Q

BEKLEYEN = {}

# ---------------------------------------------------------------- hasar
BEKLEYEN['hasar'] = dict(
    baslik='Hücre Hasarı ve Hücre Ölümü',
    hoca='Doç. Dr. Selma Erdoğan Düzcü', tarih='21 Eylül',
    sorular=[
        Q('25-26', 67, 'Hücre hasarıyla ilgili doğru olan?', 'Böbrekte kan akımının ani kesilmesi → koagülasyon nekrozu', 'Çeldiriciler: ATP↑/Ca↓ · apoptoz reversibl · apoptoz yalnız patolojik · nekrozda membran intakt'),
        Q('24-25', 69, 'Hücre hasarlanma mekanizmalarıyla ilgili doğru olan?', 'Mitokondri hasarıyla reaktif oksijen türevleri artar', 'Çeldiriciler: kişiler arası farklılık yok · ilk makroskopik değişiklik · glikojen artar · hücre içi Ca azalır'),
        Q('23-24', 61, 'Hücre hasarı mekanizmalarıyla ilgili doğru olan?', 'Apoptozda hücre membranı intakt kalır ve iltihabi reaksiyon gelişmez', 'Çeldiriciler: yalnızca enfeksiyon · şişme/yağlı değişiklik irreversibl · nekroz programlı · böbrekte likefaksiyon'),
        Q('22-23', 60, 'Nekroz ve apoptozla ilgili doğru olan?', 'Nekrozda hücre membran bütünlüğü bozulmuştur', 'Çeldiriciler: nekroz fizyolojik olabilir · apoptozda membran bozuk · apoptozda yoğun inflamasyon · apoptozda enzimler dışarı çıkar'),
        Q('21-22', None, 'Nekroz–apoptoz karşılaştırması (nükleer değişiklikler)', 'Piknoz → karyoreksis → karyolizis (nekroz)', 'Öğrenci hatırlamasından derlenmiş soru'),
    ],
)

# ---------------------------------------------------------------- adaptasyon
BEKLEYEN['adaptasyon'] = dict(
    baslik='Hücresel Adaptasyon ve Hücre İçi Birikimler',
    hoca='Dr. Öğr. Üyesi Nur Tunç Karabekiroğlu', tarih='22 Eylül',
    sorular=[
        Q('25-26', 61, "GÖRH'de alt özofagustaki çok katlı yassı epitelin intestinal tip kolumnar epitele dönüşmesi?", 'Metaplazi', 'Barrett özofagus'),
        Q('24-25', 70, 'Hangi adaptasyon prekanseröz bir durumdur?', 'Yüksek östrojen düzeyine bağlı endometrium hiperplazisi', 'Çeldiriciler: gebe uterus hipertrofisi · hepatektomi sonrası hiperplazi · sporcu kas hipertrofisi · pubertede timus atrofisi'),
        Q('23-24', 62, 'Hangisi prekanseröz DEĞİLDİR?', 'Hipertansiyon sonucu gelişen kalp hipertrofisi', 'Prekanserözler: endometrial hiperplazi · kronik gastritte intestinal metaplazi · sigarada larinks yassı metaplazisi · Barrett'),
        Q('22-23', 61, 'Hipertansiyonda artan iş yükünü karşılamak için kalp kasındaki adaptasyon?', 'Hipertrofi'),
    ],
)

# ---------------------------------------------------------------- akut
BEKLEYEN['akut'] = dict(
    baslik='İnflamasyon: Tanım, Patogenez ve Akut İnflamasyon',
    hoca='Doç. Dr. Selma Erdoğan Düzcü', tarih='22-23 Eylül',
    sorular=[
        Q('25-26', 68, 'Akut inflamasyonda ROS, nitrik oksit ve granül enzimleri hangi hücresel olayda etkin?', 'Mikroorganizmaların hücre içinde yok edilmesi', 'Adezyon (integrin), marjinasyon, kemotaksis, yuvarlanma (selektin) değil'),
        Q('25-26', 69, 'Akut ve kronik inflamasyon reaksiyonlarıyla ilgili doğru olan?', 'IL-1 ve TNF sistemik akut faz reaksiyonlarını uyarır', 'Çeldiriciler: granülomatöz akut patern · histamin plazma kökenli/vazokonstriktör · TXA₂ vazodilatatör · süpüratif kronik'),
        Q('24-25', 71, 'Akut inflamasyonun hücresel olaylarıyla ilgili doğru olan?', 'Gevşek adezyon ve yuvarlanma selektin ailesi tarafından gerçekleştirilir', 'Çeldiriciler: ilk olay fagositoz · marjinasyonda santrale · CD31 kemotaksis · ROS damar dışına çıkış'),
        Q('23-24', 63, 'Akut faz reaksiyonlarını uyaran en önemli iki sitokin?', 'TNF-α ve IL-1', 'Histamin-serotonin, NO-ROS, C3-C5, fibrinojen-plazmin değil'),
        Q('22-23', 62, "DAMP'ları tanıyan sitozolik reseptör?", 'İnflammazom', 'TLR, integrin, marjinasyon, bradikinin değil'),
        Q('22-23', 63, 'Akut inflamasyonun morfolojik paternleri arasında yer ALMAYAN?', 'Granülomatöz inflamasyon', 'Ülserasyon, pürülan, seröz, fibrinöz = akut'),
        Q('21-22', None, 'TLR reseptörleri inflamasyonun hangi aşamasında kullanılır?', 'Yabancı maddelerin (mikropların) tanınması', 'Öğrenci hatırlamasından derlenmiş soru'),
    ],
)

# ---------------------------------------------------------------- kronik
BEKLEYEN['kronik'] = dict(
    baslik='Kronik İnflamasyon',
    hoca='Doç. Dr. Selma Erdoğan Düzcü', tarih='24 Eylül',
    sorular=[
        Q('25-26', 78, 'Akciğerde kazeifikasyon nekrozlu TB granülomundaki multinükleer dev hücreler hangi hücrelerden oluşur?', 'Epiteloid histiositler', 'Lenfosit, mast hücresi, fibroblast, atipik tümör hücresi değil'),
        Q('24-25', 72, 'Hangi hastalıktaki morfolojik patern kronik inflamasyona örnektir?', 'Tüberkülozda görülen granülomatöz inflamasyon', 'Seröz (yanık), süpüratif (stafilokok), abse, akut peptik ülser = akut'),
        Q('23-24', 64, 'Kronik nonspesifik kolit biyopsisinde lamina propriada hangi hücre GÖRÜLMEZ?', 'Nötrofil', 'Eozinofil, lenfosit, makrofaj, plazma hücresi görülür'),
        Q('22-23', 74, 'Pilonidal sinüste kıl kesitlerini çevreleyen multinükleer hücrelerin kökeni?', 'Makrofaj', 'Yabancı cisim tipi dev hücre'),
    ],
)

# ---------------------------------------------------------------- iyilesme
BEKLEYEN['iyilesme'] = dict(
    baslik='İyileşme ve Tamir, Onarım Kusurları',
    hoca='Doç. Dr. Selma Erdoğan Düzcü', tarih='29 Eylül',
    sorular=[
        Q('25-26', 70, 'Yara iyileşmesinde 3-5. günde yara kabuğu altında yumuşak, pembe, granüler; mikroskopide fibroblast + iltihap hücresi + gevşek ECM?', 'Granülasyon dokusu', 'Rejenerasyon, anjiogenez, nedbe, fibroplazi değil'),
        Q('24-25', 73, 'Deri yaralarının iyileşmesiyle ilgili doğru olan?', 'Yara büzüşmesi (kontraksiyon) sekonder yara iyileşmesinde görülür', "Çeldiriciler: granülasyonsuz skar · primer'de daha fazla skar · primer'de yoğun iltihap · ilk aşamada akut iltihap yok"),
        Q('23-24', 65, "G0'da olup hücre kaybında G1'e geçen düşük çoğalma kapasiteli stabil hücre?", 'Karaciğer parankim hücresi', 'Ağız yassı epiteli, ürotelyum, lenfoid hücre = labil · kalp kası = permanent'),
        Q('22-23', 64, 'Yara iyileşme süreçleriyle ilgili doğru OLMAYAN?', '“Yara iyileşmesi sırasında önce fibrozis gelişir sonra granülasyon dokusu oluşur”', 'Doğrular: anjiogenez · VEGF ve FGF-2 · fibroblast göçü · ECM rolü'),
        Q('21-22', None, 'İyileşme evreleri sorusu', 'Granülasyon dokusu', 'Öğrenci hatırlamasından derlenmiş soru'),
    ],
)

# ---------------------------------------------------------------- odem
BEKLEYEN['odem'] = dict(
    baslik='Ödem, Hiperemi, Konjesyon ve Kanama',
    hoca='Doç. Dr. Selma Erdoğan Düzcü', tarih='25 Eylül',
    sorular=[
        Q('23-24', 66, 'Ödem oluşumunda hidrostatik basınç artışının ön planda olduğu durum?', 'Konjestif kalp yetmezliği', 'Nefrotik sendrom, malnütrisyon, protein kaybettiren enteropati = onkotik ↓ · lenfatik tıkanıklık = lenfödem'),
        Q('22-23', 65, 'Ödem morfolojisiyle ilgili doğru olan?', 'Ödem azalmış ozmotik basınçta ya da artmış hidrostatik basınçta gelişebilir', 'Çeldiriciler: koldan değerlendirilir · lenfatik obstrüksiyon ödem yapmaz · albümin artışı ödem yapar · transüda proteinden zengin'),
        Q('25-26', 71, '(Hemodinamik soru — tanım çeldiricileri, bkz. Bölüm 8)', 'Doğru: DIC tanımı', 'Hemoraji ≠ arteriol dilatasyonu (hiperemi) · Ekimoz ≠ noktasal kanama (peteşi)', ref=True),
    ],
)

# ---------------------------------------------------------------- tromboz
BEKLEYEN['tromboz'] = dict(
    baslik='Trombüs, Emboli, İnfarktüs ve Şok',
    hoca='Doç. Dr. Selma Erdoğan Düzcü', tarih='28 Eylül',
    sorular=[
        Q('25-26', 71, 'Hemodinamik bozukluklarla ilgili doğru olan?', 'DIC: mikrosirkülasyonda yaygın trombüsler ve kanamalarla giden tüketim koagülopatisi', 'Çeldiriciler: hemoraji = arteriol dilatasyonu (hiperemi) · Zahn = tromboze vende çizgilenme · ekimoz = noktasal kanama (peteşi) · infarktüs = taşınan kitle (emboli)'),
        Q('24-25', 74, 'Hangi organda soluk (beyaz) infarkt görülür?', 'Böbrek', 'Akciğer, over, testis, barsak → kırmızı infarkt'),
        Q('24-25', 75, 'Hemostazda salınımı pıhtılaşma zincirini bloke ederek antitrombotik etki gösteren?', 'Trombomodulin', 'vWF, ADP, TXA₂, fibrin = protrombotik'),
        Q('22-23', 66, 'Primer hemostazda trombosit adezyonunda GpIb ile kollajen arasında köprü?', 'von Willebrand faktör (vWF)', 'Trombin, ADP, TXA₂, pıhtılaşma zinciri değil'),
    ],
)

# ---------------------------------------------------------------- amiloid
BEKLEYEN['amiloid'] = dict(
    baslik='Amiloidoz',
    hoca='Doç. Dr. Selma Erdoğan Düzcü', tarih='25 Eylül',
    sorular=[
        Q('25-26', 72, 'FMF tanılı hastada barsak perforasyonu; vasküler ve subserozal eozinofilik materyal; Kongo red ve kristal viyole pozitif?', 'Amiloidoz (AA tipi)', 'Paradoks emboli, amniyon sıvısı embolisi, mikotik anevrizma, hidroperitoneum değil'),
        Q('24-25', 76, 'Amiloidozla ilgili doğru OLMAYAN?', '“AA, AL, ATTR amiloid tipleri H&E boyamada tespit edilir”', "Doğrular: Kongo red ile polarize ışıkta çift kırma · ekstrasellüler birikim · rektal biyopsi · MM'de AL"),
        Q('23-24', 67, 'Rektum biyopsisinde amiloid: ışık mikroskobunda pembe-kırmızı, polarize ışıkta elma yeşili veren boya?', 'Kongo red', 'Giemsa, kristal viyole, H&E, Alcian blue değil'),
        Q('22-23', 67, 'Amiloidi gösteren, polarize ışıkta elma yeşili çift kırma gösteren boya?', 'Kongo red', 'CD3, CD20 (IHK), kristal viyole, Giemsa değil'),
        Q('21-22', None, 'Amiloid birikimi hangi boyayla görüntülenir?', 'Kongo red (kristal viyole)', 'Öğrenci hatırlamasından derlenmiş soru'),
    ],
)

# ---------------------------------------------------------------- cevre
BEKLEYEN['cevre'] = dict(
    baslik='Çevresel Patojenler ve Hastalıklar (Beslenme Dahil)',
    hoca='Doç. Dr. Selma Erdoğan Düzcü', tarih='1 Ekim',
    sorular=[
        Q('25-26', 73, 'Endokrin bozukluk, amenore, konstipasyon; şiddetli PEM benzeri bulgular; kişinin isteyerek kendini aç bırakması?', 'Anoreksiya nervoza', 'Kwashiorkor, bulimia, marasmus, kaşeksi değil'),
        Q('24-25', 77, 'Larinks kanseri ve mezotelyomanın etyopatogenezinde rol alan endüstriyel ajan?', 'Asbest', 'Bisfenol A, vinil klorür, polisiklik hidrokarbon, organoklorin değil'),
        Q('23-24', 68, 'Sigarayla ilişkili hastalıkların mekanizmalarıyla ilgili doğru OLMAYAN?', '“Mukozada direkt etki ile mukus üretimini azaltır” (aslında ARTIRIR)', 'Doğrular: erken doğum riski ↑ · akciğer ca ↑ · myokard oksijenlenmesi ↓ · trombosit agregasyonu ↑'),
        Q('22-23', 68, 'Uzun süreli maruziyeti akciğer karsinomu ve mezotelyomaya neden olan?', 'Asbest', 'Benzen, vinil klorür, bisfenol A, DDT değil'),
    ],
)

# ---------------------------------------------------------------- isim
BEKLEYEN['isim'] = dict(
    baslik='Neoplazi: Tanım, İsimlendirme ve Benign–Malign Ayrımı',
    hoca='Prof. Dr. Çetin Boran', tarih='5 Ekim',
    sorular=[
        Q('23-24', 80, 'Hangisi malign bir tümördür?', 'Seminoma', 'Meningioma, fibroma, pleomorfik adenom, rabdomyoma benign'),
        Q('25-26', 80, '(Büyüme biyolojisi sorusunun doğru seçenekleri)', '“Seminoma malign bir tümördür” ✔ · “Anaplazi diferansiasyonun ileri derecede kaybıdır” ✔', "Sorunun yanlış ifadesi Bölüm 13'te", ref=True),
        Q('21-22', None, 'Üç germ tabakasında da değişiklik gösteren tümör? · Hangisi malign tümördür?', 'Teratom · Asiner karsinom', 'Öğrenci hatırlamasından derlenmiş sorular', n=2),
    ],
)

# ---------------------------------------------------------------- molekuler
BEKLEYEN['molekuler'] = dict(
    baslik='Neoplazinin Moleküler Temeli',
    hoca='Prof. Dr. Çetin Boran', tarih='5 ve 7 Ekim',
    sorular=[
        Q('25-26', 79, '“Gerektiğinde hücre siklusunu durdurur, gerekirse hücreyi apoptoza yönlendirir.”', 'p53', 'bcl-2, ras, raf, msh2 değil'),
        Q('24-25', 83, '“Hücre zarı iç yüzeyine yerleşmiştir; reseptörden aldığı büyüme sinyalini çekirdeğe taşır.”', 'RAS', 'NF-1, PTEN, p53, p16 değil'),
        Q('24-25', 84, '“İnaktive olduğunda E2F serbest kalır ve hücre siklusu ilerler.”', 'RB', 'Myc, BRCA1, MSH2, VHL değil'),
        Q('23-24', 76, 'Bloke edici monoklonal antikorla tedavi seçeneği düşünülemeyecek gen?', 'p16', 'RAS, ERBB2, c-KIT, TGF-α hedeflenebilir'),
        Q('23-24', 77, 'Hücre sinyal iletim yollarında inhibitör olarak yer alan?', 'NF1', 'p21 (CDKI), myc (TF onkogen), msh2 (tamir), ATM (hasar sensörü) değil'),
        Q('22-23', 75, "Knudson'un çift vuruş hipotezinin geçerli olduğu gen?", 'APC', 'EGFR, RAS, MYC, siklin D (onkogen) değil'),
        Q('22-23', 76, 'DNA tamir genlerinden biri?', 'MSH2', 'Bcl-2, NF-1, RB, E-kaderin değil'),
        Q('22-23', 78, 'Yanlış olan?', '“E2F, RB ile kompleks hâlde bulunan süpresör bir gendir” (E2F transkripsiyon faktörü)', 'Doğrular: replikatif havuz genişse tümör hızlı küçülür · protoonkogende tek allel yeter · tümör progresyonu tanımı · onkofetal antijenler'),
        Q('21-22', None, 'RB mutasyonu sonucu gelişen tümör · Cevabı BRCA olan soru', 'RB → retinoblastom/osteosarkom · BRCA → ailesel meme-over ca', 'Öğrenci hatırlamasından derlenmiş sorular', n=2),
    ],
)

# ---------------------------------------------------------------- buyume
BEKLEYEN['buyume'] = dict(
    baslik='Tümör Büyümesinin Biyolojisi, Anjiogenez, İnvazyon ve Metastaz',
    hoca='Prof. Dr. Çetin Boran', tarih='15 Ekim',
    sorular=[
        Q('25-26', 80, 'Hangisi doğru DEĞİLDİR?', '“Düşük büyüme fraksiyonuna sahip tümörler antineoplastik ilaç tedavisine daha iyi yanıt verir”', 'Doğrular: apoptoz tümör gelişimini önler · seminoma malign · RB kilit süpresör · anaplazi tanımı'),
        Q('24-25', 87, 'Anti-VEGF monoklonal antikor verilen hastada tümör büyümesi durdu; en olası neden?', 'Yeni damar oluşumu durmuştur', 'Mutasyon olmaması, karsinojen yokluğu, EGFR aktivasyonu, DNA tamir mutasyonu değil'),
        Q('22-23', 78, '(Doğru seçenek olarak)', '“Replikatif havuz ne kadar genişse kemoterapötiklerle tümör o kadar hızlı küçülür” ✔', 'Bkz. Bölüm 12 – sorunun yanlış ifadesi E2F', ref=True),
        Q('21-22', None, 'Hipoksi durumunda uyarılan?', 'HIF-1α', 'Öğrenci hatırlamasından derlenmiş soru'),
    ],
)

# ---------------------------------------------------------------- karsinojen
BEKLEYEN['karsinojen'] = dict(
    baslik='Karsinojen Ajanlar',
    hoca='Prof. Dr. Çetin Boran', tarih='9 Ekim',
    sorular=[
        Q('25-26', 76, 'Burkitt lenfoma ve nazofaringeal karsinomun etyopatogenezinde önemli rol oynayan?', 'Epstein-Barr virüsü', 'HPV, HBV, şistozomiyazis, H. pylori değil'),
        Q('25-26', 81, 'Promoter etkisi olan karsinojen?', 'Dietilstilbestrol', 'UV, kemoterapötikler, PAH, azo boyaları = başlatıcı'),
        Q('24-25', 78, 'Burkitt lenfoma gelişiminde rolü olan enfeksiyon?', 'Epstein-Barr virüsü', 'H. pylori, HPV, HBV, şistozomiyazis değil'),
        Q('24-25', 86, 'Kanser progresyonunu sağlayan (promoter) ajan?', 'Dietilstilbestrol (sentetik östrojen)', 'PAH, busulfan, nitrozamin, aflatoksin = başlatıcı'),
        Q('23-24', 73, 'Kondiloma akuminatum ve skuamöz hücreli karsinom gelişiminde rolü olan virüs?', 'Human papilloma virüs', 'EBV, HSV, HBV, VZV değil'),
        Q('22-23', 73, 'Transforme edici virüs grubunda sayılabilen?', 'Hepatit B virüsü', 'VZV, CMV, HSV, poliovirüs değil'),
        Q('21-22', None, 'Hepatoselüler karsinom yapan ajan?', 'Aflatoksin B1', 'Öğrenci hatırlamasından derlenmiş soru'),
    ],
)

# ---------------------------------------------------------------- konak
BEKLEYEN['konak'] = dict(
    baslik='Tümöre Karşı Konak Savunması, Tümörün Konağa Etkileri, Kanserin Tanısı',
    hoca='Prof. Dr. Çetin Boran', tarih='13 Ekim',
    sorular=[
        Q('25-26', 82, 'Hangisi onkofetal antijendir?', 'AFP', 'MUC-1, CD20, CD8, MHC değil'),
        Q('23-24', 81, 'Hangisi onkofetal antijendir?', 'CEA', 'CD20, CD30, MUC-1, MHC class II değil'),
        Q('21-22', None, 'Hangisi paraneoplastik sendrom örneğidir?', 'Cushing sendromu', 'Öğrenci hatırlamasından derlenmiş soru'),
    ],
)

# ---------------------------------------------------------------- epidem
BEKLEYEN['epidem'] = dict(
    baslik='Neoplazide Epidemiyoloji',
    hoca='Doç. Dr. Selma Erdoğan Düzcü', tarih='8 Ekim',
    sorular=[
        Q('23-24', 69, 'Türkiye birleşik veri tabanına göre erkek ve kadınlarda en sık görülen kanserler?', 'Erkekte akciğer, kadında meme kanseri', 'Erkekte prostat/mide, kadında over/tiroid/kolorektal değil'),
        Q('22-23', 69, 'Ağız boşluğunda skuamöz hücreli karsinom gelişiminde rol oynayan preneoplastik bozukluk?', 'Lökoplaki', 'Hashimoto, endometrial hiperplazi, karaciğer sirozu, Graves değil'),
    ],
)

# ---------------------------------------------------------------- epitel
BEKLEYEN['epitel'] = dict(
    baslik='Epitelyal Tümörler',
    hoca='Doç. Dr. Selma Erdoğan Düzcü', tarih='13 Ekim',
    sorular=[
        Q('25-26', 77, 'Tüm mide duvarını kalınlaştırmış, linitis plastika; müsin nedeniyle çekirdeği kenara itilmiş malign epitelyal tm?', 'Taşlı yüzük hücreli karsinom', 'Skuamöz papillom, Warthin, SCC, foliküler adenom değil'),
        Q('24-25', 81, 'Malign epitelyal tümörler arasında yer alan?', 'Adenokarsinom', 'Pleomorfik adenom, hamartomatöz polip, kondiloma akuminatum, Warthin benign'),
        Q('23-24', 74, 'Midede adenokarsinom morfolojisini gösteren özellik?', 'Tümör hücrelerinin gland benzeri yapı oluşturması', 'Büyük nükleus, muskularis invazyonu, pembe sitoplazma, belirgin nükleol değil'),
        Q('22-23', 70, 'Malign epitelyal tümörlerle ilgili doğru olan?', 'Lobüler karsinomlarda hücreler indian file (tesbih dizisi) oluşturabilir', "Çeldiriciler: taşlı yüzük iyi prognoz · papiller tiroid ca'da amiloid · anaplastik iyi diferansiye · adenoca'da keratin"),
        Q('21-22', None, 'Hangisi epitelyal kanser değildir? (polip, papillom, adenom, adenokarsinom, ÇKYE ca)', 'Benign olanlar (polip/papillom/adenom) — kanser = karsinom', 'Öğrenci hatırlamasından; kesin şık bilinmiyor'),
    ],
)

# ---------------------------------------------------------------- yumusak
BEKLEYEN['yumusak'] = dict(
    baslik='Yumuşak Doku Tümörleri',
    hoca='Dr. Öğr. Üyesi Songül Peltek Özer', tarih='12 Ekim',
    sorular=[
        Q('25-26', 62, 'Çocukluk çağının en sık görülen malign yumuşak doku tümörü?', 'Rabdomiyosarkom', 'Liposarkom, anjiyosarkom, Kaposi, MFH değil'),
        Q('24-25', 85, 'Hangisi yumuşak doku tümörüdür?', 'Leiomyosarkoma', 'Kondrosarkom (kıkırdak), RCC, malign melanom, seminom değil'),
        Q('22-23', 77, 'Hangi tümör metastaz YAPMAZ?', 'Desmoid tümör (derin fibromatozis)', 'RMS, leiomyosarkom, MPNST, MFH metastaz yapar'),
    ],
)

# ---------------------------------------------------------------- lenf
BEKLEYEN['lenf'] = dict(
    baslik='Lenf Nodu Patolojisi',
    hoca='Doç. Dr. Selma Erdoğan Düzcü', tarih='14 ve 16 Ekim',
    sorular=[
        Q('25-26', 74, 'Lenf nodunda sinüslerde çok sayıda histiyosit ve emperipolezis ile karakterize lenfadenit?', 'Rosai-Dorfman hastalığı', 'Castleman, sifiliz, kedi tırmığı, EMN değil'),
        Q('25-26', 75, 'İleri yaş, kemikte litik lezyon, CD38 + malign plazma hücre diskrazisi?', 'Multipl miyelom', 'Mantle hücreli, ALCL, Hodgkin, mikozis fungoides değil'),
        Q('24-25', 79, 'Sinüs histiyositozisinde histiyosit sitoplazmasında hücrelerin fagosite edilmemiş gibi bulunması?', 'Emperipolezis', 'Richter transformasyonu, RS hücresi, hematoksilen cisimciği, mantle zon değil'),
        Q('24-25', 80, 'Erkek, ileri yaş; multifokal litik kemik lezyonu, patolojik kırık; en sık malign plazma hücre diskrazisi?', 'Multipl miyelom', 'Foliküler, lenfoplazmositik lenfoma, hairy cell, Hodgkin değil'),
        Q('23-24', 71, 'Hodgkin ile ayırıcı tanısı yapılması gereken ve HL patogenezinde rolü olan reaktif lenfadenit?', 'Enfeksiyöz mononükleozis', 'Sifiliz, Castleman, dermatopatik, LGV değil'),
        Q('23-24', 72, 'T hücre kökenli malign lenfoma?', 'Anaplastik büyük hücreli lenfoma', 'Mantle, foliküler, küçük hücreli, Burkitt = B'),
        Q('22-23', 71, 'Periferik T hücreli lenfoma grubunda yer alan?', 'Anaplastik büyük hücreli lenfoma', 'Foliküler, mantle, marjinal zon, Burkitt = B'),
        Q('22-23', 72, 'Sinüs histiyositozisinde histiyosit sitoplazmasında canlı hücreler?', 'Emperipolezis', 'Richter sendromu, RS hücresi, granülom, atipik hücre değil'),
        Q('21-22', None, 'Popcorn görünümü, CD15 −, CD30 − ?', 'Nodüler lenfosit predominant Hodgkin lenfoma', 'Öğrenci hatırlamasından derlenmiş soru'),
        Q('21-22', None, '“Çit tarzı görünüm” (lenf nodu patolojisi)', 'Hatırlanan cevap: Castleman (?)', 'Kesin değil — öğrenci notu'),
    ],
)

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
