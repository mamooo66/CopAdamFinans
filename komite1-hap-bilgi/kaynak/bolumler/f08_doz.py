# -*- coding: utf-8 -*-
"""Kaynak: Drive › Komite-1 › PDF › Farmakoloji › 2026-2027(yeni) › Akif Hakan Kurt › 5-Doz Konsantrasyon Etki İlişkisi (22 slayt)"""

from yardim import B, C, Q  # noqa: F401

BOLUM = dict(
    key="doz", baslik="Doz-Konsantrasyon-Etki İlişkisi",
    hoca="Prof. Dr. Akif Hakan Kurt", tarih="28 Eylül", saat="2 saat",
    kaynak="5-Doz Konsantrasyon Etki İlişkisi · Prof. Dr. A. H. Kurt · 2026",
    ozet=["Son 5 yılda **3 soru**, hepsi aynı grafik (A, B, C, D ilaçlarının **kademeli doz-etki eğrileri**, slayt 20): **potens** (22-23) ve **efikasite** (23-24, 25-26).",
          "Grafiğin cevabı slaytta yazılı: **Güç: A > B > D** · **Efikasite: A = B = D > C**. Çeldiriciler: “A=B=D<C”, “A<B<C”, “A=B>C”, “A=B=D” (potens).",
          "24-25'te ayrıca **kararlı duruma erişme süresi → eliminasyon yarılanma ömrü (t½)** soruldu (soru Eliminasyon bölümünde sayıldı)."],
    slaytlar=[
        [
            C("Etki, tesir, yanıt", [
                B("**ETKİ**: ilacın esas olarak **hücre, doku ve organ** gibi nispeten yalın sistemlerde genellikle **direkt** oluşturduğu, **temel nitelikteki** değişikliklerdir."),
                B("**TESİR**: ilaca bağlı olarak bir organda veya tüm organizma üzerinde meydana gelen, **dışarıdan gözle görülebilen** ya da basit inceleme yöntemleriyle izlenebilen değişikliklerdir."),
                B("**YANIT** hem etki hem de tesiri içine alır."),
            ]),
            C("I. Doz-konsantrasyon-etki ilişkisi", [
                B("İlaçların etki oluşturabilmesi için etki yerlerinde belirli bir **minimum etkin konsantrasyonun (MEK)** üstünde olmaları gerekir."),
                B("Doz giderek artırılırsa etki **doza bağımlı olarak artar**; konsantrasyon belli bir sınıra ulaştığında etki **maksimuma** ulaşır."),
                B("Konsantrasyonun bu sınırın üzerine çıkması etkide **daha fazla artışa neden olmaz**."),
                B("İlacın dozunun etki yerinde **yeterli bir süre** ve **optimal konsantrasyonda** olması sağlanmalıdır."),
            ]),
        ],
        [
            C("Plazma konsantrasyonu-zaman eğrisi", [
                B("İlaç verildikten sonra belirli aralıklarla **kan numunesi** alınarak plazmadaki ilaç konsantrasyonları belirlenir."),
                B("Zamana karşı konsantrasyonlar grafiğe geçirilince ilaca özgü **plazma konsantrasyonu-zaman eğrileri** elde edilir."),
                B("Bu grafiklerden **farmakokinetik parametreler** hesaplanır: **sanal dağılım hacmi (Vd), klirens, yarılanma ömrü (t½)**."),
                B("Slayt başlıkları (grafik): **A. tek doz** verilmesinde eğri; **i.v. ve oral** verilişte eğriler ve **MEK**."),
            ]),
            C("Eğrilerin kantitatif değerlendirilmesinde 3 parametre", [
                B("**Doruk (maksimum) konsantrasyon değeri: Cmaks**."),
                B("**Doruk süresi: tmaks** — absorbsiyonun başlangıcından konsantrasyonun doruğa erişmesine kadar geçen süre."),
                B("**Eğrinin altındaki alanın yüzölçümü: EAA** — **doz ile orantılıdır** (ilacın non-lineer kinetik göstermemesi koşuluyla)."),
            ]),
        ],
        [
            C("Sabit aralarla yinelenen dozlar — neden?", [
                B("İlaçlar çoğu endikasyonda **belirli dozlarda (D)** ve **belirli intervallerle (T)**, **uzun süre (t)** verilerek **sürekli etki** elde etmek için kullanılır."),
                B("İlaç **ilk dozu ile etkin plazma konsantrasyonuna ulaşmaz**."),
                B("Yinelenen uygulama, ilk **bir veya birkaç gün** içinde plazma konsantrasyonunu istenen düzeye çıkarır; **terapötik etki ilacı birçok kez uyguladıktan sonra** başlar."),
            ]),
            C("Yinelenen verilişin önemli parametreleri", [
                B("**1) Kararlı durumdaki konsantrasyonun büyüklüğü** · **2) Bu konsantrasyona ulaşmak için geçen süre**."),
                B("Kararlı durum konsantrasyonu **MEK'in üzerinde**, ama **toksik konsantrasyonlara fazla yaklaşmamalı**."),
                B("Doz intervali (T) ne hastayı **taciz edecek kadar kısa**, ne de fluktuasyonlar büyük olacak kadar **uzun** olmalı."),
                B("Fluktuasyon genliği büyükse her intervalde C bir süre **MEK'in altına düşebilir**; **minimum toksik konsantrasyona** erişme olasılığı artar."),
            ]),
        ],
        [
            C("Kararlı durumda ortalama konsantrasyon (Cssort) — oral / i.m.", [
                B("T aralıklarla hangi dozda verileceği: **DOZ = total klirens × Cssort × T × vücut ağırlığı** (mg = litre/saat/kg × mg/l × saat × kg)."),
            ]),
            C("Kararlı durum konsantrasyonuna erişme hızı", [
                B("**Eliminasyon hız sabitesine, dolayısıyla yarılanma ömrüne (t½) bağımlıdır.**", y="24-25"),
                B("**1 t½** sonra platonun **%50**'sine · **2 t½** sonra **%75**'ine."),
                B("**4 yarılanma ömrü** sonra platoya eriştiği kabul edilir (**%94**)."),
            ]),
            C("Terapötik indeks (güvenlik oranı)", [
                B("Minimum toksik etki gösteren konsantrasyon ile minimum tedavi etki gösteren konsantrasyon arasındaki fark; **Tİ = TD50 / LD50**."),
                B("Tİ **küçük (dar)** ise fluktuasyonların büyüklüğü tehlike yaratır; etkiyi sürdürmek için **i.v. infüzyon** yoluna gidilebilir."),
                B("**Terapötik ilaç izlemi (TDM)**: numune yinelenen doz verilmeden **hemen önce** alınır (**Cssmin = çukur / doz öncesi konsantrasyon**)."),
            ]),
        ],
        [
            C("Yükleme dozu ve idame dozu", [
                B("**t½'si uzun** ilaçlar yinelenerek verildiğinde plato düzeyine erişme **fazla uzun** olabilir."),
                B("Hastanın klinik durumu derhal plato düzeyini ve etkinin hemen oluşmasını gerektiriyorsa ilaç önce **yükleme dozunda**, sonra interval sırasında **elimine edileni karşılayacak idame dozunda** verilir."),
                B("Slayt başlığı (grafik): aynı ilacın **tek bir yükleme dozundan sonra** aynı miktar ve intervallerle yinelenerek verilmesinde elde edilen konsantrasyon profili."),
            ]),
            C("İlacın i.v. infüzyonla verilmesi", [
                B("Bazı durumlarda **noradrenalin, lidokain, antibiyotikler** i.v. infüzyonla verilir."),
                B("İlaç vücuda **sabit hızda girer (0. derece kinetiği)**, eliminasyon **1. derece kinetiğe** göre olur."),
                B("Plato düzeyine erişme süresi **eliminasyon hız sabitesine (kel)** veya **t½'ye** bağlıdır; yinelenen verilişte de aynıdır."),
                B("İnfüzyon süresi: **2 t½ → %75** · **4 t½ → %94** (platoya erişir) · **7 t½ → %99**."),
            ]),
        ],
        [
            C("II. Doz-etki ve konsantrasyon-etki ilişkisi", [
                B("**Konsantrasyon-etki ilişkisi** → **izole organ banyosu** gibi **in vitro** koşullarda incelenir."),
                B("**Doz-etki ilişkisi** → **in vivo** çalışmalarda olay daha karmaşıktır: hem **doz-konsantrasyon** ilişkisi (**farmakokinetik**) hem **konsantrasyon-etki** ilişkisi (**farmakodinamik**) içine girer."),
            ]),
            C("Nicel inceleme: kademeli ve kuvantal doz-etki", [
                B("**1- Kademeli doz-etki ilişkisi** (slaytta grafik)."),
                B("**2- Kuvantal doz-etki ilişkisi**: incelenen etki **hep veya hiç** şeklinde ise; örn. **baş ağrısının geçmesi, kusmanın geçirilmesi, hayvanın uyuması**."),
            ]),
            C("Potens (etki gücü) ve efikasite (etki maksimumu)", [
                B("Aynı tür etki oluşturan ilaçların **potens farklarının** genellikle **pratik değeri yoktur**; **efikasitenin (etki maksimumu) pratik önemi vardır**."),
                B("**Şekil 7.10**: A, B, C ve D ilaçlarının kademeli doz-etki eğrileri (doz mg/kg, etki % Emaks); güç ve maksimum etki (efikasite) karşılaştırması."),
                B("**Güç: A > B > D** (A eğrisi en solda).", y="22-23", tuzak="“A=B=D” / “A<B<C” / “A=B>C” → potens için YANLIŞ"),
                B("**Efikasite: A = B = D > C** (A, B, D %100 Emaks'a çıkar; C daha düşük maksimumda platoya ulaşır).", y="23-24 25-26", tuzak="“A=B=D<C” / “A<B<D<C” / “A=B=C<D” → YANLIŞ"),
            ]),
            C("İlacın seçiciliği (selektiflik)", [
                B("İstenilen etkiyi oluşturan doz ile istenmeyen etkiyi oluşturan doz arasındaki orana bakılarak belirlenir."),
                B("İstenilen ve istenmeyen etki **farklı reseptörler** üzerinden oluşuyorsa **ED50 veya EC50 ne kadar küçükse ilaç o kadar selektiftir** (β-blokerler)."),
                B("Toksik etki ilacın istenilen etkisinin şiddetlenmiş hali ise **doz-etki eğrisi ne kadar yatıksa o kadar selektiftir**."),
            ]),
        ],
    ],
    sorular=[
        Q("25-26", 22, "A, B, C ve D ilaçlarının EFİKASİTE bakımından ilişkisi hangisidir? (Şekil 7.10 grafiği soruda yok)", "c) A=B=D>C",
          "PDF slayt 20 (Şekil 7.10): Efikasite A=B=D>C; C daha düşük maksimumda platoya çıkar."),
        Q("23-24", 17, "A, B, C ve D ilaçlarının EFİKASİTE bakımından ilişkisi hangisidir? (grafik soruda yok)", "e) A=B=D>C",
          "PDF slayt 20 (Şekil 7.10): “Efikasite: A=B=D>C”. Diğer şıklar yanlış (C en yüksek, A>B>D=C, A<B=C=D vb.)."),
        Q("22-23", 28, "A, B, C ve D ilaçlarının POTENS (etki gücü) bakımından ilişkisi hangisidir? (grafik soruda yok)", "d) A>B>D",
          "PDF slayt 20 (Şekil 7.10): “Güç: A>B>D”. Diğer şıklar (A<B<C, A=B>C, A=B=D, A<B>C) yanlış."),
    ],
)
