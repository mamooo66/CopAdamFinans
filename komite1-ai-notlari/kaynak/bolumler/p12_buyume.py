# -*- coding: utf-8 -*-
"""Kaynak: Drive › Komite-1 › PDF › Patoloji › 2026-2027(yeni) › Çetin Boran › 6-Neoplazilerin Büyüme Biyolojisi ve Anjiogenez (28 slayt)"""

from yardim import B, C, Q  # noqa: F401

BOLUM = dict(
    key="buyume", baslik="Tümör Büyümesinin Biyolojisi, Anjiogenez, İnvazyon ve Metastaz",
    hoca="Prof. Dr. Çetin Boran", tarih="15 Ekim", saat="1 saat",
    kaynak="6-Neoplazilerin Büyüme Biyolojisi ve Anjiogenez · Prof. Dr. Ç. Boran · 2026",
    ozet=["Son 5 yılda bu dersten **3 soru** sayıldı (21-22, 24-25, 25-26); 22-23'te bir sorunun **replikatif havuz** şıkkı da doğru ifade olarak geçti. Konular: **replikatif havuz–kemoterapi**, **apoptoz**, **anjiogenez–anti-VEGF**, **HIF-1α**.",
          "Tekrar eden tuzak (22-23, 25-26): **geniş replikatif havuz / yüksek büyüme fraksiyonu = kemoterapiye duyarlı**; **düşük büyüme fraksiyonu (kolon ca) = rezistan**.",
          "**Anti-VEGF (bevacizumab)** → **yeni damar oluşumu durur**; damarsız tümör **1-2 mm'yi aşamaz** (24-25). **Hipoksi → HIF-1α → VEGF** (21-22). İnvazyon–metastaz kısmından (E-kaderin, MMP, organ tercihi, EMT) soru çıkmadı."],
    slaytlar=[
        # ------------------------------------------------------------ s.2-4 büyüme hızı
        [
            C("Büyüme hızını belirleyen faktörler (s.2)", [
                B("**Benign** ve **iyi diferansiye** tümörler, kötü diferansiye **malign** tümörlerden genel olarak **daha yavaş** büyür."),
                B("Tümörün **büyüme hızını üç ana faktör** belirler:"),
                B("**1) Tümör hücrelerinin ikiye katlanma zamanı**: bazı **çocuk tümörlerinde 1 ay**, **kolon-A.C tümörlerinde 2-3 ay**, **iyi diferansiye tükrük bezi tümörlerinde 1 yıl**.", lvl=1),
                B("**2) Replikatif havuzda olan tümör hücrelerinin miktarı**: **antikanser ajanlar genelde replikatif havuzdaki hücreleri öldürür**.", y="22-23", lvl=1),
                B("**3) Tümörde hücre kayıplarının miktarı**.", lvl=1),
            ]),
            C("Şema (s.3): replikatif havuz", [
                B("**Dönüşmüş (transformed) hücre** ve soyundan gelen hücreler **proliferatif (replikatif) havuzda** bölünerek çoğalır."),
                B("**Nonproliferatif havuza** geçen hücreler üç yoldan birini izler: **G0** · **diferansiyasyon** · **ölüm (death)**."),
            ]),
            C("Tümör büyüklüğü ve hücre sayısı (s.4)", [
                B("**10 mikronluk** bir hücre **30 defa** ikiye katlanırsa **1 milyar (10⁹) hücre** eder = **1 gram tümör**."),
                B("**10 defa daha** ikiye katlanırsa **10¹² hücre** eder = **1 kg**: hayatla bağdaşması bakımından **sınır bir büyüklüktür**."),
                B("İkiye katlanma süresi **3 gün**, tüm hücreler **replikatif havuzda** ve **hiç hücre kaybolmuyor** varsayılırsa bu ağırlığa **90 günde** ulaşılır."),
                B("**Hızlı büyüyen tümörlerde büyüme fraksiyonu %20**."),
            ]),
        ],
        # ------------------------------------------------------------ s.5 şema + s.6 kemoterapi
        [
            C("Şema (s.5): transformasyon, progresyon, metastaz", [
                B("**Sol sütun**: normal hücre → **tek tümör hücresi** → **30 katlanma** → **1 gm – 10⁹ hücre** = **klinik olarak saptanabilen en küçük kitle**."),
                B("Devamı: **10 katlanma** → **1 kg – 10¹² hücre** = **yaşamla bağdaşan en büyük kitle**; şemada **mikroskopik metastazlar** ve **metastazlar** da gösterilir."),
                B("**Orta sütun**: **TRANSFORMATION** (dönüşüm) → **PROGRESSION**: **genetik olarak kararsız hücrelerin proliferasyonu** → **tümör hücre varyantları, heterojenite**."),
                B("**Sağ sütun**: normal hücre → **transformasyon olayları** → **tümör hücresi** → **tümör hücre varyantları** → **yaşayan hücre varyantlarının klonal ekspansiyonu** → **insan solid malignitesi**."),
                B("Solid malignitedeki varyantlar: **non-antijenik** · **invazif** · **metastatik** · **daha az büyüme faktörü gerektiren**."),
            ]),
            C("Replikatif havuz ve kanser kemoterapisi (s.6)", [
                B("**Antineoplastik ilaçlar** en büyük etkisini **siklustaki hücreler** üzerinde gösterir.", y="22-23"),
                B("Bu nedenle **yüksek büyüme fraksiyonlu** hücreler (ör. **yüksek dereceli lenfomalar**) antikanser ilaçlara **çok duyarlıdır**.", y="22-23 25-26"),
                B("**Düşük büyüme fraksiyonlu** hücreler (**kolon ca**) ise nispeten **rezistandır**.", y="25-26",
                  tuzak="“Düşük büyüme fraksiyonuna sahip tümörler antineoplastik ilaç tedavisine daha iyi yanıt verir” → YANLIŞ"),
                B("Bu durumda tedavi için tümör hücrelerinin **G0'dan hücre siklusuna kaydırılması** gerekir."),
                B("Bu, **cerrahi veya radyasyonla tümör kitlesinin küçültülmesiyle (debulking)** sağlanabilir."),
                B("**Yaşayan tümör hücreleri yeniden hücre siklusuna girer** ve **ilaç tedavisine daha duyarlı** hale gelir."),
                B("Bu yaklaşım **kombine özel tedavilerin temelini** oluşturur."),
            ]),
        ],
        # ------------------------------------------------------------ s.7-9 apoptoz, anjiogenez, moleküller
        [
            C("Apoptoz (s.7)", [
                B("**Apoptoz (apopitozis)**, **tümör gelişmesini önleyen bir bariyerdir**.", y="25-26"),
                B("**Mutasyona uğrayan hücre**, mutasyon **tamir edilemezse** apoptozisle **ortadan kaldırılır**."),
                B("Tümör geliştikten sonra da tümörde gelişen **nekroz** ve **apoptotik hücre ölümleri tümör büyümesini yavaşlatır**."),
            ]),
            C("Tümör anjiogenezisi (s.8)", [
                B("Tümörü besleyecek **yeni damar gelişmezse** tümör büyüklüğü **1-2 mm'den öteye geçemez**.", y="24-25"),
                B("Tümörde **neovaskülarizasyon**, **yara iyileşmesinde olduğu gibi**, iki yolla oluşur:"),
                B("**endotel hücre öncüllerinin** bölgeye gelmesi", lvl=1),
                B("ortamda bulunan **kapillerlerden tomurcuklanma**", lvl=1),
            ]),
            C("Anjiogenik ve anti-anjiogenik moleküller (s.9)", [
                B("**Anjiogenik moleküller**: anjiogenezi uyaran faktörleri **ya tümör hücreleri ya da ortamdaki iltihap hücreleri** salgılar (**bFGF; VEGF**)."),
                B("**Stromada depolanmış FGF**, tümör hücrelerinin ya da tümörün uyardığı stromal hücrelerin salgıladığı **proteazlarca açığa çıkarılır**."),
                B("**Anti-anjiogenik moleküller**: **anjiostatin**, **endostatin**, **vaskulostatin**."),
                B("**Sırasıyla plazminojen, kollajen ve transtretin** moleküllerinin **enzimatik parçalanması** ile açığa çıkarlar."),
            ]),
        ],
        # ------------------------------------------------------------ s.10-13 anjiogenezin kontrolü
        [
            C("Anjiogenik–antianjiogenik denge (s.10)", [
                B("**Anjiogenik ve antianjiogenik moleküller arasındaki denge** pek çok **fizyolojik stimulus** tarafından kontrol edilir."),
                B("Örnek: **hipoksi → HIF-1α sentezi → VEGF ve FGF transkripsiyonu**.", y="21-22"),
                B("**Ras ve myc mutasyonu** da **VEGF transkripsiyonunu arttırır**."),
            ]),
            C("Yeni oluşan damarlar (s.11)", [
                B("Yeni damarlar normalden farklı olarak **daha sızıntılı** ve **disorganizedir**."),
                B("Yeni damar **tümörü besler**; ayrıca **endotelden salgılanan PDGF ve insülin benzeri büyüme faktörü** tümör büyümesine katkı sağlar."),
                B("**Metastazda** da yeni oluşan damarların katkısı vardır."),
            ]),
            C("Anjiogenezin başlaması (s.12)", [
                B("**Çoğu tümörde yıllarca anjiogenez gelişmez** ve tümör **küçük bir odak** olarak kalır."),
                B("**Anjiogenezin başlaması** ile tümör **büyümeye başlar**."),
                B("**Anjiogenezi başlatan faktörler**:"),
                B("**RAS-MAP kinaz sinyal yolu**: bu yoldaki **Ras ve myc'in aktivite kazanması VEGF'yi arttırır**; pek çok tümörde **VEGF ve bFGF artmıştır**.", lvl=1),
                B("**p53 mutasyonu**.", lvl=1),
            ]),
            C("p53 ve anjiogenez; tedavi (s.13)", [
                B("**Anjiogenez inhibisyonunda p53'ün rolü** vardır: antianjiogenik molekül **trombospondin-1'i arttırır**; **VEGF ve HIF-1'i azaltır**."),
                B("**HIF-1** (hipoksi inducible faktör): görevi **VEGF transkripsiyonunu sağlamak**.", y="21-22"),
                B("**p53 mutasyonu anjiogenezi başlatabilir**."),
                B("**Bevacizumab**: **anti-VEGF monoklonal antikor** (tedavi amaçlı).", y="24-25",
                  tuzak="“Anti-VEGF ile büyümenin durması yeni mutasyon olmaması, karsinojen yokluğu, EGFR aktivasyonu ya da DNA tamir mutasyonuna bağlıdır” → YANLIŞ"),
            ]),
        ],
        # ------------------------------------------------------------ s.14-18 metastaz giriş
        [
            C("Şema (s.14): metastaz modelleri", [
                B("**Metastatik olmayan primer tümör**ün **metastaza** ilerleyişi şemada **dört modelle (A-D)** gösterilir:"),
                B("**A**: **metastatik varyantlar** → metastaz", lvl=1),
                B("**B**: **metastatik imza (signature)** → metastaz", lvl=1),
                B("**C**: **metastatik imza ve varyantlar** → metastaz", lvl=1),
                B("**D**: **stromal yanıt** + **metastatik imza ve varyantlar** → metastaz", lvl=1),
            ]),
            C("Metastaz (s.15-16)", [
                B("**Karaciğerde metastaz odakları** (s.15 fotoğrafı)."),
                B("**Metastaz, malignitenin kesin bir bulgusudur**: **uzak dokulara tümör implantları** olur ve **orada da tümör büyür**."),
                B("**Metastaz yolları**: **(1) vücut boşluklarına ekilme** · **(2) lenfatik yayılım** · **(3) hematojen yayılım**."),
                B("**Vücut boşluklarına ekilme**: **medulloblastom**, **A.C Ca**, **GİS CA**, **over tümörleri**, **mukus sekrete eden appendiks tümörleri → pseudomiksoma peritonei**.", lvl=1),
            ]),
            C("İnvazyon ve metastaz mekanizmaları (s.17-18)", [
                B("Metastaz olayı **iki basamakta** incelenir: **(1) ekstrasellüler matriksin (ECM) invazyonu** · **(2) vasküler yayılım ve tümör hücrelerinin başka dokulara yuvalanması**."),
                B("**Matriks**, **kollajen**, **glikoprotein** ve **proteoglikanlar** içerir."),
                B("**Malign tümörlerden milyonlarca hücre dolaşıma karışır**; bunlardan **küçük bir kısmı** metastatik odak oluşturur."),
                B("**ECM invazyonu ardışık basamaklarla** olur: **kohezyon kaybı** → **matriks komponentlerine tutunma** → **ECM'nin yıkılması** → **tümör hücrelerinin yıkılan alandan serbest hareketle göçmesi**."),
            ]),
        ],
        # ------------------------------------------------------------ s.19-20, 23 şema + kohezyon kaybı + tutunma
        [
            C("Şema (s.19): metastatik basamaklar", [
                B("**Primer tümör**: dönüşmüş hücre → **klonal ekspansiyon, büyüme, diversifikasyon, anjiogenez** → **metastatik subklon**."),
                B("**Bazal membrana adezyon ve invazyon** → **ekstrasellüler matriksten geçiş** → **intravazasyon**."),
                B("Dolaşımda: **konak lenfoid hücreleriyle (lenfosit) etkileşim** → **tümör hücre embolisi** (**trombositlerle** birlikte)."),
                B("**Bazal membrana adezyon** → **ekstravazasyon** → **metastatik depozit** → **anjiogenez** → **büyüme** (metastatik tümör)."),
            ]),
            C("Kohezyon kaybı (s.20, s.23-A)", [
                B("**Normal hücreler E-kaderin (E-cadherin) ile birbirine bağlanır**; E-kaderin **hücre içi yapılara β-katenin** aracılığıyla bağlanır."),
                B("Çeşitli tümörlerde **bu iki molekülde oluşan işlevsizlik kohezyon kaybına** yol açar."),
                B("**Kolon ve meme tümörleri** gibi pek çok tümörde **E-kaderin azalmıştır**."),
                B("Şema A (**hücreler arası bağlantıların gevşemesi**): **kaderinler** · **tip IV kollajen** · **bazal membran** · **laminin**."),
            ]),
            C("Matrikse tutunma (s.20, s.23-B)", [
                B("Ardından tümör hücreleri **yüzeyindeki integrin ve Ig ailesinden reseptörlerle laminin ve fibronektine** bağlanır."),
                B("Şema B (**tutunma, attachment**): **tip IV kollajen** · **laminin reseptörü** · **fibronektin reseptörü** · **laminin**."),
            ]),
        ],
        # ------------------------------------------------------------ s.21-22, 24, 25 yıkım + göç + embolus + doku tercihi
        [
            C("Matriksin yıkımı (s.21-22)", [
                B("ECM ve bazal membrana yapışmayı takiben tümör hücreleri **proteazlarla matriksi yıkar**: **matriks metalloproteinazlar (MMP)**, **katepsin D**, **ürokinaz plazminojen aktivatörü**."),
                B("**MMP'lar stromadaki iltihap hücreleri ve stromal hücrelerce de yapılır**."),
                B("Ortamda **proteaz inhibitörleri** de vardır; ancak **denge yıkım yönündedir**."),
                B("Matriks yıkımı ayrıca **anjiogenezi**, **tümör hücrelerinin büyümesini** ve **kemotaksisini** etkileyen ürünleri de **açığa çıkarır**."),
            ]),
            C("Şema (s.24): yıkım ve göç", [
                B("**C – Yıkım (degradation)**: **tip IV kollajenaz** ve **plazminojen aktivatörü** → **tip IV kollajenin parçalanması (cleavage)**."),
                B("**D – Göç (migration)**: şemada **fibronektin** ve **otokrin motilite faktörü (autocrine motility factor)** etiketlidir."),
            ]),
            C("Vasküler yayılım: tümör embolileri (s.25)", [
                B("Tümör hücreleri **vasküler yatağa girdikten sonra** **tümör embolileri** şeklinde **platelet ve lökositlerle karışık** halde yol alır."),
                B("**Çeşitli organlarda damar dışına çıkarak** **metastatik kitleler** oluşturur."),
                B("**Dolaşımda agregatların oluşması** tümör hücre **yaşamını** ve **implantasyonunu** sağlar."),
            ]),
            C("Metastazın yeri ve doku tercihi (s.25)", [
                B("**Tümörün lokalizasyonu ve drenaj yolları** metastazın yerini belirler; ancak **bazı tümörler bazı dokulara özellikle** metastaz yapar."),
                B("**Doku tercihini belirleyen etken**: her dokunun **damar endotellerinin değişik adezyon moleküllerine bağlanan ligandları** sentezlemesidir."),
            ]),
        ],
        # ------------------------------------------------------------ s.26-28 CD44, organ tercihi, kemokin, EMT
        [
            C("CD44 (s.26)", [
                B("**CD44**: bir **T lenfosit adezyon molekülü**; T lenfositin vücutta normal yerine ulaşmasını sağlar (**venül endotelindeki hyaluronat'a** bağlanır)."),
                B("**Pek çok solid tümörde saptanmıştır** ve **tümörlerin yayılmasını kolaylaştırır**."),
            ]),
            C("Organ tercihi ve kemokinler (s.27)", [
                B("**Prostat Ca** → **kemiği sever**."),
                B("**A.C Ca** → **adrenali ve beyni sever**."),
                B("**Kemokinler** de metastazda organ tercihini **bir dereceye kadar** açıklayabilir."),
                B("Örnek 1: bazı **meme karsinomları** **CXCR4** ve **CCR7** adlı **kemokin reseptörünü eksprese** eder; bu reseptörlere bağlanan kemokinleri üreten dokular **kolayca metastaza uğrar**."),
                B("Bu reseptörlerin **blokajı**, meme CA'nın **akciğer ve lenf nodüne metastazını azaltır**.", lvl=1),
            ]),
            C("Meme kanserinin kemik metastazı (s.27, örnek 2)", [
                B("**Meme kanserinin kemiğe metastazı osteolitiktir**: tümör hücreleri **PTH-RP (PTH related protein)** sentezler."),
                B("**PTH-RP osteoblastları stimüle ederek RANKL salgılatır**; **RANKL osteoklastları aktive eder**."),
                B("**Osteoklastlar matriksi yıkarken** matriks içindeki **IGF ve TGF-β** gibi **büyüme faktörleri de açığa çıkar**."),
            ]),
            C("Hedef organ, SNAIL ve TWIST (s.28)", [
                B("Bazı hedef organlar **IGF I ve II** salgılayarak tümör hücrelerinin **kendilerinde toplanmasını** sağlar."),
                B("**Çizgili kas dokusu** gibi bazı organlar **hemen hiç metastaz almaz**."),
                B("**SNAIL** ve **TWIST**: metastazı kolaylaştırdığı söylenen **iki onkogen**; **epitelyal-mezenkimal geçişi (EMT)** teşvik eder."),
                B("**EMT** sürecinde **epitelyal markırların ekspresyonu azalır** (**E-kaderin** vb.), **mezenkimal markırlar artar** (**vimentin, SMA**)."),
                B("**SNAIL ve TWIST özellikle E-kaderini azaltır**."),
            ]),
        ],
    ],
    sorular=[
        Q("25-26", 80, "Hangisi doğru DEĞİLDİR? (büyüme fraksiyonu, apoptoz, seminoma, Rb geni, anaplazi)",
          "“Düşük büyüme fraksiyonuna sahip tümörler antineoplastik ilaç tedavisine daha iyi yanıt verir”",
          "Düşük fraksiyon = rezistan, yüksek = duyarlı (s.6) · apoptoz bariyerdir (s.7) · seminoma, RB, anaplazi şıkları bu PDF'te yok"),
        Q("24-25", 87, "Anti-VEGF monoklonal antikor verilen hastada tümör büyümesi durdu; en olası neden?",
          "Yeni damar oluşumu durmuştur",
          "Anti-VEGF (bevacizumab) anjiogenezi keser; damarsız tümör 1-2 mm'yi aşamaz (s.8, 13) · mutasyon, karsinojen, EGFR, DNA tamir şıkları değil"),
        Q("22-23", 78, "Hangisi yanlıştır? (replikatif havuz şıkkı DOĞRU ifadedir)",
          "“Replikatif havuz ne kadar geniş ise kemoterapötiklerle tümör o kadar hızlı küçülür” (doğru ifade)",
          "Soru Patoloji P10'da sayılır; yanlış şık: E2F'nin süpresör gen olması · geniş replikatif havuz = ilaca duyarlı (s.2, 6)", ref=True),
        Q("21-22", None, "Hipoksi durumunda uyarılan?",
          "HIF-1α",
          "Hipoksi → HIF-1α → VEGF ve FGF transkripsiyonu (s.10) · öğrenci hatırlamasından derlenmiş soru"),
    ],
)
