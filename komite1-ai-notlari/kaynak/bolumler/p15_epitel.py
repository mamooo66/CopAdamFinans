# -*- coding: utf-8 -*-
"""Kaynak: Drive › Komite-1 › PDF › Patoloji › 2026-2027(yeni) › Selma Erdoğan Düzcü ›
8-BENİGN EPİTELYAL TÜMORLER (48 slayt) + 9-MALİGN EPİTELYAL TÜMORLER (52 slayt)"""

from yardim import B, C, Q  # noqa: F401

BOLUM = dict(
    key="epitel", baslik="Benign ve Malign Epitelyal Tümörler",
    hoca="Doç. Dr. Selma Erdoğan Düzcü", tarih="13 Ekim", saat="2 saat",
    kaynak="8-BENİGN + 9-MALİGN EPİTELYAL TÜMÖRLER · Doç. Dr. S. E. Düzcü · 2026",
    ozet=["**Son 5 yılın hepsinde soru çıktı**: taşlı yüzük + linitis plastika (25-26) · adenokarsinom = malign epitelyal (24-25) · adenokarsinom = **gland benzeri yapı** (23-24) · lobüler ca → **indian file** (22-23).",
          "22-23 tuzakları: taşlı yüzük **kötü** prognozlu · amiloid **medüller** tiroid ca'da (papillerde psammoma) · anaplastik = **indiferansiye** · keratin incisi **SCC**'de.",
          "Benign şıklar sık çeldirici: **pleomorfik adenom, Warthin, hamartomatöz polip, kondiloma akuminatum, skuamöz papillom, foliküler adenom**."],
    slaytlar=[
        # ------------------------------------------------ BENİGN: polipler
        [
            C("Benign epitelyal tümörler — 3 grup", [
                B("**Polip** · **Papillom** · **Adenom**", y="21-22"),
            ]),
            C("Polipler", [
                B("**Mukoza epitelinden** çıkan tümörlerdir."),
                B("Makroskopik: **saplı** (pediküllü) veya **sapsız**."),
                B("Mikroskopik: **yalın**, **villöz (papiller)**, **adenomatöz**, **adenomyomatöz**, **miks**."),
                B("**Burun, trakea, bronş, mide, barsak ve uterusta** görülür; **tek veya multipl**."),
                B("**Multipl polip en çok kalın barsakta** ve **herediterdir**; polipler **kalın barsakta daha sık**."),
            ]),
            C("Polip — tanım", [
                B("Mukoza yüzeyinden **lümene doğru uzanan**, makroskopik olarak görülebilen, çıkıntı yapmış **benign ya da malign** neoplaziler."),
                B("**Neoplazi dışı** nedenlere (örn. **iltihap**) bağlı da gelişebilir."),
                B("Polipi oluşturan olay **malign tümör** ise → **“polipoid kanser”** terimi daha uygundur."),
            ]),
            C("Peutz-Jeghers sendromu", [
                B("**İnce barsakta hamartomatöz polipler** + **mukokutanöz hiperpigmentasyon**."),
                B("**OD** · **20-30 yaş**."),
                B("**Safra yolları, pankreas ve overlerde** malign tümörler olabilir; **malignite için predispozandır**."),
            ]),
        ],
        [
            C("Jüvenil polip", [
                B("**Genç erişkin, çocuk** ya da **doğuşta** görülür; genelde **tektir**."),
                B("**Jüvenil polipozis sendromunda** çok sayıda olabilir; **kendi kendine kaybolabilir**."),
                B("**Kalın barsakta**, çoğunlukla **rektumda**; **erkeklerde** daha sık."),
                B("**Malignite potansiyeli yoktur**; stromasında **düz kas** da izlenebilir."),
            ]),
            C("Adenomatöz polipler", [
                B("**Familyal** olanlar adenomatöz, papiller ya da mikst; **çocuk ve gençlerde** görülür."),
                B("**Multipldir**, **karsinom insidansı yüksektir**; familyal polipoziste karsinom familyal olmayanlara göre **daha genç yaşta**."),
                B("Tipleri: **tübüler**, **tübülovillöz**, **villöz**."),
                B("Mikroskopi: **epitel altında bezler**; **fibrovasküler kor** görülür."),
                B("**Kalın barsak polipleri genelde adenomatözdür**; **ülserli** olabilir, **malignleşebilir**."),
            ]),
            C("Gardner sendromu", [
                B("**OD** · **kalın barsakta polipler**."),
                B("**İskelet sistemi (osteom)** + **bağ dokusunda multipl tümörler**."),
            ]),
            C("Villöz (papilli) polipler", [
                B("**Çapça büyük**, çoğunlukla **sapsız**; yüzeylerinde **yarıklar**."),
                B("Üzeri **silindirik epitelle** döşeli; **malignleşme oranı yüksek**."),
            ]),
            C("Poliplerde ikincil değişiklikler", [
                B("**İltihap ve ülserleşme**; **endoservikal poliplerde** sarkma, ülserleşme, **metaplaziler**."),
                B("Bazı poliplerde **siklik değişiklikler** — örn. **endometrial polipler**."),
            ]),
        ],
        # ------------------------------------------------ BENİGN: papillomlar
        [
            C("Papillom (ÇKYE ve değişici örtü epitelinin selim tümörleri)", [
                B("Bu tümörlerin genel adı **papillom**dur."),
                B("Tanım: epitel yüzeyinden **dışarı doğru**, makroskopik ya da mikroskopik **parmaksı çıkıntılar** oluşturan benign epitelyal tümör."),
            ]),
            C("ÇKYE kökenli papillomlar", [
                B("**Deri, ağız, özefagus, vagen ve serviksten** çıkar; **metaplazi zemininde** de çıkabilir."),
                B("Makroskopi: **saplı veya sapsız**."),
                B("Mikroskopi: bağ dokusundan oluşan parmak gibi çıkıntıların üstünü **ÇKYE** örter; bağ dokuda **damar ve sinirler**."),
                B("**Bazal membran sağlam**, hücre sıraları **düzgün**."),
                B("Travma ve enfeksiyonla **ülser ve iltihabi infiltrat** (sekonder değişiklik) gelişebilir."),
                B("Derinden çıkanlarda yüzeyde kalın korni tabakası → **hiperkeratozlu papillom**."),
                B("Spinal tabaka artmışsa → **akantotik papillom**; keratinde nükleus artıkları → **parakeratoz gösteren papillom**."),
            ]),
            C("Skuamöz hücreli papillom · verruka", [
                B("Skuamöz hücreli papillomda **hiperkeratoz ve akantoz** belirgindir."),
                B("**Verruka vulgaris** (**siğil**): **viral orijinli**; **kendi kendine kaybolabilir**."),
                B("**Çocuk ve gençlerde el ve parmaklarda**; **virüs partikülleri** görülebilir; bazen ayakta → **verruka plantaris**."),
            ]),
            C("Kondiloma akuminatum", [
                B("**Anüs ve genital bölgede** deri ya da mukozadan çıkan **viral orijinli** lezyon; bir **papillomdur**."),
                B("**Akantoz**, **fazla mitoz**; epitel sıraları **düzgün**; **karnabahara** benzer."),
            ]),
        ],
        [
            C("Seboreik keratoz", [
                B("**Bazal hücreli papillom** olarak da bilinir."),
                B("**İleri yaşlarda deride** görülür; **bazal hücrelerden** oluşur."),
            ]),
            C("Ürotelyal papillom", [
                B("İdrar yollarında **en sık mesanede**."),
                B("**Villöz** görünümlü; **kolay yırtılır ve kanar**; çıkarıldıktan sonra **nüks** edebilir."),
            ]),
            # ------------------------------------------------ BENİGN: adenomlar
            C("Adenom (bez epitelinden çıkan selim tümörler)", [
                B("Tanım: **glandüler dizilim gösteren** ya da **gland (bez) epitelinden köken alan ancak gland yapısı göstermeyen** benign tümörler."),
                B("**Gudde (bez) yapan organlardan** çıkar; bazen **kistik** oluşumlar yapar."),
                B("**Asinüs**, küçük yuvalar halinde **solid kitle** ve **trabeküller** oluşturur; salgı **asinüs lümeninde** birikir."),
                B("**Mukus yapanlar dışında** salgı olmaz ya da çok az olur."),
                B("Makroskopi: **birkaç mm – birkaç cm**; bazen **kapsüllü**, bazen **kapsülsüz**."),
            ]),
            C("Asinüs (halka) yapan adenomlar", [
                B("Halka yapan **adenoid** oluşumlar; **yalın** veya **papiller** adenom biçiminde."),
                B("**Yalın adenom (foliküler adenom)**: **tiroidde** sık; içi **kolloidle** dolu; **kapsüllü**; çevre normal dokuda **atrofi**."),
                B("**Papiller adenom**: **böbrek, tiroid ve ter bezlerinden**; bez boşluklarının içine doğru **papiller yapılar**."),
            ]),
        ],
        [
            C("Solid nodüler adenom", [
                B("Mikroskopik olarak **küçük solid kitleler**; **gland oluşumu yoktur** (hücreler bazen papiller yapı yapabilir)."),
                B("**Pankreas Langerhans adacıkları** ve **hipofiz ön lobundan** çıkar — **pankreas ve hipofiz adenomları fonksiyoneldir**."),
                B("**Sürrenal korteks adenomu** ve **karaciğer adenomları** da bu şekildedir."),
                B("Boyut arttıkça etrafa bası ile **kapsül** oluşur."),
            ]),
            C("Kistik adenom", [
                B("Adenomun **boşaltma kanalları ile bağlantısı yoksa** kistler oluşur; **en sık overlerde**."),
                B("Sekresyonla boşluklar genişler, **asinüs epiteli yassılaşır** → kistik adenom."),
                B("**Apokrin adenomlar**: **dış kulak yolu ve vulvadan** çıkar."),
            ]),
            C("Trabeküler ve tübüler adenom", [
                B("**Trabeküler**: **karaciğer ve tiroidde**; bağ dokusu içinde **epitelden oluşan trabeküller**."),
                B("**Tübüler**: **meme** ve **Sertoli hücrelerinden** çıkar."),
            ]),
        ],
        [
            C("Pleomorfik adenom", [
                B("**Tükürük**, bazen de **ter bezlerinden**; **en sık parotiste**."),
                B("Makro: bez çok büyür, biçimi bozulur, **nodüllü**; etrafı **kesintili bir kapsülle** çevrili."),
                B("Beyaz, sert; yer yer homojen parlak, yer yer **jelatin gibi yumuşak**; **kanama ve kistik alanlar** olabilir."),
                B("Mikro: küçük halkalar, trabeküler yapılar, solid kitleler; **küçük epitel hücreleri + myoepitel hücreleri**."),
                B("**Kıkırdak benzeri stroma**; **kıkırdak ve embriyonel bağ dokusuna** benzer alanlar → **“pleomorfik” adenom** adı."),
                B("Kapsülden uzanan **fibröz bantlar** tümörü **nodüllere** ayırır."),
            ]),
            C("Adenolenfoma (Warthin tümörü)", [
                B("**Tükürük bezi** tümörü."),
                B("**Büyük eozinofil hücrelerden** oluşan halkalar, **kist benzeri** oluşumlar ve **papiller** yapılar."),
                B("Stromada **yaygın lenfosit infiltrasyonu**."),
            ]),
            C("Oksifilik adenom (onkositoma)", [
                B("**Büyük eozinofil, hepatosit benzeri** hücreler."),
                B("**Tükürük bezleri, parotis, tiroid ve paratiroidden** çıkar."),
                B("Solid kitle ve kordonlar, bazen **asiner** yapılar; hücreler **mitokondriden zengin**; tümör **stromadan fakir**."),
            ]),
        ],
        # ------------------------------------------------ MALİGN: genel
        [
            C("Malign (habis) epitelyal tümörler = KARSİNOM (CA)", [
                B("**En sık görülen** tümörlerdir."),
                B("Benign epitelyal tümörlerden farkı: **normal dokuyu işgal ederek hasar** oluşturmaları ve **metastaz** yapmaları."),
                B("Makroskopik ve mikroskopik görünümleri benign tümörlerden farklı."),
                B("Kesit yüzeyi hücresel elemandan zengin → **gri-beyaz**, **düzensiz sınırlı**."),
            ]),
            C("Genel özellikler", [
                B("Normal dokuda **hasar**; **pleomorfizm ve anaplazi**."),
                B("**Yüksek gelişme hızı**: mitotik hız ve **atipik mitoz** varlığı."),
                B("**Metastaz** yapar."),
                B("Stroma: **nekroz ve kanama** alanları, **desmoplazi**."),
            ]),
            C("Mukoza bezlerinden çıkan karsinomlar = adenokarsinom", [
                B("**Salgı yapan epitel ve altındaki bezlerden** çıkar → **adenokarsinom**.", y="24-25 23-24"),
                B("Makroskopik: **polipoid**, **diffüz infiltran**, **solid**, **ülseröz**, **vejetan**, **karma (mikst)**."),
                B("Ayrıca **medüller**, **skiröz** ve **jelatinöz** olarak da ayrılabilir."),
            ]),
        ],
        [
            C("Adenokarsinom — makroskopik tipler", [
                B("**Polipoid karsinom**: boşluğa doğru uzanmış **mantar gibi** kitleler."),
                B("**Vejetan karsinom**: çok sayıda ince polipoid oluşum; **karnabahara** benzer; **mide, barsak, uterus ve özefagusta** sık."),
                B("**Nodüler karsinom**: büyük, üzeri düzgün nodüler yapılar; **büyük bir tabanla** mukozaya yapışık; **mide ve barsakta** daha sık."),
                B("**İnfiltran karsinom**: **diffüz** tip; mukoza altındaki dokuya yapışık; **daha çok midede**; **mataraya** benzediği için **“linitis plastika”**.", y="25-26"),
                B("İnfiltran karsinomda **kas tabakasında kontraksiyon olmaz**.", lvl=1),
                B("**Ülseröz karsinom**: geniş kenarlı, **tabanı sert, kalın** ülser; **midede** sık."),
                B("**Medüller karsinom**: **yumuşak** karsinomlar."),
                B("Jelatin gibi parlak madde → **jelatinöz** · çok sert → **skiröz** · birkaç tip bir arada → **karma (miks)** karsinom."),
            ]),
            C("Mikroskopi", [
                B("Değişik mikroskopileri vardır; **bez yapısı bulunduran doku/organların tümünden** çıkabilir."),
                B("Ön planda: **asiner**, **papiller**, **lobüler**, **mukoid**, **taşlı yüzük hücreli**, az stromalı nodüler (**medüller**), geniş-yaygın stromalı (**skiröz**), **saydam hücreli**, **indiferansiye hücreli**, **karma**."),
            ]),
        ],
        # ------------------------------------------------ MALİGN: mikroskopik tipler
        [
            C("Asiner karsinom", [
                B("**Foliküler karsinom** da denir (özellikle **tiroidde**); **asiner histolojili** organlardan çıkar.", y="21-22"),
                B("**Düzensiz, bir kısmı tamamlanmamış halkalar**; halkalar **alçak ve yüksek silindirik** hücrelerle döşeli."),
                B("**Adenomdan ayrımı zordur** → tanıda **invazyon görülmesi önemli**."),
                B("**Uterus, safra kesesi, mide ve tiroidde** görülür."),
            ]),
            C("Papiller adenokarsinom", [
                B("Papil benzeri yapılar; papilin ortası **gevşek bağ dokusu** — **fibrovasküler kor** görmek önemli."),
                B("Burada **kalsifikasyonlar (psammoma cisimcikleri)** görülebilir."),
                B("**Tiroid papiller karsinomunda** sık görülür."),
            ]),
            C("Lobüler karsinom", [
                B("**Meme ve pankreasta**; aynı veya **ayrı memelerde** olabilir."),
                B("Hücreler **indian file (tesbih dizisi)** görüntüsü oluşturur.", y="22-23"),
                B("(Görsel notu) **Pembe kolajenizasyon** alanları ne kadar fazlaysa tümör **o kadar serttir**."),
            ]),
            C("Müsinöz karsinom", [
                B("**Kolloid** veya **jelatinöz** karsinom da denir; **GİS, pankreas, safra kesesi ve memede**."),
                B("Hücreler **mukus salgılar**; mukus stromaya yayılıp karsinom hücre ve kordonlarını çevreleyen **gölcükler** oluşturur."),
                B("**Prognoz kötü** — ancak **memedeki müsinöz karsinomun prognozu iyi**."),
            ]),
        ],
        [
            C("Taşlı yüzük hücreli karsinom (signet ring cell)", [
                B("Slayt örneği: **kolonda az diferansiye (müsinöz) adenokarsinom**."),
                B("Epitel hücreleri **içinde mukus**; **nükleus bir kenara itilmiş**; HE'de mukus **saydam** → **taşlı yüzük** görüntüsü.", y="25-26"),
                B("**Prognozu mukoid adeno ca'dan daha kötü**.", y="22-23",
                  tuzak="“Taşlı yüzük hücreli karsinomlar çok iyi prognozludur” → YANLIŞ"),
            ]),
            C("Medüller karsinom", [
                B("**Meme ve tiroidde**; **yavaş gidişli**."),
                B("**Tiroidde** tümörde **amiloid** birikimi görülebilir.", y="22-23",
                  tuzak="“Tiroid papiller karsinomunda amiloid birikimi karakteristiktir” → YANLIŞ"),
                B("**Memede** stromada **lenfosit infiltrasyonu**."),
            ]),
            C("Skiröz karsinom", [
                B("Stromada **bağ doku artar** → tümörün olduğu bölge **sertleşir**."),
                B("**En sık memede** → **meme başı içeri çekilir**."),
                B("**Mide ve barsakta** da görülür; midede **fibröz dokuda saçılmış hücreler**; **pilor ve barsakta darlık** yapar."),
            ]),
            C("Şeffaf hücreli (clear cell) karsinom", [
                B("**Vajina, serviks ve endometriumda** görülür."),
                B("Geniş **berrak sitoplazma**; **glikojen** içeriğinden ötürü **PAS pozitif**."),
            ]),
            C("İndiferansiye tümör = anaplastik tümör", [
                B("Az ya da çok **solid kitleler**; **organoid yapı meydana getirmez**.", y="22-23",
                  tuzak="“Anaplastik tümörler atipi göstermeyen, iyi diferansiye tümörlerdir” → YANLIŞ"),
                B("Genellikle birbiriyle **bağlantı oluşturmayan** hücreler; **küçük** veya **büyük hücreli**."),
                B("**Küçük hücreliler lenfomaya benzer**; **tümör dev hücreleri** görülebilir."),
            ]),
        ],
        # ------------------------------------------------ MALİGN: ÇKYE karsinomları
        [
            C("Çok katlı yassı epitel (ÇKYE) karsinomları", [
                B("**Deriden** ve **ÇKYE ile örtülü mukozalardan** çıkar."),
                B("**Mide, barsak, safra kesesi, trakea ve bronşlardan** **metaplazi** sonucu gelişebilir."),
                B("Deride **en çok 50-60 yaş**; **erkeklerde** daha sık."),
                B("Makro: **yüzde** sık; **el ve ayaklarda** da görülür."),
            ]),
            C("ÇKYE ca — makroskopik tipler", [
                B("**Papiller**: papillomdan çıkabilir; **oldukça diferansiye**; **prognoz iyi**."),
                B("**Vejetan**: daha **hızlı seyirli**; yüzeyde büyük çıkıntılar."),
                B("**Nodüler**: kabarık, üzeri düz, sert, tek/çok kitle; gidişi **hızlı**, kısa sürede **infiltrasyonla** yayılır."),
                B("**Ülseröz**: geniş ülserler, **hızlı gidişli** · **Mikst**: kombine tip."),
            ]),
            C("ÇKYE ca — mikroskopik tipler", [
                B("**İntraepitelyal karsinom (karsinoma in situ)** · **infiltran karsinom** · **indiferansiye karsinom**."),
                B("**Karsinoma in situ**: tümör **bazal tabakayı geçmez**; sıralama bozulmuştur (**polarite bozukluğu**)."),
            ]),
            C("İnfiltran karsinom (skuamöz hücreli karsinom)", [
                B("**Akantoz**, **polarite kaybı**, **bazal tabakada bozulma**."),
                B("Tümör hücreleri **subepitelyal alana ve derinlere** ilerler; düzensiz kitle ve kordonlar."),
                B("**Konsantrik keratinizasyon odakları (glob kornea)** veya **keratin incileri** oluşur.", y="22-23",
                  tuzak="“Adenokarsinomlarda keratin yapımı görülür” → YANLIŞ"),
            ]),
        ],
        [
            C("İndiferansiye karsinom (ÇKYE)", [
                B("Hücreler **keratin yapamaz**; **glob kornea görülmez**."),
                B("**Spinal hücrelerce** oluşturulur fakat **diferansiasyon tanınamaz**."),
                B("Hücrelerin çap, şekil ve boyanmaları farklı; **çok sayıda mitoz**; **tümör dev hücreleri** olabilir."),
            ]),
            C("ÇKYE karsinom özel tipleri", [
                B("**Lenfoepitelyoma**: **lenfoid doku üzerindeki epitelden**; **az diferansiye**; **lenfositlerle karıştırılır**."),
                B("**Fuziform hücreli karsinom**: yassı hücreler **fuziform** şekil alır; **indiferansiye** hücreler; **sarkom ve melanoma** benzer."),
                B("Fuziform hücreli karsinom **malign mezenkimal tümörlerle karışabilir**.", lvl=1),
                B("**Verrüköz karsinom**: **larinks ve ağızda** daha sık; **prognozu iyi**."),
            ]),
            C("Bazal hücreli karsinom (BCC)", [
                B("**Lokal destrüksiyon** yapar; **malign olmasına rağmen metastaz yapmaz**."),
                B("**Sadece derinin bazal tabakasından** çıkar; **kıl foliküllerinden** de çıkabilir."),
                B("**Yüz ve üst dudak** bölgesinde daha sık; **ileri yaşta**; **güneşe maruz** bölgelerde gelişir; **iyi seyirli**."),
                B("Makro: **tek ya da multipl**; lokal destrüksiyon."),
            ]),
            C("BCC mikroskopi", [
                B("**Poligonal**, bazen **fuziform** hücreler; **mitoz** görülür; tümör **epitelin bazal tabakası ile bağlantılı**."),
                B("Kitle ve kordonların çevresinde hücreler **dikey dizilir** (bazal tabakaya benzer) → **palizatlaşma (çit şeklinde dizilim)**."),
                B("**Solid, kistik ve adenoid** yapılar; bazen **melaninden zengin** (**malign melanoma** benzer)."),
                B("Bazen küçük solid, multipl kitleler → **süperfisyel multisentrik BCC**."),
                B("Diğer görsel örnekler: **vulvada skuamöz hücreli karsinom**, **uterus endometriumunda adenokarsinom**."),
            ]),
        ],
    ],
    sorular=[
        Q("25-26", 77, "Tüm mide duvarını kalınlaştırmış, linitis plastika; müsin nedeniyle çekirdeği kenara itilmiş malign epitelyal tm?",
          "Taşlı yüzük hücreli karsinom", "Skuamöz papillom, Warthin, SCC, foliküler adenom değil"),
        Q("24-25", 81, "Malign epitelyal tümörler arasında yer alan?", "Adenokarsinom",
          "Pleomorfik adenom, hamartomatöz polip, kondiloma akuminatum, Warthin benign"),
        Q("23-24", 74, "Midede adenokarsinom morfolojisini gösteren özellik?", "Tümör hücrelerinin gland benzeri yapı oluşturması",
          "Büyük nükleus, muskularis invazyonu, pembe sitoplazma, belirgin nükleol değil · PDF: adenoca bez epitelinden çıkar"),
        Q("22-23", 70, "Malign epitelyal tümörlerle ilgili doğru olan?",
          "Lobüler karsinomlarda hücreler indian file (tesbih dizisi) oluşturabilir",
          "Çeldiriciler: taşlı yüzük iyi prognoz · papiller tiroid ca'da amiloid · anaplastik iyi diferansiye · adenoca'da keratin"),
        Q("21-22", None, "Hangisi epitelyal kanser değildir? (polip, papillom, adenom, adenokarsinom, ÇKYE ca)",
          "Benign olanlar (polip/papillom/adenom) — kanser = karsinom", "Öğrenci hatırlamasından; kesin şık bilinmiyor"),
        Q("21-22", None, "Hangisi malign tümördür?", "Asiner karsinom",
          "Neoplazi bölümünde sayıldı · asiner (foliküler) karsinom bu dersin malign epitelyal tümörlerinden", ref=True),
    ],
)
