# -*- coding: utf-8 -*-
"""Kaynak: Drive › Komite-1 › PDF › Farmakoloji › 2026-2027(yeni) › Akif Hakan Kurt › 3-İlaçların Metabolizması (32 slayt)"""

from yardim import B, C, Q  # noqa: F401

BOLUM = dict(
    key="metabolizma", baslik="İlaçların Metabolizması (Biyotransformasyon)",
    hoca="Prof. Dr. Akif Hakan Kurt", tarih="22 Eylül", saat="ADME · 4 saat",
    kaynak="3-İlaçların Metabolizması · Prof. Dr. A. H. Kurt · 2026",
    ozet=["22-23'ten 25-26'ya **her yıl 1 soru**, hepsi “hangisi **değildir**” kalıbı: üç yıl aynı soru (23-24, 24-25, 25-26) — **fazla katkıda bulunan mikrozomal CYP enzimlerinden biri değildir**; 22-23'te **biyotransformasyonla ilgili enzimatik olaylardan biri değildir**.",
          "Doğru şıklar = Tablo 5.3'teki **CYP1A2, CYP2C9, CYP2C19, CYP2D6, CYP3A4**. Çeldiriciler (listede yok): **CYP2E1, CYP2B9, CYP6D2**.",
          "Enzimatik olaylar: **Faz I = oksidasyon, redüksiyon, kopma**; **Faz II = konjugasyon**. Çeldirici: **hidroasilasyon**."],
    slaytlar=[
        [
            C("Biyotransformasyon — tanım", [
                B("**Biyotransformasyon (metabolizma)**: ilaçların **enzimlerin etkisi ile kimyasal değişikliklere** uğramasıdır. Oluşan ürüne **metabolit** denir."),
                B("İki şekilde oluşabilir: **1. Biyoinaktivasyon**, **2. Biyoaktivasyon**."),
            ]),
            C("1. Biyoinaktivasyon (detoksikasyon)", [
                B("**Etkili → etkisiz**: ilaçların **daha az etkili veya etkisiz** bileşikler haline dönüşmesi."),
                B("Bu yüzden bu biyotransformasyona **biyoinaktivasyon** veya **detoksikasyon** da denir."),
            ]),
            C("2. Biyoaktivasyon", [
                B("**Etkili → daha etkili veya toksik**; **etkisiz (ön-ilaç) → etkili**."),
                B("**Daha etkili** bileşik: **kodein → morfin**."),
                B("**Daha toksik** bileşik: **metil alkol → formaldehid ve formik asid**; **asetaminofen → N-asetil-p-benzokinonimin**."),
            ]),
            C("Ön-ilaç = inaktif prekürsör = prodrug", [
                B("Etkisiz bir bileşik vücutta biyotransformasyon sonucu **etkili** hale getirilir; etkisiz bileşiğe **ön ilaç (pro-drug, inaktif prekürsör)** denir."),
                B("**Kortizon ve prednizon** lokal uygulandıklarında etkisizdir; **sistemik** uygulanınca **karaciğerde** sırasıyla **hidrokortizon ve prednizolon**'a dönüşerek etkinlik kazanırlar."),
                B("Diğer örnekler: **karotenler (provitamin-A) → A vitamini**; **bakampisilin → ampisilin**; **enalapril → enalaprilat**."),
            ]),
        ],
        [
            C("Maksatlı olarak ön-ilaç yapma nedenleri", [
                B("**GİS absorbsiyonunu artırmak**: ADE inhibitörlerinin daha **lipofilik ön-ilaç** şeklinde yapılması."),
                B("**Uygulama yerinden absorbsiyonu yavaşlatmak**: bazı steroid hormonlar ve flufenazinin **enantat, dekanoat, sipiyonat** vb. esterleri."),
                B("**Po alımda acı tat** gibi hoşa gitmeyen nitelikleri maskelemek: **sülfizoksazol asetil** ve **kloramfenikol palmitat**."),
            ]),
            C("Tablo 5.1-A: Ön-ilaçlar → etkin metabolit", [
                B("**Kloralhidrat → trikloretanol** · **amitriptilin → nortriptilin**"),
                B("**Kortizon, prednizon → hidrokortizon, prednizolon** · **bekampisilin → ampisilin**"),
                B("**Enalapril, ramipril, silazapril vb. → enalaprilat, ramiprilat, silazaprilat**"),
                B("**Hint yağı → risinoleik asid** · **lovastatin → mevilonik asid**"),
                B("**Vitamin D3 → 1,25-dihidroksikolekalsiferol** · **sefuroksim aksetil → sefuroksim** · **klofibrat → klofibrik asid**"),
            ]),
        ],
        [
            C("Tablo 5.1-B: Gerek kendisi gerekse metaboliti etkin ilaçlar", [
                B("**Aspirin → salisilik asid** · **meperidin → normeperidin** · **imipramin → desmetilimipramin**"),
                B("**Klorpromazin → 7-hidroksiklorpromazin** · **diazepam → desmetildiazepam** · **kodein → morfin**"),
                B("**Dijitoksin → digoksin** · **losartan → EXP3174** · **prokainamid → N-asetilprokainamid** · **lidokain → de-etillidokain**"),
                B("**Nitrogliserin** ve **nitroprusiat → nitrik oksid** · **propranolol → 4-hidroksipropranolol**"),
                B("Tabloda her metabolit için etkinlik işareti verilmiştir: (F) ana ilaçtan **fazla**, (E) **eşit**, (A) **daha az**."),
            ]),
            C("Tablo 5.1-C: İlaçların etkisiz ürünlere dönüşümü", [
                B("**İlaçların çoğu** → **konjügasyon metabolitleri** (örn. glukuronatlar, N-asetil türevleri vb.)."),
                B("**Ester yapısındaki ilaçların çoğu** → **hidrolitik metabolitler**."),
                B("**Fenitoin** → parahidroksifenitoin · **katekolaminler** → **VMA, HVA** · **barbitüratlar** → yan zincirden oksidlenmiş metabolitler."),
            ]),
            C("Biyotransformasyonun genel sonuçları", [
                B("İlaçlar **daha polar** hale gelirler; **lipid/su partisyon katsayıları azalır**; **suda çözünürlükleri artar**."),
                B("Sonuç: vücuttan **daha kolay atılır** hale gelirler."),
            ]),
        ],
        [
            C("Değişmeden atılan ilaçlar", [
                B("**Çok az sayıda ilaç** vücutta **değişmeden** atılır: azot protoksid, **asetazolamid, amilorid, furosemid**, aminokaproik asid, kromoglikat, pentolinium."),
            ]),
            C("Ksenobiyotikler", [
                B("Vücutta sadece ilaçlar değil, **diğer bütün ksenobiyotikler** de biyotransformasyona uğrar."),
                B("Bazı ksenobiyotikler: **besin aditifleri, insektisid ve fungusid artıkları, hava ve suyu kirleten atıklar, egzoz ve sigara dumanı**."),
            ]),
            C("Biyotransformasyon yapan enzimlerin yerleşimi", [
                B("Bazıları az veya çok **tüm hücrelerde**; büyük kısmı belirli organlarda: **karaciğer, akciğer, böbrek, mide-barsak mukozası, kan** ve diğer yapılar; ayrıca **barsak florasındaki bakterilerin** enzimleri."),
                B("Metabolizmada **başrol oynayan organ karaciğerdir**; burada en önemli fraksiyon **mikrozomal enzimlerdir**."),
            ]),
            C("Enzimatik-olmayan biyotransformasyon", [
                B("**Çok az sayıda** ilaç nonenzimatik biyotransformasyona uğrar."),
                B("Örnekler: **mide asid ortamında kısmen parçalanan penisilin G**; **kan pH'sında parçalanan atroküryum**."),
            ]),
        ],
        [
            C("Enzimatik olaylar iki fazda gerçekleşir", [
                B("**I. Faz reaksiyonları**: **oksidasyon, redüksiyon, kopma**. Genellikle daha **polar bir grup** oluşur.", y="22-23", tuzak="“Hidroasilasyon biyotransformasyonla ilgili enzimatik olaylardan biridir” → YANLIŞ"),
                B("**II. Faz reaksiyonları**: **konjugasyon**. Esterleşme veya eterleşme sonucu **maskelenmiş polar bir grup**, kırılma sonucu açığa çıkar.", y="22-23"),
            ]),
            C("1. Oksidasyon — sitokrom P450 (CYP) enzimleri", [
                B("Büyük kısmı **karaciğer parankim hücresinin mikrozomal sitokrom P450 (CYP)** enzimleri tarafından yapılır."),
                B("**Karma fonksiyonlu oksidazlar** veya **monooksijenazlar** adını da alırlar; ilaç molekülüne **oksijen sokarlar**."),
                B("Bu sistemle eşgüdümlü çalışan **NADPH-sitokrom P450 redüktaz** sistemi vardır."),
                B("Enzimlerin **aktif noktası demir iyonudur (Fe3+)**."),
            ]),
            C("CYP katalitik döngüsü (slayttaki şema)", [
                B("**İlaç (RH) bağlanır** → **NADPH ile Fe3+ → Fe2+ indirgenir** → **O2 bağlanır** → **ikinci elektron + 2H+** → **ürün (R-OH) + H2O ayrılır**."),
            ]),
        ],
        [
            C("Başlıca mikrozomal CYP enzimleri ve katkı yüzdeleri", [
                B("**CYP3A4 %57**: ilaçların **%55-60'ının** oksidasyonuna katkıda bulunur.", y="23-24 24-25 25-26"),
                B("**CYP2D6 %25**: ilaçların yaklaşık %25'i.", y="23-24 24-25"),
                B("**CYP2C grubu %15**: ilaçların yaklaşık %15'i.", y="23-24 24-25 25-26"),
            ]),
            C("Tablo 5.3 — önemli CYP enzimleri", [
                B("Başlık: **metabolize ettiği ilaç veya ksenobiyotik sayısının fazlalığı nedeniyle** önemli olan bazı sitokrom P450 enzimleri.", y="23-24 24-25 25-26"),
                B("Tablodaki enzimler: **CYP1A2, CYP2C9, CYP2C19, CYP2D6, CYP3A4**.", y="23-24 24-25 25-26", tuzak="“CYP2E1 / CYP2B9 / CYP6D2 fazla katkıda bulunan mikrozomal enzimlerdendir” → YANLIŞ"),
            ]),
            C("Genetik polimorfizm ve CYP yerleşimi", [
                B("Bireyler arasında **enzim miktarı ve etkinliği** bakımından **genetik polimorfizme** bağlı değişkenlik vardır."),
                B("**CYP3A4**'ün **KC'deki miktarı** bireyler arasında **20 kattan fazla** değişkenlik gösterebilir."),
                B("CYP3A4 **barsak epitel hücrelerinde** de bulunur; bireyler arası farklılık **11 kata kadar** çıkabilir."),
                B("CYP sistemleri birçok organ ve dokuda bulunur; özellikle **KC sentrolobüler bölgedeki hücrelerin düz endoplazmik retikulumu** üzerinde yerleşmiştir."),
            ]),
        ],
        [
            C("Tablo 5.3 — CYP enzimlerinin substratları (1)", [
                B("**CYP1A2**: antidepresanlar (imipramin, klomipramin), **ksantinler (kafein, teofilin)**, polisiklik aromatik hidrokarbonlar, parasetamol, propranolol, varfarin.", y="23-24 24-25 25-26"),
                B("**CYP2C9**: **fenitoin**, fluvastatin, lozartan, irbesartan, oral antidiyabetikler (glipizid, glibenklamid, tolbutamid), **NSAİ analjezikler** (diklofenak, flurbiprofen, ibuprofen, indometasin, naproksen, piroksikam), varfarin.", y="24-25 25-26"),
                B("**CYP2C19**: antidepresanlar (amitriptilin, imipramin, klomipramin), **diazepam**, **proton pompası inhibitörleri** (lansoprazol, omeprazol), propranolol.", y="23-24 25-26"),
                B("**CYP2D6**: trisiklik antiaritmikler (meksiletin, propafenon); **beta-blokörler** (metoprolol, propranolol, timolol); nikotin.", y="23-24 24-25"),
                B("Antidepresanlar: amitriptilin, fluoksetin, fluvoksamin, imipramin, klomipramin, maprotilin, trazodon, venlafaksin.", lvl=1),
                B("**Nöroleptikler** (haloperidol, tioridazin); **opioid analjezikler** (dekstrometorfan, kodein, tramadol).", lvl=1),
            ]),
        ],
        [
            C("Tablo 5.3 — CYP3A4 substratları (en geniş liste)", [
                B("**CYP3A4**: antiandrojenler (finasterid, flutamid), antiaritmikler (amiodaron, dizopiramid, kinidin, lidokain), antihistaminikler (astemizol, loratadin, terfenadin).", y="23-24 24-25 25-26"),
                B("Antineoplastikler (siklofosfamid, doksorubisin, etopozid, ifosfamid, paklitaksel, vinblastin, vinkristin); **azol antifungaller** (itrakonazol, ketokonazol, mikonazol).", lvl=1),
                B("**Benzodiazepinler** (alprazolam, diazepam, midazolam, triazolam); **eritromisinler** (eritromisin, klaritromisin); ergot bileşikleri (bromokriptin, ergotamin); dapson; etinil estradiol; glitazonlar.", lvl=1),
                B("**Glukokortikoidler** (deksametazon, metilprednizolon, prednizolon, prednizon); **hipolipidemik ilaçlar** (atorvastatin, lovastatin, simvastatin).", lvl=1),
                B("**Kalsiyum kanal blokörleri** (amlodipin, nimodipin, nifedipin, nikardipin, nitrendipin, nizoldipin, verapamil); karbamazepin; kinin; kinidin; losartan; nefazodon.", lvl=1),
                B("**Opioid analjezikler** (alfentanil, fentanil); busiron; **indinavir ve diğer HİV proteaz inhibitörleri**; siklosporin; sisaprid; tamoksifen; testosteron; varfarin; zolpidem.", lvl=1),
            ]),
        ],
        [
            C("CYP enzimlerinin yaptığı oksidlenme olayları (I)", [
                B("**Aromatik halkanın hidroksillenmesi**: katalizleyen enzim **CYP1A ailesinden aril hidrokarbon hidroksilaz (AHH)** (aromatik hidrokarbonlar, steroid hormonlar, benzen türevleri...)."),
                B("**Alifatik hidroksilasyon (yan zincir oksidlenmesi)**: **barbitüratlar**."),
                B("**Diğer hidroksilasyonlar**: mikrozomal oksidazlar (piridin, kumarin, kinolin...)."),
                B("**N-, O-, S-dealkilasyon**: mikrozomal enzimler. **Kodein, O-demetilasyonla morfine**; **kafein, N-demetilasyonla kısmen teofiline** dönüşür."),
            ]),
            C("CYP enzimlerinin yaptığı oksidlenme olayları (II)", [
                B("**Desülfürasyon (kükürtsüzlenme)**: **tiopental → pentobarbital**, **paration → paraokson**."),
                B("**S-oksidasyon (sülfoksid oluşumu)**: **klorpromazin** ve diğer fenotiazinler."),
                B("**N-oksidasyon ve N-hidroksilasyon**: sekonder ve aromatik aminlerin hidroksilasyonu. Anilinden fenilhidroksilamin, nitrobenzenden benzen oluşumu."),
            ]),
            C("Mikrozomal-olmayan enzimlerin yaptığı oksidasyon", [
                B("Önemli mikrozomal-olmayan enzimler: **MAO (monoaminooksidaz), diamin oksidaz (histaminaz), ksantin oksidaz, tirozin hidroksilaz, alkol dehidrogenaz, aldehid dehidrogenaz**."),
                B("Bunlar **sitoplazmik** enzimlerdir."),
            ]),
        ],
        [
            C("2. İndirgenme (= redüksiyon)", [
                B("**NADPH, FAD ve diğer flavinlerin** yardımıyla olur."),
                B("Olayların çoğu **aldehidlerin alkollere** dönüşümüdür (örn. **kloral hidrat → trikloretanol**)."),
                B("**Azo (N=N) grubunun aminlere** dönüşümü: örn. **prontosil → sülfonamid**."),
                B("**Nitro gruplarının amin veya hidroksilamin** grubuna dönüşümü: örn. **kloramfenikolun inaktivasyonu** bu şekilde olur."),
            ]),
            C("3. Kopma (I) — hidroliz", [
                B("**Kopma**: ya ilaç molekülünden **bir grubun koparılması** ya da molekülü oluşturan **daha ufak moleküllere ayrılması** şeklinde olur."),
                B("**Hidroliz**: **esterazlar**, **peptidazlar** (proinsülin) ya da **amidazlar** (prokainamid, indometazin, lidokain) tarafından yapılır."),
                B("Esterazlar: **asetilkolin esteraz, psödokolin esteraz** (asetilkolin, süksinilkolin, prokain, aspirin...).", lvl=1),
            ]),
            C("3. Kopma (II) — dekarboksilasyon ve diğerleri", [
                B("**Dekarboksillenme**: çeşitli **dekarboksilaz** enzimlerin yardımıyla (5-hidroksitriptofan, histidin, **L-Dopa**...)."),
                B("**Glikozidlerin hidrolizi**: örn. **dijital glikozidlerinin beta-glukuronidaz** tarafından biyotransformasyonu."),
                B("**N-, O-, S-dealkilasyon** da kopma şeklinde gerçekleşebilir."),
            ]),
        ],
        [
            C("4. Konjugasyon — genel", [
                B("Bir ilaç veya metabolitinin molekülüne **bir radikalin veya endojen bir molekülün kovalent bağla** bağlanmasıyla olur."),
                B("**8 çeşidi** vardır; **ilki hariç** diğerleri **mikrozomal olmayan** enzimlerle yapılır."),
                B("Olaya **konjugasyon**, ürünlere **konjugat** denir; konjugatlar genellikle **daha kolay atılabilen polar maddelerdir**."),
            ]),
            C("1. Glukuronik asidle birleşme", [
                B("**UDP-glukuronil transferaz** ile yapılır; **mikrozomal** bir enzimdir (kloramfenikol, salisilik asid, morfin...)."),
                B("Glukuronatlar genellikle **inaktiftir**; kısmen **böbreklerden**, kısmen **karaciğer hücreleri tarafından safra içine** itrah edilir."),
                B("**Enterohepatik siklus**: safra ile barsağa gelen konjugatlar barsak lümenindeki **beta-glukuronidaz** ile hidroliz edilir; serbest ilaç absorbe edilip **portal dolaşımla KC hücrelerine** erişir."),
                B("Bu olay **ilaç etkisini önemli ölçüde uzatır**.", lvl=1),
            ]),
            C("Enterohepatik siklus (slayttaki şema)", [
                B("**Karaciğer** (glukuronid konjugasyonu) → **safra** (konjugat itrahı) → **barsak lümeni** (β-glukuronidaz ile hidroliz) → **serbest ilaç** → **portal dolaşım**."),
            ]),
        ],
        [
            C("2-3-4. Metilasyon ve asetilasyon", [
                B("**2. N-metilasyon**: **N-metil transferaz**; örn. noradrenalinden **feniletanolamin N-metil transferaz** ile **adrenalin** oluşması."),
                B("**3. O-metilasyon**: **O-metil transferaz**; örn. **adrenalin ve noradrenalinin COMT ile inaktivasyonu**."),
                B("**4. N-asetilasyon**: **N-asetil transferaz (NAT)**. Genetik nedenlerle bu enzimin az olduğu kişilere **“yavaş asetilleyiciler”** denir (histamin, **izoniazid**, sülfonamidler...)."),
            ]),
            C("5-8. Diğer konjugasyonlar", [
                B("**5. Sülfatasyon**: **sülfotransferaz**; örn. sülfonamidler, **östrojenler, asetaminofen**."),
                B("**6. Glutatyon ile konjugasyon**: **glutatyon-S-transferaz**; örn. aromatik hidrokarbonlar, aromatik nitro bileşikleri."),
                B("**7. Amino asidle konjugasyon**: **glisin veya glutamin** ile (örn. benzoik asidten glisin ile **hipürik asid**)."),
                B("**8. Diğer**: **purin ve pirimidin analoğu** ilaçlar riboz ve riboz fosfatlarla **ribonukleozid ve ribonukleotid** konjugatlarına dönüşür."),
            ]),
        ],
        [
            C("Mikrozomal enzim indüksiyonu / inhibisyonu", [
                B("**Enzim indüksiyonu**: mikrozomal bir enzimin **substratı olan bir madde tarafından sentezinin arttırılması** (ya da yıkımının yavaşlatılması)."),
                B("**Enzim inhibisyonu**: enzimin inhibe edilmesi."),
                B("**İndüksiyonun pratik önemi**: bu enzimlerle inaktive edilen ilaçların **yıkımı artar, etkinliği azalır**."),
                B("**İnhibisyonun pratik önemi**: ilaçların inaktivasyonu önlenir, **farmakolojik etkileri güçlenir**, plazma düzeyleri **toksik seviyelere** çıkabilir."),
            ]),
            C("Plazma düzeyine etkisi (slayttaki grafik)", [
                B("Aynı doz, aynı ilaç: **enzim inhibisyonu** → yavaş yıkım, **yüksek düzey**; **enzim indüksiyonu** → hızlı yıkım, **düşük düzey**."),
            ]),
            C("Oto-indüksiyon, intihar tipi inhibitör, enzim aktivasyonu", [
                B("**Oto-indüksiyon**: bazı ilaçlar kendilerini yıkan enzimleri indükler, kendi inaktivasyonlarını hızlandırır: **karbamazepin, barbitüratlar, alkol**."),
                B("**İntihar (suicide) tipi inhibitörler**: ilaç CYP ile reaktif ara ürüne oksidlendikten sonra enzimi **irreversibl inaktive** eder: **etinil estradiol, kloramfenikol, sekobarbital**."),
                B("**Enzim aktivasyonu**: ilaç tarafından **enzim sentezi arttırılmaksızın** enzim etkinliğinin arttırılmasıdır."),
            ]),
        ],
        [
            C("Tablo 5.5 — İndükleyiciler ve inhibitörler (CYP1A2, 2C9)", [
                B("**CYP1A2 indükleyiciler**: **sigara dumanı**, kömürde kızarmış ve polisiklik aromatik hidrokarbonlar, fenitoin."),
                B("**CYP1A2 inhibitörler**: enoksasin, etinil estradiol, **fluvoksamin, simetidin, siprofloksasin**."),
                B("**CYP2C9 indükleyiciler**: **barbitüratlar, fenitoin, karbamazepin, rifampisin**."),
                B("**CYP2C9 inhibitörler**: amiodaron, disülfiram, fenitoin, **flukonazol**, fluoksetin, fluvoksamin, izoniazid, itrakonazol, ketokonazol, ko-trimoksazol, metronidazol, simetidin, sulfafenazol, tiklopidin."),
            ]),
            C("Tablo 5.5 — CYP2C19 ve CYP2D6", [
                B("**CYP2C19 ve CYP2D6**: **indüklenebilir değil**."),
                B("**CYP2C19 inhibitörler**: flukonazol, fluoksetin, fluvoksamin, **omeprazol**, tiklopidin."),
                B("**CYP2D6 inhibitörler**: amiodaron, antidepresanlar (fluoksetin, paroksetin, sertralin), **kinidin**, mibefradil, nöroleptikler (haloperidol, tioridazin), simetidin, terbinafin, metoksalen."),
                B("Klasik antihistaminikler (difenhidramin, klorfeniramin, klemastin, hidroksizin, prometazin, tripelenamin) de CYP2D6 inhibitörleridir.", lvl=1),
            ]),
        ],
        [
            C("Tablo 5.5 — CYP3A4 indükleyiciler", [
                B("**Aminoglutetimid, barbitüratlar**, deksametazon ve diğer bazı kortikosteroidler, **fenitoin, grizeofulvin, karbamazepin**, pioglitazon, **rifampisin**, rifabutin."),
            ]),
            C("Tablo 5.5 — CYP3A4 inhibitörler", [
                B("**Antidepresanlar** (fluvoksamin, nefazodon); **azol antifungaller** (itrakonazol, ketokonazol, mikonazol, oksikonazol, daha az olmak üzere flukonazol)."),
                B("**Eritromisinler** (eritromisin, klaritromisin, troleandomisin); danazol; etinil estradiol; bazı kortikosteroidler (metilprednizolon, prednizolon, prednizon)."),
                B("**Greyfurt suyu**, kırmızı şarap, izoniazid, kinin, norfloksasin."),
                B("**Kalsiyum kanal blokörleri** (nifedipin, nikardipin ve olasılıkla diğer dihidropiridinler, diltiazem, verapamil)."),
            ]),
        ],
    ],
    sorular=[
        Q("25-26", 20, "İlaç metabolizmasına fazla katkıda bulunan mikrozomal enzimlerden hangisi DEĞİLDİR? (2C9 / 1A2 / 2C19 / 3A4 / 6D2)", "e) CYP6D2",
          "Tablo 5.3'teki önemli CYP'ler: 1A2, 2C9, 2C19, 2D6, 3A4; CYP6D2 listede yok."),
        Q("24-25", 29, "İlaç metabolizmasına fazla katkıda bulunan mikrozomal enzimlerden hangisi DEĞİLDİR? (2C9 / 1A2 / 2E1 / 3A4 / 2D6)", "c) CYP2E1",
          "Tablo 5.3'teki önemli CYP'ler: 1A2, 2C9, 2C19, 2D6, 3A4; CYP2E1 listede yok."),
        Q("23-24", 15, "İlaç metabolizmasına fazla katkıda bulunan mikrozomal enzimlerden hangisi DEĞİLDİR? (3A4 / 2D6 / 2C19 / 1A2 / 2B9)", "e) CYP2B9",
          "Tablo 5.3'teki önemli CYP'ler: 1A2, 2C9, 2C19, 2D6, 3A4; CYP2B9 listede yok."),
        Q("22-23", 26, "Biyotransformasyonla ilgili enzimatik olaylardan hangisi DEĞİLDİR? (oksidasyon / kopma / redüksiyon / konjugasyon / hidroasilasyon)", "e) Hidroasilasyon",
          "Faz I: oksidasyon, redüksiyon, kopma; Faz II: konjugasyon. Hidroasilasyon slaytlarda yok."),
    ],
)
