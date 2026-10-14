# -*- coding: utf-8 -*-
"""Kaynak: Drive › Komite-1 › PDF › Patoloji › 2026-2027(yeni) › Çetin Boran › 1-Neopl-isimlendirme-biyolojisi

NOT: PDF görsel ağırlıklı; bölüm yalnız Drive'ın çıkardığı metinden yazıldı (resim/şema içeriği görülmedi; metinde 'i' harfleri
düşmüştü, bağlamdan düzeltildi). Çıkarılan metin 'GRADE VE STAGE' slaytında bitiyor (dersin içeriği: genel kavramlar · isimlendirme ·
morfoloji); büyüme fraksiyonu / replikatif havuz / anjiyogenez / HIF gibi 'tümör biyolojisi' içeriği metinde yok.
"""

from yardim import B, C, Q  # noqa: F401

BOLUM = dict(
    key="neoplazi", baslik="Neoplazi: Tanım, İsimlendirme ve Morfoloji",
    hoca="Prof. Dr. Çetin Boran", tarih="5 Ekim", saat="1 saat",
    kaynak="1-Neopl-isimlendirme-biyolojisi · Prof. Dr. Ç. Boran · 2026",
    ozet=[
        "23-24'te **'hangisi malign?' → seminoma** çıktı (çeldiriciler: meningioma, fibroma, pleomorfik adenom, rabdomyoma).",
        "25-26 büyüme sorusunun doğru şıklarından ikisi bu dersten: **seminoma malign**, **anaplazi = diferansiasyonun ileri derecede kaybı**. 21-22 (hatırlama): **teratom**, **karsinom**.",
        "Büyüme fraksiyonu, replikatif havuz, anjiyogenez / anti-VEGF ve HIF-1α sorularının cevabı bu PDF'te **yok**.",
    ],
    slaytlar=[
        # 1 — genel kavramlar
        [
            C("Tanım ve terminoloji", [
                B("**Neoplazi** (**tümör**) = **yeni büyüme**: büyümede **otonom kazanılmış**, **büyüme kontrolü kaybolmuş**."),
                B("**Tümör** genel olarak **şişlik** demektir; non-neoplastik kullanımı hemen hiç kalmadı."),
                B("**Onkoloji**: tümörler üzerinde çalışan bilim dalı."),
                B("**Kanser**: tüm **kötü huylu tümörlerin** genel ismi; Latince **yengeç** isminden gelir."),
                B("Neoplastik dokudaki tüm hücreler **tek bir hücreden köken almıştır (klonal)**."),
            ]),
            C("Genel özellikler", [
                B("Benign ve malign tümörler **iki temel komponente** sahiptir:"),
                B("**1- Klonal neoplastik hücreler (parankim)**", lvl=1),
                B("**2- Stroma**: bağ dokusu, kan damarları, makrofaj ve lenfositler içerir", lvl=1),
                B("**Kollajenöz stroması bol** olan tümörlere **desmoplastik** (skirröz) tümör denir."),
            ]),
            C("Benign ve malign", [
                B("**Benign**: **lokalizedir**, **cerrahi olarak çıkarılabilir**; hasta genellikle yaşar."),
                B("**Malign**: **invazivdir**, komşu yapıları tahrip eder, **metastaz yapar**; sahibini öldürebilir."),
            ]),
        ],
        # 2 — isimlendirme
        [
            C("Benign neoplazi isimlendirmesi", [
                B("Tümörün kaynaklandığı **hücre tipine “oma” eki** ilavesiyle isimlendirilir: **lipoma, fibroma, leiomyoma, kondroma, osteoma, rhabdomyoma**.", y="23-24"),
                B("**Adenoma**: bez yapıları oluşturan ya da bezlerden kaynaklanan **benign** tümörler."),
                B("**Papillom**: herhangi bir yüzeye doğru gelişmiş **parmak benzeri yapılar** (mikroskopik ya da makroskopik)."),
                B("**Polip**: mukozal yüzeye uzanan ve **gözle görülebilen çıkıntı**."),
                B("**Kistadenom**: **kistik yapı** oluşturmuş adenom."),
            ]),
            C("Malign neoplazi isimlendirmesi", [
                B("**Sarkoma**: **mezenkimal kökenli** malign tümörler; stroması (bağ dokusu) çok az olduğundan **yumuşaktırlar** (Greek Sar = fleshy). Örn. **fibrosarkoma, kondrosarkoma**."),
                B("**Karsinoma**: **epitelial kökenli** malign tümörler. Örn. **adenokarsinoma, squamous cell karsinoma**.", y="21-22"),
                B("Epitel – germ yaprağı eşleşmeleri (slayt): **böbrek tüp epiteli – mezoderm**, **epidermis – ektoderm**, **GİS mukozası – endoderm**.", lvl=1),
                B("Slayttaki diğer malign adlar: **lenfoma / lösemi**, **seminoma**, malign **melanoma**, malign **mezotelioma**, **hepatoma (HCC)**, **glioma**.", y="23-24 25-26"),
            ]),
        ],
        # 3 — sınıflandırma
        [
            C("Sınıflandırma (slayt)", [
                B("**Mezenkimal orjinli tümörler**: lipoma, fibroma, kondroma, osteoma, osteosarkoma"),
                B("**Endotelial ve ilişkili tümörler**: hemanjioma, lenfanjioma, anjiosarkoma, **meningioma**, malign mezotelioma, sinovial sarkoma", y="23-24"),
                B("**Kas kaynaklı tümörler**: leiomyoma – leiomyosarkoma; rhabdomyoma – rhabdomyosarkoma"),
                B("**Epitelial orjinli tümörler**: skuamöz, basal hücre ve deri eki tümörleri; respiratuvar epitel, böbrek, karaciğer, mesane, testiküler germ cell, plasenta (**mol hidatiform**)"),
                B("**Melanosit** tümörler"),
                B("**Miks tümörler** (tek germ yaprağı kaynaklı): **pleomorfik adenom**, **Wilms tümörü**", y="23-24"),
                B("**Teratomlar** (birden fazla germ yaprağı kaynaklı tümörler)", y="21-22"),
            ]),
        ],
        # 4 — diferansiasyon; miks tümör, teratom, hamartom, koristom
        [
            C("Diferansiasyon", [
                B("**Benign ve malign** terimleri tümörün **biyolojik davranışını** tanımlar."),
                B("Biyolojik davranış, **diferansiasyon derecesi** ve **büyüme hızı** ile yakından ilgilidir."),
                B("**İyi diferansiye** tümörler: kaynaklandığı hücreye **tamamen benzeyen** hücrelerden kuruludur."),
                B("**Kötü diferansiye** ya da **andiferansiye** tümörler: kaynaklandığı hücre ve dokuya **hiç benzemez**; **tanı için özel teknikler gerekir**."),
            ]),
            C("Miks tümör, teratom, hamartom, koristom", [
                B("**Miks tümör**: tümörün kaynağı olan **kök hücrenin değişik yönlerde farklılaşması** ile oluşur (**pleomorfik adenom**: epitelial ve myoepitelial diferansiasyon var).", y="23-24"),
                B("**Teratom**: **embriyonik totipotent hücrelerden** kaynaklanır; **her üç germ yaprağına da farklılaşma** olur; **benign ve malign formları** vardır.", y="21-22"),
                B("**Hamartom**: **kötü organize olmuş** ve kitle olarak izlenen doku."),
                B("**Koristom**: **heterotopik doku** (ince bağırsak submukozasında pankreas bulunması gibi)."),
            ]),
        ],
        # 5 — anaplazi, displazi, mitoz
        [
            C("Anaplazi", [
                B("**Malign tümörlerin bir özelliğidir**: **diferansiasyonun ileri derecede kaybını** ifade eder.", y="25-26"),
                B("Bulgular: **pleomorfizm, hiperkromatik nukleus, nukleus/sitoplazma oranında artış, dev hücre, bizar nükleus**."),
            ]),
            C("Displazi", [
                B("**Epitelde yapı ve organizasyon bozulmuştur**; **hücre uniformitesi kaybolmuştur**."),
                B("**Pleomorfizm ve mitoz** normale göre çok belirgindir."),
                B("Grade: **hafif, orta, şiddetli** ve **karsinoma in situ**."),
                B("**Hafif ve orta şiddette displazi potansiyel olarak geri dönüşlüdür**."),
            ]),
            C("Mitoz", [
                B("Mitoz **proliferatif aktivite** gösterir; pek çok benign ve malign tümörde değişik sıklıkta mitoz görülür."),
                B("**Atipik şekilli mitozlar** malign tanı için **ipucudur**."),
                B("Hızlı büyüyen tümörlerde **beslenme yetersiz** olur ve genelde **tümör nekrozu** da görülür."),
            ]),
        ],
        # 6 — invazyon, metastaz
        [
            C("İnvazyon", [
                B("**Benign** tümörler genelde **yavaş** ve çevre doku ile **iyi bir sınır bırakarak** büyür (**ekspansiyon**)."),
                B("**Malign** tümörler genellikle çevre dokuyu **infiltre ederek destrükte eder**."),
                B("İnvazyon, benign ve malign tümörleri ayırmada kullanılan **temel bulgulardan biridir**."),
                B("Slayt görselleri: **fibroadenom** (benign) – **infiltratif duktal karsinom** (malign)."),
            ]),
            C("Metastaz", [
                B("**Malignitenin kesin bir bulgusudur**."),
                B("Yollar: **(1) vücut boşluklarına ekilme**, **(2) lenfatik yayılım**, **(3) hematojen yayılım**."),
                B("Vücut boşluklarına ekilme: **medulloblastom, akciğer Ca, GİS Ca, over tümörleri**, **mukus sekrete eden apendiks tümörleri** (**pseudomiksoma peritonei**).", lvl=1),
                B("Uzak dokulara **tümör implantları** olur ve orada da tümör büyür."),
                B("Slayt görselleri: karaciğerde metastaz odakları; akciğerde metastatik tümör; metastatik meme karsinomu (aksiller lenf nodu)."),
            ]),
        ],
        # 7 — benign / malign şeması, grade ve stage
        [
            C("Benign ve malign tümör şeması (leiomyoma – leiomyosarkoma)", [
                B("**Benign (leiomyoma)**: küçük, iyi sınırlı, yavaş büyür, noninvaziv, nonmetastatik, iyi diferansiye."),
                B("**Malign (leiomyosarkoma)**: büyük, kötü sınırlı, hızlı büyür (kanama ve nekroz ile), lokal invaziv, metastatik, kötü diferansiye."),
            ]),
            C("Grade ve stage", [
                B("**Grade**: tümörün **mikroskopik görünümüne** ve **tümörün tipine** göre yapılır."),
                B("**Stage (evreleme)**: **klinik, radyolojik ve cerrahi bulgulara** göre yapılır (tümör büyüklüğü, komşu organlara yayılım, lenf nodu metastazları ve organ metastazları)."),
            ]),
        ],
    ],
    sorular=[
        Q("25-26", 80, "(Büyüme biyolojisi sorusunun doğru seçenekleri)",
          "“Seminoma malign bir tümördür” ✔ · “Anaplazi diferansiasyonun ileri derecede kaybıdır” ✔",
          "Sorunun yanlış ifadesi Bölüm 13'te", ref=True),
        Q("23-24", 80, "Hangisi malign bir tümördür?", "Seminoma",
          "Fibroma, rabdomyoma: slayttaki benign listesinde · pleomorfik adenom: adenoma (benign) · meningioma: PDF'te yalnız sınıflama listesinde"),
        Q("21-22", None, "Üç germ tabakasında da değişiklik gösteren tümör? · Hangisi malign tümördür?", "Teratom · Asiner karsinom",
          "Öğrenci hatırlamasından derlenmiş sorular · “asiner” PDF'te geçmiyor; karsinoma = epitelial kökenli malign tümör", n=2),
    ],
)
