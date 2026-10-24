# -*- coding: utf-8 -*-
"""Kaynak: Drive › Komite-1 › PDF › Farmakoloji › 2026-2027(yeni) › Akif Hakan Kurt › 8-Antitrombositik ve Fibrinolitik İlaçlar"""

from yardim import B, C, Q  # noqa: F401

BOLUM = dict(
    key="antitrombositik", baslik="Antitrombositik ve Fibrinolitik İlaçlar",
    hoca="Prof. Dr. Akif Hakan Kurt", tarih="6 ve 12 Ekim", saat="4 saat",
    kaynak="8-Antitrombositik ve Fibrinolitik İlaçlar · Prof. Dr. A. H. Kurt · 2026",
    ozet=["Son 4 yıl her yıl **antiagregan ilaç + mekanizma eşleştirmesi** soruldu: **GP IIb/IIIa blokajı** (eptifibatid, absiksimab, tirofiban), **dipiridamol** (fosfodiesteraz inh. + adenozin yıkımı), **klopidogrel** (ADP reseptörü, irreversibl).",
          "Çeldiriciler hep aynı: **varfarin, aspirin, dipiridamol, epoprostenol, alteplaz** — mekanizmaları birbirine karıştırma.",
          "Fibrinolitikler (streptokinaz, alteplaz…) sınavda yalnızca **çeldirici** olarak geçti."],
    slaytlar=[
        [
            C("Trombosit ve agregasyon", [
                B("Trombositler **hemostaz** ve **trombus oluşumunda** önemli. Aktive olunca endotel lezyonuna **adezyon**, birbirlerine **agregasyon** yapar."),
                B("Yapışan trombositler **trombin, ADP ve TXA2** salıverir → diğer trombositleri toplar; ayrıca pıhtılaşma faktörleriyle pıhtılaşma sağlanır."),
                B("Agonistler (trombin, ADP, TXA2) trombosit yüzeyinde **en çok bulunan reseptör olan GP IIb/IIIa**'nın konfigürasyonunu değiştirip aktive eder."),
                B("GP IIb/IIIa'nın doğal ligandları: **fibrinojen** ve **von Willebrand faktörü**. Fibrinojen iki trombosit arasında **çapraz bağ** kurarak agregasyon yapar."),
            ]),
            C("Agregasyonu indükleyen / inhibe eden mediyatörler", [
                B("**İndükleyen**: trombin, ADP, TXA2, PAF, 5-HT, kollajen, adrenalin, Ca²⁺."),
                B("**İnhibe eden**: NO, PGI2, adenozin, sAMP."),
            ]),
            C("Klinik önem ve ilaç grupları", [
                B("Arter çeperinde trombus (tromboz) hasarlı bölgeye trombosit yapışmasıyla olur; kopan emboli **beyin (inme), kalp (MI), akciğer** kapillerini tıkayıp iskemi yapar."),
                B("**Antitrombositik ilaçlar**: 1) **Aspirin** 2) **Klopidogrel, tiklopidin** 3) **GP IIb/IIIa inhibitörleri** 4) **Dipiridamol** 5) **Epoprostenol (prostasiklin)**."),
                B("Bu ilaçlar **kanama süresini uzatır**."),
            ]),
        ],
        [
            C("Aspirin — mekanizma ve doz", [
                B("**Düşük doz (75-300 mg)**: trombosit **siklooksijenazını selektif ve irreversibl** inhibe eder → **TXA2 sentezini önler**."),
                B("Bu dozlarda **endotel hücresindeki prostasiklin** sentezine dokunmaz; **agregasyonu azaltır, adezyona dokunmaz**."),
                B("**Yüksek doz (3 g ve üstü)**: damar endotelindeki COX'u da inhibe eder → **PGI2 azalır**, antiagregan etki **zayıflar**."),
                B("Trombosit COX'unun **529. serin** aminoasidinin OH grubunu **asetiller** → geri dönüşümsüz inhibisyon."),
            ]),
            C("Trombositin endotelden daha çok etkilenmesinin 2 nedeni", [
                B("**1-** Trombositin **çekirdeği yok** → inhibe COX-1 **rejenere olamaz** (trombosit ömrü **8-10 gün**); endotel hücresi çekirdekli, **yeni COX-1 sentezler**."),
                B("**2-** Portal dolaşımdaki aspirin trombosit COX-1'ini asetiller; **karaciğerden çıkan kanda asetil grubunu kaybedip salisilat** olur → **endotel COX-1'ini inhibe edemez**."),
            ]),
            C("Aspirin ve NSAİ ilaç farkı", [
                B("Tüm NSAİ ilaçlar trombosit COX'unu inhibe edip kanama süresini uzatabilir, ancak etkileri **geri dönüşümlüdür** (ilaç uzaklaşınca kaybolur)."),
            ]),
        ],
        [
            C("Aspirin — endikasyon ve yan etki", [
                B("Endikasyon: **serebrovasküler** (serebral iskemi) ve **kardiyovasküler** komplikasyonlar; **MI tekrarını önler**, mortaliteyi düşürür."),
                B("Akut olmayan profilakside **75-150 mg/gün** yeterli. Akutta **yükleme 200-300 mg** tek doz oral, sonra **75-150 mg idame**."),
                B("Yan etki: **mide ülseri ve kanama**. Tek doz **300 mg** oral → kanama süresinde **4-7 gün** uzama. Kanama riskinde kullanılmaz."),
            ]),
            C("Klopidogrel (Plavix) ve tiklopidin (Ticlid)", [
                B("Trombositlerdeki **ADP reseptörlerini irreversibl** inhibe ederek trombosit aktivasyonunu engeller.", y="23-24"),
                B("**Sekonder inme profilaksisi** ve **unstabil anjina**; **aspirinle birlikte sinerjistik** etki."),
                B("En sık yan etki: **diyare ve cilt döküntüsü**; en ciddi: **trombositopeni ve lökopeni** (klopidogrel tiklopidin kadar yapmaz → üstün)."),
                B("**Tiklopidin** yan etkisi fazla olduğu için bugün pek tercih edilmez."),
                B("**Klopidogrel günde 75 mg** tek doz, genellikle aspirinle beraber."),
            ]),
        ],
        [
            C("Trombosit GP IIb/IIIa reseptör inhibitörleri", [
                B("Reseptörler fibrinojen aracılığıyla çapraz bağ yaparak agregasyon sağlar; **inhibisyonu agregasyonu baskılar**.", y="25-26 22-23"),
                B("**İ.v.** uygulanır, **pahalı** ilaçlardır."),
                B("**Absiksimab**: GP IIb/IIIa'ya karşı **monoklonal antikor**; reseptörü **irreversibl** kapatır; ayrıca **vitronektin reseptörlerini** (endotel, düz kas, trombositte integrin) de bloke eder.", y="25-26"),
                B("**Eptifibatid**: GP IIb/IIIa **blokörü**; **akut koroner sendrom** ve **perkütanöz koroner girişimde** i.v. infüzyon.", y="22-23"),
                B("**Tirofiban**: GP IIb/IIIa blokörü; **i.v. infüzyon**.", y="25-26"),
            ]),
            C("Dipiridamol (Drisentin, Tromboliz)", [
                B("Trombositlerde **fosfodiesterazı inhibe** edip **sAMP'yi artırır** → Ca²⁺ girişi azalır → adezyon ve agregasyon inhibe olur.", y="24-25"),
                B("Ayrıca **adenozinin yıkımını engelleyerek** antiagregan etki yapar.", y="24-25"),
                B("Tek antitrombotik endikasyon: **protez kalp kapakçığı** takılanlarda trombus önleme; **aspirin veya oral antikoagülanlarla kombine**."),
            ]),
            C("Epoprostenol (prostasiklin)", [
                B("**Böbrek hastalarında diyaliz** sırasında diyaliz borularına trombosit yapışmasını önlemek için **i.v. infüzyon**."),
                B("Eliminasyon yarı ömrü çok kısa (**3 dk**). Yan etki: **yüzde kızarma, sıcaklık hissi, hipotansiyon, baş ağrısı**."),
            ]),
        ],
        [
            C("Antitrombositik ilaçların endikasyonları", [
                B("1) **Akut MI** profilaksisi · 2) **akut koroner sendrom**."),
                B("3) Koroner **bypass** sonrası **greft tıkanmasının önlenmesi**."),
                B("4) **Geçici iskemik nöbetlerin** sekonder profilaksisi · 5) **Unstabil anjinada** MI oluşumunun önlenmesi."),
                B("6) Gebelikte **preeklampsinin önlenmesi**."),
                B("7) **Protez kalp kapakçığında** trombüs önleme · 8) **Diyaliz** borularında trombosit yapışmasını önleme."),
            ]),
            C("Fibrinolitik (trombolitik) ilaçlar — genel", [
                B("**Fibrinoliz** = pıhtılaşma sonucu oluşan **fibrinin kimyasal olarak parçalanması** ile pıhtının erimesi."),
                B("Fibrini eriten proteolitik enzim: **plazmin**; plazmada **791 a.a.'lik tek zincirli plazminojen** prekürsörü halinde bulunur."),
                B("Endojen **plazminojen aktivatörleri**: **doku plazminojen aktivatörü (t-PA)** ve **ürokinaz**."),
                B("İlaçlar: **1) streptokinaz 2) ürokinaz 3) alteplaz (rt-PA) 4) reteplaz 5) tenekteplaz 6) anistreplaz**. Ortak özellik: **plazminojenin plazmine dönüşümü**."),
            ]),
        ],
        [
            C("Streptokinaz (Streptase)", [
                B("**C grubu β hemolitik streptokoklardan** elde edilir; **plazminojenle kompleks** yapıp plazmine dönüşümünü aktive eder."),
                B("Trombustaki fibrine yapışık plazminojenin yanında **dolaşımdaki serbest plazminojeni de** aktive eder → istenmeyen; **hiperplazminemiye bağlı kanama**."),
                B("**Antijenik özelliği çok yüksek**: hipotansiyon, deri döküntüsü, ateş, **anafilaktik reaksiyon**."),
            ]),
            C("Ürokinaz (Abbokinas, Ukidan)", [
                B("Endojen olarak **sadece böbrek tübül hücresinde** üretilir; böbrek ve üriner sistemde fibrinolitik etkiye katkı."),
                B("**İnsan fötal böbrek hücre kültürlerinden** elde edilir; **fibrin ve fibrinojenin ikisini de** yıkar."),
                B("En önemli yan etki **kanama**. **Kullanımdan kaldırılmıştır**."),
            ]),
            C("Alteplaz (rt-PA; Actilyse)", [
                B("Endotelde sentezlenen maddenin **rekombinant DNA** preparatı. **Fibrine bağlı plazminojeni hızla aktive eder (fibrin selektif)** → sadece trombusta lokal fibrinoliz, serbest fibrinojeni pek aktive etmez."),
                B("Kullanım: **MI, masif pulmoner emboli, akut iskemik felç**. Eski pıhtıları streptokinaz ve ürokinaza göre **daha iyi** parçalar."),
                B("Avantaj: **allerjik yan etkisi az**. Komplikasyon: **GİS ve serebral kanama**."),
            ]),
        ],
        [
            C("Fibrinolitiklerde ek bilgi ve endikasyonlar", [
                B("Fibrinolitikler ilk **24 saat** içinde trombini aktive ederek **paradoksik hiperkoagülasyon** yapabilir."),
                B("Endikasyon: **akut MI**, **akciğer embolisi**, **DVT** (özellikle **ilk 72 saat**), **periferik arter trombozu**, kalp kapakçığı protezine bağlı tromboz önleme, **unstabil anjina**."),
            ]),
            C("Fibrinolitiklerin yaptığı kanamaların tedavisi", [
                B("**Taze dondurulmuş plazma** veya **tam kan**."),
                B("**Aprotinin**: fibrinolizin inhibitörü."),
                B("**Aminokaproik asit ve traneksamik asit**: plazminojen aktivasyonunu **kompetitif** inhibe eder."),
                B("**Desmopressin** (ADH analoğu): **faktör VIII aktivitesini artırır**."),
            ]),
        ],
    ],
    sorular=[
        Q("25-26", 24, "Trombosit GP IIb/IIIa reseptörünü bloke ederek antiagregan etki yapan hangisidir?",
          "Absiksimab ve tirofiban (A ve D)",
          "PDF'te ikisi de GP IIb/IIIa inhibitörü; dipiridamol=PDE inh., epoprostenol=prostasiklin, alteplaz=fibrinolitik. Anahtar şıkkı belirsiz."),
        Q("24-25", 33, "Trombositlerde fosfodiesterazı inhibe edip adenozin yıkımını engelleyerek antiagregan olan hangisidir?",
          "Dipiridamol",
          "Eptifibatid=GP IIb/IIIa, varfarin=K vit. antagonisti, klopidogrel=ADP reseptörü, aspirin=COX."),
        Q("23-24", 19, "ADP reseptörlerini irreversibl inhibe ederek trombosit aktivasyonunu önleyen ilaç hangisidir?",
          "Klopidogrel",
          "Eptifibatid=GP IIb/IIIa, dipiridamol=PDE inh., varfarin=K vit. antagonisti, aspirin=COX."),
        Q("22-23", 30, "GP IIb/IIIa reseptörlerini bloke ederek trombosit agregasyonunu önleyen ilaç hangisidir?",
          "Eptifibatid",
          "Dipiridamol=PDE inh., klopidogrel=ADP reseptörü, varfarin=K vit. antagonisti, aspirin=COX."),
    ],
)
