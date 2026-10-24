# -*- coding: utf-8 -*-
"""Kaynak: Drive › Komite-1 › PDF › Patoloji › 2026-2027(yeni) › Selma Erdoğan Düzcü › 6-AMİLOİDOZ (39 slayt)"""

from yardim import B, C, Q  # noqa: F401

BOLUM = dict(
    key="amiloid", baslik="Amiloidoz",
    hoca="Doç. Dr. Selma Erdoğan Düzcü", tarih="25 Eylül", saat="1 saat",
    kaynak="6-AMİLOİDOZ · Doç. Dr. S. E. Düzcü · 2026",
    ozet=["Son 5 yılda **her yıl 1 soru**: **Kongo kırmızısı** (21-22, 22-23, 23-24), **“AA/AL/ATTR H&E’de ayırt edilir” → YANLIŞ** (24-25), **FMF → amiloidoz** (25-26).",
          "**Kongo kırmızısı**: ışık mikroskobunda **pembe-kırmızı**, polarize ışıkta **elma yeşili çift kırma**; çeldiriciler: Giemsa, kristal viyole, H&E, Alcian blue, CD3/CD20.",
          "Tip ayrımı **spesifik immünhistokimya** ile; **FMF → AA**, **multipl myelom → AL**, **diyaliz → β2-mikroglobulin**; şüphede **rektal biyopsi** tanıya yardımcı."],
    slaytlar=[
        [
            C("Amiloidoz nedir? (slayt 2, 4)", [
                B("Amiloidoz temelde bir **protein katlanma bozukluğudur**: **ekstrasellüler dokularda fibriller** şeklinde depolanan **anormal katlanmış proteinlerden** oluşur.", y="24-25"),
                B("Tüm amiloid depolanmaları, kökenlerine bakılmaksızın **β-kıvrımlı polipeptid zincirlerinden** oluşan, **dallanmayan, 7.5-10 nm çapta fibrillerden** meydana gelir."),
                B("Aynı morfolojik görünüme sahip olsa da amiloid **yapısal olarak homojen bir protein değildir**: **20'den fazla (son sayımda 31)** farklı protein amiloid fibrilleri oluşturabilir."),
            ]),
            C("Kalite kontrol başarısızlığı (slayt 4-5)", [
                B("Normalde hatalı katlanmış proteinler hücre içinde **proteozomlar**, hücre dışında **makrofajlar** tarafından parçalanır."),
                B("Amiloidozda bu **kalite kontrol mekanizması başarısız** olur → hatalı katlanmış protein **hücre dışında birikir**."),
                B("Hatalı katlanmış proteinler **stabil değildir** → dokularda biriken **oligomerler ve fibriller** gelişir."),
            ]),
            C("Amiloidi oluşturan proteinler: 2 genel sınıf (slayt 5)", [
                B("1- **Hatalı katlanmaya eğilimli normal proteinler**: fazla miktarda üretildiklerinde fibril oluşturmak üzere bir araya gelirler."),
                B("2- **Hatalı katlanmaya ve ardından agregasyona eğilimli mutant proteinler**."),
            ]),
        ],
        [
            C("En sık amiloid proteinleri: AL (slayt 6)", [
                B("Birçok amiloid proteini formu içinde **üçü en sıktır** (slayt sırası: **AL → AA → Aβ**)."),
                B("**AL (amiloid hafif zincir)**: protein **plazma hücreleri** tarafından yapılır; **immünglobulin hafif zincirleri**, hafif zincirlerin **amino terminal fragmanları** veya her ikisinden oluşur."),
                B("AL tipi fibril proteini depolanması bazı **monoklonal B hücre proliferasyonlarıyla** birliktedir."),
            ]),
            C("AA: amiloid-ilişkili fibril / SAA (slayt 7-8)", [
                B("**SAA** (serum amiloid asosiye) protein: **karaciğerde sentezlenen**, daha büyük (**12-kDa**) bir serum prekürsöründen gelişen özgün **nonimmünglobulin** proteindir."),
                B("İltihap sırasında **IL-1 ve IL-6** gibi sitokinlerin etkisiyle **karaciğer hücrelerinde** sentezlenir → uzun süren iltihap **SAA ↑** ve **AA tipi amiloid** depolanmasına yol açar."),
                B("Yüksek serum SAA düzeyleri iltihabi durumlarda sıktır, ama çoğu durumda **amiloidoza yol açmaz**. Olası 2 açıklama:"),
                B("SAA normalde **monositten gelişen enzimlerle** solubl ürünlere parçalanır; amiloidoz gelişenlerde **enzim defekti** → yetersiz parçalanma → **solubl olmayan AA molekülleri**.", lvl=1),
                B("**SAA molekülündeki genetik yapısal anomali** onu **makrofajlarla parçalanmaya dirençli** kılar.", lvl=1),
            ]),
        ],
        [
            C("Aβ amiloid (slayt 9)", [
                B("**Alzheimer hastalığının serebral lezyonlarında** bulunur."),
                B("**Serebral plakların merkezlerini** ve **serebral kan damarlarındaki** amiloid depozitlerini oluşturan **4-kDa** bir peptiddir."),
                B("**Amiloid prekürsör protein (APP)** denilen çok daha büyük bir **transmembran glikoproteinden** gelişir."),
            ]),
            C("Transtiretin, TTR (slayt 10)", [
                B("**Tiroksin ve retinole bağlanıp bunları nakleden** normal bir serum proteinidir (adını bu özelliğinden alır)."),
                B("TTR yapısında, proteini **hatalı katlanma, agregasyon ve proteolize direnç**e yatkın hale getiren bir değişiklik yapabilir → amiloid olarak depolanan agregatlar."),
                B("TTR'ye bağlı hastalıklar: **ailesel amiloid polinöropatileri**."),
                B("TTR **yaşlıların kalbinde** depolanır (**senil sistemik amiloidoz**): protein **yapısal olarak normaldir**, ama **yüksek konsantrasyonlarda** birikir."),
            ]),
            C("β2-mikroglobulin, Aβ2m (slayt 11-12)", [
                B("**MHC class I** molekülünün bir komponenti ve normal serum proteinidir; **uzun süreli hemodiyalizdeki hastalarda** görülen amiloid fibril subünitesidir (**Aβ2m**)."),
                B("Aβ2m fibrilleri yapı olarak **normal β2m ile aynıdır**; böbrek hastalarında serumda yüksektir, **diyaliz membranlarında efektif filtre edilmediğinden** dolaşımda kalır."),
                B("Uzun süreli diyalizde **%60-80** hastada **sinovya, eklemler ve tendon kılıflarında** amiloid depolanması gelişir."),
                B("**Hormonlar (prokalsitonin)** ve **keratin** gibi farklı prekürsörlerden gelişen amiloid depolanmaları da bildirilmiştir."),
            ]),
        ],
        [
            C("Tablo 4-13: Sistemik (generalize) amiloidoz (slayt 13)", [
                B("Tablo sütunları: **klinikopatolojik kategori · ilişkili hastalık · majör fibril proteini · kimyasal ilişkili prekürsör protein**."),
                B("**Primer amiloidoz** (amiloidoz ile birlikte immünosit diskrazileri): **multipl myelom** ve diğer monoklonal plazma hücre proliferasyonları → **AL**.", y="24-25"),
                B("Prekürsör: **immünglobulin hafif zincirleri, başlıca λ tip**.", lvl=1),
                B("**Reaktif sistemik amiloidoz (sekonder)**: **kronik iltihabi durumlar** → **AA**; prekürsör **SAA**."),
                B("**Hemodiyaliz-ilişkili amiloidoz**: **kronik renal yetmezlik** → **Aβ2m**; prekürsör **β2-mikroglobulin**."),
            ]),
            C("Tablo 4-13: Herediter amiloidoz", [
                B("**Ailesel Akdeniz ateşi** → **AA**; prekürsör **SAA**.", y="25-26"),
                B("**Familyal amiloidotik nöropatiler** (birçok tip) → **ATTR**; prekürsör **transtiretin**."),
                B("**Sistemik senil amiloidoz** → **ATTR**; prekürsör **transtiretin**."),
            ]),
            C("Tablo 4-13: Lokalize amiloidoz", [
                B("**Senil serebral** (**Alzheimer hastalığı**) → **Aβ**; prekürsör **APP**."),
                B("**Endokrin, medüller tiroid karsinomu** → **A Cal**; prekürsör **kalsitonin**."),
                B("**Endokrin, Langerhans adacıkları** (**tip 2 diyabet**) → **AIAPP**; prekürsör **adacık amiloid peptidi**."),
                B("**İzole atrial amiloidoz** → **AANF**; prekürsör **atrial natriüretik faktör**."),
            ]),
        ],
        [
            C("Resim 4-32: Amiloidoz patogenezi (slayt 14)", [
                B("**Ortak yol**: **katlanmış protein** → **amiloidojenik intermediate** (ör. hatalı katlanmış protein) → monomerler **β kıvrımlı yapı** oluşturmak üzere toplanır → **fibril**."),
                B("**AL**: bilinmeyen (karsinojen?) → **monoklonal B-lenfosit proliferasyonu** → **plazma hücreleri** → **immünglobülin hafif zincirleri** → **sınırlı proteoliz** → **AL protein**."),
                B("**AA**: **kronik inflamasyon** → **makrofaj aktivasyonu** → **interlökin 1 ve 6** → **karaciğer hücreleri** → **SAA protein** → **sınırlı proteoliz** → **AA protein**."),
                B("**ATTR**: **mutasyon** → **mutant transtiretin** → **agregasyon** → **ATTR protein**."),
                B("Şemada AL ve AA **anormal miktarda protein üretimi** başlığı altında; ATTR **normal miktarda mutant protein üretimi** (ör. transtiretin) başlığı altındadır."),
            ]),
            C("Depolanmanın 3 nedeni (özet kutusu, slayt 33)", [
                B("Hatalı katlanma ve kümelenmeye yatkın proteinlerin **aşırı yapımı**."),
                B("Uygun katlanamayan ve kümelenme eğilimindeki proteinleri üreten **mutasyonlar**."),
                B("**Ekstrasellüler proteinlerin bozuk veya yetersiz proteolitik parçalanması**."),
            ]),
        ],
        [
            C("Organ dağılımı (slayt 15-16)", [
                B("**Kronik iltihabi bozukluklara sekonder amiloidoz**: tipik olarak **böbrekler, karaciğer, dalak, lenf nodları, sürrenaller, tiroid** ve diğer birçok doku etkilenir."),
                B("**Primer (AL) amiloidoz**: organ dağılımıyla sekonder tipten tam ayrılamasa da **kalp, GİS, solunum sistemi, periferik sinirler, deri ve dili** daha sık tutar."),
                B("**Herediter sendromlarda** amiloid lokalizasyonu değişkendir."),
                B("**Ailesel Akdeniz ateşi**: amiloidoz **böbrekleri, kan damarlarını, dalağı, solunum sistemini** ve (nadiren) **karaciğeri** tutabilir.", y="25-26"),
            ]),
            C("Makroskopi (slayt 17)", [
                B("Klinik bozukluk ne olursa olsun amiloidoz makroskopik olarak **belirgin olabilir veya olmayabilir**."),
                B("**Küçük miktardaki** birikim, organın kesit yüzeyi **iyot veya sülfürik asitle** (kızıl-kahverengi boyanma) boyanmadan çoğu kez fark edilmez."),
                B("**Daha fazla** birikirse organ sıklıkla **büyümüştür**; doku tipik olarak **balmumu gibi sert kıvamlı, gri**."),
            ]),
            C("Histolojik inceleme (slayt 18)", [
                B("Amiloid birikimi **daima ekstrasellülerdir** ve **hücreler arasında başlar**.", y="24-25"),
                B("Sıklıkla **bazal membranların yakın komşuluğunda** görülür."),
                B("Biriktikçe hücrelere sokulur, zamanla onları **sarıp tahrip eder**."),
                B("**AL tipinde perivasküler ve vasküler** lokalizasyonlar sıktır."),
            ]),
        ],
        [
            C("Tanı: Kongo kırmızısı (slayt 19, 24)", [
                B("Amiloidin histolojik tanısı **boyanma özelliklerine** dayanır; en sık kullanılan teknik **Kongo kırmızısı**: ışık mikroskobunda **pembe-kırmızı**, polarize ışıkta **elma yeşili çift kırma**.",
                  y="21-22 22-23 23-24 24-25",
                  tuzak="“Giemsa / kristal viyole / hematoksilen eozin / Alcian blue / CD3 / CD20” → YANLIŞ (doğru boya Kongo kırmızısı)"),
                B("Kongo kırmızısı amiloid **fibrillere bağlanır** → **kırmızı-yeşil iki renklilik (çift kırma)**; reaksiyon **bütün amiloid tiplerinde**, fibrillerin **çapraz β-kıvrımlı yapısından** dolayı oluşur."),
                B("Slayt 24 (karaciğer görüntüleri): ışık mikroskobunda **pembe-kırmızı**; polarize mikroskopta **yeşil renkli “birefringence”** (ışığı çift kırar)."),
            ]),
            C("Doğrulama ve tip ayrımı (slayt 19-20)", [
                B("Tanının doğrulanması: **elektron mikroskopisinde amorf, oryantasyonsuz, ince fibrillerin** gösterilmesi."),
                B("**AA, AL ve ATTR** amiloid tipleri **spesifik immünhistokimyasal boyanmalarla** ayırt edilebilir.",
                  y="24-25", tuzak="“AA, AL, ATTR amiloid tipleri hematoksilen eozin boyamada tespit edilir” → YANLIŞ"),
            ]),
            C("Boya görselleri (slayt 21-23)", [
                B("Görsel slaytların başlıkları: **Kongo kırmızısı**, **Kristal viyole**, **Sternberg**; ışık/polarize özellikleri **yalnızca Kongo kırmızısı** için yazılmıştır."),
            ]),
            C("Biyopsi ile tanı (slayt 31)", [
                B("Sistemik vakalarda **GİS'in sık tutulması** nedeniyle, şüphelenilen vakalarda **gingival, intestinal ve rektal biyopsiler** tanıya yardımcıdır.", y="24-25"),
            ]),
        ],
        [
            C("Böbrek (slayt 25-26)", [
                B("Böbrek amiloidozu hastalığın **en sık ve en ciddi** özelliğidir."),
                B("Makroskopi: değişmemiş görünebilir veya **anormal büyük, soluk, gri ve sert**; **uzun süreli vakalarda küçülmüş** olabilir."),
                B("Mikroskopi: depolanmalar **ön planda glomerüllerde**; ayrıca **interstisyel peritübüler dokuda** ve **kan damarı duvarlarında**."),
                B("Glomerül: önce **mezangial matriksde fokal** depolanmalar; kapiller yumağın **bazal membranlarında diffüz veya nodüler kalınlaşma**."),
                B("İlerleyince depolanma **kapiller lümene** ilerler → sonunda **vasküler yumağın total obliterasyonu**."),
                B("İnterstisyel peritübüler birikimler sıklıkla **tübüler lümenlerde amorf pembe silendirlerle** (muhtemelen proteinöz) birliktedir."),
                B("**Her boydaki kan damarlarının duvarlarında** birikim görülebilir; çoğu kez belirgin **vasküler daralma** yapar."),
            ]),
            C("Dalak (slayt 27)", [
                B("Orta derecede, hatta şiddetli **dalak büyümesi (200-800 gr)**."),
                B("Bilinmeyen nedenlerle **iki tipten biri** gelişir: **“sago dalağı”**: depolanma **dalak follikülleriyle sınırlı**, makroskopide **tapyoka benzeri granüller**."),
                B("**“Lardaceous dalak”**: başlıca **dalak sinüsleri** etkilenir; büyük **tabaka benzeri** depolanmalarla **dalak pulpasına** uzanır."),
                B("Her iki tipte dalak **sert kıvamlı**; sinüslerdeki kan, balmumu benzeri kırılgan birikimlere **kırmızımsı renk** verir."),
            ]),
        ],
        [
            C("Kalp (slayt 28)", [
                B("Kalp amiloidozu **izole organ tutulumu** ya da **sistemik dağılımın bir parçası** olarak gelişebilir."),
                B("**Sistemik tutulumla** birlikteyse çoğu kez **AL tipi**; **izole tip (senil amiloidoz)** genellikle **yaşlılara özgüdür**."),
                B("Birikimler makroskopide belirgin olmayabilir; **minimal-orta düzeyde kardiyak büyüme** yapabilir."),
                B("**En karakteristik makroskobik bulgu**: özellikle **atrial mesafelerde gri-pembe, çiy benzeri subendokardiyal kabartılar**."),
                B("Histoloji: depolanmalar tipik olarak **miyokardiyal fibriller arasında** başlayarak **miyokard boyunca** bulunur."),
            ]),
            C("Karaciğer (slayt 29)", [
                B("**Masif büyüme (9000 gr'a kadar)**; ileri vakalarda dış ve kesit yüzü ileri derecede **soluk, grimsi ve balmumsu**."),
                B("Birikim ilk olarak **Disse aralığında** ortaya çıkar, sonra **komşu hepatik parankim ve sinüzoidlere** ilerler."),
                B("Sıkışan karaciğer hücreleri **kompresyon atrofisi**ne gider; sonunda hücrelerin yerini **amiloid tabakaları** alır."),
                B("Şiddetli tutulmada bile **normal karaciğer fonksiyonu** korunmuş olabilir."),
            ]),
            C("Diğer organlar (slayt 30-31)", [
                B("Diğer organların amiloidozu genellikle **sistemik hastalıkta** görülür; **sürrenaller, tiroid ve hipofiz** sık tutulum yerleridir."),
                B("Birikim **stroma ve endotelyal hücrelerle ilişkili** başlar, ilerleyerek **parankimal hücrelere** saldırır."),
                B("Bu endokrin organlarda **belirgin fonksiyon bozukluğu yapmaksızın** büyük miktarlarda amiloid bulunabilir."),
                B("**GİS**: amiloid bazen **neoplazmlardan ayırt edilmesi gereken tümöral kitleler** oluşturabilir."),
                B("**Dilde nodüler birikimler → makroglossi**."),
            ]),
            C("Uzun süreli diyaliz: β2-mikroglobulin (slayt 31)", [
                B("β2-mikroglobulin amiloid depolanması en sık **el bileğinin karpal ligamentlerinde** olur → **median sinir kompresyonu** → **karpal tünel sendromu**."),
            ]),
        ],
        [
            C("Amiloidoz sınıflaması: 6 grup (slayt 32)", [
                B("1- **PRİMER**: **AL tipi** amiloid birikimi; kemik iliğinde **plazma hücre artışı**, serum veya idrarda **monoklonal immünglobulinler** bulunabilir.", y="24-25"),
                B("2- **REAKTİF SİSTEMİK**: **AA amiloid**; **kronik inflamasyon** vardır; en sık nedenler **tüberküloz, bronşiektazi, osteomyelit ve RA**."),
                B("3- **AİLESEL-HEREDİTER**: en iyi örnek **FMF** (serozal yüzeylerin iltihabı ile birlikte ateş nöbetleri); **AA amiloid** depolanır.", y="25-26"),
                B("4- **LOKALİZE**: en sık **akciğer, larinks, deri, mesane, dil ve göz** bölgesinde; **AL amiloid**."),
                B("5- **ENDOKRİN**: **tiroidin medüller karsinomu, pankreas adacık tümörleri, feokromasitoma** vb."),
                B("6- **YAŞLANMA AMİLOİDİ**: daha sık **kalpte** geliştiğinden **senil kardiyak amiloidoz** da denir; **transtiretinden** oluşur."),
            ]),
            C("Reaktif sistemik amiloidoz nedenleri (slayt 34)", [
                B("**Tüberküloz** · **kronik osteomyelit** · **bronşiektazi** · **romatoid artrit** · **ülseratif kolit** · **Hodgkin lenfoma** · **FMF** · **kronik deri enfeksiyonları**."),
            ]),
        ],
        [
            C("Özet kutusu: Amiloidoz (slayt 33)", [
                B("Amiloidoz, **erimeyen fibril** şeklinde toplanan hatalı katlanmış proteinlerin **ekstrasellüler depolanmalarıyla** karakterize bir bozukluktur."),
                B("**Lokalize veya sistemik** olabilir; çeşitli primer bozuklukla birlikte görülebilir:"),
                B("**Monoklonal plazma hücre proliferasyonları** (immünglobulin hafif zincirleri) · **RA gibi kronik iltihabi hastalıklar** (akut-faz proteini **amiloid A**) · **Alzheimer** (**amiloid B protein**).", lvl=1),
                B("**Ailesel durumlar** (mutant normal proteinler; ailesel amiloid polinöropatilerinde **transtiretin**) · **dializle ilişkili amiloidoz** (klirensi bozuk **β2-mikroglobulin**).", lvl=1),
                B("Amiloid depolanmaları **doku hasarına** neden olur: hücre ve dokulara **baskı yaparak** normal fonksiyonu bozar; **inflamatuar yanıt uyandırmazlar**."),
            ]),
            C("Hoca'nın slayt sonu soruları (slayt 35-38; slaytta cevap yok)", [
                B("**AA tipi birikim bulunmayan** (sarkoidoz / TBC / FMF / MM / Hodgkin): **multiple myelom (AL tipi)**; TBC, FMF, Hodgkin AA nedenleri listesinde; sarkoidoz listede yok."),
                B("Kongo kırmızısı + polarize ışıkta **sarı-yeşil çift kırınım** beklenen tümör: **tiroidin medüller karsinomu** (endokrin amiloidoz; **A Cal / kalsitonin**)."),
                B("Kronik böbrek yetmezlikli **diyaliz hastasının dirseğindeki** amiloid: **β2-mikroglobulin (Aβ2m)**."),
                B("Amiloidozda **en sık ölüm sebebi** organ tutulumu: **böbrek** (slayt 25: böbrek amiloidozu “en sık ve en ciddi özellik”)."),
            ]),
        ],
    ],
    sorular=[
        Q("25-26", 72, "FMF tanılı hastada barsak perforasyonu; vasküler ve subserozal eozinofilik materyal; Kongo red ve kristal viyole pozitif?",
          "Amiloidoz (AA tipi)",
          "Slayt 16, 32: FMF → AA amiloid · Paradoks emboli, amniyon sıvısı embolisi, mikotik anevrizma, hidroperitoneum değil"),
        Q("24-25", 76, "Amiloidozla ilgili doğru OLMAYAN?",
          "“AA, AL, ATTR amiloid tipleri H&E boyamada tespit edilir”",
          "Tipler spesifik İHK ile ayrılır (s.20) · Doğrular: Kongo red + polarize ışıkta çift kırma · ekstrasellüler · rektal biyopsi · MM'de AL"),
        Q("23-24", 67, "Rektum biyopsisinde amiloid: ışık mikroskobunda pembe-kırmızı, polarize ışıkta elma yeşili veren boya?",
          "Kongo red",
          "Giemsa, kristal viyole, H&E, Alcian blue değil · Kongo kırmızısı: pembe-kırmızı + elma yeşili çift kırma (s.19, 24)"),
        Q("22-23", 67, "Amiloidi gösteren, polarize ışıkta elma yeşili çift kırma gösteren boya?",
          "Kongo red",
          "CD3, CD20 (IHK), kristal viyole, Giemsa değil · s.19: polarize ışıkta elma yeşili çift kırma"),
        Q("21-22", None, "Amiloid birikimi hangi boyayla görüntülenir?",
          "Kongo red (kristal viyole)",
          "Öğrenci hatırlamasından derlenmiş soru · slaytta Kongo kırmızısı (s.19, 24); “Kristal viyole” yalnız görsel başlığı (s.22)"),
    ],
)
