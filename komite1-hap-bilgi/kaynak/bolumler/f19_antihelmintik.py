# -*- coding: utf-8 -*-
"""Kaynak: Drive › Komite-1 › PDF › Farmakoloji › 2026-2027(yeni) › Oruç Yunusoğlu › 10-ANTİHELMİNTİK İLAÇLAR"""

from yardim import B, C, Q  # noqa: F401

BOLUM = dict(
    key="antihelmintik", baslik="Antihelmintik İlaçlar",
    hoca="Doç. Dr. Oruç Yunusoğlu", tarih="16 Ekim (program)", saat="1 saat",
    kaynak="10-ANTİHELMİNTİK İLAÇLAR · Doç. Dr. O. Yunusoğlu · 2026",
    ozet=["Son 5 yılda bu dersten **4 soru** çıktı: **levamizol** (immünomodülatör) 22-23 ve 23-24, **GABA / ivermektin** 24-25, **albendazol = antihelmintik** 25-26 (antibakteriyel diye yanlış).",
          "Bu yılki PDF **mekanizma ağırlıklı**: albendazol / mebendazol → β-tübülin; pirantel → nikotinik AChR (spastik paralizi); ivermektin → glutamat kapılı Cl⁻ kanalı; prazikuantel → Ca²⁺ geçirgenliği ↑; niklozamid → oksidatif fosforilasyon.",
          "Levamizol PDF’te yalnızca “**tarihsel öneme sahip, rutin kullanımı sınırlı**” olarak geçer — immünomodülatör etkisi, GABA ve pirantelin emilimi PDF’te **yok**."],
    slaytlar=[
        [
            C("Helmintlerin insanda yerleşim yerleri", [
                B("**İnce bağırsak**: Ascaris lumbricoides, Taenia spp., Ancylostoma duodenale, Enterobius vermicularis."),
                B("**Kalın bağırsak**: Trichuris trichiura, Enterobius vermicularis."),
                B("**Karaciğer ve safra yolları**: Echinococcus granulosus, Fasciola hepatica, Clonorchis sinensis."),
                B("**Akciğer**: Paragonimus spp.; ekinokok kistleri ve bazı nematodların göç eden larvaları."),
                B("**Kan-damar**: Schistosoma spp. (venöz), Wuchereria bancrofti (lenfatik) · **Lenfatik damarlar**: W. bancrofti, Brugia malayi."),
                B("**Kas**: Trichinella spiralis, Taenia solium larvaları."),
                B("**Beyin ve MSS**: Taenia solium larvaları (**nörosistiserkoz**), Echinococcus spp. (nadiren)."),
                B("**Deri / deri altı**: kutanöz larva migrans etkenleri, Onchocerca volvulus · **Göz**: O. volvulus, Loa loa, bazı T. solium larvaları."),
                B("**Üriner sistem ve mesane**: Schistosoma haematobium."),
                B("Yerleşim yaşam evresine göre değişebilir; **bağırsak lümenindeki erişkin parazit** ile **dokuya yerleşen larva** tedavileri aynı olmayabilir."),
            ]),
        ],
        [
            C("Helmintlerin sınıflandırılması", [
                B("**Nematodlar** (yuvarlak solucanlar): Ascaris lumbricoides, Enterobius vermicularis, Strongyloides stercoralis."),
                B("**Sestodlar** (şerit solucanlar): Taenia saginata, Taenia solium, Echinococcus granulosus."),
                B("**Trematodlar** (yaprak solucanlar): Schistosoma spp., Fasciola hepatica."),
            ]),
            C("Antihelmintik ilaçların sınıflandırılması", [
                B("**Benzimidazoller**: albendazol, mebendazol."),
                B("**Nikotinik reseptör agonisti**: pirantel pamoat."),
                B("**Makrosiklik lakton**: ivermektin."),
                B("**Pirazinoizokinolin türevi**: prazikuantel."),
                B("**Salisilanilid**: niklozamid."),
                B("**Diğer ilaçlar**: dietilkarbamazin, piperazin."),
            ]),
            C("Etki mekanizmaları (ilaç → mekanizma → sonuç)", [
                B("**Albendazol**: β-tübüline bağlanır, mikrotübül oluşumunu bozar → enerji metabolizması bozulur."),
                B("**Mebendazol**: mikrotübül oluşumunu ve glukoz kullanımını inhibe eder → parazitin enerjisi tükenir."),
                B("**Pirantel pamoat**: nikotinik asetilkolin reseptörlerini aktive eder → **spastik paralizi**."),
                B("**İvermektin**: glutamat kapılı klor kanallarını aktive eder → nöromüsküler fonksiyon bozukluğu.", y="24-25"),
                B("**Prazikuantel**: kalsiyum geçirgenliğini artırır → kasılma ve tegüment hasarı."),
                B("**Niklozamid**: enerji metabolizmasını ve oksidatif fosforilasyonu bozar → sestodlarda enerji üretimi azalır."),
            ]),
        ],
        [
            C("Slayttaki örnek sorular", [
                B("Yanlış eşleştirme: “**Prazikuantel – kalsiyum geçirgenliğini azaltarak kas gevşemesi**” (doğrusu: kalsiyum geçirgenliğini **artırır** → kasılma). Diğer eşleştirmeler (albendazol, pirantel, ivermektin, niklozamid) doğru."),
                B("“Nikotinik asetilkolin reseptörlerini aktive ederek **nöromüsküler depolarizasyon ve spastik paralizi**” yapan ilaç: **pirantel pamoat**."),
            ]),
            C("Albendazol", [
                B("Farmakolojik grup: **benzimidazol** (antihelmintik).", y="25-26", tuzak="“Albendazol antibakteriyel ilaçtır”"),
                B("Parazitin **β-tübülinine** bağlanır; mikrotübül polimerizasyonunu ve glukoz kullanımını bozar; enerji rezervlerini azaltır."),
                B("Kullanım: **askariyazis**, **kancalı kurt**, seçilmiş **triküriazis**, **kist hidatik ve alveoler ekinokokkoz**, seçilmiş nörosistiserkoz ve doku helmintiyazları."),
                B("Advers: karın ağrısı, bulantı; **karaciğer enzimlerinde yükselme**; uzun süreli tedavide **kemik iliği baskılanması**."),
            ]),
            C("Mebendazol", [
                B("Benzimidazol; mikrotübül oluşumunu bozar, glukoz alımını ve enerji metabolizmasını inhibe eder."),
                B("Kullanım: **kıl kurdu**, askariyazis, triküriazis, kancalı kurt."),
                B("Advers: karın ağrısı, bulantı, ishal; uzun süreli tedavide **hepatotoksisite ve hematolojik toksisite**."),
                B("**Metronidazolle birlikte kullanımdan kaçınılmalı** (ciddi deri reaksiyonları)."),
            ]),
        ],
        [
            C("Pirantel pamoat", [
                B("Parazitin **nikotinik asetilkolin reseptörlerini aktive eder** → nöromüsküler depolarizasyon → **spastik paralizi**."),
                B("Kullanım: **enterobiyazis (kıl kurdu)**, askariyazis, bazı kancalı kurt enfeksiyonları."),
                B("**Piperazin ile birlikte kullanımından kaçınılmalıdır.**"),
            ]),
            C("İvermektin", [
                B("Parazitte **glutamat kapılı klor kanallarını** aktive eder → hücre membranında **hiperpolarizasyon** → nöromüsküler fonksiyon bozulur, paralizi.", y="24-25"),
                B("Kullanım: **strongiloidiyazis**, **onkoserkiazis**, seçilmiş diğer nematod enfeksiyonları."),
                B("Advers: baş dönmesi, bulantı ve GİS yakınmaları; bazı filaryal enfeksiyonlarda inflamatuvar reaksiyonlar."),
                B("**Kortikosteroid başlanmadan önce** strongiloidiyazis riski değerlendirilmeli."),
                B("**Loa loa eş enfeksiyonu** ciddi nörolojik komplikasyon riski oluşturabilir."),
                B("**Gebelik ve 15 kg altı çocuklarda** kullanım kararı özel değerlendirilmeli."),
            ]),
            C("Prazikuantel", [
                B("Parazit membranında **kalsiyum geçirgenliğini artırır** → kasılma, **spastik paralizi**, **tegüment hasarı**."),
                B("Kullanım: **şistozomiyazis**, **taeniyazis**, klonorkiyazis ve opistorkiyazis gibi seçilmiş trematod enfeksiyonları."),
                B("**Nörosistiserkoz**: tedavi öncesi görüntüleme, nöbet riski ve intrakraniyal basınç değerlendirilmeli; kortikosteroid ve antiepileptik gereksinimiyle birlikte planlanabilir."),
            ]),
        ],
        [
            C("Niklozamid ve diğer ilaçlar", [
                B("**Niklozamid**: bağırsak lümenindeki bazı **sestod** enfeksiyonlarında; **doku larvalarına karşı yeterli değil**."),
                B("**Dietilkarbamazin**: seçilmiş filaryal enfeksiyonlarda; parazit türü ve eş enfeksiyonlar değerlendirilmeli."),
                B("**Piperazin**: nöromüsküler iletimi baskılayarak **gevşek paralizi**; güncel kullanımı sınırlı."),
                B("**Levamizol**: tarihsel antihelmintik öneme sahip; insanlarda rutin kullanım alanı sınırlı."),
                B("**Tiabendazol**: benzimidazol türevi; toksisite ve tolerabilite nedeniyle çoğu durumda alternatifler tercih edilir."),
                B("**Oksamnikin**: özellikle **Schistosoma mansoni**’de tarihsel önem; prazikuantel daha yaygın."),
            ]),
            C("Türkiye’de bilinmesi gereken antihelmintikler", [
                B("**Albendazol**: bağırsak helmintleri ve seçilmiş doku helmintiyazları."),
                B("**Pirantel pamoat**: kıl kurdu ve bazı bağırsak nematodları."),
                B("**Mebendazol**: kıl kurdu ve diğer bağırsak helmintleri."),
                B("**İvermektin**: strongiloidiyazis ve seçilmiş filaryal enfeksiyonlar."),
                B("**Prazikuantel**: şistozomiyazis ve sestod enfeksiyonları."),
            ]),
        ],
        [
            C("Bağırsak nematodları — erişkin rejimleri", [
                B("**Askariyazis**: albendazol **400 mg tek doz** · mebendazol **500 mg tek doz** veya **100 mg günde 2 kez, 3 gün**."),
                B("**Triküriazis**: mebendazol **100 mg günde 2 kez, 3 gün**."),
                B("**Kancalı kurt**: albendazol **400 mg tek doz** · mebendazol 500 mg tek doz veya 100 mg günde 2 kez, 3 gün."),
                B("Rejim etken parazite, hastanın özelliklerine ve kılavuza göre değişebilir."),
            ]),
            C("Kıl kurdu tedavisi", [
                B("**Albendazol** 400 mg oral tek doz · **mebendazol** 100 mg oral tek doz · **pirantel pamoat** 11 mg/kg oral (en fazla 1 g)."),
                B("Üçünde de **2 hafta sonra tekrar** doz."),
                B("**İkinci doz neden?** İlaçlar parazit **yumurtalarını güvenilir biçimde ortadan kaldırmaz**; ikinci doz ilk tedaviden sonra yumurtalardan çıkan parazitleri hedefler."),
                B("El hijyeni, tırnak temizliği, çamaşırların uygun temizliği yeniden enfeksiyon riskini azaltır; tekrarlayan enfeksiyonda **ev içi temaslılar** değerlendirilmeli."),
            ]),
        ],
        [
            C("Strongiloidiyazis tedavisi", [
                B("**İlk seçenek: ivermektin** 200 µg/kg/gün oral, 1-2 gün."),
                B("**Alternatif: albendazol** 400 mg oral günde 2 kez, 7 gün."),
                B("**Hiperinfeksiyon / yaygın strongiloidiyazis**: ivermektin 200 µg/kg/gün, dışkı ve/veya balgam incelemeleri **2 hafta boyunca negatifleşene kadar**."),
                B("Mümkünse **immünosupresif tedavi azaltılır veya kesilir**; klinik ve mikrobiyolojik takip gerekir."),
                B("**Kortikosteroid kullanımı, transplantasyon, hematolojik maligniteler, açıklanamayan eozinofili** → Strongyloides stercoralis araştırılmalı."),
            ]),
            C("Şistozomiyazis ve taeniyazis (prazikuantel)", [
                B("**S. mansoni, S. haematobium, S. intercalatum**: toplam **40 mg/kg/gün**, iki doza bölünerek, 1 gün."),
                B("**S. japonicum, S. mekongi**: toplam **60 mg/kg/gün**, üç doza bölünerek, 1 gün."),
                B("**Taeniyazis**: **5-10 mg/kg** oral tek doz."),
                B("Tedavi zamanı ve takip parazit türüne ve maruziyete göre; hafif enfeksiyonda veya devam eden maruziyette tekrar tedavi gerekebilir."),
                B("**Nörosistiserkoz, bağırsak taeniyazisinden ayrı** değerlendirilmelidir."),
            ]),
        ],
        [
            C("Kistik ekinokokkoz ve nörosistiserkoz", [
                B("**Kistik ekinokokkoz**: etken **Echinococcus granulosus**; ilaç **albendazol**; karar kistin **evresi, boyutu ve yerleşimi**ne göre; ek: izlem, perkütan girişim veya cerrahi."),
                B("**Nörosistiserkoz**: etken **Taenia solium larvaları**; ilaç **albendazol ve/veya prazikuantel**; karar lezyon **sayısı, yerleşimi, canlılığı ve nöbet durumu**na göre; ek: kortikosteroid, antiepileptik veya cerrahi."),
            ]),
            C("Güvenlik ve ilaç izlemi", [
                B("**Gebelik**: enfeksiyonun ciddiyeti, gebelik haftası ve ilaca özgü güvenlilik verileri değerlendirilir."),
                B("**Küçük çocuklar**: yaş, kilo ve formülasyona özgü güvenlilik dikkate alınır."),
                B("**Uzun süreli albendazol**: **tam kan sayımı ve karaciğer fonksiyonları** izlenir."),
                B("**İvermektin**: Loa loa eş enfeksiyonu ve nörolojik risk değerlendirilir."),
                B("**Nörosistiserkoz**: nöbet ve inflamasyon riski tedavi öncesi değerlendirilir."),
                B("**Kist hidatik**: tedavi kararı kistin evresine ve komplikasyonlarına göre verilir."),
            ]),
        ],
    ],
    sorular=[
        Q("25-26", 17, "Aşağıdaki bilgilerden hangisi YANLIŞTIR? (metenamin / turuncu reçete / levamizol / albendazol / ampirik)",
          "D) Albendazol antibakteriyel ilaçtır",
          "Albendazol **benzimidazol grubu antihelmintik**tir. Diğer şıklar (metenamin, turuncu reçete, levamizol <2 yaş, ampirik tedavi) bu PDF’te yok."),
        Q("24-25", 48, "Hangi antihelmintik helmintlerde GABA etkinliğini stimüle eder?",
          "B) İvermektin",
          "PDF’te GABA yok; ivermektin klor kanalı (glutamat kapılı) aktive eder. Albendazol β-tübülin, pirantel nAChR, niklozamid oksidatif fosforilasyon · (PDF'te geçmiyor)"),
        Q("23-24", 33, "Hangi antihelmintiğin immünomodülatör etkisi vardır?",
          "C) Levamizol",
          "PDF’te levamizol yalnızca “tarihsel öneme sahip, rutin kullanımı sınırlı”. Albendazol, piperazin, pirantel, niklozamid immünomodülatör değil · (PDF'te geçmiyor)"),
        Q("22-23", 20, "Aşağıdakilerden hangisi doğru DEĞİLDİR? (albendazol / pirantel / levamizol / tiabendazol / emetin)",
          "B) Pirantel pamoatın oral emilimi iyidir, etkisini bağırsakta gösterir",
          "Pirantel bağırsaktan az emilir; PDF’te emilim, lipofiliklik, tiabendazolün antiinflamatuvar ve emetin etkisi yok · (PDF'te geçmiyor)"),
    ],
)
