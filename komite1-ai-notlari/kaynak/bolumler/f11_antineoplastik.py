# -*- coding: utf-8 -*-
"""Kaynak: Drive › Komite-1 › PDF › Farmakoloji › 2026-2027(yeni) › Oruç Yunusoğlu › 7-Antineoplastik ilaçlar + 8-Antineoplastik ilaçlar(Ek slayt içerir)"""

from yardim import B, C, Q  # noqa: F401

BOLUM = dict(
    key="antineoplastik", baslik="Antineoplastik İlaçlar",
    hoca="Doç. Dr. Oruç Yunusoğlu", tarih="2 Ekim", saat="3 saat",
    kaynak="7-Antineoplastik ilaçlar + 8-Antineoplastik ilaçlar (Ek slayt) · O. Yunusoğlu · 2026",
    ozet=["Son 5 yılda bu dersten **11 soru** çıktı (25-26: 2, 24-25: 2, 23-24: 4, 22-23: 2, 21-22: 1) — çoğu **tek ilaç–tek özellik** eşleştirmesi.",
          "Tekrarlayanlar: **amifostin** (sisplatinin kümülatif nefrotoksisitesi antidotu; 22-23 ve 23-24), **siklofosfamid** (steril hemorajik sistit), **doksorubisin** kardiyotoksisitesi, **allopurinol ↔ purin antimetabolitleri**, **sisplatin** (akut tübüler nekroz).",
          "Tuzaklar: **L-asparaginaz kemik iliği depresyonu yapmaz**; SSS'ne geçen ilaçlar (nitrozüreler, prokarbazin, dakarbazin, etopozid, tenopozid) listesinde **vinkristin yok**; karsinojenite **↑ alkilleyiciler / ↓ antimetabolitler**."],
    slaytlar=[
        # 1 — kanser biyolojisi
        [
            C("Etkenler ve kalıtsal yatkınlık", [
                B("**Karsinojenik etkenler**: kimyasal karsinojenler, **iyonizan radyasyon**, **onkojenik virüsler**, diğer çevresel etkenler."),
                B("**Kalıtsal yatkınlık**: germ hattı mutasyonları, kalıtsal kanser sendromları (örn. **BRCA1, BRCA2, APC, TP53**)."),
                B("**Genetik ve epigenetik değişiklikler**: kritik genlerde mutasyonlar ve ekspresyon değişiklikleri."),
            ]),
            C("Üç gen grubu", [
                B("**Proto-onkogenlerin aktivasyonu (onkogenler)**: hücre çoğalması ve sağkalımda artış — **RAS, MYC, ERBB2 (HER2)**."),
                B("**Tümör baskılayıcı genlerin işlev kaybı**: çoğalma kontrolünün kaybı, apoptozda azalma — **TP53, RB1, APC**."),
                B("**DNA onarım genlerinin işlev kaybı**: genomik kararsızlık, yeni mutasyonların birikmesi — **BRCA1, BRCA2, MLH1, MSH2**."),
            ]),
            C("Hücresel kontrolün bozulması → tümör ilerlemesi", [
                B("Hücre döngüsü kontrol noktalarının işlev kaybı → **kontrolsüz hücre çoğalması**."),
                B("**Apoptozdan kaçış** ve DNA hasarına karşı yanıtın bozulması → **klonal genişleme** ve tümör gelişimi."),
                B("**Tümör ilerlemesi**: **anjiyogenez** (vasküler büyüme faktörleri; örn. VEGF, MMP'ler), çevre dokulara **invazyon**, uzak organlara **metastaz** → **malign tümör**."),
            ]),
        ],
        # 2 — tanım, epidemiyoloji, ilke
        [
            C("Malign tümör (kanser) ve küresel epidemiyoloji", [
                B("**Kanser**: hücrelerin **kontrolsüz çoğalması**, çevre dokulara **invazyon** ve uzak organlara **metastaz** yapabilmesi ile karakterize, çok sayıda hastalığı kapsayan **hastalık grubu**."),
                B("**GLOBOCAN 2022 (IARC)**: dünyada 2022'de yaklaşık **20 milyon yeni kanser vakası** ve **9,7 milyon kansere bağlı ölüm**."),
                B("Küresel ölçekte önemli **morbidite ve mortalite** nedenidir."),
            ]),
            C("En sık kanserler (GLOBOCAN 2022; tüm yeni vakalar içindeki oran)", [
                B("**Erkeklerde**: akciğer **%15,3** · prostat **%14,2** · kolorektal **%10,4** · mide **%6,1** · karaciğer **%5,8**."),
                B("**Kadınlarda**: meme **%23,8** · akciğer **%9,4** · kolorektal **%8,9** · serviks **%6,8** · tiroid **%6,4**."),
            ]),
            C("Antineoplastik tedavinin ana ilkesi ve genel özellikleri", [
                B("**Ana ilke**: hastanın/konakçının **normal hücrelerine zarar vermeksizin** tümör hücresinin büyümesini ve çoğalmasını **durdurmak**, mümkünse **yok etmek**."),
                B("Genel özellikler: **↓ selektivite**, **antiproliferatif** etki, **immünosupresif** etki, **↓ terapötik indeks**, **mutajenik, teratojenik, karsinojenik** etkiler."),
            ]),
        ],
        # 3 — hücre siklusu 1
        [
            C("Hücre siklusu fazları (slayt şeması)", [
                B("**G0 (dinlenme fazı, hücresel siklus dışı)**: kemoterapiye **en dirençli faz**; bazı tümör hücreleri uzun süre G0'da kalabilir."),
                B("**G1** (büyüme ve protein sentezi, **8-12 saat**): hücre büyümesi, RNA ve protein sentezi. **Bu faza özgü kemoterapi ilacı yoktur**; **CDK inhibitörleri** (ör. **palbosiklib**) bazı kanserlerde kullanılır."),
                B("**S**: DNA sentezi, **6-8 saat** · **G2**: pre-mitotik dönem, **2-4 saat** · **M**: mitoz, **1-2 saat**."),
            ]),
            C("S fazı özgü ilaçlar (DNA sentezini inhibe eder)", [
                B("**Antimetabolitler**: sitozin arabinozid (Ara-C), gemsitabin, **5-florourasil (5-FU)**, kapesitabin, **6-merkaptopürin (6-MP)**, **metotreksat**, fludarabin, pemetreksed."),
                B("**Ribonükleotid redüktaz inhibitörü**: **hidroksiüre**."),
            ]),
            C("G2 fazı özgü ilaçlar (mitoza geçişi inhibe eder)", [
                B("**Topoizomeraz II inhibitörleri**: **etoposid, teniposid**, doksorubisin (özellikle S ve G2)."),
                B("**DNA hasarı oluşturan ajanlar**: **sisplatin** (özellikle G2), karboplatin, dakarbazin, **nitrozüreler** (karmustin, lomustin)."),
            ]),
            C("M fazı özgü ilaçlar (mitozu inhibe eder)", [
                B("**Mikrotübül inhibitörleri**: **vinkristin, vinblastin, vinorelbin, paklitaksel, dosetaksel, iksabepilon**."),
                B("Diğer: **eribulin** (mikrotübül dinamiğini inhibe eder)."),
            ]),
        ],
        # 4 — döneme özgü olmayan + tümör biyolojisi
        [
            C("Döneme özgü olmayan ilaçlar (birden fazla fazda etkili; çoğu zaman G0'daki hücreleri de etkiler)", [
                B("**Alkilleyici ilaçlar**: siklofosfamid, ifosfamid, melfalan, klorambusil, busulfan."),
                B("**Platin türevleri**: sisplatin, karboplatin, oksaliplatin."),
                B("**Nitrozüreler**: karmustin, lomustin, streptozosin, dakarbazin."),
                B("**Antibiyotikler** (DNA'ya interkalasyon veya serbest radikal oluşumu): doksorubisin, daunorubisin, bleomisin, mitomisin C."),
                B("**Prokarbazin**; diğer: **temozolomid**."),
            ]),
            C("Etkinliği kısıtlayan faktörler — 1) Tümör biyolojisi ve tümör–ilaç etkileşmesi", [
                B("Malign hücre sayısındaki azalma **logaritmik (eksponansiyel)**; **birinci derece kinetiğe** uyar."),
                B("Her doz hücreyi sabit miktarda değil **belirli oranda** azaltır (örn. **%90 azalma → kalan %10 hücre** bir sonraki dozun hedefidir)."),
                B("Tümörün tamamını eradike etmek pratik olarak zordur; **rezidüel hücreler nüksten sorumludur**."),
                B("Tümör hücreleri arasında **heterojenite** (büyüme hızı, ilaç duyarlılığı, genetik direnç) yanıtı sınırlar."),
            ]),
        ],
        # 5 — hücre döngüsü/proliferasyon, AUC/Cmax, farmakokinetik
        [
            C("Hücre döngüsü ve proliferasyon hızıyla ilişkili faktörler", [
                B("Önemli etmen: ilacın **hücre döngüsüne özgü (cell cycle-specific)** olup olmaması."),
                B("**Döneme özgü** ilaçlar yalnızca belirli fazda (ör. S veya M) etkilidir → **hızlı bölünen hücrelerde** daha etkilidir."),
                B("**Döneme özgü olmayan** ilaçlar G0 (istirahat) ya da aktif bölünmede **her fazda** etkili olabilir; ortak özellik: genellikle **DNA yapısını doğrudan bozarak** sitotoksik etki."),
                B("**Proliferasyon hızı**: hızla çoğalan hücreler daha duyarlı; **yavaş çoğalan veya dormant** hücreler daha dirençlidir."),
            ]),
            C("Etkinlik ve toksisite", [
                B("**Antineoplastik etkinlik** → zaman boyunca oluşan **toplam ilaç maruziyeti (EAA/AUC)**."),
                B("**Toksisite şiddeti** → genellikle **doruk konsantrasyon (Cmax)**."),
            ]),
            C("2) İlacın farmakokinetiği ve farmakolojisi", [
                B("a) **SSS'ne geçiş**: **nitrozüreler, prokarbazin, dakarbazin, etopozid, tenopozid**.", y="23-24"),
                B("b) **Dik doz-yanıt eğrisi**; ↓ terapötik indeks (sürekli terapötik doz aralığında uygulama)."),
                B("c) **Toksisiteyi azaltmak** için: birlikte **antidot**; tümör bölgesine **lokal, yüksek konsantrasyonda** uygulama; **hematopoietik büyüme faktörleri**; **kemik iliği infüzyonu (transplantasyon)**."),
            ]),
        ],
        # 6 — hasta faktörleri, direnç
        [
            C("3) Hasta ile ilgili faktörler", [
                B("Hastanın **genel aktivite durumu** ve **immün durumu**."),
                B("Hastada daha önce **kemoterapi ya da radyoterapi** yapılıp yapılmamış olması."),
                B("Diğer: yaş, seks, ırk, organların durumu…"),
            ]),
            C("4) Direnç gelişimi ve ilaca rezistans", [
                B("**Doğal (primer)** ve **kazanılmış (sekonder)** direnç; antimikrobiklerde olduğu gibi antineoplastiklerde de **etkinlik spektrumu** vardır."),
                B("Direnç kazanılmasını önlemek için ilaçlar **kombine** edilir veya **tek ilaç yeterli süre ve dozda** verilir."),
            ]),
            C("Direnç mekanizmaları", [
                B("**Azalmış uptake**: taşıyıcı proteinlerin ekspresyonu azalır → ilacın hücre içine girişi azalır."),
                B("**Efluks artışı**: özellikle **P-glikoprotein** gibi ATP-bağımlı taşıyıcıların aşırı ekspresyonu."),
                B("**Glutatyon (GSH)** ve ilişkili enzimlerle **konjugasyonun artışı** → detoksifikasyon."),
                B("**Hedef proteinde yapısal/kantitatif değişiklik** (enzim veya reseptör) → bağlanma afinitesi düşer."),
                B("**İntrasellüler detoksifikasyon artışı**: sitokrom P450, glutatyon-S-transferaz aktivitesi ↑."),
                B("**Topoizomeraz II** değişikliği (ekspresyon artışı veya yapısal modifikasyon) → bağlanma afinitesi azalır."),
                B("**DNA tamir mekanizmalarının** aktivasyonunda artış."),
            ]),
        ],
        # 7 — ortak yan etkiler 1
        [
            C("Kemik iliği, lenfoid doku ve hızlı çoğalan normal hücreler", [
                B("**Kemik iliği supresyonu (myelotoksisite)**; özellikle **lökopeni**."),
                B("**Döneme özgü** ilaçlarda **hızlı gelişen, hızlı düzelen** lökopeni; **döneme özgü olmayanlarda** **yavaş gelişen, uzun süren, geç düzelen** lökopeni."),
                B("**Lenfotoksik etki ve immünosupresyon**: humoral ve hücresel immünite baskılanır."),
                B("Hızlı çoğalan normal hücrelerin inhibisyonu: ağızda **ülser, stomatit**, bazen **enterit**; **alopesi**."),
                B("Erkekte **spermatogenez**, kadında **oogenez**, her iki seksde **seks hormonu üretimi** bozulur → **empotans, kısırlık, amenore**."),
            ]),
            C("Embriyotoksik/teratojenik; karsinojenik/mutajenik etki", [
                B("**Embriyotoksik ve teratojenik** etki; **karsinojenik ve mutajenik** etki."),
                B("**↑ karsinojenik etki**: **alkilleyiciler, prokarbazin**…"),
                B("**↓ karsinojenik etki**: **antimetabolitler, vinka alkaloidleri**…", y="22-23"),
            ]),
        ],
        # 8 — ortak yan etkiler 2
        [
            C("Bulantı-kusma, lokal reaksiyon, hiperürisemi, alerji", [
                B("**Bulantı ve kusma**; özellikle **sisplatin, dakarbazin, mekloretamin, doksorubisin, daunorubisin, epirubisin, siklofosfamid**… (metoklopramid, fenotiyazin, ondansetron, tropisetron vb.)"),
                B("**Lokal reaksiyon**: i.v. infüzyonda **ekstravazasyon** → doku zedelenmesi, nekroz. **Mekloretamin** sızmasında **sodyum tiyosülfat**, **vinkristin**'de **hyaluronidaz** ve sıcak uygulama."),
                B("**Hiperürisemi**: **purin antimetabolitleri** ile tedavi sırasında oluşabilir → **ksantin oksidaz inhibitörü “allopurinol”** verilir ve **hidrate** edilir.", y="25-26"),
                B("**Alerjik reaksiyonlar** (ürtiker, anjioödem, anafilaksi): **asparaginaz, sisplatin, melfalan**."),
            ]),
            C("Diğer toksik tesirler (organ organ)", [
                B("**Nefrotoksisite**: metotreksat, **sisplatin**."),
                B("**Kardiyotoksisite**: **doksorubisin**, fluorourasil, siklofosfamid, amsakrin.", y="25-26"),
                B("**Hepatotoksisite**: metotreksat, fluorourasil, sitarabin, aklarubisin, asparaginaz."),
                B("**Periferik nöropati**: vinka alkaloidleri, sisplatin."),
                B("**Santral nörotoksisite**: vinka alkaloidleri, fluorourasil, metotreksat, siklofosfamid."),
                B("**Akciğer toksisitesi**: **bleomisin, busulfan, mitomisin**, nitrozüre türevleri."),
                B("**Uzun süreli sıvı retansiyonu ve bacak ödemi**: **dosetaksel**.", y="23-24"),
            ]),
        ],
        # 9 — sınıflandırma
        [
            C("Farmakolojik sınıflandırma (1-4)", [
                B("**1. Alkilleyici ajanlar**: azotlu hardallar, nitrozüreler, triazen ve hidrazen türevleri, busulfan, prokarbazin vb. — **DNA bazlarıyla kovalent bağ** kurarak replikasyonu engeller."),
                B("**2. Antimetabolitler**: folat antagonistleri (**metotreksat**), pürin analogları (**6-merkaptopürin**), pirimidin analogları (**5-fluorourasil**) — nükleik asit sentezindeki **enzimleri inhibe eder**."),
                B("**3. Bitkisel kaynaklılar**: vinka alkaloidleri (vinkristin, vinblastin), taksanlar (paklitaksel, dosetaksel) — **mikrotübül dinamiğini bozarak** mitotik iğ ipliklerinin oluşumunu engeller."),
                B("**4. Sitotoksik antibiyotikler**: doksorubisin, daunorubisin, bleomisin, mitomisin — **DNA'ya interkalasyon, serbest radikal oluşumu, topoizomeraz-II inhibisyonu**."),
            ]),
            C("Farmakolojik sınıflandırma (5-8)", [
                B("**5. Platin bileşikleri ve koruyucu ajanlar**: sisplatin, karboplatin, oksaliplatin; koruyucu ajan **amifostin** — DNA zincirlerinde **çapraz bağ** oluşturarak replikasyonu durdurur."),
                B("**6. Enzim ajanları**: **L-asparaginaz** — tümör hücrelerinde gerekli **asparagini hidrolize** ederek sentezini engeller."),
                B("**7. Hormonlar ve hormon antagonistleri**: glukokortikoidler, antiöstrojenler (tamoksifen), aromataz inhibitörleri, antiandrojenler — hormon bağımlı tümör büyümesini baskılar."),
                B("**8. Diğer ve hedefe yönelik**: monoklonal antikorlar (trastuzumab, rituksimab), tirozin kinaz inhibitörleri (imatinib) — spesifik sinyal yolaklarını bloke eder."),
            ]),
        ],
        # 10 — alkilleyici genel + siklofosfamid
        [
            C("Alkilleyici ilaçlar — genel özellikler", [
                B("**En fazla kullanılan** antineoplastikler; **ön-ilaçlardır**; **döneme özgü olmayan** (en fazla **G1 ve S** dönemine etkili)."),
                B("Etki: **etilenimonyum** ve **karbonyum** türevi, **elektrofilik** reaktif metabolitler DNA ve makromoleküllerin **nükleofilik gruplarına kovalent, irreversibl** bağlanır → DNA'nın **transkripsiyon ve replikasyonu** bozulur."),
                B("**Yavaş ve çok aşamalı mutasyonla direnç**."),
                B("Ortak özellikler: **miyelotoksisite**, **lenfotoksisite-immünosupresyon**, bulantı-kusma, iştahsızlık, **mukozit**, **teratojenik, mutajenik, karsinojenik** etki, **radyomimetik etki**; **spermatogenezi en fazla deprese eden** ilaçların başındadır."),
            ]),
            C("1) Azotlu hardallar (biskloretilaminler) — Siklofosfamid", [
                B("**Siklofosfamid**: sık kullanım, **güçlü immünosupressif etkinlik**.", y="23-24"),
                B("Endikasyonlar: Hodgkin dışı lenfomalar, Hodgkin lenfoma, pediatrik solid tümörler, testis kanseri, yumuşak doku sarkomu, **Behçet hastalığı**, akut-kronik lenfositik lösemi, küçük hücreli akciğer Ca, meme/over/serviks/endometrium Ca, baş-boyun kanserleri, multipl miyelom, koryokarsinom + **romatoid artrit**."),
                B("Yan etkiler: bulantı-kusma ve diğer GİS bozuklukları, **kemik iliği depresyonu**, **steril hemorajik sistit** (**“akrolein”** oluşmasına bağlı; antidotu **“mesna”**).", y="24-25"),
            ]),
        ],
        # 11 — diğer azotlu hardallar, etilenimin, sülfonat
        [
            C("Diğer azotlu hardallar", [
                B("**Mekloretamin**: Hodgkin ve Hodgkin dışı lenfomalarda kullanılır."),
                B("**Klorambusil**: ↓ toksisite; yavaş etki; KLL, Hodgkin dışı lenfomalar, Hodgkin hastalığı, over kanseri."),
                B("**Melfalan**: klorambusile benzer; **multipl miyelomda** endikedir."),
                B("**İfosfamid**: siklofosfamid analogu; **K.İ. depresan etkisi daha az, ürotoksik etkisi daha fazla**."),
            ]),
            C("2) Etileniminler ve metilmelaminler", [
                B("**Aziridin**: meme ve over kanseri, plevral ve peritoneal effüzyonlar, mesanenin yüzeyel papiller kanseri."),
                B("**Altretamin**: güçlü emetik etki, nörotoksisite; over, meme, serviks, akciğer kanserleri ve lenfoma."),
            ]),
            C("3) Alkil sülfonatlar — Busulfan", [
                B("**Busulfan**: **kronik miyeloid lösemi (en tercih edilen ilaç)**, polisitemia vera, miyelofibrozis."),
                B("Yan etkiler: uzun süreli kullanımda **kronik pnömonit (busulfan akciğer sendromu)**, K.İ. depresyonu."),
            ]),
        ],
        # 12 — nitrozüreler, triazen
        [
            C("4) Nitrozüreler", [
                B("↑ **lipofilik** ilaçlar; **SSS'ne kolayca girerler** (redistribüsyon); ↑ **K.İ. depresyonu**, **nefrotoksisite**.", y="23-24"),
                B("**Karmustin**: Hodgkin hastalığı, Hodgkin dışı lenfomalar, **primer beyin tümörleri**, malign melanoma."),
                B("**Lomustin**: karmustin endikasyonları + **küçük hücreli akciğer kanseri**."),
                B("**Semustin**: primer beyin tümörleri, mide ve kolon kanserleri."),
            ]),
            C("5) Triazen ve hidrazen türevleri", [
                B("Etki mekanizmaları kesin belli değil; SSS'ne ↑ oranda girerler; **MAO enzimini inhibe** ederler."),
                B("**Dakarbazin**: triazen türevi; Hodgkin hastalığı, malign melanoma, yumuşak doku sarkomları."),
                B("**Prokarbazin**: metilhidrazin türevi; Hodgkin hastalığı."),
            ]),
            C("Slayttaki örnek sorular (cevaplar)", [
                B("SSS'ne kolay geçiş (yüksek lipofilik) nedeniyle **primer beyin tümörlerinde en sık tercih edilen** → **karmustin**."),
                B("**Steril hemorajik sistit** (metabolit **akrolein**), **mesna** ile önlenir → **siklofosfamid**."),
                B("Belirgin **nefrotoksisite**, bol sıvıyla hidrasyon önerilir → **sisplatin**."),
                B("Purin antimetabolitleri hiperürisemisini önleyen → **allopurinol**."),
            ]),
        ],
        # 13 — MTX, 6-MP
        [
            C("Antimetabolitler — 1) Folik asid antimetabolitleri: Metotreksat", [
                B("**Döneme özgü**; en önemli toksik etkileri **K.İ. ve barsak mukozası** üzerindedir."),
                B("**Metotreksat**: **folik asid analoğu**; **S** döneminde sitotoksik etki; **güçlü immünosupressif** etki.", y="24-25"),
                B("Etki mekanizması: **dihidrofolat redüktaz (DHFR) inhibisyonu**.", y="23-24"),
                B("Endikasyonlar: Hodgkin dışı lenfomalar, koryokarsinom, meningeal lösemi, baş-boyun, meme ve testis kanserleri, **akut lenfositik lösemi**, osteosarkom, meningeal karsinomatozis, **ağır psöriyazis**, akciğer kanseri."),
                B("Yan etkiler: K.İ. depresyonu, ağız ve barsak mukozasında ülserasyon, hepatotoksisite, nefrotoksisite, akciğerlerde infiltrasyon (**“folinik asid” ile kurtarma**)."),
            ]),
            C("2) Purin antimetabolitleri: 6-Merkaptopurin", [
                B("**6-Merkaptopurin**: purin analogu; **S** döneminde belirgin etkinlik.", y="25-26"),
                B("Etki: doğal inozinatın adenin ve guanin nükleotidlerine dönüşümünü bloke eder + membran permeabilitesini artırıp guanozin difosfat türevlerinin hücre dışına kaçmasına neden olur → DNA ve RNA sentezi bozulur."),
                B("Endikasyon: **lösemilerin idame tedavisi**. Yan etkiler: K.İ. depresyonu, ağız ve barsak mukozasında ülserasyon."),
                B("**Ksantin oksidaz** tarafından **tiyoürik aside** dönüştürülür (**allopurinol** etkinliğini ↑).", y="25-26"),
            ]),
        ],
        # 14 — 6-TG, fludarabin, 5-FU
        [
            C("Purin antimetabolitleri (devam)", [
                B("**6-Tioguanin**: DNA ve RNA sentezi bozulur; **akut miyeloid lösemi**; sindirim kanalına daha az toksiktir."),
                B("**Fludarabin**: adenin analoğu; alkilleyici ilaçlara cevapsız **B-hücreli KLL** tedavisinde **tek başına en etkili ilaç**."),
            ]),
            C("3) Pirimidin antimetabolitleri: 5-Fluorourasil", [
                B("**5-Fluorourasil**: pirimidin analogu; döneme özgü olma özelliği çok belirgin değil."),
                B("Etki: **timidilat sentetaz inhibisyonu**; DNA sentezi, RNA fonksiyonları ve protein sentezi bozulur."),
                B("Endikasyonlar (solid tümörler): dissemine **kolorektal kanser**, meme Ca, dissemine mide adenoCa, over, mesane, serviks, endometriyum, prostat, baş-boyun, pankreas, karaciğer kanserleri, cildin bazal hücreli kanseri."),
                B("Yan etkiler: anoreksi, bulantı-kusma, **mukozit (doz kısıtlayıcı yan etki)**, K.İ. depresyonu (lökopeni), **koroner spazm**, alopesi, onikoliz, dermatit, nazolakrimal kanal stenozu, **serebellar ataksi**, blefarit, konjonktivit."),
            ]),
        ],
        # 15 — sitarabin vs + vinka genel
        [
            C("Diğer pirimidin/ilgili antimetabolitler", [
                B("**Sitarabin (sitozin arabinozid)**: sitidin analogu; **S** döneminde belirgin etkinlik; **DNA polimerazı inhibe eder**, DNA onarımını bozar."),
                B("Endikasyonlar: akut miyelojen lösemi, kronik miyelojen lösemi, akut lenfositik lösemi.", lvl=1),
                B("**Gemsitabin**: lokal yayılmış ve metastatik **küçük hücreli olmayan akciğer kanseri**, **pankreas kanseri**…"),
                B("**Kladribin**: **kıl hücreli lösemi**; ↑ miyelotoksisite."),
                B("**Raltitreksed**: **timidilat sentaz inhibitörü**; metastatik kolon kanserinin palyatif tedavisi."),
            ]),
            C("Vinka alkaloidleri ve bitkisel kaynaklı diğer ilaçlar — genel", [
                B("**Mitoz zehirleri (metafaz zehirleri)**: mitozun metafaz döneminde mitozu önler; **tübülin** moleküllerine bağlanıp çöktürür, mikrotübül yapıtaşlarının bir araya gelmesini engeller (**M dönemine özgü**)."),
                B("Ortak: **nörotoksik** etki; ↑ oranda **tahriş edici** etki."),
            ]),
        ],
        # 16 — vinka alkaloidleri
        [
            C("1) Vinka alkaloidleri — Vinblastin (Velbe)", [
                B("**Vinca rosea**'dan elde edilen alkaloid."),
                B("Endikasyonlar: testis kanseri, ilerlemiş Hodgkin hastalığı, Hodgkin dışı lenfomalar, koryokarsinom, meme kanseri, nöroblastoma, baş-boyun kanseri."),
                B("Yan etkiler: lökopeni, bulantı-kusma, alopesi, **periferik nörit**, **santral nöropati** (baş ağrısı, mental depresyon, konvülsiyon).", y="23-24"),
            ]),
            C("Vinkristin (Oncovin)", [
                B("**Vinca rosea**'dan elde edilen alkaloid."),
                B("Endikasyonlar: **Burkitt lenfoması**, ilerlemiş Hodgkin hastalığı, Hodgkin dışı lenfomalar, küçük hücreli akciğer kanseri, multipl miyelom, meme-serviks kanseri, akut miyelojen lösemi, KLL, nadir pediyatrik solid tümörler (**Ewing sarkomu, nöroblastoma, embriyonal rabdomyosarkom**)."),
                B("Yan etkiler: selülit, flebit, alopesi, **periferik nöropati**, **tahriş edici etki** (hafif miyelotoksik etki)."),
            ]),
            C("Yarı sentetik türevler", [
                B("**Vindesin**: vinblastinin yarı sentetik türevi."),
                B("**Vinorelbin**: vinblastinin yarı sentetik türevi; ilerlemiş meme Ca, ilerlemiş küçük hücreli olmayan akciğer kanseri…; **belirgin miyelotoksik** etki."),
            ]),
        ],
        # 17 — podofilotoksinler
        [
            C("2) Podofilotoksinler — Podofilotoksin", [
                B("**Podophyllum peltatum**, **P. emodi**'den elde edilen bileşik."),
                B("**Lokal** olarak cilt kanserleri ve **kondiloma akuminata** tedavisinde kullanılır; barsaklar üzerine belirgin **tahriş edici** etki."),
            ]),
            C("Etopozid", [
                B("Podofilotoksinin yarı sentetik türevi; **mitoz zehiri değil**; **geç S veya G2** dönemine etkili."),
                B("Endikasyonlar: testis kanseri, Hodgkin dışı lenfomalar, küçük hücreli akciğer kanseri, koryokarsinom, nöroblastoma, akut miyelositik lösemi."),
                B("Yan etkiler: K.İ. depresyonu, bulantı-kusma, ateş, flebit, **kardiyotoksisite**, lenfoid dokuda hipoplazi, alopesi, periferik nöropati, mukozit."),
            ]),
            C("Tenipozid", [
                B("Yapısı, etki mekanizması ve yan etkileri **etopozide benzer**."),
                B("Kullanım: lenfomalar, **akut lenfoblastik lösemi (ALL)**, nöroblastoma, beyin tümörleri, mesane kanseri."),
            ]),
        ],
        # 18 — taksanlar, kamptotesin
        [
            C("3) Taksanlar", [
                B("**Taxus brevifolia** bitkisinden elde edilir."),
                B("**Tübülin sentezini stimüle** ederek mikrotübül oluşumunu **artırır** (**vinka alkaloidlerinin tersine**); **fonksiyonel olmayan** mikrotübül gelişimine neden olur."),
                B("**Nörotoksik**; ↑ oranda **tahriş edici** etki."),
            ]),
            C("Paklitaksel ve Dosetaksel", [
                B("**Paklitaksel**: primer ve metastatik over Ca (sisplatinle kombine), metastatik meme Ca. **Platin bileşikleri dışında over Ca'ya karşı en yüksek terapötik cevabı (%28)** veren ilaçtır."),
                B("Yan etkiler: **anafilaktik reaksiyonlar**, **kalpte iletim bozukluğu**, kas ağrısı, hafif bulantı-kusma, K.İ. depresyonu, alopesi, periferik nöropati.", lvl=1),
                B("**Dosetaksel**: ilerlemiş meme Ca; yan etkiler paklitaksele benzer **+ belirgin sıvı retansiyonu ve bacak ödemi**.", y="23-24"),
            ]),
            C("4) Kamptotesin türevleri", [
                B("**Camptotheca acuminata** bitkisinden alkaloidler; **topoizomeraz-I** enzimini güçlü ve selektif inhibe eder → DNA replikasyonu önlenir."),
                B("En önemli **doz kısıtlayıcı** yan etki **K.İ. supresyonu**; ayrıca asteni, anoreksi, alopesi, **kolinerjik stimülasyona bağlı erken başlayan diyare**."),
                B("**İrinotekan**: standart tedavi yetersizse metastatik **kolorektal kanser** (i.v.)."),
                B("**Topotekan**: standart tedavi yetersizse metastatik **over kanseri** (i.v.)."),
            ]),
        ],
        # 19 — daktinomisin, daunorubisin
        [
            C("Sitotoksik antibiyotikler — genel; Daktinomisin (Actinomisin-D)", [
                B("**Sadece i.v.** kullanım; **radyomimetik** etkinlik."),
                B("**Daktinomisin**: **Streptomyces parvulus**'tan; DNA çift zincirinde komşu **guanin-sitozin** baz çiftleri arasına **interkalasyon** → replikasyon ve transkripsiyonu (mRNA sentezi) bozar; **döneme özgü olmayan**."),
                B("Endikasyonlar: **gebeliğe bağlı koryokarsinom**, testis tümörleri."),
                B("Yan etkiler: K.İ. depresyonu, bulantı-kusma, hiperpigmentasyon, tahriş edici etki, diyare, cilt döküntüleri, ağız ve barsakta ülser, teratojenik etki."),
                B("**Bakteriyostatik** etki de gösterir; kullananlarda **penisilin** tedavisi yapılırsa onun antibakteriyel etkinliğini **azaltır**."),
            ]),
            C("Daunorubisin", [
                B("**Streptomyces peucetius**'tan; DNA çift zincirinde komşu G-C baz çiftleri arasına **interkalasyon** + **topoizomeraz-II**'ye bağlanıp DNA yarılması yapar."),
                B("**Döneme özgü olmayan** etki, ancak **S** döneminde ↑ etkinlik. Endikasyonlar: akut miyelojen lösemi, akut lenfositik lösemi."),
            ]),
        ],
        # 20 — daunorubisin yan etkileri, doksorubisin
        [
            C("Daunorubisin — yan etkiler ve kardiyotoksisite mekanizması", [
                B("Alopesi, **K.İ. depresyonu (doz kısıtlayıcı)**, bulantı-kusma, **tahriş edici etki** (doku zedelenmesi, nekroz), hiperpigmentasyon, teratojenik-mutajenik-karsinojenik etkinlik."),
                B("**Kardiyotoksisite (kalp yetmezliği gelişebilir)**: miyokardda akut ve kronik zedelenme.", y="25-26"),
                B("1) sarkolemmal **Na⁺/Ca²⁺ değiş-tokuşunun bozulması**", lvl=1),
                B("2) miyokard hücresinin **enerji metabolizmasının bozulması**", lvl=1),
                B("3) antrasiklinin miyokard hücrelerinde **aşırı serbest oksijen radikali** oluşturması", lvl=1),
            ]),
            C("Doksorubisin (Adriamisin) ve türevleri", [
                B("**Doksorubisin**: daunorubisin türevi; **etki mekanizmaları ve yan etkileri aynıdır**; döneme özgü olmayan, **S** döneminde ↑ etkinlik.", y="25-26"),
                B("Endikasyonlar: akut miyelojen ve lenfositik lösemi, Hodgkin ve Hodgkin dışı lenfomalar, **Wilms tümörü**, meme, akciğer, mide, pankreas, mesane, endometrium, tiroid, prostat, over, serviks Ca, cildin skuamöz hücreli kanserleri, baş-boyun."),
                B("**Epirubisin**: doksorubisin türevi; **kardiyotoksik etkisi daha az**; kolorektal kanserlerde de endike."),
                B("**Aklarubisin**: kardiyotoksik etkisi azaltılmış yeni türev."),
                B("**Mitoksantron**: yapıca antrasiklinlere benzer, **antibiyotik değildir**; döneme özgü olmayan; meme kanseri; K.İ. depresyonu, bulantı-kusma, stomatit, alopesi, miyokard toksisitesi."),
            ]),
        ],
        # 21 — bleomisin, plikamisin, mitomisin
        [
            C("Bleomisin", [
                B("**Streptomyces verticillus**'tan; hücrelerde **serbest radikal** oluşturup **DNA zincirlerinde kırılma** yapar."),
                B("**Döneme özgü** etki; en fazla **G2**, geç G1, erken S ve M dönemlerinde etkili."),
                B("Endikasyonlar: Hodgkin ve diğer lenfomalar, testis tümörleri, mesanenin yüzeyel kanseri, cildin skuamöz hücreli kanseri, serviks, baş-boyun kanserleri."),
                B("Yan etkiler: **hafif** K.İ. depresyonu, bulantı-kusma, hiperpigmentasyon, **el ayası ve dirseklerde hiperkeratoz**, alopesi, alerjik reaksiyonlar (ateş, titreme, döküntü, anafilaksi), ciltte kalınlaşma, **akciğerde pnömoni-fibrozis**."),
            ]),
            C("Plikamisin (Mitramisin) ve Mitomisin (Mutamisin)", [
                B("**Plikamisin**: DNA'ya bağımlı **RNA sentezini** inhibe eder; döneme özgü olmayan, S'de ↑ etkinlik; **sadece embriyonal hücreli testis kanserinde** endike (ancak 2. sırada)."),
                B("**Mitomisin**: DNA sentezini inhibe eder; döneme özgü olmayan, **geç G1 ve erken S**'de ↑ etkinlik; **doz kısıtlayıcı yan etki K.İ. depresyonu**."),
            ]),
        ],
        # 22 — platin
        [
            C("Sisplatin", [
                B("DNA çift zincirinde **çapraz bağlanma**; **döneme özgü olmayan** etki."),
                B("Endikasyonlar: testis kanserleri, ilerlemiş over kanseri, mesane, prostat, serviks Ca, baş-boyun kanserleri, nöroblastoma, küçük hücreli olmayan akciğer kanseri, osteojenik sarkom, özofagus kanseri."),
                B("Yan etkiler: **bulantı-kusma (en fazla)**, K.İ. depresyonu, periferik nöropati, hipokalsemi, anafilaktik reaksiyon, ateş, hemoliz, **hipomagnezemi**."),
                B("**Akut tübüler nekroz** (tedavi: **güçlü hidrasyon**); **yüksek frekanslı seslere karşı sağırlık**.", y="21-22"),
            ]),
            C("Karboplatin ve Oksaliplatin", [
                B("**Karboplatin**: **nükseden over Ca**'da; renal toksisite, ototoksisite, nörotoksisite daha az."),
                B("**Oksaliplatin**: toksisitesi daha az; **metastatik kolorektal Ca**'ya etkili ilk platin türevi; en önemli yan etki **periferik nöropati**, bazen çizgili kas spazmı (**laringospazm**)."),
            ]),
            C("Amifostin", [
                B("**Sisplatin vb. ilaçların kümülatif nefrotoksisitesini** ve over Ca'da sisplatin + siklofosfamid kombinasyonunun **nötropeniye bağlı enfeksiyon riskini** azaltan **antidot**.", y="22-23 23-24"),
                B("Sisplatinin oluşturduğu **serbest radikalleri bağlar ve nötralize** eder."),
                B("Yan etkiler: hipotansiyon, sersemlik, üşüme-titreme, hapşırma, sıcak basması, hipokalsemi…"),
            ]),
        ],
        # 23 — interferonlar 1
        [
            C("İnterferonlar — sınıflama (7. PDF)", [
                B("Antijenik özelliklerine göre insan interferonları **alfa, beta ve gama**."),
                B("**Alfa** esas olarak **lökositler**, **beta** **doku fibroblastları**, **gama** **T lenfositlerinde** sentezlenir."),
                B("Eski slayt: sitotoksik etki mekanizması **bilinmemektedir**; **NK hücrelerini** uyardıkları düşünülür; **gama interferon** tümör hücrelerini öldüren **makrofajları** uyarabilir."),
                B("Etkilerini **hücre yüzeyindeki reseptörlere** bağlanarak gösterirler."),
            ]),
            C("İnterferonlar — antineoplastik etki mekanizması (Ek slayt)", [
                B("Özgül **interferon reseptörlerine** bağlanıp **JAK/STAT** yolunu aktive eder → interferon-stimüle genlerin (**ISG**) ekspresyonu değişir."),
                B("**IFN-α ve IFN-β** → **Tip I** reseptör (**IFNAR**); **IFN-γ** → **Tip II** reseptör (**IFNGR**)."),
                B("Etkiler: tümör hücre **proliferasyonunun baskılanması**, **apoptoz** indüksiyonu, tümör hücresinde **immünojenisite ↑**, **NK hücre ve T lenfosit** antitümör aktivitesi ↑, **MHC sınıf I ekspresyonu ↑**."),
                B("Sitotoksik kemoterapiden farklı olarak **immünomodülatör ve antiproliferatif** özelliği birlikte gösteren **biyolojik ajanlar**."),
            ]),
        ],
        # 24 — interferonlar 2
        [
            C("İnterferonların güncel kullanımı", [
                B("**Saçlı hücreli lösemi (HCL)**: IFN-α tarihsel olarak önemli; günümüzde standart **kladribin ± rituksimab**. Sitotoksik tedavinin uygun olmadığı durumlarda, **gebelikte** alternatif olabilir."),
                B("**Kaposi sarkomu**: IFN-α özellikle **AIDS ilişkili** olanda tarihsel; günümüzde sınırlı; hızlı ilerleyen ve semptomatik hastalıkta genellikle tercih edilmez."),
                B("**Miyeloproliferatif neoplaziler**: **pegile interferonlar** ve **ropeginterferon alfa-2b**, özellikle **polisitemia vera**; **JAK2** gibi sürücü mutasyonlu klonal hücreleri baskılayabilir (hastalık modifiye edici potansiyel)."),
                B("**Melanom** (yüksek doz IFN-α adjuvan artık standart değil → PD-1 inhibitörleri, hedefli tedavi) ve **renal hücreli karsinom** (immün kontrol noktası inhibitörleri, hedefe yönelik) standartları değişmiştir."),
            ]),
            C("Farmakokinetik ve yan etkiler", [
                B("**Alfa-2-A interferon**: saçlı hücreli lösemi; tedavi edilenlerin **>%90**'ında ciddi enfeksiyon sıklığı azalır. **IM** uygulanır, emilimi iyidir; protein yapısında → muhtemelen proteazlarla yıkılır."),
                B("Yan etkiler: ilk günlerde **ateş, üşüme, titreme** (grip benzeri, miyalji); doza bağlı **trombositopeni ve lökopeni**; yorgunluk, iştahsızlık, kilo kaybı, alopesi, KC enzimlerinde artış."),
                B("Yüksek dozda **proteinüri** ile **geri dönüşlü nefrotoksisite**; nöropsikiyatrik etkiler (depresyon, irritabilite), **tiroid fonksiyon bozuklukları**; uzun tedavide **otoimmün olaylar**."),
            ]),
        ],
        # 25 — L-asparaginaz, hormonlar 1
        [
            C("L-Asparaginaz", [
                B("**E. coli** ve **Erwinia carotovora** kültürlerinden enzim; **asparagini aspartik asid ve amonyağa hidrolize** eder; vücuttaki asparagin stoklarını azaltır → kandaki **asparagine bağımlı tümörler** yok edilir."),
                B("**Sadece akut lenfositik lösemi** tedavisinde kullanılır."),
                B("**Kemik iliği depresyonu yapmaz.**", y="23-24", tuzak="L-Asparaginaz belirgin kemik iliği depresyonu yapar"),
                B("Yan etkiler: **pıhtılaşma bozuklukları** (tromboz, kanama); insülin sentezi bozulması → **hiperglisemi**; albumin sentezi bozulması → **hipoalbuminemi**; alerjik ve anafilaktik reaksiyonlar."),
            ]),
            C("Hormon ve hormon antagonistleri (1)", [
                B("**Estrojenler** (dietilstilbestrol, fosfesterol, etinil estradiol): geç postmenapozal kadında **meme Ca**; **prostat Ca palyatif** tedavisi (hipofizer gonadotropin ve testosteron salgısının inhibisyonu + antiandrojenik etki)."),
                B("**Progestinler** (megestrol asetat, medroksiprogesteron asetat): **endometriyum kanseri** (antiestrojenik etkileri nedeniyle)."),
                B("**Antiestrojenler** (tamoksifen sitrat, toremifen): **estrojen reseptörlerinin kompetitif blokajı**; meme Ca."),
            ]),
        ],
        # 26 — hormonlar 2 + glukokortikoid
        [
            C("Hormon ve hormon antagonistleri (2)", [
                B("**Aromataz inhibitörleri** (formestan, anastrozol, letrozol, eksemastan): **aromataz enzim inhibisyonu**; postmenapozal/menapoza girmiş kadında **ilerlemiş meme Ca**."),
                B("**Antiandrojenler** (siproteron asetat, flutamid, bikalutamid, nilutamid): **testosteron reseptörlerinin blokajı**; **ilerlemiş prostat Ca**."),
                B("**GnRH analogları** (buserelin, goserelin, triptorelin, löprolid, nafarelin): gonadotropin (FSH, LH) salıveren hipofiz hücrelerinde **desensitizasyon** → **testosteron salınımı durur**; prostat Ca'nın palyatif tedavisi + goserelin; **uterus miyomuna** etkili."),
            ]),
            C("Glukokortikoid hormonlar: Prednizon", [
                B("Etki: **lenfoid dokuda proliferasyonun inhibisyonu (lenfolitik etki)**."),
                B("Endikasyonlar: çocuklarda **akut lenfositik** veya farklılaşmış hücreli lösemi; Hodgkin hastalığı, Hodgkin dışı lenfomalar, myeloma; diğer ilaçların yaptığı K.İ. depresyonu belirtilerinin önlenmesi."),
                B("Myeloma ve kemik metastazlarına bağlı **hiperkalsemi**; radyoterapi sonrası **ödem**; hipofiz ön lobunun frenlenmesiyle meme Ca ve metastazlarının gelişimini yavaşlatma."),
                B("Yardımcı ilaç: diğer antineoplastiklere bağlı **anafilaktik reaksiyon, fibrozis** ve yanıt vermeyen **bulantı-kusma**."),
                B("Yan etkiler: **su-tuz tutulması**, hipertansiyon, adrenal korteks atrofisi, hiperglisemi, osteoporoz, immünosupresyon (enfeksiyon)."),
            ]),
        ],
        # 27 — GK kullanım amaçları
        [
            C("Glukokortikoidlerin kanser tedavisinde kullanım amaçları", [
                B("**1. Antineoplastik (lenfolitik) etki**: lenfoid doku proliferasyonunu inhibe eder; **Hodgkin/Hodgkin dışı lenfomalar, akut lenfositik lösemi, multipl myeloma**da doğrudan kullanılır."),
                B("**2. Destekleyici (adjuvan)**: kemoterapiye bağlı **bulantı-kusmayı** azaltır (antiemetiklerle kombine); K.İ. depresyonuna bağlı semptomları hafifletir."),
                B("**3. Ödem ve inflamasyon kontrolü**: **radyoterapi veya beyin tümörlerine** bağlı ödem; tümör basısına bağlı ağrı ve inflamatuvar yanıt."),
                B("**4. Hiperkalsemi**: özellikle **kemik metastazları veya myeloma** nedeniyle."),
                B("**5. İmmünsupresif/antiinflamatuvar**: **tümör lizis sendromu, sitokin salınım sendromu**, alerjik reaksiyonlar, fibrozis."),
                B("**6. Endokrin etkiler**: hipofiz ön lobu baskılanır → meme kanseri ve metastaz büyümesi yavaşlar."),
                B("Glukokortikoidler yalnızca antineoplastik değil, **kanser tedavisinin pek çok komplikasyonunu yönetmede** çok yönlü ajanlardır."),
            ]),
        ],
        # 28 — lenfolitik etki
        [
            C("Lenfolitik ve antiproliferatif etki", [
                B("**1. Lenfoid dokuda proliferasyonun inhibisyonu**: lenfositlerin **DNA sentezini ve mitozunu** baskılar; özellikle **T-lenfosit** ve bazı B-lenfosit alt tiplerinde **apoptozis** indükler → lenfoid hücrelerin küçülmesi, lenfoid organların **involüsyonu**; lenfoma ve lenfositik lösemide tümör kitlesi küçülür."),
                B("**2. Glukokortikoid reseptör aracılı gen regülasyonu**: sitoplazmik reseptöre bağlanır; kompleks nükleusa taşınıp transkripsiyonu baskılar veya bazı genleri artırır."),
                B("**IL-2, TNF-α, IFN-γ** gibi proliferatif sitokinlerin sentezi inhibe edilir; **proapoptotik genler (Bim) aktive**, **antiapoptotik genler (Bcl-2) baskılanır** → lenfositlerde apoptozis.", lvl=1),
                B("**3. Lenfoid dokularda immünsupresyon**: tümörle ilişkili immün reaksiyonları ve paraneoplastik immün yanıtları azaltır; özellikle **myeloma** gibi immün kökenli malignitelerde sitokin aracılı çoğalmayı durdurur."),
                B("**4. Sekonder etkiler**: tümöre bağlı ödem/inflamasyonu (örn. SSS tümörleri) azaltır; antiemetiklerle kombine edilince kemoterapi yan etkilerini azaltır."),
            ]),
        ],
        # 29 — GK tablo + diğer ilaçlar
        [
            C("Glukokortikoid örnekleri ve klinik kullanım (tablo)", [
                B("**Antikanser etki**: prednizon, deksametazon — özellikle **ALL ve lenfomalarda lenfoid hücre apoptozu**."),
                B("**Antiemetik**: deksametazon, metilprednizolon — kemoterapiye bağlı bulantı-kusma; genellikle diğer antiemetiklerle kombinasyon."),
                B("**Beyin ödemi**: **deksametazon** — beyin tümörü/metastazına bağlı **vazojenik ödem** ve **intrakraniyal basınç artışı**."),
                B("**Tümör ilişkili inflamasyon/semptom**: deksametazon, prednizon — inflamasyon, ağrı, basınç semptomları."),
                B("**Hipersensitivite/infüzyon reaksiyonlarının önlenmesi**: deksametazon, metilprednizolon — bazı kemoterapötik ve biyolojik ilaçlardan önce."),
                B("**Hematolojik malignitelerde kombinasyon**: prednizon, deksametazon — lenfoma, ALL, multipl miyelom protokolleri."),
                B("**İştah ve genel semptom kontrolü**: deksametazon, prednizon — ileri evre kanserde kısa süreli palyatif."),
            ]),
        ],
        # 30 — diğer antineoplastikler
        [
            C("Adrenal ajanlar", [
                B("**Mitotan**: **adrenal kortekste selektif sitotoksisite**; adrenal korteks kaynaklı kanserler."),
                B("**Aminoglutetimid, Trilostan**: adrenal korteks tümörleri; metastatik postmenapozal meme Ca."),
            ]),
            C("Diğer antineoplastik ilaçlar", [
                B("**Hidroksiüre (hidroksikarbamid)**: **ribonükleotid redüktaz** inhibisyonu; **S** dönemine özgü; **busulfana dirençli KML**. Yan etki: K.İ. depresyonu, bulantı-kusma, stomatit, alopesi."),
                B("**Amsakrin**: döneme özgü olmayan; **interkalasyon**; dirençli akut miyelojen lösemi; yan etki K.İ. depresyonu."),
                B("**Altretamin**: diğer rejimler etkisizse ilerlemiş **over Ca** (oral); **bulantı-kusma sık** (antiemetik profilaksi); periferik nöropati, nefrotoksisite, hepatotoksisite."),
                B("**Pentostatin**: nükleozid analoğu; **adenozin deaminaz inhibisyonu**; **kıl hücreli lösemi**."),
                B("**Tiretinoin**: **A vitamini analogu**; dirençli **akut promiyelositik lösemi**."),
            ]),
            C("Radyoizotoplar", [
                B("**Radyoaktif fosfor**: polisitemia vera, kronik lenfositik ve granülositik lösemi."),
                B("**Radyoaktif iyod**: tiroid Ca."),
                B("**Radyoaktif altın**: çocukların beyin tümörleri; periton-plevra boşluklarında metastaza bağlı sıvı toplanmaları."),
                B("**Stronsiyum 89**: çoklu kemik metastazı olan prostat Ca'da radyoterapi yerine kullanılır."),
            ]),
        ],
        # 31 — hedefe yönelik genel
        [
            C("Hedefe yönelik tedavi (targeted therapy) ve monoklonal antikorlar", [
                B("Kanser hücresinin **büyüme, proliferasyon, yaşam ve metastazında** rol oynayan **özgül moleküler hedefleri seçici olarak inhibe** eder; kanser büyümesine katkıda bulunan hatalı genleri, proteinleri veya doku ortamını hedefler."),
                B("Klasik sitotoksik kemoterapiden farklı olarak tedavi seçimi **tümörün moleküler özelliklerine ve biyobelirteçlere** dayanır (tümör tipi + biyobelirteç + klinik özellikler)."),
                B("Bu terapiler: **sinyal transdüksiyon inhibitörleri, immünterapiler, hormon terapileri**."),
                B("Başlıca platformlar: **monoklonal antikorlar**, **küçük moleküllü inhibitörler**, **antikor-ilaç konjugatları (ADC)**, **bispesifik antikorlar**."),
                B("**Monoklonal antikorlar** (IgG): etkilerini bağlandıkları **reseptör sinyalizasyonu**, **ADCC** (antikor-bağımlı hücresel sitotoksisite) ve **CDC** (kompleman-bağımlı sitotoksisite) ile gösterir."),
            ]),
        ],
        # 32 — hedef tablosu
        [
            C("Hedefe yönelik antineoplastikler (tablo 1)", [
                B("**HER2**: trastuzumab, pertuzumab, T-DM1, T-DXd → **meme kanseri**; **kardiyotoksisite**, T-DXd: **ILD/pnömonit**."),
                B("**EGFR**: cetuximab, panitumumab, osimertinib → kolorektal/akciğer; **deri döküntüsü, diyare, hipomagnezemi**; QT uzaması."),
                B("**VEGF**: bevacizumab → solid tümörler; **HT, proteinüri, kanama, tromboz**."),
                B("**CD20**: rituximab, obinutuzumab → B-hücreli maligniteler; **infüzyon reaksiyonu, enfeksiyon, HBV reaktivasyonu**."),
                B("**BCR-ABL**: imatinib, dasatinib, nilotinib → **KML**; **ödem, miyelosupresyon, hepatotoksisite**."),
            ]),
            C("Hedefe yönelik antineoplastikler (tablo 2)", [
                B("**BTK**: ibrutinib, acalabrutinib → B-hücreli maligniteler; **kanama, enfeksiyon, atriyal fibrilasyon**."),
                B("**BCL-2**: venetoclax → **KLL**; **tümör lizis sendromu, nötropeni**."),
                B("**CD38**: daratumumab, isatuximab → **multipl miyelom**; infüzyon reaksiyonu, enfeksiyon."),
                B("**PARP**: olaparib → **BRCA ilişkili tümörler**; anemi, bulantı, yorgunluk."),
                B("**CDK4/6**: palbociclib, ribociclib, abemaciclib → meme kanseri (HR+/HER2−); **nötropeni, diyare; QT uzaması (ribociclib)**."),
            ]),
        ],
        # 33 — Türkiye + karşılaştırma
        [
            C("Türkiye'de hedefe yönelik tedaviler", [
                B("Kullanım **TİTCK ruhsat durumu, SUT geri ödeme koşulları ve klinik endikasyona** göre değerlendirilir."),
                B("Slayt tablosu aynı hedefleri içerir (HER2; **VEGF/VEGFR**: bevacizumab ve diğer antianjiyojenikler; EGFR; BCR-ABL; CD20; PARP; CDK4/6) — yan etkiler büyük ölçüde tablo 1-2 ile aynıdır (CDK4/6: HR+/HER2− meme kanseri)."),
            ]),
            C("Konvansiyonel kemoterapi ↔ hedefe yönelik tedavi", [
                B("**Temel yaklaşım**: hızlı bölünen hücreleri öldürme/inhibe etme ↔ belirli moleküler hedefleri inhibe etme."),
                B("**Hedef seçiciliği**: görece düşük ↔ görece yüksek."),
                B("**Biyobelirteç**: tedavi seçiminde genellikle sınırlı rol ↔ çoğu zaman kritik."),
                B("**Etki mekanizması**: DNA sentezi, mitoz veya hücre bölünmesini genel olarak baskılar ↔ reseptör, kinaz, sinyal yolağı, DNA onarımı vb. özgül hedefler."),
                B("**Toksisite**: miyelosupresyon, bulantı-kusma, mukozit, alopesi ↔ hedefe/ilaca özgü (kardiyotoksisite, HT, deri toksisitesi)."),
                B("**Direnç**: ilaç atılımı, DNA onarımı, hedef değişiklikleri ↔ hedef mutasyonu, alternatif sinyal yolları, hedef kaybı."),
                B("**Etkinlik**: hedef biyolojisinden bağımsız olabilir ↔ uygun biyobelirteçli hastada daha yüksek olabilir."),
                B("**Kombinasyon**: sık ↔ konvansiyonel, immünoterapi veya diğer hedefli ilaçlarla sık."),
                B("**Örnekler**: sisplatin, doksorubisin, paklitaksel, 5-FU ↔ trastuzumab, imatinib, osimertinib, olaparib."),
            ]),
        ],
        # 34 — kanser türüne göre 1
        [
            C("Kanser türüne göre hedefe yönelik ilaçlar (Goodman & Gilman 2017 şeması) — 1", [
                B("**Kalın bağırsak**: VEGF → bevacizumab; EGFR → cetuximab, panitumumab; VEGFR2 → ramucirumab; KIT/PDGFRB → regorafenib; ziv-aflibercept."),
                B("**Prostat**: CYP17 → abiraterone; aşı → sipuleucel-T; kalsiyumu taklit → Ra-223; anti-androjen → enzalutamide."),
                B("**Akciğer**: PD-1 → nivolumab, pembrolizumab; EGFR → erlotinib, gefitinib, afatinib, osimertinib, necitumumab; ALK/MET/ROS1 → crizotinib; ALK → ceritinib, alectinib; VEGF → bevacizumab; VEGFR2 → ramucirumab."),
                B("**Melanom**: CTLA4 → ipilimumab; PD1 → nivolumab, pembrolizumab; aşı → talimogene laherparepvec; MEK → cobimetinib, trametinib; BRAF → vemurafenib, dabrafenib."),
                B("**Mide/mide-yemek borusu**: HER2 → trastuzumab; VEGFR2 → ramucirumab. **GİST**: KIT, PDGFR, ABL → imatinib; regorafenib."),
            ]),
        ],
        # 35 — kanser türüne göre 2
        [
            C("Kanser türüne göre hedefe yönelik ilaçlar — 2", [
                B("**Lenfoma**: PD1 → nivolumab; CD20 → ibritumomab tiuxetan, rituximab, obinutuzumab; CD30 → brentuximab vedotin; HDAC → vorinostat, romidepsin, belinostat; proteazom → bortezomib; BTK → ibrutinib; IL6 → siltuximab; PI3Kδ → idelalisib; antimetabolit → pralatrexate; diğer: denileukin diftitox, bexarotene."),
                B("**Lösemi**: BTK → ibrutinib; Bcl-2 → venetoclax; retinoik asit → tretinoin; ABL/KIT/PDGFR → imatinib; CD20 → rituximab, ofatumumab, obinutuzumab; ABL/SRC/KIT → dasatinib; ABL → nilotinib, bosutinib; CD52 → alemtuzumab; CD19/CD3 → blinatumomab; PI3Kδ → idelalisib."),
                B("**Tiroid**: vandetanib, lenvatinib, cabozantinib, sorafenib."),
                B("**Meme**: HR → tamoxifen, anastrozole, fulvestrant, exemestane, letrozole; HER2 → trastuzumab, pertuzumab, T-DM1, lapatinib; CDK4/6 → palbociclib; mTOR → everolimus."),
                B("**Böbrek**: PD-1 → nivolumab; mTOR → everolimus, temsirolimus; VEGF → bevacizumab; cabozantinib, axitinib, pazopanib, sorafenib, lenvatinib. **Yumurtalık**: PARP → olaparib; VEGF → bevacizumab."),
            ]),
        ],
    ],
    sorular=[
        Q("25-26", 39, "Kardiyotoksisitesi en fazla olan antineoplastik hangisidir?", "Doksorubisin",
          "Antrasiklinler kalp yetmezliği yapabilir (Na⁺/Ca²⁺ değişimi, enerji metabolizması, serbest radikal). Sisplatin, siklofosfamid, MTX, bleomisin çeldirici."),
        Q("25-26", 38, "Allopurinol hangi antikanser ilacın yaptığı hiperürisemiyi önlemek için kullanılır?", "6-Merkaptopurin",
          "Purin antimetabolitleri hiperürisemi yapar → allopurinol + hidrasyon. Doksorubisin, sisplatin, asparaginaz, siklofosfamid purin analoğu değil."),
        Q("24-25", 47, "Hangi ilaç steril hemorajik sistit oluşturur?", "Siklofosfamid",
          "Metabolit akrolein; antidot mesna. Diğer şıklarda (prokarbazin, dakarbazin, vinkristin, tenopozid) PDF bu yan etkiyi vermez."),
        Q("24-25", 52, "Hangisi folik asit antimetabolitidir?", "Metotreksat",
          "DHFR inhibitörü. Karmustin, prokarbazin = alkilleyici; doksorubisin = antrasiklin; sisplatin = platin türevi."),
        Q("23-24", 31, "Bazı antikanser ilaçların yan etkilerini azaltmak için kullanılan ilaç?", "Amifostin",
          "Sisplatin vb.'nin kümülatif nefrotoksisitesini azaltan koruyucu ajan. L-asparaginaz, amsakrin, trilostan, rituximab antineoplastik."),
        Q("23-24", 32, "Hangi ilaç beyine yeterli miktarda geçmez?", "Vinkristin",
          "SSS'ne geçenler: nitrozüreler, prokarbazin, dakarbazin, etopozid, tenopozid (PDF listesi); vinkristin listede yok."),
        Q("23-24", 38, "Hangisi yanlıştır?", "L-Asparaginaz belirgin kemik iliği depresyonu yapar",
          "Asparaginaz K.İ. depresyonu YAPMAZ. Doğru: karmustin lipofilik, MTX DHFR inh., vinblastin santral nöropati, dosetaksel sıvı retansiyonu."),
        Q("23-24", 39, "Özellikle aplastik anemi tedavisinde kullanılan ilaç hangisidir?", "Siklofosfamid",
          "PDF'te yalnız 'güçlü immünosupressif etkinlik' geçer; aplastik anemi endikasyonu geçmez · (PDF'te geçmiyor)"),
        Q("22-23", 22, "Hangisinin karsinojenik etkisi daha azdır?", "Metotreksat",
          "Antimetabolitler ve vinka alkaloidleri ↓; alkilleyiciler (siklofosfamid, mekloretamin, klorambusil, karmustin) ↑ karsinojenik."),
        Q("22-23", 23, "Sisplatinin kümülatif nefrotoksisitesini azaltan antidot?", "Amifostin",
          "Sisplatinin serbest radikallerini bağlar. Mitotan adrenal korteks ajanı; mitomisin, topotekan, etopozid antineoplastik."),
        Q("21-22", None, "Akut tübüler nekroz yapan ilaç?", "Sisplatin",
          "Tedavi/önlem: güçlü hidrasyon. Ayrıca yüksek frekanslı sağırlık, hipomagnezemi, bulantı-kusma (en fazla)."),
    ],
)
