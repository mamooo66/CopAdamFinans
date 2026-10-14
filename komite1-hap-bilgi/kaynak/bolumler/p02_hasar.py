# -*- coding: utf-8 -*-
"""Kaynak: Drive › Komite-1 › PDF › Patoloji › 2026-2027(yeni) › Selma Erdoğan Düzcü › 2-HÜCRE HASARI VE ÖLÜMÜ (83 slayt)"""

from yardim import B, C, Q  # noqa: F401

BOLUM = dict(
    key="hasar", baslik="Hücre Hasarı ve Hücre Ölümü",
    hoca="Doç. Dr. Selma Erdoğan Düzcü", tarih="21 Eylül", saat="2 saat",
    kaynak="2-HÜCRE HASARI VE ÖLÜMÜ · Doç. Dr. S. E. Düzcü · 2026",
    ozet=["Son 5 yılın **her yılında** bu dersten **1 soru** çıktı (toplam 5): hepsi **nekroz–apoptoz farkı** ve **hasar mekanizmaları** üzerine.",
          "Tekrar eden tuzak (22-23, 23-24, 25-26): **nekrozda membran bozulur + inflamasyon var**; **apoptozda membran intakt + inflamasyon yok**; apoptoz **irreversibl** ve **fizyolojik olaylarda da** görülür.",
          "Mekanizma şıkları: ATP **↓**, hücre içi Ca **↑**, glikojen **↓**, mitokondri hasarında ROT **↑**, hasar kişiler arasında **farklı**; böbrek / kalp / dalak infarktı = **koagülasyon** nekrozu (likefaksiyon değil)."],
    slaytlar=[
        [
            C("Hücre zedelenmeye nasıl cevap verir?", [
                B("**Homeostasis**: hücrenin yakın çevresini ve kendi iç ortamını oldukça dar bir fizyolojik sınır içinde **kararlı dengede** tutması."),
                B("**A- Hücre adaptasyonları**: fizyolojik stres veya patolojik uyaranlara karşı hücre canlılığını sürdürmek için **yeni duruma uyum sağlar**."),
                B("Uyum kapasitesi aşılırsa: **B- Reversibl (geri dönüşümlü) zedelenme**; **C- İrreversibl (geri dönüşümsüz)**: **nekroz**, **apoptozis**."),
            ]),
            C("Hücre zedelenmesi şeması (3. slayt)", [
                B("**Adaptasyon**: atrofi · hipertrofi · hiperplazi · metaplazi"),
                B("**Reversibl zedelenme**: **hücresel şişme**, **yağlı değişiklik**", y="23-24",
                  tuzak="“Hücresel şişme ve yağlı değişiklik irreversible hücre hasarıdır” → YANLIŞ"),
                B("**İrreversibl zedelenme**: **apoptoz**, **nekroz**", y="25-26",
                  tuzak="“Apoptozis reversible hücre hasarıdır” → YANLIŞ"),
            ]),
            C("Hücre hasarının nedenleri", [
                B("Nedenler **8 başlıkta** sıralanır:", y="23-24",
                  tuzak="“Hücre hasarına yalnızca enfeksiyonlar neden olur” → YANLIŞ"),
                B("1) **Hipoksi ve iskemi** · 2) **Fiziksel etkenler** (ısı, radyasyon, atmosferik basınç değişiklikleri) · 3) **Kimyasal etkenler** · 4) **Enfeksiyonlar**", lvl=1),
                B("5) **İmmünolojik reaksiyonlar** · 6) **Genetik faktörler** (hemoglobin S) · 7) **Beslenme dengesizlikleri** · 8) **Yaşlanma**", lvl=1),
            ]),
            C("1- İskemi veya hipoksi", [
                B("**Hipoksi** = oksijen yetersizliği: aerobik oksidatif solunumu azaltarak hücre zedelenmesine neden olan oksijen eksikliği."),
                B("**İskemi** = kanlanmanın kaybı: **arteryal akımın engellenmesi** veya **venöz drenajın azalması**."),
                B("**Hipoksinin en sık nedeni iskemi**."),
                B("Hipoksi ayrıca **pnömonide** (kanın yetersiz oksijenlenmesi), **kan kaybında** ve **CO zehirlenmesinde** (kanın oksijen taşıma kapasitesinin azalması) görülebilir."),
            ]),
        ],
        [
            C("2- Fiziksel etkenler", [
                B("**Travma** · aşırı **sıcak** · aşırı **soğuk** · atmosfer basıncında **ani değişimler** · **elektrik** · **radyasyon**"),
            ]),
            C("3- Kimyasal zedelenmeler: direkt hasar", [
                B("**Civa klorür**: hücre membranlarında proteinlerin **sülfidril gruplarına** bağlanarak iyon transportunu bozar, permeabiliteyi artırır."),
                B("Birçok **antibiyotik** ve **antineoplastik** ajan da benzer yolla hasar oluşturur."),
                B("**Siyanür**: mitokondride **sitokrom oksidazı** bloke ederek **oksidatif fosforilizasyonu** durdurur."),
                B("Kimyasalları **absorbe eden, sekrete eden ya da konsantre eden** hücreler en çok hasarı görür."),
            ]),
            C("3- Kimyasal zedelenmeler: biyolojik aktif metabolitleriyle hasar", [
                B("**CCl4 → CCl3**: karaciğer **granülsüz endoplazmik retikulumunda** bu dönüşümle **toksik metabolitler** oluşur."),
                B("**Asetaminofen (parasetamol)** karaciğerde detoksifiye edilirken **toksik ara metabolitleri** hücre hasarı yapar."),
            ]),
            C("3- Kimyasal zedelenmeler: diğer", [
                B("**Glukoz veya tuz** gibi basit kimyasallar **hipertonik** konsantrasyonlarda doğrudan ya da elektrolit homeostazını bozarak hücre zedelenmesi yapabilir."),
                B("**Arsenik, siyanür ve civa**: çok küçük miktarları yeterli sayıda hücreyi **dakikalar içinde** parçalayıp ölüme neden olabilir."),
                B("Hava kirliliği yapan maddeler, böcek ilaçları, **CO**, **asbest**, **etil alkol** ve **tedavi amacıyla kullanılan ilaçlar** (slaytta vurgulu)."),
            ]),
        ],
        [
            C("4- Mikrobiyolojik etkenler · 5- İmmünolojik reaksiyonlar", [
                B("**Mikrobiyolojik**: mikroorganizmaların lökositlerce fagositozu ve özellikle **lökositlerden salınan reaktif türevlerle** oluşan zedelenme."),
                B("**İmmünolojik**: immün sistem savunmaya yardım etse de immün reaksiyonlar hücre zedelenmesine neden olabilir: **anaflaktik reaksiyon**, **otoimmün hastalıklar**."),
            ]),
            C("6- Genetik bozukluklar · 7- Beslenme · 8- Yaşlanma", [
                B("**Genetik**: **Down sendromundaki malformasyonlar** kadar ağır ya da **orak hücreli anemide Hb S**'te bir aminoasitin yerini başka birinin alması (**eritrosit ömrü kısalır**) kadar hafif olabilir."),
                B("**Beslenme dengesizlikleri**: **protein-kalori yetersizliği**, **vitamin eksiklikleri**, **obezite – tip 2 diyabet** ilişkisi."),
                B("**Yaşlanma** iki yolla zedelenme oluşturur:"),
                B("1- Yaşlılarda **serbest radikal oluşumu fazladır**: karaciğer ve kalpte **lipofusin** pigmenti.", lvl=1),
                B("2- Toksik serbest radikalleri inaktive eden maddelerin **aktivitesi azalır**, serbest radikaller **rölatif artar**.", lvl=1),
            ]),
            C("Hücre hasarı mekanizmaları: genel prensipler", [
                B("Zedeleyici etken **ne kadar güçlü ve uzun sürerse hasar da o kadar fazla** olur."),
                B("**Düşük doz toksin** veya **kısa süreli hipoksi** → **reversibl hasar**.", lvl=1),
                B("**Yüksek doz toksin** veya **uzun süreli hipoksi** → **hücre ölümü (irreversibl hasar)**.", lvl=1),
                B("Cevap hücrenin **tipine**, **o anki durumuna** ve **tamir kapasitesine** bağlıdır: bacaktaki **çizgili iskelet kası** hipoksiye **2-3 saat**, **kalp kası 20-30 dakika** dayanır."),
                B("Hücre hasarı **kişiler arasında da farklılık gösterebilir**: CCl4 bazı insanlarda hiçbir değişiklik yapmayabilir (**enzimlerde genetik varyasyon**).", y="24-25",
                  tuzak="“Hücre hasarı kişiler arasında farklılık göstermez” → YANLIŞ"),
            ]),
        ],
        [
            C("Hücre hasarının biyokimyasal mekanizmaları (4)", [
                B("1. **Mitokondriler** ve bunların patolojik koşullarda **ATP ve ROT** (reaktif oksijen türevleri) oluşturabilme yetenekleri", y="24-25"),
                B("2. **Ca homeostazında bozukluk**"),
                B("3. **Hücre (plazma ve lizozom) membranlarının** hasar görmesi"),
                B("4. **DNA hasarı** ve **proteinlerin hatalı katlanması**"),
            ]),
            C("Mitokondri hasarı ve disfonksiyonu", [
                B("Mitokondri, hücrenin yaşamını sürdürmesini sağlayan enerjiyi **ATP** olarak üreten “**enerji santrali**”."),
                B("**ATP**: membran transportu, protein sentezi, lipogenez, fosfolipid döngüsü gibi tüm hücre içi sentez ve yıkım süreçlerinde gerekli."),
                B("Mitokondriler **hipoksi, kimyasal toksin ve radyasyona** çok duyarlıdır."),
                B("Hasarlanma yolları: **sitozolik kalsiyum artması** · **oksidatif stres (ROT)** · **oksijen yoksunluğu**."),
                B("Mitokondri hasarı **membran potansiyelini** bozar → **oksidatif fosforilizasyon** etkilenir (**ATP azalır**)."),
                B("Hasar **sitokrom c**'nin (elektron transportunun bir komponenti) **sitozola kaçmasına** yol açar → **apoptoz**."),
            ]),
            C("ATP eksikliği (sıklıkla hipoksi ve toksik nedenlere bağlı)", [
                B("ATP, mitokondrilerin **elektron transport sisteminde** oksijen indirgenmesi sırasında **ADP'nin oksidatif fosforilasyonu** ile üretilir."),
                B("**Hipoksinin ilk zarar verdiği yer** hücrenin **aerobik solunumu** (mitokondrilerde oksidatif fosforilasyon): **ATP üretimi belirgin azalır**.", y="25-26",
                  tuzak="“Hücre hasarında ATP üretiminde artış görülür” → YANLIŞ"),
                B("O2 yokluğunda **glikolitik yolak** (hücre içi **glikojenin hidrolizinden** sağlanan glikozla) da ATP üretebilir."),
                B("Bu nedenle **glikoliz kapasitesi yüksek karaciğer** hipoksiyi **beyin dokusuna göre daha iyi tolere eder**."),
            ]),
        ],
        [
            C("Hücre içinde ATP azalmasının sonuçları", [
                B("1- Hücre membranındaki **Na pompası bozulur**: hücre içinde **Na birikir** → suyun **izoosmotik** artışı → **akut hücresel şişme**; **endoplazmik retikulum genişler**."),
                B("2- **Anaerobik glikoliz artar**; glikojenden ATP üretimi başlayacağından “**hücre içi glikojen depoları azalır**”.", y="24-25",
                  tuzak="“Hücre içi glikojen depoları artar” → YANLIŞ"),
                B("3- Artan glikolizde **laktik asit ve inorganik fosfat** birikir → hücre içi **pH asidik** olur, **kromatin kümeleşmesi** ortaya çıkar."),
                B("4- **ATP bağımlı Ca pompalarının yetmezliği** → **hücre içi Ca birikimi**.", y="24-25 25-26",
                  tuzak="“…Ca pompalarının yetersizliği nedeniyle hücre içi kalsiyum azalır” / “ATP artışı, Ca azalması” → YANLIŞ"),
            ]),
            C("Kalsiyum homeostazının bozulması", [
                B("Normal sitozolik serbest Ca **< 0,1 mikromol**; ekstraselüler normal Ca **1,3 mikromol**."),
                B("**İskemi** ile hücre içi stoklardan ve hücre dışından sitoplazmaya **Ca akışı** olur."),
                B("Artan sitozolik Ca **fosfolipazları** (membran hasarı), **proteazları**, **ATPazları** ve **endonükleazları** (DNA ve kromatinin parçalanması) aktive eder."),
                B("Hücre içi Ca artışı **kaspazı doğrudan aktive eder**, mitokondri geçirgenliğini artırarak **apoptoza** neden olabilir."),
            ]),
        ],
        [
            C("Oksijen kaynaklı serbest radikallerin birikimi (oksidatif stres)", [
                B("**Serbest radikaller**: dış yörüngelerinde **tek bir elektron** bulunduran kimyasal türevler."),
                B("Kimyasal olarak **stabil değildir**; diğer moleküllerle reaksiyona girip hasar yapar (hücrede **nükleik asitler ve membran molekülleriyle** reaksiyona girip onları parçalar)."),
                B("Reaksiyona giren moleküller de serbest radikale dönüşür (**otokatalitik reaksiyon**)."),
                B("Hasar, radikallerin **üretilme ve ortamdan uzaklaştırılma hızına** bağlıdır; aşırı birikme → **oksidatif stres**."),
            ]),
            C("Serbest radikal oluşumu", [
                B("**ROT**, normalde tüm hücrelerde **mitokondri solunumu ve enerji üretimi** sırasındaki redüksiyon-oksidasyon reaksiyonlarında **az miktarda** üretilir."),
                B("ROT öncelikle fagositoz yapan **lökositlerde, nötrofillerde ve makrofajlarda**, inflamasyon ve konak savunması sırasında alınan mikropların yok edilmesi için kullanılır."),
                B("**Radyasyon**: iyonize radyasyon hücre içi suyu (H2O) **OH· ve H·** radikallerine dönüştürür."),
                B("**Nitrik oksit**: başlıca **endotel, makrofaj ve nöronlarda** oluşur; serbest radikal olarak davranabilir."),
            ]),
            C("Serbest radikal üretimini artıran faktörler", [
                B("1- Dışarıdan verilen bazı kimyasallar (**CCl4 → CCl3**) · 2- İnflamasyonda aktive **PMNL**'ler çok hızlı **süperoksit** üretir · 3- **UV ışınları ve X ışınları**."),
            ]),
            C("Serbest radikallerin aracılık ettiği hasar olayları", [
                B("Kimyasal hasar ve radyasyon hasarı · **iskemi-reperfüzyon hasarı** · **sellüler yaşlanma** · **mikropların öldürülmesi**."),
            ]),
        ],
        [
            C("Serbest radikaller 3 reaksiyonla hücre hasarı oluşturur", [
                B("1. **Membran lipidlerinin peroksidasyonu**: çift bağlı **poliansatüre** membran lipidleri serbest radikallere çok duyarlıdır; oluşan peroksitler de serbest radikal gibi davranır."),
                B("2. **DNA fragmantasyonu**: nükleer ve mitokondrial DNA'daki **timin** ile reaksiyona girip **tek iplikçik kırıkları** yapar (özellikle **hücre yaşlanması ve malign transformasyondan** sorumlu)."),
                B("3. **Protein aktivitesinin bozulması**: proteinde **disülfid çapraz bağlar** oluşturarak aktiviteyi yok eder."),
            ]),
            C("Serbest radikallerin nötralizasyonu", [
                B("**Süperoksit**, suyun varlığında hızla **O2 ve H2O2**'ye döner; enzim **SOD (süperoksit dismutaz)**."),
                B("**Katalaz** (**peroksizomlarda**): 2H2O2 → O2 + 2H2O; **bilinen en aktif enzim**."),
                B("**Glutatyon peroksidaz**: H2O2 + 2GSH → 2H2O + GSSG (glutatyon homodimer); 2GSH + 2OH· → GSSG + 2H2O."),
                B("Endojen ve eksojen **antioksidanlar**: **A, E, C vitaminleri** ve **β-karoten**."),
                B("**Transferrin, ferritin, seruloplazmin, laktoferin** gibi transport proteinler reaktif iyonları (**demir ve bakır**) minimize ederek serbest radikal oluşumunu azaltır."),
            ]),
        ],
        [
            C("Reperfüzyon hasarı", [
                B("Hücreler iskemi dolayısıyla **reversibl hasarlanmışsa**, kan akımının yeniden başlaması **serbest radikal** oluşmasına yol açar."),
                B("Klinik önemi: **serebral ve miyokardiyal infarktüse** önemli katkı yapar."),
                B("Mekanizma: kan akımının yeniden başlaması hasarlı hücreyi **yüksek kalsiyum konsantrasyonuna** maruz bırakır; **ROT üretilir**."),
                B("Reperfüzyon, **hasarlı mitokondri** ve kanla gelen **iltihap hücrelerinin** serbest radikal oluşturmasına yol açar.", y="24-25"),
            ]),
            C("Membran permeabilitesinde defektler", [
                B("Hücre hasarında en önemli membran hasarı bölgeleri: **mitokondri, plazma ve lizozom membranları**."),
                B("Nedenler: **iskemik ATP azalması ve fosfolipaz aktivasyonu**; **viral proteinler, bakteriyel toksinler, kompleman, fiziksel ve kimyasal ajanlar** ile direkt hasar."),
                B("Membran hasarına yol açan faktörler: **fosfolipid sentezinde azalma**, **fosfolipid yıkımında artış**, **hücre iskeletinde anormallikler**, **ROT**, **lipid yıkım ürünleri**."),
            ]),
            C("Membran hasarının sonuçları", [
                B("**Osmotik balans kaybolur**."),
                B("**Protein, nükleik asit, enzim ve koenzimler** hücre dışına sızar; **ATP** gibi hayati metabolitler kaybolur."),
                B("**Lizozom membran hasarı**: içindeki enzimler (**RNAaz, DNAaz, proteaz, fosfataz, glukositaz, katepsin**) sitozola sızar; hücre iskeletinde anormallikler."),
            ]),
        ],
        [
            C("Reversibl hücre hasarı", [
                B("Işık mikroskobu düzeyinde **iki şekilde** ortaya çıkar: **1- hücresel şişme**, **2- yağlı değişiklik**.", y="23-24",
                  tuzak="“Hücresel şişme ve yağlı değişiklik irreversible hücre hasarıdır” → YANLIŞ"),
            ]),
            C("Hücresel şişme", [
                B("**En sık, en hafif** zedelenmedir; hücrelerde görülen **her çeşit zedelenmenin ilk belirtisidir**."),
                B("**Plazma membranındaki enerji bağımlı iyon pompalarının yetersizliği** → iyon ve sıvı dengesi sağlanamaz → hücre şişer (osmotik basınç artışı, sıvı absorbsiyonu)."),
                B("Sitoplazmada **küçük berrak vakuoller** = **ER'un şişen / gerilen ve kopan segmentleri**; **hidropik değişiklik** veya **vakuoler dejenerasyon** da denir."),
                B("**Makroskopik**: organ büyür (hücrelerde sıvı toplanması), kapsülü gerilir, rengi solar (kapillerlerin basınç altında kalması)."),
                B("**Mikroskopik**: hücreler büyük; sitoplazma **bulanık, granüler ve vakuollü**."),
            ]),
            C("Yağlı değişiklik (hücresel yağlanma)", [
                B("Sitoplazmada **lipid vakuollerinin** belirmesi; özellikle yağ metabolizmasında rolü olan hücrelerde: **karaciğer, miyokard**."),
            ]),
            C("Reversibl zedelenmenin ultrastrüktürel değişiklikleri", [
                B("1- **Plazma membranı**: mikrovillusların kabarcıklanması, küntleşmesi veya bozulması; hücreler arası bağların gevşemesi."),
                B("2- **Mitokondri**: şişme ve fosfolipidden zengin şekilsiz yoğunlukların belirmesi."),
                B("3- **ER genişlemesi**: polizom ve ribozomların ayrılması."),
                B("4- **Nükleer**: kromatin kümelenmesi."),
                B("Sitoplazmada hasarlı hücre membranlarından kaynaklanan fosfolipid kümeleri = **miyelin figürleri**."),
            ]),
        ],
        [
            C("Nekroz", [
                B("Genellikle **öldürücü zedelenmeye** uğramış hücrelerde **enzimlerin progresif etkisi** ile oluşan morfolojik değişikliktir."),
                B("**Membran bütünlüğünün bozulması** ve hücre içeriğinin dışarı sızması ile hücrelerin parçalanması sonucu gerçekleşen hücre ölümüdür.", y="22-23 25-26",
                  tuzak="“Nekrozda hücre membran bütünlüğü intakt kalır” → YANLIŞ"),
                B("Hücre içeriğinin dışarı çıkması **inflamasyona** neden olur; ölü hücreler ortadan kaldırılır ve **onarım süreci** başlar.", y="25-26",
                  tuzak="“…inflamatuar yanıt gelişmez” → YANLIŞ"),
                B("Sıra: **membran hasarı** → hücre içeriğinin dışarı çıkması → **enzimatik sindirim** → ölü hücrelerin **miyelin figürlerine** dönüşümü → **fagositoz** → **kalsifikasyon**."),
                B("Nekrotik hücreler bir süre yerlerinde kalabilir veya enzimlerce sindirilerek tamamen kaybolabilir."),
                B("Miyelin figürleri fagosite edilir ya da yağ asitlerine parçalanır; yağ asitlerinin **kalsiyum tuzlarına bağlanması** ölü hücrenin **kalsifiye** olmasıyla sonuçlanabilir."),
            ]),
            C("Nekrozda zaman çizelgesi", [
                B("Bu olayların gelişmesi için **saatler** gereklidir."),
                B("Miyokard hücre ölümünden **20-40 dk** sonra **ultrastrüktürel** değişiklikler ortaya çıkar.", y="24-25",
                  tuzak="“İrreversibl zedelenmede ilk olarak makroskopik değişiklikler görülür” → YANLIŞ"),
                B("Hasarlı miyokarddan salınan enzimlerin (**kreatin kinaz**) kanda tespiti **2 saat** sonra mümkündür."),
                B("İrreversibl zedelenmeden **4-12 saat** sonra nekrozun **klasik histolojik özellikleri** ortaya çıkar."),
            ]),
        ],
        [
            C("Nekrozda nükleustaki morfolojik değişiklikler", [
                B("Her biri **DNA'nın spesifik olmayan yıkımı** sonucu gelişir."),
                B("1- **En erken bulgu**: kromatinin **nükleus membranı ve nükleolus etrafında kümelenmesi** (**reversibl**)."),
                B("2- **Piknoz** (**irreversibl**, **apoptozda da görülür**): nükleer büzülme ve bazofilide artma (**hiperkromazi**).", y="21-22"),
                B("3- **Karyoreksis**: **piknotik nükleusun parçalanması**; bir iki gün içinde ölü hücredeki nükleus tamamen kaybolur.", y="21-22"),
                B("4- **Karyolizis**: karyoreksis evresindeki çekirdeğin hücre lizozomlarından açığa çıkan **endonükleaz** grubu enzimlerce **eritilmesi** (DNAz aktivitesi → kromatinin oluşturduğu bazofili silinir).", y="21-22"),
            ]),
            C("Nekrozda sitoplazmik değişiklikler", [
                B("**Eozinofili artışı**: H&E'de E harfiyle temsil edilen **eozin** ile pembe boyanma özelliği artar."),
                B("Canlı hücreyle karşılaştırıldığında özellikle **glikojen partiküllerinin kaybolması** nedeniyle daha **camsı homojen** görünüm."),
                B("Organelleri enzimlerce sindirilen sitoplazma **vakuollü ve “güve yeniği”** görünümündedir."),
                B("**EM**: plazma ve organel **membran kesintileri** · mitokondrilerde **şekilsiz dansiteler** · **lizozomların parçalanması** · intrasitoplazmik **miyelin figürleri**."),
            ]),
        ],
        [
            C("Nekroz çeşitleri (6)", [
                B("1- **Koagülasyon** · 2- **Likefaksiyon** · 3- **Kazeifikasyon** · 4- **Yağ** · 5- **Gangrenöz** · 6- **Fibrinoid** nekroz"),
            ]),
            C("1- Koagülasyon nekrozu", [
                B("**En sık görülen** nekroz çeşididir."),
                B("Zedelenme yalnızca yapı proteinlerini değil **enzimleri de denatüre eder** → ölü hücrelerin proteolizle ortadan kalkması durur."),
                B("Sonuçta **çekirdeğini kaybetmiş eozinofilik hücreler günlerce veya haftalarca** varlığını sürdürebilir."),
                B("Zemindeki **doku yapısı en az birkaç gün korunur**; doku **sertleşir**."),
                B("Lökositler nekroz bölgesinde toplanır; ölü hücreler lökosit lizozom enzimleriyle sindirilir; **debris fagositozla** uzaklaştırılır."),
                B("Görüldüğü durumlar: **kan akımının ani kesilmesi** (hipoksik/anoksik zedelenme): **kalp, böbrek, dalak enfarktüsleri**.", y="23-24 25-26",
                  tuzak="“Böbrekte iskemi sonrası görülen nekroz likefaksiyon nekrozu tipindedir” → YANLIŞ"),
                B("Ayrıca **tümörlerde**, **formaldehit, civa ve asit** toksisitelerinde ve bazı **bakteri toksinlerinde** görülür."),
                B("Slayt örnekleri: **böbrekte infarkt** (koagülasyon nekrozu), **adrenalde infarkt**."),
            ]),
        ],
        [
            C("2- Likefaksiyon nekrozu", [
                B("**Proteinlerin denatürasyonundan önce** hidrolitik enzimlerin etkisiyle dokuda **erime** gerçekleşir."),
                B("Tüm hücreler sindirilir, yerini **sıvı-vizköz bir kitle** alır; sindirilmiş doku fagositlerce ortadan kaldırılır."),
                B("**Bakteriyel (bazen fungal) infeksiyonların** çok sayıda inflamatuar hücreyi harekete geçirmesiyle oluşur."),
                B("**Santral sinir sisteminde hipoksik** nedenli nekrozlar da **likefaksiyon nekrozuna** yol açar (slayt örneği: beyinde doku erimesi görülen infarkt alanı)."),
                B("Akut inflamasyon varsa oluşan sıvı **krem-sarı renkli püy** (ölen lökositler nedeniyle)."),
            ]),
            C("3- Kazeifikasyon nekrozu", [
                B("**Kazeöz = peynirimsi**: nekroz alanının **kırılgan, sarımsı beyaz** rengini tanımlar."),
                B("**Özel bir koagülasyon nekrozudur**; **tüberkülozda** görülür (slayt örneği: hiler lenf nodu, tbc)."),
                B("Hücre sınırları belirsizdir; nekrotik alan parçalanmış **granüler debris** içerir."),
                B("HE'de nekroz odağı **pembe, şekilsiz, parçalanmış hücre topluluğu** olarak görülür."),
                B("Koagülasyon nekrozunun **aksine doku yapısı silinmiştir**, hücreler ayırt edilemez."),
                B("Nekroz çoğu zaman belirgin inflamatuar reaksiyonla sınırlanır → **granülom** yapısı oluşur."),
            ]),
        ],
        [
            C("4- Gangrenöz nekroz", [
                B("Çoğunlukla bir **ekstremitenin iskemik koagülasyon nekrozunu** ifade eder."),
                B("**Farklı bir nekroz değildir**; klinikte sık kullanılan bir terimdir."),
                B("**Enfeksiyon eklenirse** **yaş gangren** olarak isimlendirilir."),
            ]),
            C("5- Yağ nekrozu", [
                B("**Özel bir tip değildir**, yağ yıkımını vurgular."),
                B("**Akut pankreatitte** lipazın pankreas dokusu içine ve peritona geçmesiyle oluşur."),
                B("Enzimler yağ dokusunu yıkar; **lipaz trigliserid esterlerini** parçalar; yağ asitleri **kalsiyumla birleşir** → **beyaz tebeşir tozu** gibi birikimler (**yağ sabunlaşması**)."),
                B("Histoloji: inflamatuar reaksiyonla çevrili, sınırları belirgin olmayan **nekrotik yağ hücreleri** + **bazofilik kalsiyum birikimi**."),
            ]),
            C("6- Fibrinoid nekroz", [
                B("Genellikle **antijen-antikor komplekslerinin arter duvarlarında** biriktiği **bağışıklık reaksiyonlarında** gelişen, ışık mikroskobuyla görülebilen özel nekroz tipidir."),
                B("Arter duvarında biriken antijen-antikor kompleksi damar dışına sızmış **fibrinle** birleşir; H&E'de **fibrinoid** denen **parlak pembe, şekilsiz** görünüm oluşur."),
            ]),
        ],
        [
            C("Apoptoz: tanım ve nekrozdan farkı", [
                B("**Programlanmış hücre ölümü** olarak bilinir; hücrenin kendi **nükleer DNA'sının** ve nükleer-sitoplazmik proteinlerinin yıkımına neden olacak **enzimleri aktive etmesiyle** gerçekleşen hücre ölümüdür.", y="23-24",
                  tuzak="“Nekroz programlanmış hücre ölümüdür ve fizyolojik olaylarda da meydana gelebilir” → YANLIŞ"),
                B("**Pek çok patolojik olayda da** görülür.", y="25-26",
                  tuzak="“Apoptozis yalnızca patolojik olaylarda meydana gelir” → YANLIŞ"),
                B("**Plazma membranı intakt kalır**, ancak yapısı değiştiğinden **fagositik hücrelerin hedefi** olur.", y="22-23 23-24",
                  tuzak="“Apoptozda hücre membran bütünlüğü bozulmuştur” → YANLIŞ"),
                B("Hücre içeriği ortama sızmadan önce çabucak ortadan kaldırıldığından **iltihabi reaksiyon gelişmez**.", y="22-23 23-24",
                  tuzak="“Apoptozda çevrede yoğun inflamasyon vardır / hücre içi enzimler dışarı çıkar” → YANLIŞ"),
                B("**Nekrozda** ise **membran bütünlüğü bozulur**, enzimatik sindirim ve **iltihabi cevap** vardır.", y="22-23 25-26",
                  tuzak="“Nekrozda membran intakt kaldığından inflamatuar yanıt gelişmez” → YANLIŞ"),
            ]),
            C("Apoptozun görüldüğü fizyolojik olaylar", [
                B("**Fizyolojik olaylar** (5 başlık):", y="22-23 25-26",
                  tuzak="“Nekroz fizyolojik ya da patolojik olabilir” → YANLIŞ"),
                B("1- **Embriyogenez** sırasında", lvl=1),
                B("2- Erişkinde **hormon kesilmesine bağlı** (menstrüel siklus; bebek sütten kesilince memelerin küçülmesi vb.)", lvl=1),
                B("3- **Sürekli prolifere olan hücre topluluklarında** delesyon: **intestinal kript epiteli** (sabit hücre sayısı için), **germinal merkezlerdeki B lenfositler**, **timusta uygun reseptör taşımayan T lenfositler**", lvl=1),
                B("4- **Akut inflamasyondaki nötrofil** ve immün cevaplardaki **lenfositlerin** işlevlerini yerine getirdikten sonra ölümleri", lvl=1),
                B("5- **Self-reaktif lenfositlerin eliminasyonu**", lvl=1),
            ]),
        ],
        [
            C("Apoptozun görüldüğü patolojik olaylar", [
                B("1- Çeşitli hasarlandırıcı uyaranlara bağlı hücre ölümleri: **radyasyon, kemoterapötik ajanlar, hafif düzey hipoksi ve ısı**"),
                B("2- **Sitotoksik T lenfositlerce** virüsle enfekte hücrelerin ve tümöral hücrelerin elimine edilmesi (**hepatit**)"),
                B("3- **Kanal obstrüksiyonuna bağlı** organın patolojik atrofisi (**pankreas, parotis, böbrek**)"),
                B("4- **Tümörlerdeki spontan** hücre ölümleri"),
                B("5- **Hatalı katlanmış proteinlerin** ortadan kaldırılması"),
            ]),
            C("Apoptoz morfolojisi", [
                B("**Hücre küçülmesi**."),
                B("**Kromatin yoğunlaşması (karakteristik)**: perifere (nükleer membrana) toplanır ve parçalanır."),
                B("**Sitoplazmik tomurcuk** ve **apoptotik cisim** oluşması; apoptotik cisimlerin **fagositozu**."),
                B("**Geç evrelere dek membran hasarı oluşmaz.**"),
                B("Mikroskopta apoptotik cisim: **yuvarlak, oval, yoğun eozinofilik sitoplazma, nükleer kromatin parçaları**."),
                B("**Apoptozda inflamasyon olmaz.**", y="22-23 23-24"),
            ]),
        ],
        [
            C("Apoptoz oluşum mekanizmaları", [
                B("**Caspase** adı verilen enzimlerin aktivasyonu ile gerçekleşir."),
            ]),
            C("1- Ekstrinsik yol (ölüm reseptörü yolağı)", [
                B("**Reseptör aracılıklı** apoptozdur (**TNF reseptörü** ve ilgili proteini **Fas (CD95)**)."),
                B("Reseptöre **ligandın bağlanması** ile aracılar kullanılarak **caspase-8** aktifleştirilir."),
                B("Bu yolak **otoreaktif lenfositlerin** ortadan kaldırılmasında etkilidir."),
            ]),
            C("2- İntrinsik yol (mitokondrial)", [
                B("**Mitokondrial permeabilitenin artması** ile apoptotik moleküller sitoplazmaya salınır."),
                B("Normalde mitokondri membranında **anti-apoptotik Bcl-2, Mcl-1 ve Bcl-x** bulunur; yaşam sinyalleri kesilirse veya hücre strese maruz kalırsa yerlerini **pro-apoptotik moleküller (Bak, Bax)** alır."),
                B("Stres: “**BH-3 only proteins**” denilen sensör proteinler (**Bim, Bid, Bad**) **Bak ve Bax**'ı aktive eder."),
                B("Sağlıklı hücrelerde anti-apoptotik **BCL-XL, MCL-1**, pro-apoptotik **BAK ve BAX**'a bağlanıp aktivasyonlarını engeller."),
                B("Permeabilite artar → **sitokrom c** gibi caspase'ları aktive eden moleküller sitoplazmaya geçer (sitoplazmada ilk **kaspaz 9** aktifleştirilir)."),
            ]),
        ],
        [
            C("Apoptozun biyokimyasal özellikleri", [
                B("**Proteinlerin parçalanması**: **caspase** nükleer matriks proteinlerini ve hücre iskeletini yıkarken **DNAaz'ları** da aktifleştirir."),
                B("**DNA'nın yıkılması**: **endonükleazlar** DNA'yı **oligonükleozomlara** ayırır."),
                B("Apoptotik hücre fagositlerce kolay tanınan **yüzey molekülleri** eksprese eder: **fosfatidil serin, trombospondin, adezif glikoproteinler**."),
            ]),
            C("p53", [
                B("**DNA zedelenmesinin tespiti** ve apoptozun başlatılmasında **anahtar rol** alır; kanser hücrelerinde sıklıkla **mutasyonlarla inaktive** edilmiştir."),
                B("p53'ün inaktivasyonu hücrenin genomik anormalliklere rağmen **intrinsik apoptozdan kaçınmasını** sağlar."),
                B("**Kemoterapi ve radyoterapi p53 sistemini aktive ederek** intrinsik apoptotik mekanizmayı uyarır."),
            ]),
            C("Defektif ve aşırı apoptoza bağlı bozukluklar", [
                B("**Defektif apoptoz**: 1- **kanser** (özellikle **p53 mutasyonu** ve **prostat ca** gibi hormona bağımlı tümörler) · 2- **otoimmün hastalıklar** (otoreaktif lenfositler elimine edilemez)."),
                B("**Aşırı apoptoz**: 1- **nörodejeneratif hastalıklar** (spinal müsküler atrofi) · 2- **iskemik hasar** (miyokard infarktüsü ve felçlerde) · 3- **virüsle infekte hücrelerin ölümü**."),
            ]),
        ],
        [
            C("Otofaji", [
                B("Hücrenin **kendi içeriklerini lizozoma taşıyarak yıkmasıdır**."),
                B("**Evrimsel olarak korunmuş** bir hayatta kalma mekanizmasıdır; **besin kıtlığında** hücreler kendi içeriklerini sindirip geri dönüştürür."),
                B("**Fizyolojik** (yaşlanma, egzersiz) ve **patolojik** (hipoksi, stres, organel hasarı) durumlarda görülür."),
                B("**Hücre bütünlüğünü korur**; **ER, mitokondri, lizozom** gibi organellerin dönüşümünü sağlar; **protein agregatlarını** temizler."),
                B("**Aşırı otofaji → hücre ölümü** (apoptoz, nekroptoz, ferroptoz)."),
            ]),
            C("Diğer hücre ölüm mekanizmaları", [
                B("**Nekroptozis (programlanmış nekroz)**: apoptoz ile nekroz arasında **hibrit** bir hücre ölümü şeklidir."),
                B("**Piroptozis (ateşli hücre ölümü)**: **lizis** ile giden, enflamatuvar mediyatörlerin (özellikle **IL-1**) salınımı ile karakterize hücre ölümüdür."),
                B("**Ferroptozis**: aşırı **demir (Fe) veya ROS** birikimi → **glutatyon-bağımlı antioksidan savunmanın çökmesi** → kontrolsüz **lipid peroksidasyonu** → hücre ölümü."),
            ]),
        ],
    ],
    sorular=[
        Q("25-26", 67, "Hücre hasarıyla ilgili doğru olan?",
          "Böbrekte kan akımının ani kesilmesi → koagülasyon nekrozu",
          "Çeldiriciler: ATP↑/Ca↓ (doğrusu ATP↓/Ca↑) · apoptoz reversibl değil · yalnız patolojik değil · nekrozda membran bozuk, inflamasyon var"),
        Q("24-25", 69, "Hücre hasarlanma mekanizmalarıyla ilgili doğru olan?",
          "Mitokondri hasarıyla reaktif oksijen türevleri artar",
          "Çeldiriciler: kişiler arası farklılık yok · ilk makroskopik değişiklik · glikojen artar · Ca azalır (doğrusu: farklılık var, ultrastrüktürel önce, glikojen↓, Ca↑)"),
        Q("23-24", 61, "Hücre hasarı mekanizmalarıyla ilgili doğru olan?",
          "Apoptozda hücre membranı intakt kalır ve iltihabi reaksiyon gelişmez",
          "Çeldiriciler: yalnızca enfeksiyon (8 neden var) · şişme/yağlı değişiklik irreversibl (reversibl) · nekroz programlı (apoptoz) · böbrekte likefaksiyon (koagülasyon)"),
        Q("22-23", 60, "Nekroz ve apoptozla ilgili doğru olan?",
          "Nekrozda hücre membran bütünlüğü bozulmuştur",
          "Çeldiriciler: nekroz fizyolojik olabilir · apoptozda membran bozuk / yoğun inflamasyon / enzimler dışarı çıkar (hepsi nekroz özelliği)"),
        Q("21-22", None, "Nekroz–apoptoz karşılaştırması (nükleer değişiklikler)",
          "Piknoz → karyoreksis → karyolizis (nekroz)",
          "Öğrenci hatırlamasından derlenmiş soru · piknoz apoptozda da görülür"),
    ],
)
