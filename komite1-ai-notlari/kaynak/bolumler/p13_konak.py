# -*- coding: utf-8 -*-
"""Kaynak: Drive › Komite-1 › PDF › Patoloji › 2026-2027(yeni) › Çetin Boran › 5-Tümöre karşı savunma, kanserin moloküler tanısı (29 slayt)

NOT: 14. sayfada metin yok (yalnız dört etiketsiz mikrofotoğraf). 6, 12, 19, 20, 22. sayfalardaki şekiller ve 28-29. sayfalardaki
paraneoplastik sendrom tablosu görselden okundu; 22. sayfanın alt yazısı slaytta kesik ("d, Point mutations, represente").
"""

from yardim import B, C, Q  # noqa: F401

BOLUM = dict(
    key="konak", baslik="Tümöre Karşı Konak Savunması, Tümörün Konağa Etkileri ve Kanserin Moleküler Tanısı",
    hoca="Prof. Dr. Çetin Boran", tarih="13 Ekim", saat="1 saat",
    kaynak="5-Tümöre karşı savunma, kanserin moleküler tanısı · Prof. Dr. Ç. Boran · 2026",
    ozet=[
        "Son 5 yılda bu dersten **2 soru** (+ 21-22'de 1 hatırlanan soru): **onkofetal antijen** iki kez soruldu (23-24 **CEA**, 25-26 **AFP**); 21-22'de **paraneoplastik sendrom örneği = Cushing sendromu**.",
        "Çeldiriciler **başka tümör antijeni gruplarından**: **MUC-1** (değişmiş glikoprotein), **CD20 / CD30** (diferansiyasyon antijeni), **CD8** (CTL), **MHC**. Onkofetal olanlar yalnız **CEA ve AFP**.",
        "Paraneoplastik sendromda öne çıkanlar: ektopik hormonla **en sık Cushing** (küçük hücreli akciğer Ca → ACTH / POMC); **hiperkalsemi** → **skuamöz** akciğer Ca (**PTHrP**); **Trousseau** = migratuvar tromboflebit.",
    ],
    slaytlar=[
        # 1 — tümör antijenleri (s.2-4)
        [
            C("Tümör antijenleri 1-3 · s.2-3", [
                B("**1- Mutant gen ürünleri**: **p53**, **RAS** vb."),
                B("**2- Hücre proteinlerinin aşırı ekspresyonu**:"),
                B("**a- Normal sellüler proteinin aşırı ekspresyonu**: örn. normalde eser miktarda olan **tirozinaz** enziminin **malign melanomda** artması.", lvl=1),
                B("**b- Kanser testis antijenleri**: yetişkinde **testis haricinde** başka doku ve hücrelerde **silinmiştir**.", lvl=1),
                B("Örn. çoğunlukla **malign melanomlarda** saptanan **MAGE** antijeni; diğer tümörlerde de saptanmış; **RAGE, GAGE** gibi tipleri var.", lvl=1),
                B("**3- Onkojenik virüsler** tarafından oluşturulan tümör antijenleri."),
            ]),
            C("Tümör antijenleri 4-6 · s.3-4", [
                B("**4- Onkofetal antijenler**: normal gelişen **fetusta** bulunan ve sonradan **azalan veya kaybolan** bazı antijenler tümör tarafından üretilebilir: **CEA**, **AFP**.",
                  y="23-24 25-26",
                  tuzak="“MUC-1, CD20, CD30, CD8 veya MHC onkofetal antijendir” → YANLIŞ (MUC-1 = değişmiş glikoprotein; CD20, CD30 = diferansiyasyon antijeni)"),
                B("Normalde **eser miktarda** bulunurlar; **bazı inflamasyonlarda** miktarı artabilir.", lvl=1),
                B("**5- Hücre yüzeyinde değişikliğe uğramış glikolipid ve glikoproteinler**: **CA125** ve **CA 19-9** (over karsinomlarında), **MUC-1** (over ve meme karsinomunda)."),
                B("**6- Hücre tipine spesifik diferansiyasyon antijenleri**: **CD20** ve **CD30**."),
                B("Bu ikisine karşı geliştirilen **antikorlar tedavide kullanılıyor**.", lvl=1),
            ]),
        ],
        # 2 — antitümör mekanizmalar: genel, CD8+ T hücrelerinin tanıdığı antijenler, efektör hücreler (s.5-7)
        [
            C("Savunma ve CD8+ T hücresi antijenleri · s.5-6", [
                B("Tümör savunmasında **hücresel immünite ön plandadır**."),
                B("Ancak tümörlere karşı **antikorlar da** saptanmış."),
                B("**CD8+ T hücrelerinin tanıdığı tümör antijenleri** (s.6 şeması):"),
                B("**Normal konak hücresi**: **MHC class I** ile ilişkili birçok **normal self antijen** gösterir → **T hücresi yanıtı yok**."),
                B("**Tümör hücreleri farklı tipte tümör antijenleri** taşır → **CD8+ CTL** tanır (şemada 4 tip):"),
                B("**Onkogen ürünü veya mutant tümör süpresör gen ürünü**: mutant **RAS**, **BCR/ABL** füzyon proteinleri; mutant **p53** proteini.", lvl=1),
                B("**Mutant self protein**: karsinojen veya radyasyonla indüklenen hayvan tümörlerinde ve **melanomlarda** çeşitli mutant proteinler.", lvl=1),
                B("**Aşırı veya aberran ekspresyonlu self protein**: aşırı ekspresyon → **tirozinaz, gp100, MART** (melanom); aberran ekspresyon → **kanser-testis antijenleri (MAGE, BAGE)**.", lvl=1),
                B("**Onkojenik virüs** (virüs antijenine özgü CD8+ CTL): servikal karsinomda **HPV E6, E7** proteinleri; EBV ile indüklenen lenfomda **EBNA** proteinleri.", lvl=1),
            ]),
            C("Efektör hücreler · s.7", [
                B("**Sitotoksik T lenfositler (CTL)**: tümörü infiltre eden **CD8+ CTL** sayısının **prognoz ile ilişkisi** çeşitli çalışmalarda gösterilmiş."),
                B("**NK hücreleri**: **önceden hassaslaşmaya gerek olmadan** tümör hücresini öldürebilir; tümöre karşı **ilk direnci** bu hücreler oluşturur."),
                B("**Sitokinlerle aktifleştirilmiş NK hücreleri** tümörlere karşı **immün terapide** kullanılıyor.", lvl=1),
                B("**Makrofajlar**: T lenfositleri ve NK hücrelerinin salgıladığı **interferon-γ**, makrofajların **potent aktivatörüdür**."),
                B("Makrofajlar T lenfositleri ve NK hücreleriyle birlikte **tümör savunmasında** yer alır.", lvl=1),
            ]),
        ],
        # 3 — immün gözetim; tümörün immün sistemden kurtulma yolları 1-3 (s.7-9)
        [
            C("İmmün gözetim · s.7-8", [
                B("**Konjenital immün yetmezliği** olanlarda **200 kat daha sık** tümör gelişir; **kazanılmış immün yetmezliklerde** de tümör sıklığı artmıştır."),
                B("İmmün yetmezliklerde gelişen tümörlerin **büyük çoğunluğu B lenfomadır**."),
                B("**X-linked lymphoproliferative syndrome**: B lenfomalar gelişir; **SAP geninde** mutasyon var (SAP, NK ve T hücre sinyal yollarında rol alır)."),
                B("**EBV infeksiyonunda** şiddetli **enfeksiyöz mononükleoz** tablosu olur ve **lenfoma** gelişir.", lvl=1),
                B("İmmün supresiflerde **sadece B-lenfoma** gelişmesi **immün gözetim hakkında şüphe** uyandırmaktadır."),
                B("İmmün sistem salgıladığı **sitokinler ve MMP enzimleri** ile **tümörün büyümesini de artırabilir**."),
            ]),
            C("Tümörün immün sistemden kurtulma yolları 1-3 · s.9", [
                B("**Çoğu tümör immün sistemi sağlam bireylerde gelişir.**"),
                B("**1- Antijen negatif tümör hücre varyantlarının selektif büyümesi.**"),
                B("**2- MHC moleküllerinin ekspresyonunun kaybı veya azalması (HLA I kaybı)** → **CTL saldırısından kurtulur**."),
                B("Ancak bu hücreler **NK hücreleri tarafından hâlâ ortadan kaldırılabilir**.", lvl=1),
                B("**NK hücrelerini IL-2 ve IL-15** gibi sitokinlerle uyarıp tekrar hastaya **tedavi amaçlı** vermek söz konusu.", lvl=1),
                B("**3- İmmün düzenleyici yolların aktivasyonu**: tümör, **antijen sunan hücrelerdeki (histiositler) kostimülatör faktör** ekspresyonunu azaltabilir."),
                B("Histiosit T lenfosit üzerindeki **CD28**'e bağlanamaz; onun yerine **inhibitör CTLA-4**'e bağlanır (cytotoxic T-lymphocyte–associated antigen 4).", lvl=1),
                B("Tümör hücreleri **PD-L1 ve PD-L2**'yi de aktive edebilir: efektör T hücrelerindeki **PD-1** reseptörünü aktive eden hücre yüzeyi proteinleri.", lvl=1),
                B("**PD-1 ve CTLA-4** reseptörlerini **bloke eden antikorların tedavide kullanılması** planlanıyor.", lvl=1),
            ]),
        ],
        # 4 — kurtulma yolları 4-6, şema (s.10-12)
        [
            C("Kurtulma yolları 4-6 · s.10-11", [
                B("**4- İmmünsupresif faktörlerin kanser hücrelerince sekresyonu**: **TGF-β**, **IL-10**, **VEGF** (T lenfosit diapedezini önler), **prostaglandin E2**."),
                B("**5- Düzenleyici immünsupresif T lenfositlerin uyarılması.**"),
                B("**5- Antijenin maskelenmesi**: tümör normalden çok **glikokaliks** salgılayarak kendi yüzeyini örter (slaytta numara ikinci kez “5”)."),
                B("**6- Sitotoksik T lenfositlerin apopitozisi**: bazı **melanomlar ve HCC'ler Fas ligandını** eksprese eder; **Fas ligandı T lenfositi apopitoza götürür**."),
            ]),
            C("Kaçış şeması · s.12", [
                B("Tümörler **antijen** veya **MHC** ekspresyonunu kaybederek immün yanıttan kaçabilir."),
                B("Ayrıca **immünsupresif sitokinler** ve T hücresindeki inhibitör reseptörler için **ligandlar (PD-L1 gibi)** üreterek kaçabilir."),
                B("**Normal**: tümör hücresi **MHC + tümör antijeni** gösterir → antijene özgü **T hücresi tanır** → T hücre aktivasyonu."),
                B("**Antijen üretememe** (antijen-kayıp varyantı) → T hücresi tümörü **tanıyamaz**.", lvl=1),
                B("**MHC genlerinde veya antijen işleme için gerekli genlerde mutasyon** (class I MHC-eksik tümör hücresi) → T hücresi tümörü **tanıyamaz**.", lvl=1),
                B("**İmmünsupresif proteinler veya inhibitör yüzey proteinleri** (inhibitör ligand–reseptör, immünsupresif sitokinler) → **T hücre aktivasyonu inhibe olur**.", lvl=1),
            ]),
        ],
        # 5 — tümör tanısı 1-4 (s.13-16)
        [
            C("Tanı 1: histoloji ve sitoloji · s.13-14", [
                B("**Eksizyonal ve insizyonal biyopsiler**."),
                B("**Aspirasyon ve sitoloji**, sitolojik yaymalar."),
                B("**Frozen**."),
                B("**İmmünofloresan, histokimyasal ve immünohistokimyasal** çalışmalar:"),
                B("**Tümörün tipinin** tayin edilmesi.", lvl=1),
                B("**Metastatik tümörün orijininin** saptanması (**PSA; TTF-1** ve moleküller ile).", lvl=1),
                B("**Prognostik ve terapötik önemi** olan moleküllerin tespiti: örn. memede **c-erbB2**, akciğer karsinomları ve lenfomalarda **ALK**.", lvl=1),
                B("s.14: yalnız dört etiketsiz mikrofotoğraf (sitoloji, histoloji, immünohistokimya örnekleri), metin yok."),
            ]),
            C("Tanı 2-4: flow, dolaşan hücre, moleküler · s.15-16", [
                B("**2- Flow cytometry**: daha çok **lösemiler** gibi **kan ile ilişkili akışkan tümörlerde** sık kullanılır."),
                B("Pek çok **hücre karakterinin hızlı ölçümünü** ve **yüzey antijenlerinin tespitini** sağlar.", lvl=1),
                B("**3- Kanda dolaşan solid tümör hücrelerinin tespiti**: **spesifik antikorlarla** kanda **eser miktardaki tümör hücrelerini** yakalamak mümkün."),
                B("Tümörlerin **erken teşhisi** ve **metastaz yapma ihtimalinin** tespiti için umut vaat eden bir yöntem.", lvl=1),
                B("**4- Moleküler ve sitogenetik tanı**:"),
                B("**PCR** ile **T-hücre reseptörü ve immünoglobulin genlerinin yeniden düzenlenmesinin** tespiti (**monoklonite** tespiti).", lvl=1),
                B("**Translokasyonların saptanması**: örn. **(11;22)(q24;q12)** translokasyonunun tespiti **Ewing sarkomu** teşhisini doğrular.", lvl=1),
                B("Rutin **sitogenetik analizler** ve **FISH** ile spesifik translokasyonların tespiti.", lvl=1),
                B("**DNA mikrodizi analizi** ile **tüm genomun** analizi.", lvl=1),
            ]),
        ],
        # 6 — moleküler ve sitogenetik yöntemlerin gerekli olduğu haller; hedefe yönelik tedavi (s.17-18)
        [
            C("Moleküler tanı: gerekli haller · s.17-18", [
                B("**Malign neoplazilerin prognozunun tespiti**:"),
                B("**NMYC** geninde artış ve kromozom **1p** kayıpları **nöroblastomda kötü prognozu** gösterir.", lvl=1),
                B("**Oligodendrogliomda** kromozom **1p ve 19q** kayıpları **tedaviye iyi yanıt** alınacağını gösterir; tersine bunlar sağlam ve **EGFR artmış** ise **kötü prognoz** işaretidir.", lvl=1),
                B("**Minimal rezidüel tümörün tespiti**: lösemi ve lenfomalarda **PCR** taramaları ile relapslar **erken evrede** yakalanabilir."),
                B("Örn. **kronik myeloid lösemide PCR ile BCR-ABL füzyon geninin** taranması.", lvl=1),
                B("**Ailesel kanser yatkınlığının tespiti**: **BRCA1, BRCA2** ve **RET** proto-onkogen gibi genlerdeki ailesel geçişli mutasyonlar spesifik ailesel kanser gelişim riskini açığa çıkarır."),
            ]),
            C("Hedefe yönelik tedaviler · s.18", [
                B("**Hedefe yönelik tedaviler** için özellikle aranan başlıca genler / moleküller:"),
                B("**PML-RARA** füzyon geni: **akut promyelositik lösemi** (slaytta “ML-RARA” yazıyor).", lvl=1),
                B("**BCR-ABL** füzyon geni: **kronik myelojen lösemi** ve **akut lenfoblastik lösemi**.", lvl=1),
                B("**ERBB1 (EGFR)** mutasyonları ve **ALK** gen yeniden düzenlenmeleri: **akciğer kanseri**.", lvl=1),
                B("**BRAF** mutasyonları: **melanom**.", lvl=1),
            ]),
        ],
        # 7 — paradigma değişimi, BRAF'omalar, moleküler profil (s.19-22)
        [
            C("Paradigma değişimi, BRAF · s.19-20", [
                B("**Kanserin sınıflandırılması** hücre kökeni ve morfolojiye göre değil, **terapötik hedeflere** göre yapılıyor."),
                B("Şema: akciğer, meme, prostat, kolon, beyin → **genetik analiz** → **hedefe yönelik tedaviler**: mutant **KIT, HER2, EGFR, BRAF, PI3K**.", lvl=1),
                B("**Ortak moleküler patogenez**: farklı tümör tiplerinde **BRAF (V600E)** mutasyonu:", lvl=1),
                B("Melanom · papiller tiroid karsinomu · kolon adenokarsinomu · Langerhans hücreli histiyositoz · hairy cell lösemi.", lvl=1),
                B("**“BRAFoma”lar BRAF inhibitörleri ile tedavi** adayıdır."),
            ]),
            C("Moleküler profil · s.21-22", [
                B("**DNA mikrodizi analizi** gibi yöntemler tümörlerin **genetik profillerinin kataloglanması** imkanını ortaya koymuştur."),
                B("**Circos plot**: erkek bir hastanın **tek bir akciğer kanserindeki** genetik değişiklikler."),
                B("Kanserdeki **24 kromozomun** her biri bir daire üzerinde gösterilir; tümöre özgü aberasyonların konumları bu kromozomlara işlenir:", lvl=1),
                B("**a**: yapısal yeniden düzenlenmeler — **mavi çizgi intrakromozomal**, **kırmızı çizgi interkromozomal**.", lvl=1),
                B("**b**: **heterozigotluk kaybı** ve **alelik dengesizlik** (bir alelin diğerine göre fazla temsili) bölgeleri — **yeşil**.", lvl=1),
                B("**c**: **kopya sayısı profilleri** — kopya **kayıpları kırmızı**, kopya **kazançları mavi**.", lvl=1),
                B("**d**: **nokta mutasyonlar** (slayttaki alt yazı burada kesiliyor).", lvl=1),
            ]),
        ],
        # 8 — tümörün konağa etkileri, kaşeksi, paraneoplastik sendrom (s.23-27)
        [
            C("Konağa etkiler, kaşeksi · s.23-24", [
                B("**Tümörün konağa etkileri**:"),
                B("**1- Lokal ve hormonal etkiler**", lvl=1),
                B("**2- Kanama ve sekonder infeksiyonlar**", lvl=1),
                B("**Rüptür ve infarksiyonlara bağlı akut semptomlar**", lvl=1),
                B("**Kanser kaşeksisi**: sıklıkla **vücut yağı ve kas kitlesinde progresif kayıp**; beraberinde **zayıflık, iştahsızlık ve anemi**."),
                B("**İştahsızlığa rağmen metabolizma hızlıdır**.", lvl=1),
                B("Sorumlu olan: kaşeksiden **salgılanan sitokinler ve proteolitik enzimler**.", lvl=1),
            ]),
            C("Paraneoplastik sendrom · s.25-27", [
                B("Kanserin **lokal ve sistemik yayılımı** ve kaynaklandığı dokunun **hormonal etkileri ile açıklanamayan** semptomlar kompleksidir."),
                B("**Endokrinopatiler**: endokrin organ kökenli olmayan kanserin ürettiği hormona **ektopik hormon** denir."),
                B("Ektopik hormon üretimi ile **en sık Cushing sendromu** gelişir.", y="21-22", lvl=1),
                B("Özellikle **küçük hücreli akciğer karsinomu**, **kortikotropin benzeri peptidler ve pro-opiomelanokortin (POMC)** salgılayarak bu sendroma yol açar.", lvl=1),
                B("**Hiperkalsemi**: **akciğer skuamöz hücreli kanseri** sorumludur; **PTH, PTHrP**."),
                B("**Akantozis nigrikans**: **mide, uterus ve akciğer** kanserlerinde görülür."),
                B("**Hipertrofik osteoartropati**: **en sık bronkojenik karsinomda** görülür."),
                B("Ekstremite distal uç kemiklerinde **periosteal yeni kemik yapımı**, bitişikteki eklemde **artrit**, parmaklarda **çomaklaşma** olur.", lvl=1),
                B("Çomak parmak **siyanotik kalp hastalığı**, **diffüz akciğer hastalığı**, **Ü.K** (ülseratif kolit) gibi pek çok kronik hastalıkta da olur.", lvl=1),
                B("**Vasküler ve hematolojik sendromlar**: **migratuvar tromboflebit (Trousseau sendromu)**, **DIC**."),
            ]),
        ],
        # 9 — paraneoplastik sendromlar tablosu (s.28-29): sendrom → en sık kanser → mekanizma
        [
            C("Tablo: endokrinopatiler · s.28", [
                B("Sütunlar: **sendrom → en sık kanser türleri → nedensel mekanizma**."),
                B("**Cushing sendromu**: küçük hücreli akciğer karsinomu, pankreas karsinomu, nöral tümörler → **ACTH veya ACTH benzeri madde**.", y="21-22"),
                B("**SIADH (uygunsuz ADH salgılanması sendromu)**: küçük hücreli akciğer karsinomu, intrakraniyal neoplazmlar → **ADH veya atriyal natriüretik hormonlar**."),
                B("**Hiperkalsemi**: akciğer skuamöz hücreli karsinomu, meme, renal ve over karsinomu, erişkin T hücreli lösemi/lenfoma → **PTHrP, TGF-α, TNF, IL-1**."),
                B("**Hipoglisemi**: fibrosarkom, diğer mezenkimal sarkomlar, hepatoselüler karsinom → **insülin veya insülin benzeri madde**."),
                B("**Karsinoid sendrom**: bronşiyal adenom (karsinoid), pankreas karsinomu, mide karsinomu → **serotonin, bradikinin**."),
                B("Bulgular: **taşikardi, diyare, nefes darlığı, ataklar halinde yüzde kızarma, spider anjiyom**.", lvl=1),
                B("**Polisitemi**: renal karsinom, serebellar hemanjiyom, hepatoselüler karsinom → **eritropoietin**."),
            ]),
            C("Tablo: sinir-kas, deri · s.28-29", [
                B("**Miyasteni**: bronkojenik karsinom → **immünolojik**."),
                B("**Merkezi ve periferik sinir sistemi bozuklukları**: meme karsinomu."),
                B("**Akantozis nigrikans**: mide, akciğer, uterus karsinomu → **immünolojik**; **epidermal büyüme faktörü** salgılanması."),
                B("**Dermatomiyozit**: bronkojenik, meme karsinomu → **immünolojik**."),
            ]),
            C("Tablo: kemik, damar, diğer · s.29", [
                B("**Hipertrofik osteoartropati ve parmaklarda çomaklaşma**: bronkojenik karsinom → mekanizma **bilinmiyor**."),
                B("**Venöz tromboz (Trousseau fenomeni)**: pankreas karsinomu, bronkojenik karsinom, diğer kanserler → **tümör ürünleri (pıhtılaşmayı aktive eden müsinler)**."),
                B("**Nonbakteriyel trombotik endokardit**: ileri kanserler → **hiperkoagülabilite**."),
                B("**Anemi**: timik neoplazmlar → bilinmiyor."),
                B("**Nefrotik sendrom** (diğer): çeşitli kanserler → **tümör antijenleri, immün kompleksler**."),
            ]),
        ],
    ],
    sorular=[
        Q("25-26", 82, "Hangisi onkofetal antijendir?", "AFP",
          "MUC-1 (değişmiş glikoprotein), CD20 (diferansiyasyon), CD8 (CTL), MHC değil · slayt: onkofetal = CEA, AFP"),
        Q("23-24", 81, "Hangisi onkofetal antijendir?", "CEA",
          "CD20, CD30 (diferansiyasyon), MUC-1 (değişmiş glikoprotein), MHC class II değil · slayt: onkofetal = CEA, AFP"),
        Q("21-22", None, "Hangisi paraneoplastik sendrom örneğidir?", "Cushing sendromu",
          "Öğrenci hatırlamasından derlenmiş soru · slayt: ektopik hormonla en sık Cushing (küçük hücreli akciğer Ca → ACTH/POMC)"),
    ],
)
