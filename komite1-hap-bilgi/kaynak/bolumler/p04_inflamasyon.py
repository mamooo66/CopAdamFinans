# -*- coding: utf-8 -*-
"""Kaynak: Drive › Komite-1 › PDF › Patoloji › 2026-2027(yeni) › Selma Erdoğan Düzcü › 3-AKUT VE KRONİK İNFLAMASYON
(NOT: Drive okuma aracı metni 79. slaytta — araşidonik asit / siklooksijenaz yolu — kesti; PDF 11,7 MB olduğundan indirme de yapılamadı.
Bu modül yalnızca okunabilen slayt 1-79 metninden hazırlandı; devamı eklenecek.)"""

from yardim import B, C, Q  # noqa: F401

_KESIK = " · (PDF metni kesik; doğrulanamadı)"

BOLUM = dict(
    key="inflamasyon", baslik="Akut ve Kronik İnflamasyon",
    hoca="Doç. Dr. Selma Erdoğan Düzcü", tarih="22-24 Eylül", saat="5 saat",
    kaynak="3-AKUT VE KRONİK İNFLAMASYON · Doç. Dr. S. E. Düzcü · 2026",
    ozet=["Son 5 yılda bu dersten **10 resmi + 1 hatırlanan soru**: akut tarafta **hücresel olaylar** (selektin, hücre içi öldürme), "
          "**TLR / inflammazom**, akut faz sitokinleri, morfolojik paternler; kronik tarafta **granülom, dev hücre, kronik iltihap hücreleri**.",
          "Tuzaklar: **selektin = gevşek yapışma + yuvarlanma** (sıkı adezyon = integrin) · **marjinasyon = duvara (periferiye) yaklaşma** · "
          "**CD31 = transmigrasyon** (kemotaksis değil) · **ROT / NO / granül enzimleri = hücre içi öldürme** · "
          "**inflammazom = DAMP, sitozol** (TLR = PAMP) · **histamin hücre kökenli**, **TXA₂ vazokonstriktör**.",
          "**Eksik kısım:** PDF metni 79. slaytta (siklooksijenaz yolu) kesildi; diğer mediatörler, morfolojik paternler ve kronik "
          "inflamasyon bu modülde yok. Bu bölümlerin sorularında “PDF metni kesik” notu vardır."],
    slaytlar=[
        # ---------------------------------------------------------------- 1
        [
            C("İnflamasyon (iltihap, yangı) — tanım ve amaç", [
                B("Vaskülarize dokuların enfeksiyon ve doku hasarına karşı **koruyucu yanıtı**: normalde kan dolaşımında olan "
                  "**lökositleri ve plazma proteinlerini** hasar yerine getirir."),
                B("Amaç: zedelenmeye yol açan **nedeni** (mikroorganizma, toksin) ve zedelenmeden doğan **nekrotik hücre/dokuları** "
                  "ortadan kaldırmak; enfeksiyonu **sınırlamak**, yarayı **iyileştirmek**."),
                B("Etken ve ona bağlı doku zararı: yerinde **eritilmeye**, vücut dışına **atılmaya**, **sınırlandırılarak (demarkasyon)** "
                  "ayrı tutulmaya çalışılır."),
                B("Organ/doku adına **-it / -itis** eki getirilir (apandisit, konjonktivit, menenjit)."),
            ]),
            C("İnflamasyonun nedenleri", [
                B("**1-** Enfeksiyonlar (bakteriyel, fungal, viral, parazitik) · **2-** Doku nekrozu · **3-** Yabancı cisimler · "
                  "**4-** İmmün reaksiyonlar · **5-** Travma"),
                B("Ayrıca toksinler ile fiziksel ve kimyasal etkenler."),
            ]),
            C("İki ana form: akut ve kronik inflamasyon", [
                B("**Akut**: **kısa süreli** (birkaç dakika – birkaç gün); **plazma sıvı ve protein eksüdasyonu** + belirgin "
                  "**nötrofil lökosit (PNL)** birikimi.", y="23-24"),
                B("**Kronik**: daha uzun (**günler – yıllar**); histolojik olarak **lenfosit, plazmosit ve makrofaj** toplanması, "
                  "**doku yıkımı ve onarımı**; onarım **vasküler proliferasyon ve fibrozis** ile birliktedir.", y="23-24"),
                B("Başlangıç uyaranı, plazma/hücrelerden vasküler ve hücresel yanıtı düzenleyen **kimyasal mediatörlerin** salınımını "
                  "tetikler; mediatörler yanıtı **güçlendirir**."),
                B("Yanıt, hasar verici uyaran kalkınca ve mediatörler dağılıp **katabolize/inhibe** edilince sonlanır."),
            ]),
        ],
        # ---------------------------------------------------------------- 2
        [
            C("Sonlanma, onarım ve zarar potansiyeli", [
                B("Zararlı ajan elimine edilince inflamasyon **sonlanır**; zedelenen dokunun yeniden yapılanması için olaylar başlar "
                  "(inflamasyon **onarımla iç içedir**)."),
                B("Onarım: doku **rejenere yerli parankimal hücrelerle** yer değiştirir **ya da** defekt **fibroblastik nedbe** ile dolar "
                  "(**nedbeleşme**)."),
                B("Hasar potansiyeli: **romatoid artrit**, **ateroskleroz** ve böcek ısırması/ilaca **anaflaktik yanıt** zemininde de iltihabi yanıt vardır."),
                B("**Perikard**ta bakteriyel inflamasyon sonrası **skarlaşma** kalbi kalın **fibröz** dokuyla sarar → **daimi kalp fonksiyon bozukluğu**."),
                B("İnflamasyon olmazsa: enfeksiyonlar **kontrolsüz** kalır, yaralar iyileşmez, hasarlı doku **kronikleşir**."),
            ]),
            C("Tanıma: inflamasyonun ilk adımı", [
                B("İlk adım: mikroorganizma ve nekrotik hücrelerin **hücresel reseptörler** ve **dolaşan proteinler** tarafından "
                  "**tanınması**; mikroplar ve ölü hücreler **tehlike sinyali** verir.", y="21-22"),
                B("Sinyalleri alan reseptörler **fagositlerde, dendritik hücrelerde** ve **epitel hücrelerinde** bulunur."),
                B("3 grup: **1- Toll-benzeri reseptörler (TLR)** · **2- İnflammazom** · **3- Dolaşan proteinler**."),
            ]),
            C("3- Dolaşan proteinler", [
                B("Plazma proteinleri mikroorganizmaları tanır; kanla gelen mikropları **öldürmek** ve enfeksiyonu uyarmak üzere işlev görür."),
                B("**Kompleman sistemi** (inflamasyon mediatörlerini üretir) · **Mannoz bağlayan lektin** (mikrobiyal şekerleri tanır) · "
                  "**Kollektinler** (mikroorganizmayı tanır, fagositoz yapar)."),
            ]),
        ],
        # ---------------------------------------------------------------- 3
        [
            C("1- Toll-benzeri reseptörler (TLR) — mikroorganizma reseptörleri", [
                B("**Plazma membranında ve endozomlarda** bulunur → **hücre içi ve hücre dışı** mikropları fark eder; **10 tane TLR** vardır.",
                  y="22-23", tuzak="“DAMP'ları tanıyan sitozolik reseptör = Toll benzeri reseptör” → YANLIŞ (doğrusu inflammazom)"),
                B("Birçok organizmada ortak **PAMP**'ları (pathogen-associated molecular patterns) tanır.", y="21-22"),
                B("Aktivasyon → **transkripsiyon faktörü** → **inflamasyon mediatörleri**, **antiviral sitokinler (interferon)**, "
                  "lenfosit aktivasyon proteinleri (**IL-1β**) → lökositler inflamasyon yerinde toplanır."),
                B("Şekil: TLR ürünü sitokinler (örn. **TNF**) → **adezyon molekülü ekspresyonunda artış** → akut inflamasyon."),
                B("Sitoplazmadaki ve membrandaki **TLR-dışı** ailelerin reseptörleri de farklı mikrop sınıflarının ürünlerini tanır (şekil)."),
            ]),
            C("2- İnflammazom — hücre hasarı sensörleri", [
                B("Tüm hücrelerde, hasar sonucu salınan/değişen **DAMP**'ları (damage-associated molecular patterns) tanıyan "
                  "**sitozolik reseptörler** vardır.", y="22-23"),
                B("Sinyaller: **ürik asit** (DNA yıkım ürünü) · **ATP** (hasarlı mitokondriden) · **azalmış intrasellüler K⁺** "
                  "(membran hasarıyla iyon kaybı) · **DNA** (sitoplazmaya salınınca).", lvl=1),
                B("Reseptörler **IL-1 yapımını uyaran** multiprotein sitozolik kompleks = **inflammazom**'u aktive eder → **kaspaz-1** aktifleşir "
                  "→ **IL-1** aktifleşir → lökositleri toplar, inflamasyonu uyarır."),
                B("Yapı (şekil): **NLRP3** (lösin bakımından zengin sensör protein) + adaptör + **kaspaz-1** (inaktif → aktif). "
                  "**Fagolizozomla karıştırılmamalı.**"),
                B("Tetikleyiciler (şekil): hücre-dışı ATP, K⁺ çıkışı, ROT, **endojen kristaller** (MSU, CPP, kolesterol), **eksojen kristaller** "
                  "(şap, asbest). MSU: monosodyum ürat; CPP: kalsiyum pirofosfat.", lvl=1),
            ]),
        ],
        # ---------------------------------------------------------------- 4
        [
            C("Akut inflamasyon — genel", [
                B("Zedelenmeye karşı **ani ve erken** yanıt. İşlevi: zararlı etkenin **tanınması** → lökositlerin **toplanması** → etkenin "
                  "**ortadan kaldırılması** → yanıtın **düzenlenmesi** → **rezolusyon (onarım)**."),
                B("Sonuç: uyaran kalkar → yanıt azalır → doku onarılır; **ya da** zedelenme sürer → **kronik inflamasyon**."),
                B("2 ana bileşen: **1- Vasküler değişiklikler** (vazodilatasyon, damar duvarında geçirgenlik artışı) · "
                  "**2- Hücre olayları** (lökosit göçü, lökosit aktivasyonu)."),
                B("**5 klasik bulgu**: sıcaklık (**calor**) · kızarıklık (**rubor**) · şişme (**tumor**) · ağrı (**dolor**) · fonksiyon kaybı (**functio laesa**)."),
            ]),
            C("Vasküler akım ve çap değişiklikleri", [
                B("**Vazodilatasyon**: mediatörlerin, özellikle **histaminin** damar düz kasına etkisiyle (geçici vazokonstriksiyonu takip edebilir); "
                  "**arterioller ilk etkilenir**."),
                B("Lokal kan akımı artışı → **kızarıklık (eritem)** ve **sıcaklık**."),
                B("Sonra küçük damarlarda **permeabilite artışı** + ekstravasküler dokuya **proteinden zengin sıvı eksüdasyonu** → eritrositler "
                  "konsantre, **viskozite artar**, dolaşım yavaşlar."),
                B("Mikroskopide **içi eritrositle dolu çok sayıda dilate küçük damar** = **staz**."),
            ]),
            C("Vasküler permeabilite artışı", [
                B("Vazodilatasyon + artmış kan akımı → **intravasküler hidrostatik basınç** ↑ → kapillerlerden sıvı filtrasyonu ↑."),
                B("**Transüda**: plazma ultrafiltratı, **çok az protein**. Permeabilite artışıyla proteinden zengin sıvı ve hücrelerin bile geçtiği "
                  "**eksüdasyona (eksüda)** dönüşür."),
                B("Plazmadan protein kaybı → **vasküler ozmotik basınç ↓**, **interstisyel ozmotik basınç ↑** → su ve iyonlar dışarı çıkıp birikir = **ödem**."),
            ]),
        ],
        # ---------------------------------------------------------------- 5
        [
            C("Endotel sızıntısı — 3 mekanizma", [
                B("**1- Endotel hücre retraksiyonu (büzülmesi)**: permeabilite artışının **en sık** nedeni; **intersellüler aralıklar** genişler."),
                B("**Histamin, bradikinin, lökotrienler** vb. ile düzenlenir; **reversibl**, kısa süreli (**ani geçici yanıt**); esas olarak "
                  "**postkapiller venüllerde**.", lvl=1),
                B("**2- Direkt endotel hasarı**: endotel hücre **nekrozu** → hücreler ayrılır; genellikle **ağır zedelenmelerde** (yanık, enfeksiyon); "
                  "sıklıkla **trombosit adezyonu ve tromboz** eşlik eder."),
                B("**3- Yeni damar oluşumu (sızıntı) — transitoz**: sıvı/proteinin endotel hücreleriyle artan taşınması (**intrasellüler "
                  "vezikülovakuolar yol**); özellikle **VEGF** gibi mediatörlere maruz kalınca."),
            ]),
            C("Akut inflamasyonda lenf damarları", [
                B("**Lenf akışı artar**: hücre artıkları, ödem sıvısı ve lökositlerin damar dışı aralıktan boşalmasına yardım eder."),
                B("Şiddetli inflamatuar yanıtta lenf damarları mikroorganizmayı **lenf bezlerine** taşıyıp **yayılmasına katkı** sağlar."),
                B("Lenf kanallarında/bezlerinde sekonder inflamasyon: **lenfanjit** ve **lenfadenit**."),
            ]),
            C("Lökositlerin damar dışına çıkışı — hücresel olaylar", [
                B("**1- Marjinasyon ve yuvarlanma** · **2- Adezyon** · **3- Endotel hücreleri arasından transmigrasyon** · "
                  "**4- Kemotaktik uyarıyı izleyerek migrasyon** · **5- Fagositoz ve degranülasyon**.",
                  y="24-25", tuzak="“Hücre olaylarından ilk olarak fagositoz gerçekleşir” → YANLIŞ"),
                B("Özet: rolling → **selektinler** · adezyon → **integrinler ↔ ICAM, VCAM** · transmigrasyon (diapedez) → **postkapiller venüller** · "
                  "kemotaksis → **IL-8, C5a, LTB4**, bakteriyel ürünler."),
                B("Fagositoz → **opsonizasyon (IgG, C3b)** kolaylaştırır; mikrop öldürme: **ROS, NO, lizozomal enzimler**."),
            ]),
        ],
        # ---------------------------------------------------------------- 6
        [
            C("1- Marjinasyon ve yuvarlanma (rolling)", [
                B("Normal akımda eritrosit ve lökositler **merkezden** ilerler; erken inflamasyonda permeabilite artar, sıvı lümenden çıkar, **akım yavaşlar**."),
                B("Lökositler **santral bölgeden ayrılıp lümenin periferine (damar duvarına)** göç eder = **marjinasyon**.",
                  y="24-25", tuzak="“Marjinasyonda nötrofiller damar duvarından uzaklaşarak santral bölgeye yakınlaşır” → YANLIŞ"),
                B("Sonra endotel yüzeyinde **geçici yapışarak yuvarlanırlar** = **yuvarlanma (rolling)**; anahtar-kilit benzeri **adezyon molekülleri** bağlanır."),
                B("**Geçici ve gevşek adezyon + yuvarlanma → selektin ailesi**; selektinler **şekerleri bağlayan ekstrasellüler bölgeli** reseptörlerdir.",
                  y="24-25"),
            ]),
            C("Selektinler", [
                B("**E-selektin (CD62E, ELAM-1)**: **endotelde**; **sitokin veya endotoksin** uyarımıyla oluşur; lökosit adezyonuna yol açar."),
                B("**P-selektin (CD62P, GMP140)**: **trombosit ve endotelde** (endotelde **Weibel-Palade cisimciklerinde**); **histamin ve trombin** ile "
                  "**birkaç dakikada** yüzeye çıkar → yuvarlanmada önemli."),
                B("**L-selektin (CD62L, LAM-1)**: **lökosit yüzeyinde**; lenfosit ve lökosit toplanmasında rol alır."),
                B("Endotelde beliren selektinler, nötrofil yüzeyindeki **Sialyl Lewis X (CD15s)** ile **zayıf bağ** kurar → nötrofil **yavaşlar ve yuvarlanır**."),
            ]),
            C("2- Adezyon (sıkı yapışma)", [
                B("Selektin–Sialyl Lewis X bağıyla yavaşlayan nötrofil **daha geniş yüzeyle endotele oturur**."),
                B("**İntegrinler**: lökositlerin endotele, hücrelerin ECM'e yapışmasına aracılık eden **heterodimerik transmembran glikoproteinler** "
                  "(ECM'de reseptör görevi görür)."),
                B("**Daha kuvvetli bağ**: nötrofil **integrinleri** ↔ endotel hücrelerinin immunglobulin yapısındaki **ICAM-1** ve **VCAM-1** reseptörleri."),
                B("Bu bağ lökositi endotelde **sabitler** = **lökosit adezyonu**; nötrofil **hareketsiz** durur. **ICAM-1** için ana integrinler: "
                  "**LFA-1 (CD11a/CD18)** ve **Mac-1 (CD11b/CD18)**."),
            ]),
        ],
        # ---------------------------------------------------------------- 7
        [
            C("3- Transmigrasyon (diapedez, emigrasyon)", [
                B("Hareketsiz nötrofil, endotel hücreleri arasından **ameboid hareketlerle** geçip damar dışına çıkar; nötrofil ve endotel yüzeyindeki "
                  "**CD31 (PECAM-1)** reseptörleri önemli rol oynar.",
                  y="24-25", tuzak="“CD31 kemotaksisi gerçekleştirir” → YANLIŞ"),
                B("Özellikle **postkapiller venüllerde** olur."),
                B("Akut inflamasyonun birçok tipinde ilk **6-24 saatte nötrofiller** baskın, sonraki **24-48 saatte monositler** lehine değişir "
                  "(adezyon molekülleri ve kemotaktik faktörlerin sırayla salınımı)."),
                B("Nötrofiller damar dışında **24-48 saatte apopitoza** uğrar; monositler **doku makrofajı** olarak daha uzun yaşar."),
            ]),
            C("4- Kemotaksis ve aktivasyon", [
                B("Ekstravazasyondan sonra lökositlerin **kimyasal uyaranı izleyerek** zedelenme bölgesine göçü = **kemotaksis**; ekzojen ve endojen maddeler "
                  "kemotaktik ajan olabilir."),
                B("**Kemotaktik ajanlar**: **a-** bakteriyel ürünler · **b-** kompleman, özellikle **C5a** · **c-** AA metabolizmasının **lipooksijenaz yolu**, "
                  "özellikle **LTB4** · **d-** sitokinler, özellikle **kemokin** ailesi (**IL-8**)."),
                B("**Kemokinler**: inflamasyon yerinde birçok hücrenin salgıladığı, endotel yüzeyindeki **kemoatraktan sitokinler**; lökositler kemokinle "
                  "karşılaşınca **aktive** olur."),
                B("**TNF ve IL-1** gibi sitokinler **endotel hücrelerini aktive eder**."),
            ]),
            C("Kemotaksis — hücre içi mekanizma", [
                B("Kemotaktik ajan → lökosit reseptörü → **fosfolipaz C** → fosfolipit metabolitleri (fosfatidil inozitol, digliserol) → **intrasellüler Ca²⁺** ↑."),
                B("Artmış sitozolik Ca²⁺, hücre iskeleti **kontraktil elemanlarını** harekete geçirir."),
                B("Lökosit **psödopod** çıkarıp ara maddeye tutunur, **ameboid** ilerler; akut iltihapta gelişen **ödem** bu hareketi kolaylaştırır."),
            ]),
        ],
        # ---------------------------------------------------------------- 8
        [
            C("4. Fagositoz ve degranülasyon", [
                B("Fagositoz ve lizozomal enzim salınımı, inflamasyon alanında lökosit birikimiyle gerçekleşir. **3 ilişkili aşama**:"),
                B("**A-** lökositin partikülü **tanıması ve tutunması** · **B-** **fagositik vakuol** oluşturmak üzere **kuşatması** · "
                  "**C-** yutulan materyalin **öldürülmesi ve parçalanması**.", lvl=1),
                B("Tanıma/tutunma: **mannoz reseptörleri**, **çöpçü (scavenger) reseptörleri** ve **opsonin** denen serum proteinleriyle kaplanma; "
                  "opsoninler lökositteki spesifik reseptörlere bağlanır."),
                B("**Nötrofiller yalnızca opsonin ile işaretli** antijen veya hücreleri fagosite eder."),
            ]),
            C("Opsoninler ve opsonin reseptörleri", [
                B("**Opsoninler**: **IgG** antikorları · kompleman aktivasyonunun **C3b** yıkım ürünü · plazma lektinleri (özellikle **mannoz bağlayıcı lektin**)."),
                B("**Reseptörler**: IgG için **Fc reseptörü** · kompleman fragmanları için **CR1 ve CR3** · kollektinler için **C1q**."),
                B("Opsonin reseptörleri, opsoninle kaplı mikropların **hızlı fagositozunu** kolaylaştırır."),
            ]),
            C("Fagolizozom ve degranülasyon", [
                B("**Psödopodlar** partikülü kuşatmak için yayılır → **fagositik vakuol**; vakuol membranı **lizozomal granül membranı** ile kaynaşır."),
                B("Granül içeriği **fagolizozom**a boşalır = lökosit **degranülasyonu**. Son aşama: mikropların **öldürülmesi ve parçalanması**."),
            ]),
        ],
        # ---------------------------------------------------------------- 9
        [
            C("Mikroorganizmaların hücre içinde yok edilmesi", [
                B("**1- Reaktif oksijen türevleri (ROT / ROS)** · **2- Nitrik oksit (NO)** · **3- Granül enzimleri ve diğer proteinler**.", y="25-26"),
                B("Öldürme geniş ölçüde **ROT** ile olur; **ROT ve lizozom enzimleri** en önemli **mikrobisid** maddelerdir.",
                  y="24-25", tuzak="“Reaktif oksijen türevleri nötrofilin damar dışına çıkışını sağlar” → YANLIŞ"),
                B("Fagositoz → **oksidatif patlama**: ani ↑ **oksijen tüketimi**, **glikojenoliz**, ↑ glikoz oksidasyonu, ROT üretimi."),
                B("Lökosit **NADPH oksidaz** hızla aktive olur → **süperoksit** → **H₂O₂**; H₂O₂ + **myeloperoksidaz (MPO)** → **HOCl** (hipoklorus radikali) "
                  "ve **NaOCl**: güçlü oksidan ve antimikrobiyal ajanlar."),
            ]),
            C("Nitrik oksit (NO)", [
                B("**Nitrik oksit sentaz (NOS)** ile **argininden** üretilen, çözünebilir bir gaz; NO türevleri de **ROT gibi** etki eder."),
                B("3 NOS: **eNOS** (endotelyal) · **iNOS** (indüklenebilir; **mikrobiyal öldürmede etkili**) · **nNOS** (nöronal)."),
            ]),
            C("Granül enzimleri", [
                B("Nötrofillerde **2 tip granül**: **1- Spesifik (sekonder, küçük)**: lizozim, kollejenaz, jelatinaz, laktoferrin, histaminaz, alkalen fosfataz."),
                B("**2- Azurofilik (primer, büyük)**: **MPO**, bakterisidal faktörler, asit hidrolazlar, nötral proteazlar."),
                B("Fagositik veziküller bu granüllerle birleşip yutulanı ortadan kaldırır; ölü mikroorganizmalar **lizozomal asit hidrolazlarla** parçalanır."),
                B("**Elastaz**, bakteri öldürmede en önemli enzimlerdendir."),
                B("Oksidatif yanma olmadan da öldürenler: **BPI** (bakterisidal permeabilite arttırıcı protein), **lizozim, laktoferrin, major bazik protein, "
                  "defensinler** → mikrop membranında **delikler** açar."),
                B("Lizozomal enzimler yalnız fagolizozoma değil **ekstrasellüler boşluğa** da çıkar → **doku hasarı ve matriks parçalanması**."),
            ]),
        ],
        # ---------------------------------------------------------------- 10
        [
            C("Nötrofil ekstrasellüler tuzakları (NET)", [
                B("**Hücre dışı fibriler ağlar**: antimikrobiyal maddeleri enfeksiyon bölgesinde yoğunlaştırır, mikroorganizmaları **hapsedip yayılmasını engeller**."),
                B("**Viskoz nükleer kromatin ağı** + granül proteinleri (antimikrobiyal peptit ve enzimler); **fagositozdan bağımsız** hücre öldürür."),
                B("Oluşurken nötrofilin **çekirdeği kaybolur, hücre ölür**. **Sepsiste kanda** saptanabilir."),
            ]),
            C("Lökosit fonksiyon bozuklukları — 1. Adezyon", [
                B("Genetik veya edinsel bozukluklar → **tekrarlayıcı ve hayatı tehdit edici enfeksiyonlara** eğilim."),
                B("**LAD-1**: lökosit integrinlerinin (**LFA-1, Mac-1**) **CD18** alt grubunda **sentez bozukluğu** → endotel adezyonu düzgün olmaz."),
                B("**LAD-2**: aktive endoteldeki selektinlere bağlanan oligosakkarit **Sialyl Lewis X yok** → nötrofiller selektine bağlanamaz, **rolling yapamaz**."),
            ]),
            C("2- Kemotaksis veya fagositoz bozuklukları", [
                B("**Chediak-Higashi sendromu**: **OR**; **mikrotübül düzeninde bozukluk** → lökosit hareket yetmezliği + fagozom içine "
                  "**lizozomal degranülasyon** bozukluğu; tekrarlayan ciddi enfeksiyonlar."),
                B("**Job sendromu**: nötrofilin **kemotaktik ajana yanıtı bozuk**, ajanları takip edemez → olay yerinde akut iltihap tam gelişmez "
                  "(**soğuk abse**)."),
            ]),
            C("3- Mikrobisidal aktivite · 4- TLR · 5- İnflammazom bozuklukları", [
                B("**Kronik granülomatöz hastalık (CGD)**: **süperoksit** yapan **NADPH oksidaz** komponentlerinden birinin **genetik eksikliği**; "
                  "bakteri kuşatılınca **oksijene bağlı öldürme** mekanizmaları aktive olmaz."),
                B("**TLR sinyal yolaklarında mutasyon** → enfeksiyonlara **aşırı duyarlılık**."),
                B("**İnflammazom** bileşenlerini kodlayan genlerde mutasyon → **kriyopirine eşlik eden periyodik ateş sendromları (CAPS)**: "
                  "**düşmeyen ateş** ve inflamasyon belirtileri."),
            ]),
        ],
        # ---------------------------------------------------------------- 11
        [
            C("Kimyasal mediatörler — genel özellikler", [
                B("**A-** Plazma proteinlerinden veya hücrelerden **lokal** üretilir."),
                B("**Plazma kökenli** (kompleman, kininler, pıhtılaşma faktörleri): dolaşımdaki **prekürsörler** **proteolitik ayrılma** ile aktive olur.", lvl=1),
                B("**Hücre kökenli**: genellikle **intrasellüler granüllerde** (mast hücresinde **histamin**); gerektiğinde salınır veya uyarıya yanıt "
                  "**de novo** sentezlenir (**prostaglandinler** gibi).", lvl=1, y="25-26"),
                B("**B-** Çoğu, hedef hücrelerdeki **spesifik reseptörlere** bağlanarak etki eder."),
                B("**C-** Hedef hücreleri **ikincil mediatör** salgılatır; bunlar ilk uyarıyı güçlendirir **veya** tersi etkiyle kontrol altına alır."),
                B("**D-** İşlevleri **sıkı düzenlenir**: salınınca çoğu hızla azalır (**AA metabolitleri**), enzimle inaktive olur (**bradikinin – kininaz**) veya elimine edilir."),
            ]),
            C("Hücre kökenli mediatörler — 1. Vazoaktif aminler: Histamin", [
                B("Dokularda özellikle **damar çevresindeki mast hücrelerinde**; ayrıca dolaşımdaki **bazofil ve trombositler**de. **Hazır** histamin mast hücre granüllerindedir.",
                  y="25-26", tuzak="“Histamin plazma kökenli mediatördür ve arteriollerde vazokonstrüksiyon yapar” → YANLIŞ"),
                B("Salgılatan uyaranlar: **1)** fiziksel zedelenme (**travma, ısı**) · **2)** **IgE**'nin mast hücresi **Fc reseptörlerine** bağlanmasıyla immün "
                  "reaksiyonlar · **3)** **C3a ve C5a** (anafilatoksinler)", lvl=1),
                B("**4)** lökosit kökenli histamin salgılatıcı proteinler · **5)** **nöropeptitler** (P maddesi vb.) · **6)** bazı sitokinler (**IL-1, IL-8**).", lvl=1),
                B("Etki: **arteriollerde dilatasyon**, **venüllerde permeabilite artışı** (venülde endotel kontraksiyonu, interendotelyal bağlantıların genişlemesi); "
                  "mikrodolaşımda esas olarak **H1 reseptörü**.", y="25-26"),
                B("Salınımdan hemen sonra **histaminaz** ile inaktive edilir."),
            ]),
            C("Serotonin (5-hidroksitriptamin)", [
                B("Histamin benzeri etkili **vazoaktif mediatör**; primer olarak **trombosit** ve **enterokromafin (nöroendokrin) hücrelerde**."),
                B("**Trombosit agregasyonu** ile salınır; **pıhtılaşma sırasında vazokonstriksiyon** yapar."),
            ]),
        ],
        # ---------------------------------------------------------------- 12
        [
            C("2- Araşidonik asit (AA) metabolitleri — eikozanoidler: prostaglandinler ve lökotrienler", [
                B("**20 karbonlu** yağ asitlerinden oluştuğu için **eikozanoidler**; **inflamasyon ve hemostaz** dahil birçok olayı etkiler."),
                B("AA normalde **membran lipitinin parçası**; **fosfolipaz A2** aktivasyonuyla ortama salınır."),
                B("**Kısa ömürlü hormonlar** gibi: yapıldıkları yerde **lokal** etki eder, sonra çok hızlı (spontan veya enzimatik) yok edilir."),
                B("Reaksiyonu başlatan enzimin adıyla anılan **2 ana yol** vardır."),
            ]),
            C("A- Siklooksijenaz yolu", [
                B("Ürünler: **PGE2, PGD2, PGF2α, PGI2 (prostasiklin)** ve **tromboksan (TXA2)**."),
                B("Prostaglandinler **mast hücreleri, makrofajlar, endotel** ve birçok hücrede üretilir; her biri **spesifik enzim** etkisiyle oluşur."),
                B("**Trombositlerde tromboksan sentetaz** vardır. **TXA2**: güçlü **trombosit agregan** ve **vazokonstriktör** ajan.",
                  y="25-26", tuzak="“Tromboksan A2 damarlarda vazodilatasyon yapar” → YANLIŞ"),
            ]),
        ],
    ],
    sorular=[
        Q("25-26", 68, "Akut inflamasyonda ROS, nitrik oksit ve granül enzimleri hangi hücresel olayda etkin?",
          "Mikroorganizmaların hücre içinde yok edilmesi",
          "Adezyon (integrin), marjinasyon, kemotaksis, yuvarlanma (selektin) değil"),
        Q("25-26", 69, "Akut ve kronik inflamasyon reaksiyonlarıyla ilgili doğru olan?",
          "IL-1 ve TNF sistemik akut faz reaksiyonlarını uyarır",
          "Yanlışlar: granülomatöz akut patern · histamin plazma kökenli/vazokonstriktör · TXA₂ vazodilatatör · süpüratif kronik" + _KESIK),
        Q("25-26", 78, "Akciğerde kazeifikasyon nekrozlu TB granülomundaki multinükleer dev hücreler hangi hücrelerden oluşur?",
          "Epiteloid histiositler",
          "Lenfosit, mast hücresi, fibroblast, atipik tümör hücresi değil" + _KESIK),
        Q("24-25", 71, "Akut inflamasyonun hücresel olaylarıyla ilgili doğru olan?",
          "Gevşek adezyon ve yuvarlanma selektin ailesi tarafından gerçekleştirilir",
          "Çeldiriciler: ilk olay fagositoz · marjinasyonda santrale · CD31 kemotaksis (CD31 = transmigrasyon) · ROS damar dışına çıkış"),
        Q("24-25", 72, "Hangi hastalıktaki morfolojik patern kronik inflamasyona örnektir?",
          "Tüberkülozda görülen granülomatöz inflamasyon",
          "Seröz (yanık), süpüratif (stafilokok), abse, akut peptik ülser = akut" + _KESIK),
        Q("23-24", 63, "Akut faz reaksiyonlarını uyaran en önemli iki sitokin?",
          "TNF-α ve IL-1",
          "Histamin-serotonin, NO-ROS, C3-C5, fibrinojen-plazmin değil" + _KESIK),
        Q("23-24", 64, "Kronik nonspesifik kolit biyopsisinde lamina propriada hangi hücre GÖRÜLMEZ?",
          "Nötrofil",
          "PDF: kronik = lenfosit, plazmosit, makrofaj; nötrofil = akut (eozinofil: PDF metni kesik)"),
        Q("22-23", 62, "DAMP'ları tanıyan sitozolik reseptör?",
          "İnflammazom",
          "TLR (PAMP; membran/endozom), integrin, marjinasyon, bradikinin değil"),
        Q("22-23", 63, "Akut inflamasyonun morfolojik paternleri arasında yer ALMAYAN?",
          "Granülomatöz inflamasyon",
          "Ülserasyon, pürülan, seröz, fibrinöz = akut" + _KESIK),
        Q("22-23", 74, "Pilonidal sinüste kıl kesitlerini çevreleyen multinükleer hücrelerin kökeni?",
          "Makrofaj",
          "Yabancı cisim tipi dev hücre" + _KESIK),
        Q("21-22", None, "TLR reseptörleri inflamasyonun hangi aşamasında kullanılır?",
          "Yabancı maddelerin (mikropların) tanınması",
          "Öğrenci hatırlamasından derlenmiş soru"),
    ],
)
