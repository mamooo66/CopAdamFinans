# -*- coding: utf-8 -*-
"""Kaynak: Drive › Komite-1 › PDF › Farmakoloji › 2026-2027(yeni) › Akif Hakan Kurt › 10-Sülfonamidler ve Trimetoprim"""

from yardim import B, C, Q  # noqa: F401

BOLUM = dict(
    key="sulfonamid", baslik="Sülfonamidler ve Trimetoprim",
    hoca="Prof. Dr. Akif Hakan Kurt", tarih="13 Ekim", saat="2 saat",
    kaynak="10-Sülfonamidler ve Trimetoprim · Prof. Dr. A. H. Kurt · 2026",
    ozet=["Son 5 yılda bu dersten **4 soru** çıktı: 25-26 ve 24-25 “sülfonamidler için **yanlıştır**”, 23-24 ve 22-23 “hangi **özel kullanımlı** sülfonamid” (yanık / göz).",
          "Tekrarlayan tuzaklar: sülfonamid enzimi **dihidropteroat sentetaz** (DHFR değil), **idrar yollarında çökme** (kristalüri), **ko-trimaksazol = sülfametoksazol + trimetoprim**.",
          "Özel kullanım eşleşmeleri: **gümüş sülfadiazin → yanık**, **sulfasetamid → konjunktivit (göz)**, **sulfasalazin → ülseratif kolit / RA**."],
    slaytlar=[
        [
            C("Sülfonamidler — genel ve etki mekanizması", [
                B("Bakteri enfeksiyonlarının tedavi ve önlenmesinde **sistemik olarak kullanıma giren ilk etkin kemoterapötik**."),
                B("Bakteriler folik asidi dışarıdan alamaz; **PABA**’dan kendileri sentezler. Memeliler folik asidi dışarıdan alır."),
                B("Sülfonamidler **PABA analoğudur (antimetabolit)**; **dihidropteroat sentetaz** enzimi için onunla yarışarak **folik asid sentezini inhibe eder**.", y="25-26", tuzak="“Dihidrofolat redüktaz enzimi için yarışarak folik asid sentezini inhibe ederler”"),
                B("Sonuçta bakterilerde **RNA ve DNA sentezi bozulur**."),
            ]),
            C("Antimikrobik spektrum", [
                B("**Gram (+)**: A grubu β-hemolitik streptokoklar, Strep. pneumoniae, Bacillus anthracis’in bazı suşları."),
                B("**Diğerleri**: H. influenzae, H. ducreyi, Brucella, Pseudomonas pseudomallei, Vibrio cholerae, Corynebacterium diphtheriae, Yersinia pestis, Calymmatobacterium granulomatis."),
                B("Ayrıca: Actinomyces, Nocardia, **Plasmodium, Toxoplasma**, bazı Enterobacteriaceae."),
            ]),
            C("Farmakokinetik", [
                B("Mide-barsak kanalından **iyi absorbe** edilir; plazma proteinlerine **%20-80** bağlanır."),
                B("**BOS hariç** diğer vücut sıvılarına iyi nüfuz eder.", y="25-26"),
                B("**KC’de N-asetilasyonla inaktive** edilir; kısmen **glomerüler filtrasyon / tubuler salgılanma** ile böbrekten atılır."),
                B("Eliminasyon yarılanma ömrü ilaca göre değişir (**4-150 saat**)."),
            ]),
        ],
        [
            C("Sınıflandırma", [
                B("Farmakokinetik özellik ve kullanım alanı farklılıklarına göre sınıflandırılır."),
                B("**1- Kısa ve orta etki süreli**: **sulfadiazin, sulfizoksazol, sulfametoksazol**."),
                B("**2- Uzun etkili depo sulfonamidler**: günde **tek doz**; **toksisitelerinin ciddiliği nedeniyle tercih edilmezler**."),
                B("**3- Özel kullanılış yerlerine sahip** sulfonamidler (aşağıda)."),
            ]),
            C("Özel kullanılış yerleri", [
                B("**Sulfasetamid**: **konjunktivit** tedavisinde.", y="22-23"),
                B("**Gümüş-sülfadiazin %1 krem**: **yanık tedavisinde**.", y="23-24"),
                B("**Marfanil (mafenid)**: %10 krem; **%2-5 merhem dermatit profilaksi ve tedavisinde**."),
                B("**Sulfasalazin**: **ülseratif kolit** ve diğer idiyopatik enflamatuvar kalın barsak hastalıkları ve **romatoid artrit**te **antiinflamatuvar** olarak."),
                B("Barsakta etkili metaboliti **5-aminosalisilat**a ayrışır; etkili şekli **mesalazin** olarak ilaç yapılmıştır; **olsalazin, balsalazin** türevleri de kullanılır.", lvl=1),
            ]),
            C("Sulfizoksazol ve sülfametaksazol", [
                B("**Sulfizoksazol**: suda çözünürlüğü yüksek; **kristalüri yapmaz**, böbrek toksisitesi az; yarılanma ömrü **6 saat**."),
                B("Sistemik ve **üriner infeksiyonlarda en çok tercih edilen sülfonamid**.", y="25-26", lvl=1),
                B("**Sülfametaksazol**: sulfizoksazole göre absorbsiyonu daha düşük, eliminasyonu yavaş; **kristalüri oluşturabilir**.", y="25-26"),
                B("**Trimetoprim ile kombinasyonu ko-trimaksazol** olarak bilinir.", y="24-25 25-26"),
            ]),
        ],
        [
            C("Kullanılış yerleri ve yan etkiler", [
                B("**Daha güçlü bakterisid etkili ko-trimaksazolün çıkması** tek başına kullanım alanlarını daraltmıştır."),
                B("Kalan endikasyon: hastane dışında gelişen **nonkomplike İYE**."),
                B("Tedavi sırasında idrar yollarında çökme olmaması için **günlük su tüketimi 1,5 litrenin altına düşmemeli**."),
            ]),
            C("Sülfonamidlerin yan tesirleri", [
                B("**Alerjik belirtiler**."),
                B("**İdrar yollarında çökme** (kristalüri).", y="24-25", tuzak="“İdrar yollarında çökme yapmazlar”"),
                B("**Hematolojik bozukluklar**: **G6PD eksikliğinde hemoliz**; nadiren kemik iliği depresyonu."),
                B("**GİS bozuklukları**."),
                B("**Doğuma yakın dönemde alınırsa kernikterus** yapabilir."),
                B("Nadiren **hepatit** ve **nörotoksik etki**."),
                B("**Depo sulfonamidler** fatal bir deri hastalığı olan **Stevens-Johnson sendromu** yapabilir.", y="24-25"),
            ]),
        ],
        [
            C("Ko-trimaksazol (tablet, süspansiyon, ampul)", [
                B("**Trimetoprim**: t½ **11 saat**; oran **1**; tablet **80 mg**, forte **160 mg**. Yapıca bir **sıtma ilacı olan primetamine benzer**."),
                B("**Sülfametoksazol**: t½ **10-12 saat**; oran **5**; tablet **400 mg**, forte **800 mg**."),
                B("Kombine preparatlara **ko-trimaksazol (CTX)** denir.", y="24-25 25-26"),
                B("**Ardışık blok** (dihidropteroat sentaz ve dihidrofolat redüktaz) → tek başına etkiden daha güçlü antibakteriyel etki (**potansiyalizasyon**)."),
                B("Trimetoprim ile kombinasyona sulfametoksazolün seçilme nedeni: **yarı ömürlerinin yakın olması**."),
            ]),
            C("Antibakteriyel spektrum", [
                B("**Gram (−) aerob enterobakterler**e orta-yüksek derecede etkili; en duyarlı: **E. coli, Proteus, Salmonella, Shigella**."),
                B("Gram (−) diğerleri: H. influenzae, Acinetobacter, Citrobacter, Brucella, V. cholerae, Yersinia, B. pertussis, G. vaginalis."),
                B("**Gram (+) kokların çoğu**: S. pneumoniae, S. pyogenes, S. aureus, S. epidermidis · **Gram (−) koklar**: N. meningitidis, N. gonorrhoeae."),
                B("Diğerleri: **Nocardia, Pneumocystis carinii, M. tuberculosis** da duyarlı."),
            ]),
            C("Farmakokinetik", [
                B("Trimetoprim görece fazla lipofilik; **tama yakın absorbe**; dokulara ve vücut sıvılarına çok iyi nüfuz eder."),
                B("**Prostat** ve bazı dokularda plazmadakinden **birkaç kat fazla**."),
                B("**Böbrek yetmezliğinde** her iki komponentin eliminasyonu yavaşlar."),
            ]),
        ],
        [
            C("Başlıca endikasyonlar — genitoüriner ve solunum yolu", [
                B("**E. coli ve diğer enterobakterlerin** yaptığı yukarı ve aşağı **İYE’de ilk tercih** edilecek ilaçlardan biri."),
                B("**Akut sistit** (tek doz forte tb); **kronik rekürren İYE ve piyelonefrit**; **akut ve kronik bakteriyel prostatit**te güçlü etkinlik."),
                B("**Ürojenital gonore**: hasta penisiline alerjik veya penisilinaz salgılayan gonokok ise penisilin yerine."),
                B("**Alt solunum yolu hastane dışı infeksiyonları** (S. pneumoniae, H. influenzae gibi); **akut bronşit**, **kronik bronşitlerin önlenmesi**."),
                B("**Üst solunum yolu**: akut otitis media ve sinüzitte kullanılabilir."),
            ]),
            C("GİS infeksiyonları ve diğerleri", [
                B("**Shigella etkenli enterit**te **florokinolonların alternatifi**.", y="24-25"),
                B("**Tifo dahil Salmonella** infeksiyonlarında florokinolonların ve kloramfenikolün alternatifi."),
                B("**Enteropatojenik E. coli**’ye bağlı çocuk ishali."),
                B("İmmünosupresyonlu veya AİDS’li hastalarda **Pneumocystis carinii pnömonisi**nde **en çok tercih edilen ilaç**."),
                B("**Nocardia asteroides**: ko-trimaksazol veya tek başına sulfonamid **en tercih edilen**."),
                B("**Melioidozis (P. pseudomallei)**: en tercih edilen 3 ilaçtan biri (diğerleri **seftazidim ve seftriakson**)."),
            ]),
        ],
        [
            C("Ko-trimaksazol — yan tesirler", [
                B("**Trimetoprim**e bağlı en sık: **kaşıntı, ciltte makülopapüler / morbiliform döküntü**; nadiren Kİ depresyonu."),
                B("Memeli hücresindeki **dihidrofolat redüktaza afinitesi bakterininkine göre çok düşük** olsa da **uzun süreli kullanımda folik asid eksikliği** → **megaloblastik anemi**."),
                B("Bu nedenle **uzun sürecek tedavilerde mutlaka folik asid verilmeli**."),
            ]),
            C("Kontrendikasyonlar", [
                B("Trimetoprim **folik asid antimetaboliti** olduğundan **gebelerde teratojenik** etki gösterebilir."),
                B("Süte geçtiği için bebeklerde folik asid eksikliği olacağından **emziren annelere ve 12 aydan küçük bebeklere önerilmez**."),
                B("**Streptokokal farenjit ve tonsillitte kontrendikedir.**", y="24-25"),
            ]),
        ],
    ],
    sorular=[
        Q("25-26", 27, "Sülfonamidler için YANLIŞ olan hangisidir?",
          "A) Dihidrofolat redüktaz enzimi için yarışarak folik asid sentezini inhibe ederler",
          "Sülfonamidler **dihidropteroat sentetaz** için PABA ile yarışır. B, C (BOS hariç), D (kristalüri), E (sulfizoksazol en çok tercih edilen) doğru."),
        Q("24-25", 37, "Sülfonamidler için YANLIŞ olan hangisidir?",
          "B) İdrar yollarında çökme yapmazlar",
          "İdrar yollarında **çökme** yan etkidir. Doğru: ko-trimaksazol kombinasyonu, strep. farenjit/tonsillitte kontrendike, depo → Stevens-Johnson, Shigella’da FQ alternatifi."),
        Q("23-24", 22, "Yanık tedavisinde yaygın kullanılan sülfonamid hangisidir?",
          "C) Gümüş sulfadiazin",
          "Sulfasetamid → konjunktivit; sulfasalazin → ülseratif kolit/RA; sulfizoksazol → sistemik ve üriner infeksiyon; sülfametaksazol → ko-trimaksazol bileşeni."),
        Q("22-23", 33, "Oftalmik enfeksiyonlarda yaygın kullanılan topikal sülfonamid hangisidir?",
          "A) Sulfasetamid",
          "Sulfasetamid → konjunktivit. Gümüş sulfadiazin → yanık; sulfasalazin → ülseratif kolit/RA; sulfizoksazol → üriner infeksiyon. Sulfadoksin PDF’te yok."),
    ],
)
