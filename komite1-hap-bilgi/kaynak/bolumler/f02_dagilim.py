# -*- coding: utf-8 -*-
"""Kaynak: Drive › Komite-1 › PDF › Farmakoloji › 2026-2027(yeni) › Akif Hakan Kurt › 2-İlaçların Dağılımı (24 slayt)"""

from yardim import B, C, Q  # noqa: F401

BOLUM = dict(
    key="dagilim", baslik="İlaçların Dağılımı",
    hoca="Prof. Dr. Akif Hakan Kurt", tarih="22 Eylül", saat="ADME · 4 saat",
    kaynak="2-İlaçların Dağılımı · Prof. Dr. A. H. Kurt · 2026",
    ozet=["22-23'ten 25-26'ya **her yıl 1 soru**, hepsi aynı kalıp: “İlaçların dağılımı ile ilgili hangisi doğru / yanlıştır?”. 21-22'de **sanal dağılım hacmi** sorusu.",
          "Hep aynı **çeldiriciler**: BOS'ta **pasif / aktif ters yazılması**, albumine **bazik** ilaç, etki yeri göstergesi olarak **bağlı** fraksiyon, **non-iyonize** ortamda toplanma, sekestrasyonda **küçük Vd**, kalp glikozidi → **tiroid**.",
          "Doğru şıklar: albumin = **asidik**, serbest fraksiyon = **gösterge**, glikozidler = **kalp-böbrek-çizgili kas-yağ**, morfin / heroin = **mide suyu**, tiopental = **redistribüsyon**, opioid → **fetusta solunum depresyonu**."],
    slaytlar=[
        [
            C("Dağılım — tanım", [
                B("**Farmakokinetiğin dört ana süreci**: Absorbsiyon → **Dağılım** → Metabolizma (Biyotransformasyon) → Eliminasyon (**ADME**)."),
                B("**İlaçların dağılımı**: absorbsiyon sonucu kana geçen ilacın kapillerlerden damar dışına (genellikle **pasif diffüzyon** ile) geçerek **interstisyel sıvıya** dağılmasıdır."),
                B("İlaçlar başta **plazma proteinleri** olmak üzere hücre dışı ve içinde çeşitli makromoleküllere ve yapılara bağlanabildiğinden **dağılım pek çok ilaç için homojen değildir**.", y="23-24"),
            ]),
            C("Fizyolojik sıvı kompartmanları", [
                B("**Plazma**: %4 (3-3,5 litre)"),
                B("**İnterstisyel sıvı** kompartmanı: %13 (9 litre)"),
                B("**İntraselüler sıvı** kompartmanı: %41 (29 litre)"),
                B("**Plazma + interstisyel** sıvı kompartmanı birlikte **ekstrasellüler sıvıyı** oluşturur."),
            ]),
            C("Kompartmanlara göre dağılan ilaçlar", [
                B("**Sadece plazmada**: yüksek molekül ağırlıklı polisakkaritler olan **dekstranlar**, **heparin, varfarin, süramin, Evans mavisi**."),
                B("**Bütün sıvı kompartmanlarına**: bazı ufak, iyonize olmayan, plazma proteinlerine az bağlanan ilaçlar — **alkol, antipirin, üre**."),
                B("İnsanda **İV 1 g antipirin** ile **total vücut sıvısı hacmi** ölçülebilir.", lvl=1),
                B("**Sadece ekstraselüler sıvıda**: **tübokürarin, gentamisin, karbenisilin** — hidrofilik olduklarından hücre içine giremezler."),
            ]),
            C("Kompartman hacmi ölçüm yöntemleri", [
                B("**Plazma hacmi**: Evans mavisi, radyoaktif albümin · **Ekstraselüler sıvı hacmi**: İnülin"),
                B("**İntraselüler sıvı hacmi**: aminopirin, tritium oksid, döteryum oksid · **Kırmızı hücre völümü**: işaretli eritrositler"),
            ]),
        ],
        [
            C("Organ kanlanması", [
                B("Özel durumlar dışında ilaçların dağılımı **heterojendir**."),
                B("**Kalp, akciğerler, böbrekler, karaciğer** gibi **fazla kanlanan** organlara geçiş **hızlıdır**.", y="22-23"),
                B("**Yağ dokusu, kemikler, iskelet kasları** gibi **az kanlanan** organlara geçiş **yavaş ve geç** olur."),
            ]),
            C("Albümin", [
                B("**Özellikle asidik ilaçlar** yüksek oranda bağlanır.", y="23-24 24-25 25-26", tuzak="“Albumine bazik ilaçlar yüksek oranda bağlanır” → YANLIŞ"),
                B("**Kısıtlı bağlanma noktaları** içerir; belirli bir noktaya yapıları farklı olan ilaçlar bağlanabilir."),
                B("**Afinitesi yüksek** olan, düşük olanı bağlanma noktasından **kovabilir**."),
            ]),
            C("α1-asid glikoprotein", [
                B("İlaç moleküllerini bağlayan **2. önemli makromolekül**; **akut faz proteini**, **KC'de** yapılır."),
                B("**Bazik ilaçları** bağlayan başlıca proteindir (dipiridamol, kinidin, imipramin, propranolol vs.)."),
                B("Düzeyi bireylerarasında **fazlaca değişkenlik** gösterir."),
            ]),
            C("Proteine göre bağlanan ilaçlara örnekler", [
                B("**α1-asid glikoproteine**: dipiridamol, kinidin, propranolol, prazosin, lidokain, verapamil, pindolol, imipramin, klorpromazin."),
                B("**Lipoproteinlere**: sikloserin (DDL), imipramin, kinidin, klorpromazin, tetrasiklin."),
                B("**Gama-globülinlere**: tubokürarin, pankuronyum, morfin, kodein."),
            ]),
        ],
        [
            C("Bağlanmanın özellikleri", [
                B("İlaçların protein ve moleküllere **bağlanması reversibldir**."),
                B("Afinite (Ka) yerine **disosiasyon sabitesi (Kd)** kullanımı adet olmuştur: **Kd = 1/Ka = k2/k1**."),
                B("Bağlanmada rol alabilen bağ türleri: **hidrojen bağları, iyonik bağlar, van der Waals bağları** — bunlardan biri veya birkaçı rol alabilir."),
            ]),
            C("Bağlanma oranı şunlara bağlıdır", [
                B("**Protein konsantrasyonu** · **ilaç konsantrasyonu** · proteindeki **ilaç bağlanma yerlerinin sayısı** · bu yerlerin **ilaca afinitesi**."),
            ]),
            C("Doygunluk", [
                B("İlaç bağlanması terapötik konsantrasyonlarda **doygunluktan hayli uzaktır (%1'in altı)**."),
                B("Az sayıda ilacın (**aspirin, dizopiramit, kinidin, prednizolon** vs.) plazma proteinlerindeki bağlanma bölgeleri terapötik konsantrasyonlarda önemli ölçüde (**%50-60**) doyurulmuştur."),
                B("Böyle ilaçlarda **dozun artırılması serbest ilaç fraksiyonunu fazlaca artırır**."),
            ]),
        ],
        [
            C("Kan proteinlerine bağlanma % — güçlü bağlananlar", [
                B("**%99**: dikomarol, varfarin, fenilbutazon, naproksen"),
                B("**%98**: furosemid, tolbutamid · **%97**: indometasin · **%96**: imipramin · **%95**: klotiazid"),
                B("**%93**: probenesid · **%89**: rifampisin · **%81**: salisilik asid"),
            ]),
            C("Kan proteinlerine bağlanma % — orta derecede bağlananlar", [
                B("Kinidin **75** · kloramfenikol **70** · metotreksat **63** · aspirin **61** · teofilin **59** · penisilin G **52** · sülfadiazin **45** · streptomisin **35**"),
            ]),
            C("Kan proteinlerine bağlanma % — zayıf bağlananlar", [
                B("Morfin **35** · oksitetrasiklin **31** · digoksin **29** · tetrasiklin **24** · amfetamin **22** · ampisilin **13** · gentamisin **10** · parasetamol **4** · izoniazid **0** · allopurinol **0**"),
            ]),
        ],
        [
            C("Hastalıklarda protein bağlanmasının değişmesi — albumin", [
                B("**Azalma**: yaş (yeni doğan, yaşlılık), yanıklar, siroz, cerrahi girişim, enteropatiler, gebelik, nefrotik sendrom."),
                B("**Artış**: hipotiroidizm, nörolojik hastalıklar."),
            ]),
            C("α1-asid glikoprotein", [
                B("**Azalma**: yaş (yeni doğan), ağır siroz, oral kontraseptifler, gebelik, nefrotik sendrom."),
                B("**Artış**: yaş (yaşlılık), kanser, inflamasyon, miyokard infarktüsü, infeksiyonlar, obesite, romatoid artrit, böbrek yetmezliği."),
            ]),
            C("Lipoproteinler", [
                B("**Azalma**: hipertiroidizm, malnutrisyon · **Artış**: hipotiroidizm, alkolizm."),
            ]),
            C("Plazmada bağlı ve serbest ilaç fraksiyonları", [
                B("**Yalnızca serbest** ilaç molekülleri kapillerlerden ekstrasellüler sıvıya (bu arada **etki yerine**) geçebilir."),
                B("İlacın etkilediği yapıdaki konsantrasyonunun **yakın göstergesi** (dolayısıyla **ilaç etkisinin ölçüsü**) plazmadaki **serbest ilaç fraksiyonudur**.", y="24-25 25-26", tuzak="“…yakın göstergesi plazmadaki bağlı ilaç fraksiyonudur” → YANLIŞ"),
                B("**Bağlı kısım** kanda **ilaç deposu / rezervuarı** görevi yapar: serbest moleküller uzaklaştıkça yenisi serbestleşir, **etki süresi uzar**."),
                B("**Sadece serbest** ilaç fraksiyonları **glomerüler filtrasyona** uğrar."),
            ]),
        ],
        [
            C("Dağılım hızı — ilaç veya doku ile ilgili dört faktöre bağlıdır", [
                B("**Difüzyon hızı**: **lipofilik ve az iyonize**, ufak moleküllerde diffüzyon hızı **yüksektir**.", y="22-23"),
                B("**Doku perfüzyon hızı**: **fazla kanlanan dokuya geçiş hızlıdır**; tersi de doğrudur.", y="22-23"),
                B("**İlacın doku komponentlerine afinitesi**: dokunun kandan ilaç çekme (**ekstraksiyon**) kapasitesidir."),
                B("**Plazma proteinlerine bağlanma**: bağlanma arttıkça geçiş hızı **azalır**."),
            ]),
            C("İlaçların santral sinir sistemine geçişi", [
                B("Beyin, ilaç etkisine karşı kendini koruyacak bir yapıya sahiptir (**kan-beyin engeli**).", y="22-23"),
                B("**SSS'ni etkileyen ilaçlar fazla lipofilik** bileşiklerdir."),
            ]),
            C("Kan-beyin engelinin permeabilitesi", [
                B("**Gevşetip permeabiliteyi artıranlar**: **ansefalit, menenjit**, beyne **radyoterapi**, beyin arteri içine **hipertonik solüsyon** injeksiyonu, **yüksek konsantrasyonda alkol**, **sitotoksik ilaçlar**."),
                B("**Glukokortikoidler** ise artmış permeabiliteyi **azaltırlar**."),
            ]),
        ],
        [
            C("Kan-beyin engeli bulunmayan bölgeler", [
                B("**Area postrema** (4. ventrikül tabanında) · **eminentia media** (3. ventrikül çevresinde) · **subfornikal organ** (3. ventrikül çevresinde) · **nörohipofiz** · **supraoptik krista** · **epifiz**."),
            ]),
            C("Kan-beyin engelinin yapısı", [
                B("Endotel hücreleri arasında **porus yoktur (tight junction)**."),
                B("Endotelin altındaki **bazal membran deliksizdir**; **tek sıra astrosit** ile sarılmıştır."),
                B("Endotel luminal membranında **p-glikoproteinler (efflux)** bulunur."),
            ]),
            C("İlaçların BOS'a geçişi", [
                B("BOS'un oluştuğu çeper **sıkı kavşaklı endotel tabakası** ve **tek sıralı koroid epitelinden** oluşur (**kan-BOS engeli**)."),
                B("Bu yapı **sadece lipofilik maddelerin** geçişine uygundur: **lipofilik ilaçlar pasif difüzyonla**, **iyonize bazı ilaçlar** ise **aktif transportla** BOS içine girerler.", y="24-25 25-26", tuzak="“İyonize ilaçlar pasif difüzyonla, lipofilik ilaçlar ise aktif transportla BOS içine girerler” → YANLIŞ"),
                B("**Akut menenjitte** kapiller permeabilite artışı nedeniyle ilaç BOS'a girebilir."),
                B("**Kronik dönemde** permeabilite azaldığından ilacı **intratekal veya intraventriküler** vermek gerekebilir."),
            ]),
        ],
        [
            C("Sekestrasyon", [
                B("İlaçların dokularda bazı hücre içi veya hücre dışı yapılara **sıkı şekilde bağlanmalarıdır**; dokular arasında **eşitsiz dağılıma** yol açar."),
                B("Dokulara bağlanma **ilaç rezervuarı (deposu)** görevi yapabilir."),
                B("Tedavi başlangıcında verilen ilacın büyük kısmı depolara gideceğinden **etki geç başlayabilir** (**amiodaron** gibi) → **yükleme dozu** gerekebilir."),
            ]),
            C("Sekestrasyon örnekleri", [
                B("**İmipramin ve SSRI'lar** — akciğerlerde."),
                B("**Tetrasiklinler** — kalsiyumla şelasyon yaparak **kemik ve dişlerde**."),
                B("**Kalp glikozidleri** — **kalp, böbrek, çizgili kas, yağ dokusu, karaciğer**.", y="24-25 25-26", tuzak="“Kalp glikozidleri tiroid bezinde birikebilir” → YANLIŞ"),
                B("**İyod ve iyodürler** — **tiroid bezinde** birikebilir.", y="25-26"),
            ]),
            C("Redistribüsyon (yeniden dağılım)", [
                B("**Fazla liposolübl** maddeler (**genel anestezikler, tiopental**) alındıklarında başlangıçta **beyin, kalp, böbrek** gibi **fazla kanlanan** dokularda toplanırlar.", y="23-24"),
                B("Daha sonra **daha az kanlanan yağ dokusu, kas dokusu** gibi dokulara çekilip toplanırlar → başlangıçtakinden **farklı yeni bir dağılım kalıbı**."),
                B("Redistribüsyon bu ilaçların **etki yerlerinden uzaklaşmasına** ve **etkinin sona ermesine** neden olur."),
            ]),
        ],
        [
            C("İyon tuzağı", [
                B("Pasif diffüzyona uygun bir membranla ayrılmış iki kompartımanda **pH farkı** varsa, ilaç **daha fazla iyonize olmasına uygun olan kompartımanda toplanma** eğilimindedir.", y="22-23 23-24", tuzak="“İlaçlar çoğu kez non-iyonize halde bulunacakları ortamda toplanma eğilimindedir” → YANLIŞ"),
                B("**Non-iyonize kısımlar** membrandan geçebildiği için her iki kompartımanda **denge** haline ulaşır."),
                B("Böylece **asidik ilaçlar pH'sı daha yüksek** olan tarafta konsantre olurlar."),
                B("**Bazik ilaçlar** hücre içine (**pH 7,0**) hücre dışından (**pH 7,4**) daha fazla girerler."),
                B("**Bazik ilaçlar mide suyunda** toplanma eğilimi gösterirler (**morfin, heroin**).", y="24-25"),
            ]),
            C("İlaçların plasentadan fetusa geçişi", [
                B("**Liposoluble, non-iyonize** ilaç molekülleri kolayca plasentadan fetusa geçebilir.", y="22-23"),
                B("Doğum eylemi sırasında gebeye uygulanan **genel anestezikler ve opioid analjezikler** kolayca plasentayı geçerek **fetusta solunum depresyonuna** neden olabilir.", y="25-26"),
                B("Plasentada az sayıda ilacın **villus kapillerlerine** sokulmasını önleyen **p-glikoprotein** de bulunur; aynı sistem **beyin kapiller hücrelerinin lumene bakan kısımlarında** bulunur."),
            ]),
        ],
        [
            C("Sanal dağılım hacmi (Vd) — tanım", [
                B("İlaçların vücutta **plazma konsantrasyonlarına eşit konsantrasyonda dağıldıkları varsayılan sıvı hacmi** = **sanal dağılım hacmi**, **Vd** ile gösterilir."),
                B("**Vd (litre) = Vücuttaki toplam ilaç miktarı / O andaki plazmadaki ilaç konsantrasyonu (C)**"),
                B("Genellikle ilaçların dağıldıkları **fizyolojik sıvı kompartımanlarının toplamına karşılık gelmez**."),
            ]),
            C("Sekestrasyon ve protein bağlanmasının etkisi", [
                B("İlaçların dokulara bağlanmaları (**sekestrasyon**) sonucu **C küçük** bulunacağından **Vd çok daha büyük** bulunur. Örn. **digoksinin Vd'si ≈ 600 litre**.", y="23-24", tuzak="“Sekestrasyon olan ilacın sanal dağılım hacmi küçük bulunur” → YANLIŞ"),
                B("**Plazma proteinlerine fazla bağlanan** ilaçların plazma konsantrasyonları da yüksek bulunacağından **Vd küçük** bulunur."),
            ]),
            C("Vd karşılaştırması (slayttaki grafik)", [
                B("**Toplam vücut suyu ≈ 42 L** · **tübokürarin ≈ 9-12 L** · **furosemid** (yüksek protein bağlanması) **≈ 7-10 L** · **digoksin** (dokularda sekestre) **≈ 600 L**."),
                B("**Sekestrasyon arttıkça C küçülür, Vd büyür.**"),
            ]),
        ],
        [
            C("Vd'nin sağladığı üç önemli yarar", [
                B("**1)** Ölçülen plazma konsantrasyonundan vücutta o anda var olan **toplam ilaç miktarı** bulunabilir; veya bilinen miktarda ilaç varken **plazma konsantrasyonu** tahmin edilebilir."),
                B("**2)** Belirli bir plazma konsantrasyonu sağlamak için verilmesi gereken **ilaç dozunu** kestirmemizi sağlar."),
                B("**3)** İlacın total klirensine dayanarak **eliminasyon hızı** veya göstergesi **eliminasyon hız sabitesi (kel)** kestirilir: **kel = klirens / Vd**."),
            ]),
            C("Büyük dağılım hacmi", [
                B("Dağılım hacmi büyükse: genellikle ya **dokular ilaca yaygın bir şekilde maruz kalıyordur** ya da **belli bir dokuda birikiyordur**. Genellikle **etki süresinin uzunluğunu** da gösterir.", y="21-22"),
            ]),
            C("Dağılımın kinetiği", [
                B("**Basitleştirilmiş farmakokinetik kompartıman modelleri** kullanılır; varsayımlar üzerine kurulmuş ve teoriktirler."),
                B("**Tek kompartımanlı model**: tüm vücut tek kompartımandır."),
                B("**İki kompartımanlı dışarıya açık model**:"),
                B("**Santral kompartman**: ufak sanal hacimli — kan + fazla kanlanan organlar (kalp, akciğer, böbrek, karaciğer vs.)", lvl=1),
                B("**Periferik kompartman**: daha büyük hacimli — az kanlanan organlar (cilt, yağ dokusu, iskelet kasları, kemik vs.)", lvl=1),
                B("**Dışarıya açık olan santral kompartmandır**: ilaç buradan vücuda girer ve buradan elimine edilir."),
            ]),
        ],
    ],
    sorular=[
        Q("25-26", 19, "İlaçların dağılımı ile ilgili verilen bilgilerden hangisi DOĞRUDUR?",
          "a) Morfin kolayca plasentayı geçerek fetusta solunum depresyonuna neden olabilir",
          "Slayt: opioid analjezikler plasentayı geçip fetusta solunum depresyonu yapar. Yanlışlar: BOS'ta pasif/aktif ters, glikozid–tiroid, bağlı fraksiyon, albumin–bazik."),
        Q("24-25", 28, "İlaçların dağılımı ile ilgili verilen bilgilerden hangisi YANLIŞTIR?",
          "b) İyonize ilaçlar pasif difüzyonla, lipofilik ilaçlar aktif transportla BOS'a girer",
          "Doğrusu: lipofilik → pasif, iyonize bazı ilaçlar → aktif. Doğrular: albumin–asidik, serbest fraksiyon, glikozid sekestrasyonu, morfin-heroin mide suyunda."),
        Q("23-24", 14, "İlaçların dağılımı ile ilgili verilen bilgilerden hangisi YANLIŞTIR?",
          "b) Sekestrasyon olan ilacın sanal dağılım hacmi küçük bulunur",
          "Sekestrasyonda C küçülür, Vd çok büyür. Doğrular: iyonize ortamda toplanma, tiopental (redistribüsyon), asidik–albumin, homojen olmayan dağılım."),
        Q("22-23", 25, "İlaçların dağılımı ile ilgili verilen bilgilerden hangisi YANLIŞTIR? (AHK)",
          "a) İlaçlar çoğu kez non-iyonize halde bulunacakları ortamda toplanma eğilimindedir",
          "Doğrusu: daha fazla iyonize olacakları ortamda toplanır (iyon tuzağı). Doğrular: kanlanma, SSS geçişi sınırlı, plasenta, lipofilik küçük molekül difüzyonu."),
        Q("21-22", None, "Sanal dağılım hacmi büyük olursa hangisi olur?",
          "Daha uzun etki",
          "Vd büyükse ilaç dokulara yaygın dağılıyor ya da belli dokuda birikiyordur; genellikle etki süresinin uzunluğunu da gösterir."),
    ],
)
