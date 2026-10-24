# -*- coding: utf-8 -*-
"""Kaynak: Drive › Komite-1 › PDF › Farmakoloji › 2026-2027(yeni) › Akif Hakan Kurt › 1-Farmakolojiye Giriş (33 slayt)"""

from yardim import B, C, Q  # noqa: F401

BOLUM = dict(
    key="f_giris", baslik="Farmakolojiye Giriş ve Absorpsiyon",
    hoca="Prof. Dr. Akif Hakan Kurt", tarih="21 Eylül", saat="2 saat",
    kaynak="1-Farmakolojiye Giriş · Prof. Dr. A. H. Kurt · 2026",
    ozet=["Her yıl 1 soru: **“İlaçların absorpsiyon hızını etkileyen faktörler”** (22-23, 23-24, 24-25, 25-26) — şıklar bu PDF'in absorpsiyon slaytlarından birebir.",
          "Tuzaklar ters çevrilmiş ifadeler: **tok karna** alım konsantrasyonu azaltır · inert maddeyle büyütme absorpsiyonu **yavaşlatır** · β-blokör kendi absorpsiyonunu **azaltır** · iyonik ilaç lipidde **çözünmez** · lipid/su oranı **yüksek** ve konsantrasyonu **yüksek** olan hızlı.",
          "Giriş kısmından (tanımlar, dallar, kaynaklar, eşdeğerlik) son 5 yılda doğrudan soru çıkmadı."],
    slaytlar=[
        [
            C("Tanım ve amaç", [
                B("Farmakoloji = **ilaç bilimi**; ilaçlarla biyolojik sistemler arasındaki ilişkiyi inceler."),
                B("Biyoaktif moleküller, subsellüler yapılar, hücre, doku, organlarda **in vitro**; deney hayvanı ya da insanda **in vivo**; bilgisayar modelleriyle **in silico** araştırma."),
                B("Esas amaç: hastalıkların **tedavisi, teşhisi ve önlenmesi (proflaksi)** için en uygun etkin maddeleri saptamak ve ilaç olarak geliştirmek; ayrıca yeni ilaç hedeflerini (gen, reseptör, enzim, sinyal yolakları…) araştırmak."),
            ]),
            C("İlaç (DSÖ tanımı)", [
                B("“Fizyolojik sistemleri veya patolojik durumları incelemek veya alanın yararı için değiştirmek amacı ile kullanılan **madde ve ürünler**” (terim bugün bile çok açık değil)."),
                B("Yararlı terapötik etkiyi başlıca **3 şekilde** oluşturur:"),
                B("1- **Altta yatan olayı etkileme**: somatik veya psişik işlev ve bozuklukları etkiler", lvl=1),
                B("2- **Eksik maddeyi yerine koyma**: hormon, vitamin gibi maddeleri yerine koyar", lvl=1),
                B("3- **İstilacıyı etkisiz kılma**: patojen, parazit, hücre veya mikropları etkisiz hâle getirir", lvl=1),
            ]),
            C("Terminoloji", [
                B("**Etki (action)**: hücre, doku, organ gibi izole/yalın sistemlerde ilacın genellikle direkt ve temel etkileri — örn. **vazodilatasyon**."),
                B("**Tesir (effect)**: bir organda veya tüm organizmada ölçülebilen, değerlendirilebilen değişiklikler — örn. **hipotansiyon**."),
                B("**Yanıt (response)**: hem etki hem de tesiri içine alır."),
                B("**Absorpsiyon**: ilacın uygulama yerinden emilerek kana karışması. **Doz**: bir defada verilen ilaç miktarı."),
                B("**Farmasötik şekiller (farmasötik dozaj formları)**: etkin maddelerin kolay uygulanması için özel sunum şekilleri — tablet, şurup, ampül, flakon, süpozituvar, merhem, TTS vd."),
            ]),
        ],
        [
            C("Formülasyon ve tedavi türleri", [
                B("**İlaç formülasyonu**: etkin maddelerin uygun yardımcı maddelerle karıştırılması; seçimde stabilite, biyoyararlanım, kolay uygulanabilirlik dikkate alınır — **farmasötik teknolojinin** alanı."),
                B("**Radikal tedavi**: hastalık nedeninin tamamen ortadan kaldırılması (örn. bazı bakteri infeksiyonlarının antibakteriyel ilaçlarla tedavisi)."),
                B("**Palyatif / semptomatik tedavi**: nedeni ortadan kaldırmadan semptom ve işaretlerin kısmen veya tamamen düzeltilmesi."),
                B("Örnek: diş absesi ağrısına analjezik → **semptomatik**; abseye neden olan mikroorganizmanın antibiyotikle öldürülmesi → **radikal**."),
                B("İlaçların **büyük kısmı** radikal tedaviden ziyade **palyatif** tedavi olanağı sağlar."),
            ]),
            C("İlaç etkisinin temel özellikleri", [
                B("1- **En önemli özellik: seçicilik (selektivite)** — istenen yapı ve olayları etkilemeli, diğerlerini etkilememeli; genellikle mutlak değil **göreceli**."),
                B("2- **Etkinin geçici olması** — ilaç kesilince etki kısa sürede kalkmalı; **kalıcı etki genellikle zehirin özelliğidir**."),
                B("3- **Doza bağımlılık** — etki, dozun artırılıp azaltılmasıyla paralellik göstermeli."),
            ]),
            C("Rasyonel tedavi ve zehir", [
                B("**Rasyonel tedavi**: her ilacın mutlaka yan tesiri vardır; **yarar/zarar oranı** dikkate alınır — oran ne kadar yüksekse hasta için o kadar iyi."),
                B("**Zehir**: ilaç olarak kullanılamayacak kadar toksik bileşikler; **rölatif** bir terim."),
            ]),
        ],
        [
            C("Farmakolojinin dalları", [
                B("**Klinik farmakoloji**: yeni ilaçların bulunması ve geliştirilmesi; klinik ilaç araştırmaları **4 faz**; geliştirme **minimum ~8-10 yıl**, ortalama maliyet **~1 milyar USD**."),
                B("**Farmakovijilans**: advers (ters, istenmeyen, yan) etkilerin ve ilaca ait diğer problemlerin belirlenmesi, anlaşılması, değerlendirilmesi ve önlenmesi; ilaç güvenliliğinin **toplum içinde** incelenmesi."),
                B("**Farmakodinami**: ilacın **vücuda ne yaptığı** ve mekanizmaları. **Farmakokinetik**: **vücudun ilaca ne yaptığı**."),
                B("**Kemoterapi**: istilacılara karşı tedavi."),
                B("**Farmakoterapi** (uygulamalı farmakoloji, tedavi bilimi, terapötik): hastaya göre en uygun tedavi rejimini (uygun ilaç, doz, süre) tespit eder."),
                B("**Farmakogenomik (farmakogenetik)**: bireylerin genetik değişkenliğine bağlı ilaç yanıtı farklılıkları."),
            ]),
            C("İlaç kaynakları", [
                B("Başlıca: **bitkiler, hayvanlar, mikroorganizmalar, madenler (mineraller), kimyasal sentez**."),
                B("Hammadde bulma güçlüğü ve zaman nedeniyle günümüzde genellikle **kimyasal sentez** (total ya da yarı sentetik)."),
            ]),
            C("Biyoteknolojik ilaçlar", [
                B("**Yaşayan organizmalar** kullanılarak üretilir; etkin molekül hücrenin ürettiği binlerce maddeden ayıklanıp saflaştırılır; süreç karışık, ileri teknoloji gerektirir."),
                B("Üretim: **hücre kültürü → fermentasyon → hasat → saflaştırma → formülasyon → bitmiş tıbbi ürün**."),
                B("Esas: etkin maddeyi (örn. **insan insülini**) sentezleten gen çıkarılıp **vektör DNA'sına** katılır, vektör hızlı bölünen hücreye (**E. coli**) sokulur (**gen klonlama**) → **biyofarmasötikler**."),
            ]),
        ],
        [
            C("Biyoteknolojik ilaç örnekleri", [
                B("İnsülin ve analogları · antianemik · antitrombotik ilaçlar · immünomodülatörler · hipofiz, hipotalamus hormonları (GH vd)"),
                B("Antineoplastikler (**monoklonal antikorlar-MAB**) · oftalmolojikler (**bevasizumab**, MAB) · sindirim sistemi ve metabolizma ürünleri"),
                B("Vitamin K ve diğer hemostatikler · seks hormonları · KOAH ilaçları · bağışık serumlar ve immünoglobulinler"),
            ]),
            C("İlaçların sınıflandırılması", [
                B("1- **Kimyasal yapıya** göre: kolinesterleri, katekolaminler"),
                B("2- **Etki yerine** göre: kalp glikozidleri, otonomik ilaçlar"),
                B("3- **Kullanım amacına** göre: antihipertansifler, analjezikler"),
                B("4- **Bitkisel kaynağa** göre: opium alkaloidleri, belladonna alkaloidleri"),
            ]),
            C("İlaç adları", [
                B("**Genel ad (jenerik ad)**: müstahzardaki farmakolojik etkiden sorumlu **etkin maddenin adı** — amoksisilin, kodein, asetilsalisilik asid."),
                B("**Müstahzar adı (ticari ad)**: ilacı bulan firmanın ürettiği, doğrudan hasta kullanımına sunulan ürün — Aspirin, Rocephin, Vermidon, Duocid."),
            ]),
            C("Eşdeğerlik ve biyoyararlanım", [
                B("**Farmasötik eşdeğerlik**: iki farklı ticari ürünün **aynı etkin maddeyi aynı miktarda**, aynı veya benzer farmasötik şekilde içermesi."),
                B("**Biyoeşdeğerlik**: farmasötik eşdeğer preparatların aynı dozda verildikten sonra **biyoyararlanımlarının aynı/benzer** olması."),
                B("**Biyoyararlanım**: dozaj formundaki ilacın **sistemik dolaşıma** ve böylece etki yerine ulaşma **hızı ve derecesi**; ağızdan alınan ilacın sistemik dolaşıma ne kadar geçtiğini gösterir."),
                B("Örnek: oral %100 → **%30 biyoyararlanım** = %30'u sistemik dolaşıma girdi, %70'i metabolize oldu ve/veya uzaklaştırıldı."),
            ]),
        ],
        [
            C("Biyolojik membranlardan geçiş", [
                B("Etki için ilaç doku/organa istenen sürede belli konsantrasyonda ulaşmalı: önce **emilmesi (absorpsiyon)**, sonra vücutta **dağılması** gerekir."),
                B("Aşılacak yapı: ağızdan → **GİS mukozası**; burundan → **burun mukozası**; doku içine → dokudaki **kapiller endotelyum**."),
                B("**İntravenöz** uygulamada **absorpsiyondan bahsedilmez** (ilaç kana karışmıştır)."),
            ]),
            C("Absorpsiyon hızı — 1. İlaçla ilgili faktörler (I-II)", [
                B("**I. Fizikokimyasal özellikler — a) Molekül büyüklüğü**: **düşük molekül ağırlıklılar** cüsselilere göre **daha yüksek hızda** geçer.", y="22-23 23-24"),
                B("Bunlar bazen kasıtlı olarak **inert bir maddeyle birleştirilip büyütülerek absorpsiyonu yavaşlatılır** → uzun etki (i.m. hormon: **testosteron sipiyonat, medroksiprogesteron asetat**).",
                  y="24-25 25-26", tuzak="“…büyütülerek absorpsiyonu hızlandırılır” → YANLIŞ"),
                B("**b) Lipofiliklik**: **lipid/su partisyon oranı yüksek** (yağda çözünürlüğü yüksek) ilaçlar membranları **hızlı ve kolay** geçer.",
                  y="22-23 23-24", tuzak="“Lipid/su partisyon oranı düşük ilaçlar membranları hızlı ve kolay geçer” → YANLIŞ"),
                B("Lipofilik = **non-iyonize**, yağda çözünür, membranı hızlı geçer · Hidrofilik = **iyonize**, suda çözünür, membranı zor geçer."),
                B("**İyonik olanlar lipidde çözünmez, membranları zor geçer.**", y="24-25 25-26",
                  tuzak="“İyonik ilaçlar lipidde iyi çözünür ve membranları kolay geçer” → YANLIŞ"),
                B("**II. Farmasötik şekil/çözücü**: **sıvı** formlar katılardan **daha hızlı** emilir; sıvılar arasında: **solüsyon → süspansiyon → emülsiyon**."),
                B("Bazı ilaçlar kasten **suda çözünmeyen esterleri** haline sokularak **etki süreleri uzatılır**; genellikle **kas içine** uygulananlar (**prokain penisilin, steroid hormon esterleri**).",
                  y="21-22 24-25 25-26", tuzak="“Esterle bağlanırsa kas içinden emilim süresi kısalır” (21-22*) → YANLIŞ"),
                B("İnjeksiyonluk solüsyonun **pH'sı** interstisyel alandan çok farklı yapılırsa ilaç **çöker** → uzun etki. Ağızdan **kontrollü salınımlı** formlar (farklı zamanlarda salan mikro kapsüller)."),
            ]),
        ],
        [
            C("Absorpsiyon hızı — 1. İlaçla ilgili faktörler (III-IV)", [
                B("**III. İlaç konsantrasyonu**: uygulama yerinde **konsantrasyon yüksekse** absorpsiyon genellikle **hızlı**.",
                  y="22-23 23-24", tuzak="“İlaç konsantrasyonu düşük olursa absorpsiyon genellikle hızlı olur” → YANLIŞ"),
                B("**Tok karna** ilaç almak konsantrasyonu **azaltır** → emilim yavaşlayabilir; çabuk etki istenince (örn. **şiddetli baş ağrısı**) **aç karna** verilmesi uygun.",
                  y="24-25 25-26", tuzak="“Aç karna ilaç almak konsantrasyonu azaltır ve emilimi yavaşlatır” → YANLIŞ"),
                B("**IV. Farmakolojik özellik**: **vazokonstriktörler** uygulama yerinde kan akımını azaltır, **vazodilatörler** artırır."),
                B("Lokal anesteziklere katılan **vazokonstriktör** absorpsiyonu **azaltır**, etki süresini **uzatır** (örn. diş hekimliği)."),
            ]),
            C("Absorpsiyon hızı — 2. Veriliş yeriyle ilgili biyolojik faktörler", [
                B("**I. Kan akım hızı**: uygulama yerindeki **kan akımı arttıkça** absorpsiyon **artar**.", y="22-23 23-24"),
                B("Kan akımını azaltan **şok, KKY, hipotansiyon, miksödem, arter tıkanıklığı** absorpsiyon hızını azaltır."),
                B("Bazen ilaç **kalp debisini azaltarak** doku perfüzyonunu bozup **kendi absorpsiyonunu azaltabilir** — örn. **beta blokörler**.",
                  y="24-25 25-26", tuzak="“Beta blokörler … kendi absorbsiyonunu artırabilirler” → YANLIŞ"),
                B("**II. Absorbe eden yüzeyin genişliği ve geçirgenliği**: yüzey alanı **büyük** ve geçirgen → absorpsiyon **artar** (küçükse yavaş).", y="22-23 23-24"),
                B("**Mukozalar** ciltten daha geçirgen · **ince barsak villusları** yüzeyi genişletir · inhalasyonda **alveol** geçirgenliği fazla → hızlı absorpsiyon."),
            ]),
            C("Mide-barsak kanalından absorpsiyonu etkileyenler", [
                B("Midenin boşalma süresi · barsak motilitesi · mide-barsak mukozasından geçen kan akımı"),
                B("Barsak epitelindeki **P-glikoproteinler** (örn. **siklosporini** barsak lümenine atarak absorpsiyonunu azaltır)"),
                B("Malabsorpsiyon (Crohn, total gastrektomi, ince barsak rezeksiyonu…)"),
            ]),
        ],
        [
            C("Midenin boşalma süresi", [
                B("Mide içeriğinin **yarıya inmesi** için geçen süre; normal erişkinde **1 saat**. İlacın esas absorpsiyon yeri olan **ince barsağa** erişme süresini etkiler."),
                B("**Geciktirenler**: çok sıcak besinler, ağır egzersiz, yağlı diyet, ülserasyon, gebelik, yaşlılık, diyabet, viskoz içecekler, **antikolinerjik ilaçlar**."),
                B("**Hızlandıranlar**: soğuk içecekler, hafif egzersiz, **sağ yana yatma**, malabsorpsiyon."),
            ]),
            C("Barsak motilitesi ve besinlerin etkisi", [
                B("**İshalde** geçiş hızlanır → absorpsiyon azalır (özellikle aktif transport/kolaylaştırılmış difüzyonla emilen **demir, tiamin, B12** çok azalır)."),
                B("Motilite azalınca geçiş uzasa da dissolüsyon/disintegrasyon yetersiz olduğundan absorpsiyon **oranı artmaz**."),
                B("Aç/tok karna alım absorpsiyon **oranını (biyoyararlanımı) değiştirmez**, **hızını** değiştirebilir."),
                B("**Aç karna**: ilaç midede kalmadan barsağa geçer → plazma düzeyi hızlı yükselir, **doruk daha yüksek**, etki daha çabuk başlar."),
                B("Aç karna = son yemekten **2 saat sonra** başlayıp gelecek yemekten **1 saat önce** biten süre."),
            ]),
            C("Hücrelerden geçiş", [
                B("Hücreler arasından (**parasellüler / interstisyel**) ya da doğrudan hücre içinden (**transsellüler**)."),
                B("**Pasif difüzyon**: transsellüler ve parasellüler · **Taşıyıcı aracılı**: aktif ve kolaylaştırılmış transport · **Diğer**: pinositoz, reseptör aracılı endositoz."),
                B("**Pasif difüzyon**: yön ve gücü **konsantrasyon farkı** belirler; taşıyıcı yok, enerji harcanmaz, **doyurulmaz**. Membranlardan geçiş **genellikle pasif difüzyonla**."),
                B("**Aktif transport**: taşıyıcı var, **enerji harcanır**, **doyurulabilir ve yarışmalı**."),
                B("**Kolaylaştırılmış transport**: taşıyıcı var, enerji harcanmaz, yönü konsantrasyon farkı belirler; pasif difüzyondan **çok daha hızlı**."),
                B("Taşıma türleri: **uniport, ko-transport (simport), kontratransport (antiport)**."),
            ]),
        ],
        [
            C("İyonizasyon", [
                B("Çoğu ilaç **zayıf asid veya zayıf baz** → sulu ortamda iyonize ve non-iyonize halde; iyonizasyon **ortamın pH'sına** ve ilacın **pKa** değerine bağlı."),
                B("Baz: R-NH2 + H⁺ ⇌ R-NH3⁺ · Asid: R-COOH ⇌ R-COO⁻ + H⁺"),
                B("İyonizasyon oranı **Henderson-Hasselbalch** denklemiyle saptanır:"),
                B("Asidler: **pKa − pH = log ([iyonize olmamış] / [iyonize])**", lvl=1),
                B("Bazlar: **pH − pKa = log ([iyonize olmamış] / [iyonize])**", lvl=1),
                B("**Zayıf asid** ilaç zayıf **bazik ortamda iyonize**, zayıf **asidik ortamda non-iyonize** → bu son haliyle membranları kolay geçer."),
            ]),
            C("Absorpsiyon kinetiği", [
                B("Absorpsiyon genellikle **pasif difüzyonla**; hızı kontrol eden faktör **konsantrasyon**. Çok az ilaç aktif/kolaylaştırılmış transportla emilir."),
                B("**Sıfırıncı derece kinetiği**: **Hız = k (sabit)** — aktif transportta ve metabolizma/eliminasyonun **doyurulmasında** (zehirlenme, aşırı ilaç alımı, intoksikasyon); konsantrasyon **doğrusal** azalır."),
                B("**Birinci derece kinetiği**: **Hız = k × C** (k sabit) — **pasif difüzyonda**; **üssel (eksponansiyel)** azalma."),
            ]),
        ],
    ],
    sorular=[
        Q("25-26", 18, "Absorpsiyon hızını etkileyen faktörlerle ilgili DOĞRU olan?",
          "Bazı ilaçlar kasten suda çözünmeyen esterleri haline sokularak etki süreleri uzatılabilir",
          "Yanlışlar: iyonik ilaç lipidde iyi çözünür · inert maddeyle büyütme hızlandırır · β-blokör kendi absorpsiyonunu artırır · aç karna konsantrasyonu azaltır"),
        Q("24-25", 27, "Absorpsiyon hızını etkileyen faktörlerle ilgili YANLIŞ olan?",
          "Aç karna ilaç almak konsantrasyonu azaltır ve emilimi yavaşlatabilir",
          "Doğrusu: TOK karna. Doğrular: iyonik ilaç lipidde çözünmez · β-blokör kendi absorpsiyonunu azaltır · inert maddeyle büyütme yavaşlatır · esterler etkiyi uzatır"),
        Q("23-24", 13, "Absorpsiyon hızını etkileyen faktörlerle ilgili YANLIŞ olan?",
          "Lipid/su partisyon oranı düşük ilaçlar membranları hızlı ve kolay geçer",
          "Doğrusu: oranı YÜKSEK olanlar. Doğrular: yüksek MA → yavaş · konsantrasyon yüksek → hızlı · kan akımı ↑ → absorpsiyon ↑ · yüzey küçük → yavaş"),
        Q("22-23", 24, "Absorpsiyon hızını etkileyen faktörlerle ilgili YANLIŞ olan?",
          "İlaç konsantrasyonu düşük olursa absorpsiyon genellikle hızlı olur",
          "Doğrusu: konsantrasyon YÜKSEK → hızlı. Doğrular: düşük MA → hızlı · lipofilik hızlı geçer · kan akımı ↑ → absorpsiyon ↑ · yüzey büyük → hızlı"),
        Q("21-22", None, "Absorpsiyonla ilgili hangisi doğru? (hatırlanan; şıklarda “esterle bağlanırsa kas içine emilim süresi kısalır” vardı)",
          "Suda çözünmeyen ester → i.m. absorpsiyon yavaşlar, etki süresi uzar",
          "Hatırlanan şık bu haliyle yanlış: esterleşme etkiyi uzatır (prokain penisilin, steroid hormon esterleri)"),
    ],
)
