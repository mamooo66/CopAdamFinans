# -*- coding: utf-8 -*-
"""Kaynak: Drive › Komite-1 › PDF › Farmakoloji › 2026-2027(yeni) › Akif Hakan Kurt › 6-Farmakovijilans"""

from yardim import B, C, Q  # noqa: F401

BOLUM = dict(
    key="farmakovijilans", baslik="Farmakovijilans",
    hoca="Prof. Dr. Akif Hakan Kurt", tarih="7 Ekim", saat="1 saat",
    kaynak="6-Farmakovijilans · Prof. Dr. A. H. Kurt · 2026",
    ozet=["Son 5 yılda bu dersten **soru çıkmadı**.",
          "Çıkarsa muhtemel konular: **AİR / advers ilaç olayı / ciddi advers reaksiyon tanımları**, klinik denemelerin sınırlamaları, **spontan bildirim**, **MedWatch (FDA, 1993)**, **TADMER (1985)**."],
    slaytlar=[
        [
            C("Farmakovijilans (FV)", [
                B("**pharmacon + vigilancia** (1974): ilaca dair etkilerde **uyanık olma**."),
                B("**Advers etkilerin** ve ilaca ait diğer problemlerin **belirlenmesi, değerlendirilmesi, anlaşılması ve önlenmesine** yönelik bilimsel çalışma ve aktiviteler."),
                B("**İlaç güvenliliğinin toplum içinde incelenmesi**."),
            ]),
            C("Advers ilaç reaksiyonu (AİR)", [
                B("İnsanlarda hastalığın tedavisi, teşhisi, önlenmesi, fiziksel işlevin düzeltilmesi/modifikasyonu için kullanılan **normal dozlarda** ortaya çıkan, ilaca ait **zararlı, amaçlanmamış cevap**."),
                B("**Sebep-etki ilişkisi açık**. **Kasıtlı ilaç kullanımı (intihar ve diğer nedenler) ve zehirlenmeler tanımın dışında**."),
            ]),
            C("Advers ilaç olayı", [
                B("AİR'in aksine ilaç ile şüphe edilen etki arasında **sebep-etki ilişkisi tam ortaya konulmamıştır**."),
            ]),
            C("Ciddi advers reaksiyon", [
                B("**Ölüm**, **yaşamı tehdit eden durum**."),
                B("**Hastanede yatmaya ihtiyaç** duyan ya da mevcut **yatış süresini uzatan** durum."),
                B("**Kalıcı / önemli yetiyitimi (sakatlık)**."),
                B("**Konjenital anomali / doğum defekti** yapan AİR'ler."),
            ]),
        ],
        [
            C("AİR'in önemi", [
                B("Slayttaki sıralama (Lazarou, JAMA 1998): **1. kardiyovasküler hastalıklar · 2. kanser ve diğer neoplazmlar · 3. inme · 4. advers ilaç reaksiyonları** (pnömoni, diyabet, trafik kazalarından önce)."),
                B("AİR nedeniyle **hastaneye başvuru yüzdesi** (WHO 2002): **Norveç %11,5 · Fransa %13,0 · İngiltere %16,0**."),
                B("Ülkemize ekstrapolasyon zor: gelişmekte olan ülkelerde **düşük AİR bildirimi**, **substandart ve sahte ilaç**, **bağımsız bilgi eksikliği**, **akılcı olmayan ilaç kullanımı**."),
            ]),
            C("Klinik denemelerin sınırlamaları", [
                B("**Pre-klinik** çalışmalar (deney hayvanı) toksisite profilini gösterir; **öngörüsü kısıtlı**."),
                B("**Kısa süre**: kronik kullanımda gelişen etkiler belirlenemez."),
                B("**Dar popülasyon**: çocuklar, çocuk doğurma çağındaki kadınlar, yaşlılar genelde yok."),
                B("**Dar endikasyon aralığı**; **sınırlı karşılaştırma grubu** (genelde plasebo)."),
                B("**Küçük örneklem**: 1.000-5.000 özne."),
            ]),
            C("2.000 hastada AİR için eşik sayı ve olasılık", [
                B("**1/500** (azatiyoprin → lenfoma): olasılık **0,98**."),
                B("**1/1.000** (praktolol → göz hasarı): **0,86**."),
                B("**1/10.000** (penisilin → anafilaksi): **0,18**."),
                B("**1/50.000** (kloramfenikol → aplastik anemi): **0,04**."),
            ]),
        ],
        [
            C("Ruhsatlandırma ve ilaç faciaları", [
                B("İlaç ruhsatlandırması: **kalite, efikasi, güvenlik (?)**."),
                B("Halkta geniş yankı uyandıran facialar **modern ilaç düzenleyici yasalar için itici güç**: **pre- ve post-talidomit**."),
                B("**Sülfonamit eliksiri (1937)** → **Gıda, İlaç ve Kozmetik Yasası (1938)**."),
                B("**Talidomit epidemisi (1962)** → **Kefauver-Harris Tadilleri (1962)**; İngiltere'de **sarı kart sistemi**."),
            ]),
            C("Etken madde — advers etki (slayttaki liste; 1997-2001, rofekoksib 2004)", [
                B("**Deksfenfluramin, fenfluramin**: kalp kapakçığı problemleri."),
                B("**Terfenadin, astemizol, grepafloksasin**: ölümcül kalp aritmileri."),
                B("**Bromfenak**: ağır karaciğer hasarı · **Troglitazon**: hepatik yetmezlik."),
                B("**Mibefradil**: potansiyel zararlı etkileşimler · **Fenilpropanolamin**: hemorajik inme."),
                B("**Sisaprid**: ciddi kardiyak advers etkiler · **Serivastatin**: rabdomiyoliz."),
                B("**Rapaküronyum**: bronkospazm · **Rofekoksib**: kalp krizi ve inme."),
            ]),
        ],
        [
            C("FV veri kaynakları", [
                B("Pazarlama öncesi denemeler · **spontan bildirim sistemleri** · otomatik veritabanları · ad hoc veri toplama."),
                B("Yayınlanmış literatür ve ilaç bültenleri · firma sponsorluğunda çalışmalar · ilaç kullanım çalışmaları · **farmakoepidemiyolojik metodlar**."),
            ]),
            C("Spontan bildirim sistemleri", [
                B("Piyasaya çıktıktan sonra **AİR belirlemenin başlıca yolu**: sağlık çalışanlarının **gönüllü bildirimi**."),
                B("**Nadir olaylar** (fulminan karaciğer yetmezliği, rabdomiyoliz) için **uygun**."),
                B("**Yaygın rahatsızlıkların** (kalp krizi, inme) **artmış insidansını** belirlemek **daha zor**."),
            ]),
            C("MedWatch (FDA, 1993)", [
                B("Advers olayların (**tıbbi cihazlar dahil**) **gönüllü bildirimine** dayanan program."),
                B("Başarıları: **Chaparral** (diyet suplemanı) → hepatotoksisite; **Norplant** (implante kontraseptif) → uygulama yeri infeksiyonu, trombositopeni; **fenfluramin + fentermin** → kalp kapakçığı rahatsızlığı."),
            ]),
        ],
        [
            C("Rofekoksib örneği (30 Eylül 2004)", [
                B("**FDA endikasyonları (Mayıs 1999)**: osteoartrit semptomları, yetişkinde akut ağrı, menstrüel semptomlar, yetişkin ve çocukta romatoid artrit semptomları."),
                B("Firma açıklaması: **kalp krizi ve inme** gibi KV olayların göreli riski, tedavi başlangıcından **18 ay sonra plaseboya göre arttı** → klinik deneme durduruldu."),
                B("**80'den fazla ülkede** pazarlanmıştı (1999-); 2003'te dünya çapında satışı **2,5 milyar dolar**."),
            ]),
            C("FV her ülke için gereklidir", [
                B("Ülkeler / bölgeler arası farklar: **hastalık sıklığı ve reçeteleme pratikleri**; ilaç üretim süreci (ürün ve bileşimi etkiler); **geleneksel ve tamamlayıcı tıp (bitkisel) ürünlerle etkileşmeler**."),
            ]),
            C("Türkiye'de FV", [
                B("**1985: TADMER** (Türk İlaç Advers Etkilerini İzleme ve Değerlendirme Merkezi)."),
                B("**1987**: TADMER, **DSÖ Uluslararası İlaç İzleme İşbirliği Merkezi'ne** üyeliğe kabul edildi; klinik araştırma yönetmeliği yayınlandı."),
                B("**1999**: TADMER “Avrupa FV Toplantısı”; “İlaç Advers Etkilerinin İzlenmesi Hakkında Yönetmelik” (2000-200?)."),
            ]),
            C("Sonuç", [
                B("İlaca bağlı istenmeyen olaylar **başlıca halk sağlığı problemi**; AİR'ların anlaşılması ve önlenmesi **ulusal öncelikli** konudur."),
                B("Tüm sağlık çalışanları FV'nin hasta bakımı ve sağlık bütçesine katkısını anlamalı; **spontan bildirim ve bildirimlerin kalitesi** önemlidir."),
            ]),
        ],
    ],
    sorular=[],
)
