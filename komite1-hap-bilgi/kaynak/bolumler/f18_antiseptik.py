# -*- coding: utf-8 -*-
"""Kaynak: Drive › Komite-1 › PDF › Farmakoloji › 2026-2027(yeni) › Oruç Yunusoğlu › 9-Antiseptik ve Dezenfektanlar"""

from yardim import B, C, Q  # noqa: F401

BOLUM = dict(
    key="antiseptik", baslik="Antiseptik ve Dezenfektanlar",
    hoca="Doç. Dr. Oruç Yunusoğlu", tarih="16 Ekim (program)", saat="1 saat",
    kaynak="9-Antiseptik ve Dezenfektanlar · Doç. Dr. O. Yunusoğlu · 2026",
    ozet=["Son 5 yılda bu dersten **2 soru** çıktı (23-24, 24-25): **üriner antisepsi** (metenamin) ve **yiyeceklerde koruyucu** — ikisinin doğru cevabı da **bu yılki PDF’te geçmiyor**.",
          "Bu yılki PDF **kavram + ajan karşılaştırması** ağırlıklı: antiseptik / dezenfektan / sterilizasyon farkı, Spaulding, alkol-iyot-klor-klorheksidin-H₂O₂ mekanizma, spor ve klinik kullanım.",
          "Aynı şık grubu iki yılda tekrarlandı (borik asit, formaldehit, metenamin, izopropanol, metaraminol); **formaldehit PDF’te dezenfektan** (toksik, irritan, kullanımı sınırlı), **izopropanol alkol**."],
    slaytlar=[
        [
            C("Temel kavramlar", [
                B("Sistemik antibiyotiklerden farklı olarak **selektiviteleri düşüktür**; mikroorganizmalar yanında **insan hücrelerine de zarar** verebilir."),
                B("Genellikle **lokal veya yüzeysel** kullanılırlar."),
                B("**Antiseptik**: **canlı dokulara** uygulanan antimikrobik madde."),
                B("**Dezenfektan**: **cansız yüzey ve materyallerde** mikroorganizmaları azaltmak/öldürmek için kullanılan madde."),
                B("**Jermisid**: mikroorganizmaları öldüren **genel terim**."),
            ]),
            C("Etkinliği belirleyen faktörler", [
                B("**Konsantrasyon, temas süresi, sıcaklık, mikroorganizma türü, organik madde varlığı, yüzeyin yapısı, pH**."),
                B("**En önemli prensip: önce temizlik, sonra dezenfeksiyon/sterilizasyon.**"),
            ]),
            C("İdeal antiseptik / dezenfektan", [
                B("Düşük konsantrasyonda etkili · **geniş spektrum** · **hızlı etki** · organik maddelerden fazla etkilenmeyen."),
                B("Dokuya/materyale zarar vermeyen · **stabil** · ucuz ve kolay uygulanır · **toksisitesi düşük**."),
            ]),
        ],
        [
            C("Temizlik, antisepsi, dezenfeksiyon, sterilizasyon", [
                B("**Temizlik**: yüzey/materyal → **kir ve organik materyali uzaklaştırma**."),
                B("**Antisepsi**: canlı doku → mikroorganizma yükünü azaltma."),
                B("**Dezenfeksiyon**: cansız materyal → patojen mikroorganizmaları yok etme/azaltma."),
                B("**Sterilizasyon**: kritik tıbbi materyal → **tüm mikroorganizmaları, sporlar dahil**, ortadan kaldırma."),
            ]),
            C("Spaulding sınıflaması", [
                B("**Kritik**: steril doku veya damar sistemi → **sterilizasyon**."),
                B("**Yarı kritik**: mukoza veya bütünlüğü bozulmuş deri → **yüksek düzey dezenfeksiyon / sterilizasyon**."),
                B("**Kritik olmayan**: sağlam deri → **düşük/orta düzey dezenfeksiyon**."),
            ]),
            C("Sınıflandırma (slayttaki sırayla)", [
                B("1. **Alkoller** · 2. **Aldehitler** · 3. **Halojenler** (iyot, klor) · 4. **Klorheksidin** · 5. **Okside edici ajanlar**"),
                B("6. **Ağır metaller** · 7. **Sabunlar** · 8. **Fenoller** · 9. **Katyonik yüzey-aktif ajanlar**"),
            ]),
        ],
        [
            C("Alkoller (etanol, izopropanol)", [
                B("Etki mekanizması: **protein denatürasyonu**, **hücre membranının bozulması**."),
                B("**Hızlı bakterisid** etki; vejetatif bakteriler, birçok mantar ve **zarflı virüsler**e etkili."),
                B("**Sporlara etkili değil**; **sterilizasyon amacıyla kullanılmaz**."),
                B("En etkili konsantrasyon genel olarak **%60-90**; **%70 alkol** yaygın kullanılan konsantrasyon."),
                B("Kullanım: **el antisepsisi, sağlam deri antisepsisi, küçük yüzeylerin dezenfeksiyonu**."),
                B("Dezavantaj: **kuruluk, irritasyon, yanıcı**; organik materyalli yüzeyde etkinlik azalabilir; sporları öldürmez."),
                B("**Alkol = hızlı etki + sporosidal değil.**"),
            ]),
            C("Aldehitler", [
                B("**Formaldehit**: proteinleri modifiye ederek mikrobisid; bakteri, mantar, virüs ve **sporlar**a etkili; **güçlü irritan ve toksik**; sağlık hizmetlerinde kullanımı **sınırlı**."),
                B("CDC: formaldehit toksisite ve irritasyon nedeniyle yaygın tercih edilen sterilizan/yüksek düzey dezenfektanlardan çıkarılmıştır.", lvl=1),
                B("**Glutaraldehit**: **yüksek düzey dezenfeksiyon**; bazı tıbbi cihazlarda; **kontakt dermatit ve solunum yolu irritasyonu** yapabilir."),
            ]),
        ],
        [
            C("Halojenler — iyot", [
                B("**Proteinleri, enzimleri, özellikle −SH gruplarını okside ederek** mikrobiyal hücre fonksiyonlarını bozar."),
                B("**Geniş spektrumlu**: bakteri, mantar ve birçok virüs; bazı koşullarda **sporlara da etkili**."),
            ]),
            C("İyodun preparatları", [
                B("**Tentürdiyot**: iyot + alkol; güçlü antiseptik; hasarlı dokuda irritasyon yapabilir."),
                B("**Povidon-iyot**: **iyodofor**; deride yavaş şekilde serbest iyot açığa çıkarır; **preoperatif cilt antisepsisi**."),
                B("Avantaj: iyoda göre **daha az irritan** olabilir.", lvl=1),
                B("Dezavantaj: **iyot alerjisi/duyarlılığı**; bazı klinik durumlarda dikkat gerekir.", lvl=1),
            ]),
            C("Halojenler — klor", [
                B("Klor → **hipokloröz asit (HOCl)** oluşumu → mikrobiyal protein ve enzimlerin **oksidasyonu**."),
                B("**Güçlü mikrobisid**; **su ve yüzey dezenfeksiyonunda yaygın**."),
                B("**Organik maddeler** etkinliği azaltır; **yüksek pH’da** etkinlik azalır."),
                B("Etkinlik = **konsantrasyon + temas süresi + pH + organik yük**."),
            ]),
        ],
        [
            C("Klorheksidin", [
                B("Mekanizma: **hücre membranını bozar**, membran geçirgenliğini değiştirir."),
                B("Kullanım: **cilt, el, cerrahi antisepsi**; **ağız ve dental hijyen** ürünleri."),
                B("Avantaj: deride **kalıcı antimikrobik etki**."),
                B("Dezavantaj: **göz ve orta kulak** gibi hassas dokularda **kullanılmamalı**; yanlış kullanımda irritasyon ve ciddi doku hasarı."),
            ]),
            C("Potasyum permanganat", [
                B("**Okside edici** ajan; **bakterisid ve fungisid**; **astrenjan** etki gösterebilir."),
                B("Bazı yüzeysel dermatolojik durumlarda tarihsel olarak kullanılmıştır; dokuları **kahverengi-mor** boyayabilir."),
            ]),
            C("Ağır metaller", [
                B("**Gümüş bileşikleri**: antimikrobik; **gümüş sülfadiazin → yanıklarda lokal antimikrobik**."),
                B("**Gümüş nitrat**: günümüzde kullanımı oldukça sınırlı."),
                B("**Cıva bileşikleri**: toksisite ve duyarlılık nedeniyle **büyük ölçüde terk edilmiştir**."),
            ]),
            C("Sabunlar", [
                B("**Anyonik yüzey aktif** maddeler; kir, yağ, sekresyon ve mikroorganizmaları **mekanik olarak uzaklaştırır**; özellikle **geçici deri florası**nı."),
                B("El hijyeninde **mekanik temizlik** mikrobiyal yükü azaltmada temel basamak."),
            ]),
        ],
        [
            C("Fenoller", [
                B("Mekanizma: **hücre membranının geçirgenliğini bozar**."),
                B("**Orta düzeyde mikrobisid**; sporlara etkisiz; geniş spektrumlu değil."),
                B("**Fenol**: korozif, toksik, **karsinojenik risk** nedeniyle günümüzde rutin kullanımda değil."),
                B("**Hekzaklorofen**: **bakteriyostatik**; tekrarlayan kullanımda kalıcı etki; **hasarlı deride absorbsiyon artar**."),
            ]),
            C("Katyonik yüzey aktif ajanlar", [
                B("**Benzalkonyum klorür, setrimid, kuarterner amonyum bileşikleri**."),
                B("Hücre membranının geçirgenliğini bozar; **düşük konsantrasyonlarda etkili**."),
                B("**Anyonik sabunlarla birlikte kullanılmamalı** — birbirlerinin antimikrobik etkinliğini azaltır."),
            ]),
            C("Grupların karşılaştırılması (mekanizma · spor · ana kullanım)", [
                B("**Alkoller**: protein denatürasyonu · spor **yok** · cilt/yüzey."),
                B("**İyot**: oksidasyon · spor **±** · cilt antisepsisi."),
                B("**Klor**: oksidasyon · spor **konsantrasyona bağlı** · su/yüzey."),
                B("**Klorheksidin**: membran hasarı · spor **yok** · cilt/el antisepsisi."),
                B("**H₂O₂**: oksidatif hasar · spor **konsantrasyona bağlı** · antisepsi/dezenfeksiyon."),
            ]),
        ],
        [
            C("Spektrum karşılaştırması (bakteri · mantar · virüs · spor)", [
                B("**Etanol / izopropanol**: +++ · ++ · ++/+++ · **−**"),
                B("**Klorheksidin**: +++ · ++ · ++ · **−**"),
                B("**Povidon-iyot**: +++ · +++ · +++ · **±**"),
                B("**Klor / hipoklorit**: +++ · +++ · +++ · **+/++**"),
                B("**H₂O₂**: +++ · +++ · +++ · **konsantrasyona bağlı**"),
                B("**Kuarterner amonyum**: ++ · ± · değişken · **−**"),
            ]),
            C("Klinikte hangisi nerede?", [
                B("**El hijyeni**: alkol bazlı el antiseptiği veya sabun + su."),
                B("**Sağlam deri**: alkol, klorheksidin, iyodofor."),
                B("**Preoperatif cilt**: klorheksidin veya iyodofor içeren uygun ürün."),
                B("**Su dezenfeksiyonu**: klor bileşikleri · **cansız yüzey**: ürüne uygun dezenfektan."),
                B("**Kritik cerrahi alet**: sterilizasyon · **mukoza ile temas eden cihaz**: yüksek düzey dezenfeksiyon/sterilizasyon."),
            ]),
        ],
        [
            C("Dezenfeksiyonda en sık yapılan hatalar", [
                B("1. **Temizlik yapmadan** dezenfektan kullanmak → organik materyal etkinliği azaltır."),
                B("2. **Konsantrasyonu yanlış hazırlamak** → fazla seyreltme etkinliği azaltır."),
                B("3. **Temas süresine uymamak** → dezenfektan uygulanıp hemen silinmemeli."),
                B("4. Her yüzey için **aynı ürünü** kullanmak → dezenfektanlar birbirinin yerine geçmez."),
                B("5. **Dezenfeksiyonu sterilizasyon sanmak** → sporlar için uygun sterilizasyon gerekir."),
            ]),
            C("Sterilizasyon", [
                B("Mikroorganizmaların **tüm formlarının, sporlar dahil**, ortadan kaldırılması."),
                B("Yöntemler: **buharlı sterilizasyon (otoklav)**, **etilen oksit**, **hidrojen peroksit gaz plazma**, **perasetik asit sistemleri**, diğer düşük sıcaklık yöntemleri."),
                B("Otoklav sıcaklık, basınç ve süresi cihaz/yük tipine göre **valide edilmiş döngü**yle belirlenir; tek bir “120 °C/30 dk” **evrensel kural değildir** (CDC: üretici önerileri)."),
            ]),
            C("Sterilizasyon ve dezenfeksiyon", [
                B("**Sterilizasyon**: tüm mikroorganizmalar; **sporlar yok edilir**; kritik materyal/cerrahi alet için gerekli; otoklav, EtO, H₂O₂."),
                B("**Dezenfeksiyon**: patojenlerin çoğunu azaltmak/yok etmek; **sporlar her zaman yok edilmez**; kritik materyal için yeterli değil; alkol, klor, H₂O₂."),
            ]),
        ],
        [
            C("Ajan özeti (mekanizma · önemli kullanım · önemli dezavantaj)", [
                B("**Etanol, izopropanol**: protein denatürasyonu · el/cilt, cilt/yüzey · **sporları öldürmez**."),
                B("**Povidon-iyot**: oksidasyon · cilt · irritasyon/uygunluk sınırlamaları."),
                B("**Klor**: oksidasyon · su/yüzey · **organik madde ile etkinlik azalır**."),
                B("**Klorheksidin**: membran hasarı · cilt/el · **göz ve hassas dokularda risk**."),
                B("**H₂O₂**: oksidasyon · dezenfeksiyon · konsantrasyona bağlı toksisite."),
                B("**Perasetik asit**: oksidasyon · yüksek düzey dezenfeksiyon/sterilizasyon · **korozif** olabilir."),
                B("**Glutaraldehit**: protein/nükleik asit modifikasyonu · yüksek düzey dezenfeksiyon · irritan/toksik."),
                B("**Kuarterner amonyum**: membran hasarı · yüzey · **sporosidal değil**."),
                B("**Fenoller**: membran hasarı · sınırlı · toksisite."),
            ]),
        ],
    ],
    sorular=[
        Q("24-25", 55, "Aşağıdakilerden hangisi yiyeceklerde koruyucu olarak kullanılır?",
          "A) Borik asit",
          "B) Formaldehit (PDF’te dezenfektan), C) Metenamin (üriner antiseptik), D) İzopropanol (alkol), E) Metaraminol · (PDF'te geçmiyor)"),
        Q("23-24", 40, "Aşağıdakilerden hangisi üriner antisepsi amacıyla kullanılıyor?",
          "C) Metenamin",
          "Borik asit, formaldehit (PDF’te dezenfektan), izopropanol (alkol), metaraminol üriner antiseptik değil · (PDF'te geçmiyor)"),
    ],
)
