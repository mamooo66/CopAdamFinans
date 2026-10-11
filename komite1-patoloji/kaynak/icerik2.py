# -*- coding: utf-8 -*-
"""Komite 1 Patoloji hap bilgi slaytlarının içeriği (Bölüm 11-22)."""

from icerik import B, C, Q, BOLUMLER

# ---------------------------------------------------------------- 11
BOLUMLER.append(dict(
    no=11, key="isim", baslik="Neoplazi: Tanım, İsimlendirme ve Benign–Malign Ayrımı",
    hoca="Prof. Dr. Çetin Boran", tarih="5 Ekim", saat="1 saat",
    kaynak="2025-26 ders slaytı: Neoplazi – isimlendirme (Ç. Boran)",
    ozet=["“Hangisi malign?” → -oma ile bitip malign olanlar: SEMİNOMA (2 kez), lenfoma, melanoma, mezotelyoma, hepatoma.",
          "Teratom = 3 germ yaprağı · anaplazi = diferansiasyonun ileri derecede kaybı · metastaz = malignitenin kesin bulgusu."],
    slaytlar=[
        [
            C("Temel kavramlar", [
                B("**Neoplazi (tümör)**: büyümede **otonomi** kazanmış, büyüme kontrolü kaybolmuş yeni doku; **klonal** (tüm hücreler tek hücreden)."),
                B("İki komponent: **parankim** (neoplastik hücreler — davranışı belirler) + **stroma** (bağ doku, damar, makrofaj, lenfosit — destek)."),
                B("Kollajenden zengin sert stroma = **desmoplazi** → **skiröz** tümör (ör. meme)."),
                B("**Benign**: lokal kalır, cerrahi olarak çıkarılabilir, hasta genellikle yaşar. **Malign**: invaziv, komşu yapıları tahrip eder, **metastaz** yapar."),
                B("Kanser = tüm malign tümörlerin genel adı (Latince yengeç); onkoloji = tümör bilimi."),
            ]),
            C("Benign isimlendirme: hücre tipi + “-oma”", [
                B("Lipoma, fibroma, kondroma, osteoma, **leiomyoma**, **rabdomyoma**."),
                B("**Adenom**: bez yapısı oluşturan / bez epitelinden kaynaklanan benign epitelyal tm. **Papillom**: yüzeyden parmaksı çıkıntılar."),
                B("**Polip**: mukozadan lümene uzanan, gözle görülen çıkıntı (benign veya malign). **Kistadenom**: kistik adenom (over)."),
            ]),
            C("Malign isimlendirme", [
                B("**SARKOM**: **mezenkimal** kökenli malign (stroma az → yumuşak, “etli”): fibrosarkom, liposarkom, **leiomyosarkom**, rabdomyosarkom, kondrosarkom, osteosarkom.", y="24-25"),
                B("**KARSİNOM**: **epitel** kökenli malign (3 germ yaprağından da: böbrek tübülü – mezoderm, epidermis – ektoderm, GİS mukozası – endoderm): **adenokarsinom** (glandüler), **skuamöz hücreli karsinom**.", y="24-25"),
                B("“-oma” ile bittiği hâlde **MALİGN**: **SEMİNOMA**, **lenfoma**, **melanoma**, **mezotelyoma**, **hepatoma (HCC)**, **glioma** (+ multipl miyelom).", y="23-24 25-26",
                  tuzak="Meningioma, fibroma, pleomorfik adenom, rabdomyoma → benign (çeldirici)"),
                B("**Blastom**: embriyonik doku tümörleri (nöroblastom, retinoblastom, nefroblastom/Wilms, hepatoblastom, medulloblastom). Malign tümör örneği: **asiner karsinom** (pankreas, tükürük bezi).", y="21-22"),
            ]),
        ],
        [
            C("Özel tümör terimleri", [
                B("**Mikst tümör**: **tek germ yaprağı**, kök hücrenin farklı yönlerde farklılaşması — **pleomorfik adenom** (epitelyal + miyoepitelyal; tükürük bezi), Wilms tümörü."),
                B("**TERATOM**: **totipotent (germ) hücrelerden**; **üç germ yaprağının (ektoderm, mezoderm, endoderm) dokuları**; benign (over matür kistik teratom – dermoid) ve malign formları var.", y="21-22"),
                B("**Hamartom**: o organın normal dokularının **düzensiz organize** kitlesi (ör. akciğer hamartomu)."),
                B("**Koristom**: normal dokunun **yanlış yerde** bulunması — heterotopi (ince barsak submukozasında pankreas)."),
            ]),
            C("Diferansiasyon, anaplazi, displazi", [
                B("**Diferansiasyon**: tümör hücrelerinin köken aldığı hücreye morfolojik/fonksiyonel benzerliği (iyi → kötü → **andiferansiye/anaplastik**)."),
                B("**ANAPLAZİ = diferansiasyonun ileri derecede kaybı** → malign tümörlerin özelliği: **pleomorfizm**, **hiperkromatik nükleus**, **N/S oranı ↑**, belirgin nükleol, **atipik mitoz**, **tümör dev hücresi**, polarite kaybı.", y="25-26"),
                B("**Displazi**: epitelde yapı ve organizasyon bozukluğu, uniformite kaybı, pleomorfizm, mitoz ↑; hafif-orta-şiddetli; **hafif-orta geri dönüşlü**; tüm kat = **karsinoma in situ** (bazal membran sağlam)."),
                B("**Atipik şekilli mitozlar** malignite ipucu; hızlı büyüyen tümörde beslenme yetersiz → **tümör nekrozu**."),
            ]),
            C("Benign ↔ Malign ve grade/stage", [
                B("**İnvazyon**: benign → **ekspansil, kapsüllü**, iyi sınırlı; malign → **infiltratif, destrüktif** (benign–malign ayrımında temel bulgu)."),
                B("**METASTAZ = malignitenin KESİN bulgusu**. Yollar: **vücut boşluğuna ekilme** (over, GİS ca; müsinöz apendiks tm → **psödomiksoma peritonei**; medulloblastom), **lenfatik** (karsinomlar), **hematojen** (sarkomlar; en sık karaciğer, akciğer)."),
                B("**Grade (derece)**: **mikroskopik** — diferansiasyon derecesi ve mitoz. **Stage (evre)**: klinik/radyolojik/cerrahi — **TNM** (boyut, lenf nodu, uzak metastaz); prognozda **evre daha önemli**."),
            ]),
        ],
    ],
    sorular=[
        Q("23-24", 80, "Hangisi malign bir tümördür?",
          "Seminoma", "Meningioma, fibroma, pleomorfik adenom, rabdomyoma benign"),
        Q("25-26", 80, "(Büyüme biyolojisi sorusunun doğru seçenekleri)",
          "“Seminoma malign bir tümördür” ✔ · “Anaplazi diferansiasyonun ileri derecede kaybıdır” ✔", "Sorunun yanlış ifadesi Bölüm 13'te", ref=True),
        Q("21-22", None, "Üç germ tabakasında da değişiklik gösteren tümör? · Hangisi malign tümördür?",
          "Teratom · Asiner karsinom", "Öğrenci hatırlamasından derlenmiş sorular", n=2),
    ],
))

# ---------------------------------------------------------------- 12
BOLUMLER.append(dict(
    no=12, key="molekuler", baslik="Neoplazinin Moleküler Temeli",
    hoca="Prof. Dr. Çetin Boran", tarih="5 ve 7 Ekim", saat="4 saat",
    kaynak="2025-26 ders slaytları: Tümörün moleküler temeli 1-2 (Ç. Boran)",
    ozet=["5 yılda 10 soru — her yıl en az 1! Genin tarifi verilip adı soruluyor: p53, RAS, RB/E2F, NF1, APC, MSH2, BRCA.",
          "Tümör süpresör = Knudson iki vuruş · protoonkogen = tek allel yeterli · p16 antikorla bloke edilemez."],
    slaytlar=[
        [
            C("Temel ilkeler", [
                B("Kanserin temeli **öldürücü olmayan genetik hasar** (çevresel, kalıtsal veya sporadik); tümör **monoklonal** (X'e bağlı G6PD izoenzimi, HUMARA metilasyonu, Ig/TCR gen düzenlenmesi, spesifik translokasyonla gösterilir)."),
                B("4 gen sınıfı: **protoonkogenler** (mutant allel **dominant** — tek allel mutasyonu yeterli) · **tümör süpresör genler** (**resesif** — iki allel) · **apoptoz genleri** · **DNA tamir genleri** (mutator fenotip; iki allel).", y="22-23"),
                B("Karsinogenez **çok basamaklı**dır; **tümör progresyonu** = zamanla invazivlik, metastaz gibi yeni yetenekler kazanma (tümör heterojenitesi; kanser kök hücreleri).", y="22-23"),
                B("**Malign transformasyon özellikleri**: büyüme sinyalinde kendine yeterlilik · büyüme inhibitörlerine duyarsızlık (TGF-β, CDKI) · **apoptoza direnç** (p53 mutasyonu, BCL-2) · DNA tamir defekti · **sınırsız bölünme (telomeraz)** · **anjiogenez** · **invazyon-metastaz** · **immün kaçış** · metabolik değişim (Warburg)."),
            ]),
            C("Hücre siklusu ve kontrol noktaları", [
                B("**Siklin D–CDK4** → **RB fosforilasyonu** → **E2F serbest** → G1/S geçişi; siklin E–CDK2 (S), siklin A–CDK2 (G2/M), siklin B–CDK1 (mitoz)."),
                B("CDK inhibitörleri: **CIP/KIP** — **p21 (p53 ile indüklenir)**, **p27 (TGF-β ile)**, p57 · **INK4/ARF (CDKN2A)** — **p16/INK4a** (siklin D–CDK4'ü bloke eder, RB'yi hipofosforile tutar), **p14/ARF** (**MDM2'yi inhibe** ederek p53'ü korur)."),
                B("Kontrol noktaları: **G1/S** (DNA hasarı → siklus durur, tamir; olmazsa apoptoz) · **G2/M** (iyonizan radyasyon hasarında önemli). Hasar sensörleri: **ATM**, ATR, RAD ailesi; ileticiler: CHK kinazlar."),
            ]),
            C("Hedefe yönelik antikor tedavisi", [
                B("Monoklonal antikorlar **hücre yüzeyi/ekstrasellüler** molekülleri bloke eder: **HER2 (trastuzumab)**, EGFR, **VEGF (bevacizumab)**, CD20, CD30; **c-KIT → imatinib** (TKİ); mutant RAS'ı bloke eden ajanlar geliştiriliyor."),
                B("**p16** hücre içi bir **tümör süpresör** → bloke edici antikor tedavisi **düşünülemez**.", y="23-24"),
            ]),
        ],
        [
            C("Onkogenler — büyüme faktörü ve reseptörleri", [
                B("Büyüme faktörü: **PDGF** (glioblastom; tümör hem PDGF hem reseptörünü yapar), **TGF-α** (sarkomlar, astrositom), FGF, HGF."),
                B("Tümörlerde **en sık mutant sinyal yolu: reseptör tirozin kinaz yolu** (MAPK ve PI3K/AKT)."),
                B("**ERBB1 (EGFR)**: SCC'lerin %80'i, glioblastom; akciğer adenoca'da nokta mutasyonu (EGFR inhibitörü). **ERBB2 (HER2/neu)**: **meme**, over, mide, akciğer adenoca'da **amplifikasyon** → monoklonal antikor."),
                B("**RET**: **MEN 2A/2B, ailesel medüller tiroid ca** (tam fonksiyon kaybı → Hirschsprung). **c-KIT**: **GIST** (imatinib), seminom. **ALK**: akciğer adenoca (EML4-ALK), ALCL. **FLT3**: AML."),
            ]),
            C("Onkogenler — sinyal iletimi, TF, siklus", [
                B("**RAS**: GTP bağlayan sinyal proteini; **hücre zarının iç yüzüne** yerleşir, **reseptörden aldığı büyüme sinyalini (MAPK/PI3K) çekirdeğe taşır**; tümörlerin %15-20'sinde nokta mutasyonu → GTPaz aktivitesi kaybı → **sürekli aktif** (KRAS: kolon, akciğer, pankreas).", y="24-25"),
                B("**BRAF** (melanom, kolon; BRAF inhibitörü), **PI3K**; PI3K antagonisti **PTEN** kaybı aynı sonucu verir."),
                B("Non-reseptör TK: **ABL — t(9;22) BCR-ABL (Philadelphia) → KML** (+ ALL), **imatinib** · **JAK2** → polisitemia vera, myeloproliferatif hastalıklar."),
                B("Transkripsiyon faktörü: **MYC — Burkitt t(8;14)** (Ig geni yanına), **N-MYC — nöroblastom** (amplifikasyon, kötü prognoz)."),
                B("Siklin/CDK: **siklin D1 — mantle hücreli lenfoma t(11;14)**, MM, meme; **CDK4** amplifikasyonu: melanom, sarkom, glioblastom."),
            ]),
        ],
        [
            C("Tümör süpresör genler (1)", [
                B("**RB** (13q14): hipofosforile RB **E2F'i bağlayarak** G1→S geçişini engeller; **RB inaktive olunca E2F serbest kalır, siklus ilerler** — siklusta **kilit süpresör**.", y="24-25 25-26 21-22"),
                B("**E2F** bir **transkripsiyon faktörüdür** (süpresör gen DEĞİL).", y="22-23",
                  tuzak="“E2F, RB geni ile kompleks hâlde bulunan süpresör bir gendir” → YANLIŞ"),
                B("Retinoblastom (%60 sporadik — iki allel somatik; ailesel — bir allel doğuştan) + **osteosarkom**. RB'yi etkisizleştirenler: mutasyon, CDK4/siklin D amplifikasyonu, p16 kaybı, **HPV E7**."),
                B("**Knudson'un iki vuruş hipotezi**: ailesel formda 1. mutasyon germline, 2. somatik (heterozigotluk kaybı) → **tümör süpresör genler** için geçerli (RB, **APC**, p53, NF1…).", y="22-23",
                  tuzak="EGFR, RAS, MYC, siklin D (onkogenler) için geçerli DEĞİL"),
                B("**TP53 (17p13.1) — “genomun bekçisi”**: DNA hasarında artar (yarı ömrü ~20 dk; **MDM2** yıkar) → **p21 ile siklusu durdurur** → tamir (GADD45) → tamir olmazsa **apoptoza yönlendirir** (BAX, PUMA).", y="25-26"),
                B("p53: tümörlerin **~%50'sinde mutant**; **Li-Fraumeni** (germline; sarkom, meme, lösemi, beyin, adrenal korteks); **HPV E6** p53'ü yıkar; MDM2 amplifikasyonu inaktive eder; trombospondin-1 ile anjiogenezi baskılar."),
            ]),
            C("Tümör süpresör genler (2)", [
                B("**APC** (WNT yolu): β-katenini yıkım kompleksinde tutar; kaybı → β-katenin çekirdekte TCF ile **MYC, siklin D1 ↑**; **FAP**; β-katenin mutasyonu: hepatoblastomların %50'si."),
                B("**E-kaderin (CDH1)**: hücreler arası adezyon; kaybı invazyon-metastazı kolaylaştırır — **ailesel mide kanseri**, lobüler meme ca."),
                B("**NF1 (nörofibromin)** = **GTPaz aktive edici protein → RAS'ı inaktive eder** → **sinyal iletim yolunda inhibitör**; nörofibromatozis tip 1 (nörofibrom, optik gliom, Lisch nodülü, café-au-lait).", y="23-24"),
                B("**NF2 (merlin)**: bilateral akustik schwannom, meningiom, ependimom. **VHL**: HIF-1α yıkımı → kaybında VEGF ↑ (berrak hücreli RCC, hemanjioblastom, feokromositoma)."),
                B("**PTEN** (PI3K/AKT inhibitörü): **Cowden**, endometrium ca. **SMAD2/4** (TGF-β): kolon, **pankreas**. **PTCH**: Gorlin (BCC, medulloblastom). **STK11**: Peutz-Jeghers. **WT1**: Wilms. **CDKN2A**: ailesel melanom, pankreas."),
            ]),
        ],
        [
            C("Apoptozdan kaçış", [
                B("**BCL-2** (antiapoptotik) — **foliküler lenfoma t(14;18)**: Ig geni yanına taşınır → aşırı ekspresyon."),
                B("İntrinsik: p53 → BAX/BAK → sitokrom c → APAF-1; BH3-only (BAD, BID, PUMA) dengeyi kurar. Ekstrinsik: Fas (CD95); **FLIP** kaspaz-8'i inhibe eder; IAP'lar kaspazları baskılar."),
            ]),
            C("DNA tamir defektleri ve genomik instabilite", [
                B("**Yanlış eşleşme (mismatch) tamiri**: **MSH2**, **MLH1**, PMS1/2 → **HNPCC (Lynch)**: **mikrosatellit instabilitesi**, proksimal kolon, endometrium, over ca.", y="22-23"),
                B("**Nükleotid eksizyon tamiri (NER)**: UV → pirimidin dimerleri → **kseroderma pigmentozum** (deri kanserleri)."),
                B("**Homolog rekombinasyon**: **BRCA1, BRCA2** (ailesel meme + over ca; BRCA2 erkek meme ca), **ATM** (ataksi-telenjiektazi, iyonizan radyasyona duyarlılık), **Bloom** (helikaz), **Fanconi anemisi**.", y="21-22"),
                B("RAG1/2, AID mutasyonları → lenfoid neoplazilere zemin."),
            ]),
            C("Diğer moleküler olaylar", [
                B("**Telomeraz** yeniden aktive → **sınırsız replikasyon** (normal hücre 60-70 bölünme → senesans)."),
                B("**Warburg etkisi** (aerobik glikoliz) → **18F-FDG PET** ile görüntüleme."),
                B("Kromozomal: **translokasyon** (BCR-ABL, MYC, BCL-2, siklin D1, **EWS-FLI1 t(11;22) Ewing**) · **delesyon** (RB, VHL) · **amplifikasyon** (**N-MYC – nöroblastom**, **HER2 – meme**; HSR, double minutes) · **kromotripsis**."),
                B("**Epigenetik**: süpresör gen promoter **hipermetilasyonu**, histon değişiklikleri, genomik imprinting (Prader-Willi/Angelman); **miRNA** (miR-155 → MYC)."),
                B("Tek onkogen yetmez (RAS + MYC birlikte → transformasyon); kolorektal karsinogenez: **APC → KRAS → SMAD4 → TP53** (adenom-karsinom sekansı)."),
            ]),
        ],
    ],
    sorular=[
        Q("25-26", 79, "“Gerektiğinde hücre siklusunu durdurur, gerekirse hücreyi apoptoza yönlendirir.”",
          "p53", "bcl-2, ras, raf, msh2 değil"),
        Q("24-25", 83, "“Hücre zarı iç yüzeyine yerleşmiştir; reseptörden aldığı büyüme sinyalini çekirdeğe taşır.”",
          "RAS", "NF-1, PTEN, p53, p16 değil"),
        Q("24-25", 84, "“İnaktive olduğunda E2F serbest kalır ve hücre siklusu ilerler.”",
          "RB", "Myc, BRCA1, MSH2, VHL değil"),
        Q("23-24", 76, "Bloke edici monoklonal antikorla tedavi seçeneği düşünülemeyecek gen?",
          "p16", "RAS, ERBB2, c-KIT, TGF-α hedeflenebilir"),
        Q("23-24", 77, "Hücre sinyal iletim yollarında inhibitör olarak yer alan?",
          "NF1", "p21 (CDKI), myc (TF onkogen), msh2 (tamir), ATM (hasar sensörü) değil"),
        Q("22-23", 75, "Knudson'un çift vuruş hipotezinin geçerli olduğu gen?",
          "APC", "EGFR, RAS, MYC, siklin D (onkogen) değil"),
        Q("22-23", 76, "DNA tamir genlerinden biri?",
          "MSH2", "Bcl-2, NF-1, RB, E-kaderin değil"),
        Q("22-23", 78, "Yanlış olan?",
          "“E2F, RB ile kompleks hâlde bulunan süpresör bir gendir” (E2F transkripsiyon faktörü)",
          "Doğrular: replikatif havuz genişse tümör hızlı küçülür · protoonkogende tek allel yeter · tümör progresyonu tanımı · onkofetal antijenler"),
        Q("21-22", None, "RB mutasyonu sonucu gelişen tümör · Cevabı BRCA olan soru",
          "RB → retinoblastom/osteosarkom · BRCA → ailesel meme-over ca", "Öğrenci hatırlamasından derlenmiş sorular", n=2),
    ],
))

# ---------------------------------------------------------------- 13
BOLUMLER.append(dict(
    no=13, key="buyume", baslik="Tümör Büyümesinin Biyolojisi, Anjiogenez, İnvazyon ve Metastaz",
    hoca="Prof. Dr. Çetin Boran", tarih="15 Ekim", saat="1 saat",
    kaynak="2025-26 ders slaytı: Neoplazilerin büyüme biyolojisi ve anjiogenez (Ç. Boran)",
    ozet=["Büyüme fraksiyonu–kemoterapi ilişkisi 2 kez: YÜKSEK büyüme fraksiyonu = kemoterapiye DUYARLI.",
          "Anti-VEGF (bevacizumab) → yeni damar oluşumu durur · hipoksi → HIF-1α → VEGF."],
    slaytlar=[
        [
            C("Büyüme kinetiği", [
                B("Büyüme hızını belirleyen 3 faktör: **ikiye katlanma süresi**, **büyüme fraksiyonu (replikatif havuzdaki hücre oranı)**, **hücre kaybı** (apoptoz, nekroz)."),
                B("Tek hücre → **30 katlanma = 10⁹ hücre ≈ 1 g** (klinik saptanabilir en küçük kitle) → **+10 katlanma = 10¹² hücre ≈ 1 kg** (yaşamla bağdaşan üst sınır)."),
                B("Hızlı büyüyen tümörlerde bile büyüme fraksiyonu ~%20; çoğu hücre G0'da. Benign/iyi diferansiye tümörler genelde daha yavaş büyür."),
            ]),
            C("Replikatif havuz ve kemoterapi", [
                B("Antineoplastik ilaçlar **siklustaki hücreleri** öldürür → **büyüme fraksiyonu YÜKSEK** tümörler (yüksek dereceli lenfoma, lösemi) **çok duyarlı**; **düşük büyüme fraksiyonlu** tümörler (kolon, meme ca) **dirençli**.", y="25-26 22-23",
                  tuzak="“Düşük büyüme fraksiyonlu tümörler antineoplastik tedaviye daha iyi yanıt verir” → YANLIŞ"),
                B("“Replikatif havuz ne kadar genişse kemoterapötikle tümör o kadar hızlı küçülür” → DOĞRU.", y="22-23"),
                B("**Debulking** (cerrahi/radyoterapiyle kitle küçültme) → G0 hücreler siklusa girer → ilaca duyarlılık ↑ (kombine tedavinin temeli)."),
                B("**Apoptoz tümör gelişimine karşı bir bariyerdir**; tümördeki nekroz/apoptoz büyümeyi yavaşlatır.", y="25-26"),
            ]),
            C("Tümör anjiogenezi", [
                B("Damarlanma olmadan tümör **1-2 mm**'yi geçemez; yeni damar: endotel öncüllerinin gelmesi veya kapillerlerden tomurcuklanma."),
                B("Anjiogenik: **VEGF, bFGF** (tümör/iltihap hücresi; stromadan proteazla açığa çıkar). Antianjiogenik: **anjiostatin** (plazminojen), **endostatin** (kollajen), **vaskülostatin** (transtiretin), **trombospondin-1**."),
                B("**Hipoksi → HIF-1α → VEGF ve FGF transkripsiyonu ↑**; **RAS/MYC** (MAPK) VEGF'i artırır.", y="21-22"),
                B("**p53** trombospondin-1'i artırır, VEGF/HIF-1'i azaltır → **p53 mutasyonu anjiogenezi başlatır**. Tümör damarları **sızdırgan, düzensiz**; endotel PDGF/IGF salgılar."),
                B("**Bevacizumab = anti-VEGF monoklonal antikor** → **yeni damar oluşumu durur** → tümör büyümesi durur.", y="24-25"),
            ]),
        ],
        [
            C("İnvazyon — ECM invazyonu basamakları", [
                B("1) **Hücreler arası bağların gevşemesi**: **E-kaderin kaybı** (β-katenin ile sitoskeletona bağlı); **SNAIL, TWIST** → **epitelyal-mezenkimal geçiş (EMT)** (E-kaderin ↓, vimentin/SMA ↑)."),
                B("2) **Matrikse tutunma**: integrinler → **laminin, fibronektin** reseptörleri."),
                B("3) **ECM yıkımı**: **matriks metalloproteinazlar (tip IV kollajenaz)**, katepsin D, ürokinaz plazminojen aktivatörü (tümör + stroma/iltihap hücreleri); yıkım ürünleri anjiogenez ve kemotaksisi uyarır."),
                B("4) **Göç (migrasyon)**: otokrin motilite faktörleri, kemotaksis."),
            ]),
            C("Metastaz — vasküler yayılım ve yuvalanma", [
                B("Tümör hücreleri dolaşımda **trombosit/lökositlerle emboli** oluşturur; milyonlarca hücreden çok azı metastaz yapar."),
                B("Organ tercihi: drenaj yolu + **endotel adezyon molekülleri**, **kemokinler** (meme ca **CXCR4, CCR7** → akciğer, lenf nodu), **CD44** (hiyaluronata bağlanır)."),
                B("**Prostat ca → kemik** · **akciğer ca → adrenal ve beyin** · **meme ca → kemik (osteolitik: PTHrP → RANKL → osteoklast)**; IGF salgılayan organlar tümörü çeker; **çizgili kas** neredeyse hiç metastaz almaz."),
            ]),
            C("Tümör metabolizması", [
                B("**Warburg etkisi**: bol O₂'de bile **aerobik glikoliz** — glikoliz az ATP verir (2 ATP; oksidatif fosforilasyon çok daha fazla) ama hızlı çoğalan hücreye **biyosentez için ara ürün** sağlar → **18F-FDG PET** ile tümör ve aktif dokular (kemik iliği) pozitif."),
            ]),
        ],
    ],
    sorular=[
        Q("25-26", 80, "Hangisi doğru DEĞİLDİR?",
          "“Düşük büyüme fraksiyonuna sahip tümörler antineoplastik ilaç tedavisine daha iyi yanıt verir”",
          "Doğrular: apoptoz tümör gelişimini önler · seminoma malign · RB kilit süpresör · anaplazi tanımı"),
        Q("24-25", 87, "Anti-VEGF monoklonal antikor verilen hastada tümör büyümesi durdu; en olası neden?",
          "Yeni damar oluşumu durmuştur", "Mutasyon olmaması, karsinojen yokluğu, EGFR aktivasyonu, DNA tamir mutasyonu değil"),
        Q("22-23", 78, "(Doğru seçenek olarak)",
          "“Replikatif havuz ne kadar genişse kemoterapötiklerle tümör o kadar hızlı küçülür” ✔", "Bkz. Bölüm 12 – sorunun yanlış ifadesi E2F", ref=True),
        Q("21-22", None, "Hipoksi durumunda uyarılan?",
          "HIF-1α", "Öğrenci hatırlamasından derlenmiş soru"),
    ],
))

# ---------------------------------------------------------------- 14
BOLUMLER.append(dict(
    no=14, key="karsinojen", baslik="Karsinojen Ajanlar",
    hoca="Prof. Dr. Çetin Boran", tarih="9 Ekim", saat="1 saat",
    kaynak="2025-26 ders slaytı: Karsinojenik ajanlar (Ç. Boran)",
    ozet=["5 yılda 7 soru! EBV → Burkitt (2 kez, + nazofarinks ca) · DES = PROMOTER (2 kez).",
          "HPV → kondiloma + SCC · HBV = transforme edici virüs · aflatoksin → HCC."],
    slaytlar=[
        [
            C("Kimyasal karsinogenez: başlatma + promosyon", [
                B("3 temel karsinojen: **kimyasallar**, **radyan enerji**, **onkojenik mikroplar**."),
                B("**Başlatıcı (inisiyatör)**: DNA'da **kalıcı hasar (mutasyon)**; elektrofilik — DNA/RNA/proteinlerin nükleofilik bölgelerine saldırır; **tek başına kanser yapamaz**."),
                B("**PROMOTER**: başlatılmış hücrede **proliferasyon** yaptırır; **tek başına tümör geliştiremez**, başlatıcıdan **SONRA** uygulanmalı (önce verilirse tümör olmaz)."),
                B("Promoter örnekleri: **forbol esteri** (PKC aktivatörü), **fenobarbital** (TGF-β yolunu bloke), **ÖSTROJEN, DİETİLSTİLBESTROL (DES)**, **safra asitleri** (yağlı diyet → kolon ca), **alkol** (muhtemel).", y="24-25 25-26"),
            ]),
            C("Başlatıcılar", [
                B("**Direkt etkili** (metabolik aktivasyon gerekmez; genelde **zayıf**): **alkilleyici ajanlar** — **siklofosfamid, klorambusil, busulfan**, nitrozoüreler, β-propiolakton, dimetil sülfat → tedavi sonrası **AML**.", y="24-25 25-26",
                  tuzak="Busulfan, kemoterapötikler PROMOTER değil, başlatıcıdır"),
                B("**İndirekt (prokarsinojen; sitokrom P450 ile aktive)**: **polisiklik aromatik hidrokarbonlar (benzo[a]piren)** — sigara, ızgara/yanmış hayvan yağları, tütsülenmiş et-balık; CYP1A1 polimorfizmi akciğer ca riskini ↑.", y="24-25 25-26"),
                B("**Aromatik aminler ve azo boyaları**: kauçuk sanayinde **β-naftilamin → mesane ca (×50)**; gıda azo boyaları (tereyağı sarısı, scarlet red) → HCC.", y="25-26"),
                B("**AFLATOKSİN B1** (Aspergillus flavus; yerfıstığı, mısır, pirinç) → **HCC** (p53 mutasyonu).", y="21-22 24-25"),
                B("**Nitrozamin/amidler**: koruyucu nitratlar → midede nitrit → **mide ca**. Diğer: asbest, **vinil klorür (KC hemanjiosarkomu)**, arsenik (deri), krom-nikel (akciğer), insektisitler.", y="24-25"),
            ]),
            C("Radyasyon", [
                B("**UV**: karsinojen olan **UVB (280-320 nm)**; UVC ozonda tutulur. **Pirimidin dimerleri** → NER ile tamir (bozuksa **kseroderma pigmentozum**, OR); RAS/p53 mutasyonu → BCC, SCC, melanom.", y="25-26"),
                B("**İyonizan** (X, γ, α, β, nötron): en sık **lösemi**, ikinci **tiroid ca**; GİS, kemik ve deri nispeten dirençli."),
            ]),
        ],
        [
            C("Onkojenik DNA virüsleri", [
                B("**HPV**: yüksek riskli **tip 16, 18** (31, 33, 35, 51) → **serviks/anogenital SCC**; düşük riskli **tip 6, 11** → **kondiloma akuminatum (genital siğil)**.", y="23-24"),
                B("HPV mekanizması: **E6 → p53** yıkımı (+ TERT ↑, ölümsüzleşme) · **E7 → RB**'ye bağlanır (+ p21, p27 inaktivasyonu)."),
                B("**EBV**: **CD21** üzerinden B hücreye girer; **LMP-1** (aktif CD40 gibi; NF-κB, JAK/STAT; BCL-2 ↑), **EBNA-2** (siklin D ↑), vIL-10 → poliklonal B proliferasyonu."),
                B("EBV ilişkili tümörler: **BURKİTT lenfoma** (endemik Afrika; sıtma ko-faktör), **NAZOFARİNKS karsinomu**, **Hodgkin lenfoma**, immünsüprese hastada B hücreli lenfoma; mide ca, NK/T lenfoma.", y="24-25 25-26"),
                B("**HBV** (ve HCV): **HCC**; indirekt ve multifaktöriyel — kronik hasar + rejeneratif hiperplazi; **HBx** proteini transkripsiyon faktörlerini aktive eder → **transforme edici virüs**.", y="22-23",
                  tuzak="VZV, CMV, HSV, poliovirüs transforme edici virüs değil"),
                B("**HHV-8 (KSHV)** → Kaposi sarkomu · **Merkel hücreli poliomavirüs** → Merkel hücreli ca."),
            ]),
            C("Onkojenik RNA virüsü ve bakteriler", [
                B("**HTLV-1**: insanda tümör yapan iyi tanımlanmış **tek RNA virüsü**; **CD4+ T** tropizmi → **erişkin T hücreli lösemi/lenfoma**; **Tax** geni; tropikal spastik paraparezi."),
                B("**Helicobacter pylori** → **mide adenokarsinomu** + **MALT lenfoma** (marjinal zon); kronik inflamasyon + **CagA** geni."),
                B("Diğer: Schistosoma haematobium → mesane SCC; Clonorchis → kolanjiokarsinom.", g="ENFEKSİYON 23-24"),
            ]),
        ],
    ],
    sorular=[
        Q("25-26", 76, "Burkitt lenfoma ve nazofaringeal karsinomun etyopatogenezinde önemli rol oynayan?",
          "Epstein-Barr virüsü", "HPV, HBV, şistozomiyazis, H. pylori değil"),
        Q("25-26", 81, "Promoter etkisi olan karsinojen?",
          "Dietilstilbestrol", "UV, kemoterapötikler, PAH, azo boyaları = başlatıcı"),
        Q("24-25", 78, "Burkitt lenfoma gelişiminde rolü olan enfeksiyon?",
          "Epstein-Barr virüsü", "H. pylori, HPV, HBV, şistozomiyazis değil"),
        Q("24-25", 86, "Kanser progresyonunu sağlayan (promoter) ajan?",
          "Dietilstilbestrol (sentetik östrojen)", "PAH, busulfan, nitrozamin, aflatoksin = başlatıcı"),
        Q("23-24", 73, "Kondiloma akuminatum ve skuamöz hücreli karsinom gelişiminde rolü olan virüs?",
          "Human papilloma virüs", "EBV, HSV, HBV, VZV değil"),
        Q("22-23", 73, "Transforme edici virüs grubunda sayılabilen?",
          "Hepatit B virüsü", "VZV, CMV, HSV, poliovirüs değil"),
        Q("21-22", None, "Hepatoselüler karsinom yapan ajan?",
          "Aflatoksin B1", "Öğrenci hatırlamasından derlenmiş soru"),
    ],
))

# ---------------------------------------------------------------- 15
BOLUMLER.append(dict(
    no=15, key="konak", baslik="Tümöre Karşı Konak Savunması, Tümörün Konağa Etkileri, Kanserin Tanısı",
    hoca="Prof. Dr. Çetin Boran", tarih="13 Ekim", saat="1 saat",
    kaynak="2025-26 ders slaytı: Tümöre karşı savunma, kanserin moleküler tanısı (Ç. Boran)",
    ozet=["Onkofetal antijen 2 kez: CEA (23-24) ve AFP (25-26) — çeldiriciler MUC-1, CD20, CD30, CD8, MHC.",
          "Paraneoplastik sendrom: en sık endokrinopati Cushing (küçük hücreli akciğer ca)."],
    slaytlar=[
        [
            C("Tümör antijenleri", [
                B("1) **Mutant gen ürünleri**: p53, RAS, BCR-ABL…"),
                B("2) **Aşırı eksprese normal proteinler**: **tirozinaz (melanom)**; **kanser-testis antijenleri** (**MAGE**, GAGE, RAGE — erişkinde yalnız testiste)."),
                B("3) **Onkojenik virüs antijenleri** (HPV E6/E7, EBV)."),
                B("4) **ONKOFETAL ANTİJENLER**: fetal dokuda bulunup sonradan azalan/kaybolan, tümörde yeniden üretilen antijenler — **CEA** (kolon, pankreas, mide, meme ca), **AFP** (**HCC**, yolk sac/germ hücreli tm); inflamasyonda da hafif ↑ olabilir; takip için değerli.", y="23-24 25-26"),
                B("5) **Değişmiş yüzey glikolipid/glikoproteinleri**: **CA-125 (over)**, **CA 19-9** (pankreas, over), **MUC-1** (over, meme) — onkofetal DEĞİL.", y="23-24 25-26"),
                B("6) **Hücre tipine özgü diferansiasyon antijenleri**: **CD20** (B; rituksimab), **CD30** (Hodgkin, ALCL) — onkofetal DEĞİL.", y="23-24 25-26"),
                B("Diğer belirteçler: **PSA** (prostat), **hCG** (koryokarsinom), CA 15-3 (meme), kalsitonin (medüller tiroid ca)."),
            ]),
            C("Antitümör immünite", [
                B("Ana savunma **hücresel immünite**: **CD8+ sitotoksik T** (MHC I; tümörü infiltre eden CTL ↑ = iyi prognoz), **NK hücreleri** (ön duyarlılaşma gerekmez; **MHC I kaybeden hücreleri öldürür** — ilk savunma), **makrofajlar** (IFN-γ ile aktive)."),
                B("**İmmün gözetim**: konjenital immün yetmezlikte tümör **~200 kat** sık; immünsüpresyonda en sık **B hücreli lenfoma**; **X'e bağlı lenfoproliferatif sendrom (SAP)** → şiddetli EBV enfeksiyonu, lenfoma."),
            ]),
        ],
        [
            C("Tümörün immün sistemden kaçışı", [
                B("Antijen negatif varyantların seçilimi · **MHC I kaybı** (CTL'den kaçar, NK'ya hedef olur)."),
                B("**İmmün kontrol noktaları**: APC'de kostimülatör (B7) ↓ → T hücre **CD28** yerine inhibitör **CTLA-4**'e bağlanır; tümör **PD-L1/PD-L2** → T hücrede **PD-1** → inhibisyon → tedavide **anti-PD-1/PD-L1, anti-CTLA-4**."),
                B("İmmünsüpresif salgılar: **TGF-β, IL-10, VEGF, PGE₂**; Treg uyarılması; glikokaliksle antijen maskelenmesi; **Fas ligandı** (melanom, HCC) → CTL apoptozu."),
            ]),
            C("Tümörün konağa etkileri", [
                B("Lokal bası/obstrüksiyon, hormon üretimi (fonksiyonel adenom), kanama ve sekonder enfeksiyon (ülserasyon), rüptür/infarkt."),
                B("**Kanser kaşeksisi**: progresif yağ + kas kaybı, iştahsızlık, anemi; **bazal metabolizma ARTMIŞTIR**; TNF, IL-6, proteolitik faktörler sorumlu."),
            ]),
            C("Paraneoplastik sendromlar", [
                B("Tümörün yayılımı ve kaynak dokunun hormonal etkisiyle **açıklanamayan** sistemik bulgular; kanserin **ilk bulgusu** olabilir.",
                  g="İÇ HAST. 24-25"),
                B("**Cushing sendromu** — ektopik hormonlarla **en sık endokrinopati**; **küçük hücreli akciğer ca** (ACTH/POMC), pankreas ca, nöral tm.", y="21-22"),
                B("**SIADH → hiponatremi** (küçük hücreli akciğer ca) · **hiperkalsemi**: **PTHrP** (akciğer **skuamöz hücreli ca**, meme, böbrek, over, ATLL) · hipoglisemi (fibrosarkom, HCC) · **karsinoid sendrom** (serotonin, bradikinin) · **polisitemi** (eritropoetin: RCC, serebellar hemanjiom, HCC).",
                  g="İÇ HAST. 22-23"),
                B("Nöromüsküler: **myastenia gravis** (timoma, bronkojenik ca), **Lambert-Eaton** (küçük hücreli akciğer ca). Deri: **akantozis nigrikans** (mide, akciğer, uterus ca), **dermatomiyozit**.",
                  g="İÇ HAST. 22-23 · 23-24"),
                B("**Hipertrofik osteoartropati + çomak parmak** (bronkojenik ca) · **Trousseau** migratuvar tromboflebit (**pankreas**, akciğer — müsin) · DIC · **nonbakteriyel trombotik endokardit** · nefrotik sendrom."),
            ]),
        ],
        [
            C("Kanserin laboratuvar tanısı", [
                B("**Histolojik/sitolojik**: eksizyonel/insizyonel biyopsi, **İİAB**, sitolojik yayma (Pap), **frozen**."),
                B("**İmmünohistokimya**: tümör tipi; **metastatik tümörün kökeni** (**PSA** – prostat, **TTF-1** – akciğer/tiroid); prognostik/tedavi molekülleri (**c-erbB2/HER2** – meme, **ALK** – akciğer ca ve lenfoma)."),
                B("**Flow sitometri**: lösemi/lenfomalarda yüzey antijenleri, hızlı çoklu ölçüm. **Dolaşan tümör hücreleri** (likit biyopsi)."),
                B("**Moleküler/sitogenetik**: PCR ile **Ig/TCR gen düzenlenmesi → monoklonalite**; translokasyon (**t(11;22) → Ewing sarkomu**); FISH; DNA mikrodizi/NGS."),
            ]),
            C("Moleküler yöntemler ne zaman gerekli?", [
                B("**Prognoz**: **N-MYC artışı + 1p kaybı → nöroblastom kötü**; oligodendrogliomada **1p/19q kaybı → tedaviye iyi yanıt** (EGFR artışı kötü)."),
                B("**Minimal rezidüel hastalık**: KML'de PCR ile **BCR-ABL** taraması."),
                B("**Ailesel yatkınlık**: **BRCA1, BRCA2, RET** germline mutasyonları."),
                B("**Hedefe yönelik tedavi**: **PML-RARA** (akut promiyelositik lösemi), **BCR-ABL** (KML, ALL), **EGFR/ALK** (akciğer ca), **BRAF** (melanom — “BRAFoma”lar)."),
            ]),
        ],
    ],
    sorular=[
        Q("25-26", 82, "Hangisi onkofetal antijendir?",
          "AFP", "MUC-1, CD20, CD8, MHC değil"),
        Q("23-24", 81, "Hangisi onkofetal antijendir?",
          "CEA", "CD20, CD30, MUC-1, MHC class II değil"),
        Q("21-22", None, "Hangisi paraneoplastik sendrom örneğidir?",
          "Cushing sendromu", "Öğrenci hatırlamasından derlenmiş soru"),
    ],
))

# ---------------------------------------------------------------- 16
BOLUMLER.append(dict(
    no=16, key="epidem", baslik="Neoplazide Epidemiyoloji",
    hoca="Doç. Dr. Selma Erdoğan Düzcü", tarih="8 Ekim", saat="1 saat",
    kaynak="Robbins Temel Patoloji + T.C. Sağlık Bakanlığı kanser istatistikleri",
    ozet=["Türkiye: erkekte en sık AKCİĞER, kadında MEME kanseri (23-24).",
          "Preneoplastik lezyonlar: lökoplaki → ağız SCC (22-23)."],
    slaytlar=[
        [
            C("İnsidans ve mortalite", [
                B("Dünyada en sık kanserler **akciğer** ve **meme**; kanser ölümlerinde **1. akciğer**."),
                B("**TÜRKİYE**: **erkekte en sık AKCİĞER** (trakea-bronş-akciğer), ardından prostat, kolorektal, mesane, mide; **kadında en sık MEME**, ardından tiroid, kolorektal, uterus korpus.", y="23-24",
                  tuzak="“Erkekte prostat, kadında meme” → YANLIŞ (erkekte 1. akciğer, 2. prostat) · “erkekte mide” → YANLIŞ"),
                B("Çocuklarda en sık: **lösemi (ALL)**, SSS tümörleri, lenfoma; ayrıca nöroblastom, Wilms, retinoblastom, **rabdomyosarkom**."),
            ]),
            C("Risk faktörleri", [
                B("**Coğrafya/çevre**: mide ca (Japonya; nitrozamin, tütsülenmiş gıda), HCC (HBV, aflatoksin), Burkitt (Afrika — EBV + sıtma), nazofarinks ca (Güney Çin — EBV)."),
                B("**Yaşam tarzı**: sigara, alkol, diyet, **obezite**, üreme öyküsü (uzun östrojen maruziyeti → meme/endometrium ca); mesleki karsinojenler; enfeksiyonlar (~%15 kanser).", g="İÇ HAST. 25-26"),
                B("**Yaş**: karsinomların çoğu **55 yaş sonrası** (mutasyon birikimi, immün yanıt ↓)."),
                B("**Kronik inflamasyon**: ülseratif kolit/Crohn → kolon ca; H. pylori → mide ca/MALT; HBV/HCV → HCC; Barrett → adenoca; Schistosoma → mesane SCC."),
                B("**İmmün yetmezlik**: EBV ilişkili lenfoma, HPV ilişkili SCC, Kaposi (HHV-8)."),
            ]),
        ],
        [
            C("Prekanseröz (preneoplastik) lezyonlar", [
                B("**LÖKOPLAKİ** (ağız, vulva, penis; beyaz plak, skuamöz hiperplazi/displazi) → **ağız boşluğunda SCC**.", y="22-23",
                  tuzak="Hashimoto, endometrial hiperplazi, siroz, Graves ağız SCC zemini değil"),
                B("**Endometrial hiperplazi** (östrojen) → endometrium adenoca · **Barrett** → özefagus adenoca · **kronik atrofik gastrit/intestinal metaplazi** → mide adenoca.", y="23-24 24-25"),
                B("Kolonun **villöz adenomu** (yüksek risk), **solar keratoz** → SCC, **serviks displazisi (CIN/SIL)** → SCC, **siroz** → HCC, kronik ülser/yanık skarı (**Marjolin ülseri**) → SCC."),
            ]),
            C("Kalıtsal kanser sendromları", [
                B("**OD kalıtsal sendromlar** (süpresör gen germline mutasyonu): ailesel **retinoblastom (RB)**, **FAP (APC)**, **Li-Fraumeni (TP53)**, **NF1/NF2**, **MEN1, MEN2 (RET)**, **BRCA1/2**, **Lynch/HNPCC (MSH2, MLH1)**, VHL, Cowden (PTEN), Peutz-Jeghers (STK11), Gorlin (PTCH)."),
                B("**OR DNA tamir defekti sendromları**: kseroderma pigmentozum, ataksi-telenjiektazi, Bloom, Fanconi anemisi."),
                B("Ailesel kanser ipuçları: erken yaş, ≥2 yakın akraba, multipl/bilateral tümör (meme, over, kolon, pankreas)."),
                B("Önleme: sigara bırakma, **HPV ve HBV aşısı**, H. pylori eradikasyonu, taramalar (Pap smear, mamografi, kolonoskopi)."),
            ]),
        ],
    ],
    sorular=[
        Q("23-24", 69, "Türkiye birleşik veri tabanına göre erkek ve kadınlarda en sık görülen kanserler?",
          "Erkekte akciğer, kadında meme kanseri", "Erkekte prostat/mide, kadında over/tiroid/kolorektal değil"),
        Q("22-23", 69, "Ağız boşluğunda skuamöz hücreli karsinom gelişiminde rol oynayan preneoplastik bozukluk?",
          "Lökoplaki", "Hashimoto, endometrial hiperplazi, karaciğer sirozu, Graves değil"),
    ],
))

# ---------------------------------------------------------------- 17
BOLUMLER.append(dict(
    no=17, key="epitel", baslik="Epitelyal Tümörler",
    hoca="Doç. Dr. Selma Erdoğan Düzcü", tarih="13 Ekim", saat="2 saat",
    kaynak="2025-26 ders notları (S. E. Düzcü) + Robbins Temel Patoloji",
    ozet=["Her yıl gibi: adenokarsinom (gland yapısı / malign epitelyal), taşlı yüzük (linitis plastika), lobüler (indian file).",
          "Ders notu: “Kondiloma akuminatum her sene soruluyor” · “Karsinoma in situ soruluyor”."],
    slaytlar=[
        [
            C("Benign epitelyal tümörler — yüzey epiteli", [
                B("**Papillom**: yüzeyden parmaksı çıkıntılar (fibrovasküler kor); **skuamöz papillom** (ağız, larinks; HPV 6/11), **ürotelyal papillom** (en sık mesane), **verruka vulgaris** (siğil, viral)."),
                B("**KONDİLOMA AKUMİNATUM**: **genital/anogenital** papillom; **HPV 6 ve 11**; **akantoz**, **koilositler**; bir çeşit siğil.", y="23-24"),
                B("**Seboreik keratoz**: yaşlılarda deride “yapıştırılmış gibi” pigmente lezyon (ani çoklu çıkış → Leser-Trélat)."),
            ]),
            C("Benign epitelyal tümörler — bez epiteli", [
                B("**Adenom**: kolonda **tübüler, villöz (en yüksek malignite riski), tübülovillöz**; foliküler adenom (tiroid, kolloid dolu), solid adenom (hipofiz, Langerhans — fonksiyonel), kistadenom (over)."),
                B("Polipler: **adenomatöz** (neoplastik; displazi) · **jüvenil polip** (hamartomatöz, çocuk, rektum) · **Peutz-Jeghers** (OD, hamartomatöz, mukokutanöz pigmentasyon) · **FAP/Gardner** (OD; yüzlerce adenom; Gardner'da osteom, dezmoid)."),
                B("**Pleomorfik adenom (benign mikst tümör)**: **tükürük bezinin en sık tümörü**, en sık **parotis**; epitel/miyoepitel + miksoid/kondroid stroma; nüks eğilimi."),
                B("**Warthin tümörü**: parotis; **sigara** ilişkili; onkositik çift sıra epitel + lenfoid stroma. **Onkositom**: mitokondriden zengin eozinofilik hücreler."),
                B("**Hamartomatöz polip, kondiloma, Warthin, pleomorfik adenom = BENİGN**; epitelyal kanser değil.", y="24-25 21-22"),
            ]),
            C("Karsinom — genel", [
                B("En sık malign tümörler; **lenfatik** yolla yayılma eğilimi; desmoplazi → **skiröz** tip (en sık meme)."),
                B("**Karsinoma in situ**: displazi **tüm epitel kalınlığında**, **bazal membran sağlam** → invazyon/metastaz yok (serviks, DCIS, Bowen). Bazal membran aşılınca → **invaziv karsinom**."),
            ]),
        ],
        [
            C("Skuamöz (yassı) hücreli karsinom", [
                B("Çok katlı yassı epitelden (deri, ağız, larinks, özefagus, serviks, vulva, anüs) veya **skuamöz metaplazi** zemininde (bronş, mesane); erkekte daha sık."),
                B("İyi diferansiye: **keratin incileri (glob korne)**, **hücreler arası köprüler**, diskeratoz; kötü diferansiyede keratinizasyon azalır."),
                B("Özel tipler: **verrüköz karsinom** (iyi diferansiye, metastaz nadir), iğsi hücreli, **lenfoepitelyoma** (nazofarinks; EBV; lenfomayla karışır)."),
            ]),
            C("ADENOKARSİNOM", [
                B("Bez/gland epitelinden; **tümör hücrelerinin GLAND (bez) benzeri yapı oluşturması** = adenokarsinom morfolojisi; **malign epitelyal tümör**.", y="23-24 24-25",
                  tuzak="Nükleus büyüklüğü, muskularis invazyonu, pembe sitoplazma, belirgin nükleol adenoca'ya ÖZGÜ değil"),
                B("**Müsin** üretir (PAS, Alcian blue +); **keratin incisi YAPMAZ**.", y="22-23",
                  tuzak="“Adenokarsinomlarda keratin yapımı görülür” → YANLIŞ"),
                B("**Papiller adenokarsinom**: fibrovasküler korlu papiller yapılar, **psammom cisimcikleri** (tiroid papiller ca, over seröz ca). **Asiner karsinom** (pankreas, tükürük bezi) malign.", y="21-22"),
            ]),
            C("Özel karsinom tipleri", [
                B("**TAŞLI YÜZÜK HÜCRELİ KARSİNOM**: sitoplazmada **yoğun müsin → çekirdek kenara itilir**; **diffüz mide ca** → tüm duvar kalınlaşır = **LİNİTİS PLASTİKA**; **kötü prognozlu, agresif**; overe metastaz = Krukenberg.", y="25-26 22-23",
                  tuzak="“Taşlı yüzük hücreli karsinomlar çok iyi prognozludur” → YANLIŞ"),
                B("**Lobüler karsinom (meme)**: kohezyonsuz küçük hücreler **“INDIAN FILE” (tesbih dizisi)** dizilimi; E-kaderin kaybı.", y="22-23"),
                B("**Medüller karsinom (meme)**: yumuşak, **stromada yoğun lenfosit infiltrasyonu**. **Müsinöz (kolloid/jelatinöz) karsinom**: **memede prognozu iyi**."),
                B("**Medüller TİROİD karsinomu**: C hücresi (kalsitonin) → **stromada AMİLOİD**.", y="22-23",
                  tuzak="“Tiroid papiller karsinomunda amiloid birikimi karakteristiktir” → YANLIŞ (medüller)"),
                B("**Anaplastik (indiferansiye) karsinom**: belirgin atipi, **kötü diferansiye**, tümör dev hücreleri.", y="22-23",
                  tuzak="“Anaplastik tümörler atipi göstermeyen iyi diferansiye tümörlerdir” → YANLIŞ"),
                B("**Berrak (şeffaf) hücreli** (böbrek; vajina-serviks-endometrium) · **bazal hücreli karsinom** (derinin bazal tabakası; **lokal destrüktif, metastaz beklenmez**)."),
            ]),
        ],
    ],
    sorular=[
        Q("25-26", 77, "Tüm mide duvarını kalınlaştırmış, linitis plastika; müsin nedeniyle çekirdeği kenara itilmiş malign epitelyal tm?",
          "Taşlı yüzük hücreli karsinom", "Skuamöz papillom, Warthin, SCC, foliküler adenom değil"),
        Q("24-25", 81, "Malign epitelyal tümörler arasında yer alan?",
          "Adenokarsinom", "Pleomorfik adenom, hamartomatöz polip, kondiloma akuminatum, Warthin benign"),
        Q("23-24", 74, "Midede adenokarsinom morfolojisini gösteren özellik?",
          "Tümör hücrelerinin gland benzeri yapı oluşturması", "Büyük nükleus, muskularis invazyonu, pembe sitoplazma, belirgin nükleol değil"),
        Q("22-23", 70, "Malign epitelyal tümörlerle ilgili doğru olan?",
          "Lobüler karsinomlarda hücreler indian file (tesbih dizisi) oluşturabilir",
          "Çeldiriciler: taşlı yüzük iyi prognoz · papiller tiroid ca'da amiloid · anaplastik iyi diferansiye · adenoca'da keratin"),
        Q("21-22", None, "Hangisi epitelyal kanser değildir? (polip, papillom, adenom, adenokarsinom, ÇKYE ca)",
          "Benign olanlar (polip/papillom/adenom) — kanser = karsinom", "Öğrenci hatırlamasından; kesin şık bilinmiyor"),
    ],
))

# ---------------------------------------------------------------- 18
BOLUMLER.append(dict(
    no=18, key="yumusak", baslik="Yumuşak Doku Tümörleri",
    hoca="Dr. Öğr. Üyesi Songül Peltek Özer", tarih="12 Ekim", saat="1 saat",
    kaynak="2025-26 ders slaytı: Yumuşak doku tümörleri (S. P. Özer)",
    ozet=["3 soru: rabdomyosarkom = çocukluk çağının en sık yumuşak doku sarkomu · desmoid metastaz yapmaz · leiomyosarkom yumuşak doku tm.",
          "Slayttaki “en sık”lar: erişkinde lipom (benign) ve MFH (sarkom); liposarkomda miksoid alt tip."],
    slaytlar=[
        [
            C("Genel", [
                B("**Mezenkimal kökenli, non-epitelyal** dokuların tümörleri (**iskelet sistemi hariç**): **kas, yağ, fibröz doku, damar, periferik sinir**.", y="24-25",
                  tuzak="Kondrosarkom (kıkırdak), RCC, malign melanom, seminom yumuşak doku tm değil"),
                B("Yerleşim: **%40 uyluk**, %30 gövde ve retroperiton. Sarkomlar hematojen yayılır (en sık **akciğer**)."),
                B("Etiyoloji: **radyasyon**, kimyasal/termal yanık, travma, fenoksiherbisid, klorofenol, **HHV-8**; sendromlar: **Li-Fraumeni, NF1, Gardner**, Osler-Weber-Rendu."),
            ]),
            C("Yağ dokusu tümörleri", [
                B("**Lipom**: **erişkin çağın en sık yumuşak doku tümörü**; en sık **subkutan**; tek, sporadik, ağrısız. Tipler: klasik, fibrolipom, **anjiyolipom**, myolipom, myelolipom."),
                B("**Hibernom**: **kahverengi yağ dokusu** tümörü; çocukta; arka boyun ve retroperiton."),
                B("**Liposarkom**: 5-6. dekat; derin dokular, **retroperiton**, alt ekstremite. Tanı: **lipoblast** (**S-100 +**), **MDM2 +**."),
                B("**İyi diferansiye ve miksoid → low grade**; yuvarlak hücreli ve **pleomorfik → high grade**; iyi diferansiyeler metastaz yapmaz, lokal nüks; ~%10'u dediferansiye olur."),
                B("**En sık alt tip (ders slaytı): miksoid liposarkom** — hiyaluronattan zengin matriks + **“tavuk kümesi / kaz ayağı” damarlanma**."),
            ]),
            C("Fibröz tümörler ve tümör benzeri lezyonlar", [
                B("**Nodüler fasiit**: **reaktif** fibroblastik proliferasyon (neoplazi değil) — **sarkomla karışır**; gençlerde, **hızlı büyür**, bazen ağrılı; en sık üst ekstremite ve gövde; %15 travma sonrası; tedavi **basit eksizyon**."),
                B("**Fibromatozlar**: lokal infiltratif, **cerrahi sonrası sık nüks**; yüzeyel: **palmar (Dupuytren kontraktürü)**, **penil (Peyronie)**, fibromatosis colli (konjenital tortikolis)."),
                B("**Derin fibromatozis = DESMOİD TÜMÖR** (agresif/muskuloaponörotik fibromatozis): sıklıkla **kadın, gebelikte/sonrası**, **ön karın kasları**; lokal agresif ama **METASTAZ YAPMAZ**.", y="22-23"),
                B("**Fibrom** (benign) · **Fibrosarkom** (malign; derin dokular — kalça, diz, gövde; **“herringbone” — balık kılçığı paterni**)."),
            ]),
        ],
        [
            C("Fibrohistiyositik tümörler", [
                B("**Fibröz histiyositom (dermatofibrom)**: deri ve subkutis, erişkin; eksizyon kür sağlar."),
                B("**Dermatofibrosarkoma protuberans**: **borderline malign**; dermis-subkutiste yavaş büyüyen nodüller."),
                B("**Malign fibröz histiyositom (MFH)**: **erişkinin en sık yumuşak doku sarkomu** (ders slaytı); **radyasyon sonrası en sık sarkom**; 50-70 yaş; tipler: **storiform-pleomorfik**, inflamatuvar, anjiyomatoid, miksoid (miksofibrosarkom)."),
            ]),
            C("Kas tümörleri", [
                B("**RABDOMYOSARKOM**: **gençlerin/çocukluk çağının EN SIK yumuşak doku sarkomu**; agresif, lenf nodu metastazı yapabilir; derin kas grupları, retroperiton.", y="25-26",
                  tuzak="Liposarkom, anjiosarkom, Kaposi, MFH değil"),
                B("RMS tipleri: **embriyonal (en sık; <10 yaş)**, **alveoler (10-25 yaş)**, **pleomorfik (erişkin, nadir)**. Vajen/baş-boyun (burun, kulak)/safra kanalında üzüm salkımı polipoid kitle = **“sarcoma botryoides”** (**Nicholson'un kambiyum tabakası**)."),
                B("**Rabdomyom**: çizgili kasın benign tm; baş-boyun; **kardiyak rabdomyom → tuberoz skleroz**."),
                B("**Leiomyom**: düz kasın benign tm; **en sık uterus** (kadınlarda çok sık). **LEİOMYOSARKOM**: düz kasın malign tm → **yumuşak doku tümörü**.", y="24-25"),
            ]),
            C("Diğerleri", [
                B("**Sinovyal sarkom**: eklem çevresi malign tm; **bifazik** (iğsi + epitelyal hücre); **keratin + vimentin +**."),
                B("Periferik sinir kılıfı: benign **schwannom**, **nörofibrom**; malign **MPNST** (NF1)."),
                B("Damar: benign **hemanjiyom** (kapiller, kavernöz, **piyojenik granülom**), **lenfanjiyom**; malign **anjiyosarkom**, **Kaposi sarkomu**."),
                B("**Kaposi sarkomu (HHV-8)** — 4 tip: **klasik** (yaşlı), **lenfadenopatik / endemik Afrika**, **transplant ilişkili**, **AIDS ilişkili**."),
            ]),
        ],
    ],
    sorular=[
        Q("25-26", 62, "Çocukluk çağının en sık görülen malign yumuşak doku tümörü?",
          "Rabdomiyosarkom", "Liposarkom, anjiyosarkom, Kaposi, MFH değil"),
        Q("24-25", 85, "Hangisi yumuşak doku tümörüdür?",
          "Leiomyosarkoma", "Kondrosarkom (kıkırdak), RCC, malign melanom, seminom değil"),
        Q("22-23", 77, "Hangi tümör metastaz YAPMAZ?",
          "Desmoid tümör (derin fibromatozis)", "RMS, leiomyosarkom, MPNST, MFH metastaz yapar"),
    ],
))

# ---------------------------------------------------------------- 19
BOLUMLER.append(dict(
    no=19, key="lenf", baslik="Lenf Nodu Patolojisi",
    hoca="Doç. Dr. Selma Erdoğan Düzcü", tarih="14 ve 16 Ekim", saat="4 saat",
    kaynak="2025-26 ders notları (S. E. Düzcü) + Robbins Temel Patoloji",
    ozet=["5 yılda 10 soru! ★ EMPERİPOLEZİS / Rosai-Dorfman 3 kez · multipl miyelom 2 kez · ALCL = T hücreli 2 kez.",
          "Ayrıca: EMN ↔ Hodgkin ayırıcı tanısı · NLPHL = popcorn hücre, CD15−/CD30−."],
    slaytlar=[
        [
            C("Normal lenf nodu", [
                B("**Korteks**: B hücreleri → foliküller (germinal merkez) · **Parakorteks**: **T hücreleri** + **interdigitating dendritik hücreler** (T'ye antijen sunar; kemik iliği kökenli, Langerhans hücreleriyle ilişkili) → **hücresel immünitenin ana bölgesi**."),
                B("**Medulla**: **plazma hücreleri** (sekretuar bölge) · **Sinüsler**: fagositik **histiyositler**."),
            ]),
            C("Reaktif lenfadenitler", [
                B("**Akut nonspesifik**: lokal/sistemik enfeksiyon; ağrılı; büyük germinal merkez, mitoz; abse olabilir."),
                B("**Foliküler hiperplazi** (B uyarısı): folikül sayı/boyutu ↑, **tingible body makrofajlar → “yıldızlı gök”**, **germinal merkez polaritesi korunur**, mantle zon belirgin; **en önemli ayırıcı tanı: foliküler lenfoma**."),
                B("**Parakortikal (interfoliküler) hiperplazi** (T uyarısı): viral (**EBV**), aşı, ilaç (fenitoin). **Sinüs histiyositozu**: tümör drene eden lenf nodu. Diffüz patern: EMN ve viral lenfadenopatiler."),
                B("**ENFEKSİYÖZ MONONÜKLEOZ (EBV)**: parakortikal hiperplazi, **atipik lenfositler (Downey)**, **Reed-Sternberg benzeri hücreler** → **Hodgkin lenfoma ile ayırıcı tanı**; EBV **HL patogenezinde de rol oynar**.", y="23-24"),
            ]),
            C("★ Rosai-Dorfman ve diğer özel lenfadenitler", [
                B("**ROSAI-DORFMAN (yaygın/masif lenfadenopatili sinüs histiyositozu)**: genç, **boyunda masif ağrısız LAP**; sinüslerde çok sayıda büyük **histiyosit (S-100 +)**.", y="25-26"),
                B("Histiyosit sitoplazmasında **canlı lenfosit, plazma hücresi, nötrofil, eritrosit** “fagosite edilmemiş gibi” durur = **EMPERİPOLEZİS**.", y="22-23 24-25 25-26",
                  tuzak="Richter transformasyonu, RS hücresi, hematoksilen cisimciği, mantle zon değil"),
                B("**Kedi tırmığı** (Bartonella): **yıldızsı mikroabseli nekrotizan granülom** · **Castleman** (hiyalin-vasküler: atrofik germinal merkez + hiyalinize damar “lolipop”, mantle zonda “soğan zarı”; plazma hücreli: IL-6, HHV-8) · **dermatopatik lenfadenit** (Langerhans + melanin yüklü makrofaj) · sifiliz (plazma hücre, kapsülit) · **toksoplazma** (foliküler hiperplazi + epiteloid histiyosit kümeleri) · LGV (stellat abse)."),
            ]),
        ],
        [
            C("Lenfoid neoplazilere genel bakış", [
                B("Lenfoma: doku kitlesi/lenf nodu; lösemi: kemik iliği + kan. Lenfoid neoplazilerin **%80-85'i B hücre kökenli** (çoğu germinal/post-germinal merkez)."),
                B("Belirteçler: **CD45 (LCA)** tüm lökositler · **B: CD19, CD20**, CD79a · **T: CD3 (en güvenilir)**, CD2, CD5, CD7 · plazma hücresi: **CD38, CD138** · Hodgkin: **CD15, CD30**."),
                B("**B-ALL**: çocukluk çağının en sık kanseri; TdT +; t(12;21) ETV6-RUNX1 (iyi), **t(9;22) BCR-ABL** (kötü). **T-ALL**: adölesan erkek, **mediastinal kitle**."),
            ]),
            C("Periferik B hücreli neoplaziler (1)", [
                B("**KLL/SLL**: Batı'da en sık erişkin lösemisi; yaşlı; **CD5 + CD23 +**; küçük lenfositler + **proliferasyon merkezleri (psödofolikül)**, smudge hücre; **hipogamaglobulinemi**, otoimmün hemolitik anemi; BCL-2 ↑; **Richter transformasyonu** (agresif DLBCL'ye dönüşüm); medyan sağkalım 4-6 yıl."),
                B("**Foliküler lenfoma**: **t(14;18) IGH-BCL2** → BCL-2 ↑ (reaktif germinal merkezde BCL-2 −); nodüler patern; **sentrosit (çentikli) + sentroblast**; mitoz/apoptoz az; ağrısız LAP; DLBCL'ye dönüşebilir."),
                B("**DLBCL**: en sık NHL, agresif. **Burkitt**: **t(8;14) MYC**, endemik (çene, EBV) / sporadik (ileoçekal), Ki-67 ~%100, **“yıldızlı gök”**; **B hücreli**."),
            ]),
            C("Periferik B hücreli neoplaziler (2)", [
                B("**Mantle hücreli**: yaşlı erkek; **t(11;14) siklin D1**; CD5 + CD23 −; GİS'te lenfomatoid polipozis. **Marjinal zon**: **MALT** (mide – **H. pylori**, antibiyotikle regresyon; **Sjögren**, Hashimoto; lenfoepitelyal lezyon), splenik, nodal (monositoid B)."),
                B("**Lenfoplazmositik lenfoma (Waldenström)**: yaşlı; **IgM ↑ → hiperviskozite**; plazmasitoid lenfositler; **Russell (sitoplazma) ve Dutcher (nükleus) cisimcikleri (PAS +)**. **Hairy cell lösemi**: masif splenomegali, pansitopeni, **TRAP +**, BRAF V600E."),
                B("Çeldiricilerde hepsi **B hücreli**: mantle, foliküler, küçük hücreli (SLL), Burkitt, marjinal zon.", y="22-23 23-24"),
            ]),
        ],
        [
            C("Plazma hücre neoplazileri", [
                B("**MULTİPL MİYELOM**: **en sık malign plazma hücre diskrazisi**; **ileri yaş, erkek**; kemikte **multifokal litik (“zımba deliği”) lezyonlar** (vertebra, kafatası; RANKL ↑) → **patolojik kırık**, kemik ağrısı.", y="24-25 25-26"),
                B("Plazma hücreleri **CD38 +, CD138 +**; M-proteini (en sık IgG), idrarda **Bence Jones** (hafif zincir), **rulo formasyonu**; **CRAB**: hiperkalsemi, böbrek yetmezliği (miyelom böbreği), anemi, kemik lezyonu; **AL amiloidoz**; enfeksiyon yatkınlığı.", y="25-26",
                  tuzak="Mantle, ALCL, Hodgkin, mikozis fungoides, foliküler, hairy cell plazma hücre diskrazisi değil"),
                B("Soliter plazmositom; **MGUS** (en sık monoklonal gamopati; yılda ~%1 MM'ye ilerler)."),
            ]),
            C("T ve NK hücreli neoplaziler", [
                B("**ANAPLASTİK BÜYÜK HÜCRELİ LENFOMA (ALCL)**: **T hücre kökenli**, periferik T hücreli lenfoma grubunda; **CD30 (Ki-1) +**; **ALK + (t(2;5)) → iyi prognoz**, genç-erkek; **at nalı/böbrek şekilli nükleuslu** “hallmark” hücreler.", y="22-23 23-24"),
                B("**Periferik T hücreli lenfoma, NOS**: posttimik, yaşlı, agresif; RS benzeri hücreler görülebilir."),
                B("**Mikozis fungoides / Sézary**: **kutanöz CD4+ T helper** lenfoma; epidermiste **Pautrier mikroabseleri**; Sézary = **jeneralize eritrodermi + LAP + kanda atipik (serebriform) hücreler**."),
                B("**ATLL**: **HTLV-1**; deri lezyonu, LAP, **hiperkalsemi**. **NK/T hücreli lenfoma, nazal tip**: **EBV**, orta hat destrüksiyonu. **Enteropati ilişkili T lenfoma**: **gluten enteropatisi**. Hepatosplenik γδ T, pannikülit benzeri T, anjiyoimmünoblastik T, büyük granüler lenfositik lösemi."),
            ]),
            C("Hodgkin lenfoma (HL)", [
                B("Neoplastik hücre **Reed-Sternberg (RS)**: büyük, çift/çok lobüllü nükleus, **“baykuş gözü”** nükleoller; tümörün küçük kısmı, geri kalanı reaktif hücreler (lenfosit, eozinofil, plazma hücresi, histiyosit). Klasik HL: **CD15 +, CD30 +, CD45 −**; **EBV** ilişkisi; komşu lenf nodlarına yayılım; **Ann Arbor** evrelemesi."),
                B("Klasik alt tipler: **Nodüler sklerozan** (en sık; **kadın**, genç, mediasten; kollajen bantlar + **lakuner hücre**; prognoz iyi) · **Mikst selüler** (**erkek**, EBV +, **HIV** ilişkili; çok sayıda RS + eozinofil, plazma hücresi) · **Lenfositten zengin** · **Lenfositten fakir** (**en nadir, en kötü prognoz**)."),
                B("**NODÜLER LENFOSİT PREDOMİNANT HL**: **“POPCORN” (L&H) hücreleri**; **CD20 +, CD15 −, CD30 −**; EBV −; **en iyi prognozlu HL**.", y="21-22"),
                B("RS varyantları: lakuner (NS), popcorn (NLPHL), mumyalanmış (dejeneratif). **Ayırıcı tanı: enfeksiyöz mononükleoz** (RS benzeri hücre).", y="23-24"),
            ]),
        ],
    ],
    sorular=[
        Q("25-26", 74, "Lenf nodunda sinüslerde çok sayıda histiyosit ve emperipolezis ile karakterize lenfadenit?",
          "Rosai-Dorfman hastalığı", "Castleman, sifiliz, kedi tırmığı, EMN değil"),
        Q("25-26", 75, "İleri yaş, kemikte litik lezyon, CD38 + malign plazma hücre diskrazisi?",
          "Multipl miyelom", "Mantle hücreli, ALCL, Hodgkin, mikozis fungoides değil"),
        Q("24-25", 79, "Sinüs histiyositozisinde histiyosit sitoplazmasında hücrelerin fagosite edilmemiş gibi bulunması?",
          "Emperipolezis", "Richter transformasyonu, RS hücresi, hematoksilen cisimciği, mantle zon değil"),
        Q("24-25", 80, "Erkek, ileri yaş; multifokal litik kemik lezyonu, patolojik kırık; en sık malign plazma hücre diskrazisi?",
          "Multipl miyelom", "Foliküler, lenfoplazmositik lenfoma, hairy cell, Hodgkin değil"),
        Q("23-24", 71, "Hodgkin ile ayırıcı tanısı yapılması gereken ve HL patogenezinde rolü olan reaktif lenfadenit?",
          "Enfeksiyöz mononükleozis", "Sifiliz, Castleman, dermatopatik, LGV değil"),
        Q("23-24", 72, "T hücre kökenli malign lenfoma?",
          "Anaplastik büyük hücreli lenfoma", "Mantle, foliküler, küçük hücreli, Burkitt = B"),
        Q("22-23", 71, "Periferik T hücreli lenfoma grubunda yer alan?",
          "Anaplastik büyük hücreli lenfoma", "Foliküler, mantle, marjinal zon, Burkitt = B"),
        Q("22-23", 72, "Sinüs histiyositozisinde histiyosit sitoplazmasında canlı hücreler?",
          "Emperipolezis", "Richter sendromu, RS hücresi, granülom, atipik hücre değil"),
        Q("21-22", None, "Popcorn görünümü, CD15 −, CD30 − ?",
          "Nodüler lenfosit predominant Hodgkin lenfoma", "Öğrenci hatırlamasından derlenmiş soru"),
        Q("21-22", None, "“Çit tarzı görünüm” (lenf nodu patolojisi)",
          "Hatırlanan cevap: Castleman (?)", "Kesin değil — öğrenci notu"),
    ],
))

# ---------------------------------------------------------------- 20
BOLUMLER.append(dict(
    no=20, key="dalak", baslik="Dalak Patolojisi",
    hoca="Dr. Öğr. Üyesi Songül Peltek Özer", tarih="19 Ekim", saat="1 saat",
    kaynak="2025-26 ders slaytı: Dalak patolojisi (S. P. Özer)",
    ozet=["Patolojiden 1 soru: splenik ven trombozu → konjestif splenomegali (23-24).",
          "İç Hastalıkları her yıl splenomegali soruyor: aplastik anemide splenomegali YOK · masif splenomegali nedenleri."],
    slaytlar=[
        [
            C("Yapı ve fonksiyon", [
                B("**Vücudun en büyük sekonder lenfoid organı**; korteks-medulla ayrımı yok; **beyaz pulpa** (**PALS = T hücreleri**, germinal merkez ve **marjinal zon = B hücreleri**) + **kırmızı pulpa** (kordonlar, sinüzoidler)."),
                B("Fonksiyon: **yaşlı/hasarlı kan hücrelerinin ve yabancı maddelerin splenik makrofajlarca fagositozu** (kanın filtrasyonu); **antikor üretimi** (ITP'de yanlış antikor); sekonder hematopoez; kemik iliği hücrelerinin sekestrasyonu."),
                B("**Hipersplenizm**: kırmızı pulpaya aşırı kan göçü → aşırı yıkım → **pansitopeni** (halsizlik, enfeksiyon yatkınlığı)."),
                B("**Herediter sferositoz** (membran proteini defekti) ve **ITP** → tedavide **splenektomi**."),
            ]),
            C("Rüptür, splenektomi, asplenik durum", [
                B("**Splenik rüptür**: en sık **künt travma**; **spontan rüptür**: **EBV (EMN)**, sıtma, tifo, lenfoid tümörler → intraperitoneal kanama."),
                B("Splenektomi en sık **travmatik rüptür** nedeniyle; sonra ITP ve hipersplenizm."),
                B("**Otosplenektomi**: **orak hücreli anemi** — önce hemoliz + splenomegali, sonra orak hücreler dalak damarlarını tıkar → infarkt/fibrozis."),
                B("Asplenide **kapsüllü bakteri** enfeksiyonları (pnömokok, H. influenzae, meningokok) → **aşılama**. Konjenital: **hipoplazi**, **aksesuar dalak**."),
            ]),
            C("Dalak tümörleri", [
                B("Çoğu **sekonder** tutulum (lenfoma/lösemi); primer lenfoma olarak **splenik marjinal zon lenfoması**."),
                B("**En sık primer benign: hemanjiyom** (lenfanjiyom) · **en sık primer malign: anjiyosarkom**."),
                B("İnfarkt: dalak **soluk (anemik) infarkt** (uç arter)."),
            ]),
        ],
        [
            C("Splenomegali nedenleri (1)", [
                B("1) **Enfeksiyonlar**: **EBV – enfeksiyöz mononükleoz** (LAP, splenomegali, Downey hücreleri, Monospot; komplikasyon: hepatit, menenjoensefalit, pnömoni, **minör travmayla rüptür**), TB, sifiliz, **bruselloz**, **tifo** (S. typhi; Peyer plakları, ülser-perforasyon, lökopeni), **sıtma**, **kala-azar**, toksoplazma.",
                  g="İÇ HAST. 25-26"),
                B("2) **Portal HT ilişkili KONJESTİF splenomegali**: **karaciğer sirozu**, **kalp yetmezliği**, **portal veya SPLENİK VEN TROMBOZU**.", y="23-24",
                  tuzak="TB, ekinokok, Hodgkin, amiloidoz konjestif splenomegali yapmaz (çeldirici)"),
            ]),
            C("Splenomegali nedenleri (2) ve masif splenomegali", [
                B("3) **Depo hastalıkları**: **Gaucher** (glukoserebrozidaz ↓, glukoserebrozid birikimi; tip 1 iskelet + dalak; **masif**), **Niemann-Pick** (sfingomiyelinaz ↓; nörolojik), mukopolisakkaridoz (dermatan/heparan sülfat)."),
                B("4) **Hematolenfoid**: Hodgkin ve **non-Hodgkin** (beyaz pulpa), lenfoplazmositik lenfoma, **multipl miyelom**, **myeloproliferatif** (**KML**, polisitemia vera, primer miyelofibroz), hairy cell; **hemolitik anemiler**. Romatolojik hastalıklar."),
                B("**MASİF splenomegali**: **KML**, primer miyelofibroz, hairy cell lösemi, **Gaucher**, sıtma, kala-azar; ders slaytı: **alkolik siroz, şistozomiyazis, hemokromatoz**, herediter sferositoz.",
                  g="İÇ HAST. 22-23 · 23-24 · 24-25"),
                B("**Aplastik anemi** ve **demir eksikliği anemisi** splenomegali (masif) yapmaz — İç Hastalıklarında defalarca soruldu.",
                  g="İÇ HAST. 22-23 · 23-24 · 24-25"),
            ]),
        ],
    ],
    sorular=[
        Q("23-24", 70, "Portal hipertansiyon ilişkili konjesyon varlığıyla karakterize splenomegali?",
          "Splenik ven trombozu", "Tüberküloz, ekinokok, Hodgkin lenfoma, amiloidoz değil"),
        Q("İÇ HAST.", None, "İlişkili İç Hastalıkları çıkmışları (22-23 S44 · 23-24 S42 · 24-25 S8 · 25-26 S47)",
          "Aplastik anemide splenomegali görülmez · demir eksikliği anemisi masif splenomegali yapmaz · EMN'de splenomegali + servikal LAP",
          "Patoloji sorusu değil; konu tekrarı için eklendi", ref=True),
    ],
))

# ---------------------------------------------------------------- 21
BOLUMLER.append(dict(
    no=21, key="immun", baslik="İmmün Sistem Patolojisi",
    hoca="Dr. Öğr. Üyesi Songül Peltek Özer", tarih="20-22 Ekim", saat="5 saat",
    kaynak="2025-26 ders slaytları: İmmün sistem 1-3 (S. P. Özer) + ders notları",
    ozet=["EN ÇOK SORU ÇIKAN BAŞLIK: 5 yılda 15 soru (2025-26'da tek başına 4 soru).",
          "Hipersensitivite tipleri (4 kez) · tolerans genleri (FOXP3, AIRE, Fas, CD28) · immün yetmezlikler (CD40, SCID, Bruton, DiGeorge)."],
    slaytlar=[
        [
            C("Doğal ↔ Edinsel immünite", [
                B("**Doğal**: nonspesifik, hızlı, **hafıza yok**, çeşitlilik sınırlı. Bileşenler: **epitel bariyerleri**, **nötrofil, makrofaj**, **NK hücreleri**, dendritik hücre, mast hücresi, eozinofil; humoral: **kompleman**, interferon, lizozim, IL-1.", y="22-23",
                  tuzak="CD8 CTL, B lenfosit, CD4 T helper → edinsel immünite"),
                B("Reseptörler: **TLR** (membran/endozom; asıl bariyer), **NLR → inflammazom** (sitozol), **RIG-like** (sitozol, viral nükleik asit), **C-tipi lektin** (makrofaj/DC; fungal glikan), GPCR (N-formil metiyonil peptidler)."),
                B("Doğal immünitenin iki sonucu: **inflamasyon** ve **antiviral savunma**."),
                B("**Edinsel**: **spesifik**, çeşitlilik çok fazla, **immünolojik hafıza**, self'e tolerans; **humoral** (antikor: nötralizasyon, opsonizasyon, kompleman) + **hücresel** (hücre içi patojenler). **Klonal seleksiyon**; reseptör çeşitliliği **RAG1/RAG2** (yokluğunda lenfosit matüre olamaz)."),
                B("Santral lenfoid organ: **kemik iliği (B)**, **timus (T)**; periferik: lenf nodu, dalak, tonsil, MALT."),
            ]),
            C("Lenfositler ve APC", [
                B("**Th1**: **IL-2, IFN-γ** → makrofaj aktivasyonu, gecikmiş tip aşırı duyarlılık · **Th2**: **IL-4** (IgE), **IL-5 (eozinofil aktivasyonu)**, IL-13 → parazit, alerji."),
                B("**Th17**: **IL-17, IL-22** → **nötrofil ve monosit toplanması**; ekstrasellüler bakteri-mantar savunması ve **otoimmün hastalıklar** → nötrofilden zengin otoimmün inflamasyon.", y="24-25"),
                B("**CD8+ sitotoksik T**: **MHC I** ile sunulan antijeni tanır → **virüsle enfekte ve tümör hücrelerini doğrudan öldürür** (perforin-granzim, Fas-FasL).", g="PEDİATRİ 25-26"),
                B("**B hücre**: kemik iliği; kan lenfositlerinin %10-20'si; yüzeyde **IgM ve IgD** (BCR); **CD21 = EBV reseptörü**; **CD40** (Th'deki CD40L ile → sınıf değişimi)."),
                B("**NK**: antijen reseptörü yok, önceden duyarlılaşma gerekmez; **CD16** (IgG Fc reseptörü → ADCC), **CD56**; aktive edici **NKG2D**; **MHC I taşıyan sağlıklı hücreyi öldürmez**."),
                B("APC: **dendritik hücre** (deride **Langerhans**; germinal merkezde **foliküler dendritik hücre**), makrofaj, B hücre."),
            ]),
        ],
        [
            C("MHC (HLA) ve sitokinler", [
                B("**MHC sınıf I (HLA-A, -B, -C)**: **tüm çekirdekli hücreler + trombositler** → CD8. **MHC sınıf II (HLA-DP, -DQ, -DR)**: APC (makrofaj, B, DC) → CD4."),
                B("HLA–hastalık: **HLA-B27 → ankilozan spondilit** (reaktif artrit, akut anterior üveit; OR 100-200), **HLA-DR4 → RA**, DR3/DR4 → tip 1 DM, DQ2/DQ8 → çölyak, **HLA-A3 → hemokromatoz**, **HLA-BW47 → 21-hidroksilaz eksikliği**."),
                B("Sitokinler: IL-1, TNF, IL-6 (akut faz), **IL-8 (kemotaksis)**, IL-2 (T proliferasyonu), IFN-γ, GM-CSF/G-CSF (hematopoez), **TGF-β ve IL-10 (immünsüpresif)**; RA'da **anti-TNF** dramatik yanıt."),
            ]),
            C("Aşırı duyarlılık (hipersensitivite) reaksiyonları", [
                B("**TİP I (anafilaktik/ani)**: **Th2 + IgE** → mast hücresi degranülasyonu; primer mediatör: **histamin**, proteaz, heparin; sekonder: **LTC₄/D₄**, PGD₂, PAF, sitokinler; erken faz (dakikalar) + geç faz (eozinofil). **Alerjik rinit (mevsimsel göz kaşıntısı-burun akıntısı)**, anafilaksi, atopik astım, besin alerjisi. **Atopi**: lokal tip I'e yatkınlık.", y="25-26"),
                B("**TİP II (antikor aracılı)**: **IgG/IgM** hücre/doku antijenine → opsonizasyon-fagositoz, kompleman lizisi, fonksiyon bozukluğu → **otoimmün hemolitik anemi**, transfüzyon reaksiyonu, Rh uyuşmazlığı, ITP, **Goodpasture**, akut romatizmal ateş, pemfigus, **Graves** (TSH-R uyarıcı Ab), **myastenia gravis** (ACh-R).", y="24-25"),
                B("**TİP III (immün kompleks)**: Ag-Ab kompleksleri **damar duvarı**, glomerül, eklemde birikir → kompleman → nötrofil → **akut nekrotizan VASKÜLİT (fibrinoid nekroz)**, GN, artrit. **SLE**, poststreptokokal GN, **PAN** (HBsAg-Ab), **serum hastalığı** (sistemik), **Arthus** (lokal).", y="23-24 21-22"),
                B("**TİP IV (T hücre aracılı)**: CD4 Th1/Th17 (sitokin, makrofaj aktivasyonu) — **PPD/tüberkülin**, **granülom (TB)**, **kontakt dermatit**, MS, RA; CD8 sitotoksisite — **transplant reddi**, viral hepatit, **tip 1 DM**."),
                B("Transplant: **hiperakut** (önceden var olan Ab), akut hücresel/antikor aracılı (vasküler), kronik (transplant arteriopatisi); HLA farklılığı; GVHD."),
            ]),
        ],
        [
            C("Self tolerans", [
                B("**SANTRAL tolerans**: timus/kemik iliğinde self-reaktif lenfositlerin **delesyonu** veya reseptör düzenlenmesi; **AIRE** timusta self (periferik doku) antijenlerin ekspresyonunu sağlar → mutasyonunda **otoimmün poliendokrinopati**.", y="22-23",
                  tuzak="IPEX (FOXP3), PD-1, CTLA-4, FAS → PERİFERİK tolerans"),
                B("**Periferik tolerans — anerji**: kostimülasyon (**B7–CD28**) yokluğu veya inhibitör **CTLA-4 / PD-1** bağlanması; **CTLA-4, B7'ye CD28'den daha yüksek afinite** gösterir."),
                B("**Regülatuvar T (Treg)**: **CD4+ CD25+ (IL-2Rα) FOXP3+** T helper alt grubu; **IL-10, TGF-β**, CTLA-4 ile baskılar; **FOXP3 mutasyonu → IPEX** (immün disregülasyon, poliendokrinopati, enteropati, X'e bağlı); fetal toleransta önemli.", y="25-26"),
                B("**Delesyon (apoptoz)**: otoreaktif lenfositler **Fas–FasL** veya BIM ile ölür → **Fas mutasyonunda otoreaktif lenfositler apoptoza uğratılamaz** → otoimmünite, **ALPS**.", y="24-25"),
                B("**Antijen sekestrasyonu**: testis, göz, beyin (immün ayrıcalıklı)."),
            ]),
            C("Otoimmünite mekanizmaları", [
                B("**Genetik yatkınlık**: HLA; **PTPN22** (RA, tip 1 DM), **NOD2** (Crohn), IL2RA, CTLA4, IL23R."),
                B("**Enfeksiyonların rolü**: APC'de **kostimülatör (B7) ekspresyonu ↑** → self-reaktif T hücrede **CD28** aracılı aktivasyon → toleransın kırılması.", y="23-24",
                  tuzak="CTLA-4 (inhibitör), CD3, AIRE, FOXP3 değil — cevap CD28"),
                B("**Moleküler mimikri** (akut romatizmal ateş), doku hasarıyla gizli antijenlerin açığa çıkması/değişmesi."),
                B("Özellikler: kronik ve **ilerleyici** (yavaşlatılır, yok edilemez); **kadınlarda daha sık**; organ spesifik (tip 1 DM, MS, Hashimoto, Graves, myastenia) veya sistemik (SLE, RA, SSc, Sjögren)."),
            ]),
        ],
        [
            C("Sistemik otoimmün hastalıklar (1)", [
                B("**SLE**: kadın 30-40 yaş (K/E 9/1); **TİP III** (+ tip II); **ANA** (%95-100, spesifik değil), **anti-dsDNA ve anti-Sm (SLE'ye spesifik)**, antifosfolipid Ab (tromboz; **sifiliz testinde yalancı +**); erken kompleman (C1q, C2, C4) eksikliği; LE hücresi; **akut nekrotizan vaskülit**; lupus nefriti (**sınıf IV diffüz proliferatif — en sık ve en ağır, “wire loop”**), **malar döküntü**, **noneroziv artrit**, serözit, **Libman-Sacks** endokarditi.", y="22-23 23-24"),
                B("**İlaca bağlı lupus**: hidralazin, prokainamid, izoniazid, D-penisilamin, anti-TNF; **anti-histon Ab**."),
                B("**Romatoid artrit**: kadın 30-40; **küçük eklemler (PİF, MKF)**; **pannus** → erozyon → ankiloz; Th1 (IFN-γ), Th17 (IL-17), **TNF** (anti-TNF tedavi); **anti-CCP (sitrüllinlenmiş peptid) — RA'ya spesifik**; **romatoid faktör = IgG'nin Fc kısmına karşı antikor** (%80, spesifik değil).", y="22-23"),
            ]),
            C("Sistemik otoimmün hastalıklar (2)", [
                B("**Sjögren**: kuru göz + kuru ağız; lenfosit infiltrasyonu; **anti-SS-A (Ro), anti-SS-B (La)**; RF %75; **marjinal zon lenfoma riski ×40**."),
                B("**Sistemik skleroz**: fibrozis; **anti-DNA topoizomeraz I (Scl-70) → diffüz SSc'ye tanı koydurucu**; **antisentromer → sınırlı tip/CREST**; Raynaud %70.", y="22-23"),
                B("**MİKS BAĞ DOKUSU HASTALIĞI**: SLE + polimiyozit + RA + SSc özellikleri; **anti-U1 RNP**; orta renal tutulum; **kortikosteroide yanıtı ÇOK İYİ**.", y="22-23",
                  tuzak="“MCTD diğer otoimmün hastalıklara göre tedaviye daha dirençlidir” → YANLIŞ"),
                B("Miyopatiler: **dermatomiyozit** (perimisyal; heliotrop, Gottron; anti-Mi-2; malignite) · **polimiyozit** (CD8, endomisyal) · inklüzyon cisimcikli (distal, asimetrik) · anti-Jo-1 (interstisyel akciğer). **IgG4 ilişkili hastalık**: storiform fibrozis, obliteratif flebit."),
            ]),
        ],
        [
            C("Doğal immünite yetmezlikleri", [
                B("Lökosit: **LAD-1** (CD18 β2-integrin), **LAD-2** (selektin ligandı – fukozil transferaz), **Chediak-Higashi** (lizozomal trafik), **kronik granülomatöz hastalık** (fagosit oksidaz – oksidatif patlama ↓), MPO eksikliği."),
                B("Kompleman: **C1q, C2, C4 eksikliği → SLE benzeri** · **C3 → ağır piyojenik enfeksiyon** · **C5-C9 → bakteriyel (Neisseria)** · **C1 inhibitör → herediter anjiyoödem** · GPI-bağlı regülatörler (CD55, CD59) → PNH (ders slaytında “HÜS” geçiyor)."),
                B("**TLR3 defekti → rekürren HSV ensefaliti** · **MyD88 defekti → destrüktif bakteriyel pnömoni**."),
            ]),
            C("Edinsel immünite yetmezlikleri (1) — matürasyon defektleri", [
                B("**Lenfosit MATÜRASYON defektleri** (Robbins): **SCID** (T ± B; X'e bağlı IL-2Rγ, OR **ADA**, RAG) · **X'e bağlı agamaglobulinemi (Bruton)** · **DiGeorge**.", y="25-26 22-23",
                  tuzak="X'e bağlı lenfoproliferatif sendrom (SAP) kitapta aktivasyon defekti olarak geçer"),
                B("**SCID** = T lenfosit diferansiasyon yolunda mutasyon/eksiklik; hem hücresel hem humoral.", y="22-23"),
                B("**Bruton**: **BTK** (Xq21.22) → pre-B → B matürasyonu durur; erkek; **6. aydan sonra** rekürren bakteriyel enfeksiyon, enterovirüs, **Giardia** (IgA yok); B hücre çok az; %35 otoimmünite; IVIG."),
                B("**DiGeorge**: **22q11 delesyonu**; 3.-4. faringeal cep → **timus hipoplazisi (T eksikliği)** + **paratiroid hipoplazisi (hipokalsemi, tetani)** + kalp/yüz anomalileri."),
            ]),
            C("Edinsel immünite yetmezlikleri (2) — aktivasyon/fonksiyon defektleri", [
                B("**HİPER-IgM SENDROMU**: **CD40L (X'e bağlı) veya CD40** mutasyonu → **sınıf değişimi yok** → **IgM ↑**, IgG/IgA/IgE ↓; Pneumocystis.", y="23-24",
                  tuzak="BTK (Bruton), 22q11 (DiGeorge), ADA (SCID), MHC II defekti değil"),
                B("**CVID**: **B hücre sayısı normal** ama plazma hücresine farklılaşamaz → hipogamaglobulinemi; otoimmünite %20; **mide ca ×50**. **İzole IgA eksikliği**: en sık. **XLP (SAP)**: EBV'ye fatal yanıt, lenfoma. **Wiskott-Aldrich**: trombositopeni + egzama + enfeksiyon."),
            ]),
            C("AIDS", [
                B("**HIV**: **CD4** + koreseptör **CCR5** (erken, makrofaj-tropik) / **CXCR4** (geç, T-tropik); **CD4+ T kaybı** → hücresel immünite çöker; AIDS: **CD4 <200/mm³** veya AIDS tanımlayıcı hastalık."),
                B("**Fırsatçı enfeksiyonlar**: **Pneumocystis jirovecii** (en sık), **Candida**, **CMV** (retinit, kolit), **Toxoplasma gondii** (beyin absesi), Cryptococcus, MAC, TB, HSV, JC virüs.", y="25-26",
                  tuzak="S. pneumoniae klasik fırsatçı etken DEĞİL"),
                B("AIDS ilişkili tümörler: **Kaposi sarkomu (HHV-8)**, **B hücreli lenfomalar** (DLBCL, Burkitt, primer SSS — EBV), serviks/anal SCC (HPV)."),
            ]),
        ],
    ],
    sorular=[
        Q("25-26", 63, "42 yaş erkek; yılın belli dönemlerinde artan göz kaşıntısı, gözyaşı, burun akıntısı — mekanizma?",
          "Tip I hipersensitivite", "Tip II, III, IV, otoimmünite değil"),
        Q("25-26", 64, "AIDS hastalarında fırsatçı enfeksiyon etkenlerinden biri OLMAYAN?",
          "Streptococcus pneumoniae", "P. jirovecii, C. albicans, CMV, T. gondii fırsatçı"),
        Q("25-26", 65, "Foxp3 geni hangi hücrelerin regülasyonunda önemli rol oynar?",
          "T helper (CD4+ CD25+ regülatuvar T)", "Eozinofil, makrofaj, mast hücresi, nötrofil değil"),
        Q("25-26", 66, "SCID, Bruton, DiGeorge, X'e bağlı lenfoproliferatif sendrom — hangileri lenfosit matürasyon defektidir?",
          "Kitaba göre I, II, III — şıklarda yok; en uygun: d) I, II, III ve IV",
          "⚠ Cevap anahtarı yok: Robbins'te XLP “aktivasyon defekti”; sınavda beklenen muhtemelen d"),
        Q("24-25", 88, "Bir otoimmün hastalıkta inflamasyon nötrofilden zenginse rol alan lenfosit?",
          "T-helper-17", "Th1, Th2, NK, CTL değil"),
        Q("24-25", 89, "Antikora bağımlı eritrosit yıkımı → hemolitik anemi; hipersensitivite tipi?",
          "Tip II", None),
        Q("24-25", 90, "Fas mutasyonu olan kişide otoimmün hastalık gelişmesinin en olası mekanizması?",
          "Otoreaktif lenfositler apoptoza uğratılamaz", "Sinyal iletimi, süpresör gen, antikor sentezi, CTLA-4 aktivasyonu değil"),
        Q("23-24", 75, "Enfeksiyonla ekspresyonu artarsa otoimmüniteye yatkınlık oluşturan hücre yüzey molekülü (reseptörü)?",
          "CD28", "CTLA4, CD3, AIRE, Foxp3 değil"),
        Q("23-24", 78, "Yaygın vaskülitlerle seyreden tablo — hipersensitivite tipi?",
          "Tip III", None),
        Q("23-24", 79, "IgM aşırı yüksek + immün yetmezlik; lenfosit gelişim bozukluğu?",
          "CD40 mutasyonu (hiper-IgM sendromu)", "Btk, 22q11 delesyonu, ADA, MHC II ekspresyon bozukluğu değil"),
        Q("22-23", 79, "Doğal immünitenin komponenti olan hücre?",
          "NK hücreleri", "CD8 CTL, B lenfosit, CD4 Th = edinsel (dendritik hücre derste APC olarak edinsel başlıkta)"),
        Q("22-23", 80, "Santral immün toleransta görev alan?",
          "AIRE", "IPEX, PD-1, CTLA-4, FAS = periferik tolerans"),
        Q("22-23", 81, "Yanlış olan?",
          "“Miks konnektif doku hastalığı diğer otoimmün hastalıklara göre tedaviye daha dirençlidir”",
          "Doğrular: SLE tip III · RF anti-IgG · Scl-70 SSc tanı koydurucu · RA'da anti-sitrüllinlenmiş peptid"),
        Q("22-23", 82, "T lenfosit diferansiasyon yolundaki mutasyon/eksiklikle oluşan immün yetmezlik?",
          "Şiddetli kombine immün yetmezlik (SCID)", "Hiper-IgM, CVID, Bruton, Chediak-Higashi değil"),
        Q("21-22", None, "Tip 3 hipersensitivite örneği?",
          "Vaskülit / SLE", "Öğrenci hatırlamasından derlenmiş soru"),
    ],
))

# ---------------------------------------------------------------- 22
BOLUMLER.append(dict(
    no=22, key="enf", baslik="İnfeksiyon Hastalıklarının Patolojisi (Bakteri, Virüs, Mantar, Parazit)",
    hoca="Dr. Öğr. Üyesi Songül Peltek Özer", tarih="23 ve 26 Ekim", saat="4 saat",
    kaynak="Robbins Temel Patoloji (bu derslerin slaytı klasörde yok)",
    ozet=["Her yıl 1 soru: iltihap paterni (T. pallidum → mononükleer), Enterobius → apandisit, tinea versikolor = mantar.",
          "AIDS fırsatçıları (25-26) ve onkojenik virüsler (HBV) diğer bölümlerde."],
    slaytlar=[
        [
            C("Genel prensipler", [
                B("Giriş yolları: deri, solunum, **GİS (fekal-oral)**, ürogenital (cinsel), **vertikal** (plasenta — TORCH, doğum kanalı, süt)."),
                B("Yayılım: lokal invazyon, lenfatik, **hematojen** (bakteriyemi, viremi, septik emboli), sinir yolu (kuduz, HSV, VZV)."),
                B("Hasar mekanizmaları: direkt hücre ölümü (sitopatik virüs), **toksinler** — **endotoksin** (gram − LPS → septik şok, DIC), **ekzotoksin** (difteri, kolera, tetanoz, botulinum), **süperantijen** (TSST-1 → toksik şok); enzimler; **konak immün yanıtı** (TB granülomu, HBV hepatiti)."),
                B("İmmün kaçış: antijenik varyasyon, **kapsül** (pnömokok, meningokok, H. influenzae), latent kalış (herpes), immünsüpresyon (HIV)."),
                B("Doku boyaları: **Gram**, **Ziehl-Neelsen** (aside dirençli), **gümüş** (GMS — mantar; Warthin-Starry — spiroket, Bartonella), **PAS** (mantar, Whipple), **mukikarmin** (Cryptococcus), **Giemsa** (H. pylori, Leishmania, Plasmodium)."),
            ]),
            C("Enfeksiyona inflamatuvar yanıt paternleri", [
                B("1) **Süpüratif (polimorfonükleer)**: **piyojenik ekstrasellüler bakteriler** (S. aureus, S. pyogenes, **S. pneumoniae**, gram − basiller) → nötrofil, pü, abse; **pnömokok → LOBER pnömoni** (konjesyon → kırmızı → gri hepatizasyon → rezolüsyon).", y="23-24 21-22"),
                B("2) **Mononükleer ve granülomatöz**: virüs, **hücre içi bakteri**, **spiroket**, parazit; **Treponema pallidum (sifiliz) → plazma hücreden zengin mononükleer inflamasyon** + obliteratif endarterit; granülomatöz: **M. tuberculosis**, M. leprae, mantarlar.", y="23-24",
                  tuzak="S. aureus, grup A streptokok, C. perfringens, C. jejuni → süpüratif/nekrotizan"),
                B("3) **Sitopatik-sitoproliferatif** (virüs): inklüzyonlar — **CMV “baykuş gözü”**, **HSV Cowdry A**, **kuduz Negri cisimciği**; dev hücreler (HSV, VZV, kızamık — Warthin-Finkeldey); epitel proliferasyonu (**HPV koilosit**, molluskum)."),
                B("4) **Doku nekrozu**: **C. perfringens** (gazlı gangren, α-toksin), fulminan HBV, **E. histolytica**, HSV ensefaliti. 5) **Kronik inflamasyon + skar**: HBV/HCV → siroz, şistozomiyaz → portal fibrozis, TB, filariazis."),
            ]),
        ],
        [
            C("Bakteriyel enfeksiyonlar", [
                B("**S. aureus**: **fronkül, karbonkül, impetigo**, abse, osteomiyelit, endokardit, haşlanmış deri sendromu, **toksik şok (TSST-1)**."),
                B("**S. pyogenes**: farenjit, **kızıl** (zımpara kağıdı döküntü, çilek dil), **erizipel**, impetigo, nekrotizan fasiit; sekeller: **akut romatizmal ateş, poststreptokokal GN**. **S. pneumoniae**: lober pnömoni, otitis, menenjit (asplenik hasta).", y="22-23"),
                B("**Clostridium**: **perfringens** (gazlı gangren), **tetani** (tetanospazmin), **botulinum** (ACh salınımı ↓), **difficile → psödomembranöz kolit** (antibiyotik ilişkili; bakteriyel).", y="22-23"),
                B("**Difteri**: farinkste **gri psödomembran**, ekzotoksin → miyokardit, nöropati. **Boğmaca**: trakeal sitotoksin (silyalı hücre ölümü), pertussis toksini → **lenfositoz**.", g="PEDİATRİ 23-24"),
                B("**Tüberküloz**: primer **Ghon odağı** + hiler LN = **Ghon kompleksi** (kalsifiye → Ranke); sekonder **apikal**, kavitasyon; **kazeifiye granülom** (Th1, Langhans); **miliyer TB**, **Pott**; EZN; PPD (tip IV). Lepra: tüberküloid (granülom) vs lepromatöz (köpüklü makrofaj)."),
                B("**Sifiliz**: primer **ağrısız sert şankr**; sekonder (avuç içi-ayak tabanı döküntü, condyloma lata); tersiyer **gom**, **aortit (vasa vasorum endarteriti)**, nörosifiliz; konjenital. **Tifo** (Peyer plakları), **Bartonella** (kedi tırmığı), **Actinomyces** (sülfür granülleri), Whipple (PAS + makrofaj)."),
            ]),
            C("Viral enfeksiyonlar", [
                B("Akut: **kızamık** (Koplik, Warthin-Finkeldey), **kabakulak** (parotit, orşit, pankreatit), polio. Latent: **HSV** (ganglion; Tzanck — çok çekirdekli dev hücre), **VZV** (suçiçeği → zona), **CMV** (sitomegali, baykuş gözü; konjenital, transplant, AIDS)."),
                B("**Kronik hepatit**: **HBV, HCV** (± HDV) → siroz, HCC; **HAV ve HEV kronikleşmez**.", y="21-22"),
                B("**Transforme edici (onkojenik) virüsler**: **HBV**, HCV, **EBV**, **HPV**, **HHV-8**, **HTLV-1**, Merkel poliomavirüs.", y="22-23",
                  tuzak="VZV, CMV, HSV, poliovirüs değil"),
                B("**EBV — enfeksiyöz mononükleoz**: ateş, farenjit, LAP, splenomegali, hepatit; **atipik lenfositler (CD8+ T)**; heterofil Ab (Monospot); splenik rüptür."),
                B("**COVID-19 (SARS-CoV-2)**: **ACE2** (tip II pnömosit, endotel); **diffüz alveoler hasar** — **eksüdatif faz** (ödem, **hiyalin membran**, fibrin) → **organizasyon/proliferatif faz** (tip II pnömosit hiperplazisi) → **fibrotik faz**; mikrotrombüs (endotelit), sitokin fırtınası (IL-6).", y="21-22"),
            ]),
        ],
        [
            C("Mantar enfeksiyonları", [
                B("**Yüzeyel**: dermatofitler (Trichophyton, Microsporum, Epidermophyton) → **tinea** capitis/corporis/cruris/pedis/unguium; **TİNEA (PİTİRİYAZİS) VERSİKOLOR → Malassezia furfur** (“spagetti-köfte”) → **bakteriyel DEĞİL, mantar**.", y="22-23",
                  tuzak="İmpetigo, erizipel, kızıl, psödomembranöz enterokolit → bakteriyel"),
                B("**Candida** (en sık; maya + psödohif; oral, vajinal, özefagus; nötropenide sistemik) · **Aspergillus** (**45° dallanan septalı** hif; anjioinvazif; aspergillom; ABPA)."),
                B("**Mucor/Rhizopus (zigomikoz)**: **90° dallanan geniş septasız** hif; **diyabetik ketoasidozda rinoserebral**, anjioinvazif — diyabette mortal seyir.", g="ENFEKSİYON 22-23 · 24-25"),
                B("**Cryptococcus** (kapsül — mukikarmin, Hint mürekkebi; AIDS'te **menenjit**) · **Histoplasma** (makrofaj içinde küçük mayalar, granülom) · **Pneumocystis jirovecii** (AIDS'te en sık fırsatçı; **köpüklü intraalveoler eksüda**; GMS)."),
            ]),
            C("Paraziter enfeksiyonlar", [
                B("**ENTEROBIUS VERMICULARIS (oksiyür)**: en sık helmint (çocuk); gece perianal kaşıntı, **selofan bant testi**; **apendiks lümenine yerleşip AKUT APANDİSİT etiyolojisinde rol** oynayabilir.", y="24-25",
                  tuzak="HSV, HPV, E. histolytica, molluskum kontagiozum değil"),
                B("**Entamoeba histolytica**: kolonda **şişe şekilli ülserler**, eritrofagositoz; **amip karaciğer absesi** (“ançüez ezmesi”). **Giardia**: ince barsak, malabsorpsiyon (IgA eksikliği/Bruton'da kalıcı)."),
                B("**Plasmodium (sıtma)**: P. falciparum — serebral sıtma, hemoliz, splenomegali, hemozoin. **Leishmania**: **kala-azar** (masif hepatosplenomegali, **Leishman-Donovan cisimcikleri**), kutanöz (şark çıbanı)."),
                B("**Toxoplasma**: konjenital (**koryoretinit, hidrosefali, intrakraniyal kalsifikasyon**), AIDS'te **beyin absesi**, lenfadenit. **Ekinokok (kist hidatik)**: karaciğer > akciğer; kız veziküller, “hidatik kum”."),
                B("**Schistosoma**: mansoni/japonicum → **“pipe-stem” portal fibrozis**, portal HT, splenomegali; **haematobium → mesane SCC**. Trichinella (kas), **sistiserkoz** (beyin, nöbet), Strongyloides (immünsüpresyonda hiperenfeksiyon), filaria (elefantiazis); parazitlerde **eozinofili** (Th2, IL-5)."),
            ]),
        ],
    ],
    sorular=[
        Q("24-25", 82, "Akut apandisit etyolojisinde rol oynayabilen enfeksiyon ajanı?",
          "Enterobius vermicularis", "HSV, HPV, E. histolytica, molluskum kontagiozum değil"),
        Q("23-24", 82, "Vücutta mononükleer inflamasyona yol açan bakteri?",
          "Treponema pallidum", "S. aureus, grup A streptokok, C. perfringens, C. jejuni → süpüratif/nekrotizan"),
        Q("22-23", 83, "Hangisi bakteriyel bir hastalık DEĞİLDİR?",
          "Tinea versikolor (Malassezia — mantar)", "İmpetigo, erizipel, kızıl, psödomembranöz enterokolit bakteriyel"),
        Q("25-26", 64, "(AIDS fırsatçı enfeksiyonları — bkz. Bölüm 21)",
          "Fırsatçı olmayan: S. pneumoniae", None, ref=True),
        Q("21-22", None, "Pnömokok pnömonisi · Kronik hepatit yapmayan ajan · COVID-19 akciğer patolojisi evreleri",
          "Süpüratif, lober tutulum · HAV/HEV kronikleşmez (HBV/HCV yapar) · eksüdatif faz (DAH)", "Öğrenci hatırlamasından; şıklar tam bilinmiyor", n=3),
    ],
))
