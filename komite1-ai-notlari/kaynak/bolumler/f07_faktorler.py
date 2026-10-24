# -*- coding: utf-8 -*-
"""Kaynak: Drive › Komite-1 › PDF › Farmakoloji › 2026-2027(yeni) › Oruç Yunusoğlu › 3-İLAÇLARIN ETKİLERİ DEĞİŞTİREN FAKTÖRLER (53 slayt)"""

from yardim import B, C, Q  # noqa: F401

BOLUM = dict(
    key="faktorler", baslik="İlaç Etkisini Değiştiren Faktörler",
    hoca="Doç. Dr. Oruç Yunusoğlu", tarih="25 Eylül", saat="2 saat",
    kaynak="3-İlaçların Etkilerini Değiştiren Faktörler · O. Yunusoğlu · 2026",
    ozet=["Son 5 yılda bu dersten **2 soru** çıktı: **böbrek yetmezliğinde renal itrah hızı düşen ilaçlar** (24-25) ve **yaş / veriliş yolu / plasebo** doğru-yanlış sorusu (22-23).",
          "Tuzak: **oral dozlar parenteralden yüksektir çünkü oral biyoyararlanım daha DÜŞÜKTÜR** (daha yüksek değil).",
          "Böbrek yetmezliğinde itrahı düşen liste: **probenesid, aminoglikozitler, fenobarbital, fenilbutazon, digoksin, tetrasiklinler** — **minosiklin ve doksisiklin hariç**."],
    slaytlar=[
        # 1
        [
            C("Temel fikir", [
                B("Bazı faktörler ilacın **etki yerindeki konsantrasyonunu (farmakokinetiğini)**, diğerleri organ/hücrelerin **yanıt verme yeteneğini (farmakodinamiğini)** değiştirir."),
                B("Sonuçta **dozlamada (miktar ve sıklık) değişiklik** yapılması ve **dozlamın bireyselleştirilmesi** gerekir."),
                B("Hedef zinciri: **hangi faktör → hangi PK/PD parametresi → hangi klinik sonuç?**"),
            ]),
            C("İlaç etkisini değiştiren faktörler (slayttaki sıra)", [
                B("1. **Vücut ağırlığı, dağılım hacmi, klirens** · 2. **Yaş** · 3. **Absorpsiyonun azalması ve eliminasyon organlarının hastalıkları**"),
                B("4. **Cinsiyet** · 5. **Veriliş yolu** · 6. **Veriliş zamanı, gün içi ritm ve diğer ritmler** · 7. **Çevresel faktörler ve diyet**"),
                B("8. **Genetik faktörler** · 9. **Önceden var olan hastalık hali ve özel durumlar** (gebelik) · 10. **İlaç etkisini tamponlayan ikincil olaylar**"),
                B("11. **Biyolojik değişkenlik** · 12. **Kiralite** · 13. **Tolerans, taşifilaksi, desensitizasyon** · 14. **Sosyal çevre ve ruhsal durum**"),
                B("15. **Diğer ilaçların vücutta bulunması** · 16. **Plasebo ve plasebo etkisi** · ayrıca **uyunç (compliance)**"),
            ]),
        ],
        # 2
        [
            C("1. Vücut ağırlığı", [
                B("İlacın dağıldığı **sıvı kompartmanlarının ve dokuların hacmini** yansıtır."),
                B("Hem yaşla hem erişkinde değişir; **sabit dozlamada ilaç derişimlerini ve etkisini** değiştirebilir."),
                B("**Doz ≠ yalnızca kilogram**: yağsız kütle, yağ kütlesi, sıvı hacmi ve organ fonksiyonu önemlidir."),
                B("Tek doz veya kısa sürede birkaç doz verilirken ağırlığa göre doz hesabında kişinin **gerçek ağırlığı değil, YAĞSIZ ideal ağırlığı** esas alınır."),
            ]),
            C("Klirens (CL)", [
                B("İlacın **kandaki ve etki yerindeki konsantrasyonunu** ve konsantrasyonun zamana göre seyrini belirler."),
                B("**CL = eliminasyon hızı / C** (C = C kan, C plazma ya da C bağlanmamış)."),
                B("**CL ↓** → idame dozunu veya doz aralığını yeniden düşün."),
            ]),
            C("Dağılım hacmi (Vd)", [
                B("**Vd = vücuttaki ilaç miktarı / kan ya da plazmadaki ilaç konsantrasyonu**."),
                B("Vd yaşa göre değişir: **sıvı hacmi çocukta erişkine oranla daha fazladır**."),
                B("**Şişmanlıkta yağ dokusu hacmi, ödemle su hacmi artar**; bu kompartmanlarda dağılım değişir."),
                B("**Vd ↑** → **yükleme dozu** gereksinimi ↑ olabilir."),
            ]),
        ],
        # 3
        [
            C("2. Yaş", [
                B("İlacın **eliminasyon hızı yaşa göre değişkenlik gösterir**; **yenidoğan ve yaşlılarda** daha belirgindir.", y="22-23"),
            ]),
            C("Yenidoğan ve bebeklerde", [
                B("**Eliminasyon mekanizmaları olgunlaşmamıştır.**", y="22-23"),
                B("Sıvı kompartman oranı fazla, **yağ dokusu oranı düşük**."),
                B("**Plazma proteinleri azdır.**", y="22-23"),
                B("**Kan-beyin bariyeri** tam olgunlaşmamıştır."),
                B("**Mide asit salgısı nötral**, mide boşalma süresi uzamıştır."),
                B("**Kalp debisi ve kalp atım hızı** nedeniyle ilacın **dağılım hızı daha fazladır**; dağılan ilaç daha hızlı dengeye erişir."),
            ]),
            C("Pediatride 3 çağ", [
                B("**Yenidoğan**: doğumdan sonraki **ilk 4 hafta**."),
                B("**Bebek**: **5. haftadan 52. haftanın sonuna** kadar."),
                B("**Çocuk**: **1. yaştan 16. yaşın sonuna** kadar."),
            ]),
            C("Yaşlılarda", [
                B("**Mide asiditesi azalır**, villuslar atrofiye uğrar."),
                B("**KC kan akımı azalır**, enzim aktivitesi düşer."),
                B("**Böbrek kan akımı, glomerüler filtrasyon hızı ve tübüler sekresyon azalır.**"),
            ]),
        ],
        # 4
        [
            C("3. Absorpsiyonun azalması ve eliminasyon organlarının hastalıkları", [
                B("**Şok ve konjestif kalp yetmezliğinde** dokulardan geçen kan akımı azalır → **i.v. ve GİK absorpsiyonu** etkilenir."),
                B("**Böbrek hastalıkları**: renal itrah hızı azaldığından ilaçların **etkinliği artar**."),
                B("**Karaciğer hastalıklarında** ilaçların **hepatik klerensleri azalır**."),
                B("Karaciğer bozukluğu bazı **ön-ilaçların aktif şekle dönüşümünü azaltır** → bu ilaçların etkisi azalmış olabilir."),
            ]),
            C("Böbrek yetmezliğinde renal itrah hızı ↓ → etkinlik ↑", [
                B("Değişmeden böbreklerden atılan ilaçlardan: **probenesid, aminoglikozitler, fenobarbital, fenilbutazon, digoksin**.", y="24-25", tuzak="“Probenesid / fenobarbital / fenilbutazon / digoksinin renal itrah hızı böbrek yetmezliğinde düşmez” → YANLIŞ"),
                B("**Tetrasiklinler** — **minosiklin ve doksisiklin hariç**.", y="24-25"),
                B("**CL renal ↓** → AUC ↑ / t½ ↑ olabilir → **doz azaltma veya doz aralığını uzatma** düşünülebilir; karar **ilaç-spesifiktir**."),
            ]),
            C("Karaciğer hastalıklarında", [
                B("Karaciğerde **yüksek oranda eliminasyona uğrayan (yağda çözünürlüğü yüksek)** ilaçların **etki süresi uzar**: **lidokain, morfin, meperidin**."),
                B("**Ön-ilaçların** aktif şekle dönüşümü azalır, **etkileri azalır**: **kortizon, prednizon, primidon**."),
            ]),
        ],
        # 5
        [
            C("4. Cinsiyet", [
                B("**Kadında yağ oranı daha fazla**, **erkekte kas dokusu görece fazla**; bu yapısal farklar ilaç dağılımını etkiler (yağ dokusunun dağılımı ve depolanma)."),
                B("Seks hormonlarına bağlı olarak **mikrozomal enzim aktivitesi** değişir; **androjenlerin etkisiyle erkekte ilaç eliminasyonu daha hızlıdır**."),
            ]),
            C("5. Veriliş yolu", [
                B("İlaçların **oral dozları parenteral uygulamaya oranla daha yüksektir**, çünkü ilacın **biyoyararlanımı daha düşüktür**.", y="22-23", tuzak="“Oral dozlar parenteralden yüksektir çünkü biyoyararlanım daha yüksektir” → YANLIŞ"),
                B("**Oral**: absorpsiyon değişkenliği + intestinal/hepatik **ilk geçiş**."),
                B("**İ.v.**: biyoyararlanım **%100**; hızlı ve öngörülebilir sistemik maruziyet."),
                B("**İ.m./s.c.**: kan akımı, doku özellikleri, formülasyon ve enjeksiyon tekniği önemli."),
                B("**Transdermal**: deri geçirgenliği ve formülasyon belirleyici; **kontrollü salım**."),
                B("**İntranazal/bukkal/sublingual**: bazı ilaçlarda ilk geçişi **kısmen azaltabilir**."),
                B("Modern yaklaşım: **doz + yol + formülasyon + uygulama tekniği** birlikte değerlendirilir."),
            ]),
            C("6. Veriliş zamanı, gün içi ritm ve diğer ritmler", [
                B("**Gün içi ritm (sirkadyen ritim)** nedeniyle ilaçların **veriliş zamanına göre yarı ömürleri değişebilir**."),
            ]),
        ],
        # 6
        [
            C("7. Çevresel faktörler", [
                B("Çevre kirliliğine yol açan maddeler **biyotransformasyon enzimlerini** etkileyerek ilaç etkisini değiştirir."),
                B("**Poliklorlu bifeniller, DDT ve organik klorlu insektisidler, polisiklik aromatik hidrokarbonlar** → **mikrozomal enzimleri indükler**."),
                B("**Sigara dumanı ve karbonmonoksit** → **sitokrom P450 enzimlerini inhibe eder**."),
            ]),
            C("7. Diyet", [
                B("Besinlerdeki **doğal maddeler, katkı maddeleri, beslenme yetersizliği, alkol ve kahve** gibi içecekler ilaca karşı reaksiyonu değiştirebilir."),
                B("Besinlerdeki bazı **iyonlar ilaçları bağlar**: sütlü besinlerden gelen **Ca²⁺ tetrasiklinleri bağlar**."),
                B("**Greyfurt suyu** (bazı flavonoidler) **CYP3A4'ü inhibe eder** → bu enzimle yıkılan ilaçların toksisitesi artar: **terfenadin, astemizol** gibi antihistaminikler, **atorvastatin**."),
                B("**K vitamini içeren yeşil sebzeler (brokoli, ıspanak)** ve **oral antikoagülanlar (varfarin)**."),
            ]),
            C("8. Genetik faktörler", [
                B("**Genetik polimorfizm** eliminasyon hızını, ilaç reseptörlerinin, transport proteinlerinin ve diğer hedef yapıların niteliğini/niceliğini değiştirir."),
                B("Sonuç: ilaç etkisi **bireyler, etnik gruplar ve ırklar arasında** değişkenlik gösterir."),
            ]),
        ],
        # 7
        [
            C("9. Önceden var olan hastalık hali / özel durumlar", [
                B("**Myastenia gravis** · **konjestif kalp yetmezliği** · **bronşial astım** · **atopi** · **gebelik**."),
            ]),
            C("Gebelik", [
                B("**Mide-barsak kanalı motilitesi azalır**; mide suyunun bileşimi değişir → ilaç absorpsiyonu **gecikebilir ve azalabilir**."),
                B("**Karaciğerde biyotransformasyon yapan enzimlerin etkinliği artar.**"),
                B("**Böbrek kan akımı ve glomerüler filtrasyon hızı artar.**"),
                B("**Kan ve interstisyel sıvı hacmi artar**; plazma protein konsantrasyonu azalır."),
                B("Dolaşan kan ve interstisyel sıvı artışı ve **fötüs içine dağılım** nedeniyle ilaçların **gerçek ve sanal dağılım hacimleri artar**."),
                B("Sabit “doz azalt/artır” kuralı yerine **gebelik haftası, ilaç, hedef maruziyet ve anne–fetüs güvenliği** birlikte değerlendirilir."),
            ]),
            C("10. İlaç etkisini tamponlayan ikincil olaylar", [
                B("İlaç etkisi → **nöral veya hormonal homeostaz mekanizmalarının aktivasyonu** → **etkinin azalması**."),
            ]),
        ],
        # 8
        [
            C("11. Biyolojik değişkenlik", [
                B("**Bireyler arasında gözlenen etki değişkenliği**: cins, ağırlık, çevresel koşul ve benzer genetik yapı aynı olsa bile etki derecesi bireyler arasında farklı olabilir."),
            ]),
            C("12. Kiralite", [
                B("**Kiral karbon (asimetrik karbon atomu)**; **R (sağ), S (sol)** izomerler (enantiyomerler) = **konfigürasyon**."),
                B("**Dekstro (d veya +) / levo (l veya −)** = polarize ışığı çevirme yönü."),
                B("Enantiyomerlerin farklı etkileri olabilir: **dekstropropoksifen → antitüssif**; **levopropoksifen → morfin benzeri analjezik** (slayttaki gösterim)."),
            ]),
            C("14. Sosyal çevre ve ruhsal durum · 15. Diğer ilaçlar", [
                B("**Diğer ilaçların vücutta bulunması**: **farmakodinamik ve farmakokinetik etkileşmeler**."),
            ]),
            C("16. Plasebo · uyunç", [
                B("**Plasebo**: ilaçlara özgü farmasötik şekillere sokulan, fakat **gerçekte ilaç değil, inert madde** içeren preparatlar.", y="22-23"),
                B("**Uyunç (compliance)**: hastanın ilaçlar hakkında **hekim tavsiyesine uyma isteği ve derecesi**."),
                B("Etkili olanlar: **hastanın ruhsal durumu, zihinsel yetenekleri, kültür düzeyi**, ilaç alınış şekli, zamanı, sayısı vb.", lvl=1),
            ]),
        ],
        # 9
        [
            C("13. Tolerans", [
                B("Sürekli kullanılan ilaca karşı **yanıtın giderek azalması**; aynı etki için **daha yüksek doz** ihtiyacı. Örn. **opioid analjezikler**."),
                B("**Çapraz tolerans**: etki mekanizması aynı ilaçlardan birine tolerans gelişince çoğunlukla diğerlerine de gelişir. Örn. alkoliklerde **uyku ilaçlarına** karşı tolerans."),
            ]),
            C("Toleransın oluşumuna göre türleri", [
                B("**1. Biyokimyasal (farmakokinetik) tolerans**: **otoindüksiyon**. Örn. **alkol, barbitüratlar, karbamazepin**."),
                B("**2. Farmakodinamik (hücresel) tolerans**: hücre ve reseptörleri ilaca sürekli maruz kalırsa **adaptasyon** gelişir."),
                B("Agonist varlığında → **down regülasyon**; antagonist varlığında → **up regülasyon**.", lvl=1),
            ]),
            C("Taşifilaksi", [
                B("**Çabuk gelişen tolerans (akut tolerans)**; genellikle etki **birkaç dozdan sonra** azalır."),
                B("Toleranstan farkı: **doz artırılsa da etki değişmez**; tedaviden çok **deneysel koşullarda** gelişir."),
                B("Örnekler: **efedrin, amfetamin, tiramin, nikotin, vazopressin, 5-HT₃ reseptör agonistleri**."),
            ]),
        ],
        # 10
        [
            C("Desensitizasyon", [
                B("Agonist uygulanması sonucu **1 saniyeden 1 saate** kadar değişen kısa sürede hedef hücrelerin **yanıt verebilirliğinin (ilaç etkisinin) azalması**."),
                B("Genellikle **reseptör sayısında azalma (down regülasyon) görülmez**."),
                B("İki tür: **homolog** ve **heterolog** desensitizasyon."),
                B("Gelişmesi için **agonistin sürekli ortamda bulunması** gerekir."),
                B("Oluşma hızı **agonist konsantrasyonuna bağlıdır**; oluşmuş desensitizasyonun **geri dönme hızı konsantrasyondan bağımsızdır**."),
            ]),
            C("Desensitizasyon mekanizmaları", [
                B("1. **Reseptör konformasyonunun bozulması** — **nikotinik reseptörler**."),
                B("2. **Reseptör molekülünün kovalent modifikasyonu** — **β-adrenerjik reseptörler**."),
                B("3. **Sekestrasyon**: reseptörlerin bir araya gelerek birleşmesi → uyarılabilirliklerinin azalması."),
                B("4. **Reseptörün G proteini ile kenetlenmesinin bozulması** veya GTP'nin G proteini ile etkileşiminin bozulması — **opioid reseptörler**."),
                B("5. **İkinci ulak düzeyindeki adaptif değişmeler** — agonist etkinin **cAMP'ye bağımlı** olduğu reseptörler."),
            ]),
            C("Slayt sonu soruları (içerikten cevap)", [
                B("Yaşlıda doğru değişiklik: **böbrek kan akımı, GFH ve tübüler sekresyon azalır**."),
                B("KC hastalığında doğru: **karaciğerde yüksek oranda elimine edilen bazı ilaçların etki süresi uzayabilir**."),
                B("Taşifilaksi: **ilacın birkaç dozundan sonra etkinliğinin hızla azalması**."),
            ]),
        ],
    ],
    sorular=[
        Q("24-25", 44, "Hangi ilacın böbrek yetmezliğinde renal itrah hızı düşmez? (probenesid, fenobarbital, fenilbutazon, minosiklin, digoksin)", "Minosiklin",
          "İtrahı düşenler: probenesid, aminoglikozitler, fenobarbital, fenilbutazon, digoksin, tetrasiklinler (minosiklin ve doksisiklin hariç)"),
        Q("22-23", 21, "Aşağıdakilerden hangisi doğru DEĞİLDİR?", "Oral dozlar parenteralden yüksektir çünkü oral biyoyararlanım daha yüksektir",
          "Doğrusu: oral biyoyararlanım daha DÜŞÜK. Doğru: eliminasyon yaşa göre değişir; yenidoğanda eliminasyon olgunlaşmamış, plazma proteini az; plasebo = inert madde"),
    ],
)
