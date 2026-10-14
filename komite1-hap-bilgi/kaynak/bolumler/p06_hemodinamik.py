# -*- coding: utf-8 -*-
"""Kaynak: Drive › Komite-1 › PDF › Patoloji › 2026-2027(yeni) › Selma Erdoğan Düzcü › 5-HEMODİNAMİK BOZUKLUKLAR
(Drive'dan yalnızca ilk 80 slaytın metni okunabildi: sıvı dengesi, ödem, hiperemi/konjesyon, hemoraji, hemostaz ve
Virchow triadına kadar tromboz. 81. slayttan sonrası okunamadığı için bu bölümde yoktur.)"""

from yardim import B, C, Q  # noqa: F401

BOLUM = dict(
    key="hemodinamik", baslik="Hemodinamik Bozukluklar",
    hoca="Doç. Dr. Selma Erdoğan Düzcü", tarih="25 ve 28 Eylül", saat="3 saat",
    eksik='PDF 9 MB: Drive yalnızca **ilk 80 slaytın** metnini verebildi (tromboz başında, “Endotelyal hasar” slaytında kesiliyor). Sonraki kısım — **trombüsün devamı, DIC, emboli, infarktüs, şok** — bu bölümde **yok**; PDF küçültülüp yüklenince eklenecek.',
    kaynak="5-HEMODİNAMİK BOZUKLUKLAR · Doç. Dr. S. E. Düzcü · 2026",
    ozet=["Son 5 yılda **6 soru**: **ödem mekanizması** (22-23, 23-24), **vWF = GpIb–kollajen köprüsü** (22-23), **trombomodülin** (24-25), "
          "**hemodinamik tanım çeldiricileri** (25-26), **soluk infarkt** (24-25).",
          "Tuzaklar: ödem **koldan değil bacak/sakrumda** (bağımlı) · **lenfatik obstrüksiyon ödem yapar** · **albümin ↓ → ödem** · "
          "**transuda proteinden fakir** · **hiperemi = arteriol dilatasyonu** · **ekimoz 1-2 cm, peteşi 1-2 mm**."],
    slaytlar=[
        [
            C("Sıvı dengesi ve kan akımı bozuklukları", [
                B("Hücre ve dokuların sağlıklı olması için oksijen dağıtımını sağlayan ve artıkları yok eden normal **sirkülasyon (dolaşım)** yanında **normal sıvı dengesi** de gerekir."),
                B("**Vasküler volüm**, **vasküler basınç**, **protein içeriği** ve **endotel işlevindeki** değişiklikler suyun vasküler duvarı geçmesine neden olur."),
                B("Total vücut sıvısı başlıca **2 kompartmanda**: **intrasellüler (hücre içi)** ve **ekstrasellüler (hücre dışı)** sıvı."),
                B("Ekstrasellüler sıvı: a) **intersellüler (hücreler arası) = interstisyel (dokular arası)** sıvı; b) **intravasküler sıvı (kan plazması)**.", lvl=1),
                B("**Homeostaz**: internal çevrenin **sabit veya statik (dengede duran)** koşullarda korunmasıdır; vücut sıvılarında homeostaz **öncelikle böbreklerde** sağlanır."),
                B("Suyun vücuttan ayrılmasında başlıca yollar: **böbrekler, GİS, akciğer, deri**."),
                B("Aşırı terleme/zorlu solunum veya mide-barsak yoluyla anormal sıvı kaybında (diyare) **böbreğin düzenleyici mekanizmaları su kaybını kısıtlar**."),
            ]),
            C("Böbrekte sıvı hacminin düzenlenmesi: ADH", [
                B("Sıvı hacmi böbrek tarafından **2 yolla** düzenlenir: **1) ADH (vazopresin)**, **2) aldosteron**."),
                B("**ADH**: böbrek tübüllerinden **su geri emilimini** sağlar; **nörohipofizden (arka hipofiz)** salgılanır."),
                B("Su alımı azalınca **ADH ↑** → su geri emilip kana verilir; aşırı su alınınca **ADH üretimi durur** → toplayıcı kanallarda su geri emilmez, vücut dışına atılır.", lvl=1),
            ]),
        ],
        [
            C("Aldosteron ve renin-anjiyotensin", [
                B("**Aldosteron**: **böbreküstü bezi korteksinden** salgılanır; böbrek tübüllerinden **Na⁺ ve onunla birlikte suyun geri emilimini (su retansiyonu)** sağlar."),
                B("Salgılanması daha çok **renin-anjiyotensin** mekanizmasıyla düzenlenir."),
                B("**Renin**: böbrekte oluşturulan enzim; böbrek arterlerine gelen **kan akımı ve hacminin düşmesi renin salgısını artırır**.", lvl=1),
                B("Renin, **anjiyotensinojeni → anjiyotensin I → aktif form anjiyotensin II**'ye dönüştürür.", lvl=1),
                B("**Anjiyotensin II** aldosteron salgısını artırır; güçlü **vazokonstriktördür** → kan basıncını artırır.", lvl=1),
                B("**Kalp yetmezliğinde** böbrekte kan akımı azalır (hipovolemi) → yetersiz perfüzyon → **renin-anjiyotensin-aldosteron** uyarılır → **Na ve su tutulumu → ödem**."),
            ]),
            C("Ödem ve efüzyon: tanımlar", [
                B("Vücut ağırlığının ortalama **%60'ı sudur**; bu suyun **%40'ı intrasellüler**, **%20'si ekstrasellüler** alanda yer alır."),
                B("Dokularda hücreler arası aralıkta sıvı birikimi: **ÖDEM**. Vücut boşluklarında anormal oranda sıvı birikimi: **EFÜZYON**."),
                B("Ödem ve efüzyon **iltihabi** veya **iltihabi olmayan** olabilir; ödem **yaygın (sistemik-genel)** veya **lokalize (yerel-fokal)** bir olaydır."),
                B("**Anazarka**: tüm vücudu tutan, derialtı bağ dokusunda belirgin şişme yapan, şiddetli ve yaygın ödem."),
                B("Efüzyon türleri: **hidrotoraks** (plevra), **hidroperikardium** (perikard), **hidroperitoneum** (periton; asit)."),
            ]),
        ],
        [
            C("Transuda ve eksuda", [
                B("Normalde damar içine giren ile çıkan sıvı miktarı birbirine yakındır; çok az fazla sıvı ekstrasellüler aralıkta kalır, o da **lenfatiklerle dolaşıma** döner."),
                B("**Transuda**: **iltihabi olmayan** ödem sıvısı; **hidrostatik basınç artışı veya intravasküler kolloid azalması** sonucu gelişir.",
                  y="22-23", tuzak="“Transuda vasfında ödem proteinden zengin olup dansitesi yüksektir” → YANLIŞ"),
                B("**Düşük protein ve kolloid** içerir (ör. sol kalp yetmezliğine bağlı akciğer ödemi); **özgül ağırlığı 1.012'nin altında**.", lvl=1),
                B("**Eksuda**: **iltihabi** sıvı birikimi; **artmış vasküler permeabilite** ile oluşan inflamatuar ödem sıvısı."),
                B("**Proteinden ve hücreden zengin** (akut iltihap); **özgül ağırlığı 1.020'den fazla**.", lvl=1),
            ]),
            C("Ödemin oluşumu: Starling", [
                B("Ödemin mikroskopik görünümü: **doku boşluklarının genişlemesi**; doku **gevşek** görünümdedir."),
                B("Ödem, intravasküler kompartmandan interstisyel sıvıya doğru hareket ettiren **güçlerin artması** sonucu oluşur."),
                B("**Starling kanunlarına** göre normal sıvı değişimi, damar içi ve dışı **hidrostatik ve osmotik basınçlarla** düzenlenir."),
                B("**İltihabi olmayan ödemin** oluşumu şu şekillerde özetlenebilir:"),
                B("1- İntravasküler alandaki **hidrostatik basınç artışı** · 2- Plazmada **kolloidal osmotik basıncın azalması**", lvl=1, y="22-23"),
                B("3- **Lenfatik akımın bozulması** · 4- Böbreklerde **tuz ve su retansiyonu**", lvl=1),
            ]),
        ],
        [
            C("Artmış hidrostatik basınç", [
                B("Ödem ve efüzyon nedenleri, **artmış hidrostatik basınç**: **A. konjestif kalp yetmezliği, B. portal hipertansiyon, C. venöz obstrüksiyon, D. konstriktif perikardit**.",
                  y="22-23 23-24"),
                B("**Derin ven trombozunda** bir bacağa sınırlı ödem."),
                B("**Konjestif kalp yetmezliği**: böbrek kanlanması azalır, **santral venöz basınç artar**; böbrekte **renin-anjiyotensin-aldosteron sistemi** devreye girer."),
                B("**Renal vazokonstriksiyon**, **su ve tuz tutulumu**, **ADH salınımı**.", lvl=1),
                B("Tutulan sıvı damar içinde tutulamaz, böbrekten su ve tuz tutulumu sürer → **ödem daha da artar**.", lvl=1),
                B("Renal vazokonstriksiyon kanlanmayı daha da azaltır → **idrar çıkışı azalır**, ödem daha da artar.", lvl=1),
            ]),
            C("Azalmış plazma ozmotik basıncı", [
                B("**Kolloid ozmotik basıncından primer olarak albümin** sorumludur."),
                B("**Protein kayıpları veya azalmış protein sentezinde** ozmotik basınç düşer → **sekonder hiperaldosteronizm**; azalan protein yerine konulmadıkça tutulan su damar içinde muhafaza edilemez.",
                  y="22-23", tuzak="“Plazma albümin seviyesinin artışı ödeme neden olur” → YANLIŞ"),
                B("Nedenler: **nefrotik sendrom (albümin kaybı)**, **siroz (azalmış albümin sentezi)**, **malnütrisyon**, **protein kaybettiren gastroenteropatiler**."),
            ]),
            C("Lenfatik obstrüksiyon; Na ve su tutulumu", [
                B("**Lenfatiklerin obstrüksiyonu**: genelde **lokalize**; **inflamasyonlar veya tümörlere sekonder** (meme karsinomunda deri lenfatiklerinin tıkanması = **portakal kabuğu görünümü**).",
                  y="22-23", tuzak="“Lenfatiklerin obstrüksiyonu ödeme neden olmaz” → YANLIŞ"),
                B("**Lenf nodu disseksiyonları** sonucu ödem; **filariasis**: inguinal lenfatiklerin parazitik infeksiyonu → **elefantiasis**."),
                B("**Na ve su tutulumu**: primer olarak **post-streptokoksik glomerülonefrit** ve **akut böbrek yetmezliği** gibi renal fonksiyonu kısıtlayan hastalıklarda görülür."),
            ]),
        ],
        [
            C("Ödem morfolojisi", [
                B("Subkutanöz ödemin **klinik tespiti** (makroskopik tanı mikroskopik tanıdan daha önemli): **çukurlaşan (pitting) ödem**."),
                B("Belirgin ödematöz subkutan dokuya parmakla baskı → interstisyel sıvı yer değiştirir, parmak kalkınca yer **çökük kalır** = **pitting ödem**."),
                B("Subkutan ödem, hidrostatik basıncın en yüksek olduğu **kalp seviyesinin altındaki** kısımları tutar: en çok **ayaktayken bacaklarda**, **yatarken sakrumda** → **bağımlı ödem**.",
                  y="22-23", tuzak="“Subkutan ödemin klinik değerlendirilmesi koldan yapılır” → YANLIŞ"),
                B("**Nefrotik sendromda** ödem daha yaygın ve şiddetlidir; ilk bulgusu **periorbital ödem** olabilir (ilk olarak **gevşek bağ dokusunda**)."),
                B("Ödem makroskopik olarak kolay saptanır; mikroskopide **ekstrasellüler matriks elemanları arasında ayrılma ve berraklaşma** görülür."),
                B("Herhangi bir dokuyu tutabilse de ödem en sık **subkutan dokular, akciğer ve beyni** etkiler."),
            ]),
            C("Pulmoner ödem ve beyin ödemi", [
                B("**Pulmoner ödem**: **en sık sol ventrikül yetmezliğinde**; ayrıca **böbrek yetmezliği, ARDS, pulmoner infeksiyonlar ve hipersensitivite reaksiyonlarında**."),
                B("Akciğerler normalden **2-3 kat ağırdır**; kesit yüzünden **köpüklü, bazen kanla boyalı sıvı** sızar (hava + ödem sıvısı + ekstravaze eritrositler).", lvl=1),
                B("**Beyin ödemi** nedenleri: **travma, apse, tümör, venöz akımın tıkanması, infeksiyon**; **lokalize** (ör. apse/tümör) veya **generalize** olabilir."),
                B("Yaygın ödemde beyin **şiş**, giruslar genişlemiş (kafatası basısıyla yassılaşmış), **sulkuslar daralmıştır**.", lvl=1),
            ]),
        ],
        [
            C("Ödemin klinik önemi ve özeti", [
                B("**Cilt ödemi** altta yatan **ciddi hastalığı** gösterir; ayrıca **yara iyileşmesini bozar** (belirgin subkutan ödem de)."),
                B("**Akciğer ödemi** oksijen değişimini önler; biriken sıvı **enfeksiyona zemin** hazırlar. **Beyin ödemi herniasyona** yol açabilir."),
                B("Ödem nedenleri (özet): **artmış hidrostatik basınç** (ör. kalp yetmezliği) · **artmış vasküler geçirgenlik** (ör. inflamasyon)."),
                B("Plazma albümin azalmasına bağlı **azalmış kolloid ozmotik basınç**: **azalmış sentez** (ör. karaciğer hastalığı, protein malnütrisyonu) veya **artmış kayıp** (ör. nefrotik sendrom).", lvl=1),
                B("**Lenfatik obstrüksiyon** (ör. inflamasyon, neoplazi) · **sodyum birikimi** (ör. böbrek yetmezliği)."),
            ]),
            C("Hiperemi ve konjesyon", [
                B("Her iki durumda da bir alandaki **kan miktarı normale göre artmıştır**."),
                B("**Hiperemi**: **arteriol dilatasyonu ve artmış kan akımına** bağlı **aktif** olay; bir alana gelen kan miktarında artış (egzersiz, iltihap). Hiperemik dokular **kırmızıdır**.",
                  y="25-26", tuzak="“Hemoraji: arteriol dilatasyonu ile artmış kan akımı” → YANLIŞ"),
                B("**Konjesyon**: **venöz kanın dokudan uzaklaştırılması yavaşlamıştır** (konjestif kalp yetmezliği, lokal venöz tıkanmalar); dokular **mavi-kırmızı** (**siyanoz**)."),
            ]),
        ],
        [
            C("Hiperemi-konjesyon morfolojisi", [
                B("Konjesyon arttıkça dokuda **deoksijenize hemoglobin** birikir → doku **mavi** renk alır; konjesyon ile **ödem genelde bir aradadır**."),
                B("**Uzun süren konjesyon (kronik pasif konjesyon)** → hipoksi → **parankim hücre hasarı**."),
                B("Kronik konjesyon alanında **kapiller rüptür** → küçük **kanama odakları** ve **hemosiderin yüklü makrofajlar**."),
                B("Hiperemik/konjesyonlu dokuların kesit yüzeyleri **ıslak ve tipik olarak kanlıdır**."),
            ]),
            C("Akciğerde konjesyon", [
                B("**Akut pulmoner konjesyon**: kapillerler eritrositlerle dolu; **septal ödem** ve fokal **intraalveolar kanama** olabilir."),
                B("**Kronik pulmoner konjesyon**: septumlar **kalınlaşmış ve fibrotik**; alveollerde çok sayıda **hemosiderin yüklü makrofaj (kalp yetmezliği hücreleri)**."),
            ]),
            C("Karaciğerde konjesyon", [
                B("**Akut hepatik konjesyon**: **santral ven ve sinüzoidler** kanla genişlemiş; **santral hepatosit dejenerasyonu** (nekroza bağlı santral hepatosit kaybı bile olabilir)."),
                B("**Periportal hepatositler** hepatik arteriollere yakın oldukları için daha iyi kanlanır; şiddetli hipokside daha az hasar görür, yalnızca **reversible yağlı değişiklik** gelişebilir."),
            ]),
            C("Karaciğerin kronik pasif konjesyonu", [
                B("Gross: **lobül merkezi kırmızı-kahve renkli ve deprese (hafif çökük)**, çevresi konjesyonsuz açık kahve → **nutmeg (hindistan cevizi) karaciğeri**."),
                B("Mikroskopi: **kanama**, **hemosiderin yüklü makrofajlar**, **sentrilobüler hepatosit nekrozu**."),
                B("Çok uzun süreli, şiddetli konjesyon (en sık **kalp yetmezliği** ile) → **hepatik fibrozis (kardiyak siroz)**."),
                B("Lobülün santral kısmı kanın **en son ulaştığı alan** olduğundan hepatik kan akımının azaldığı **her durumda (ör. şok)** **sentrilobüler nekroz** gelişebilir; önceden konjesyon gerekmez."),
            ]),
        ],
        [
            C("Hemoraji (kanama)", [
                B("**Kanama: damar dışına kanın kaçması**."),
                B("**Büyük damarların rüptürü**: ateroskleroz, travma, inflamatuvar veya neoplastik erozyonlar. **Küçük damarların rüptürü**: daha çok **hemorajik diatezlerde**."),
                B("Kanama **vücut dışına** olabilir; bir **doku içine birikirse hematom**."),
                B("Vücut boşluklarına kanamalar lokalizasyonuna göre adlandırılır: **hemotoraks, hemoperikardium, hemoperitoneum, hemartroz**."),
            ]),
            C("Peteşi, purpura, ekimoz", [
                B("**Peteşi**: deri, müköz membran veya serozal yüzeydeki **küçük (1-2 mm)** kanamalar."),
                B("**Purpura**: daha büyük (**3-5 mm**) kanamalar."),
                B("**Ekimoz**: daha da büyük (**1-2 cm**) **subkutan** kanamalar (ezik, çürük).",
                  y="25-26", tuzak="“Ekimoz: deri ve mukozalarda çok küçük noktasal kanama” → YANLIŞ"),
                B("Ekstravaze eritrositler **makrofajlarca** fagosite edilip yıkılır."),
                B("**Hemoglobin (kırmızı-mavi) → bilirubin (mavi-yeşil) → hemosiderin (altın sarısı-kahverengi)** dönüşümü ekimozun **karakteristik renk değişimini** oluşturur.", lvl=1),
            ]),
            C("Kanamanın klinik etkileri", [
                B("Total kan hacminin **%20'sinden azı** kaybedilirse ciddi sorun olmaz; **kalp veya akciğer hastalığı** varsa hafif kayıplar bile oksijen taşıma kapasitesini ciddi düşürür."),
                B("Total kanın **%20'sinden fazlasının** kaybı **hemorajik şok**a yol açar."),
                B("**Beyin içine kanama** az da olsa öldürücüdür; **kronik rekürren kanamalar** → **demir eksikliği anemisi**."),
                B("Görseller: **kolonda peteşial kanama (trombositopeniye bağlı)**, **fetal intraserebral kanama**."),
            ]),
        ],
        [
            C("Hemostaz: tanımlar", [
                B("**Normal hemostaz**: kanın damar içinde **akışkan halde tutulması**; damarda hasar olursa hasar yeri **lokalize hemostatik tıkaç** ile hemen kapatılır."),
                B("Patolojik karşılığı **tromboz**: normal, hasarlanmamış veya az hasarlanmış damar içinde **kan pıhtısı (trombüs)** oluşması."),
                B("Aşamalar: **primer hemostaz** · **sekonder hemostaz** · **antitrombotik mekanizmaların devreye girmesi**."),
                B("Rolü olanlar: **damar duvarı** (endotel, bazal membran, kollajen) · **trombositler** · **koagülasyon kaskadı**."),
            ]),
            C("Endotel: düzenleyici rol", [
                B("**Endotel hücreleri hemostazın en önemli düzenleyicileridir**."),
                B("Normal endotel, zedelenme/aktivasyondan önce **trombosit agregasyonunu ve koagülasyonu inhibe eden, fibrinolizi uyaran antikoagülan faktörleri** eksprese eder."),
                B("Bu denge bozulunca (zedelenme ve aktivasyondan sonra) endotel **prokoagülan aktivite** kazanır."),
            ]),
            C("Normal endotelin antitrombotik etkileri", [
                B("**İntakt endotel** trombosit, plazma koagülasyon faktörleri ve son derece trombojenik **subendotelyal ekstrasellüler matriks** arasındaki etkileşimi engeller."),
                B("**Antiplatelet, antikoagülan ve fibrinolitik** etkileri vardır:"),
                B("**Antiplatelet**: plateletin ECM ile temasını önler (**fiziksel bariyer**); **ADPaz** sentezleyerek **ADP'yi parçalar** → trombosit agregasyonu inhibe edilir.", lvl=1),
                B("**Antikoagülan**: **membrana bağlı heparin benzeri moleküller** ve bir trombin reseptörü (**trombomodülin**) vasıtasıyla; **doku faktörü yolu inhibitörünün (TFPI)** de majör kaynağıdır.", lvl=1, y="24-25"),
                B("**Fibrinolitik**: **doku tipi plazminojen aktivatörü (tPA)** salgılayarak **fibrinolizi tetikler**.", lvl=1),
            ]),
        ],
        [
            C("Aktive/hasarlı endotelin protrombotik özellikleri", [
                B("1- **Trombositlerin aktivasyonu**: **vWF sentezi**."),
                B("2- **Pıhtılaşma faktörlerinin aktivasyonu**: **TNF ve IL-1** ile uyarılma → **doku faktörü** salgısı; doku faktörü koagülasyonun **başlıca in vivo aktivatörüdür**, **trombomodülin ekspresyonunu baskılar**."),
                B("3- **Plazminojen aktivatör inhibitörlerinin (PAI)** sentezi (**antifibrinolitik etki**)."),
            ]),
            C("Trombositler: yapı ve adezyon", [
                B("**Kemik iliği megakaryositlerinden** kan akımına giren, **nükleus içermeyen** hücre parçacıklarıdır."),
                B("**Vasküler defektleri kapatan hemostatik tıkaç** oluşumu ve aktif koagülasyon faktörlerinin bir yüzeyde birikimini sağlayarak normal hemostazda **kritik rol** oynar."),
                B("Trombosit fonksiyonu **integrin ailesine ait birkaç glikoprotein reseptörüne**, **kontraktil hücre iskeletine** ve **iki tip sitoplazmik granüle** bağlıdır: **α granülleri ve δ granülleri**."),
                B("Platelet ECM ile temas ederse: **adezyon, şekil değişikliği, sekresyon ve agregasyon** olur."),
                B("**Adezyon (yapışma)**: platelet yüzeyindeki **glikoprotein Ib (Gp Ib)** ile **kollajen** arasında köprü kurulmasıyla olur; **köprüyü vWF (von Willebrand faktörü) kurar**.", y="22-23"),
                B("**Gp Ib eksikliği: Bernard-Soulier sendromu**.", lvl=1),
            ]),
        ],
        [
            C("Trombosit aktivasyonu ve agregasyon", [
                B("**Sekresyon**: **Ca⁺⁺** sekresyonu koagülasyon kaskadı için önemlidir; sekrete edilen **ADP güçlü agregandır**; aktivasyon yüzeyde **fosfolipid kompleksinin** belirmesine yol açar."),
                B("Adezyon ve sekresyonu takiben salgılanan **ADP ve TxA2** **primer agregasyonu** gerçekleştirir."),
                B("Bu sırada koagülasyon kaskadında **trombin** oluşur; trombin agregasyonu daha da artırıp bölgeyi **fibrin ağı** ile örer (**sekonder hemostaz**)."),
                B("**Agregasyon**: henüz fibrine dönüşmemiş **fibrinojen**, trombosit yüzeyindeki **Gp IIb-IIIa reseptörlerini** birbirine bağlayarak birçok trombositi bir araya getirir."),
                B("**Gp IIb-IIIa reseptör eksikliği: Glanzmann trombasteni**; **Gp IIb-IIIa inhibitörleri** tedavide (antikoagülan olarak) verilmiştir.", lvl=1),
                B("**Trombin** monosit, nötrofil ve eritrosit adezyonunu da artırarak pıhtı içinde bunların da artışını sağlar."),
            ]),
            C("Koagülasyon kaskadı (pıhtılaşma zinciri)", [
                B("Hemostatik sürecin önemli komponentidir; **nihai hedef trombin oluşturmaktır**; **trombin fibrinojeni fibrine çevirir**."),
                B("Zincirdeki her basamak **fosfolipid kompleksi üzerinde** ve **Ca⁺⁺ iyonları** varlığında gerçekleşir."),
                B("**İntrinsik ve ekstrinsik** yollarla başlatılabilir; bu iki yolağın aktivasyonu klinikte takip edilir:"),
                B("**Protrombin zamanı (PT)**: **ekstrinsik yol** (F VII, X, II, V ve fibrinojen) → **kumadin takibi**.", lvl=1),
                B("**Parsiyel tromboplastin zamanı (PTT)**: **intrinsik yol** (F XII, XI, VIII, X, V, II ve fibrinojen) → **heparin takibi**.", lvl=1),
            ]),
        ],
        [
            C("Trombin", [
                B("**Fibrini oluşturur**, **trombosit agregasyonunu artırır**."),
                B("**Endoteli aktive eder**: trombinle aktive edilen endotel **t-PA, NO, PGI2 ve PDGF** salgılar (**pıhtıyı sınırlandırmak için**)."),
                B("**Nötrofil adezyonunu artırır**; **mononükleer iltihabi hücreleri aktive eder**."),
            ]),
            C("Koagülasyon kaskadının kontrolü", [
                B("1- **Antitrombin III**: **trombin, faktör IXa, Xa, XIa ve XIIa** aktivitesini önler; endotel yüzeyinde **heparin benzeri moleküllere** bağlanırsa aktive olur."),
                B("2- **Trombomodülin**: **trombin reseptörüdür**; trombin bağlanırsa **Protein C ve S**'i aktive eder → bunlar **F Va ve VIIIa**'yı inaktive eder.", y="24-25"),
                B("3- **Doku faktör yolu inhibitörü (TFPI)**: **endotelden salgılanır**; **F Xa ve VIIa-doku faktörünü** inaktive eder."),
            ]),
            C("Fibrinolitik kaskad", [
                B("**Fibrinoliz büyük ölçüde plazmin** ile gerçekleşir; **plazmin, plazminojenin proteolizi** ile üretilir."),
                B("**F XII bağımlı** plazmin aktivasyonu."),
                B("**Ürokinaz benzeri plazminojen aktivatörü (u-PA)**: serumda bulunan plazmini aktive eder."),
                B("**Doku tipi PA (t-PA)**: **endotel sentezler**; **fibrine bağlanırsa en aktif** hali ile çalışır."),
                B("**Streptokinaz**: **bakteri ürünü** plazminojen aktivatörüdür."),
                B("Plazminin fibrini yıkmasıyla oluşan **fibrin yıkım ürünleri zayıf antikoagülandır**."),
                B("**D-dimer**: kanda saptanan fibrin yıkım ürünüdür; çeşitli **trombotik hastalıkların teşhisinde** faydalanılır."),
            ]),
            C("Tromboz: patogenez (Virchow triadı)", [
                B("**Trombozun patogenezi — Virchow triadı**: **1- endotelyal hasar** · **2- staz veya türbülan akımlar** · **3- pıhtılaşma eğiliminde artış (hiperkoagülabilite)**."),
                B("**Endotelyal hasar**: endotel hasarlanınca **prokoagülan etkiler artarken antikoagülan etkiler azalır**."),
                B("Endotel hasarının nedenleri: **ateroskleroz**, **hipertansiyon**, **toksik ürünler (sigara, homosistein, radyasyon)**."),
            ]),
        ],
    ],
    sorular=[
        Q("25-26", 71, "Hemodinamik bozukluklarla ilgili doğru olan?",
          "DIC: mikrosirkülasyonda yaygın trombüsler ve kanamalarla giden tüketim koagülopatisi",
          "Hiperemi = arteriol dilatasyonu (hemoraji değil) · ekimoz 1-2 cm, peteşi 1-2 mm · DIC, Zahn, infarkt: PDF 81+. slayt okunamadı"),
        Q("24-25", 74, "Hangi organda soluk (beyaz) infarkt görülür?", "Böbrek",
          "Akciğer, over, testis, barsak → kırmızı infarkt · (PDF 81+. slayt okunamadı; doğrulanamadı)"),
        Q("24-25", 75, "Hemostazda salınımı pıhtılaşma zincirini bloke ederek antitrombotik etki gösteren?", "Trombomodulin",
          "Trombomodülin: trombin reseptörü → Protein C/S → F Va, VIIIa inaktif · vWF, ADP, TXA₂, fibrin = protrombotik"),
        Q("23-24", 66, "Ödem oluşumunda hidrostatik basınç artışının ön planda olduğu durum?", "Konjestif kalp yetmezliği",
          "Nefrotik sendrom, malnütrisyon, protein kaybettiren gastroenteropati = ozmotik basınç ↓ · lenfatik tıkanıklık = lenfatik obstrüksiyon"),
        Q("22-23", 65, "Ödem morfolojisiyle ilgili doğru olan?",
          "Ödem azalmış ozmotik basınçta ya da artmış hidrostatik basınçta gelişebilir",
          "Yanlış şıklar: koldan değerlendirilir (PDF: bacak/sakrum) · lenfatik obstrüksiyon ödem yapmaz · albümin ↑ ödem yapar · transüda proteinden zengin"),
        Q("22-23", 66, "Primer hemostazda trombosit adezyonunda GpIb ile kollajen arasında köprü?", "von Willebrand faktör (vWF)",
          "Trombin, ADP, TXA₂, pıhtılaşma zinciri değil · Gp Ib eksikliği = Bernard-Soulier"),
    ],
)
