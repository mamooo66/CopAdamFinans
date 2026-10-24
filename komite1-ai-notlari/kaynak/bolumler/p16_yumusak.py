# -*- coding: utf-8 -*-
"""Kaynak: Drive › Komite-1 › PDF › Patoloji › 2026-2027(yeni) › Songül Petek Özer › 1-Yumuşak Doku Tümörleri (65 slayt)"""

from yardim import B, C, Q  # noqa: F401

BOLUM = dict(
    key="yumusak", baslik="Yumuşak Doku Tümörleri",
    hoca="Dr. Öğr. Üyesi Songül Peltek Özer", tarih="12 Ekim", saat="1 saat",
    kaynak="1-Yumuşak Doku Tümörleri · Dr. Öğr. Üyesi S. Peltek Özer · 2026",
    ozet=["Son 5 yılda bu dersten **3 soru** çıktı: **25-26** RMS, **24-25** leiomyosarkom, **22-23** metastaz yapmayan tümör (desmoid).",
          "**Gençlerde en sık yumuşak doku sarkomu = RMS** (embriyonal tip en sık, 10 yaş altı); çeldiriciler liposarkom, anjiosarkom, Kaposi, MFH.",
          "**Desmoid (fibromatoz)** lokal infiltratif, nüks eder → “metastaz yapmaz” şıkkı; **RMS lenf nodu metastazı yapabilir**."],
    slaytlar=[
        # 1 — genel bilgiler (slayt 4, 7)
        [
            C("Tanım ve yerleşim (slayt 4)", [
                B("**Mezenkimal kökenli nonepitelial** dokudan köken alır (**iskelet sistemi hariç**)."),
                B("**Kas, yağ, fibröz doku, damar ve periferik sinirlerin** tümörleridir."),
                B("**%40 alt ekstremiteden** (uyluk-kalça), **%30 gövde ve retroperitondan**, **%10 baş-boyundan** ortaya çıkar."),
            ]),
            C("Etiyopatogenez ve sendromlar (slayt 4)", [
                B("Etiyopatogenez: **radyasyon**, **kimyasal ve termal yanıklar**, **travma**, **fenoksiherbisid**, **klorofenol**, **HHV-8**."),
                B("Sendromlar: **Li-Fraumeni**, **NF-1**, **Gardner**, **Osler-Weber-Rendu**."),
            ]),
            C("Sınıflama (slayt 5-6; PDF'te İngilizce liste)", [
                B("**Yağ dokusu**: lipomlar · **liposarkom**."),
                B("**Fibröz doku** (tümörler ve tümör benzeri lezyonlar): **nodüler fasiit** · **fibromatozlar** (yüzeyel, derin) · **fibrosarkom**."),
                B("**Fibrohistiositik**: fibröz histiositom · **dermatofibrosarkoma protuberans** · **malign fibröz histiositom**."),
                B("**İskelet kası**: rabdomiyom · **rabdomiyosarkom**."),
                B("**Düz kas**: leiomyom · malign potansiyeli belirsiz düz kas tümörleri · **leiomyosarkom**.", y="24-25"),
                B("**Damar**: hemanjiom · lenfanjiom · hemanjioendotelyom · hemanjioperisitom · **anjiosarkom**."),
                B("**Periferik sinir**: nörofibrom · schwannom · granüler hücreli tümör · **malign periferik sinir kılıfı tümörü**."),
                B("**Histogenezi belirsiz**: **sinovyal sarkom** · alveolar soft part sarkom · epitelioid sarkom · **undiferansiye pleomorfik sarkom**."),
            ]),
            C("Ders akışı (slayt 7)", [
                B("**Fibröz** · **fibrohistiositik** · **lipomatöz** · **düz kas** · **çizgili kas** · **damar** · **perivasküler** · **snovial** tümörler."),
            ]),
        ],
        # 2 — lipomatöz tümörler (slayt 8-18)
        [
            C("Lipom (slayt 8-13)", [
                B("**Erişkin çağın en sık yumuşak doku tümörü**."),
                B("En sık **subkutan** dokudan çıkar; sıklıkla **tek, sporadik ve ağrısız**."),
                B("Tipleri: **klasik tip**, **anjiyolipom**, **kondrolipom**, **miyolipom**."),
                B("**Sırt, omuz, proksimal ekstremite, abdomende** ağrısız subkutan kitle."),
                B("**Anjiyolipom önkolda ve ağrılı**."),
                B("**GİS, oral kavite, intramusküler** pek çok yerde görülebilir (slayt 11: ince barsakta lipom)."),
            ]),
            C("Hibernom (slayt 14)", [
                B("**Kahverengi yağ dokusunun** tümörü; **çocukta** izlenir."),
                B("En sık yerleşim: **arka boyun ve retroperiton**."),
                B("**Eksizyon sonrası rekürrens veya malignleşme beklenmez**."),
            ]),
            C("Liposarkom — genel (slayt 16-18)", [
                B("**Yağ dokusunun malign tümörü**; en sık **5-6. dekatta**."),
                B("**Alt ekstremite ve abdomen** başta olmak üzere **derin dokular ve visseral bölgelerden** çıkar."),
                B("Alt tipleri: **atipik lipomatöz tümör / iyi diferansiye liposarkom**, **miksoid**, **pleomorfik**, **dediferansiye** liposarkom."),
                B("Mikroskopi görseli: **lipoblast** (slayt 18)."),
            ]),
        ],
        # 4 — liposarkom alt tipleri (slayt 19-25)
        [
            C("İyi diferansiye liposarkom (slayt 19, 25)", [
                B("Yerleşim: **retroperiton, uyluk**."),
                B("**Lipoma benzer**; **fibröz bantlar**, **vasküler yapılar**, **mitoz**, **pleomorfik hücreler**; **mitoz ≤ 4 / 10 HPF**."),
                B("**Çoğu nonmetastatik**, **lokal nükslerle** seyreder."),
                B("**%10'u dediferansiye** olarak **yüksek grade** lezyonlara döner."),
            ]),
            C("Dediferansiye liposarkom (slayt 21)", [
                B("**Retroperiton**; **yüksek mitoz**; **survi kötü**."),
                B("**MDM2 / CDK4 amplifikasyonu**."),
            ]),
            C("Pleomorfik liposarkom (slayt 20)", [
                B("**Pleomorfik hücreler**; **belirgin mitoz**, **atipik mitozlar**."),
                B("**Kapsülsüz, çok hızlı büyüyen retroperitoneal kitle**."),
                B("**MDM2 / CDK4 negatif**."),
            ]),
            C("Miksoid liposarkom (slayt 22-23)", [
                B("Yerleşim: **uyluk**; **miksoid zemin**."),
                B("**Dallanan kapillerler** (**kaz ayağı paterni**)."),
                B("**İyi diferansiye görünümde lipoblastlar**; **DDIT3 pozitif**."),
            ]),
        ],
        # 5 — fibroblastik tümörler (slayt 26-34)
        [
            C("Nodüler fasiit (slayt 26-30)", [
                B("**Reaktif fibroblastik proliferasyon**; **sarkomlarla karıştırılabilir**."),
                B("**En sık görülen pseudosarkomatöz proliferasyon**."),
                B("En sık **önkol volar yüzde**; **hızlı büyür**, bazen **ağrılıdır**."),
                B("En sık **üst ekstremite ve gövdede**; **%15'i travmayı takiben** gelişir."),
                B("Tedavi: **basit eksizyon**."),
            ]),
            C("Fibromatozlar (slayt 31-33)", [
                B("**Lokal infiltratif büyüyen** bir grup fibroblastik proliferasyon.", y="22-23"),
                B("**Cerrahi çıkarılma sonrası sıklıkla nüks** ederler.", y="22-23"),
                B("**Yüzeyel** ve **derin** tipleri vardır."),
                B("Yüzeyel fibromatozların en iyi bilinenleri:"),
                B("**Palmar fibromatozis** (**Dupuytren kontraktürü**)", lvl=1),
                B("**Penil fibromatozis** (**Peyronie kontraktürü**)", lvl=1),
                B("**Fibromatosis colli** (**konjenital tortikolis**)", lvl=1),
            ]),
            C("Desmoid tümör (slayt 34)", [
                B("**Desmoid tümör** (slayt 2'de “desmoid fibromatosis”; sınavda “derin fibromatozis” şıkkı): **ekstremitede, abdomende** görülür.", y="22-23"),
                B("**FAP'lı hastalarda operasyon sonrası** görülebilir."),
                B("**β-katenin nükleer pozitif**."),
            ]),
        ],
        # 6 — UPS, fibrohistiositik tümörler (slayt 35-39)
        [
            C("Undiferansiye pleomorfik sarkom (slayt 35-36)", [
                B("**Herhangi bir lokalizasyonda**, **yaşlılarda**."),
                B("**İmmünler**: diğer sarkomatöz lezyonları **dışlamak için**."),
                B("**Radyasyon sonrası** gelişim."),
                B("Slayt 35 (görsel liste) **undifferentiated pleomorphic sarcoma** ile biter; liste ek slaytlarda."),
            ]),
            C("Fibröz histiositom — dermatofibrom (slayt 37)", [
                B("Sıklıkla **deri ve subkutan dokuda** izlenir."),
                B("En sık **erişkinlerde** görülür."),
                B("**Eksizyon kür sağlar**."),
            ]),
            C("Dermatofibrosarkoma protuberans — DFSP (slayt 38-39)", [
                B("**Borderline malignensi**."),
                B("Sıklıkla **dermis ve subkutiste yavaş büyüyen nodüler lezyonlar** yapar."),
                B("Mikroskopi (slayt 39): **honeycomb patern**, **kollajenöz stroma**, **damarlar**, **hemosiderin pigmenti**."),
                B("**CD34 pozitifliği**."),
            ]),
        ],
        # 7 — çizgili kas tümörleri (slayt 40-47)
        [
            C("Rabdomiyosarkom — RMS (slayt 40-41)", [
                B("**Gençlerde görülen en sık yumuşak doku sarkomu RMS**'dur.", y="25-26"),
                B("**Desmin**, **myogenin**, **myoD1** pozitifliği."),
                B("En sık **ekstremitelerin derin kas grupları** ve **retroperitoneal bölgeyi** tutar."),
                B("**Agresif** tümörlerdir; **lenf nodu metastazı yapabilir**.", y="22-23"),
            ]),
            C("RMS tipleri (slayt 42-44)", [
                B("**Embriyonal RMS**: **en sık görülen tip**; **10 yaş altı çocuklarda**."),
                B("**Alveoler RMS**: görülme yaşı **10-25**."),
                B("**Pleomorfik RMS**: **nadir**; **yetişkinde** görülür."),
            ]),
            C("Embriyonal RMS — sarcoma botryoides (slayt 45-46)", [
                B("**Vajende; baş-boyun (burun, kulak)** bölgesinde **yumuşak, jelatinöz, üzüm görüntüsünde dışarı sarkan kitleler** → **“sarcoma botryoides”**."),
                B("Slayt 46: **Nicholson'un cambium tabakası** (altyazı: safra kanalı)."),
            ]),
            C("Rabdomiyom (slayt 47)", [
                B("**Çizgili kasın benign tümörü**; en sık **baş-boyun** bölgesinde."),
                B("**Kardiyak rabdomiyomlar tuberos sklerozla** birliktelik gösterebilir."),
            ]),
        ],
        # 8 — sinovyal sarkom, düz kas, periferik sinir (slayt 48-56)
        [
            C("Sinovyal sarkom (slayt 48-50)", [
                B("**Eklemlerde** görülen **malign** tümörlerdir."),
                B("Histoloji: **fibroblast tipinde iğsi hücreler** + **epitelial hücreler** → **bifazik** büyüme paterni."),
                B("**Hem keratin hem de vimentin pozitif**."),
            ]),
            C("Düz kas tümörleri (slayt 51-53)", [
                B("Sınıflamada: **leiomyom**, **malign potansiyeli belirsiz düz kas tümörleri**, **leiomyosarkom**.", y="24-25"),
                B("Slaytlarda yalnızca görseller var: **leiomyoma** (slayt 51-52), **leiomyosarcoma** (slayt 53)."),
            ]),
            C("Periferik sinir kılıfı tümörleri (slayt 54)", [
                B("**Benign**: **schwannom**, **nörofibrom**."),
                B("**Malign**: **malign periferik sinir kılıfı tümörü**."),
            ]),
            C("Damar tümörleri (slayt 57-60, 64-65)", [
                B("**Benign**: **hemanjiom**, **lenfanjiom**."),
                B("**Malign**: **anjiosarkom**, **Kaposi sarkomu**."),
                B("Görsel örnekler: **infantil hemanjioendotelioma** (slayt 58), **kavernöz hemanjioma** (slayt 59), **pyojenik granülom** (slayt 60)."),
                B("**Anjiosarkom**: slayt 64-65'te yalnızca görseller."),
            ]),
            C("Kaposi sarkomu (slayt 61-63)", [
                B("Etken: **Human herpes virus 8 (HHV-8)**; **4 tip** vardır:"),
                B("**Klasik tip**: yaşlılarda görülür.", lvl=1),
                B("**Lenfadenopatik tip** (Afrika tipi, endemik tip).", lvl=1),
                B("**Transplantlarda görülen tip**.", lvl=1),
                B("**AIDS ile ilişkili tip**.", lvl=1),
            ]),
        ],
        # 10 — ek: WHO 5. baskı (slayt 2) — adipositik + fibroblastik
        [
            C("Ek · WHO 5. baskı — Adipositik tümörler (slayt 2)", [
                B("Lipomatosis · Lipomatosis of nerve · Lipoblastoma and lipoblastomatosis · Lipoblastoma-like tumour · **Angiolipoma** · Myolipoma of soft tissue · Chondroid lipoma"),
                B("Spindle cell lipoma and pleomorphic lipoma · **Hibernoma** · Atypical spindle cell / pleomorphic lipomatous tumour"),
                B("**Atypical lipomatous tumour / well-differentiated liposarcoma** · **Dedifferentiated liposarcoma** · **Myxoid liposarcoma** · **Pleomorphic liposarcoma** · Myxoid pleomorphic liposarcoma"),
            ]),
            C("Ek · Fibroblastik ve miyofibroblastik tümörler (slayt 2)", [
                B("**Nodular fasciitis** · Proliferative fasciitis and proliferative myositis · Myositis ossificans and fibro-osseous pseudotumour of digits · Ischaemic fasciitis · Elastofibroma"),
                B("Fibrous hamartoma of infancy · **Fibromatosis colli** · Juvenile hyaline fibromatosis · Calcifying fibrous tumour · Inclusion body fibromatosis · Fibroma of tendon sheath"),
                B("Desmoplastic fibroblastoma · Myofibroblastoma · Calcifying aponeurotic fibroma · SMAD3-rearranged fibroblastic tumour · PRRX1-rearranged fibroblastic tumour"),
                B("Angiomyofibroblastoma · Cellular angiofibroma · Angiofibroma of soft tissue · Nuchal-type fibroma · Acral fibromyxoma · Gardner fibroma"),
                B("**Palmar and plantar fibromatosis** · **Desmoid fibromatosis** · Lipofibromatosis · Giant cell fibroblastoma"),
                B("**Dermatofibrosarcoma protuberans** · Solitary fibrous tumour · Inflammatory myofibroblastic tumour"),
            ]),
        ],
        # 11 — ek: WHO 5. baskı (slayt 2 sonu = slayt 35, slayt 3) — fibroblastik devamı, histiositik, perisitik, düz kas, iskelet kası
        [
            C("Ek · Fibroblastik listenin devamı (slayt 2'nin sonu = slayt 35)", [
                B("Low-grade myofibroblastic sarcoma · Superficial CD34-positive pleomorphic fibroblastic tumour · Myxoinflammatory fibroblastic sarcoma · Nodular necrotizing fibroblastic tumour"),
                B("Infantile fibrosarcoma · **Myxofibrosarcoma** · Low-grade fibromyxoid sarcoma · Sclerosing epithelioid fibrosarcoma · **Undifferentiated pleomorphic sarcoma**"),
            ]),
            C("Ek · Fibrohistiositik ve sinovyal tümörler (slayt 3)", [
                B("Tenosynovial giant cell tumour · Chondroid synoviocytic neoplasm · Plexiform fibrohistiocytic tumour · Giant cell tumour of soft tissue · Keratin-positive giant cell-rich tumour"),
            ]),
            C("Ek · Perisitik (perivasküler) tümörler (slayt 3)", [
                B("Glomus tumour · Myopericytoma, including myofibroma · SRF-rearranged myoid neoplasm · Angioleiomyoma"),
            ]),
            C("Ek · Düz kas tümörleri (slayt 3)", [
                B("**Leiomyoma** · EBV-associated smooth muscle tumour · **Leiomyosarcoma**"),
            ]),
            C("Ek · İskelet kası tümörleri (slayt 3)", [
                B("**Rhabdomyoma** · Inflammatory rhabdomyoblastic tumour · **Embryonal rhabdomyosarcoma** · **Alveolar rhabdomyosarcoma** · **Pleomorphic rhabdomyosarcoma**"),
                B("Fusion-associated spindle cell rhabdomyosarcomas · MYOD1-mutant spindle cell / sclerosing rhabdomyosarcoma"),
            ]),
        ],
        # 12 — ek: WHO 5. baskı (slayt 3) — GİST, kondro-osseöz, periferik sinir, belirsiz farklılaşma
        [
            C("Ek · GİST ve kondro-osseöz tümörler (slayt 3)", [
                B("**Gastrointestinal stromal tumour** · SDH-deficient gastrointestinal stromal tumour"),
                B("Kondro-osseöz: Soft tissue chondroma · Extraskeletal osteosarcoma"),
            ]),
            C("Ek · Periferik sinir kılıfı tümörleri (slayt 3)", [
                B("**Schwannoma** · **Neurofibroma** · Perineurioma · Granular cell tumour · Dermal nerve sheath myxoma · Solitary circumscribed neuroma"),
                B("Ectopic meningioma and meningothelial hamartoma · Benign triton tumour / neuromuscular choristoma · Hybrid nerve sheath tumour"),
                B("**Malignant peripheral nerve sheath tumour** · Epithelioid malignant peripheral nerve sheath tumour · Malignant melanotic nerve sheath tumour"),
            ]),
            C("Ek · Farklılaşması belirsiz tümörler (slayt 3)", [
                B("Intramuscular myxoma · Juxta-articular myxoma · OGT-rearranged mesenchymal neoplasm · Deep (aggressive) angiomyxoma · Acral fibrochondromyxoid tumour"),
                B("Angiomatoid fibrous histiocytoma · Ossifying fibromyxoid tumour · Myoepithelioma, myoepithelial carcinoma, and mixed tumour"),
                B("Pleomorphic hyalinizing angiectatic tumour of soft parts · Haemosiderotic fibrolipomatous tumour · Phosphaturic mesenchymal tumour · GLI1-altered mesenchymal tumour"),
                B("Kinase-altered spindle cell neoplasms · NUT-rearranged sarcoma · PATZ1-rearranged sarcoma"),
                B("**Synovial sarcoma** · Epithelioid sarcoma · Alveolar soft part sarcoma · FET-CREB family epithelioid mesenchymal tumours · Clear cell sarcoma of soft tissue"),
                B("Extraskeletal myxoid chondrosarcoma · Desmoplastic small round cell tumour · Extrarenal rhabdoid tumour · PEComa · Intimal sarcoma"),
            ]),
        ],
    ],
    sorular=[
        Q("25-26", 62, "Çocukluk çağının en sık görülen malign yumuşak doku tümörü?", "Rabdomiyosarkom",
          "PDF: “gençlerde en sık yumuşak doku sarkomu RMS”; embriyonal tip 10 yaş altı. Liposarkom, anjiosarkom, Kaposi, MFH değil"),
        Q("24-25", 85, "Hangisi yumuşak doku tümörüdür?", "Leiomyosarkoma",
          "Düz kas tümörü (slayt 5). Kondrosarkom, RCC, malign melanom, seminom PDF'in yumuşak doku listelerinde yok"),
        Q("22-23", 77, "Hangi tümör metastaz YAPMAZ?", "Desmoid tümör (derin fibromatozis)",
          "PDF: fibromatozlar lokal infiltratif, nüks eder; RMS lenf nodu metastazı yapabilir. “Metastaz yapmaz” cümlesi yok · (PDF'te geçmiyor)"),
    ],
)
