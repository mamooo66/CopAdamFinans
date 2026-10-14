# -*- coding: utf-8 -*-
"""Kaynak: Drive › Komite-1 › PDF › Farmakoloji › 2026-2027(yeni) › Oruç Yunusoğlu › 1-İlaç Uygulama Yolları (106 slayt)"""

from yardim import B, C, Q  # noqa: F401

BOLUM = dict(
    key="uygulama", baslik="İlaç Uygulama Yolları ve Farmasötik Biçimler",
    hoca="Doç. Dr. Oruç Yunusoğlu", tarih="23 Eylül", saat="2 saat",
    kaynak="1-İlaç Uygulama Yolları · O. Yunusoğlu · 2026",
    ozet=["Son 5 yılda bu dersten **5 soru** çıktı; hepsi temel sınıflama: **enteral / parenteral ayrımı**, **%100 biyoyararlanım = i.v.**, göze uygulanan preparat = **kolir**, oral yolun özellikleri.",
          "Tuzaklar: **intranazal** enteral değildir (21-22); **enteral** parenteral listede yoktur (24-25); **ovül** vajinaldir, göze uygulanan **kolir**dir (22-23).",
          "Oral yol: kolay, ekonomik, **en sık kullanılan**; **bilinci yerinde olmayana verilmez**; biyoyararlanım sorunludur — en hızlı etki ve %100 biyoyararlanım **i.v.** için geçerlidir (25-26)."],
    slaytlar=[
        # 1 — sınıflama, lokal yollar
        [
            C("Uygulama yerleri ve yolları — sınıflama", [
                B("İlaçların uygulama yerleri ve yolları, ilacın etkilemesi istenen yerin durumuna göre ikiye ayrılır: **A. Lokal**, **B. Sistemik**."),
                B("**Lokal uygulama**: ilacın cilt, mukozalar gibi **vücut yüzeyinde bir yere** veya **enjektör iğnesi ile doğrudan ulaşılabilen bir dokuya** uygulanması."),
                B("**Sistemik uygulama**: ilacın **kolaylıkla ulaşılamayan bir dokuda, organda veya tüm vücutta** etki göstermesi isteniyorsa."),
                B("İlaç **doğrudan kan dolaşımına** verilebilir veya uygulandığı yerden **absorbe edilerek** kan dolaşımına geçer ve etki yerine ulaşır.", lvl=1),
            ]),
            C("Lokal ilaç uygulama yolları", [
                B("Ağız içine · mide-barsak kanalına · **intratekal** · **intravajinal** · **intraplevral ve intraperitoneal**"),
                B("Rektum veya kolon içine · **deriye (epidermal / perkütan)** · **deri içine (intrakütan)** · **göze**"),
                B("**İntranazal** · **intrakardiyak** · **intrauterin** · **intraartiküler**", y="21-22"),
                B("Ayrıca slaytlarda: **kulak içine** ve **lezyon içine** uygulama."),
            ]),
            C("Sistemik etki için uygulama yerleri", [
                B("**Parenteral** · **Enteral** · **Transdermal** · **İnhalasyon** yolu ile uygulama."),
            ]),
        ],
        # 2 — deri, intrakütan
        [
            C("Deriye uygulama (epidermal veya perkütan)", [
                B("Deriden absorpsiyon **uygulama alanı genişliğine** ve ilaçların **yağda çözünürlüğüne** bağlıdır."),
                B("**Yağda çözünen ilaçlar çok kolay emilir** (organik fosfatlar, nikotin)."),
                B("Cildin absorpsiyon yeteneğini azaltan tabaka **stratum korneum**'dur; **sıyrık, yanık ve yara** sonucu bu tabaka ve epidermis kalkmışsa absorpsiyon **artar**."),
                B("**Oklüzyon** derinin hidratasyonunu artırır; nem ve ısı artar, absorpsiyon artar."),
                B("Bölgeye göre absorpsiyon: **skrotum > kulak arkası > koltuk altı > saçlı deri > göğüs > ön kol > bacak**."),
                B("Topikal uygulamada **sistemik etki** de görülebilir (**kortikosteroidler**)."),
            ]),
            C("Lokal uygulanabilen farmasötik şekiller", [
                B("**Merhem** · **krem** · **pomad** · **toz (pudra)** · **çözelti** · **süspansiyon** · **losyon**"),
            ]),
            C("Deri içine (intrakütan) injeksiyon", [
                B("**Allerji testleri** veya diğer cilt testleri için ilaç çözeltisi veya serumlar, **lokal anestezikler** bu yolla verilebilir."),
                B("Verilen çözelti hacmi **0,1 ml'den fazla olmamalıdır**."),
            ]),
        ],
        # 3 — göz
        [
            C("Göze uygulama", [
                B("Göze uygulanan ilaçlar: **kolir**, oftalmik (oküler) preparatlar.", y="22-23", tuzak="“Göze uygulanan preparat ovül / ampul / flakon / apirojen adını alır” → YANLIŞ"),
                B("Gözde amaçlar: **göz içi basıncını düşürmek**; **miyozis veya midriyazis** gibi etkiler; **göz kuruluğunda nemlendirmek**."),
                B("Diğer lokal etkiler (antibakteriyel, antienflamatuar); göz ameliyatlarında kan ve dokuları uzaklaştırmak (göz banyoları, yıkama çözeltileri)."),
                B("Göze uygulanan ilaçlar **steril** olmalıdır; ameliyatlarda kullanılan göz banyoları ve yıkama çözeltileri **koruyucu içermemeli, steril ve apirojen** olmalıdır.", y="22-23"),
                B("Şekiller: çözeltiler (sulu veya yağlı), **süspansiyonlar (göz damlası)**, merhemler, kremler ve **göz kapağının içine yerleştirilen oküler insert**."),
                B("Başlıca **lokal etki** için uygulanır; oküler yolla **sistemik etki** de elde etmek mümkündür."),
            ]),
            C("Göze uygulama — dikkat edilecekler", [
                B("**Göz damlası** konjonktiva kısmının içine damlatılır; **merhem/pomad** alt konjonktival kese içine, **içten dışa** doğru ince şerit şeklinde sıkılır."),
                B("Birden fazla damla uygulanacaksa sonrakinden önce **en az 5 dakika** beklenir; **süspansiyon** damlalar her kullanımdan önce **çalkalanır**."),
                B("Yanma, kaşıntı, kızarıklık görülebilir; damlalar **birkaç dakikadan uzun** yanma veya kaşıntı yapmamalıdır."),
                B("Çözelti **nazolakrimal kanaldan buruna** geçip istenmeyen sistemik etki yapabilir; **atropin ve timolol** gibi ilaçlarda gözün **iç köşeleri parmakla kapatılır**."),
                B("Kapağı açıldıktan sonra göze uygulanan ilaçlar **en çok 15 gün** kullanılır."),
            ]),
        ],
        # 4 — intranazal, kulak, ağız, mide-barsak
        [
            C("İntranazal uygulama", [
                B("**Dekonjestan, antihistaminik, kortikosteroidler** lokal etki amacıyla **damla veya sprey** şeklinde uygulanabilir.", y="21-22", tuzak="“İntranazal yol enteral bir yoldur” → YANLIŞ"),
                B("Burun mukozası ilaçlara **son derece geçirgendir**; uygulamadan sonra ilaç **ilk geçiş etkisine uğramaz**."),
                B("**Vazopresin, kalsitonin, oksitosin** ve türevleri **sistemik etki** için sprey şeklinde buruna uygulanabilir."),
                B("**Yağlı solüsyonlar** intranazal uygulanmamalı: alt solunum yollarına aspire edilip **lipid pnömonisi** yapar (özellikle bebeklerde)."),
            ]),
            C("İntranazal uygulamada dikkat edilecek noktalar", [
                B("Uygulamadan önce **burun temizlenmeli**; damla **sırt üstü, baş iyice geri** çekilerek uygulanır ve birkaç dakika böyle kalınır."),
                B("Mikroorganizmalar direkt temasla yayıldığından **damlalık burun mukozasına temas ettirilmemeli**."),
                B("İlacın **tüm sinüs ağızlarına** ulaşması isteniyorsa baş **dizlerin arasına gelecek şekilde hızla öne eğilir**, birkaç saniye kalınır."),
            ]),
            C("Kulak içi · ağız içi · mide-barsak", [
                B("**Kulak**: antihistaminikler, glukokortikoidler, antibiyotikler lokal etki için damla; kulak damlası **oda ısısında** olmalı (aksi halde çok ağrı yapar)."),
                B("**Ağız içi (bukkal)**: ağız/boğaz mukozası ve **diş eti (gingiva)** hastalık ve lezyonlarında **gargara, sprey, pastil** ile lokal."),
                B("**Mide-barsak kanalına**: oradan absorbe olamadan etki gösteren ilaçlar (**antiasitler, laksatifler**)."),
            ]),
        ],
        # 5 — intratekal, intrakardiyak, intraartiküler
        [
            C("İntratekal uygulama", [
                B("İlacın **subaraknoid aralığa (3.-4. lomber vertebralar arası)** enjekte edilmesi — **lomber ponksiyon**."),
                B("Spinal kökler veya meninksler üzerinde lokal etki için **lokal anestezikler veya antibiyotikler**."),
                B("Bu yolla verilenler: **lokal anestezik solüsyonlar (spinal anestezi)**, **antineoplastik ilaçlar (metotreksat)**, bazı antibakteriyel ve antifungal ilaçlar."),
                B("Teknik: orta hatta genellikle **3.-4. lomber vertebralar**; enjekte edilecek solüsyonun hacmine **eşit hacimde BOS çekilir**, sonra enjeksiyon yapılır."),
            ]),
            C("İntrakardiyak uygulama", [
                B("**Acil durumlarda kalbi uyarmak (kardiyak resusitasyon)** için **adrenalin** gibi stimülan ilaçlar ve **atropin** miyokard içine veya doğrudan kalp boşluğuna özel enjektörle uygulanır."),
                B("Kalın ve uzun özel iğne ile **sol 4. interkostal aralıkta sternumun hemen yanından**, daha seyrek **processus xiphoideus**'un yanından girilir."),
            ]),
            C("İntraartiküler uygulama", [
                B("**Eklem romatizması** gibi hallerde ilaç (örn. **glukokortikoidler**) doğrudan eklem içine enjekte edilir; **sistemik yan etkiler azalır**."),
                B("Bazı eklem iltihaplarında **kortikosteroid veya antibakteriyel** ilaçların solüsyon ve süspansiyonları eklem içine enjekte edilebilir."),
            ]),
        ],
        # 6 — intrauterin, vajinal, rektum, lezyon
        [
            C("İntrauterin uygulama — iki tip", [
                B("Uterusla ilgili ameliyatlardan sonra dokunun toplanmasını hızlandırmak ve kanamayı azaltmak için **uterus kasına (miyometriyum) oksitosin** enjeksiyonu."),
                B("Doğum kontrolü için **rahim içi araçların (RİA)** yerleştirilmesi veya bazı ilaçların uterusa direkt uygulanması."),
                B("Tıbbi abortus amacıyla **oksitosik prostaglandinler serviks içine (intramural)** injekte edilebilir."),
            ]),
            C("Vajina içine (intravajinal) uygulama", [
                B("**Vajinal tablet, fitil, ovül, vajinal krem, jel ve köpük** şeklindeki ilaçların vajina içine uygulanması.", y="22-23"),
                B("**Vajina mukozası absorpsiyona ciltten daha elverişlidir**."),
                B("Gebe kalmayı önleyen **spermisid** ilaçlar (köpük, fitil, ovül) de intravajinal uygulanabilir."),
            ]),
            C("Rektum veya kolon içine uygulama", [
                B("Hemoroid, anal fissür, polip gibi yüzeyel hastalıklarda lokal etki için **supozituvar, enema, lavman veya merhem**."),
                B("**Sistemik etki** de elde edilebilir (örn. bebeklere **parasetamol supozituvarı**)."),
                B("Absorpsiyon için **ince barsaktan daha az elverişli**; emilim yüzeyi yaklaşık **0,05 m²**; supozituvar gibi katı formlarda rektumda su az olduğundan **dissolüsyon zor**."),
                B("**Alt ve orta hemoroidal venler doğrudan vena cava inferiora** açıldığından karaciğere uğramaz → **ilk geçiş etkiden korunur**."),
            ]),
            C("Lezyon içine uygulama", [
                B("Bazı **tümöral veya iltihabi yüzeyel lezyonlarda** uygun ilaçlar lezyon içine injekte edilebilir."),
                B("**Kist hidatik**: ameliyatta kist içi parazitleri öldürmek için **hipertonik tuz solüsyonu veya formaldehid** injeksiyonu ile yıkanır."),
            ]),
        ],
        # 7 — parenteral genel
        [
            C("Parenteral uygulama — yollar", [
                B("**İntravenöz (i.v.)** · **intramüsküler (i.m.)** · **subkütan (s.c.)** · **kemik iliği içine** · **intraarteriyel (i.a.)** enjeksiyon.", y="24-25", tuzak="“Enteral yol da parenteral veriliş yoludur” → YANLIŞ"),
                B("Parenteral = ilaçların **enjeksiyon yolu** ile uygulanması."),
            ]),
            C("Parenteral — ne zaman?", [
                B("Mide-barsak kanalında **emilmeyen veya yıkılan** ilaçlar bu yolla uygulanır."),
                B("**Ağızdan ilaç alamayan** hastalarda ve **hızlı etki** istenen durumlarda uygulanabilir."),
                B("**Acil etki** isteniyorsa veya hastanın durumu ilacın oral verilmesine uygun değilse parenteral verilir."),
                B("Parenteral verilen ilaçların **biyoyararlanımı genellikle, fakat her zaman değil, tamdır (%100)**.", y="22-23"),
            ]),
            C("Parenteral preparatlar", [
                B("**Steril**, vücut pH'sına eşit veya yakın, tercihen **izotonik** ve **pirojensiz (apirojen)** olmalı; **partikül içermemeli**.", y="22-23"),
                B("**10 ml'ye kadar bolus** enjeksiyon; bunu aşan miktarlar **infüzyon** şeklinde verilir."),
                B("Farmasötik şekil: **çözelti – süspansiyon (ampul – flakon)**.", y="22-23"),
                B("**İnfüzyon pompaları**: ayakta tedavi gören hastalara **sürekli parenteral** ilaç uygulaması için geliştirilmiş sistemler; **antibiyotikler, antineoplastikler** bu yolla uygulanabilir."),
            ]),
        ],
        # 8 — i.v.
        [
            C("İntravenöz (i.v.) enjeksiyon", [
                B("İlacın **enjektör aracılığı ile doğrudan periferik bir vene** uygulanması."),
                B("**Biyoyararlanımı %100'dür.**", y="22-23 25-26", tuzak="“Oral (rektal, intravajinal, intrakardiyak) yolda biyoyararlanım %100 kabul edilir” → YANLIŞ"),
                B("Uygulama hızı ayarlanabilir, kandaki ilaç düzeyine göre değiştirilebilir; **bolus enjeksiyonda hemen cevap** alınır.", y="25-26", tuzak="“Oral yolda en hızlı etki başlangıcı sağlanır” → YANLIŞ"),
            ]),
            C("Şu durumlarda i.v. yol seçilir", [
                B("**Acil etki** istendiğinde."),
                B("İlaç **biyolojik membranları geçemeyen** bir yapıdaysa."),
                B("İlaç **ilk geçiş etkisine yüksek oranda** uğruyorsa."),
                B("**Büyük hacimli sıvılar** ve **irritan** ilaçlar için."),
            ]),
            C("İ.v. yolun dezavantajları", [
                B("Yalnızca **suda çözünen** ve suyla karışan çözücülerde çözünen ilaçlar uygulanır; **yağlı çözelti ve süspansiyonlar i.v. verilmez (emboli)**."),
                B("Suda çözünürlüğü düşük ilaçlar hızlı injekte edilirse **damar içinde çöker** (diazepam, 5 mg/dk)."),
                B("**Uygulanan ilaç geri alınamaz.** Çoğu kez hasta kendi kendine uygulayamaz, **uzman gerekir**; ağrılıdır; dozaj şekilleri genellikle daha pahalıdır."),
                B("Damar zedelenmesi; doku içi yerine damar içine enjeksiyon; **anafilaksi riski yüksek**; immünsupresyonlu hastada **enfeksiyon riski fazla**."),
                B("**Ekstravazasyon** olursa irritan ilaçlar **doku hasarı** yapar."),
            ]),
        ],
        # 9 — i.m.
        [
            C("İntramüsküler (i.m.) enjeksiyon", [
                B("İlacın **uygun bir kas dokusu içine** enjekte edilmesi."),
                B("Sulu çözeltiler yanında **yağlı çözeltiler ve süspansiyonlar** da i.m. uygulanabilir."),
                B("Uygulanan ilacın **tamamının emileceği kesin**; absorpsiyon **hızı değişkendir**."),
                B("Hacim **5 ml'yi geçmemeli**; 10 ml'lik solüsyon **ikiye bölünerek sağ ve sol kalçaya** uygulanabilir."),
                B("Uygulama yerleri: **deltoid kas (kol)**, **vastus lateralis (uyluk)**, **gluteus maksimus (kaba et)**."),
            ]),
            C("İ.m. — absorpsiyon hızını etkileyen faktörler", [
                B("**Lokal kan akımı, masaj, egzersiz**."),
                B("**Enjeksiyon bölgesi**: en hızlı absorpsiyon **deltoid kas**; en yavaş **gluteal bölge**."),
                B("İlacın fizikokimyasal özellikleri (**suda çözünürlük**)."),
                B("**Cinsiyet**: kadınlarda gluteal emilim daha zayıftır."),
            ]),
            C("İ.m. — avantajlar", [
                B("**Komplians** (hastanın tedaviye uyumu) sağlanır; etki **oral uygulamaya göre daha hızlı** başlar."),
                B("Enjeksiyon yerinde ağrı yapan ilaçlar **lokal anestezik** ile birlikte verilebilir."),
                B("**Absorpsiyon süresi uzatılabilir**: gliserin gibi viskoz taşıyıcılar, yavaş hidroliz edilen yağ asidi esterleri, suda az çözünen preparatlar (**prokain penisilin G**)."),
            ]),
        ],
        # 10 — i.m. komplikasyon, s.c., i.a., kemik iliği
        [
            C("İ.m. — komplikasyonlar", [
                B("**Ağrı** (benzil penisilin G) · **abse** · **pigmentasyon** (demir)"),
                B("Gluteal enjeksiyon sonucu **siyatik sinir hasarı**."),
            ]),
            C("Subkütan (s.c.) enjeksiyon", [
                B("**Cilt altına** yapılan enjeksiyon; genellikle **kol ve bacağın dış yüzüne**, **2 ml'yi geçmeyen** hacimlerde."),
                B("Absorpsiyon i.m.'ye göre **daha yavaş ve düzensiz**; **irritan ilaçlar bu yolla uygulanmaz**."),
                B("Uygulama yerine **masaj ve sıcak uygulama** absorpsiyonu hızlandırır."),
                B("**Pellet veya kristalize** şekil uzun süreli etki sağlar (**insülin**)."),
                B("**Vazodilatör madde** veya **hiyaluronidaz** eklenmesi absorpsiyonu artırır; **adrenalin gibi vazokonstriktör** eklenmesi yavaşlatır."),
                B("Lokal anestezik + vazokonstriktör: bölgede kalma süresi artar, etki uzar, **sistemik etki azalır**."),
            ]),
            C("İntraarteriyel (i.a.) ve kemik iliği içine enjeksiyon", [
                B("**İ.a.** (özel durumlarda): anjiyografi gibi radyolojik muayeneler için **radyoopak madde**."),
                B("Kanser kemoterapisinde **tümör bulunan organa giden artere** uygulanır → diğer dokulardaki istenmeyen etkiler en aza iner."),
                B("**Kemik iliği içine**: bebeklerde, bazen yetişkinlerde **damar bulunamazsa** uygun kemik iliği (**sternum**) içine; ilaç buradan hızla kana geçer. **Çok nadir** başvurulur."),
            ]),
        ],
        # 11 — enteral, oral
        [
            C("Enteral uygulama", [
                B("İlacın **sindirim kanalına (mide-bağırsak)** uygulanması ve buradan **absorbsiyona bırakılması**; en çok kullanılan **oral** uygulamadır."),
                B("Yollar: **oral (per oral, p.o.)** · **sublingual ve bukkal** · **rektal**.", y="21-22 24-25", tuzak="“İntranazal yol enteraldir” → YANLIŞ"),
            ]),
            C("Oral uygulama (p.o.)", [
                B("İlacın **ağızdan yutularak** alınması; **kolay, ekonomik ve düzenli** olduğundan **en sık kullanılan** yöntemdir.", y="25-26"),
                B("**Uzun süreli** ilaç kullanımına uygundur; genellikle hasta **uyunç problemi** oluşturmaz."),
                B("En önemli absorpsiyon yeri **ince barsaklar** (yaklaşık **200 m²** emilim alanı); kalın barsaktan emilim **önemsiz**."),
                B("Farmasötik şekillere göre absorpsiyon: **çözelti > emülsiyon > süspansiyon > kapsül > tablet**."),
            ]),
            C("Oral yolun sınırları", [
                B("Fizikokimyasal özellikleri nedeniyle **absorbe edilemeyen** veya GİS'te **yıkılan** ilaçlar için tercih edilmez."),
                B("**Bulantı-kusma** şikâyeti olan veya **bilinci yerinde olmayan** hastalara uygulanmaz.", y="25-26", tuzak="“Oral yol bilinci kapalı hastalarda güvenle uygulanabilir” → YANLIŞ"),
                B("Oral uygulamada en büyük sorun **biyoyararlanımdır**; absorpsiyonda hem fizyolojik hem ilaçla ilgili birçok faktör rol oynar.", y="25-26", tuzak="“Oral yolun biyoyararlanımı daima %100'dür” → YANLIŞ"),
                B("Oral şekiller: **tablet, kapsül, draje, enterik kaplı tablet, çiğneme tableti, granül, şase, şurup**."),
            ]),
        ],
        # 12 — tablet/şurup uyarıları, sublingual
        [
            C("Tablet ve kapsüllerde uyarılar", [
                B("Doktor/eczacı aksi belirtmemişse **bölmeyiniz, çiğnemeyiniz, kapsülleri açmayınız**."),
                B("**Suda veya başka sıvılarda eriterek almayınız** — etkiyi yok edebilir, ciddi yan etkiye yol açabilir."),
                B("Yutma sorunu varsa doktor/eczacıya danışılıp ilaç değiştirilebilir; ilaçlar **bol su** ile alınır."),
                B("**Süt, meyve suyu** gibi içecekler etkiyi azaltabilir veya yan etkileri artırabilir."),
            ]),
            C("Şurup", [
                B("Her kullanımdan önce **çalkalanır**; toz şurup kullanım kılavuzuna göre hazırlanır (özel su yoksa **kaynayıp soğumuş su**)."),
                B("Aksi belirtilmedikçe **buzdolabına konmaz**; doz ilacın **kendi ölçeği** ile ölçülür."),
            ]),
            C("Sublingual veya bukkal uygulama", [
                B("**Dil altı** veya **diş eti ile yanak mukozası arasına** uygulanır; kan dolaşımına geçip **sistemik etki** sağlar."),
                B("Ağız mukozası **lenf ve kan damarlarından çok zengin**; karaciğerden geçmeden **hızla** sistemik dolaşıma geçer."),
                B("İlaç **mide-barsak kanalı ve/veya karaciğerden ilk geçiş etkisinden kurtulur**."),
                B("**Presistemik eliminasyona** fazla uğrayanlar: **nifedipin, izosorbit dinitrat**, bazı ergot alkaloidleri, bazı steroid hormonlar (**metiltestosteron**), **piroksikam**."),
                B("**Ağız kuruluğu** varsa veya önceden **antikolinerjik** uygulanmışsa dikkatli olunur; hastaya **çok az su** ile ilacı uygulaması önerilir."),
            ]),
        ],
        # 13 — rektal, transdermal
        [
            C("Rektal uygulama (sistemik etki için)", [
                B("İlaç **mideyi tahriş** ediyorsa; **bulantı-kusma** vb. nedenle oral uygulanamıyorsa; oral uygulama **kontrendike** ise; hastanın **bilinci açık değil** ise."),
                B("**Küçük çocuklarda tercih edilir.**"),
                B("Gİ/hepatik **ilk geçiş etkisinden kısmen kurtulma** olabilir; absorpsiyon oral uygulamaya göre **daha düzensizdir**."),
                B("Hem **sistemik** hem **lokal** etki sağlanabilir."),
            ]),
            C("Transdermal uygulama", [
                B("İlacın **sistemik etki** göstermesi amacıyla **deri üzerine** uygulanması; **ilk geçiş etkisi önlenir**, **uzun süreli etki** sağlanır."),
                B("İlaç **yeterince lipofilik** ve **etkinliği yüksek (küçük dozlarla etkili)** olmalıdır."),
                B("Şekiller: **merhem** (nitrogliserin) veya **TTS (flaster; transdermal terapötik sistem)**."),
                B("**TTS**: ilaç cilde uygulanan bir disk içindedir; **sabit hızla** cilde geçip emilir → etkili olduğu sürece **kararlı plazma düzeyi**."),
                B("TTS ile uygulananlar: **skopolamin, nitrogliserin, klonidin, östrojen, testosteron** (slayt: nitrogliserin, testosteron, estradiol, **fentanil**)."),
                B("TTS yapısı: dış örtü, **rezervuar**, **hız kontrol eden membran**, yapışkan tabaka, koruyucu band (yırtılıp atılır)."),
            ]),
        ],
        # 14 — inhalasyon genel
        [
            C("İnhalasyon yolu ile uygulama", [
                B("Alveollerin **çok geniş yüzey alanı** ve **son derece geçirgen epitel membranı**, akciğerlerde **kan akım hızının çok yüksek** olması absorpsiyon için avantajlıdır."),
                B("Absorpsiyon **pasif difüzyonla** gerçekleşir."),
                B("Uygulananlar: **gaz ve buhar halindeki genel anestezikler** (azot protoksit, sevofluran), **yağda çözünürlüğü fazla** ilaçlar, **astım ve KOAH ilaçları**."),
                B("**Lokal ve sistemik** etki oluşturulabilir."),
            ]),
            C("İnhalasyon tedavisinin üstünlükleri", [
                B("İlacın **doğrudan hedef organa** ulaştırılması · **daha hızlı etki** · **düşük doz** · **daha az yan etki**"),
            ]),
            C("İnhalasyon sistemleri", [
                B("**Ölçülü doz inhaler (ÖDİ)** · **kuru toz inhaler (KTİ)** · **nebülizatör**"),
                B("Cihazlar: Turbuhaler, Aerolizer (inhalasyon kapsülü), Handihaler (inhalasyon kapsülü), Diskus, ÖDİ, hazne (spacer veya chamber), nebülizatör-nebül."),
            ]),
            C("Endotrakeal uygulama", [
                B("**Endotrakeal tüp takılmış** hastalarda (ameliyat sırasında) ilaç çözeltisi **trakea mukozası** üzerine uygulanır; absorpsiyon **tam ve hızlıdır**."),
                B("Bebeklerde **respiratuvar distres sendromunda (RDS) surfaktanlar** endotrakeal uygulanır."),
            ]),
        ],
        # 15 — ÖDİ, spacer
        [
            C("ÖDİ kullanımı", [
                B("Kapak açılır ve **çalkalanır**; ayakta durulur veya dik oturulur, **soluk verilir**."),
                B("ÖDİ **baş parmak ve işaret parmağı arasında, püskürtme yeri aşağıda** tutulur; dudaklar arasına alınır veya ağzın tam önünde tutulur."),
                B("**Soluk almaya başlandığında** püskürtülür ve soluk alımı sürdürülür (**yavaş ve derin** nefes); soluk **10 saniye** kadar tutulur ve verilir."),
            ]),
            C("ÖDİ kullanımında yapılan hatalar — \"el-ağız uyumu\"", [
                B("Kapağın açılmaması · ÖDİ'in **çalkalanmaması** · inspirasyondan **önce veya sonra** püskürtmek"),
                B("Birden fazla kez sıkmak · **derin soluk almamak** · **soluğunu tutmamak** · **iki doz arası beklememek**"),
            ]),
            C("Spacer (hazne) kullanımı", [
                B("**El-ağız uyumu gösteremeyen çocuk ve yaşlılarda** büyük yarar sağlar."),
                B("ÖDİ'den çıkan **büyük partiküllerin orofarenkse gitmesini engeller** (spacer içine çöker); **küçük hava yollarına** ilacın daha iyi ulaşmasını sağlar."),
                B("**İnhaler steroid** kullanımında **oral kandidiyazis daha az** görülür; acil koşullarda nebülizer olmadığında oldukça etkilidir."),
                B("Dezavantaj: **taşınması zor, kullanımı pratik değil**."),
                B("Multi breath: inhaler çalkalanıp spacer'a yerleştirilir; yavaş nefes alınırken ilaç püskürtülür, birkaç nefes daha devam edilir (her nefeste **klik sesi**); tekrar için **~30 sn** beklenir."),
            ]),
        ],
        # 16 — KTİ, kapsül, nebülizasyon
        [
            C("Kuru toz inhalerler (KTİ)", [
                B("**İnspirasyon akımı ile çalışır**, ilacın otomatik salınımını sağlar (hastanın inspirasyon akımı ilacı aerosol haline getirir)."),
                B("**El-ağız uyumu gerektirmez**; akciğerlere ulaşan ilaç miktarı **ÖDİ'den fazla**, orofarenkste biriken miktar **daha az**."),
                B("Şerit şeklinde **blister** yapı; ilaçla birlikte taşıyıcı madde **laktoz**; **kortikosteroid, bronkodilatör** ve karışımını içeren formlar (**Diskus** da bu gruptadır)."),
            ]),
            C("İnhaler kapsül", [
                B("Kapsül + taşıyıcı madde (**laktoz**) + **kortikosteroid** veya **bronkodilatör** ilaç içeren formlar."),
                B("Kullanım: kapak açılır → kapsül yuvaya yerleştirilip kapatılır → yan **düğmelere bir kez basılıp bırakılır (kapsül kırılır)**."),
                B("Ağızlık ağza konup **hızla derin nefes** alınır; **vızıldama sesi** duyulmalıdır."),
            ]),
            C("Nebülizasyon tedavisi (slayttaki maddeler)", [
                B("Mavi sütun: **minimum kooperasyon** · orofarenkste biriken ilaç miktarı **çok az** · ilaç uzun dönemde dağılır · **güçlü plasebo etki**."),
                B("Ayrıca slaytta: daha iyi tolere edilir · kombine ilaç verilebilir · **yüksek doz** ilaç verilebilir."),
                B("Siyah sütun (dezavantaj): **pahalı** · **zaman kaybı** · **taşınması zor** · **pratik değil** · **kontaminasyon**."),
            ]),
        ],
        # 17 — genel kurallar, ilk geçiş derlemesi, PDF soruları
        [
            C("Çeşitli yollardan ilaç uygulamada dikkat edilecek noktalar", [
                B("Lokal ilaç uygulamasından **önce ve sonra eller yıkanır**; rektal ve vajinal uygulamada **el temizliğine** dikkat edilir."),
                B("Göze uygulanan ilaçlar kapağı açıldıktan sonra **en çok 15 gün** kullanılır."),
                B("**Aerosoller ve süspansiyonlar** kullanmadan önce **çalkalanır**."),
                B("**Son kullanma tarihi** her zaman kontrol edilir; **i.m. ve i.v.** uygulamalar **uzman kişiler** tarafından yapılır."),
            ]),
            C("İlk geçiş etkisi — slayttaki ifadeler (derleme)", [
                B("**Intranazal**: ilk geçiş etkisine uğramaz · **sublingual/bukkal**: mide-barsak ve karaciğerden ilk geçiş etkisinden kurtulur."),
                B("**Transdermal**: ilk geçiş etkisi önlenir · **rektal**: kısmen kurtulma (alt ve orta hemoroidal venler)."),
                B("**İ.v.**: ilaç ilk geçiş etkisine yüksek oranda uğruyorsa seçilen yol."),
            ]),
            C("Slayt sonu soruları (içerikten cevap)", [
                B("%100 biyoyararlanım kabul edilen yol → **intravenöz**."),
                B("İlk geçiş etkisinden büyük ölçüde kaçınarak hızlı sistemik etki → **sublingual**."),
                B("Transdermal için uygun ilaç özelliği → **yeterince lipofilik** olması."),
            ]),
        ],
    ],
    sorular=[
        Q("25-26", 34, "Oral ilaç uygulama yolu için doğru ifade hangisidir?", "Self-medikasyon için en uygun yoldur",
          "Çeldirici: ilk geçişten korunma/%100/en hızlı etki (i.v.); bilinci kapalıda verilmez; oral: kolay, ekonomik, en sık · (PDF'te geçmiyor)"),
        Q("24-25", 56, "Aşağıdakilerden hangisi parenteral veriliş yolu değildir?", "Enteral",
          "Parenteral: i.v., i.a., kemik iliği içine, i.m., s.c.; enteral = oral, sublingual/bukkal, rektal"),
        Q("22-23", 14, "Hangi ilaç uygulama yolunda biyoyararlanım %100 kabul edilir?", "İntravenöz",
          "Çeldirici: intravajinal, rektal, intrakardiyak, oral"),
        Q("22-23", 15, "Göze uygulanan ilaç preparatına ne denir?", "Kolir",
          "Ovül = vajinal; ampul/flakon = parenteral çözelti-süspansiyon; apirojen = pirojensiz"),
        Q("21-22", None, "Enteral olmayan yol hangisidir? (intranazal, oral, rektal, intrabukkal, sublingual)", "İntranazal",
          "Enteral yollar: oral, sublingual/bukkal, rektal; intranazal lokal/mukozal yoldur"),
    ],
)
