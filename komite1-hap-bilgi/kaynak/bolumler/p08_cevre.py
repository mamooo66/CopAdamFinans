# -*- coding: utf-8 -*-
"""Kaynak: Drive › Komite-1 › PDF › Patoloji › 2026-2027(yeni) › Selma Erdoğan Düzcü › 7-ÇEVRESEL HASTALIKLAR
(slayt başlığı "Çevresel Hastalıklar ve Patojenler"; 84 slayt, metin tabanlı okuma — fotoğraf/görsel sayfalar atlandı)"""

from yardim import B, C, Q  # noqa: F401

BOLUM = dict(
    key="cevre", baslik="Çevresel ve Beslenme Hastalıkları",
    hoca="Doç. Dr. Selma Erdoğan Düzcü", tarih="1 Ekim", saat="2 saat",
    kaynak="7-ÇEVRESEL HASTALIKLAR · Doç. Dr. S. E. Düzcü · 2026",
    ozet=["**Asbest** (22-23, 24-25): **akciğer ca + mezotelyoma (+ larinks ca)** → çeldiriciler benzen, vinil klorür, bisfenol A, DDT, polisiklik hidrokarbon.",
          "**Sigara** (23-24): mukus üretimini **artırır** (“azaltır” YANLIŞ); trombosit agregasyonu ↑, myokard oksijenlenmesi ↓, erken doğum ↑ doğru.",
          "**Anoreksiya nervoza** (25-26): kendini isteyerek aç bırakma + amenore + konstipasyon + PEM benzeri bulgu; çeldirici kwashiorkor, marasmus, bulimia, kaşeksi."],
    slaytlar=[
        [
            C("Çevresel hastalık ve iklim değişikliği (s.2)", [
                B("**Çevresel hastalık**: beslenme kökenli hastalıklar ile çalışma ortamında karşılaşılanları da kapsayan **kimyasal ve fiziksel zedelenmeler** sonucu oluşan bozukluklar."),
                B("**İklim değişikliği, hava kirliliği ve küresel ısınma** pek çok hastalığın sıklığını artırır:"),
                B("**Kardiyovasküler, serebrovasküler ve solunum** hastalıkları ↑ · **gastroenterit, kolera** gibi bulaşıcı hastalıklar ↑", lvl=1),
                B("Bitkisel üretim bozukluğu ile **malnutrisyon** ↑ · **sıtma** gibi vektörlerle bulaşan hastalıklar ↑", lvl=1),
            ]),
            C("Toksikoloji ve ksenobiyotikler (s.3)", [
                B("**Toksikoloji**: toksik ajanların yayılımı ve etki mekanizmalarını inceleyen **zehir bilimi**. **Zehir tanımlaması doza bağımlıdır.**"),
                B("**Ksenobiyotikler**: çevrede bulunan, **solunum, sindirim ve deri teması** ile vücuda alınan **ekzojen kimyasallar**."),
                B("Kimyasallar **idrar ve gaita** ile atılabilir, **solunan hava** ile elenebilir; atılamayanlar **kemik, yağ doku, beyin** ve diğer dokularda birikebilir."),
                B("Bazıları değişmez; bazıları **suda çözünen maddelere metabolize** olur (**detoksifikasyon**) veya **toksik metabolitlere aktive** edilir."),
            ]),
            C("Ksenobiyotik metabolizması (s.4-5)", [
                B("**Çözücülerin ve ilaçların çoğu lipofiliktir**: kandaki lipoproteinle taşınıp hücre membranındaki lipid bileşenlerine penetre olur."),
                B("**Faz 1**: **hidroliz, oksidasyon, redüksiyon** — en önemli enzim **sitokrom P450** (**polimorfizm** gösterir)."),
                B("**Faz 2**: **glukronizasyon, sülfasyon, metilasyon, glutatyon ile konjugasyon** → **suda çözünen metabolitler**."),
                B("**P-450** ksenobiyotikleri hem **detoksifiye eden** hem de hücre zedelenmesine neden olan **aktif bileşiklere dönüştüren** reaksiyonları katalizler."),
                B("**Her iki reaksiyon da reaktif oksijen türevleri** üretebilir.", lvl=1),
            ]),
        ],
        [
            C("Ozon ve kükürt dioksit — hava kirliliği (s.7)", [
                B("**Ozon**: otomobil egzozlarından salınan **azot oksitleri** ilgilendiren, **güneş ışığı etkisiyle** ortaya çıkan gaz."),
                B("Oksitler ve ince partiküllerle **smog (dumanlı sis)** oluşturur; **serbest radikallerle reaksiyona girdiğinden toksiktir**."),
                B("**Sülfür dioksit ve asit aerosoller**: **kömür ve yakıt kullanan enerji santralleri**."),
            ]),
            C("Karbon monoksit (s.7)", [
                B("**Karbon içeren materyallerin tam olmayan oksidasyonu** ile oluşur; irritan, **kokusuz, tatsız** gaz."),
                B("**Sistemik asfiksi**: **hemoglobine bağlanarak oksijen taşınmasını engeller**; hipoksi → **SSS depresyonu**."),
                B("**Akut zehirlenme**: **karboksihemoglobin** nedeniyle deri ve mukozalarda **çilek kırmızısı renk değişikliği**, **beyin ödemi**, nöronal değişiklikler."),
                B("**Kronik zehirlenme**: düşük doz sürekli maruziyet → **beyinde iskemik değişiklikler**; tanıda **yüksek karboksihemoglobin**."),
            ]),
            C("İç ortamda hava kirliliği (s.7)", [
                B("**Tütün, CO, asit aerosoller, asbestoz, odun dumanı, radon**."),
                B("**Radon**: radyoaktif, **uranyumdan üretilir**, **akciğer kanser riski**."),
            ]),
        ],
        [
            C("Kurşun (s.10)", [
                B("**En önemli kaynak: ev boyası ve benzin**; **çocuklar erişkine göre daha fazla absorbe eder**."),
                B("Kurşunun **%80-85'i kemiklerde ve yeni gelişen dişlerde** tutulur; fazlası **nörolojik defisitlere** yol açar."),
            ]),
            C("Kurşun toksisitesi — morfoloji (s.11)", [
                B("**Kan, böbrek, kemik iliği ve GİS**'i etkiler; kemikte **kalsiyum ile rekabete girerek kıkırdak remodelizasyonunu bozar**."),
                B("**Kan**: **mikrositik hipokrom anemi** (eritrositlerde **bazofilik beneklenme**); kemik iliğinde **hem sentezi inhibisyonu**, **çinko protoporfirin** oluşumu."),
                B("**Beyin**: çocukta **IQ düşüklüğü, psikoz, nöbet, koma**; erişkinde **periferik demyelinizan nöropati** (**düşük el, düşük ayak**)."),
                B("**GİS**: iyi lokalize edilemeyen **kolik**. **Böbrek**: **intranükleer kurşun inklüzyonu** ile giden **proksimal tübül hasarı**."),
            ]),
            C("Civa (s.14)", [
                B("**Kaynak**: civa ile kontamine **balıklar (kılıç, lüfer, köpek balığı)**; civa buharı yayan **amalgam diş dolgusu**."),
                B("Endüstriyel kontaminasyondan kaynaklanan **inorganik civa bakterilerce metil civaya** dönüşür → **yiyecek zincirine** girer (kılıç balığı, köpek balığı, lüferde çok yoğun)."),
                B("**Gelişmekte olan beyin metil civaya aşırı duyarlıdır**; beyinde **iyon kanallarını bloke eder**."),
                B("**Minamata hastalığı** (serebral felç, sağırlık, körlük): **fetüsün yüksek doz civaya maruziyeti** ile oluşur."),
            ]),
        ],
        [
            C("Arsenik (s.15)", [
                B("Rönesans İtalya'sında **popüler zehir**; **toprakta, suda, ahşap koruyucuda, herbisidlerde** bulunur."),
                B("**Mitokondrial oksidatif fosforilasyonu bozar**; büyük miktarda alınınca **GİS, CVS, SSS** bozuklukları."),
                B("**Kronik maruziyet**: **hiperkeratoz, hiperpigmentasyon, BCC ve SCC** (**el içi ve ayak tabanında multipl lezyon**)."),
            ]),
            C("Kadmiyum (s.16)", [
                B("Esas olarak **nikel-kadmiyum pillerde** kullanılır; toplumsal maruz kalmada en önemli kaynak **yiyecekler**."),
                B("**Obstrüktif akciğer hastalığı, böbrek toksisitesi**."),
                B("Japonya'da pirinç tarlası sulamada kullanılan **kadmiyum bulaşmış su** → kadınlarda **itai-itai (ah-ah) hastalığı** (renal hastalıkla ilişkili **osteoporoz, osteomalazi**)."),
            ]),
            C("Endüstriyel ve tarımsal ajanlara maruziyet (s.18)", [
                B("1- **Organik çözücüler** (kloroform, karbontetraklorür): baş dönmesi, **MSS depresyonu** · **Benzen** (lastik sanayi): **lösemi riski ↑**"),
                B("2- **Polisiklik hidrokarbonlar**: kömür ve gazın çelik dökümhanelerinde yüksek ısıda yanmasıyla oluşur → **akciğer, mesane ca riski ↑**"),
                B("3- **Organoklorokinler** (böcek ilacı) **DDT**: nörolojik toksisite, **antiöstrojenik, antiandrojenik**"),
                B("4- **Dioksinler**: folikülit, akneiform dermatoz, karaciğer ve SSS anormallikleri · **Klorakne**: akne, kist, hiperpigmentasyon, hiperkeratoz"),
                B("5- **Bisfenol A (BPA)**: gıda şişeleri, **endokrin sistem bozucu** · 6- **Vinil klorür**: **karaciğer anjiosarkomu**"),
                B("7- **Mineral tozları → pnömokonyozlar**: kömür tozu, **silika** (kum ocakları), **asbestozis** (madencilik), **berilyum** (madencilik)"),
                B("**Asbest** → **akciğer ca, mezotelyoma, larinks kanseri, mide ve kolon kanseri**; akciğerlerde **diffüz fibrozis** yapar.",
                  y="24-25 22-23",
                  tuzak="“Mezotelyoma / larinks ca etyolojisinde bisfenol A, vinil klorür, polisiklik hidrokarbon, DDT, benzen” → YANLIŞ"),
            ]),
        ],
        [
            C("Tütünün etkileri (s.20)", [
                B("**Tütün, insan kanserinin en yaygın ekzojen nedenidir.**"),
                B("**Akciğer kanserlerinin %90'ından sorumludur.**", y="23-24"),
                B("Yılda **4 milyondan fazla** insanın ölümüne neden olur; **en önlenebilir insan ölümü nedeni**; yaşam süresini **doza bağımlı** kısaltır."),
                B("Tütün dumanı **2000'den fazla bileşik** içerir: **nikotin, polisiklik hidrokarbonlar, nitrozaminler, aromatik aminler** bunlardan bazılarıdır."),
                B("Sigara ile ilişkili en sık hastalıklar: **amfizem, kronik bronşit, akciğer kanseri**."),
            ]),
            C("Nikotin (s.21)", [
                B("Tütün yaprağında bulunan bir **alkaloid**; tütünle ilgili hastalıklara **doğrudan neden olmaz**, ancak **yüksek düzeyde bağımlılık** oluşturur."),
                B("Beyindeki reseptörlere bağlanır; **katekolamin deşarjı** ile **kalp hızı ve kan basıncını yükseltir**, kalp kasılma gücü ve atım miktarı artar."),
            ]),
            C("Sigara ile ilişkili hastalıkların mekanizması (s.22)", [
                B("**Mukozada direk etki** ile **inflamasyon ve artmış mukus üretimi**, lökositlerin akciğerde birikimi, **amfizem**.",
                  y="23-24", tuzak="“Mukozada direk etki ile mukus üretimini azaltır” → YANLIŞ"),
                B("**Trombosit agregasyon artışı, myokard oksijenlenme azalması**, ventriküler fibrilasyon eşik düşmesi, ateroskleroz, MI.", y="23-24"),
                B("**Oral kavite, özefagus, pankreas ve mesane** kanserlerinin gelişimine katkı sağlar."),
                B("Annenin sigara içmesi **erken doğum ve spontan düşüğü** artırır.", y="23-24"),
                B("**Pasif içicilerde akciğer kanser riski 1,3 kat** artar; sigara içilen ortamdaki çocuklarda **respiratuar hastalıklar ve astım** artar."),
                B("**Pasif içicilik**, nikotin metaboliti **kotinin**'in kandaki ölçümü ile yapılır."),
            ]),
        ],
        [
            C("Alkol — emilim ve metabolizma (s.26)", [
                B("Alkolün aşırı alımı **fiziksel ve psikolojik bozukluklara** yol açar."),
                B("**Etanol** değişikliğe uğramadan **mide ve ince barsaktan emilir**, tüm vücut sıvılarına ve dokularına dağılır; **%10'dan azı** değişmeden **idrar, ter ve solunum havası** ile atılır."),
                B("Ana enzim: **hepatosit sitozolündeki alkol dehidrogenaz**."),
                B("**Alkol dehidrogenaz + sitokrom P450 izoenzimi (özellikle CYP2E1) + katalaz** = **üçlü enzim sistemi** → **asetaldehite** metabolize olur."),
                B("Kanda yüksek oranda bulunduğunda **diğer ilaçların katabolizmasını geciktirip ilaç etkinliğini artırabilir**."),
            ]),
            C("Etanol metabolizmasının toksik etkileri (s.28)", [
                B("Alkol dehidrogenaz ile oksidasyon **NAD+ azalmasına**, **NADH artışına** yol açar."),
                B("**NAD+** karaciğerde **yağ asitlerinin oksidasyonunda** görev aldığından eksikliği alkoliklerde **karaciğerde yağ birikimine** neden olur."),
                B("**Asetaldehit** birçok toksik etkiye sahiptir."),
                B("İntestinal floradaki **gram negatif bakteri ürünü endotoksin** salınımı → **TNF ve sitokin salınımı**."),
            ]),
            C("Akut alkolizm (s.30)", [
                B("**MSS**: ilk olarak **serebral kortikal yapıları** etkileyen **depresan**; bozulmuş kortikal ve entelektüel davranış."),
                B("Hepatosit sitoplazmasında **yağ damlacığı birikimi → hepatik steatoz**; **akut gastrik zedelenme ve ülserasyon**."),
            ]),
            C("Kronik alkolizm (s.31-32)", [
                B("**Tüm organları** etkiler: karaciğer, GİS, MSS, CVS ve pankreasta **ciddi morbidite ve kısalmış yaşam süresi**."),
                B("**Karaciğer**: **alkolik hepatit, siroz, portal hipertansiyon**, artmış **hepatosellüler kanser** riski."),
                B("**GİS**: **gastrit, gastrik ülser, özefagus varisi**."),
                B("**Tiamin eksikliği**: **periferik nöropati** ve **Wernicke-Korsakoff sendromu** (nörolojik bozukluk)."),
                B("**CVS**: **dilate hipertansiyon, konjestif kardiyomiyopati, koroner kalp hastalığı**."),
                B("**Gebelikte düşük dozda bile fetal alkol sendromu**: mikrosefali, gelişme geriliği, yüz anormalliği, mental fonksiyon azalması."),
                B("**Akut ve kronik pankreatit** riski artar; **oral kavite, özefagus, karaciğer ve meme kanseri** riskinde artış."),
            ]),
        ],
        [
            C("Terapötik ilaçlarla hasar — istenmeyen reaksiyon ve HRT (s.33-34)", [
                B("**İstenmeyen ilaç reaksiyonları**: ilaçların tedavi sırasındaki **beklenmedik etkileri**."),
                B("**Menopozal hormon tedavisi (eski adı HRT)**: **östrojenlerin progestajen ile birlikte** verilmesi; **yalnız östrojen** içeren ilaçlar **histerektomize hastalarda** kullanılır."),
                B("**Tek başına östrojen** → **endometrium kanser riski ↑**; **östrojen + progesteron** uzun süreli HRT → **meme kanseri riski ↑**."),
                B("**HRT ve OKS** → **tromboembolizm riski ↑**."),
            ]),
            C("Oral kontraseptifler (s.35)", [
                B("Çoğunlukla **sentetik östradiol ve progesteron**."),
                B("**Endometriyal ve over kanserine karşı koruyucu** etkisi vardır."),
                B("Karaciğerde **hepatik adenom** ile ilişkili; **tromboembolizm** ve **koroner arter hastalığı** riskini artırır."),
            ]),
            C("Asetaminofen (s.36)", [
                B("**Analjezik ve antipiretik**; terapötik dozlarda karaciğerde **glukronid veya sülfat ile konjuge** edilir."),
                B("**%5 kadarı** hepatik **P450** sistemiyle **NAPQI**'ye (N-asetil-p-benzoquinoneimine) metabolize edilir."),
                B("**Yüksek dozda NAPQI birikir → sentrilobüler hepatik nekroz**; toksisite: **bulantı, kusma, diyare**, bazen **şok**."),
            ]),
            C("Aspirin (asetil salisilik asit) (s.37)", [
                B("Aşırı dozda: **respiratuar alkaloz**, sonrasında **metabolik asidoz**."),
                B("**Kronik aspirin zehirlenmesi**: günlük **3 g veya daha fazla** alanlarda — baş ağrısı, baş dönmesi, **kulak çınlaması**, bulantı, kusma, **gastrik ülser**, diyare."),
                B("**Analjezik nefropatisi**: aspirin ve asetaminofen gibi ilaçların **uzun yıllar** kullanımına bağlı **renal papiller nekrozlu tübülointerstisyel nefrit**."),
            ]),
        ],
        [
            C("Nonterapötik toksik ajanlar — 1- Kokain (s.38-39)", [
                B("**Koka bitkisi yapraklarından** elde edilen **alkaloid**; **crack**: saf alkaloidin **kokain hidroklorürden kristalizasyonu** ile elde edilir, **kokainden daha güçlü**."),
                B("**Koklanarak, tütün ile sarılıp içilerek, subkutan, intravenöz** kullanılır."),
                B("**Belirgin öfori ve mental uyanıklık** → **en fazla bağımlılık yapanlardan biri**; **fiziksel bağımlılık yok**, **psikolojik bağımlılık** bulguları son derece ağır."),
                B("**Kardiyovasküler** (sempatomimetik): taşikardi, hipertansiyon, periferik vazokonstrüksiyon; **miyokardiyal iskemi, koroner arter spazmı, ölümcül aritmi, trombüs**."),
                B("**MSS**: **hiperpireksi ve nöbet**. **Gebelikte**: spontan düşük, **fetal hipoksi, nörolojik gelişim bozukluğu**."),
                B("**Kronik kullanım**: **nazal septum perforasyonu**, akciğer difüzyon kapasitesinde azalma, **dilate kardiyomiyopati**."),
            ]),
            C("2- Eroin (s.41)", [
                B("**Haşhaş bitkisinden** elde edilen bağımlılık yapıcı **opioid**, **morfinle yakından ilişkili**; **intravenöz, subkutan**; **kokainden daha tehlikeli**."),
                B("**Öfori, halüsinasyon, sedasyon** yapabilir."),
                B("Etkiler: **ani ölüm, pulmoner hastalık, enfeksiyonlar (staf aureus), deri lezyonları (abse, selülit, ülser)**, "
                  "renal hastalıklar (**amiloidoz, fokal segmental glomerüloskleroz**)."),
            ]),
            C("3- Marihuana (s.42)", [
                B("**En yaygın kullanılan yasa dışı ilaç**; **Cannabis sativa** bitkisinden; psikoaktif madde **tetrahidrokannabinol**."),
                B("İstenmeyen etki: **allerjik reaksiyonlar**; **duyusal algı ve motor koordinasyon bozulur** (4-5 saatte geçer)."),
                B("**Kalp atım sayısını (bazen kan basıncını) artırır**, **anjina** yapabilir; sigaraya göre derin soluk nedeniyle **3 kat daha fazla katran** alımı."),
            ]),
        ],
        [
            C("Fiziksel ajanlarla hasar — 1- Mekanik travma (s.44)", [
                B("**Abrazyon**: deri yüzeyinin **kazıma ya da ovalama** ile yüzey epiteli hücrelerinin zedelenmesi; **yalnız epidermis soyulur**."),
                B("**Kontüzyon (berelenme)**: **künt travma** ile damarların zedelenip **kanın doku dışına çıkması**."),
                B("**Laserasyon**: **keskin olmayan cisim** ile kuvvet uygulanarak dokunun **aşırı gerilmesi** sonucu **düzensiz yırtılma**."),
                B("**Kesici yaralanma**: **keskin aletle** kan damarlarının yaralanması."),
                B("**Delici yaralanma**: **uzun ve dar aletle**; dokunun derinlerine ulaşırsa **penetran**, dokuyu tamamen geçerse **perforan**."),
            ]),
            C("2- Termal hasar — termal yanık (s.46)", [
                B("Derecesi: **derinlik, tutulan vücut alanı yüzdesi**, sıcak buhar solunmasıyla **iç zedelenme**, sıvı-elektrolit dengesinin korunması, yara enfeksiyonunun önlenebilmesine göre değişir."),
                B("**Tam kat yanık**: **epidermisin total kaybı**; sinir uçları harap olduğundan **ağrısız**."),
                B("**Kısmi yanık**: **büllü ve ağrılı**; histoloji: canlı doku komşuluğunda hızla **inflamatuar hücre toplanması**, belirgin eksüdasyon, **koagülasyon nekrozu**."),
            ]),
            C("Yanığın sonuçları (s.47)", [
                B("**Vücut yüzeyinin %50'sinden fazlasını** aşan yanıklar (yüzeyel ya da derin) **ağır ve ölümcül**."),
                B("**%20'sinden fazlası** yandığında yanık bölgesinde ve vücut sıvısında azalma → **hipovolemik şok**, **pulmoner ödem**."),
                B("**İnhalasyon hasarı**: ısınmış havanın doğrudan solunması. **Ölümün başta gelen nedeni**: **sepsis kaynaklı organ yetmezlikleri**."),
                B("En yaygın ciddi sekeller: **renal yetmezlik, ARDS, pnömoni, septik şok**."),
            ]),
        ],
        [
            C("Hipertermi (s.48)", [
                B("Uzun süren çevre sıcaklığına maruziyet → **sıcak krampları, sıcak bitkinliği, sıcak çarpması**."),
                B("**Sıcak krampları**: aşırı terleme ile **elektrolit kaybı**."),
                B("**Sıcak bitkinliği**: su kaybına bağlı **hipovolemiyi kompanse etmeye çalışan kardiyovasküler sistemin yetersiz kalışı**."),
                B("**Sıcak çarpması**: yüksek ısı ve neme bağlı; **terleme durur, vücut ısısı artar**; **rektal ısının 41°'ye ulaşması tehlikeli**."),
            ]),
            C("Malign hipertermi (s.49)", [
                B("İskelet kasındaki kalsiyum düzeylerini kontrol eden **RYR1** gibi genlerdeki **mutasyonlardan kaynaklanan genetik durum**."),
                B("Cerrahi sırasında **anestezikler** iskelet kasında kalsiyumu artırır → **kaslarda katılaşma, artmış ısı üretimi**."),
                B("Tedavi edilmezse **%80 mortalite**."),
            ]),
            C("Hipotermi ve elektriksel hasar (s.50-51)", [
                B("**Hipotermi**: **32°'de önce bilinç kaybı**, sonra **bradikardi ve atrial fibrilasyon**."),
                B("**Donma** hasarı: hücre içi-dışı sıvı **kristalizasyonu ile tuz yoğunluğu**, hücre içi fiziksel parçalanma, dolaylı **dolaşım değişiklikleri**; **vazokonstrüksiyon ve permeabilite artışı**."),
                B("**Elektriksel hasar** ölümcül olabilir: **yanıklar, VF, kalp ve solunum merkezi yetersizliği**; tip, şiddet ve yanık yaygınlığı akımın **geçtiği yola** ve **amperine** bağlı."),
            ]),
        ],
        [
            C("İyonizan radyasyon hasarı — tanım (s.52)", [
                B("**Radyasyon**: yüksek hızlı partiküller ya da dalgalar şeklinde dolaşan **enerji**; **iyonize ve noniyonize** olarak ayrılır."),
                B("**Noniyonize** (UV, kızılötesi ışık, mikrodalga, ses dalgası): moleküldeki atomları **hareket ettirebilir / titreştirebilir**."),
                B("**İyonize**: sıkıca bağlı **elektronları yerinden sökecek** enerjiye sahip; serbest elektronların diğer atomlarla çarpışması yeni elektron salınımına yol açar → **iyonizasyon**."),
            ]),
            C("Kaynaklar ve biyolojik etkiler (s.53)", [
                B("Ana kaynaklar: **X ve gama ışınları** (çok yüksek frekanslı elektromanyetik dalgalar), **yüksek enerjili nötronlar**, **alfa ve beta partikülleri**."),
                B("Medikal uygulamada **zorunlu**; ancak **mutajenik, karsinojenik ve teratojenik**."),
                B("Biyolojik etkiler: **alınma hızı, alan boyutu, hücre proliferasyonu, hipoksi ve vasküler hasara** bağlı olarak değişir."),
                B("**Vücudun tamamı düşük dozda bile** maruz kalsa çok zararlı etkiler görülebilir."),
            ]),
            C("Morfoloji (s.54)", [
                B("Hayatta kalan hücrelerde **delesyon, kırıklar, kopmalar → kromozomal yapısal değişiklikler**; mitotik iplikçik düzensizliği → **anöploidi**."),
                B("**Nükleer şişme, apoptoz, anormal şekilli hücreler**; **tam onarılamayan DNA hasarı → neoplastik transformasyona zemin**."),
                B("Sitoplazmik değişiklikler: **şişme, mitokondriyal disfonksiyon, ER dejenerasyonu**; sitoplazma membranı bozulabilir."),
                B("**Vasküler dejenerasyon, nekroz ve fibrozis** belirgin."),
            ]),
        ],
        [
            C("Beslenme hastalıkları — malnütrisyon (s.58)", [
                B("**Sağlıklı diyet**: günlük **enerji** (protein, yağ, karbonhidrat); **esansiyel aminoasit ve yağ asitleri**; **vitaminler** ile **kalsiyum ve fosfat** gibi mineraller."),
                B("**Primer malnütrisyon**: bu komponentlerden **biri veya tümü eksik**."),
                B("**Sekonder malnütrisyon**: besin alımı **yeterli**; **malabsorbsiyon, kullanım ve depo bozukluğu, aşırı kayıp, artmış gereksinim**."),
                B("Diyet yetersizliği nedenleri: **yoksulluk, bilgisizlik, kronik alkolizm, akut-kronik hastalıklar, kişisel diyet kısıtlaması**."),
            ]),
            C("Protein enerji malnütrisyonu (PEM) ve marasmus (s.59-60)", [
                B("**Şiddetli PEM ölümcül** olabilir; tüm **kalori ve proteinlerin** vücut ihtiyacını karşılayamaması; **marasmus ve kwashiorkor**."),
                B("İki protein kompartmanı: **somatik** (iskelet kası proteinleri) ve **visseral** (visseral organlar)."),
                B("**MARASMUS**: çocuğun yaş, boy ve cinse göre normal kilosunun **%60'ına** inmesi."),
                B("**Somatik kompartman azalması** → **kas kitlesi kaybı, ekstremitelerde aşırı incelme, gelişme geriliği**.", lvl=1),
                B("**Visseral kompartman çok azalmaz** → **serum albumin normal ya da hafif düşük**.", lvl=1),
                B("**Anemi, multivitamin eksikliği, T hücre aracılı immün yetersizlik**.", lvl=1),
            ]),
        ],
        [
            C("KWASHIORKOR (s.61)", [
                B("**Protein kaybı göreceli olarak kalori kaybından fazla** olduğunda oluşur."),
                B("**Protein yoksulluğu = visseral kompartman kaybı** → **hipoalbuminemi** → **yaygın ve lokalize ödem**."),
                B("**Ağırlık normalin %60-80'i**; artmış su retansiyonu nedeniyle **kilo kaybı maskelenir**; **deri altı yağ dokusu ve kas kitlesi marasmusun aksine korunur**."),
                B("**Kar tanelerini andıran deri lezyonları** (hiperpigmentasyon, deskuamasyon, hipopigmentasyon); **saç incelmesi, düzleşmesi**."),
                B("**Büyümüş yağlı karaciğer**, uyuşukluk, isteksizlik, iştah kaybı; vitamin eksiklikleri, sekonder enfeksiyonlar, immünite defektleri."),
            ]),
            C("PEM morfolojisi (s.62)", [
                B("**Büyüme geriliği**; **kwashiorkorda periferik ödem**; **kas atrofisi ve yağ kaybı marasmusta daha belirgin**."),
                B("**İnce barsak villus ve mikrovillus kaybı, mukozal atrofi, kriptlerde mitoz azalması, laktat intoleransı**: **kwashiorkorda** belirgin (marasmusta daha az)."),
                B("**Her ikisinde kemik iliği hipoplazisi ve anemi**; **beyin**: serebral atrofi, nöron sayısında azalma, myelinizasyon bozukluğu."),
            ]),
            C("Sekonder PEM — kaşeksi (s.64)", [
                B("**Sekonder PEM**: **kronik hastalar**."),
                B("**Kaşeksi**: sekonder PEM'in **kanser hastalarında görülen ilerlemiş formu** — **iştah azalması**, tümör hücresinden salgılanan **proteolizis indükleyici faktör** gibi **kaşektinler**, **sitokinler**."),
            ]),
        ],
        [
            C("Anoreksiya nervoza (s.65)", [
                B("**Belirgin kilo kaybı ile sonuçlanan, kişinin kendini isteyerek aç bırakması**; klinik bulgular **şiddetli PEM'e benzer**.", y="25-26"),
                B("**Endokrin bozukluklar**: düşük **GnRH** sekresyonu ile **amenore**; tiroid hormonu azalması ile **bradikardi, hipotermi, konstipasyon, saç değişiklikleri**.", y="25-26"),
                B("Vücut kılları **lanugo** şeklinde artabilir; **kardiyak aritmiye yatkınlık, osteoporoz, ani ölüm**."),
            ]),
            C("Bulimia (s.66)", [
                B("**Aşırı yemek yeme ve kusmaya zorlama**; devamlı yemek yerler; **anoreksiyadan daha sık, prognozu daha iyi**."),
                B("Komplikasyonlar (zorlamalı kusma ve laksatif kullanımı): **kardiyak aritmiye yol açan elektrolit dengesizliği**, **mide içeriğinin akciğere aspirasyonu**, **özefagusta yırtılmalar**."),
            ]),
            C("A vitamini (s.67-69)", [
                B("Sağlıklı olmak için **13 vitamin**: **A, D, E, K yağda eriyen** (daha kolay depo edilir, malabsorbsiyonda emilimi azalır) + suda eriyenler."),
                B("**Retinol, retinal, retinoik asit**; **karaciğer, balık, yumurta, süt, tereyağı**; havuç, kabak, ıspanak **karotenoid** sağlar."),
                B("Fonksiyon: **az ışıkta normal görme**, özelleşmiş hücre **diferansiyasyonu**, enfeksiyonlara bağışıklık, **mukus salgılayan hücrelerin düzenli farklılaşması**."),
                B("**Eksiklik**: immün yetmezlik, **gece körlüğü**, **yassı epitel metaplazisi**, **kseroftalmi** (kuru göz), **kserozis konjunktiva**, keratin debris = **Bitot lekeleri**, "
                  "**keratomalazi**, en son **tam körlük**."),
                B("**Toksisite**: akut — baş ağrısı, baş dönmesi, kusma, bulanık görme; kronik — kilo kaybı, anoreksiya, bulantı, kusma, kemik ve eklem ağrısı."),
            ]),
        ],
        [
            C("D vitamini — fonksiyon (s.71)", [
                B("**Kalsiyum ve fosforun kan düzeyini** devam ettirir; **raşitizm, osteomalazi ve hipokalsemik tetaniyi** önler."),
                B("**Enterositlerde kalsiyum transportunu** düzenleyerek **intestinal kalsiyum emilimini artırır**."),
                B("**Distal renal tübül** epitel hücrelerinde **kalsiyum geri emilimini** uyarır."),
                B("**PTH ile birlikte** çalışır: osteoblastlardaki **RANK ligandı** düzeyi ve öncül hücrelerdeki **RANK reseptörlerinin aktivasyonu** (slayt ifadesi)."),
                B("**Kemik mineralizasyonunu** sağlar; **osteoblastları uyarır**."),
            ]),
            C("D vitamini eksikliği — morfoloji (s.72-73)", [
                B("**Hipokalsemi** yapar. **Raşitizm**: kıkırdak hücrelerinin olgunlaşmaması, epifizer kıkırdakta aşırı büyüme, **osteoid matriks birikimi**, iskelette deformasyon."),
                B("**Kraniotabes**: oksipital kemiğin düzleşmesi, parietal kemiklerin basmakla içeri çökmesi ve eski pozisyonuna dönebilmesi; osteoid fazlalığı → **frontal çıkıntı, köşeli görünüm**."),
                B("**Raşitik tesbihler** (göğüs kafesinde osteoid/kıkırdak aşırı büyümesi); **güvercin göğsü** (kostalar içeri çöker, sternum öne çıkar); **Harrison çentiği** (diyafram kenarında içe çekilme)."),
                B("**Lomber lordoz ve bacaklarda eğrileşme**; yetişkinlerde eksikliği normal **kemik remodelizasyonunu bozar**."),
                B("**Toksisite**: çocuklarda **metastatik kalsifikasyon**; yetişkinlerde **kemik ağrısı ve hiperkalsemi**."),
            ]),
            C("C vitamini — askorbik asit (s.74)", [
                B("**Süt, karaciğer, balık, sebze ve meyvelerde** bol bulunur."),
                B("Eksikliği: büyüme çağında **kemik hastalığı**; erişkinde **kanama ve yara iyileşme defektleri** ile karakterize **skorbüt**."),
                B("Fonksiyon: inaktif öncüllerinden **prolil ve lizil hidroksilaz aktivasyonu**; **antioksidan**."),
            ]),
        ],
        [
            C("Obezite — tanım ve ölçüm (s.77)", [
                B("**Halk sağlığı sorunu** (diyabet, hipertansiyon gibi pek çok hastalıkla ilişkili); **enerji regülasyon bozukluğu**."),
                B("**Yağ hücrelerinin normal sayısı adolesan çağda sabitlenir.**"),
                B("**BMI = ağırlık (kg) / boy (m)²**: **18,5-25 normal** · **25-30 fazla kilolu** · **>30 obez**."),
                B("Diğer ölçümler: **deri kıvrım ölçümleri**; **bel/kalça oranı** (risk)."),
            ]),
            C("Vücut ağırlığını düzenleyen nörohümoral mekanizmalar (s.78-79)", [
                B("**1- Periferik (afferent) sistem**:"),
                B("Yağ hücrelerinde **leptin ve adiponektin** (**leptin besin alımını azaltır**) · pankreasta **insülin**", lvl=1),
                B("Midede **ghrelin** (**iştahı artırır**) · kolonda **peptit YY** (**tokluk işareti**)", lvl=1),
                B("**2- Efferent sistem**: **arkuat nukleus** (hipotalamus) periferik sinyalleri birleştirir, işler, yeni sinyaller üretir; **POMC/CART** nöronları ve **NPY/AgRP** nöronları ile iletilir."),
                B("**NPY/AgRP kilo almayı artırır**; **POMC/CART kilo kaybettirir**."),
                B("**Leptin**: yağ dokusu bol olduğunda salgılanır; **POMC/CART'ı uyarıp NPY/AgRP'yi inhibe ederek** besin alımını azaltır."),
            ]),
            C("Obezitenin klinik sonuçları (s.80)", [
                B("**Tip 2 diyabet** (insülin direnci, hiperinsülinemi) · **hipertansiyon** · **hipertrigliseridemi ve düşük HDL** ile **koroner arter hastalığı** riski ↑"),
                B("**Kanser**: erkekte **özefagus, tiroid, kolon, böbrek**; kadında **özefagus, endometrium, safra kesesi, böbrek**."),
                B("**Nonalkolik steatohepatit** · **kolelitiazis riski 6 kat** · **dejeneratif eklem hastalıkları**."),
                B("**Hipoventilasyon (Pickwickian) sendromu**: gece ve gün boyu somnolans, uykuda apne, polisitemi, sağ kalp yetmezliği."),
                B("**CRP ve TNF** benzeri proinflamatuar sitokinler obezlerde daha yüksek."),
            ]),
        ],
        [
            C("Slayt sonu örnek sorular (s.81-83) — cevaplar slayt içeriğinden", [
                B("**Uzun süre maruziyette lösemi ve aplastik anemi** nedeni (Eylül-94; asbest, nikel, toluen, etilen glikol, benzen):"),
                B("→ **Benzen** (s.18: lastik sanayi, lösemi riski ↑)", lvl=1),
                B("**İnsanda asbest lifleri ile ilişkili tümör** (Nisan-88; mezotelyoma, timoma, hepatoma, glioblastom, tiroid papiller ca):"),
                B("→ **Mezotelyoma** (s.18)", lvl=1),
                B("**A vitamini eksikliğinde görülmesi en az olası göz bulgusu** (Şubat 2018; gece körlüğü, katarakt, kseroftalmi, konjunktivit, korneal ülserasyon):"),
                B("→ **Katarakt** (s.69'daki eksiklik bulguları arasında yok)", lvl=1),
            ]),
        ],
    ],
    sorular=[
        Q("25-26", 73, "Amenore, konstipasyon, şiddetli PEM'e benzer bulgular; kişinin isteyerek kendini aç bırakması sonucu belirgin kilo kaybı — en olası tanı?",
          "Anoreksiya nervoza",
          "Çeldiriciler: kwashiorkor (ödem, yağlı karaciğer) · marasmus · bulimia (aşırı yeme + kusma) · kaşeksi (kanserde sekonder PEM)"),
        Q("24-25", 77, "Larinks kanseri ve mezotelyomanın etyopatogenezinde rol alan endüstriyel ajan?",
          "Asbest",
          "Çeldiriciler: bisfenol A (endokrin bozucu) · vinil klorür (karaciğer anjiosarkomu) · polisiklik hidrokarbon (akciğer, mesane ca) · organoklorokin (DDT)"),
        Q("23-24", 68, "Sigarayla ilişkili hastalıkların mekanizmalarıyla ilgili doğru OLMAYAN?",
          "“Mukozada direk etki ile mukus üretimini azaltır” (aslında ARTIRIR)",
          "Doğrular: erken doğum riski ↑ · akciğer ca ↑ · myokard oksijenlenmesi ↓ · trombosit agregasyonu ↑"),
        Q("22-23", 68, "Uzun süreli maruziyeti akciğer karsinomu ve mezotelyomaya neden olan?",
          "Asbest",
          "Çeldiriciler: benzen (lösemi) · vinil klorür (karaciğer anjiosarkomu) · bisfenol A (endokrin bozucu) · böcek ilacı DDT"),
    ],
)
