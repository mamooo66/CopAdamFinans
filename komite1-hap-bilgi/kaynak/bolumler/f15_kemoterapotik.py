# -*- coding: utf-8 -*-
"""Kaynak: Drive › Komite-1 › PDF › Farmakoloji › 2026-2027(yeni) › Oruç Yunusoğlu › 6-Kemoterapötiklere giriş"""

from yardim import B, C, Q  # noqa: F401

BOLUM = dict(
    key="kemoterapotik", baslik="Kemoterapötiklere Giriş",
    hoca="Doç. Dr. Oruç Yunusoğlu", tarih="8 Ekim", saat="1 saat",
    kaynak="6-Kemoterapötiklere giriş · O. Yunusoğlu · 2026",
    ozet=["Son 5 yılda bu dersten **3 soru**: 22-23 S19 (rezistansı azaltma ilkeleri) ve **aynı soru iki yıl üst üste** — 23-24 S34, 24-25 S49 (**hücre duvarı sentezini inhibe etmeyen ilaç**).",
          "Tuzak: rezistansı azaltmak için **dar spektrumlu** ilaç kullanılır (geniş değil); doz **yeterli**, süre **mümkün olduğunca kısa**.",
          "Hücre duvarı: **β-laktamlar, glikopeptidler (vankomisin), fosfomisin, basitrasin**. **Eritromisin** (makrolid) = **50S protein sentezi**; **novobiosin** slayt şemasında **DNA giraz**."],
    slaytlar=[
        # 1 — temel ilke, tarihçe, sınıflar
        [
            C("Kemoterapide temel ilke", [
                B("**Konakçıya hiç veya çok az toksik etki yapan** bir kimyasal maddenin, hastalık etkeni üzerinde **ölümcül (letal) veya toksik etki** oluşturmasıdır."),
                B("Hedeflenen mikroorganizmayı etkisiz hale getirirken **konak hücreye minimum zarar** vermektir."),
            ]),
            C("Tarihçe (slayt)", [
                B("**17. yüzyıl**: enfeksiyon hastalıklarının tedavisinde kimyasal maddelerin kullanımı başladı; bu maddelere **“kemoterapötik”** adı verildi."),
                B("**20. yüzyıl başı**: **Paul Ehrlich** — **“seçici toksisite (selective toxicity)”** kavramı."),
            ]),
            C("Patojen etkenin cinsine göre sınıflar (slayt)", [
                B("Kemoterapide kullanılan ilaçlar genellikle **kullandığı patojen etkenin cinsine göre** sınıflara ayrılır:"),
                B("**Antineoplastik** (kanser hücreleri) · **antibakteriyel** (bakteriler; antibiyotikler) · **antihelmintik** (helmintler, parazitik solucanlar) · **antiviral** (virüsler)", lvl=1),
                B("**Antifungal** (mantar/fungus hücreleri) · **antimalaryal** (Plasmodium) · **antiamibik** (Entamoeba histolytica)", lvl=1),
            ]),
        ],
        # 2 — bakteriyostatik / bakterisid, MİK / MBK
        [
            C("Etki derecesine göre iki grup", [
                B("Kemoterapötikler, terapötik dozlarda vücut sıvılarında oluşturdukları konsantrasyonda mikroorganizmalar üzerindeki **etki derecelerine göre iki gruba** ayrılır."),
                B("**Bakteriyostatik**: bakteri hücrelerinin **gelişme ve üremesini durdurur, doğrudan öldürmez**; duran bakteriler **bağışıklık sistemi tarafından yok edilir**."),
                B("Örnekler: **tetrasiklinler, kloramfenikol, eritromisin**.", lvl=1),
                B("**Bakterisid**: bakteri hücrelerini **doğrudan öldürür (letal etki)**; **hızlı etki gerektiren durumlarda** tercih edilir."),
                B("Örnekler: **penisilinler, sefalosporinler, aminoglikozidler**.", lvl=1),
                B("Slayt grafiği (zaman – canlı bakteri sayısı): kontrol, **tetrasiklin (bakteriyostatik)** ve **penisilin (bakterisidal)** eğrileri; ilaç uygulama anı işaretli."),
            ]),
            C("Antimikrobik ilaçların kantitatif göstergeleri", [
                B("**MİK (MIC)**: bakteriyostatik etki gücünün, sıvı kültür ortamında duyarlık testleriyle ölçülen **minimum inhibitör konsantrasyon** değeri. **Değer ne kadar küçükse bakteriyostatik etki gücü o kadar fazladır.**"),
                B("**MBK (MBC)**: bakterisid etki gücünün göstergesi, **minimum bakterisid konsantrasyon**; sıvı kültürde standart koşullarda bakterilerin **%99.9'dan fazlasını** öldüren minimum ilaç konsantrasyonu."),
            ]),
        ],
        # 3 — spektrum, gram + / -
        [
            C("Antimikrobik spektrum", [
                B("Belirli bir kemoterapötiğe **duyarlı olan mikroorganizma türlerinin tümüne** o ilacın **antimikrobik spektrumu** denir."),
                B("**Dar spektrumlu**: yalnız bir veya birkaç bakteri türüne etkili. Örn. **izoniyazid (sadece mikobakteri suşları)**."),
                B("**Geniş spektrumlu**: fazla sayıda bakteri ve diğer mikroorganizma türlerine etkili. Örn. **tetrasiklinler**."),
                B("**Genişletilmiş spektrumlu**: **Gram (+)** bakterilere olduğu kadar **önemli sayıda Gram (–)** bakteriye de etkili. Örn. **ampisilin**."),
            ]),
            C("Gram (+) ve Gram (–) bakteri duvarı (slayt)", [
                B("**Gram (+)**: Gram boyamada **mor/mavi**; **kalın peptidoglikan tabakası**; **teikoik asitler** bulunur. Örn. Staphylococcus, Streptococcus."),
                B("**Gram (–)**: Gram boyamada **pembe/kırmızı**; **ince peptidoglikan tabakası**; **dış membran (LPS içerir)** bulunur. Örn. E. coli, Pseudomonas, Neisseria."),
            ]),
        ],
        # 4 — slayt tablosu: bakterisid / bakteriyostatik ilaçlar
        [
            C("Bakterisid antibakteriyel ilaçlar (slayt tablosu)", [
                B("**β-laktamlar**: penisilinler, sefalosporinler, karbapenemler, monobaktamlar"),
                B("**Glikopeptidler**: vankomisin, teikoplanin"),
                B("**Aminoglikozidler**: gentamisin, amikasin, tobramisin, streptomisin"),
                B("**Fluorokinolonlar**: siprofloksasin, levofloksasin, moksifloksasin"),
                B("**Lipopeptidler**: daptomisin · **Polimiksinler**: polimiksin B, kolistin"),
                B("**Nitroimidazoller**: metronidazol, tinidazol (anaeroblara karşı)"),
                B("**Rifamisinler**: rifampin, rifabutin, rifaksimin (mikobakteriler dahil)"),
            ]),
            C("Bakteriyostatik antibakteriyel ilaçlar (slayt tablosu)", [
                B("**Tetrasiklinler**: tetrasiklin, doksisiklin, minosiklin"),
                B("**Makrolidler**: eritromisin, klaritromisin, azitromisin"),
                B("**Linkozamidler**: klindamisin, linkomisin"),
                B("**Sülfonamidler**: sülfametoksazol, sülfadiazin (trimetoprim kombinasyonu)"),
                B("**Kloramfenikol** (özellikle menenjit ve rickettsial enfeksiyonlarda)"),
                B("**Oksazolidinonlar**: linezolid, tedizolid · **Streptograminler**: kinupristin/dalfopristin"),
            ]),
        ],
        # 5 — etki mekanizmaları 1-3
        [
            C("Etki mekanizmaları — 1) hücre duvarı sentezinin inhibisyonu", [
                B("**Peptidoglikan sentezini veya çapraz bağlanmasını** inhibe ederek hücre duvarı oluşumunu bozar.", y="23-24 24-25"),
                B("**β-laktamlar** (penisilinler, sefalosporinler, karbapenemler, monobaktamlar) · **glikopeptidler** (vankomisin, teikoplanin) · **fosfomisin** · **basitrasin**.", y="23-24 24-25"),
                B("Slayt şemasında hücre duvarı: sikloserin, vankomisin, basitrasin, penisilinler, sefalosporinler, monobaktamlar, karbapenemler.", y="23-24 24-25"),
            ]),
            C("2) hücre membranının bozulması", [
                B("Sitoplazma membranının yapısını ve geçirgenliğini bozarak hücre içeriğinin sızmasına ve **hücre ölümüne** yol açar."),
                B("**Polimiksinler** (kolistin = polimiksin E, polimiksin B) · **daptomisin** (Gram-pozitif bakterilerde)."),
            ]),
            C("3) protein sentezinin inhibisyonu", [
                B("Bakteri ribozomlarının **30S veya 50S** alt birimlerine bağlanarak protein sentezini inhibe eder."),
                B("**30S**: **aminoglikozidler, tetrasiklinler**. Şemada: tetrasiklinler, spektinomisin, streptomisin, gentamisin, kanamisin, amikasin."),
                B("**50S**: **makrolidler, linkozamidler, kloramfenikol, oksazolidinonlar (linezolid), streptograminler**. Şemada: **eritromisin (makrolidler)**, kloramfenikol, klindamisin, linkomisin.", y="23-24 24-25"),
                B("Şemada protein sentezi (tRNA): mupirosin, puromisin."),
            ]),
        ],
        # 6 — etki mekanizmaları 4-5
        [
            C("4) nükleik asit sentezi veya işlevinin inhibisyonu", [
                B("Bakteri **DNA veya RNA sentezini** ya da nükleik asitlerin işlevini inhibe ederek çoğalmalarını engeller."),
                B("**Florokinolonlar** (siprofloksasin, levofloksasin, moksifloksasin): **DNA giraz (topoizomeraz II)** ve **topoizomeraz IV**."),
                B("**Rifamisinler** (rifampin, rifabutin, rifaksimin): **RNA polimeraz**."),
                B("**Metronidazol / tinidazol** (anaerob bakterilere ve bazı protozoalara etkili) · **nitrofurantoin** (üriner sistem enfeksiyonları)."),
                B("Şemada **DNA giraz**: kinolonlar (nalidiksik asit, siprofloksasin) ve **novobiosin**; **RNA elongasyonu**: aktinomisin; **DNA-dependent RNA polimeraz**: rifampin, streptovarisinler.", y="23-24 24-25"),
            ]),
            C("5) folat sentezi / metabolizmasının inhibisyonu", [
                B("**Tetrahidrofolik asit sentezini veya kullanımını** inhibe ederek nükleotid sentezini (DNA/RNA) bozar."),
                B("Basamaklar: **PABA** → (**sülfonamidler** bloke eder; dihidropteroat sentetaz) → dihidrofolik asit → (**trimetoprim** bloke eder) → tetrahidrofolik asit → nükleotid sentezi."),
                B("**Sülfonamidler** (sülfametoksazol, sülfadiazin) · **trimetoprim** (sıklıkla sülfametoksazol ile kombinasyon) · **dapson** (cüzzam, bazı mikobakteriyel enfeksiyonlar)."),
            ]),
        ],
        # 7 — rezistans mekanizmaları
        [
            C("Rezistansın fenotipik mekanizmaları", [
                B("Dış duvardaki **porus (boşluklu) yapısının bozulması** sonucu bakterinin **ilaca permeabilitesinin azalması**."),
                B("**İlacı yıkan enzim** salgılanmaya başlanması (penisilinleri ve sefalosporinleri yıkan **β-laktamazlar** gibi)."),
                B("İlaca duyarsız (dayanıklı) **yeni bir enzim türü** sentezi."),
                B("İlacın **hücre içinde modifikasyonu** ile etkinliğinin azaltılması (**aminoglikozidler** bakteride çeşitli enzimler tarafından bu şekilde inaktive edilir)."),
                B("Rezistan bakteri türünde antibakteriyel ilacın **ortamdan alınmasının azalması**."),
                B("İlacın hücre içindeki **etki yerine bağlanmasının azalması** (örn. aminoglikozidlerin **ribozomun 30S alt birimine** bağlanmasının azalması)."),
            ]),
            C("Direnç türleri (slayt başlıkları)", [
                B("**Antimikrobiyal direnç (tanım)** · **doğal (intrinsik) direnç** · **kazanılmış direnç** · **çapraz direnç**."),
            ]),
        ],
        # 8 — rezistansı azaltma, duyarlık testleri
        [
            C("Rezistans kazanma olasılığını azaltmak için dikkat edilecekler", [
                B("Enfeksiyon etkeni bakteri **duyarlı ise veya duyarlı olduğuna inanılıyorsa** ilaç kullanılmalıdır.", y="22-23"),
                B("İlaç **yeterli dozda** ve **mümkün olduğu kadar kısa bir süre** uygulanmalıdır.", y="22-23"),
                B("Olanak bulunan yerlerde ilaç uygulamadan önce hastadan **izole edilen bakteri ile duyarlık testleri** yapılmalı, ilaç buna göre saptanmalıdır.", y="22-23"),
                B("**Bölgedeki çeşitli bakterilerde rezistans prevalansı** iyi bilinmelidir.", y="22-23"),
                B("**Mümkün olduğu kadar dar spektrumlu** kemoterapötikler kullanılmalıdır.", y="22-23",
                  tuzak="“Mümkün olduğu kadar geniş spektrumlu kemoterapötikler kullanılmalıdır” → YANLIŞ"),
                B("**Salmonella ve Shigella** gibi bazı bakteriler insana kısmen hayvanlardan geçtiğinden kemoterapötiklerin **hayvanlarda kullanımı da kısıtlanmalıdır**."),
            ]),
            C("Duyarlık testleri ve antibiyogram", [
                B("Kemoterapötik seçimi, olanak varsa **patojen etkenin izolasyonu ve duyarlık testleri** ile yapılır; sonuçta bakterinin **antibiyogramı** saptanır."),
                B("Başlıca **üç in vitro duyarlık testi**: **I. disk difüzyon**, **II. agar dilüsyon** (katı ortamda), **III. buyonda dilüsyon** (sıvı ortamda)."),
                B("Antibiyogram basamakları (slayt): etkenin **izolasyonu ve tanımlanması** → duyarlık testinin uygulanması → sonuçların **EUCAST / CLSI** kriterlerine göre yorumu (**S** duyarlı, **I** artırılmış maruziyette duyarlı, **R** dirençli)."),
            ]),
        ],
        # 9 — kemoprofilaksi, direnç
        [
            C("Kemoprofilaksi", [
                B("Kemoterapötikleri kısa veya uzun süre kullanarak belirli enfeksiyonların önlenmesi; **bakterilerde rezistans gelişmesi ve ileride enfeksiyon oluştuğunda çaresiz kalabilme pahasına** yapılan bir uygulamadır."),
                B("Başka bir hastalığı (örn. **kalp kapakçık bozukluğu**) olanlarda **sekonder bakteriyel enfeksiyonu** önlemek için yapılır."),
                B("**Cerrahi girişimlerle ilgili**: belirli girişimlerden hemen önce veya girişim sırasında, **postoperatif enfeksiyonları** önlemek için başvurulabilir."),
            ]),
            C("Antibiyotik direnci neden önemli?", [
                B("Akut enfeksiyon hastalıkları dünyada ölümlerin **%25'inden**, gelişmekte olan ülkelerde **%45'inden** sorumludur (DSÖ)."),
                B("Uygun tedavinin **başarısız olması**, etkili tedavinin gecikmesi → hastalık/komplikasyon riski ↑; **hastanede yatış süresi ve maliyet ↑**; ciddi enfeksiyonlarda **mortalite ↑**; tedavi seçenekleri kısıtlanır."),
                B("Klinik sonuçlar: **daha geniş spektrumlu** antibiyotik ihtiyacı, **daha toksik veya uygulaması zor** ilaçlar, **daha yüksek maliyet**, enfeksiyonu kontrol altına almada güçlük."),
            ]),
            C("Antibiyotik direnciyle savaşma", [
                B("**Antibiyotik farkındalığı**: reçetelerin azaltılması — uygun endikasyon, uygun doz ve süre, gereksiz kullanımdan kaçınma, direnç gelişmelerinin takibi."),
                B("**Viral enfeksiyonlarda** ve **tıp dışı amaçlarla** antibiyotik kullanımının durdurulması; firmaların yeni ve daha ucuz strateji geliştirmesi."),
                B("Yanlış yaygın kullanım: **tarımda**, hastalar ve sağlık/veterinerlik çalışanlarınca; **çiftlik hayvanlarının büyümesini artırmak için gıda katkısı** olarak kullanım."),
            ]),
        ],
    ],
    sorular=[
        Q("25-26", 17, "Yanlış olan hangisi? (burada yalnız e şıkkı: ampirik tedavi)",
          "e) DOĞRU — Ampirik tedavi, etken mikroorganizma tanımlanmadan önce başlatılan antibiyotik tedavisidir (soruda yanlış olan başka şık)",
          "PDF'te ampirik tedavi tanımı yok (yalnız duyarlık testine göre seçim). Soru Farmakoloji F19'da sayılır · (PDF'te geçmiyor)", ref=True),
        Q("24-25", 49, "Hangisi bakteri hücre duvarı sentezini inhibe etmek suretiyle etki ETMEZ? (novobiosin, vankomisin, aztreonam, imipenem, eritromisin)",
          "e) Eritromisin (makrolid; 50S protein sentezi)",
          "Vankomisin glikopeptid, aztreonam monobaktam, imipenem karbapenem = hücre duvarı. Novobiosin PDF şemasında DNA giraz → a da hücre duvarını etkilemiyor"),
        Q("23-24", 34, "Hangisi bakteri hücre duvarı sentezini inhibe etmek suretiyle etki ETMEZ? (novobiosin, vankomisin, aztreonam, imipenem, eritromisin)",
          "e) Eritromisin (makrolid; 50S protein sentezi)",
          "24-25 S49 ile aynı soru. Novobiosin PDF şemasında DNA giraz (a da hücre duvarını etkilemiyor); diğer üçü hücre duvarı inhibitörü"),
        Q("22-23", 19, "Rezistans kazanma olasılığını azaltmak için hangisi DOĞRU DEĞİLDİR?",
          "a) Mümkün olduğu kadar geniş spektrumlu kemoterapötikler kullanılmalıdır",
          "PDF: mümkün olduğu kadar DAR spektrumlu kullanılmalı. Rezistans prevalansı bilinmeli, yeterli doz, kısa süre, duyarlık testi (b-c-d-e) doğru"),
    ],
)
