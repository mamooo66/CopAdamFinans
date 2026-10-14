# -*- coding: utf-8 -*-
"""Kaynak: Drive › Komite-1 › PDF › Patoloji › 2026-2027(yeni) › Çetin Boran › 4-Karsinojenik Ajanlar (33 slayt)

NOT: 6. ve 24. sayfada çıkarılmış metin yok (yalnız görsel), 29. sayfada ('Burkitt gelişimi') yalnız başlık var; bu sayfalar görülmedi.
"""

from yardim import B, C, Q  # noqa: F401

BOLUM = dict(
    key="karsinojen", baslik="Karsinojenik Ajanlar",
    hoca="Prof. Dr. Çetin Boran", tarih="9 Ekim", saat="1 saat",
    kaynak="4-Karsinojenik Ajanlar · Prof. Dr. Ç. Boran · 2026",
    ozet=[
        "Son 5 yılda bu dersten **7 soru**: **EBV–Burkitt** (24-25, 25-26), **promoter = dietilstilbestrol** (24-25, 25-26), **HPV** (23-24), **HBV** (22-23), **aflatoksin B1–HCC** (21-22).",
        "**Promoter** sorularında çeldiriciler hep **başlatıcılar**: PAH, busulfan / kemoterapötikler, nitrozamin, aflatoksin, azo boyaları (25-26'da UV de).",
        "Virüs sorularında doğru şık slayttaki eşleşme: **EBV** ↔ Burkitt + nazofarengeal Ca, **HPV** ↔ genital siğil + skuamöz Ca, **HBV** ↔ onkojenik virüs.",
    ],
    slaytlar=[
        # 1 — giriş, başlatıcı / promoter kavramı (s.1-4)
        [
            C("Üç temel karsinojen", [
                B("**Kimyasal karsinojenler** · **radyan enerji** · **onkojenik virüsler**."),
            ]),
            C("Başlatıcı ajan ve promoter", [
                B("Kimyasal karsinojenler iki gruba ayrılır: **tümörü başlatıcı ajanlar** ve **tümör progresyonunu sağlayan ajanlar (promoter)**."),
                B("**Promoter tek başına tümör geliştiremez**; **proliferasyon** sağlar."),
                B("Örnekler: **forbol esteri** → **protein kinaz C**'yi aktive eder; **fenobarbital** → **TGF-β yolunu bloke** eder.", lvl=1),
                B("**Başlatıcı ajan** da **tek başına kanseri ortaya çıkaramaz**."),
            ]),
            C("Başlatıcı + promoter deney şeması (slayt)", [
                B("**Grup 2**: başlatıcı ajandan sonra haftada iki defa **promoter** uygulanmış (aylarca)."),
                B("**Grup 3**: **promoter** uygulanmasına aylar sonra başlanmış."),
            ]),
            C("Başlatıcı kimyasal karsinojenler", [
                B("Oldukça **elektrofildir** (elektron eksik atomlar taşır); elektrondan zengin kısımlara (**nükleofilik**) saldırırlar."),
                B("Hedefleri: **DNA, RNA ve proteinler**."),
                B("İkiye ayrılır: **1- direk etki eden karsinojenler**, **2- metabolik etki ile karsinojene dönüşenler**."),
            ]),
        ],
        # 2 — direk / indirekt etkili, PAH (s.5, 7-9, 11-12)
        [
            C("1- Direk etki eden karsinojenler", [
                B("**Metabolik dönüşüme ihtiyaç duymadan** karsinojen etkiye sahiptir; genelde **zayıf karsinojen**dir."),
                B("Çoğunlukla **kanser tedavisinde kullanılan ilaçlardır**: **alkilleyici kemoterapötik ajanlar** — tedavi sonrası daha çok **akut miyeloid lösemi**ye yol açarlar."),
                B("Örnekler: **siklofosfamid, klorambusil, busulfan** (zayıf karsinojen)."),
                B("Slayt listesi — **alkylating agents**: β-propiolactone, dimethyl sulfate, diepoxybutane, anticancer drugs (cyclophosphamide, chlorambucil, nitrosoureas…); **acylating agents**: 1-acetyl-imidazole, dimethylcarbamyl chloride."),
            ]),
            C("2- İndirekt etkili karsinojenler", [
                B("Vücutta **metabolik dönüşüm** ile karsinojenik etki kazanırlar (**prokarsinojen**)."),
                B("Çoğu karsinojen **sitokrom P-450** sistemince metabolize edilir; bu enzim **polimorfiktir**."),
                B("Örnek: P-450 geni **CYP1A1**, sigara içicilerde **polisiklik aromatik hidrokarbonları (benzopiren)** metabolize ederek **akciğer kanseri riskini 7 kat** artırır."),
            ]),
            C("Polisiklik aromatik hidrokarbonlar (PAH)", [
                B("Metabolik işlemlerden geçerek karsinojene dönüşürler; **sigarada** bulunurlar."),
                B("**Izgara ve tütsülenmiş etlerdeki hayvan yağlarından** açığa çıkarlar: ızgara sırasında hayvan yağları yanarak PAH çıkar; **tütsülenmiş et ve balıklarda** da bulunur."),
                B("Slayt listesi: benz[a]anthracene, **benzo[a]pyrene**, dibenz[a,h]anthracene, 3-methylcholanthrene, 7,12-dimethylbenz[a]anthracene."),
            ]),
        ],
        # 3 — aromatik aminler, doğal ürünler, nitrosamin, diğer (s.10, 13-16)
        [
            C("Aromatik aminler, amidler ve azo boyaları", [
                B("**Sitokrom P-450 oksidaz sistemi** ile karsinojene dönüştürülürler."),
                B("**β-naftilamin** (kauçuk sanayinde kullanılır) **mesane Ca riskini 50 kat** artırır."),
                B("**Azo boyaları HCC yapar**."),
                B("Bazı azo boyaları **gıda sanayinde** kullanılır: **tereyağı sarısı**, **scarlet red** (kirazları canlı gösterir)."),
                B("Slayt listesi: 2-naphthylamine (β-naphthylamine), benzidine, 2-acetylaminofluorene, **dimethylaminoazobenzene (butter yellow)**."),
            ]),
            C("Doğal oluşan karsinojenler", [
                B("**Aflatoksin B1**: mısır, pirinç, yerfıstığı gibi mahsullerde üreyen **Aspergillus flavus** mantarınca oluşturulur; **HCC yapar**.", y="21-22"),
                B("Slayt listesi: aflatoksin B1, griseofulvin, cycasin, safrole, betel nuts."),
            ]),
            C("Nitrosamin ve amidler", [
                B("**Nitratlar** yiyeceklere **koruyucu** olarak katılır; **midede nitritlere dönüşerek** kanser yaparlar."),
            ]),
            C("Diğer karsinojenler", [
                B("**Asbest** · **insektisit**"),
                B("**Vinil klorid** → karaciğerde (K.C) **hemanjiosarkom**"),
                B("**Arsenik** → **deri kanseri**"),
                B("**Krom, nikel** gibi metaller → **akciğer Ca**"),
            ]),
        ],
        # 4 — promoterler, UV (s.17-19)
        [
            C("İnternal-external promoter ajanlar", [
                B("**Östrojen** · **dietilstilbestrol**", y="24-25 25-26",
                  tuzak="“PAH, busulfan (kemoterapötik), nitrozamin, aflatoksin, azo boyaları promoterdir” → YANLIŞ (bunlar başlatıcı)"),
                B("**Safra asidi**: aşırı yağ alımı safra asidi sentezini artırır → **kolon Ca**'da **promoter** görevi görür."),
                B("**Alkol** de muhtemel bir promoterdir."),
            ]),
            C("Radyasyon karsinogenezi: UV", [
                B("**Hem UV hem de iyonize radyasyon** kanser yapar."),
                B("UV **deri kanserleri** yapar; etki **maruz kalma süresine, şiddetine ve derinin rengine** bağlıdır."),
                B("UV üçe ayrılır: **UVA (320-400 nm)**, **UVB (280-320 nm)**, **UVC (200-280 nm)**."),
                B("**Karsinojen olan UVB**'dir; **UVC ozon tabakasında filtre edilir**."),
                B("Etki, DNA'da **pirimidin dimerleri** oluşmasına bağlıdır; hasar **NER** ile tamir edilir."),
                B("Bu fonksiyon bozuksa **Xeroderma pigmentosum** oluşur (**otozomal resesif**)."),
                B("**UVB**, **RAS** ve **p53**'te de mutasyon yapar."),
            ]),
        ],
        # 5 — iyonizan radyasyon, mikrobik karsinojenler (s.20-21)
        [
            C("İyonizan radyasyon", [
                B("**Elektromanyetik ışınlar** (X ve gama ışınları) ve **partiküler** ışınlar (α partikülü, β partikülü, nötronlar, protonlar): **ikisi de karsinojen**."),
                B("Radyasyona bağlı gelişen tümörler: **lösemi (en sık)**, **tiroid kanseri (ikinci sıklıkta)**."),
                B("**GİS, kemik ve deri** tümör gelişimi bakımından radyasyona **nispeten dirençli**."),
            ]),
            C("Mikrobik karsinojenler (slayt listesi)", [
                B("**Onkojenik DNA virüsleri** · **HPV** · **EBV** · **Kaposi sarkom herpes virüsü (KSHV = Herpesvirus 8)** · **hepatit B ve C virüsleri** · **Merkel cell poliyoma virüs**.", y="22-23"),
                B("**Merkel cell poliyoma virüs** ciltte **Merkel cell Ca** yapar.", lvl=1),
            ]),
        ],
        # 6 — HPV (s.22-23)
        [
            C("HPV (Human papilloma virus)", [
                B("Yaklaşık **70 genetik tipi** vardır; **en kanserojen olanları tip 16 ve 18**."),
                B("Daha zayıf karsinojenler: **31, 33, 35, 51**."),
                B("**Serviks ve anogenital bölgede skuamöz hücreli karsinom** yapar.", y="23-24"),
                B("**Genital siğillerde HPV 6 ve 11** etkendir.", y="23-24"),
            ]),
            C("HPV — moleküler etki", [
                B("Virüs **E6 ve E7 proteinleri** ile **supresör genlere bağlanarak** işlevlerini bozar."),
                B("**p53** polimorfiktir; bazı tipleri E6'dan daha çok etkilenir."),
                B("**E6** proteini **TERT**'yi uyarır (TERT = telomerazın katalitik alt birimi; hücrelerin ölümsüzleşmesine katkıda bulunur)."),
                B("**E7** proteini **RB**'ye bağlanır; ayrıca CDK inhibitörleri **p21 ve p27**'yi de inaktive eder."),
            ]),
        ],
        # 7 — EBV hastalıkları (s.25-26, 28)
        [
            C("EBV (Epstein-Barr virus)", [
                B("Normalde yaygın olarak **asemptomatik** hastalık yapar; semptomatik hastalığı **enfeksiyöz mononükleoz**."),
                B("EBV **4 tip tümörün** patogenezinde yer alır:"),
                B("**Burkitt lenfomanın Afrika tipi**", y="24-25 25-26", lvl=1),
                B("**B-cell lenfoma** (immünsüpresiflerde)", lvl=1),
                B("**Hodgkin lenfoma**", lvl=1),
                B("**Nazofarengeal Ca**", y="25-26", lvl=1),
                B("İlave olarak **mide karsinomlarının bazılarını**, **T cell lenfoma** ve **NK lenfoma** yapabilir."),
            ]),
            C("EBV ve Burkitt lenfoma", [
                B("EBV **poliklonal B hücre proliferasyonu** yapar; sürekli proliferasyon **çeşitli mutasyonların** oluşmasına zemin hazırlar."),
                B("Enfeksiyon dünyada yaygındır; **sadece Afrika'da Burkitt lenfoma** yapar (iyi tanımlanmamış ko-faktörler sayesinde) — **malarya**.", y="24-25 25-26"),
            ]),
        ],
        # 8 — EBV mekanizması (s.27)
        [
            C("EBV — transformasyon mekanizması", [
                B("EBV lökosit yüzeyindeki **CD21** molekülüne tutunarak hücre içine girer."),
                B("**LMP-1** (latent membran proteini-1): lenfositte **NF-κB ve JAK/STAT** sinyal yolunu uyararak lenfositi **proliferasyona** götürür."),
                B("LMP-1 **aktif bir CD40 reseptörü gibi** davranır (bu reseptör T lenfositten sinyal alınca B lenfositi proliferasyona götürür).", lvl=1),
                B("LMP-1 **Bcl-2**'yi uyararak hücreyi **apopitozdan korur**."),
                B("Virüsün **EBNA-2** geni **siklin D** genini uyarır; ayrıca **LMP-1 ekspresyonunu artırır**."),
                B("EBV ayrıca **viral vIL-10** içerir: monosit ve makrofajların aktive T lenfositlerce uyarılmasını engeller (bu fonksiyon transformasyon için gerekli)."),
            ]),
        ],
        # 9 — HBV/HCV, HTLV-1, H. pylori (s.30-33)
        [
            C("Hepatit B virüsü (HBV)", [
                B("**Hepatoselüler Ca (HCC)** yapar; onkojenik etkisi **indirekt ve multifaktöriyel**.", y="22-23"),
                B("Oluşturduğu hepatit tablosu ve beraberindeki **rejeneratif hiperplazi**.", lvl=1),
                B("Virüsün **HBx proteini** pek çok transkripsiyon faktörünü ve sinyal transdüksiyon yolunu aktifleştirir.", lvl=1),
                B("**Hepatit C virüsü** de HCC yapar: hem **rejenerasyona bağlı** hem **direk tümorojenik etki** ile; mekanizma HBV kadar açık değil."),
            ]),
            C("Onkojenik RNA virüsleri: HTLV-1", [
                B("İnsanda tümör yapıcı, iyi tanımlanmış **tek RNA virüsü HTLV-1**'dir (Human T-cell leukemia virus-1)."),
                B("AIDS virüsü gibi **CD4 T lenfositlere afinitesi** vardır; bu lenfositlerde **transformasyon** yapar."),
                B("Ayrıca **tropikal spastik paraparezi**, **uveit**, **artrit** gibi hastalıklar yapar."),
                B("**tax geni** transformasyonda rol alır: **protoonkogenleri aktive eder**, **süpresör genleri inaktive eder**, **DNA tamiratını engeller**."),
            ]),
            C("Helicobacter pylori", [
                B("**Gastrik enfeksiyon** yapar; aynı zamanda **mide Ca** ve **mide lenfoması** yapar."),
                B("Oluşturduğu lenfoma tipi: **MALToma (marjinal zon lenfoması)**."),
                B("**İnflamasyon ve rejenerasyon** sonucu tümör riskini artırmanın yanı sıra **CagA (sitotoksin-associated A) geni** ile **proliferasyonu stimüle eder**."),
            ]),
        ],
    ],
    sorular=[
        Q("25-26", 76, "Burkitt lenfoma ve nazofaringeal karsinomun etyopatogenezinde önemli rol oynayan?", "Epstein-Barr virüsü",
          "HPV, HBV, şistozomiyazis, H. pylori değil · slayt: EBV 4 tümör — Burkitt (Afrika tipi), B-cell lenfoma, Hodgkin, nazofarengeal Ca"),
        Q("25-26", 81, "Promoter etkisi olan karsinojen?", "Dietilstilbestrol",
          "Kemoterapötik alkilleyiciler, PAH, azo boyaları = başlatıcı · UV = radyasyon karsinojeni"),
        Q("24-25", 78, "Burkitt lenfoma gelişiminde rolü olan enfeksiyon?", "Epstein-Barr virüsü",
          "H. pylori, HPV, HBV, şistozomiyazis değil · slayt: sadece Afrika'da Burkitt yapar (malarya)"),
        Q("24-25", 86, "Kanser progresyonunu sağlayan (promoter) ajan?", "Dietilstilbestrol (sentetik östrojen)",
          "PAH, busulfan, nitrozamin, aflatoksin = başlatıcı"),
        Q("23-24", 73, "Kondiloma akuminatum ve skuamöz hücreli karsinom gelişiminde rolü olan virüs?", "Human papilloma virüs",
          "Genital siğil: HPV 6 ve 11 · skuamöz Ca: HPV 16 ve 18 · EBV, HSV, HBV, VZV değil"),
        Q("22-23", 73, "Transforme edici virüs grubunda sayılabilen?", "Hepatit B virüsü",
          "VZV, CMV, HSV, poliovirüs slayttaki onkojenik virüs listesinde yok"),
        Q("21-22", None, "Hepatoselüler karsinom yapan ajan?", "Aflatoksin B1",
          "Öğrenci hatırlamasından derlenmiş soru"),
    ],
)
