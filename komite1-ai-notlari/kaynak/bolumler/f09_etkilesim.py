# -*- coding: utf-8 -*-
"""Kaynak: Drive › Komite-1 › PDF › Farmakoloji › 2026-2027(yeni) › Oruç Yunusoğlu › 4-ilaç-ilaç etkileşimleri end"""

from yardim import B, C, Q  # noqa: F401

BOLUM = dict(
    key="etkilesim", baslik="İlaç-İlaç Etkileşimleri",
    hoca="Oruç Yunusoğlu", tarih="29 Eylül", saat="2 saat",
    kaynak="4-ilaç-ilaç etkileşimleri end · O. Yunusoğlu · 2026",
    ozet=["**Antagonizma türleri** (kimyasal / fizyolojik / farmakolojik) **5 yılın 5'inde** soruldu; çoğu soru **örnek ilaç çifti** istiyor (örnekler 2026 PDF'inde yok).",
          "25-26: **Sınıf I-VI klinik anlam tablosu** (Sınıf IV'te serum/lab izlemi gerekir), **verapamil = P-gp inhibitörü**, sumasyon / potansiyalizasyon tanımı.",
          "Tuzaklar: **potansiyalizasyon etkiyi artırır** (azaltmaz); **fizyolojik** antagonizma **ayrı reseptör**, **farmakolojik** antagonizma **aynı reseptör**; **farmasötik** etkileşme vücut dışında (çökelti)."],
    slaytlar=[
        # 1 — önem
        [
            C("Advers ilaç olayları ve önlenebilirlik", [
                B("Advers ilaç olayları **önemli bir hasta güvenliği sorunudur**; önemli bir bölümü **önlenebilir**."),
                B("Önlenebilirlik oranı; **hasta grubu, klinik ortam ve çalışmanın yöntemine** göre değişir. Advers ilaç olaylarının yaklaşık **%28–56'sı önlenebilir**."),
                B("İlaç hataları: **yanlış ilaç, yanlış doz, yanlış uygulama yolu, uygunsuz ilaç kombinasyonları, yetersiz izlem**."),
                B("**İlaç etkileşimleri**, önlenebilir advers ilaç olaylarının **önemli nedenlerinden biridir**."),
            ]),
            C("Etkileşimlere bağlı zarar verileri", [
                B("Etkileşimlere bağlı **ölüm sayısı kesin bilinmiyor** — küresel ölçekte ayrı gösteren güvenilir epidemiyolojik veri yok."),
                B("İlaç ilişkili zarar, sağlık hizmetlerinde **önlenebilir zararın yaklaşık %50'si**; **her 20 hastadan 1'i** önlenebilir ilaç ilişkili zarardan etkilenir."),
                B("Bu zararların yaklaşık **%25'i yaşamı tehdit edici**."),
                B("Etkileşimler özellikle **polifarmasi, ileri yaş ve yüksek riskli ilaç kullanımı**nda önemli risk faktörüdür."),
            ]),
        ],
        # 2 — olumlu/olumsuz, önemi
        [
            C("Olumsuz etkileşme", [
                B("İlaç etkisinde **kayıp**"),
                B("İlaç etkisinde **beklenmeyen artış**"),
                B("**Toksisite**"),
            ]),
            C("Olumlu etkileşme", [
                B("İlacın **terapötik etkinliğinde artış**"),
                B("**İlaç yan etkisinde azalma**"),
                B("**İlaç toksisitesinin tedavisi**"),
            ]),
            C("İlaç etkileşimlerinin önemi", [
                B("Tabibler için ilaç yazmak **ciddi bir karardır**; ilaçları doğru kullanmak ve yan etki/zararı erken fark etmek **bilgi, ilgi ve dikkat** ister."),
                B("**Bütün etkileşimleri bilmek imkansız**; ama **sık reçete ettiklerimizi ve ciddi sonuçlara yol açanları** bilmek mümkündür."),
                B("Etkileşmelerin gelişimi **zamana bağlıdır**; öngörülebilirlik ve dolayısıyla **önlenebilirlik yüksektir**."),
            ]),
        ],
        # 3 — yanıt örneği, türler, mekanizmalar
        [
            C("İlaç yanıtı örneği (A = 5, B = 5)", [
                B("**A + B = 10 → Sumasyon** (toplam etki, tek başlarına oluşturdukları etkilerin toplamına eşit)", y="25-26"),
                B("**A + B = 50 → Sinerjizm**", y="21-22"),
                B("**A + B = 2 → Antagonizm**"),
            ]),
            C("İlaç etkileşim türleri", [
                B("**İlaç-ilaç** · **ilaç-gıda** · **ilaç-madde** · **ilaç-hastalık** · **ilaç-laboratuvar test** etkileşimleri."),
            ]),
            C("İlaç-ilaç etkileşimi: 3 düzey", [
                B("**Farmasötik**: örn. **sodyum tiyopental ile vekuronyum**un IV uygulama seti içinde birlikte kullanımında **çökelti oluşması**.", y="22-23"),
                B("**Farmakokinetik**: **emilim, dağılım, metabolizma, atılım**.", y="21-22"),
                B("**Farmakodinamik**: farmakolojik etki düzeyindeki etkileşimler (**sinerjizm – antagonizm**).", y="21-22"),
            ]),
        ],
        # 4 — farmakokinetik + metabolizma
        [
            C("Farmakokinetik etkileşimler", [
                B("Bir ilacın başka bir ilacın **sistemik konsantrasyonunu değiştirerek** etki yerinde **“ne kadar miktarda”** ve **“ne kadar süre ile”** bulunacağını etkilemesi sonucu olur.", y="21-22"),
                B("Etkileşme ilaçların **etki yerinden uzakta** oluşur (absorbsiyon, dağılım, metabolizma, ekskresyon).", y="21-22"),
                B("Sonuç: vücut sıvılarında ve etki yerinde **ilaç konsantrasyonu ↑ veya ↓**.", y="21-22"),
            ]),
            C("Metabolizma düzeyinde — CYP enzimleri üzerinden", [
                B("Bir ilaç, başka bir ilacın metabolizmasından sorumlu **CYP enzimini inhibe veya indükler**."),
                B("**Enzim inhibisyonu**: metabolizma ↓ → ilaç düzeyi ve etkisi ↑ (**↑ toksisite**).", y="21-22"),
                B("**Enzim indüksiyonu**: metabolizma ↑ → ilaç düzeyi ve etkisi ↓ (**↓ etkinlik**).", y="21-22"),
                B("Aynı CYP enziminin **substratı** olan ilaçlar arasında metabolizma için **rekabet** oluşabilir."),
                B("Bir ilaç aynı zamanda bir CYP enziminin **substratı** ve başka bir CYP enziminin **inhibitörü** olabilir."),
                B("**Nonmikrozomal enzimlerde de inhibisyon olur.**"),
            ]),
        ],
        # 5 — klinik örnekler, slayt soruları, listeler
        [
            C("Klinik örnekler (slayt)", [
                B("**Kinidin**: CYP2D6 ile metabolize olur; **güçlü CYP2D6 inhibitörü** → CYP2D6 substratı ilaçların düzeyini artırabilir."),
                B("**Eritromisin**: CYP3A4 ile metabolize olur + CYP3A4 **inhibitörü** → CYP3A4 substratı ilaçların düzeyini artırabilir."),
                B("**Rifampisin**: **güçlü enzim indükleyicisi** → birçok ilacın metabolizmasını artırarak düzeyini ve etkinliğini azaltabilir."),
            ]),
            C("Slayttaki sorular (cevap)", [
                B("Rifampisinle birlikte kullanılan ilacın plazma konsantrasyonu belirgin azalıyor → en olası mekanizma **CYP enzimlerinin indüksiyonu**."),
                B("Eritromisin + CYP3A4 ile metabolize olan ilaç → **metabolizma yavaşlar, plazma düzeyi artar**."),
            ]),
            C("İndükleyenler / inhibe edenler (slayt listesi)", [
                B("**İndükleyenler**: **Rifampisin**, **St John's wort**."),
                B("**İnhibe edenler**: ketokonazol, itrakonazol, flukonazol · eritromisin vb. **makrolidler** · fluvoksamin, fluoksetin, sertralin · nefazodon · "
                  "kalsiyum kanal blokerleri (**Verapamil**) · omeprazol · **greyfurt suyu**.", y="25-26"),
                B("Aynı slaytta geçen diğer ilaç adları: siklosporin, takrolimus; terfenadin, astemizol, digoksin, midazolam, sakinavir."),
            ]),
        ],
        # 6 — itrah
        [
            C("Atılım (itrah) düzeyinde — tübüler sekresyon", [
                B("**Katyon transport sistemi**: prokainamid, sisplatin, simetidin, tetraetil amonyum."),
                B("**Anyon transport sistemi**: penisilin G, probenesid, siprofloksasin, sefalosporinler, riboflavin, para-aminohippurat."),
                B("Rekabet örnekleri: **tetraetil amonyum × sisplatin**; **probenesid × penisilin–sefalosporin**."),
                B("**Digoksin** böbreklerden **P-glikoprotein pompası** ile tübüler sekresyona uğrar."),
            ]),
            C("İdrar pH'sı ve itrah — zayıf asidik ilaçlar", [
                B("**Zayıf asidik ilaçlar**: varfarin vb. antikoagülanlar, salisilat, fenobarbital, sulfadiazin, sulfamerazin, tolbutamid, nitrofurantoin, nalidiksik asid, tetrasiklin."),
                B("**İdrar asit → itrah ↓**; **idrar bazik → itrah ↑**."),
            ]),
            C("İdrar pH'sı ve itrah — zayıf bazik ilaçlar", [
                B("**Zayıf bazik ilaçlar**: amfetaminler, efedrin, fenitoin, klorpromazin, amitriptilin, imipramin, meperidin, kinin, kinidin, teofilin."),
                B("**İdrar asit → itrah ↑**; **idrar bazik → itrah ↓**."),
            ]),
        ],
        # 7 — farmakodinamik
        [
            C("Farmakodinamik etkileşmeler", [
                B("Etkileşen ilaçların ya **aditif etki ile toplam etkiyi artırması** ya da **ters etki ile toplam etkiyi azaltması veya tamamen ortadan kaldırması** durumunda meydana gelir.", y="21-22"),
                B("**SSS depresanları birbirinin etkisini potansiye eder.**", y="25-26 21-22",
                  tuzak="“Potansiyalizasyon: iki ilaç birlikte kullanıldığında etkileri azalır, birbirlerinin etkisini zayıflatırlar” → YANLIŞ"),
            ]),
            C("Antagonizma türleri (slayt)", [
                B("**Kimyasal antagonizma**.", y="25-26 23-24"),
                B("**Fizyolojik antagonizma**: **ayrı reseptör** mekanizması ile **zıt yönde** etkilidir.", y="25-26 21-22"),
                B("**Farmakolojik antagonizma**: iki ilaç **aynı reseptöre** bağlanır.", y="24-25 22-23"),
            ]),
        ],
        # 8 — sınıflar
        [
            C("Etkileşim sınıfları (Sınıf — klinik anlam — örnek)", [
                B("**I — Kontrendikedir.** En az bir güvenilir kaynakta/ürün bilgisinde birlikte kullanımı kontrendikedir. Örn. **sildenafil + nitrat**.", y="25-26"),
                B("**II — Mümkünse birlikte kullanılmamalı**; yarar riskten fazla ise kullanılabilir. Örn. **statin + gemfibrozil**.", y="25-26"),
                B("**III — Etkileşim aynı sınıftaki tüm ilaçlar için geçerli değildir**; alternatif ilaç tercih edilebilir. Örn. **makrolid + statin**."),
                B("**IV — İlaçlardan en az biri için serum düzeyi veya laboratuvar izlemi gerekebilir**; doz ayarı yapılabilir. Örn. **digoksin + loop diüretik**.", y="25-26",
                  tuzak="“Sınıf IV: genellikle ciddi toksisite oluşturmaz, serum düzey takibi gerekmez” → YANLIŞ"),
                B("**V — İlaçlardan birinin düzeyi artabilir veya azalabilir**; toksisite veya tedavi yetersizliği açısından izlem gerekir. Örn. **verapamil + beta-bloker**.", y="25-26"),
                B("**VI — Diğer ilacın başlanması veya kesilmesiyle** etkileşim ortaya çıkabilir; izlem ve gerekirse doz ayarı. Örn. **varfarin + tiroid ilaçları**.", y="25-26"),
            ]),
        ],
        # 9 — klinik örnek tablosu
        [
            C("Etkileşim — mekanizma / sonuç — klinik yaklaşım (slayt tablosu)", [
                B("**Sildenafil + nitrat**: ↑ cGMP → ciddi hipotansiyon → **birlikte kullanılmaz**."),
                B("**Simvastatin + gemfibrozil**: ↑ statin maruziyeti → miyopati / rabdomiyoliz → **kaçınılmalı**."),
                B("**Simvastatin + güçlü CYP3A4 inhibitörü**: ↑ simvastatin düzeyi → rabdomiyoliz riski → kaçınılmalı / alternatif statin."),
                B("**Ritonavir + simvastatin**: güçlü CYP3A inhibisyonu → ↑ simvastatin düzeyi → **kontrendike**."),
                B("**Ritonavir + sildenafil**: CYP3A4 inhibisyonu → ↑ sildenafil maruziyeti → doz/tedavi düzenlenmeli."),
                B("**Varfarin + amiodaron**: varfarin etkisi ↑ → INR ↑ / kanama riski → INR yakın izlenir."),
                B("**Digoksin + amiodaron**: digoksin düzeyi ↑ → digoksin toksisitesi → düzey ve klinik izlem."),
                B("**ACEİ/ARB + K⁺ tutucu diüretik**: hiperkalemi → K⁺ ve böbrek fonksiyonu izlenir."),
            ]),
        ],
        # 10 — dar TI, TI, yarı ömür
        [
            C("Etkileşmeye yatkın ilaçlar: terapötik aralığı dar olanlar", [
                B("**Oral antikoagülanlar** (varfarin) · **antikanser** (5-florourasil) · **immünsupresif** (siklosporin)"),
                B("**Antiaritmik** (kinidin) · **dijital glikozidleri** (digoksin) · **antikonvülzanlar** (fenitoin) · **oral hipoglisemik** (gliburid)"),
            ]),
            C("Terapötik indeks (TI)", [
                B("**TI = MTK / MEK**."),
                B("**MEK**: minimum etkili konsantrasyon (istenilen tedavi etkisini gösterebildiği en az ilaç miktarı)."),
                B("**MTK**: toksik etkiye ulaşmadan önceki maksimum konsantrasyon."),
                B("**Dar terapötik indeksli ilaçlarda kan düzeyleri sıkı takip edilmelidir**: digoksin, teofilin, varfarin."),
            ]),
            C("İlaç yarı ömrü (T½)", [
                B("İlacın kandaki miktarının **yarıya düşmesi için geçmesi gereken süre**."),
                B("**T½ uzadıkça doz aralığı artar**, **T½ kısaldıkça doz aralığı sıklaşır**."),
            ]),
        ],
        # 11 — en önemli 10 (1-5)
        [
            C("En önemli 10 / malpraktis açısından yüksek riskli 10 etkileşim (1-5)", [
                B("**1- Sildenafil + nitrat**: güçlü vazodilatasyon → ciddi hipotansiyon, senkop, iskemi → **birlikte kullanılmaz**."),
                B("**2- Opioid + benzodiazepin**: SSS depresyonu → solunum depresyonu, koma, ölüm → kaçınılmalı; zorunluysa yakın izlem."),
                B("**3- Metotreksat + trimetoprim (/sulfametoksazol)**: metotreksat toksisitesi → miyelosupresyon, mukozit → kaçınılmalı."),
                B("**4- Varfarin + NSAİİ**: antikoagülasyon + GİS hasarı → majör kanama, GİS kanaması → kanama/INR izlemi."),
                B("**5- Varfarin + amiodaron**: varfarin etkisi ↑ → INR ↑, ciddi kanama → INR yakın izlenir, doz ayarlanır."),
            ]),
        ],
        # 12 — (6-10)
        [
            C("En önemli 10 / malpraktis açısından yüksek riskli 10 etkileşim (6-10)", [
                B("**6- Digoksin + amiodaron**: digoksin düzeyi ↑ → toksisite, bradikardi, aritmi → digoksin düzeyi ve EKG izlemi."),
                B("**7- Simvastatin + gemfibrozil**: statin maruziyeti ↑ → miyopati, rabdomiyoliz, akut böbrek hasarı → kaçınılmalı."),
                B("**8- SSRI/SNRI + MAO inhibitörü**: serotonerjik aktivite ↑ → **serotonin sendromu**, hipertermi, nöbet → birlikte kullanılmaz; uygun wash-out."),
                B("**9- ACEİ/ARB + spironolakton**: K⁺ ↑ → ciddi hiperkalemi, kardiyak aritmi → K⁺ ve böbrek fonksiyonu izlenir."),
                B("**10- Lityum + NSAİİ**: lityum renal klirensi ↓ → lityum toksisitesi, nörolojik toksisite → yakın izlem / doz ayarı."),
            ]),
        ],
        # 13 — en tehlikeli 10
        [
            C("En tehlikeli 10 ilaç etkileşimi (slayt listesi)", [
                B("**Warfarin + NSAİ** (asetilsalisilik asit, parasetamol, metamizol sodyum)"),
                B("**Warfarin + sülfonamid**"),
                B("**Warfarin + makrolid** antibiyotikler"),
                B("**Warfarin + kinolon** grubu antibiyotikler"),
                B("**Warfarin + fenitoin**"),
                B("**ACE inhibitörü + potasyum preparatı**"),
                B("**ACE inhibitörü + spironolakton**"),
                B("**Digoksin + amiodaron**"),
                B("**Digoksin + verapamil**"),
                B("**Teofilin + kinolon** antibiyotik"),
            ]),
        ],
    ],
    sorular=[
        Q("25-26", 13, "Etkileşim sınıflandırması (Sınıf I-VI) ile ilgili YANLIŞ ifade hangisi?",
          "c) Sınıf IV: ciddi toksisite oluşturmaz, serum düzey takibi gerekmez",
          "PDF: Sınıf IV'te serum düzeyi/laboratuvar izlemi gerekebilir, doz ayarı yapılabilir. I, II, V, VI şıkları PDF ile uyumlu."),
        Q("25-26", 14, "Aşağıdakilerden hangisi P-glikoprotein inhibitörüdür?",
          "e) Verapamil",
          "PDF: verapamil 'inhibe edenler' listesinde; rifampisin indükleyici. Deksametazon, fenitoin, karbamazepin PDF'te yok · (PDF'te geçmiyor)"),
        Q("25-26", 42, "Hangisi yanlıştır? (fizyolojik / kimyasal / kompetitif antagonist, sumasyon, potansiyalizasyon)",
          "e) Potansiyalizasyon: etkileri azalır, birbirlerinin etkisini zayıflatırlar",
          "Potansiyalizasyon = supra-aditif, etki ↑ (PDF: SSS depresanları potansiye eder; sumasyon 5+5=10, sinerjizm 5+5=50). Kompetitif tanımı PDF'te yok"),
        Q("24-25", 45, "Farmakolojik antagonizmaya örnek eşleştirme hangisi?",
          "d) Morfin — Nalokson",
          "PDF: farmakolojik antagonizma = iki ilaç aynı reseptöre bağlanır. Heparin–protamin, demir–desferrioksamin kimyasal; örnekler PDF'te yok · (PDF'te geçmiyor)"),
        Q("23-24", 30, "Aşağıdakilerden hangisi kimyasal antagonizmaya örnektir?",
          "b) Heparin — Protamin",
          "Kimyasal birleşerek etkisiz kılma. Morfin–nalokson farmakolojik, dopamin–haloperidol / histamin–simetidin reseptör düzeyi. Örnek PDF'te yok · (PDF'te geçmiyor)"),
        Q("22-23", 17, "Farmasötik etkileşmeye örnek OLMAYAN hangisi?",
          "c) Simetidin — İzoniazid",
          "Farmasötik = vücut dışı fizikokimyasal uyuşmazlık (PDF: tiyopental + vekuronyum çökelti). Diğer şıklar karışım uyuşmazlığı · (PDF'te geçmiyor)"),
        Q("22-23", 18, "Farmakolojik antagonizmaya örnek OLMAYAN hangisi?",
          "e) Propranolol — Aspirin",
          "Diğerleri aynı reseptör üzerinden antagonizma (ACh–atropin, morfin–nalokson, östrojen–tamoksifen, adrenalin–fenoksibenzamin) · (PDF'te geçmiyor)"),
        Q("21-22", None, "Fizyolojik antagonizma?",
          "Farklı (ayrı) reseptör üzerinden, zıt yönde etki",
          "PDF: 'ayrı reseptör mekanizma ile zıt yönde etkilidir'. Farmakolojik antagonizma ise aynı reseptöre bağlanır."),
        Q("21-22", None, "Farmakokinetik ilaç etkileşimleri ile ilgili hangisi doğru? (hatırlanan şık: 'OK etkinliği…')",
          "Tam şık hatırlanmıyor — 'OK etkinliği' içeren şık",
          "PDF: enzim indüksiyonu (örn. rifampisin) → metabolizma ↑, ilaç düzeyi/etkinliği ↓; inhibisyon → düzey ↑. OK, PDF'te geçmiyor · (PDF'te geçmiyor)"),
        Q("21-22", None, "Supraaditif etkileşim? (hatırlanan: 1 + 0 = 2)",
          "Potansiyalizasyon",
          "PDF'te potansiyalizasyon tanımı yok; yalnızca 'SSS depresanları birbirinin etkisini potansiye eder' ve sinerjizm 5+5=50 · (PDF'te geçmiyor)"),
    ],
)
