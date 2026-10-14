# -*- coding: utf-8 -*-
"""Kaynak: Drive › Komite-1 › PDF › Farmakoloji › 2026-2027(yeni) › Akif Hakan Kurt › 7-Antikoagülan İlaçlar"""

from yardim import B, C, Q  # noqa: F401

BOLUM = dict(
    key="antikoagulan", baslik="Antikoagülan İlaçlar",
    hoca="Prof. Dr. Akif Hakan Kurt", tarih="5 Ekim", saat="2 saat",
    kaynak="7-Antikoagülan İlaçlar · Prof. Dr. A. H. Kurt · 2026",
    ozet=["Her yıl **heparin / DMAH etki mekanizması** soruldu (21-22, 22-23, 23-24, 24-25): heparin = **antitrombin III aktivasyonu**; DMAH = **faktör Xa** (XIIa, Xa, kallikrein) inhibisyonu.",
          "Çeldirici şık: “**antitrombin III reseptörlerinin antagonizması**”, ADP reseptör blokajı, fosfodiesteraz aktivasyonu, faktör VII/IXa/XIa.",
          "25-26: **‘hangisi doğrudur’ karması** — DMAH, fondaparinux, lepirudin, varfarin etkileşimleri ve **argatroban/dabigatran** karıştırması."],
    slaytlar=[
        [
            C("Tanımlar (slayttaki ifadeyle)", [
                B("**Antitrombotik**: oluşmuş pıhtıyı eritir. **Antikoagülanlar**: **trombus (damar içi pıhtı)** oluşmasını ve gelişmesini inhibe eder."),
                B("Etki: pıhtılaşma faktörlerinin **sentezini bozarak**, **antikoagülan faktör etkinliğini artırarak** veya pıhtılaşma faktörlerinin **etkinliğini bozarak** koagülasyon yeteneğini azaltırlar."),
            ]),
            C("Pıhtılaşmayı engellemek için 2 grup ilaç", [
                B("1- **Heparin**: **antitrombin III etkinliğini artırarak** ve bazı pıhtılaşma faktörlerini inaktive ederek etkilidir.", y="21-22 23-24"),
                B("2- **K vitamini antagonistleri**: karaciğerde K vitaminine bağımlı **protrombin, faktör VII, IX ve X** sentezinin esas olarak **son basamağını** bozar."),
            ]),
            C("Heparinin yapısı", [
                B("**Sığır akciğerinden** ve **domuz ince barsak mukozasından** elde edilir; lineer zincirli kompleks **sülfatlanmış polisakkarit (glukozaminoglikan)**."),
                B("İlaç olarak **5.000-30.000 (ortalama 12.000) dalton** arası heparin fragmentlerinin **heterojen karışımı**."),
                B("Etkinlik, elde edildiği kaynağa ve karışımdaki öğelerin **molekül ağırlığına** göre değişir."),
            ]),
        ],
        [
            C("Heparinin etki mekanizması", [
                B("Heparin **antitrombin III'e (heparin kofaktörü)** sıkıca bağlanır ve **aktif hale getirir**.", y="21-22 23-24", tuzak="“Antitrombin III reseptörlerinin antagonizması” → YANLIŞ"),
                B("Antitrombin III, aktif merkezinde **reaktif serin rezidüsü** bulunan aktif proteaz faktörlerini inhibe eder: **trombin, XIIa, XIa, Xa, IXa, kallikrein**."),
                B("Antikoagülan etkiye **en fazla katkı**: **trombin ve faktör Xa** inhibisyonu."),
                B("Aktif AT-III: **1-** trombin oluşumunu azaltır, **2-** trombinin fibrinojen üzerindeki etkilerini inhibe eder."),
                B("Ayrıca damar endotelinde birikerek **elektronegatif yük** oluşturur."),
            ]),
            C("Heparin dozunun titre edilmesi", [
                B("Heparin etkinliği **aPTZ** ile değerlendirilir; normal **24-36 sn**; tedavide **1,5-2,5 misli uzama** hedeflenir."),
                B("**aKZ**: VII dışındaki faktörler · 80-130 sn · izlenen ilaç **heparin**."),
                B("**aPTZ**: VII dışındaki faktörler · 24-36 sn · **heparin ve oral antikoagülanlar**."),
                B("**PZ**: II, V, VII, X · 11-12 sn · **oral antikoagülanlar**."),
            ]),
            C("Heparin ünitesi", [
                B("Etkinlik **biyolojik ünite** ile belirlenir: 1 Ü = **0 °C'de 1 ml kedi kanının pıhtılaşmasını 24 saat önleyen** miktar; müstahzarlarda **1 ml'de 5000 Ü**."),
                B("**Anti-Xa (AXa) ünitesi**: **DMAH**'lerin etkinliği bununla ölçülür."),
            ]),
        ],
        [
            C("Düşük molekül ağırlıklı heparin (DMAH) — genel", [
                B("Standart heparinin **yararlılığını artırmak, sakıncalarını azaltmak** için **1980'lerde** üretildi."),
                B("Heparinin polisakkaritlerinin **depolimerizasyonu** veya standart heparinin **fraksiyonlanması** ile elde edilir (**MA 5000-8000** veya daha az)."),
                B("**Dalteparin** (Fragmin), **enoksaparin** (Clexane), **nadroparin** (Fraxiparin), parnaparin (Flaxum), tinzaparin (İnnohep), bemiparin, reviparin, sertoparin, ardeparin."),
            ]),
            C("DMAH — etki mekanizması", [
                B("Damar endotelinden **daha az lipoprotein lipaz** salıverirler."),
                B("Antitrombin III tarafından **faktör XIIa, Xa ve kallikreinin inhibe edilmesini potansiyalize** eder; **IXa ve XIa'nın** inhibisyonunu **değiştirmez**.", y="22-23 24-25", tuzak="“Faktör IXa / XIa inhibisyonu” ve “faktör VIIa inhibisyonu” → YANLIŞ"),
                B("**Pıhtılaşma zamanını çok az değiştirerek**, olasılıkla kanamaya neden olmaksızın **trombus oluşmasını engeller**.", y="25-26"),
            ]),
            C("Anti-faktör Xa / anti-faktör IIa oranı", [
                B("DMAH'de oran **daha yüksek (4:1, 2:1)**; standart heparinde **1:1**."),
                B("Nedeni: bayağı heparin AT III-trombin kompleksinde **her ikisine** bağlanır; **DMAH sadece AT III'e** bağlanır."),
                B("**Trombosit yüzeyine bağlı faktör Xa** bayağı heparine **dirençli**, **DMAH ile inhibe edilebilir**."),
            ]),
        ],
        [
            C("DMAH'in klinik üstünlükleri", [
                B("**Kanamaya daha az neden olur**: antitrombin etkinliği düşük; **vWf ile kompleks yapma eğilimi düşük** → mikrovasküler kanama eğilimi azalır."),
                B("Standart tedavi protokollerinde **izlem testine gerek yok**."),
                B("s.c. / i.v. **biyoyararlanım daha yüksek**; plazmada serbest (aktif) fraksiyon daha yüksek, **plazmada daha uzun kalır**."),
                B("**Heparinle indüklenen trombositopeni** ve **osteopeni** riski daha düşük."),
            ]),
            C("DMAH'in dezavantajları", [
                B("Aşırı dozda kanama olursa etkisi **hemen sonlanmaz**; **protamin sülfat** etkilerini **kısmen** nötralize eder."),
                B("**Gebelikte** güvenliği ve etkililiği yeterince değerlendirilmemiştir."),
            ]),
            C("Heparin preparatları", [
                B("**Heparin sodyum**: eskiden beri kullanılan **bayağı heparin** (sığır AC, domuz barsak mukozası)."),
                B("**Heparin kalsiyum**: domuz barsağı mukozasından; Ca tuzu; tromboembolizm proflaksisinde **düşük doz** uygulamalarında tercih edilir."),
                B("**DMAH**: antitrombin etkisi düşük, **anti-Xa etkisi güçlü**, aPTZ'yi uzatma yeteneği düşük; doz titrasyonu için **anti-Xa aktivite testi** kullanılır."),
            ]),
        ],
        [
            C("Heparin farmakokinetiği", [
                B("Sindirim kanalından **absorbe edilmez**, sadece **parenteral**; hemen etki için **i.v.**, proflaksi için **s.c.**"),
                B("Damar endotelindeki konsantrasyonu plazmadakinin **100 katı** olabilir."),
                B("Plazma yarılanma ömrü dozuna göre (**doyurulabilir kinetik**) **½-3 saat**."),
                B("Eliminasyon: **retiküloendotelyal sistem** hücreleri. Gebelerde **fötal dolaşıma geçmez**."),
            ]),
            C("Uygulama şekilleri", [
                B("**DVT** ve ona bağlı AC tromboembolizmi: **heparin DMAH'lere tercih edilir** (DMAH de kullanılabilir)."),
                B("Yüksek riskli hastalar (**obezler, 40 yaş üstü, malign tümörlü**) ameliyat sonrası DVT proflaksisi: **DMAH tercih edilir**, normal tedavi dozundan **düşük dozda s.c.**; bayağı heparin de kullanılabilir."),
                B("Ağır tromboembolik olaylarda heparine başlanırken **varfarine de başlanır**."),
            ]),
            C("Heparin rezistansı", [
                B("Seyrek; çok yüksek doz (**50.000 Ü/gün**) ancak etki eder."),
                B("Nedenler: **faktör VIII yüksekliği**; **heparin klirensinin hızlanması** (masif AC embolizmi); **AT-III eksikliği**."),
                B("AT-III eksikliği: **kalıtsal** (normalin %40-60'ı); **nefrotik sendrom, siroz** (%25'in altı)."),
            ]),
        ],
        [
            C("Heparinin yan tesirleri", [
                B("En önemlisi aşırı dozda **spontan kanama**; mutad dozlarda **purpura, ekimoz, melena, hematüri**."),
                B("Yüksek dozda uzun süreli kullanım → **osteoporoz**."),
                B("**Kısa süreli hafif trombositopeni** (2-5 gün) ve **geç trombositopeni** (5-10 gün sonra)."),
                B("1 haftadan uzun tedavide **aldosteron salgısını azaltarak hiperkalemi**."),
            ]),
            C("Antidot — protamin sülfat", [
                B("Kanamada heparin kesilir; **protamin sülfat** yavaş i.v. enjeksiyon / infüzyon ile verilir."),
                B("Protamin: **balık spermasından** elde edilen, **argininden zengin → bazik** protein."),
                B("**Asidik** heparinle **kompleks oluşturup inaktif** hale getirir."),
                B("Protamin alerjisinde **toluidin mavisi** veya **heksadimetrin** kullanılabilir."),
            ]),
            C("Fondaparinux (sentetik heparin türevi; ARIXTRA)", [
                B("Antitrombin aracılığıyla **faktör Xa inhibisyonu**, **trombin inhibisyonu yapmaz** (kısa polimer uzunluğu nedeniyle).", y="25-26"),
                B("s.c.; **2 saatte doruk** düzey; **t½ = 17-21 saat**. Pıhtılaşma **izlemi gerekmez**."),
                B("Heparin ve DMAH'den **daha az HIT** (heparinle indüklenen trombositopeni) yapar."),
                B("Endikasyon: **kalça / diz cerrahisi** tromboproflaksisi, pulmoner embolizm, DVT."),
            ]),
        ],
        [
            C("Diğer parenteral antikoagülanlar", [
                B("**Lepirudin**: sülüğün tükrük bezindeki **hirudinin (direkt trombin inhibitörü) rekombinant türevi**; böbrekten atılır, **aPTZ izlemi** gerekir, **antidotu yoktur**; **HIT'li hastalarda tercih** edilir.", y="25-26"),
                B("**Bivalirudin**: lepirudine benzer mekanizma; **böbrek yetmezliğinde doz ayarı**; **koroner anjiyoplastide heparine alternatif**."),
                B("**Argatroban**: **L-arjinin yapısına benzer sentetik** bileşik; **trombinin katalitik bölgesine reversibl** bağlanır; HIT riski olanlarda lepirudin alternatifi; **KC'de metabolize** edilir.", tuzak="“Dabigatran, L-arjinin yapısına benzer sentetik bileşik olup trombinin katalitik bölgesine reversibl bağlanır” → YANLIŞ (bu argatroban)", y="25-26"),
            ]),
            C("Oral antikoagülanlar — genel", [
                B("Sentez yoluyla üretildiklerinden heparine göre **ucuz**."),
                B("Etki **24 saat sonra** başlar (önceden sentezlenmiş faktörlerin etkisi sürdüğü için); tedavi kesilince etki **birkaç gün** daha devam eder."),
                B("**PZ daha sık** bakılmalı: **KC fonksiyon bozukluğu, KKY, sık diyare, diyetle K vitamini alımı artmış/azalmış** durumlar."),
            ]),
        ],
        [
            C("Varfarin — mekanizma ve farmakokinetik", [
                B("**Varfarin ve dikumarol** (kumarin antikoagülanlar): **K vitamininin kofaktör fonksiyonlarını bozarak** pıhtılaşma faktörlerinin çoğunun **karaciğerde sentezini azaltır**."),
                B("**Teratojenik**, düşüğe neden olabilir → **hamilelerde kesinlikle kullanılmaz**."),
                B("Kişiler arası değişkenlik fazla (günlük doz **4 kata kadar**); metabolizma **CYP2C9** (belirgin genetik polimorfizm); **doz bireyselleştirilmeli**."),
                B("Plazma proteinlerine **%97-98** bağlanır; **sütle bebeğe geçebilir**."),
            ]),
            C("Varfarin etkileşmeleri", [
                B("**Barbitüratlar, bazı antiepileptikler**: CYP **indükler** → etkiyi **azaltır**."),
                B("**Antidepresanlar, antifungaller, makrolid antibiyotikler, omeprazol**: KC enzimlerini **inhibe** eder → etkiyi **artırır**.", y="25-26"),
                B("**Asidik ilaçlar** (aspirin, fenilbutazon, diklofenak, sulfanilüreler): albüminden **serbestleştirerek** etkiyi artırır."),
                B("**Geniş spektrumlu antibiyotikler**: barsakta K vitamini yapan bakterileri azaltarak etkiyi artırır."),
            ]),
        ],
        [
            C("Varfarin yan tesirleri ve kontrendikasyonlar", [
                B("Sık: aşırı dozda **spontan kanama**. Plasentadan fetusa **kolayca geçer**."),
                B("**Varfarin sendromu**: yarık dudak-damak, nazal hipoplazi, büyüme geriliği, mental retardasyon, körlük, hidrosefalus."),
                B("**Kontrendikasyon**: kanama eğilimi yaratan lezyon / hastalık; hemostaz bozukluğu olan kan hastalıkları; ağır HT, peptik ülser; özafagus varisleri, arteryel anevrizma; **PZ bakılamıyorsa**; büyük cerrahi girişim."),
            ]),
            C("Heparin ve oral antikoagülanların klinik kullanımı", [
                B("**Derin ven trombozu**; **akut MI** ve diğer koroner sendromlar (nekroz bölgesinde trombus önleme)."),
                B("**Romatizmal kalp kapakçığı**; **atriyum fibrilasyonunda** tromboemboli önleme; kalp kapağı protezleri ve bypass sonrası; iskemik tromboembolik inme."),
                B("**Gebelikte** tromboemboli riski varsa **heparin tercih edilir**."),
                B("Kardiyopulmoner kateterizasyon, hemodiyaliz, organ transplantasyonu."),
            ]),
        ],
        [
            C("Yeni nesil oral antikoagülanlar", [
                B("**Dabigatran** (PRADAXA): **spesifik, yarışmalı direkt trombin inhibitörü**, bir **ön ilaç**.", tuzak="“L-arjinin yapısına benzer sentetik bileşik” → YANLIŞ (argatroban)", y="25-26"),
                B("Dabigatran: ketokonazol, itrakonazol, vorikonazol, posakonazol, rifampisin, karbamazepin, fenitoin, fenobarbital ile birlikte **kontrendike**.", lvl=1),
                B("Dabigatran: FDA onaylı doz **2 × 150 mg**; **2 × 110 mg** = **80 yaş üstü** ve kanama riski olanlar.", lvl=1),
                B("**Apiksaban** (ELIQUIS): **reversibl, kompetitif, direkt faktör Xa aktif bölge inhibitörü**; besinlerle veya tek başına alınır; yaklaşık **5 mg günde 2 kez**."),
                B("**Rivaroksaban** (XARELTO): **faktör Xa'yı engeller**; **günde 1 kez 20 mg**; böbrek problemi varsa **15 mg**'a düşürülebilir."),
                B("**Edoksaban** (LİXİANA): **faktör Xa'yı engeller**; **günde 1 kez 60 mg**."),
            ]),
        ],
    ],
    sorular=[
        Q("25-26", 23, "Antikoagülan ilaçlar için hangisi doğrudur? (dabigatran/DMAH/fondaparinux/lepirudin/varfarin)",
          "B, C, D, E PDF'e göre doğru (A yanlış)",
          "A = argatroban tanımı (dabigatran: direkt trombin inh. ön ilaç). Kök muhtemelen ‘yanlıştır’ ya da çoklu doğru; anahtar belirsiz."),
        Q("24-25", 32, "DMAH'nin antikoagülan etki mekanizmalarından biri hangisidir?",
          "Faktör Xa inhibisyonu",
          "DMAH: AT III aracılı XIIa, Xa, kallikrein inhibisyonu; IXa/XIa değişmez. Trombin/IIa aktivasyonu çeldirici."),
        Q("23-24", 18, "Heparinin antikoagülan etki mekanizması hangisidir?",
          "Antitrombin III aktivasyonu",
          "Çeldiriciler: AT III reseptör antagonizması, ADP reseptör blokajı, fosfodiesteraz aktivasyonu, faktör VIIa inhibisyonu."),
        Q("22-23", 29, "DMAH'nin esas antikoagülan etki mekanizması hangisidir?",
          "Faktör XIIa, Xa ve kallikrein inhibe edilmesi",
          "Çeldiriciler: AT III reseptör antagonizması, ADP reseptör blokajı, fosfodiesteraz aktivasyonu, faktör VIIa inhibisyonu."),
        Q("21-22", None, "Heparin etkisini nasıl gösterir?",
          "Antitrombin III (aktivasyonu)",
          "Heparin AT-III'e sıkıca bağlanıp onu aktif hale getirir."),
    ],
)
