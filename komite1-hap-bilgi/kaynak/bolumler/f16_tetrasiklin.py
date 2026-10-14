# -*- coding: utf-8 -*-
"""Kaynak: Drive › Komite-1 › PDF › Farmakoloji › 2026-2027(yeni) › Akif Hakan Kurt › 9-Tetrasiklinler Amfenikoller"""

from yardim import B, C, Q  # noqa: F401

BOLUM = dict(
    key="tetrasiklin", baslik="Tetrasiklinler ve Amfenikoller",
    hoca="Prof. Dr. Akif Hakan Kurt", tarih="12 Ekim", saat="2 saat",
    kaynak="9-Tetrasiklinler Amfenikoller · Prof. Dr. A. H. Kurt · 2026",
    ozet=["Son 5 yılda bu dersten **5 soru** çıktı (22-23, 23-24, 24-25 ×2, 25-26); hepsi “hangisi doğru / **yanlıştır**” tipinde.",
          "Tekrarlayan tuzaklar: **BOS hariç** dağılım (“tüm dokulara” diye yanlış), **minosiklin** = en uzun etkili + en lipofilik (doksisikline kaydırılır), **stafilokok / streptokok / enterokok → tercih edilmez**.",
          "Amfenikoller: kloramfenikolde **oral palmitat**, **parenteral süksinat** esteri (ters verilir); yarı ömür **~3 saat**; **kan-beyin engelini en fazla geçen** ilaç."],
    slaytlar=[
        [
            C("Tetrasiklinler — etki mekanizması", [
                B("Bakteri hücresinde **ribozomal 30 S alt birimine reversibl olarak bağlanır**, protein sentezini durdurur."),
                B("**Bakteriyostatik** etkilidir."),
            ]),
            C("Etki spektrumu", [
                B("**Tetrasiklinler en geniş spektrumlu antimikrobik ilaçlardır.**", y="22-23 23-24"),
                B("**Minosiklin ve doksisiklin** diğer tetrasiklinlere rezistan mikroorganizmalara da etki eder."),
                B("**Gram (+) koklar**: artık çoğu rezistandır."),
                B("**Gram (+) aerobik ve anaerobik basiller** (B. anthracis, Clostridiumlar, Listeria monocytogenes): **penisilin G kadar güçlü olmamakla beraber** etkilidir."),
            ]),
            C("Gram (−) basiller — ilk tercih edilen ilaçlar", [
                B("**Brucella**, **Vibrio cholerae**, **Pseudomonas mallei**, **Pseudomonas pseudomallei**, **Hemophilus ducreyi**, **Calymmatobacterium granulomatis** enfeksiyonlarında **ilk tercih**."),
            ]),
            C("Ayrıca etkili oldukları bakteriler", [
                B("Yersinia pestis · Yersinia enterocolitica · Bordetella pertussis · Francisella tularensis · Pasteurella multocida."),
            ]),
        ],
        [
            C("Bakteriler dışında duyarlı mikroorganizmalar", [
                B("**Riketsiyalar**: R. prowazeki, Coxiella burnetii."),
                B("**Klamidyalar**: C. trachomatis, C. pneumoniae, C. psittaci."),
                B("**Spiroketler**: Treponema pallidum, Borrelia recurrentis (rekürren ateş), Borrelia burgdorferi (Lyme hastalığı)."),
                B("**Mycoplasma pneumoniae**, **Actinomyces israelii**, **Ureaplasma urealyticum**."),
                B("**Entamoeba histolytica** ve **Plasmodium** gibi protozoonlar duyarlıdır."),
                B("**Funguslar tetrasiklinlere duyarlı değildir.**", y="22-23 23-24"),
            ]),
            C("Farmakokinetik — absorpsiyon", [
                B("Farmakokinetik özellikleri kendi aralarında **değişkenlik gösterir**."),
                B("GİS’ten emilim: **minosiklin %100, doksisiklin %95, tetrasiklin %77, oksitetrasiklin %60**, diğerleri daha az.", y="25-26", tuzak="“minosiklin %60, doksisiklin %77, oksitetrasiklin %100”"),
                B("**Ca, Fe, Zn, Al, Mg** gibi 2 ve 3 değerli metal bileşikleri tetrasiklinle **şelat** yapıp inaktive eder; şelatlar suda çözünmez → **absorbe edilmez**."),
                B("**Antiasitler** (Ca, Al, Mg), **antianemikler** (demir) ve **süt, yoğurt** gibi kalsiyumdan zengin yiyecekler **birlikte alınmamalı**.", y="22-23 23-24"),
            ]),
        ],
        [
            C("Dağılım", [
                B("Plazma proteinlerine değişik oranlarda bağlanır: **en fazla doksisiklin, metasiklin, demetilklortetrasiklin (%90-93)**, **en az oksitetrasiklin (%35)**."),
                B("**BOS hariç** tüm vücut dokularına ve sıvılarına dağılımları iyidir.", y="22-23 23-24 24-25 25-26", tuzak="“Tüm vücut dokularına ve sıvılarına dağılımları iyidir”"),
                B("**Minosiklin** ve ikinci sırada **doksisiklin** en fazla **lipofilik** olanlardır.", y="24-25 25-26", tuzak="“Doksisiklin en fazla lipofilik olan tetrasiklindir”"),
                B("**Sadece minosiklin** BOS ve SSS’ne yeterli ölçüde geçer; ancak **vestibüler toksisitesi** kullanımını kısıtlar."),
                B("Minosiklin **salya ve gözyaşına** da önemli oranda geçer → **menengokokal menenjit profilaksisi** için önemli."),
            ]),
            C("Doku geçişi ve itrah", [
                B("Bütün tetrasiklinler **kemik dokusuna** ve **malign tümör dokusuna** iyi geçer."),
                B("**Plasentayı geçip fetal kemik ve dişlerde birikir**; **anne sütüne** de geçer."),
                B("Vücuttan itrahı başlıca **böbreklerden ve safra içinden** olur.", y="25-26"),
            ]),
        ],
        [
            C("Kullanılış", [
                B("**Oral ya da parenteral** kullanılır; cilt ve göz pomadı, göz damlası, ovül olarak **lokal** kullanımı da vardır.", y="22-23"),
                B("Etki gücünün yüksekliği ve diğer üstünlükleri nedeniyle **doksisiklin** diğer tetrasiklinlere **tercih edilir**."),
            ]),
            C("En tercih edilen antibiyotik oldukları durumlar", [
                B("**Riketsiya enfeksiyonları** (epidemik tifus, Q ateşi gibi): **kloramfenikol de** oldukça etkilidir."),
                B("**Kolera**, **granüloma inguinale** (Calymm. granulomatis), **borreliozis**, **leptospiroz**."),
                B("Klamidyaların yaptığı **psitakozis, keratokonjonktivit, pnömoni**."),
                B("**Pelvis içi infeksiyonlarda** kombine tedavide kullanılır."),
            ]),
            C("Tercih edilmedikleri enfeksiyonlar", [
                B("Rezistan suşların fazlalığı nedeniyle **stafilokok, streptokok ve enterokok enfeksiyonlarında tercih edilmez**.", y="23-24 24-25", tuzak="“Stafilokok, streptokok ve enterokok enfeksiyonlarında tercih edilir”"),
            ]),
        ],
        [
            C("Tetrasiklin, oksitetrasiklin", [
                B("**Doksisiklin’in çıkmasıyla** klinik kullanımı azalmıştır."),
                B("**Kısa etkilidirler**; **6 saatte 250-500 mg**; terapötik düzeye ulaşmak için **yükleme dozu** verilir."),
                B("**12 yaş altı çocuklarda kullanılmaz.**"),
            ]),
            C("Demetilklortetrasiklin (demeklosiklin)", [
                B("**Orta etki sürelidir.**"),
                B("**En fazla fotosensitivite** yapan tetrasiklin türevidir."),
            ]),
            C("Doksisiklin", [
                B("**Etki süresi uzun** olan tetrasiklindir."),
                B("Mide-barsak kanalından **tama yakın absorbe** edilir; dokularda ve vücut sıvılarında fazla toplanır."),
                B("**Eliminasyon karaciğerden** olduğu için **böbrek yetmezliğinde güvenle** kullanılır."),
                B("Yetişkin: **ilk gün 2 × 100 mg**, sonra **100 mg/gün** (bir veya iki dozda); şiddetli enfeksiyonda 2 × 100 mg."),
            ]),
            C("Minosiklin", [
                B("**En uzun etki süreli tetrasiklindir.**", y="24-25 25-26", tuzak="“Doksisiklin etki süresi en uzun olan tetrasiklindir”"),
                B("Antimikrobik ve farmakokinetik özellikleri doksisikline benzer."),
                B("**%70’e varan oranda reversibl vestibüler bozukluk** yaptığından artık pek tercih edilmez."),
            ]),
        ],
        [
            C("Yan etkiler — GİS, diş-kemik", [
                B("**1. GİS**: bulantı, kusma, anoreksi, ishal sık."),
                B("Birkaç günlük tedaviden sonra barsakta **Candida** hakim olur; flora bozukluğuna bağlı ishal, **C. difficile** psödomembranöz koliti.", lvl=1),
                B("**2. Diş ve kemik**: kalsiyuma bağlanarak **kahverengi lekelenme**; gebelikte fetal diş/kemikte renk değişikliği, gelişme bozukluğu, **kemik deformiteleri**."),
                B("**Gebelere 4. aydan sonra verilmemeli.**", lvl=1),
                B("**Bebek ve 12 yaş altı çocuklarda kontendikedir**: mine ve dentinde hipoplazi, kalıcı dişlerde gelişme bozukluğu.", lvl=1),
            ]),
            C("Karaciğer ve böbrek", [
                B("**3. Hepatotoksik**: önceden karaciğer fonksiyon bozukluğu olanlarda ve **gebelerde** yüksek doz → karaciğerde **yağlı dejenerasyon**."),
                B("**4. Nefrotoksik**: böbrek fonksiyon bozukluğunda yüksek doz/uzun süre → **asidoz, azotemi, hiperfosfatemi**, elektrolit bozukluğu."),
                B("**Doksisiklinde daha az** görülür → böbrek yetmezliğinde **doksisiklin tercih edilmeli**.", lvl=1),
            ]),
        ],
        [
            C("Alerjik ve hipersensitivite", [
                B("**5. Alerjik**: seyrek olarak ürtiker, anjiyonörotik ödem, dermatit."),
                B("**6. Fotosensitivite**: özellikle **demeklosiklin ve doksisiklin** ile, **sarışınlarda** daha fazla; cilt renginde koyulaşma, dermatit, **tırnaklarda pigmentasyon**."),
                B("İlacın ciltte birikmesine bağlıdır; özellikle **yazın** oluşur.", lvl=1),
            ]),
            C("Tromboflebit, hematolojik", [
                B("**Tromboflebit**: i.v. uygulamada; i.m. verilişte ağrı ve infiltrasyon. **Türkiye’de parenteral tetrasiklin preparatları artık üretilmemektedir.**"),
                B("**7. Hematolojik**: barsak florası bozulunca **K vitamini sentezi azalır** → kanama eğilimi; nadiren **nötropeni** ve **hemolitik anemi**."),
            ]),
            C("SSS ve diğer", [
                B("**8. SSS**: **minosiklin** lipid çözünür olduğundan SSS’ne penetre olur; en sık **vestibüler toksisiteye bağlı vertigo** (baş dönmesi, bulantı, denge bozukluğu, kulak çınlaması)."),
                B("**9. Beyin psödotümörü**: **yenidoğan ve bebeklerde** fontanellerde şişme, papilla ödemi; **beyin tümörünü taklit eden reversibl sendrom** (pseudotümör serebri), kafa içi basınç artışına bağlı.", y="24-25"),
                B("Beyin psödotümörü yapan diğer ilaçlar: **nalidiksik asit ve amiodaron**.", lvl=1),
                B("**10. Gebelerde**: fötusla ilgili toksik tesirlerin yanı sıra **katabolik asidoz**."),
            ]),
        ],
        [
            C("Amfenikoller — genel", [
                B("Bu grupta **kloramfenikol ve tiamfenikol** bulunur."),
                B("4 önemli özelliği nedeniyle diğer antibiyotiklere üstündür: **geniş spektrumlu**, **yan etki insidensi düşük**, **vücutta dağılımı iyi**, **ucuz**.", y="24-25"),
            ]),
            C("Etki mekanizması", [
                B("Bakteri ribozomlarının **50 S alt birimine** bağlanıp protein sentezini bozar; **bakteriyostatiktir**."),
                B("Kloramfenikol ayrıca **memeli hücresinde 70 S ribozomların** yaptığı proteinleri de inhibe ederek **aplastik anemi**ye neden olabilir."),
                B("**Eritromisin, linkomisin ve klindamisin** ile **aynı bağlanma yeri için yarıştıklarından birlikte kullanılmazlar.**", y="24-25"),
            ]),
            C("Etki spektrumu", [
                B("**Gram (+) koklar**: Strep. pneumoniae, Strep. pyogenes, Staph. aureus · **Gram (+) basiller**: Nocardia hariç hemen hepsi."),
                B("**Gram (−)**: Neisseria, H. influenzae, C. diphtheriae, Bordetella pertussis, Brucella, Vibrio cholerae · **anaerob**: Bacteroides’ler (Gram −), C. perfringens (Gram +)."),
                B("**Enterobakterler**: Salmonella, Shigella, E. coli, Klebsiella pneumoniae, Proteus mirabilis."),
                B("**Bakteri dışı**: Riketsiya, Klamidya, T. pallidum, Leptospiralar."),
            ]),
        ],
        [
            C("Kloramfenikol — farmakokinetik", [
                B("**Çok lipofiliktir**; ince barsaktan emilimi **%100’e yakın**; doruk konsantrasyon **1-2 saat** (15-20 µg/ml)."),
                B("**Oral yoldan palmitat esteri** verilir; barsakta hızla hidroliz olarak absorbe edilir.", y="24-25", tuzak="“Oral yoldan süksinat esteri kullanılır”"),
                B("**Parenteral yoldan süksinat esteri** kullanılır; bu haliyle etkisiz, vücutta hızla hidroliz olarak aktif kloramfenikole dönüşür."),
                B("Beyin, BOS ve vücut sıvıları dahil **tüm dokulara yüksek konsantrasyonda** dağılır."),
                B("**Kan-beyin engelini en fazla geçen ilaçtır**: beyin dokusuna plazmadan **9 kat fazla**, BOS’a plazmanın **%50’si** kadar geçer.", y="24-25"),
                B("**Fetüse geçişi kolay**; **karaciğerde metabolize** edilir → karaciğer yetmezliğinde doz ayarlanmalı."),
                B("**Eliminasyon yarı ömrü ~3 saat.**", y="24-25"),
            ]),
            C("Yenidoğan ve bebek", [
                B("**Yenidoğan ve 2 haftalığa kadar** bebeklerde yarı ömür **24 saat**e çıkar (glükoronil sentez ve böbrek eliminasyon mekanizması tam oluşmadığından)."),
                B("**2-4 haftalık** bebeklerde ~**12 saat** → prematüreler ve yenidoğanlar toksik etkilere çok duyarlı."),
            ]),
        ],
        [
            C("Kloramfenikol — kullanımı", [
                B("**40 yılı aşkın** süredir **tifo (Salmonella typhi)** tedavisinde; ilaç kesilince **nüks olasılığı fazla**; **myelotoksik etki** nedeniyle kısıtlı; tifoda **6 saatte 1 g, 4 hafta**."),
                B("Günümüzde S. typhi suşları kloramfenikol, ko-trimoksazol ve ampisiline **multirezistan** → **fluorokinolonlar ilk tercih**; kontrendike oldukları **çocuk ve gebelerde ilk tercih seftriakson**."),
                B("Kan-beyin ve kan-sıvı engelini en iyi geçtiği için **H. influenzae menenjiti**nde **ampisilinle kombine** ya da ampisiline direnç varsa **tek başına**."),
                B("**N. meningitidis ve S. pneumoniae menenjiti**nde hasta **penisilin G’ye alerjik** ise kloramfenikol ve sefalosporinler alternatiftir (**sefalosporinler tercih edilir**)."),
            ]),
            C("Diğer kullanım alanları", [
                B("**Aerob Gram (−) basiller, stafilokok menenjiti** ve **Bacteroides fragilis’in yaptığı beyin absesi**nde kloramfenikol tercih edilir."),
                B("**Tifüs, Q ateşi** gibi riketsiya enfeksiyonlarında tetrasiklin kullanılamıyorsa (gebelik vb.) **alternatif**."),
                B("Gözün tabakalarına iyi geçtiği için **göz enfeksiyonlarında** ve **vajina infeksiyonlarında**."),
                B("**Bruselloz, tularemi, veba, listeria**’da tek ya da kombine."),
                B("**Yersinia enterocolitica sepsisi**nde en çok tercih edilen iki ilaçtan biri (diğeri **aminoglikozitler**)."),
            ]),
        ],
        [
            C("Preparatlar ve dozlar", [
                B("**1) Kloramfenikol · 2) Kloramfenikol palmitat · 3) Kloramfenikol sodyum süksinat · 4) Tiamfenikol.**"),
                B("**Palmitat**: tatsız ester; **çocuk ve bebeklere** özgü **süspansiyon** müstahzarları için."),
                B("**Sodyum süksinat**: **enjeksiyonluk** müstahzarlar için; vücutta hidroliz edilip serbest kloramfenikole dönüşür."),
                B("Doz: **yetişkin ve çocuk 50 mg/kg/gün** (4 eşit doz); **yenidoğan 25 mg/kg/gün** (4 eşit doz)."),
                B("Gebelikte **Gray sendromu**na neden olabilir; **anne sütüne geçer**."),
            ]),
            C("Tiamfenikol", [
                B("Kloramfenikolden **daha az etkilidir**."),
                B("GİS ve i.m. yerden **daha iyi absorbe** edilir; plazma proteinlerine **daha az bağlanır**; **%50-70’i değişmeden böbrekten** atılır → **böbrek yetmezliğinde doz ayarı**; yarı ömür **2-3 saat**."),
                B("Kloramfenikolden farklı olarak **safra yolu infeksiyonları**nda da kullanılır (safra yoluyla itrahı daha fazla)."),
                B("Doz: yetişkin **2 × 750 mg – 3 × 500 mg**; çocuk **20-30 mg/kg/gün** (2 eşit doz)."),
                B("Kontrendikasyon: **aşırı duyarlılık, hematopoietik bozukluklar, anüri**; gebelerde ve yenidoğanlarda emniyeti kesinleşmemiş."),
            ]),
        ],
        [
            C("Amfenikol yan etkileri", [
                B("**1) Kemik iliği depresyonu**"),
                B("**2) GİS bozuklukları**"),
                B("**3) Alerjik** cilt döküntüleri, ürtiker, anjiyoödem."),
                B("**4) Gri sendrom**: prematüre ve yenidoğanda kloramfenikol **konjügasyonla yeterince metabolize edilemez**, kan düzeyi çok yükselir."),
                B("Tablo: **akut solunum ve dolaşım depresyonu, hipotermi, kas gevşemesi, karında distansiyon, metabolik asidoz, ciltte gri renk**.", lvl=1),
                B("Gri sendrom, ilacı **aşırı dozda alan erişkinlerde** de ortaya çıkabilir.", lvl=1),
                B("**5) Herxheimer reaksiyonu**: yüksek doz kloramfenikolle **öldürülen tifo basillerinin toksinleriyle** oluşan **dolaşım kollapsı**; tedavisinde **sistemik glukokortikoidler** kullanılabilir."),
                B("**6) Nörotoksik**: başağrısı, ruhsal depresyon, deliryum, konfüzyon; nadiren **periferik nörit, optik nöropati**."),
            ]),
        ],
    ],
    sorular=[
        Q("25-26", 26, "Tetrasiklin grubu antibiyotikler için doğru olan hangisidir?",
          "B) Minosiklin etki süresi en uzun olan tetrasiklindir",
          "A yanlış (BOS hariç), C (en lipofilik minosiklin), D (%100/95/77/60). Not: PDF’e göre E (itrah böbrek+safra) da doğru — anahtar belirsiz."),
        Q("24-25", 35, "Tetrasiklin grubu antibiyotikler için YANLIŞ olan hangisidir?",
          "C) Doksisiklin etki süresi en uzun olan tetrasiklindir",
          "En uzun etkili **minosiklin**. Diğer şıklar doğru: beyin psödotümörü, BOS hariç dağılım, minosiklin en lipofilik, stafilokok/strep/enterokokta tercih edilmez."),
        Q("24-25", 36, "Amfenikol grubu antibiyotikler için YANLIŞ olan hangisidir?",
          "E) Oral yoldan süksinat esteri kullanılır",
          "Oral **palmitat**, parenteral **süksinat**. Diğerleri doğru: geniş spektrum, t½ ~3 sa, kan-beyin engelini en çok geçen, eritromisin/klindamisinle birlikte verilmez."),
        Q("23-24", 21, "Tetrasiklin grubu antibiyotikler için YANLIŞ olan hangisidir?",
          "E) Stafilokok, streptokok ve enterokok enfeksiyonlarında tercih edilir",
          "Rezistan suşlar nedeniyle **tercih edilmez**. Diğerleri doğru: Ca’lı yiyecek/antiasit/antianemik alınmaz, BOS hariç dağılım, fungus duyarlı değil, en geniş spektrum."),
        Q("22-23", 32, "Tetrasiklin grubu antibiyotikler için YANLIŞ olan hangisidir?",
          "B) Tüm vücut dokularına ve sıvılarına dağılımları iyidir",
          "**BOS hariç** dağılım iyidir. Diğerleri doğru: Ca/antiasit/antianemik, fungus duyarlı değil, en geniş spektrum, oral ya da parenteral kullanım."),
    ],
)
