# -*- coding: utf-8 -*-
"""Kaynak: Drive › Komite-1 › PDF › Patoloji › 2026-2027(yeni) › Çetin Boran › 2-Tm_in moloküler temeli-1 (47 slayt) + 3-Tm_in moloküler temeli-2 Çok basamaklı karsinogenez (50 slayt)"""

from yardim import B, C, Q  # noqa: F401

BOLUM = dict(
    key="molekuler", baslik="Kanserin Moleküler Temeli ve Çok Basamaklı Karsinogenez",
    hoca="Prof. Dr. Çetin Boran", tarih="5 ve 7 Ekim", saat="4 saat",
    kaynak="2-Tm'in moloküler temeli-1 + 3-Tm'in moloküler temeli-2 · Prof. Dr. Ç. Boran · 2026",
    ozet=[
        "Son 5 yılda **her yıl 1-3 soru** (≈10): **p53** işlevi · **RAS** · **RB–E2F** · **p16** · **NF1** · **APC (Knudson)** · **MSH2** · **BRCA** · RB tümörleri.",
        "Hep **gen → görev / sınıf eşleştirme**: onkogen (RAS, ERBB2, c-KIT, MYC, siklin D) · süpresör (RB, p53, p16, NF1, APC) · tamir (MSH2, BRCA).",
        "Tuzaklar: **E2F** süpresör gen değil **transkripsiyon faktörü** · antikorla hedeflenenler ERBB2, RAS, c-KIT; **p16** süpresör · protoonkogende **tek allel** yeter.",
    ],
    slaytlar=[
        # ---------------------------------------------------------------- PDF-1 (Kanserin moleküler temeli)
        [
            C("Genetik hasar ve monoklonalite", [
                B("**Öldürücü olmayan genetik hasar** kanserin temelidir; hasar **çevresel etkilerle** oluşabilir, **genetik olarak geçebilir** ya da **tesadüfen (sporadik)** ortaya çıkabilir."),
                B("Tümör, genetik hasarlı **tek bir öncü hücreden** gelişir (**monoklonalite**)."),
                B("Monoklonalite saptama: polimorfik **X-bağımlı moleküller** — **G6PD**, iduronat-2-sülfataz, fosfogliserat kinaz (kadınlarda); **HUMARA** (insan androjen reseptör geni) metilasyon paterni."),
                B("Ayrıca **spesifik translokasyonlar** (KML: **Philadelphia kromozomu, BCR-ABL**) ve **Ig / T-hücre reseptör genlerinin** yeniden düzenlenme paterni kullanılır."),
            ]),
            C("Kanser kök hücreleri (T-IC)", [
                B("**Meme kanseri ve lösemilerde** kanser kök hücresi saptanmıştır (**T-IC = tumor initiating cell**); **kendini yenileme** ve **uzun süreli kalıcılık** kapasitesi vardır."),
                B("Lösemik kök hücreler kendini yenilemeyi sürdürmek için **BMI1** genini eksprese eder; BMI1, **p16INK4a** ve **p14ARF** süpresör genlerini baskılar."),
                B("Meme tümörü kök hücreleri tümör kitlesinin **%2'sini**, myeloid lösemi kök hücreleri **%0.1-1'ini** oluşturur."),
                B("Normal hücreler gibi **düşük proliferasyon hızına** sahiptir → **eliminasyonları daha zor**."),
            ]),
            C("Büyüme ve diferansiyasyonda görev alan 4 temel gen", [
                B("**Protoonkogenler**: mutant allel bakımından **dominant** onkogen — **bir allelin mutasyonu yeter**.", y="22-23"),
                B("**Tümör süpresör genleri**: **resesif** onkogen."),
                B("**Apopitoz genleri**: **dominant veya resesif**."),
                B("**DNA tamir genleri**: genetik instabilite (**mutator fenotip**) için **her iki allel de inaktive** olmalı — resesif."),
            ]),
        ],
        [
            C("Tümör progresyonu", [
                B("Karsinogenez **fenotipik ve genotipik** düzeyde **çok basamaklı** bir süreçtir."),
                B("**Aşırı büyüme, lokal invazyon ve metastaz** kabiliyetleri **ayrı ayrı zamanlarda** kazanılır.", y="22-23"),
            ]),
            C("Malign transformasyon için gerekli 8 temel değişiklik", [
                B("1- **Dış uyarı olmadan büyüme** (onkogen aktivasyonu ile)"),
                B("2- **Büyüme inhibitörlerine duyarsızlık** (TGF-β ve siklin bağımlı kinaz inhibitörleri = CDKI gibi)"),
                B("3- **Apopitoza direnç**: **p53 mutasyonu** ya da antiapopitotik genlerin (**Bcl-2, Bcl-x, Mcl-1**) aktivasyonu"),
                B("4- **DNA tamirinde defekt**"),
                B("5- **Sınırsız bölünme** kabiliyeti (**telomerin** uzunluğunun ve fonksiyonunun korunması ile)"),
                B("6- **Anjiyogenez**"),
                B("7- **İnvazyon ve metastaz** kabiliyeti"),
                B("8- **İmmün yanıttan kurtulma**"),
            ]),
            C("Normal hücre siklusu", [
                B("**G0** = hücrelerin **dinlenme evresi**; çoğalma için hücre **G1 ve ileri evrelere** taşınmalıdır."),
                B("Siklusun düzenli ilerlemesi **siklin**, **siklin bağımlı kinazlar (CDK)** ve **inhibitörleri** ile sağlanır."),
                B("CDK, siklinle bağlanıp **fosforile olarak** aktivite kazanır; görev bitince **siklin ayrılır**, CDK **inaktive** olur."),
                B("En önemli siklinler **D, E, A ve B**; siklus esnasında **sırayla** ortaya çıkarlar."),
            ]),
        ],
        [
            C("Siklin–CDK kompleksleri", [
                B("**Siklin D – CDK4**: **RB süpresör genini fosforiller** → siklusun **kilidini açar** (G1 kısıtlama noktasından geçiş)."),
                B("Diğer kinazlara oranla özellikle **CDK4 amplifikasyonu** sık: **melanom, sarkom, glioblastom**.", lvl=1),
                B("**Siklin E – CDK2**: siklusun **S fazında** daha fazla ilerlemesi için gerekli."),
                B("**Siklin A** (**E2F'in yardımıyla** oluşur) → **CDK2'ye** bağlanır → **G2/M** kontrol noktasının geçilmesi."),
                B("**Siklin B – CDK1**: son aşama; **mitoz tamamlanır**."),
            ]),
            C("RB – E2F", [
                B("Normalde **RB**, **E2F denilen transkripsiyon faktörü** ile sıkı bir bileşik oluşturarak **bölünmeyi önler**.",
                  y="24-25 22-23", tuzak="“E2F, RB geni ile birlikte kompleks halde bulunan süpresör bir gendir” → YANLIŞ (E2F transkripsiyon faktörüdür)"),
            ]),
            C("Hücre siklusu inhibitörleri (CDKI)", [
                B("İki ana grup: **Cip/WAF (CIP/KIP)** ve **INK4/ARF** aileleri."),
                B("**Cip/WAF**: **p21, p27, p57** (CDKN1A-D) — siklin–CDK komplekslerine bağlanıp **siklusu bloke eder**."),
                B("**p21** → **p53 ile indüklenir**; **p27** → **TGF-β** gibi büyüme baskılayıcılara yanıt verir.", lvl=1),
                B("**INK4/ARF**: **p14, p15, p16, p17, p18, p19** (CDKN2A-C) — **siklin/CDK4 ve siklin/CDK6** üzerine selektif etki eder."),
                B("**p16INK4a**: **CDK4'e bağlanarak aktivasyonunu önler**; siklin D–CDK4'e bağlanıp **RB'nin inhibitör etkisini** destekler.", y="23-24", lvl=1),
                B("**p14ARF**: **MDM2'yi inhibe ederek p53 düzeyini arttırır** (p53'ün yıkılmasını önler).", lvl=1),
            ]),
        ],
        [
            C("Hücre siklusu kontrol noktaları (2 ana nokta)", [
                B("**G1/S**: DNA'da hasar varsa siklus **burada durdurulur**; tamirat olur, siklus ilerler; **tamirat yapılamazsa hücre apopitoza** yönlendirilir."),
                B("**G2/M**: sentez fazından sonraki **DNA hasarı tespit ve tamir edilir**; **iyonizan radyasyon hasarlarında** önemlidir."),
                B("DNA hasarını tespit eden **tarayıcı moleküller**: **RAD ailesi, ATM**; bilgi aktarıcı molekül: **CHK kinazlar**."),
            ]),
            C("Onkogen kavramları", [
                B("**Onkogen**: hücre çoğalmasında hücreye **otonomi** kazandıran gen (siklinler vb.)."),
                B("**Protoonkogen**: onkogenin **normal hücredeki karşıtı**; büyüme ve proliferasyonda görev alır, onkogene dönüşürse hücreyi **transformasyona** götürür."),
                B("**Onkoprotein**: onkogenin **protein ürünü**; transforme hücrede **herhangi bir uyarı olmadan sürekli** üretilir."),
                B("**Onkogen ürünleri**: büyüme faktörleri, büyüme faktör reseptörleri, **sinyal taşıyıcılar**, **transkripsiyon faktörleri**, **hücre siklus komponentleri**."),
            ]),
            C("Normalde hücrenin bölünmeye yönlendirilmesi", [
                B("1- **Büyüme faktörünün** membran yüzeyindeki **reseptörüne bağlanması**"),
                B("2- **Reseptör aktivasyonu** ve bunun **membran iç yüzeyindeki sinyal ileticilere** yansıtılması"),
                B("3- Sinyal taşıyan moleküllerin **çekirdeğe ulaşması**"),
                B("4- **DNA transkripsiyonuna aracılık eden** moleküllerin uyarılması ve transkripsiyonu izleyen **bölünme**"),
            ]),
        ],
        [
            C("Onkogenlerin keşfi", [
                B("İlk kez **akut transforme edici retrovirüslerde** saptandı (**v-onc**): **v-fes** (feline sarkom virüsü), **v-sis** (simian sarkom virüsü)."),
                B("Bazı tümör yapıcı virüsler onkogen içermez; **konaktaki protoonkogenin yakınına implante** olup onu onkogene çevirir."),
                B("Virüsün aracılık etmediği **spontan tümörlerde** de onkogen saptanmıştır; **saptanan ilk onkogen RAS mutasyonudur**."),
            ]),
            C("Major sinyal yolları", [
                B("**Reseptör tirozin kinaz**, **G protein-bağlı reseptör**, **JAK/STAT**, **WNT**, **Notch**, **Hedgehog**, **TGFβ/SMAD** ve **NF-κB** yolları."),
                B("Tümörlerde **en sık mutasyona uğrayan** onkogenik sinyal yolu **reseptör tirozin kinaz** yoludur."),
                B("İki ana kaskad: **MAPK** yolu ve **PI3K/AKT** yolu."),
            ]),
            C("Reseptör tipine göre ligandlar", [
                B("**İntrinsik tirozin kinaz aktiviteli reseptöre** bağlananlar: **EGF, TGF-α, VEGF, PDGF**."),
                B("**Yedi transmembran G-protein reseptörüne** bağlananlar: vazopressin, serotonin, histamin, epinefrin, glukagon, paratiroid hormonu, kortikotropin vb."),
            ]),
            C("Kısaltmalar", [
                B("**PI3**: fosfatidil inositol 3 kinaz · **IP3**: inositol trifosfat · **JAK**: Janus kinaz · **STAT**: signal transducers and activators of transcription · **PKB**: protein kinaz B · **MAP**: mitojen aktive protein · **AKT**: serin/treonin protein kinaz"),
            ]),
        ],
        [
            C("Büyüme faktörleri", [
                B("**Glioblastomalarda PDGF** aşırı yapılır; tümör aynı zamanda **PDGF reseptörünü** de içerir."),
                B("Pek çok **sarkom TGF-α** üretir ve reseptörünü içerir."),
                B("**FGF** birçok kanserde artmıştır."),
                B("Büyüme faktörü artışı **tek başına neoplastik transformasyon için yeterli değildir**, ancak **spontan mutasyon riskini arttırır**."),
            ]),
            C("Büyüme faktörü reseptörleri", [
                B("Reseptörlerin **onkojenik versiyonları sürekli aktiftir** ve içeriye **sürekli sinyal** gönderir."),
                B("**RET**: protoonkogen; **tirozin kinaz reseptörünü** kodlar, normalde **nöroendokrin hücrelerden** eksprese edilir."),
                B("**RET mutasyonları** → **MEN 2A, 2B** ve **familyal medüller tiroid karsinom** sendromları; **tam fonksiyon kaybı** → **aganglionik megakolon**.", lvl=1),
                B("**FLT3** (FMS-like tirozin kinaz 3): **miyeloid lösemilerde** sürekli sinyal üretir."),
                B("Birçok **kronik myeloid lösemide PDGF geni**, **translokasyonla ETS ailesinden bir transkripsiyon geniyle** birleşerek aktivite kazanmıştır."),
            ]),
            C("Mutasyonsuz artmış ekspresyon: EGFR (ERB B1)", [
                B("Bazen protoonkogende mutasyon yoktur, **ekspresyon artmıştır**: **EGFR (ERB B1)** — **skuamöz hücreli CA'ların %80'inde**, **glioblastomaların %50'sinde**, **baş-boyun kanserlerinin %80-100'ünde**."),
                B("**ERB B1 nokta mutasyonları** **akciğer adenokarsinomlarında** saptanmış; **EGFR tirozin kinazını aktive eder** (**EGFR inhibitörleri** tedavide kullanılır)."),
            ]),
        ],
        [
            C("ERB B2 (HER2/Neu)", [
                B("**EGFR ailesinin** bir üyesi; **kanserlerin %25'inde** ekspresyonu artmıştır (**meme, over, akciğer-mide ve tükürük bezi adenokarsinomları**)."),
                B("Bu reseptöre karşı geliştirilmiş **monoklonal antikorlar** tedavi seçeneği olarak kullanılır.", y="23-24"),
            ]),
            C("c-KIT", [
                B("**GIST'te c-KIT** (tirozin kinaz reseptörü) hedef alan benzer tedavi: **imatinib mesilat**.", y="23-24"),
            ]),
            C("ALK", [
                B("**Yeniden düzenlenme** tirozin kinaz aktiviteli ALK'yı aktifleştirebilir: bazı **akciğer adenokarsinomlarında EML4-ALK füzyon geni** → sürekli tirozin kinaz aktivitesi (**ALK inhibitörleri** tedavide kullanılır)."),
            ]),
            C("RAS ailesi — sinyal transdüksiyonu yapan proteinler", [
                B("Sinyal transdüksiyonu yapan proteinlerin **en iyi bilinen örneği RAS ailesi** (**GTP-bağlayıcı protein**): **HRAS, KRAS, NRAS**; **MAPK kaskadı** ve **PI3K/AKT** yolunu kullanır.", y="24-25"),
                B("İnsandaki **tüm tümörlerin %15-20'sinde RAS'ta nokta mutasyonu** vardır."),
                B("**Mutant RAS**, GTPaz-aktive edici proteine bağlanır ama **GTPaz'a dirençlidir** → **devamlı aktif** kalır."),
                B("**NF-1 = nörofibromin**: bir **GTPaz aktive edici proteindir**.", y="23-24", lvl=1),
                B("**Mutant RAS'ı bloke edici antikorlar** geliştirilmeye çalışılıyor.", y="23-24"),
            ]),
        ],
        [
            C("RAS ile ilişkili diğer genler", [
                B("**Onkogenik BRAF ve PI3K mutasyonları** da **sürekli sinyal üretimi** ile sonuçlanabilir; bazı ileri evre **malign melanomlarda BRAF inhibitörleri** faydalıdır."),
                B("**PI3K'ün antagonisti PTEN** (süpresör gen) mutasyonla etkisizleşirse **aynı sonuç** ortaya çıkar."),
            ]),
            C("Nonreseptör tirozin kinaz: c-abl", [
                B("Sinyal transdüksiyon yolunda görev alır ve **hücre çoğalmasını kontrol eder**; **en önemli örnek c-abl**."),
                B("**KML ve bazı ALL'de** c-abl normal yerinden **22. kromozoma taşınır [t(9;22)]** ve **BCR** geniyle **füzyon** yapar."),
                B("Füzyon ürünü (**Philadelphia kromozomu**) **sürekli tirozin kinaz aktivitesi** sağlar; **imatinib mesilat BCR-ABL** tirozin kinaz molekülünü hedef alır."),
            ]),
            C("JAK2", [
                B("**JAK2** mutasyonu: **JAK/STAT** yoluna katılır; **sitokin reseptörlerinden** aldığı sinyali çekirdeğe iletir."),
                B("**STAT** ailesi transkripsiyon faktörlerini aktive eder: **polisitemia vera**, **primer miyelofibrozis** gibi **miyeloproliferatif hastalıklar**."),
            ]),
            C("Transkripsiyon faktörleri", [
                B("**myc, myb, jun, fos, Rel** onkoproteinleri transforme hücrenin **çekirdeğinde** bulunur; **siklinlerin ekspresyonunu** düzenler."),
                B("**myc en çok etkilenen gendir**: **Burkitt lenfomada t(8;14)** ile **Ig geni–myc füzyonu** → myc fazla eksprese edilir."),
            ]),
        ],
        [
            C("Siklin ve CDK'ler", [
                B("**CDK4** ve **D siklinlerinin** regülasyonunun bozulması **proliferasyon lehine** bir durum yaratır."),
                B("**CDKI mutasyonları** da regülasyonu bozar: **CIP/KIP ailesi** (p21, p27; CDKN1A-D), **INK4/ARF ailesi** (p16, p14; CDKN2A-C)."),
            ]),
            C("Tablo 7-6 — Büyüme faktörleri (onkogen → ilişkili tümör)", [
                B("**PDGF-β zinciri (PDGFB)** → **astrositom**"),
                B("**FGF**: **HST1** → **osteosarkom** · **FGF3** → **mesane ve mide kanserleri**, meme kanseri, melanom"),
                B("**HGF** → **tiroid kanseri**, hepatosellüler karsinom"),
                B("**TGF-α (TGFA)** → **astrositom**"),
            ]),
            C("Tablo 7-6 — Büyüme faktörü reseptörleri", [
                B("**EGF-reseptör ailesi: ERBB1 (EGFR), ERBB2 (HER2)** → **akciğer adenokarsinomu, meme karsinomu**"),
                B("**FLT3** → **lösemi**"),
                B("**RET** (nörotrofik faktör reseptörü) → **MEN 2A ve 2B, ailesel medüller tiroid karsinomu**"),
                B("**ALK** → **akciğer adenokarsinomu, bazı lenfomalar**"),
                B("**PDGFRB** → **gliomlar, lösemiler**"),
                B("**KIT** (stem cell/steel faktör reseptörü) → **GIST, seminom, lösemiler**"),
            ]),
        ],
        [
            C("Tablo 7-6 — Sinyal transdüksiyonunda görevli proteinler", [
                B("**GTP-bağlayıcı**: **KRAS** → kolon, akciğer, pankreas tümörleri · **HRAS** → mesane, böbrek tümörleri · **NRAS** → melanom, hematolojik maligniteler"),
                B("**GNAQ** → **uveal melanom** · **GNAS** → **hipofiz adenomu**, diğer endokrin tümörler"),
                B("**Nonreseptör tirozin kinaz: ABL** → **KML, ALK'sız değil ALL** "),
                B("**RAS sinyal iletimi: BRAF** → melanom, lösemiler, kolon karsinomu, diğerleri"),
                B("**WNT sinyal iletimi: β-catenin** → **hepatoblastom, hepatosellüler karsinom**"),
                B("**Notch: NOTCH1** → lösemiler, lenfomalar, meme karsinomu"),
                B("**JAK/STAT: JAK2** → **miyeloproliferatif hastalıklar, ALL**"),
            ]),
            C("Tablo 7-6 — Nükleer düzenleyiciler ve hücre siklusu düzenleyicileri", [
                B("**Transkripsiyon aktivatörleri**: **C-MYC** → **Burkitt lenfoma** · **N-MYC** → **nöroblastom**"),
                B("**Siklin D** → **mantle hücreli lenfoma, multipl miyelom**; meme ve özofagus kanserleri"),
                B("**Siklin E** → **meme kanseri**"),
                B("**CDK4** → **glioblastom, melanom, sarkom**"),
            ]),
        ],
        # ---------------------------------------------------------------- PDF-2 (Tümör süpresör genler ... çok basamaklı karsinogenez)
        [
            C("Süpresör gen tablosu — mitojenik sinyal yolu inhibitörleri (1)", [
                B("**APC** (adenomatöz polipozis koli): **WNT** inhibitörü · **ailesel**: kolon polipleri ve karsinomu · **sporadik**: mide, kolon, pankreas karsinomu; melanom"),
                B("**NF1** (nörofibromin-1): **RAS/MAPK** inhibitörü · **ailesel**: **NF tip 1** (nörofibrom, malign periferik sinir kılıfı tümörü) · **sporadik**: nöroblastom, juvenil myeloid lösemi", y="23-24"),
                B("**NF2** (merlin): sitoskelet stabilitesi, **Hippo** yolu · **ailesel**: **NF tip 2** (akustik schwannom, meningiom) · **sporadik**: schwannom, meningiom"),
            ]),
            C("Mitojenik sinyal yolu inhibitörleri (2)", [
                B("**PTCH** (patched): **Hedgehog** inhibitörü · **ailesel**: **Gorlin sendromu** (bazal hücreli ca, medulloblastom, çeşitli benign tümörler) · **sporadik**: bazal hücreli ca, medulloblastom"),
                B("**PTEN**: **PI3K/AKT** inhibitörü · **ailesel**: **Cowden sendromu** (benign deri/GİS/SSS büyümeleri; meme, endometrium, tiroid ca) · **sporadik**: çeşitli kanserler (özellikle karsinom, lenfoid tümör)"),
                B("**SMAD2, SMAD4**: **TGF-β** yolu komponenti; **MYC ve CDK4** ekspresyonunu baskılar, CDK inhibitörlerini indükler · **ailesel**: **juvenil polipozis** · **sporadik**: kolon ve pankreas karsinomu"),
            ]),
            C("Hücre siklusu ilerleyişinin inhibitörleri", [
                B("**RB** (retinoblastom proteini): **G1/S geçişi** inhibitörü · **ailesel**: **retinoblastom sendromu** (retinoblastom, osteosarkom, diğer sarkomlar) · **sporadik**: retinoblastom; osteosarkom; meme, kolon, akciğer ca", y="21-22"),
                B("**CDKN2A** (p16/INK4a ve p14/ARF): **p16** CDK'lerin negatif regülatörü; **p14** p53'ün dolaylı aktivatörü · **ailesel**: **melanom** · **sporadik**: pankreas, meme, özofagus ca, melanom, bazı lösemiler", y="23-24"),
            ]),
        ],
        [
            C("“Pro-growth” metabolizma ve anjiyogenez programı inhibitörleri", [
                B("**VHL**: **hipoksi ile indüklenen transkripsiyon faktörlerinin (HIF1α)** inhibitörü · **ailesel**: VHL sendromu (serebellar hemanjioblastom, retinal anjiom, renal hücreli ca) · **sporadik**: renal hücreli ca"),
                B("**STK11 (LKB1)**: **AMPK kinaz ailesi aktivatörü**; besin/enerji düşükken hücre büyümesini baskılar · **ailesel**: **Peutz-Jeghers** (GİS polipleri, GİS ve pankreas ca) · **sporadik**: çeşitli karsinomlar (%5-20)"),
                B("**SDHB, SDHD** (süksinat dehidrogenaz alt birimleri): TCA döngüsü, oksidatif fosforilasyon · **ailesel**: paraganglioma, feokromositoma · **sporadik**: paraganglioma"),
            ]),
            C("İnvazyon ve metastaz inhibitörleri", [
                B("**CDH1** (E-cadherin): **hücre adezyonu**, hücre hareketinin inhibisyonu · **ailesel**: mide kanseri · **sporadik**: mide karsinomu, lobüler meme karsinomu"),
            ]),
            C("Genomik stabilite sağlayıcılar", [
                B("**TP53** (p53): **DNA hasarına yanıt olarak siklus arresti ve apopitoz** · **ailesel**: **Li-Fraumeni sendromu** (çeşitli kanserler) · **sporadik**: **insan kanserlerinin çoğu**", y="25-26"),
            ]),
            C("DNA tamir faktörleri", [
                B("**BRCA1, BRCA2**: DNA **çift zincir kırıklarının tamiri** · **ailesel**: meme ve over ca; erkek meme ca; KLL (BRCA2) · **sporadik**: nadir", y="21-22"),
                B("**MSH2, MLH1, MSH6**: DNA **mismatch tamiri** · **ailesel**: **herediter nonpolipozis kolon karsinomu** · **sporadik**: kolon ve endometrium karsinomu", y="22-23"),
            ]),
            C("Mekanizması bilinmeyenler", [
                B("**WT1** (Wilms tümörü-1): transkripsiyon faktörü · **ailesel**: Wilms tümörü · **sporadik**: Wilms tümörü, bazı lösemiler"),
                B("**MEN1** (menin): transkripsiyon faktörü · **ailesel**: **MEN-1** (hipofiz, paratiroid, pankreas endokrin tümörleri) · **sporadik**: aynı tümörler"),
            ]),
        ],
        [
            C("RB geni — retinoblastom", [
                B("Retinoblastom için **RB geninde mutasyon** gerekir; **sporadik** tümörde genin **her iki alleli de** mutasyona uğrar (retinoblastomların **%60'ı sporadik**); RB geni **13q14**'te."),
                B("**Herediter** olguda mutant bir allel **doğuştan** gelir; sonradan retinada, bu alleli taşıyan binlerce hücreden birinde **2. mutasyon (LOH = loss of heterozygosity)** oluşur → **retinoblastom**, daha az olarak **osteosarkom** (**Knudson'un 2 vuruş hipotezi**).", y="22-23 21-22"),
                B("RB mutasyonu diğer birçok tümörün gelişimini de kolaylaştırır: **glioblastom, small cell karsinom, meme ve mesane kanserleri**."),
            ]),
            C("RB'nin işlevi", [
                B("**Tümör baskılayıcı “pocket” protein**: **hipofosforile halde E2F transkripsiyon faktörlerine bağlanarak G1/S geçişini engeller**; diferansiyasyonu düzenleyen çeşitli transkripsiyon faktörleriyle de etkileşir.", y="24-25"),
            ]),
            C("RB'nin etkisinin bozulma nedenleri", [
                B("**RB'nin mutasyonla** etkisizleşmesi"),
                B("**CDK4 ve siklin D** genlerinin **amplifikasyonu**"),
                B("**CDK inhibitörlerinin** kaybı veya mutasyonu (**p16/INK4a**)"),
                B("Çeşitli **viral proteinlerin** RB etkisini nötralize etmesi (**HPV E7**)"),
            ]),
        ],
        [
            C("p53 — genomun bekçisi", [
                B("**p53 genomun bekçisidir**; gen adı **TP53**, protein ürünü **p53**; **17p13.1**'de yerleşir. Etkisini esas olarak **p21** üzerinden gösterir."),
                B("**Kanserlerin çoğunda değişmiştir**: tümörlerin **%50'sinde** p53 mutasyonu vardır."),
                B("**Hücre siklusu arrestine ve apopitoza** yol açar; **G1/S kontrol noktası için gereklidir**, **G2/M kontrol noktasının ana bileşenidir**.", y="25-26"),
                B("Apopitozu **BAX** gibi proapopitotik genlerin transkripsiyonunu indükleyerek sağlar; p53 düzeyleri **MDM2** ile **negatif geri bildirimle** düzenlenir."),
            ]),
            C("Li-Fraumeni sendromu", [
                B("Bazen **tek mutant allel kalıtsal** geçer, **ikinci allel spontan mutasyona** uğrar → tümör gelişir: **Li-Fraumeni sendromu**."),
                B("Risk **50'li yaşlarda 25 kat** artmıştır: **sarkomlar, meme kanseri, lösemi, beyin ve adrenal korteks tümörleri**."),
            ]),
            C("p53 işleyişi: durdur → tamir et → apopitoz", [
                B("Hasarsız hücrede p53'ün **ömrü kısadır (20 dakika)**; hasar uyarısında **yapımı artar, yıkımı azalır**."),
                B("**Siklusu durdurur (p21 üzerinden)**, hücre **tamir genlerince tamir edilir**; **tamir edilemezse apopitoza yönlendirilir** (**Bax ve PUMA = BBC3** uyarılarak).", y="25-26"),
                B("p53, miRNA ailesinden **miR-34**'ü de aktive eder: hücre büyümesi durur, apopitoz olur; miR-34 **p53'ten bağımsız** aktive edilse de büyüme durup apopitoz gerçekleşebilir."),
            ]),
        ],
        [
            C("p53 ve DNA hasarı yanıtı", [
                B("DNA tamirinde **ATM** (ataxia-telangiectasia mutated) ve **ATR** önemlidir; hasarda **p53'ün** ve **DNA tamir genlerinin** transkripsiyonunu arttırırlar."),
                B("p53 **GADD45** (growth arrest and DNA damage) genini arttırır; bu gen DNA tamirine yardım eder."),
                B("Tamir gerçekleşirse p53 **MDM2'yi arttırarak kendi yıkımını** sağlar → siklus başlar; **hasar tamir olmazsa apopitoz**."),
            ]),
            C("p53 ailesi: p63 ve p73", [
                B("**p63**: **tabakalı yassı epitelin diferansiyasyonu** için gerekli."),
                B("**p73**: kemoterapötik ajanların oluşturduğu DNA hasarından sonra **güçlü proapopitotik** etki."),
                B("Tümörde **p53 ve özellikle p73 mutantsa**, kemoterapiyle oluşan DNA hasarına bağlı **apopitoz aksar**."),
            ]),
            C("p53'ü mutasyon dışında inaktive eden faktörler", [
                B("**HPV'nin E6 molekülü**"),
                B("Bazı tümörlerde **MDM2'nin aşırı yapılması** (**MDM2 ve MDMX p53'ü yıkar**)"),
            ]),
        ],
        [
            C("APC / β-catenin (WNT yolu)", [
                B("**WNT** sinyal yolunun bir komponentidir; yol embriyogenezde **hücre akıbeti, adezyon, hücre polaritesi**, ayrıca **hematopoietik kök hücre yenilenmesi** için gereklidir."),
                B("**APC'nin görevi β-catenin'i inaktif tutmaktır** (APC, β-katenin, **aksin ve GSK3β** ile kompleks halinde)."),
                B("β-catenin serbest kalırsa **çekirdeğe gidip TCF** (transkripsiyon faktörü) ile kompleks yapar → **c-MYC ve siklin D1** gibi genlerin üretimi artar."),
                B("β-catenin ayrıca **E-cadherin**'e bağlanarak **hücreler arası kohezyonu** sağlar; **β-catenin–E-cadherin aksının aksaması metastazı kolaylaştırır**."),
            ]),
            C("APC — herediter durum", [
                B("**Adenomatöz polipozis**'te APC geninin **bir alleli mutant** olarak çocuğa geçer; **diğer allelde de mutasyon** olursa **adenomlar** gelişir.", y="22-23"),
                B("**Kanser** gelişmesi için **ilave mutasyonlar** da gereklidir."),
                B("β-katenin **hepatoblastomaların %50'sinde**, **hepatosellüler karsinomların %20'sinde** mutantır."),
            ]),
            C("E-cadherin (CDH1)", [
                B("**Adeziv glikoprotein**; mutasyonu **invazyon ve metastazı** kolaylaştırır. **Ailesel mide kanserinde** E-cadherin (**CDH1**) mutasyonu vardır."),
                B("Transkripsiyon repressörü **SNAIL**, E-cadherin miktarını azaltarak invazyon ve metastazı kolaylaştırabilir."),
            ]),
        ],
        [
            C("CDKN2A", [
                B("CDKN2A lokusu iki protein kodlar: **1) p16/INK4a** — CDK inhibitörü (**RB kontrol noktasını güçlendirir**); **2) p14/ARF** — **p53 destrüksiyonunu önler**.", y="23-24"),
                B("**Birçok tümörde p16INK4a'nın işlevi kaybolmuştur**: p16, RB'nin fosforillenip siklusun açılmasını önler; p14ARF **MDM2'yi inhibe** ederek p53 yıkımını engeller.", y="23-24"),
            ]),
            C("TGF-β yolu", [
                B("Normal **epitelyal, endotelyal ve hematopoietik** hücrelerde potansiyel **antiproliferatiftir**."),
                B("**HNPCC** sendromlu tümörlerin **%70'inde** bu yol inaktiftir."),
                B("Önemli komponentler: **SMAD2** (bazı kolorektal kanserlerde mutant) ve **SMAD4** (**pankreas karsinomlarında** mutant)."),
            ]),
            C("NF-1 (nörofibromin)", [
                B("Genin **bir alleli mutant** geçer; **ikinci allelde de mutasyon** olursa **nörofibromatozis tip-1**: nörofibromlar + **optik glioma** + iriste pigmente nodül (**Lisch nodülleri**) + kutanöz hiperpigmente maküller (**café au lait**)."),
                B("**Nörofibromin GTPaz'ı aktive eden bir proteindir**, dolayısıyla **RAS'ı inaktive eder**.", y="23-24"),
            ]),
            C("NF-2 (merlin)", [
                B("Protein ürünü **nörofibromin 2 = merlin**; yokluğunda **hücreler arası bağlar oluşturulamaz** ve **büyüme inhibitörlerine duyarsızlık** olur."),
                B("Mutasyonunda **nörofibromatozis tip-2**: **bilateral akustik schwannoma + multipl meningioma + ependimoma**."),
            ]),
        ],
        [
            C("VHL (von Hippel-Lindau)", [
                B("Von Hippel-Lindau hastalığında tanımlanan gen: **serebellum ve retinada hemanjioblastom + clear cell renal Ca + feokromositom**."),
                B("Mutasyonunda **HIF-1α yıkımı gerçekleşemez**, **anjiyojenik faktörler sürekli salınır**; **sporadik clear cell renal Ca**'da da VHL mutasyonu vardır."),
            ]),
            C("PTEN", [
                B("**Endometrium Ca ve glioblastomalarda** sıklıkla bu gen kaybolmuştur; PTEN **PI3K/AKT (protein kinaz B)** sinyal yolunu **bloke eder**."),
                B("**Cowden sendromunda** PTEN mutasyonu vardır: **deri eki tümörleri** + epitelyal kanser insidansında artış (özellikle **meme, endometrium, tiroid**)."),
            ]),
            C("WT-1", [
                B("**Böbrek-gonad gelişiminde** rol alır; mutasyonu **Wilms tümörü**ne yol açar (lösemi ve meme kanserlerinde de mutasyon saptanabilir)."),
            ]),
            C("PTCH (Patched)", [
                B("**Hedgehog/Patched** yolunda görev alır; mutasyonunda **N-MYC ve D siklinler artar**; mutasyonu **nevoid bazal hücreli karsinom (Gorlin) sendromu** yapar."),
            ]),
            C("STK11 (LKB1)", [
                B("**Serin/treonin kinazı** kodlar; **hücre metabolizması düzenlenmesinde** rol alır; mutasyonunda **Peutz-Jeghers sendromu** gelişir, **GİS ve pankreas kanserlerine** yatkınlık oluşur."),
            ]),
        ],
        [
            C("Apopitozdan kurtulma", [
                B("Neoplastik hücre çoğalması **onkogen aktivasyonu** ve **süpresör gen inaktivasyonu** ile sağlanır; **apopitozdaki aksama** neoplastik kitlenin artmasına yardım eder."),
                B("**Bcl-2 antiapopitotik** bir gendir; **foliküler lenfomalarda t(14;18)** ile **Ig geninin yanına taşınır** → Bcl-2 fazla üretilir → **apopitozdan kaçış**."),
            ]),
            C("Apopitoz yolları", [
                B("**Ekstrinsik** (**CD95/Fas** reseptörü aracılıklı) ve **intrinsik** (**DNA hasarı** ile uyarılma) olmak üzere iki yol vardır."),
                B("**İntrinsik yol**: p53 proapopitotik **BAX ve BAK**'ı uyarır → **sitokrom c mitokondriden sitoplazmaya** geçer → apopitoz başlar."),
            ]),
            C("Dengeyi ve kaspazları etkileyen moleküller", [
                B("**BH3-only proteinler** (**BAD, BID, PUMA**): proapopitotik (**BAX, BAK**) ve antiapopitotik (**BCL2, BCL-XL, MCL1**) moleküller arasında **dengeyi** sağlar; hasarda **antiapopitotikleri nötralize eder**."),
                B("**FLIP**: CD95/Fas yolunda **kaspaz 8'in aktive olmasını önleyerek** apopitozu engeller (bazı tümörler üretebilir)."),
                B("**APAF-1** (apopitotik peptidaz aktive edici faktör-1): **sitozolde**; **IAP** (inhibitors of apoptosis): sağlıklı hücrede **kaspazları kontrol altında tutar**."),
            ]),
        ],
        [
            C("DNA tamir defekti ve genetik instabilite", [
                B("Bölünme sırasında **rastlantısal** olarak veya **çevresel ajanlarla** sürekli mutasyon olur; hatalar **tamir genleri** ile onarılır."),
                B("Tamir genleri **doğuştan mutantsa** → **genetik instabilite sendromları**; **sporadik tümörlerde** de tamir gen mutasyonu ve genetik instabilite saptanmıştır."),
            ]),
            C("3 tip DNA tamiri", [
                B("**Hatalı eşleşme (mismatch) tamiri** — genleri: **MSH2, MLH1, PMS, PMS2**", y="22-23"),
                B("**Nükleotid eksizyon** tamiri"),
                B("**Rekombinasyon** ile tamir"),
            ]),
            C("HNPCC (herediter nonpolipozis kolon kanseri sendromu)", [
                B("**Hatalı eşleşme tamir genlerinde defekt**; tümörler **proksimal kolonda** gelişir; **endometrium ve over** kanserleri de sıktır."),
                B("Genetik instabilite ile mutasyona uğrayan diğer başlıca genler: **TGF-β reseptör II**, β-catenin yolunun **TCF** komponenti, **BAX**."),
            ]),
            C("Mikrosatellit instabilitesi", [
                B("Hatalı eşleşme gen mutasyonlarının en önemli sonuçlarından biri **mikrosatellit instabilitesi**dir."),
                B("**Mikrosatellit**: DNA'da **1-6 nükleotidlik ardışık diziler**; bireyde **sabittir**, **tüm organlarda aynıdır**."),
                B("Mismatch tamir geni defektinde bu tekrar dizilerinde **kısalmalar** olur = **mikrosatellit instabilitesi**; saptanması **mismatch tamir gen defektinin göstergesidir**."),
                B("Başlıca mismatch tamir genleri: **MSH2, MLH1, PMS, PMS2**.", y="22-23"),
            ]),
        ],
        [
            C("Xeroderma pigmentosum", [
                B("**UV ışınları pirimidin artıklarında çapraz bağlar** oluşturarak replikasyonu önler; bu hasar **NER (nükleotid eksizyon tamiri)** ile onarılır."),
                B("**NER fonksiyonunun aksaması cilt kanserlerinin** gelişimine yol açar."),
            ]),
            C("Homolog rekombinasyon yolu ile DNA tamiri", [
                B("**BRCA1 ve BRCA2**'nin homolog rekombinasyon tamir yolu ile ilişkisi gösterilmiştir; **BRCA mutasyonlarında familyal meme kanserleri** gelişir.", y="21-22"),
                B("Bu tamir genlerinin mutasyonu bir dizi **genetik geçişli hastalığa** yol açar:"),
                B("**Ataksi-telenjiektazi**: **iyonize radyasyona hassasiyet**", lvl=1),
                B("**Bloom sendromu**: iyonize radyasyona hassasiyet, **cücelik + fotosensitivite + immün yetmezlik + hipogonadizm**; defektif **helikaz** geni → rekombinasyon tamiri aksar; pek çok tümör gelişebilir", lvl=1),
                B("**Fanconi anemisi**: **çapraz bağ yapan kemoterapötiklere hassasiyet** (hipoplazik dalak-böbrek-radius-başparmak); homolog rekombinasyon tamiri ile ilişkili", lvl=1),
            ]),
            C("ATM ve lenfoid genler", [
                B("**Ataksi-telenjiektazi**de **ATM** geninde defekt vardır; ATM normalde **DNA çift bağ kırıklarında p53'ü uyararak siklusu durdurur** (özellikle **iyonize radyasyon hasarı**)."),
                B("**RAG1, RAG2, AID** (antigen-induced cytosine deaminase) mutasyonları **genomik instabiliteye** yol açarak **lenfoid dokuda neoplazilere** zemin hazırlar."),
            ]),
        ],
        [
            C("Tümör hücrelerinin sınırsız replikasyon potansiyeli", [
                B("Normal somatik hücre belli bir bölünme sayısından (**60-70 kez**) sonra **yaşlanarak** bölünmeyi durdurur."),
                B("**Telomer** her bölünmeden sonra bir miktar **kısalır**; kritik noktada **p53 aktive olarak siklusu durdurur**."),
                B("**Germinal hücrelerde telomeraz** bu kısalmayı önleyerek **sınırsız replikasyon** kabiliyeti kazandırır."),
                B("**Pek çok tümörde de telomeraz aktivitesi geri kazanılmıştır**."),
            ]),
            C("Tümör hücresinde metabolik değişiklikler", [
                B("Bol oksijen ortamında bile tümör hücresi **glukoz metabolizmasından (aerobik glikoliz)** enerji sağlama eğilimindedir = **Warburg etkisi**."),
                B("**Glikoliz: molekül başına 2 ATP**; mitokondride **oksidatif fosforilasyon: 20 ATP**."),
                B("Aerobik glikoliz hızlı çoğalan hücreye **selüler komponent sentezi için ara metabolitler** sağlar; oksidatif fosforilasyonda bu özellik yoktur."),
                B("**PET**: hastaya **18F-florodeoksiglukoz** (metabolize edilemeyen glukoz türevi) enjekte edilir; **tümör hücreleri ve aktif çoğalan dokular (kemik iliği) PET pozitiftir**."),
            ]),
        ],
        [
            C("Tümörle ilişkili genlerin disregülasyonu", [
                B("Genetik hasar **nokta mutasyonu**, **kromozom segmenti** düzeyinde veya **karyotipte saptanabilecek kadar büyük** olabilir; **tespiti tanıda kullanılabilir**."),
            ]),
            C("1- Translokasyonlar", [
                B("Protoonkogeni **iki yolla** aktive eder:"),
                B("normal yerinden alınıp **komşu düzenleyici elemanlardan uzaklaşması**", lvl=1),
                B("**iki farklı genin füzyonu** → ortaya çıkan **hibrid ürün** onkojenik olabilir", lvl=1),
            ]),
            C("Translokasyon tablosu", [
                B("**KML**: t(9;22)(q34;q11) — **ABL** 9q34 + **BCR** 22q11"),
                B("**Akut lösemiler (AML, ALL)**: t(4;11)(q21;q23) — **AF4** + **MLL**; t(6;11)(q27;q23) — **AF6** + **MLL**"),
                B("**Burkitt lenfoma**: t(8;14)(q24;q32) — **c-myc** 8q24 + **IgH** 14q32"),
                B("**Mantle hücreli lenfoma**: t(11;14)(q13;q32) — **siklin D** 11q13 + **IgH** 14q32"),
                B("**Foliküler lenfoma**: t(14;18)(q32;q21) — **IgH** 14q32 + **bcl-2** 18q21"),
                B("**T-hücreli ALL**: t(8;14)(q24;q11) — **c-myc** + **TCR-α**; t(10;14)(q24;q11) — **Hox11** + **TCR-α**"),
                B("**Ewing sarkom**: t(11;22)(q24;q12) — **Fli-1** 11q24 + **EWS** 22q12 → **füzyon gen**"),
            ]),
        ],
        [
            C("2- Delesyonlar", [
                B("**RB** geninin silinmesi → **retinoblastom**; **VHL** geninin delesyonu → **renal hücreli karsinom**."),
                B("**T-hücreli ALL**'de **TAL1** protoonkogeninin yanındaki, onu kontrol eden genin kaybı bu genin **aktifleşmesini** sağlayabilir."),
            ]),
            C("3- Gen amplifikasyonları", [
                B("Genin DNA dizisi **reduplikasyon ve amplifikasyonla** çoğalır; protoonkogenin **yüzlerce kopyası** yapılır."),
                B("Amplifiye gen kromozomda **mikroskopta görülebilen** değişiklik yapar: **homojen boyanan alanlar (HSR)** veya **multipl kromozom benzeri yapılar (dms = double minutes)**."),
                B("Örnekler: **meme karsinomunda ERBB2 (Her2) reseptörü** aşırı artabilir; **nöroblastomda N-myc amplifikasyonu** görülebilir."),
            ]),
            C("4- Chromothripsis (kromotripsi)", [
                B("Genomda **subsitogenetik düzeyde çok sayıda küçük delesyon ve insersiyon** olur → **yeniden düzenlenme**."),
                B("**Tüm kanser hücresi genomunun DNA dizi analizi** ile ortaya çıkarılır."),
                B("Kromotriptik kırılmalar ve rastgele birleşme–tamir sonucu **birçok süpresör genin işlevi bozulur** veya **onkogenler aktivite kazanabilir**."),
            ]),
        ],
        [
            C("Epigenetik değişiklikler", [
                B("Bazı süpresör genler **DNA bazlarında değişiklik olmadan hipermetilasyon** ile inaktive olabilir."),
                B("Metilasyon **genomik imprinting**'e de katılır: genin **maternal veya paternal alleli** metilasyonla değiştirilir/inaktive edilir (**Prader-Willi** ve **Angelman**)."),
                B("**Prader-Willi**: 15. kromozomdaki genin **paternal alleli işlevsiz**; mental retardasyon, hipotoni, kısa vücut, küçük el-ayak, hipogonadizm.", lvl=1),
                B("**Angelman**: **maternal alleller işlevsiz**; MR, ataksi, felçler, uygunsuz gülmeler.", lvl=1),
                B("Tümörlerde imprinted gen **ters yönde demetilasyona** da uğrayabilir (**biallelik ekspresyon**)."),
                B("**Histonlardaki değişiklikler**: genlerin yakınındaki histonlardaki değişiklikler hücre davranışını değiştirebilir."),
            ]),
            C("Kanserde mutasyona uğrayan epigenomik düzenleyici genler", [
                B("**DNMT3A** (DNA metilasyonu) → **AML (%20)**"),
                B("**MLL1** (histon metilasyonu) → **infantlarda akut lösemi (%90)**"),
                B("**MLL2** (histon metilasyonu) → **foliküler lenfoma (%90)**"),
                B("**CREBBP/EP300** (histon asetilasyonu) → **diffüz büyük B hücreli lenfoma (%40)**"),
                B("**ARID1A** (nükleozom pozisyonlama/kromatin yeniden şekillenmesi) → **over berrak hücreli karsinom (%60)**, endometrium karsinomu (%30-40)"),
                B("**SNF5** (aynı işlev) → **malign rabdoid tümör (%100)**"),
                B("**PBRM1** (aynı işlev) → **renal karsinom (%30)**"),
            ]),
        ],
        [
            C("Kodlanmayan RNA'lar ve kanser", [
                B("**microRNA'lar (miR)**: küçük, **kodsuz, tek zincirli** RNA'lar; **22 nükleotid** uzunluğunda."),
                B("Normal **hücre büyümesi, diferansiyasyonu ve yaşaması** ile ilgili görevleri vardır → bozukluklarında **karsinogenezde** de rol alırlar."),
                B("**miR-200** metastazı kolaylaştırır; **miR-155** B lenfomalarda **myc'yi arttırarak** proliferasyon sağlar."),
            ]),
            C("Çok basamaklı karsinogenez: tek onkogen yetmez", [
                B("**Tek bir onkogen çoğunlukla** hücreyi transformasyona götürmeye **yetmez**."),
                B("**Mutant RAS**: hücreyi **büyüme faktörüne gerek bırakmadan** çoğaltır; **Myc**: büyüme faktörlerine duyarlılığı arttırır ve hücreyi **ölümsüz** kılar."),
                B("**İkisinin birlikte etkisi** deney ortamında **transforme immortal fibroblast** oluşturur."),
            ]),
        ],
        [
            C("Çok basamaklı karsinogenezin moleküler temeli", [
                B("Çoğu tümörde **multipl onkogen aktivasyonu** ve **süpresör gen inaktivasyonu** vardır; bu değişiklikler **değişik aşamalarda** kazanılmıştır."),
                B("Kanser için gereken gen sayısına örnek: **(1) RAS aktivasyonu; (2) RB inaktivasyonu; (3) p53 inaktivasyonu; (4) PP2A inaktivasyonu** (birçok sinyal yolunun negatif regülatörü, tümör baskılayıcı fosfataz); **(5) telomeraz aktivasyonu**."),
                B("Tüm bu mutasyonları geçirmiş bir hücreden **kesin malign tümör** gelişir."),
            ]),
            C("Kolorektal karsinom gelişiminde moleküler model", [
                B("**Normal kolon → risk altındaki mukoza → adenomlar → karsinom**."),
                B("**1. vuruş** (germ-line/kalıtsal veya somatik/kazanılmış süpresör gen mutasyonu): **APC (5q21)**."),
                B("**2. vuruş** (metilasyon anormallikleri, normal allellerin inaktivasyonu): **APC, β-catenin**."),
                B("**Proto-onkogen mutasyonu**: **K-RAS (12p12)** (adenom evresi)."),
                B("**Karsinom**: ek süpresör genlerin **homozigot kaybı** — **TP53 (17p13)**, **LOH 18q21 (SMAD2 ve 4)**; ek mutasyonlar, kaba kromozomal değişiklikler, **telomeraz** ve pek çok diğer gen."),
                B("**Wild-type TP53** varlığında adenom **onkogenin tetiklediği senesens**e gider (şema)."),
            ]),
        ],
    ],
    sorular=[
        Q("25-26", 79, "“Gerektiğinde hücre siklusunu durdurur, gerekirse hücreyi apoptoza yönlendirir.” Tarif edilen gen?", "p53",
          "Siklusu p21 üzerinden durdurur; tamir olmazsa Bax/PUMA ile apopitoz · bcl-2, ras, raf, msh2 değil"),
        Q("24-25", 83, "“Hücre zarı iç yüzeyine yerleşmiştir; reseptörden aldığı büyüme sinyalini çekirdeğe taşır.” Tarif edilen gen?", "RAS",
          "Sinyal transdüksiyonu yapan GTP-bağlayıcı protein · NF-1, PTEN, p53, p16 değil"),
        Q("24-25", 84, "“İnaktive olduğunda E2F serbest kalır ve hücre siklusu ilerler.” Bu gen?", "RB",
          "RB, E2F'i bağlı tutarak G1/S geçişini engeller · Myc, BRCA1, MSH2, VHL değil"),
        Q("23-24", 76, "Bloke edici monoklonal antikorla tedavi seçeneği düşünülemeyecek gen?", "p16",
          "p16 süpresör (CDK inhibitörü) · hedeflenebilir: ERBB2 (mAb), RAS (bloke edici antikor), c-KIT (imatinib); TGF-α için PDF'te tedavi yok"),
        Q("23-24", 77, "Hücre sinyal iletim yollarında inhibitör olarak yer alan gen?", "NF1",
          "NF1 (nörofibromin) GTPaz'ı aktive ederek RAS'ı inaktive eder · p21 CDKI, myc TF onkogen, msh2 tamir, ATM hasar tarayıcı değil"),
        Q("22-23", 75, "Knudson'un çift vuruş hipotezinin geçerli olduğu gen?", "APC",
          "APC: bir allel kalıtsal + diğer allel mutasyonu → adenom (Knudson adı PDF'te RB'de) · EGFR, RAS, MYC, siklin D onkogen"),
        Q("22-23", 76, "DNA tamir genlerinden biri?", "MSH2",
          "Mismatch tamir: MSH2, MLH1, PMS, PMS2 · Bcl-2 (antiapopitotik), NF-1 ve RB (süpresör), E-kaderin (adezyon) değil"),
        Q("22-23", 78, "Hangisi yanlıştır? (E2F–RB, protoonkogen allel, tümör progresyonu, replikatif havuz, onkofetal antijen)",
          "“E2F, RB ile kompleks halde bulunan süpresör bir gendir” (E2F transkripsiyon faktörüdür)",
          "Doğrular: protoonkogende tek allel yeter · tümör progresyonu tanımı · replikatif havuz ve onkofetal antijen ifadeleri bu PDF'ten değil"),
        Q("21-22", None, "RB mutasyonu sonucu gelişen tümör · Cevabı BRCA olan soru", "RB → retinoblastom/osteosarkom · BRCA → ailesel meme-over ca",
          "Öğrenci hatırlamasından derlenmiş sorular", n=2),
    ],
)
