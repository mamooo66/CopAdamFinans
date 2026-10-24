# -*- coding: utf-8 -*-
"""Kaynak: Drive › Komite-1 › PDF › Farmakoloji › 2026-2027(yeni) › Akif Hakan Kurt › 4-İlaçların Eliminasyonu (29 slayt)"""

from yardim import B, C, Q  # noqa: F401

BOLUM = dict(
    key="eliminasyon", baslik="İlaçların Eliminasyonu",
    hoca="Prof. Dr. Akif Hakan Kurt", tarih="22 Eylül", saat="ADME · 4 saat",
    kaynak="4-İlaçların Eliminasyonu · Prof. Dr. A. H. Kurt · 2026",
    ozet=["22-23'ten 25-26'ya **her yıl 1 soru** (24-25'te 2): “İlaçların eliminasyonu ile ilgili hangisi **yanlıştır**?” kalıbı + 24-25'te **kararlı plazma konsantrasyonuna erişme süresi → t½**.",
          "Her yıl dönen **doğru şıklar**: **presistemik eliminasyonu yüksek** (aspirin, propranolol, verapamil, morfin, imipramin), **halotan / azot protoksid** akciğerden hızlı, **tübüler reabsorpsiyon itrahı azaltır**, **anyonik + katyonik taşıyıcı**.",
          "**Çeldiriciler**: tetrasiklin / eritromisin estolat safraya **basit difüzyonla** (doğrusu aktif transport) · hepatik klirens **böbreklere** itrah (doğrusu safraya) · salisilat, varfarin, nitrazepam yaşlanmayla **azalır** (doğrusu artar) · **alkol, barbitürat** salya ile atılır (doğrusu iyodür, bromür, lityum)."],
    slaytlar=[
        [
            C("Eliminasyon — giriş", [
                B("İlaçlar ya **hiç değişmeden** ya da bir kısmı **metabolize olduktan sonra**, değişmemiş ilaç ve metabolitleri şeklinde vücuttan elimine edilirler."),
                B("**Hidrofilik** ilaç: doğrudan atılımla **değişmemiş ilaç** olarak atılır."),
                B("**Lipofilik** ilaç: **biyotransformasyon → hidrofilik metabolit → atılım**; ilaç + metabolit olarak atılır."),
                B("**Eliminasyon = biyotransformasyon + atılım**."),
            ]),
            C("Vücutta metabolize edilen ilaçların atılım yolları", [
                B("**1.** Karaciğerden **safra** içine atılım."),
                B("**2.** **Böbreklerden atılım (esas mekanizma)**: a. **glomerüler filtrasyon**, b. **tübüler sekresyon**, c. **tübüler reabsorpsiyon**."),
                B("**3.** Akciğerlerden · **4.** Salya içinde · **5.** Süt içinde · **6.** Diğer vücut salgılarıyla (ter, gözyaşı, genital vs.)."),
            ]),
            C("Böbreklerden atılım — genel", [
                B("İlaçların **hem metabolitleri hem de değişmemiş şekilleri** atılır."),
            ]),
        ],
        [
            C("A. Glomerüler filtrasyon (GF)", [
                B("Bir **pasif diffüzyon** olayıdır.", y="22-23", tuzak="“Glomerüler filtrasyon aktif transport olayıdır” → YANLIŞ"),
                B("Glomerül membranı **plazma protein moleküllerinden daha küçük** molekülleri geçirir."),
                B("Sadece plazmadaki **serbest ilaç fraksiyonu** filtrasyona uğrar."),
                B("GF hızı **glomerüler kan akımı ile doğru orantılıdır**."),
                B("**İnülin** sadece GF ile atıldığından **GF hızını saptamak** için kullanılır."),
            ]),
            C("Süzülen hacim ve geri emilim", [
                B("Süzülen su hacmi, glomerüllerden geçen plazmanın yaklaşık **%20'si**; dolayısıyla geçen serbest ilacın da **%20'si** süzülür."),
                B("Süzülen sıvının **%99'u geri emilir**. Geri emilme oranı ultrafiltrattaki **glikoz için %100**, ilaçlar için çok düşüktür."),
                B("Biyotransformasyon sonucu ilaçlar **daha polar** olur, lipid/su partisyon katsayıları azalır, suda çözünürlük artar → daha kolay atılır."),
            ]),
        ],
        [
            C("B. Tübüler sekresyon (salgılanma)", [
                B("Bir **aktif transport** olayıdır; esas olarak **proksimal tübülüs** hücreleri içinde olur."),
                B("Salgılamaya plazmadaki **bağlı fraksiyon** da katıldığından **kapasitesi GF'den fazladır**."),
                B("Tübülüs hücrelerinde **anyonik (asidik)** ve **katyonik (bazik ilaçlara özgü)** iki ayrı taşıyıcı molekül vardır.", y="22-23 23-24"),
                B("Benzer yapıdaki ilaçlar aynı taşıyıcı için **yarışır**, birbirlerinin atılımını azaltırlar (örn. **probenesid** → penisilinler veya sefalosporinlerin atılımını azaltır)."),
                B("**P-glikoprotein (MDR-1)** de proksimal tübülüste taşıyıcıdır: **kinidin, digoksin, kolşisin** ve bazı kanser ilaçlarının itrahı."),
                B("**P-aminohipürik asid** ve **penisilin G** yalnızca tübülüslerden salgılandığından **renal plazma akım hızını saptamak** için kullanılır.", y="25-26"),
            ]),
            C("Tablo 6.1 — Tübülüslerden salgılanarak itrah edilen ilaçlar", [
                B("**Asidik ilaçlar**: asetazolamid, p-aminohipürik asid, ilaçların glükuronik asid ve sülfat konjügatları, glisin konjügatları."),
                B("Penisilinler, sefalosporinler, salisilatlar, furosemid ve tiazid diüretikler, indometasin, nitrofurantoin, probenesid, benzbromaron.", lvl=1),
                B("**Bazik ilaçlar**: amilorid, morfin, meperidin, dihidrokodein, kinin, kinidin, simetidin, triamteren, tiamin."),
                B("Kuvaterner amonyum türevleri (neostigmin, d-tübokürarin); dopamin, serotonin, histamin ve N-metilhistamin; guanidin türevleri; prokain ve prokainamid.", lvl=1),
            ]),
        ],
        [
            C("C. Tübüler reabsorpsiyon", [
                B("Esas olarak bir geri alım, yani **itrahı azaltan** bir olaydır; **pasif difüzyonla** olur.", y="22-23 23-24 24-25", tuzak="“Tübüler reabsorpsiyon itrahı arttıran bir olaydır” → YANLIŞ"),
                B("Az sayıdaki bazı maddeler **aktif transportla** reabsorbe olur."),
                B("Klinik örnek: **salisilat zehirlenmesinde** idrar pH'sı **bazikleştirilerek (sodyum bikarbonat)** tübüler reabsorpsiyon azaltılır."),
            ]),
            C("Renal klirens, eliminasyon yarılanma ömrü", [
                B("**Renal klirens**: böbreklerden itrah sonucu **bir dakikada değişmemiş (metabolize olmamış) ilaçtan temizlenen sanal plazma hacmi**."),
                B("**İlacın eliminasyon hızı, klirense ve sanal dağılım hacmine bağlıdır.**", y="25-26"),
                B("**Eliminasyon yarılanma ömrü (t½)** eliminasyon hızının göstergesidir; **t½ = 0.693 (Vd / Cl)**."),
                B("Kural: eliminasyon yarılanma ömrünün **4-5 katı** sürede ilacın vücuttan **tamamen atıldığı** kabul edilir."),
                B("Her yarılanma ömründe kalan miktar yarıya iner: **%100 → 50 → 25 → 13 → 6 → 3** (0.-5. t½)."),
            ]),
            C("Böbrek itrah fonksiyonunun yaşa göre değişmesi", [
                B("**Yeni doğanda** (vücut ağırlığına göre) itrah fonksiyonu erişkine göre **düşüktür**; hızla artar ve erişkin yaşa kadar artar."),
                B("Bundan sonra **her yıl yaklaşık %1** etkinlik azalır; **65 yaş ve üstünde** azalma belirginleşir → **terapötik indeksi dar** ilaçlarda **doz ayarlaması** yapılmalı."),
            ]),
        ],
        [
            C("Karaciğerden safra içine atılım", [
                B("Bazı ilaçlar ve metabolitleri (özellikle **konjugasyon ürünleri**) karaciğer hücreleri tarafından **safra içine atılır, feçes içinde itrah** edilir."),
                B("**Enterohepatik siklus**: ince barsakta enzimlerle hidrolize edilip serbest hale gelen aktif ilaç **tekrar emilir** ve genel dolaşıma geçer."),
                B("**Geçiş mekanizması**: bazı ilaçlar karaciğer hücresinden safraya **basit difüzyonla**, bazıları **aktif transportla (tetrasiklinler, eritromisin estolat)** geçer.", y="24-25 25-26", tuzak="“Tetrasiklin ve eritromisin estolat karaciğer hücresinden safraya basit difüzyonla geçer” → YANLIŞ"),
            ]),
            C("Safraya itrahın derecesini etkileyen 3 özellik", [
                B("**1. Molekülün kimyasal yapısı**: moleküle eklenen grupların niteliği itrah hızını etkiler."),
                B("**2. Molekülün polarlığı**: **fazla iyonize olanlar hızlı itrah** edilir (d-tübokürarin, bromsulfoftalein vs.)."),
                B("**3. Molekül ağırlığı**: sıçan araştırmalarında genellikle **MA 325'in üzerindekiler** itrah edilir; **ufak moleküller** safraya pek itrah edilmez."),
            ]),
            C("KC hücresi membranında aktif transport taşıyıcıları (4 sistem)", [
                B("**Organik asidler** için: karboksilik, glukuronik ve sülfonik asid türevleri."),
                B("**Organik bazlar** için: eritromisin ve kuvaterner amonyum bileşikleri gibi."),
                B("**Nötral organik bileşikler** için: glikozitler ve steroitler gibi."),
                B("**P-glikoprotein**: ilaçları hücre içinden lümene atar."),
            ]),
        ],
        [
            C("Hepatik klirens", [
                B("Karaciğerde ilacın **metabolize edilmesi ve safraya itrahı** sonucu **bir dakikada ilaçtan temizlenen sanal plazma hacmi**.", y="25-26", tuzak="“Karaciğerde metabolize edilmesi ve böbreklere itrahı sonucu temizlenen sanal plazma hacmi hepatik klirenstir” → YANLIŞ"),
                B("**Clh = Q × E**: **Q** = karaciğer kan akım hızı, **E** = karaciğerden geçerken meydana gelen **ekstraksiyon oranı**."),
            ]),
            C("İlk geçiş (first pass) / presistemik eliminasyon", [
                B("Absorpsiyon tam olsa bile **sistemik dolaşıma geçen miktar düşük** olabilir."),
                B("Presistemik eliminasyonu yüksek ilaçlar: **aspirin, propranolol, verapamil, morfin, imipramin**...", y="23-24 24-25 25-26"),
            ]),
            C("Yaşlanmanın hepatik eliminasyona etkisi", [
                B("Yaşlanma ile hepatik eliminasyonu **azalan** ilaçlar: **imipramin, barbitüratlar, meperidin, propranolol, kinidin, kinin, teofilin, diazepam**.", y="24-25"),
                B("Yaşlanma ile hepatik eliminasyonu **artan** ilaçlar: **etanol, izoniazid, lidokain, lorazepam, salisilat, varfarin, nitrazepam**.", y="23-24", tuzak="“Salisilat, varfarin ve nitrazepam yaşlanma ile hepatik eliminasyonu azalan ilaçlardır” → YANLIŞ"),
            ]),
            C("Total klirens", [
                B("**Total klirens = renal klirens + hepatik klirens**."),
            ]),
        ],
        [
            C("Akciğerlerden atılım", [
                B("**Gazların ve uçucu sıvıların** itrahında önemlidir."),
                B("Kandan alveol boşluğuna **pasif difüzyonla** geçer, **ekspirasyonla** atılır (**halotan, azot protoksid**).", y="22-23 23-24 24-25"),
                B("Bunlar **ufak moleküllü, non-elektrolit** ve **lipid/su partisyon katsayısı yüksek** maddelerdir."),
                B("Toplam akciğer yüzeyi **~200 m²** ve **fazla kanlanan** organ olması itrahı **çok hızlı** yapar."),
            ]),
            C("Salya içinde itrah", [
                B("**İyodürler, bromürler ve lityum** gibi bazı ilaçlar tükrük bezlerinden **pasif difüzyonla** salya içine geçip atılır.", y="22-23", tuzak="“Alkol, barbitürat ve bromürler pasif difüzyonla salya içine geçerek atılırlar” → YANLIŞ"),
            ]),
            C("Süt içinde itrah — iyon tuzağı", [
                B("**İnsan sütü plazmaya göre daha asidiktir (pH = 7.08)**; emziren annenin aldığı **bazik (alkali) ilaçlar iyon tuzağı** ile sütte toplanır, bebeğe geçebilir."),
                B("Örnekler: **kloramfenikol, alkol, lityum, barbitürat, opiatlar, sülfonamidler**..."),
                B("Şema: plazma (pH 7.4) **B (non-iyonize)** → anne sütü (pH 7.08) **BH+** (daha asidik ortamda kısmen iyonize, hapsolur)."),
            ]),
        ],
        [
            C("Tablo 6.2 — Emziren kadınlarda kontrendike ilaçlar → bebekteki sakıncası", [
                B("**Altın bileşikleri**: aşırı duyarlılık reaksiyonları, hematolojik ve renal toksisite · **Amiodaron**: tiroid bozukluğu olasılığı"),
                B("**Antineoplastik ilaçlar**: kemik iliği depresyonu · **Kloramfenikol**: kemik iliği depresyonu olasılığı"),
                B("**Doksepin**: solunum depresyonu yapabilir (günde 75 mg veya daha fazla verilirse) · **Ergotamin**: ergotizm olasılığı"),
                B("**İndometasin**: konvülsiyon yapabilir · **İyodürler (öksürük ilaçları dahil)**: tiroid bozukluğu olasılığı"),
                B("**Lityum**: hipotermi ve “floppy baby” sendromu · **Estrojenler (yüksek doz)**: erkek bebekte feminizasyon yapabilir"),
                B("**Penisilamin**: hematolojik ve renal toksisite olasılığı · **Fenindion**: hemorajik hastalık (hematom) yapabilir"),
                B("**Tetrasiklinler**: dişlerde diskolorasyon olasılığı · **Vitamin A ve D (yüksek doz)**: A ve D hipervitaminozu olasılığı"),
            ]),
        ],
        [
            C("Yapay itrah — hemodiyaliz", [
                B("**ABY ve KBY**'de kullanılır; **endojen toksik maddelerin** uzaklaştırılmasında kullanılır. Diyalizle eksilen ilaç miktarı yerine konmalıdır."),
                B("Kullanım alanları: **alkol, metanol, aspirin** zehirlenmeleri."),
                B("Uygun ilaç zehirlenmesi koşulları: **plazma proteinlerine bağlanması düşük**; **dokuya fazla bağlanmamış** (sekestrasyona uğramamış); normal durumda eliminasyonu **böbreklerden değişmeden** olan."),
            ]),
            C("Hemoperfüzyon ve periton diyalizi", [
                B("**Hemoperfüzyon**: **proteine bağlanan ve yağda çözünen** ilaçlar da **kartuştaki kömür** tarafından tutulabildiğinden hemodiyalize oranla **daha etkin** bir yöntemdir."),
                B("**Periton diyalizi**: periton boşluğu içinden **fizyolojik sıvı** geçirmek suretiyle yapılır."),
            ]),
            C("İlaç eliminasyonunun kinetiği", [
                B("Eliminasyon başta **KC** olmak üzere çeşitli organlarda **inaktif metabolitlere dönüştürülerek**; esas olarak **böbreklerle** itrah edilerek olur."),
                B("Bazı ilaçlar **tamamen/büyük kısmı KC'de metabolize**; bazıları az veya hiç metabolize edilmeden **büyük oranda böbreklerden** elimine edilir."),
                B("İlaçların büyükçe bir kısmı **hem KC'de metabolize edilir hem de böbreklerden kısmen değişmeden** itrah edilir."),
            ]),
        ],
        [
            C("Doza bağımlı (non-lineer) kinetik", [
                B("**Non-lineer kinetik**: dozun artması ile farmakokinetik olayın **hızı ve boyutundaki değişmeler arasındaki lineer ilişkinin**, olayın **doygunluğa erişmesi** sonucu kaybolması."),
                B("Örnek: ilacın **plazma proteinlerine bağlanmanın doyurulmasından sonraki** süreçte olduğu gibi."),
            ]),
            C("Lineer ve non-lineer kinetiğe uyan ilaçlar", [
                B("İlaçların **çoğu** olağan tedavi dozlarında **lineer kinetiğe** uyar."),
                B("**Az sayıda ilaç** için tedavi dozlarında eliminasyonla ilgili olayların **doygunluğa erişmesi** nedeniyle **non-lineer kinetik** söz konusu olur."),
            ]),
        ],
    ],
    sorular=[
        Q("25-26", 21, "Eliminasyonla ilgili hangisi YANLIŞTIR? (presistemik · PAH/penisilin G · hepatik klirens · eliminasyon hızı · safraya aktif transport)", "c) Hepatik klirens: metabolize + böbreklere itrah",
          "Hepatik klirens = KC'de metabolize edilme ve SAFRAYA itrah sonucu 1 dakikada temizlenen sanal plazma hacmi; diğer şıklar doğru."),
        Q("24-25", 30, "Eliminasyonla ilgili hangisi YANLIŞTIR? (presistemik · halotan · yaşlanma · reabsorpsiyon · tetrasiklin/eritromisin estolat safraya)", "e) Tetrasiklin ve eritromisin estolat safraya basit difüzyonla geçer",
          "Doğrusu AKTİF transport. Morfin/imipramin/verapamil presistemik yüksek; halotan, azot protoksid akciğerden hızlı; imipramin, barbitürat, meperidin yaşlanmayla azalır."),
        Q("24-25", 31, "Kararlı plazma konsantrasyonuna erişme süresi hangisine bağlıdır?", "c) Yarılanma ömrü (t½)",
          "Cmax, EAA, Vd, tmaks değil. Doz dersi PDF'i: kararlı duruma erişme hızı eliminasyon hız sabitesine, yani t½'ye bağlıdır (4 t½ → %94)."),
        Q("23-24", 16, "Eliminasyonla ilgili hangisi YANLIŞTIR? (presistemik · halotan · yaşlanma · reabsorpsiyon · tübülüs taşıyıcıları)", "c) Salisilat, varfarin, nitrazepam yaşlanmayla hepatik eliminasyonu azalır",
          "Doğrusu ARTAR (etanol, izoniazid, lidokain, lorazepam, salisilat, varfarin, nitrazepam). Diğer şıklar PDF'e uygun."),
        Q("22-23", 27, "Eliminasyonla ilgili hangisi YANLIŞTIR? (GF · salya · tübülüs taşıyıcıları · halotan · reabsorpsiyon)", "b) Alkol, barbitürat ve bromürler salya içine geçerek atılır",
          "Salya ile atılanlar: iyodürler, bromürler, lityum. GF pasif diffüzyon; anyonik+katyonik taşıyıcı; halotan hızlı; reabsorpsiyon itrahı azaltır."),
    ],
)
