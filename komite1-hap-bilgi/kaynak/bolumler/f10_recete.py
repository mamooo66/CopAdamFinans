# -*- coding: utf-8 -*-
"""Kaynak: Drive › Komite-1 › PDF › Farmakoloji › 2026-2027(yeni) › Oruç Yunusoğlu › 5-Reçete Bilgisi"""

from yardim import B, C, Q  # noqa: F401

BOLUM = dict(
    key="recete", baslik="Reçete Bilgisi",
    hoca="Doç. Dr. Oruç Yunusoğlu", tarih="1 Ekim", saat="1 saat",
    kaynak="5-Reçete Bilgisi · O. Yunusoğlu · 2026",
    ozet=["Son 5 yılda bu dersten **1 soru** çıktı (24-25 S53, “hangisi yanlıştır”): reçete yazma hakkı, **müstahzar** tanımı, jenerik isim, kısıtlı ilaçlar.",
          "Tuzak: **müstahzar (hazır) ilaç** tanımı şıkta **“offisinal ilaç”** diye verildi → YANLIŞ.",
          "25-26 S17'nin b şıkkı (**turuncu reçete = hemofili ürünleri**) bu dersten; soru Farmakoloji F19'da sayılır."],
    slaytlar=[
        # 1 — ilaç, yasa, yetki, sınıflandırma
        [
            C("Tıpta (beşeri tababet) kullanılan ilaçlar", [
                B("Genellikle **ilaç ürünleri (müstahzar, drug product)** olarak hazırlanır; **majistral** ve **offisinal** ilaçlar da vardır."),
                B("İlgili yasaya göre kurulmuş **eczanelerde**, **eczacının denetimi / gözetimi altında** kullanıma sunulur."),
                B("İlaçlar eczanelerden (bazı ilaçlar hariç) **mutlaka reçete karşılığında** sağlanır."),
                B("**1262 sayılı İspençiyari ve Tıbbî Müstahzarlar Kanunu m.1** ve **6197 sayılı Eczacılar ve Eczaneler Hakkındaki Kanun m.24** gereğince ülkemizde satışı yapılan **bütün ilaçlar reçeteye tabidir**."),
            ]),
            C("Reçete yazma yetkisi", [
                B("**Tıp doktorlarına**, **diş hekimlerine** (kısıtlı sayıda ilaç için), **veteriner hekimlere** (veteriner hekimliği ilaçları için) verilmiştir."),
            ]),
            C("Beşeri Tıbbi Ürünlerin Sınıflandırılmasına Dair Yönetmelik (m.5)", [
                B("Beşeri tıbbi ürünler Bakanlıkça ruhsatlandırılırken: **a) reçeteye tabi ürünler**, **b) reçeteye tabi olmayan ürünler** olarak sınıflandırılır."),
            ]),
        ],
        # 2 — akılcı ilaç kullanımı, kurallar
        [
            C("Akılcıl (rasyonel) ilaç kullanımı", [
                B("Reçete düzenlemesi **rasyonel (akılcıl) ilaç kullanımı** kurallarına göre yapılmalıdır."),
                B("Hastaların **klinik bulgularına uygun** ilacı, **bireysel özelliklerine uyan** ilacı, **uygun süre ve dozajda**, **en uygun maliyetle**, **kolayca** sağlayabilmeleridir."),
            ]),
            C("Akılcı tedavi süreci (5 adım)", [
                B("**1.** Hastanın problemini tanımlayın."),
                B("**2.** Tedavi amaçlarını belirleyin (terapötik hedef nedir, tedavi ile neyi başarmak istiyorsunuz?)."),
                B("**3.** Seçeceğiniz ilacın **etkililiği, güvenliliği, uygunluğu ve maliyetini** değerlendirin."),
                B("**4.** Tedaviye başlanması: reçetenin hazırlanması; hastaya gerekli **bilgi, talimat ve uyarıların** yapılması."),
                B("**5.** Tedavinin izlenmesi."),
            ]),
            C("Reçete yazma kuralları", [
                B("Reçete, **hastanın da anlayacağı biçimde** yazılmalıdır."),
                B("Hekim yeterli farmakoloji bilgisine sahip olmalı: **endikasyonlar, etkileşmeler (ilaç-ilaç, ilaç-besin), farmakokinetik özellikler, dozlar, toksikolojik özellikler**."),
                B("Hekim, farmakoloji bilgisini **klinik durumlara uygulayabilme becerisini** kazanmış olmalıdır."),
            ]),
        ],
        # 3 — mevzuat
        [
            C("Hekim ve mevzuat", [
                B("Hekim, sağlıkla ilgili **yasal düzenlemeleri (mevzuat)** bilmek durumundadır."),
                B("**Reçete yazmak her hekimin mesleki hakkıdır.**", y="24-25"),
                B("Mevzuat gereği **bazı ilaçlar sadece hastanede yatan hastalara** yazılabilir.", y="24-25"),
                B("Mevzuat gereği **bazı ilaçlar sadece ilgili uzman hekim tarafından** yazılabilir.", y="24-25"),
                B("**Geçerli uzman raporu varsa reçete tekrarını pratisyen hekim de yapabilir.**"),
                B("Sınırlı sayıda bazı ilaçlar haricinde **tüm ilaçlar yasa gereği reçeteyle satılmak zorundadır**."),
            ]),
            C("Reçete = resmi belge", [
                B("Reçete, **hekimin imzasını taşıyan** ve **hekime hukuksal sorumluluk yükleyen resmi bir belgedir**."),
                B("Reçetenin resmiliği, hastanın **sosyal güvenlik kurumlarından güvence taşımasıyla ilişkili değildir**."),
                B("**Sosyal güvencesi olmayan hastaya** yazılan reçete de resmi belgedir, ama hasta **cepten öder**."),
                B("Reçetenin resmi belge olması, hekimliğin aynı zamanda bir **kamu görevi** olmasıyla da ilgilidir."),
            ]),
        ],
        # 4 — sorumluluk, KTT
        [
            C("Eczacı ve hekimin sorumluluğu", [
                B("Hastaya yazılmış ve verilmiş olsa da **reçetenin muhatabı eczacıdır**."),
                B("Reçetenin **yapılmasından (hazırlanmasından) eczacı** sorumludur."),
                B("Reçetenin yapılmasındaki hatalar hekime ait olmakla birlikte, reçetedeki hatalardan **kısmen eczacı da sorumludur** (denetim işlevi ve görevi)."),
                B("Reçeteden birincil derecede hekim sorumlu olsa da; **reçetedeki yanlışları saptayamamak, yanlış ilaç vermek, yanlış bilgilendirme eczacının kusurudur**."),
                B("Hekim ve eczacının ihmal ve kusuru için **özel yasalar olmadığı** için **genel yargı hükümleri** dikkate alınır."),
                B("Meslek örgütlerinin **‘özdenetimi’**."),
            ]),
            C("Kanıta dayalı tıp", [
                B("Reçete yazarken ‘Kanıta dayalı tıp’ yaklaşımıyla **‘Neden bu ilacı?’** ya da **‘Neden değil?’** sorularına yanıt aranır."),
                B("Tedavi **otomatize biçimde değil**, hastayla ve hastalıkla ilgili verilerin çok dikkatli belirlenmesiyle planlanır."),
                B("**Kısaca hastalık yoktur; hasta vardır!**"),
            ]),
        ],
        # 5 — bölümleri 1-4
        [
            C("Reçetenin bölümleri — genel", [
                B("**Boş kağıttan da reçete olabilir**: tıp ve eczacılık mensuplarının aralarında kurdukları **geleneksel usullere uygun** olsun, **hekimin adı-soyadı ve imzası** bulunsun."),
            ]),
            C("1) Tarih · 2) Hekime ait bilgiler", [
                B("**1) Reçetenin yazıldığı tarih.**"),
                B("**2) Hekime ait bilgiler**: **adı, soyadı, diploma tescil numarası, uzmanlık alanı** reçetede yer almalıdır."),
                B("**Çalıştığı kurum, adres** (özellikle muayenehaneler için), **telefon numaraları** yazılmalıdır."),
                B("**Hekimin imzası (ya da kaşesi) mutlaka** bulunmalıdır."),
                B("Bu bilgiler yalnızca hastanın değil, gereğinde **eczacının da iletişim kurması** için gereklidir."),
            ]),
            C("3) Hastaya ait bilgiler · 4) Simge (süperskripsiyon)", [
                B("**3) Hasta**: **adı, soyadı, cinsiyeti, yaşı, tanısı, adresi, telefonu**. Cinsiyet ve yaş, olası sorun/karışıklıklar için uyarıcı olabilir. Bu bilgiler **etikete de aynen aktarılmalıdır**."),
                B("**4) Simge (süperskripsiyon)**: **‘R’, ‘Rx’ (R/) veya ‘Rp’**. Latince **“Kabul ediniz”** anlamına gelen **“recipe”**den gelir. Geleneksel bir simge olmaktan öte anlamı yoktur."),
            ]),
        ],
        # 6 — inskripsiyon
        [
            C("5) Önerilen ilacın adı (inskripsiyon)", [
                B("**Reçetenin esas kısmıdır.**"),
                B("Müstahzar, majistral ya da ofisinal ilaç olsa da **adı mutlaka reçetede yer almalıdır** (örn. Getamisin göz/kulak damlası, biboratlı su, penisilin solüsyonu)."),
            ]),
            C("Müstahzar (hazır) ilaç", [
                B("**Fabrikalarda, standart bir formüle göre hazırlanarak, özel ambalajlar içinde eczanelerde satışa sunulan** ilaçlardır.", y="24-25",
                  tuzak="“Offisinal ilaç; fabrikalarda, standart bir formüle göre hazırlanarak, özel ambalajlar içinde eczanelerde satışa sunulan ilaçlardır” → YANLIŞ (bu tanım müstahzarındır)"),
            ]),
            C("Jenerik ve ticari isim", [
                B("Reçeteye **‘jenerik’** ya da **‘ticari’** isim yazılabilir."),
                B("**‘Jenerik isim’ Dünya Sağlık Örgütü tarafından verilen genel addır** (örn. gentamisin).", y="24-25"),
                B("**‘Ticari isim’ (müstahzar ismi)** ise **üretici firma** tarafından verilen addır."),
            ]),
        ],
        # 7 — subskripsiyon
        [
            C("6) Önerilen ilaçla ilgili ek bilgiler (subskripsiyon)", [
                B("Bir ilacın farklı ambalajları olabilir: “16'lık kutu” / “30'luk kutu”; “50 ml'lik şişe” / “100 ml'lik şişe”."),
                B("Tedavi süresi, bir kezlik doz ya da günlük toplam doz hesaplanarak **yeterli, en uygun ve en az artık bırakacak ambalaj** belirlenip reçeteye yazılmalıdır."),
                B("Miktar şöyle belirtilebilir: “**16 tabletlik 1 kutu**” veya “30 tabletlik 2 kutu”; “50 mililitrelik 2 şişe” veya “100 mililitrelik 1 şişe”."),
                B("**“Taneyle ilaç uygulaması”** geçerliyse “12 tablet” veya “60 tablet” diye belirtilebilir."),
            ]),
            C("Verilecek miktarı belirten simgeler", [
                B("**“D”**: Fransızca ‘Donne’, İngilizce ‘Dispense’, Türkçe **‘Ver’** anlamında."),
                B("**“B”**: Fransızca ‘Boite’, İngilizce ‘Kutu’ anlamında."),
                B("Verilecek miktar **Romen rakamıyla** belirtilse bile **yazıyla da** eklenmelidir."),
            ]),
        ],
        # 8 — instrüksiyon
        [
            C("7) Önerilen ilacın kullanım tarifi (instrüksiyon)", [
                B("İlacın **nasıl kullanılacağı ayrıntılarıyla** anlatılmalıdır."),
                B("Reçetedeki simgesi **“S” veya “Sign”**; Latince **“Etiketin üzerine yaz!”** (İngilizcesi “label”) demektir."),
                B("Reçeteye yazılan bu bilgilerin hastaya verilen **kutuya (ambalaja) eczacı tarafından aktarılması** istenir."),
                B("Yazılacaklar: **doz, günde kaç kez, hangi yoldan, nasıl (aç/tok vb.), ne kadar süreyle**; bu bilgiler aynen kutuya eczacı tarafından aktarılmalıdır."),
                B("**Etiketleme**, gerçekte bu işlemdir."),
                B("İlaç bir **cihaz (aparey)** yardımıyla (inhaler vb.) uygulanacaksa çok açık tarif edilmeli, gerekirse **demonstrasyon** yapılmalıdır."),
            ]),
        ],
        # 9 — reçete çeşitleri
        [
            C("Reçete çeşitleri — normal, turuncu, mor", [
                B("**Normal reçete.**"),
                B("**Turuncu reçete**: **hemofili ürünlerinin** yazıldığı reçetedir.", y="25-26"),
                B("Hemofili reçetelerine **hematoloji veya iç hastalıkları veya çocuk sağlığı ve hastalıkları uzman hekimi** tarafından **yalnız FAKTÖR** yazılabilir.", lvl=1),
                B("**Mor reçete**: **faktörler dışındaki kan ürünlerinin** yazıldığı reçetedir."),
                B("Hemofili hastalarının faktör (turuncu) ve diğer kan ürünü (mor) reçeteleri **dört nüshalıdır**: 1. nüsha eczane → **İl Sağlık Müdürlüğü**; 2. nüsha **Kurum**; 3. nüsha **eczanede**; 4. nüsha **karnede** kalır."),
            ]),
            C("Yeşil ve kırmızı reçete", [
                B("**Yeşil reçete**: **bağımlılık yapma özelliği ve suistimal riski** olan **psikotrop madde** içeren ilaçlar. **Kendinden kopyalı (otokopili), üç nüshalı, seri numaralı**."),
                B("**Kırmızı reçete**: bağımlılık yapma özelliği ve suistimal (**opioid**) riski olan psikotrop madde içeren ilaçlar. **Kendinden kopyalı (otokopili), üç nüshalı, seri numaralı**."),
            ]),
        ],
        # 10 — e-reçete
        [
            C("E-reçete nedir?", [
                B("Hekimin **kendi bilgisayarında otomasyon sistemleri üzerinden elektronik olarak** hazırladığı reçetelerdir."),
                B("Eczane, **e-reçete sorgu bölümünden TC kimlik veya e-reçete numarasıyla** elektronik reçeteyi **MEDULA ekranında** görüntüleyebilir."),
                B("Eczanede yapılacak sonraki işlemler **manuel reçeteyle yapılan işlemlerle aynıdır**."),
            ]),
            C("E-reçetenin beklenen faydaları", [
                B("Doktor, eczacı ve hasta **işlemlerinin hızlanması**."),
                B("**El yazısından kaynaklanan hataların ortadan kalkması**."),
                B("**Elektronik karar destek sistemlerinin** hayata geçirilmesi."),
                B("Reçetelerin değerlendirilmesinin **elektronik ortamda süreklilik** kazanması."),
            ]),
        ],
        # 11 — manuel reçete istisnaları
        [
            C("Manuel reçete için istisnai durumlar (a-b-c-d)", [
                B("**a)** Kamu idareleri bünyesindeki **kurum hekimlikleri**, **işyeri hekimlikleri**, **verem savaş dispanserleri**, **ana-çocuk sağlığı ve aile planlaması merkezleri**, sağlık merkezi ve toplum sağlığı merkezleri, **112 acil sağlık hizmeti birimleri**, üniversitelerin **mediko-sosyal birimleri**, **TSK 1., 2. ve 3. basamak** sağlık hizmet sunucularında düzenlenen reçeteler."),
                B("**b)** **Majistral ilaç** içeren reçeteler."),
                B("**c)** **Kişiye özel yurt dışından getirtilen** ilaçları içeren reçeteler."),
                B("**d)** Yabancı ülkelerle yapılan **“Sosyal Güvenlik Sözleşmeleri”** kapsamında Kurum tarafından sağlık hizmeti verilen kişilere düzenlenen reçeteler."),
            ]),
            C("Manuel reçete için istisnai durumlar (e-i)", [
                B("**e)** MEDULA hastane sisteminden **provizyon alınamamasına** rağmen sağlık hizmeti sunulması durumunda düzenlenen reçeteler."),
                B("**f)** **Acil hal** kapsamında düzenlenen reçeteler."),
                B("**g)** Aile hekimlerinin **“gezici sağlık hizmeti”** kapsamında düzenledikleri reçeteler."),
                B("**h)** **Evde bakım hizmeti** kapsamında düzenlenen reçeteler."),
                B("**i)** **MEDULA ve/veya sağlık hizmet sunucusu sisteminin çalışmaması** nedeniyle e-reçetenin düzenlenememesi halinde manuel düzenlenen; üzerinde **“Sistemlerin çalışmaması nedeniyle e-reçete düzenlenememiştir”** ibaresi (kaşe veya el yazısı) bulunan ve bu ibarenin **reçeteyi düzenleyen hekim tarafından onaylandığı** reçeteler."),
            ]),
        ],
    ],
    sorular=[
        Q("25-26", 17, "Yanlış olan hangisi? (burada yalnız b şıkkı: turuncu reçete)",
          "b) DOĞRU — Turuncu reçete hemofili ürünlerinin yazıldığı reçetedir (soruda yanlış olan başka şık)",
          "PDF s.31: turuncu reçete = hemofili ürünleri (yalnız faktör); mor = faktör dışı kan ürünleri. Soru Farmakoloji F19'da sayılır.", ref=True),
        Q("24-25", 53, "Reçete bilgisi ile ilgili YANLIŞ ifade hangisi?",
          "b) “Offisinal ilaç; fabrikalarda, standart formüle göre hazırlanıp özel ambalajla eczanede satılan ilaçlardır”",
          "Bu tanım müstahzar (hazır) ilaca aittir. Mesleki hak, uzman/yatan hasta kısıtı, jenerik isim = DSÖ doğru."),
    ],
)
