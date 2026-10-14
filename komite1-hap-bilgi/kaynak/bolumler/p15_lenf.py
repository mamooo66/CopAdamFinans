# -*- coding: utf-8 -*-
"""Kaynak: Drive › Komite-1 › PDF › Patoloji › 2026-2027(yeni) › Selma Erdoğan Düzcü ›
11-LENF NODU PATOLOJİSİ 1 (74 slayt) · 12-LENF NODU PATOLOJİSİ 2 (70 slayt; kapak: “Beyaz Kan Hücrelerinin
Neoplastik Proliferasyonları”). Görsel sayfalardaki metin kutuları (kitap alıntıları) da okundu:
PDF1 s.21, s.69 · PDF2 s.24, 37, 40, 42, 59, 60, 61, 69 (özet). ★ = hocanın slayttaki yıldız (*) vurgusu."""

from yardim import B, C, Q  # noqa: F401

BOLUM = dict(
    key="lenf", baslik="Lenf Nodu Patolojisi",
    hoca="Doç. Dr. Selma Erdoğan Düzcü", tarih="14 ve 16 Ekim", saat="4 saat",
    kaynak="11-LENF NODU PATOLOJİSİ 1 · 12-LENF NODU PATOLOJİSİ 2 · Doç. Dr. S. E. Düzcü · 2026",
    ozet=["Her yıl soru gelen ders: **emperipolezis / Rosai-Dorfman** 3 yıl (22-23, 24-25, 25-26); **multipl myelom** 2 yıl (en sık malign plazma hücre diskrazisi, litik lezyon, ileri yaş, CD38+).",
          "**Anaplastik büyük hücreli lenfoma = periferik (matür) T** (22-23, 23-24) — çeldiriciler hep B hücreli. **EMN** Hodgkin'i taklit eder (23-24). **EBV → Burkitt** (24-25, 25-26; Karsinojen dersinde sayıldı).",
          "Hatırlanan “çit tarzı” sorusu: PDF'te çit tarzı = **kedi tırmığı / LGV granülomu**; Castleman'da “soğan zarı” dizilim."],
    slaytlar=[
        # ------------------------------------------------ PDF 1 · normal yapı
        [
            C("Yapı ve fonksiyon", [
                B("Lenf nodları vücudun tüm bölge ve organlarını **drene eden lenfatik sistem** boyunca yerleşir."),
                B("**Lenfoid doku ve destek dokudan** oluşan **kapsüllü** yapılar; bağ dokuyla desteklenmiş, farklı yapısal ve fonksiyonel zonlar şeklinde düzenlenmiştir."),
                B("Destek dokusu: **fibröz doku, retikulin fibrilleri, retikulum hücreleri**. Kapsül ve trabeküller fibröz dokudan; alt yapı desteğini **ince retikulin fibriller** sağlar."),
                B("Hücrelerin büyük çoğunluğu **lenfositler**; ayrıca fagositik **histiyositler (makrofajlar)**, özel aksesuar hücreler (**dendritik retikulum** ve **interdigitating retikulum** hücreleri) ve stromal hücreler."),
            ]),
            C("4 yapısal ve fonksiyonel kısım", [
                B("**Korteks**: B hücreleri ve foliküller (lenfoid folliküller – **B lenfositler**)."),
                B("**Parakorteks**: foliküllerin derinliklerinde; **T hücreleri** (parakortikal bölge – T lenfositler)."),
                B("**Meduller zon**: **plazma hücrelerinin** yoğun olduğu, **sekretuar** kısım (medulla – makrofaj ve plazma hücreleri; **lenfosit azdır**)."),
                B("**Sinüsler**: **fagositer histiyositleri** içerir."),
            ]),
            C("Foliküller", [
                B("**Primer** folikül: küçük, sınırlı, **dolaşıma katılan lenfosit** birikimleri."),
                B("**Sekonder** folikül: lenfoid folikülün **antijenik uyarılmasından sonra** gelişen **germinal merkez** + çevresinde primer folikül için karakteristik küçük lenfositlerin bulunduğu **mantle zon**."),
            ]),
        ],
        [
            C("Germinal merkez", [
                B("Küçük ve büyük **çentikli (sentrosit)**, büyük **çentiksiz (sentroblast)** hücreler, dendritik hücreler ve **“tingible body” makrofajları** içerir."),
                B("Daha az oranda **T hücreleri (daha çok CD4+)** bulunur."),
                B("Tingible body makrofajlar: **karyorektik debris** içeren, **berrak sitoplazmalı**; GM hücreleri arasında görülür."),
            ]),
            C("Dendritik retikulum hücreleri", [
                B("**Germinal merkez immün reaksiyonunda** rol oynar; nükleusları genellikle **uzundur**."),
                B("Sitoplazma uzantıları GM hücreleri arasına girerek **folikülün yapısını şekillendiren bir ağ** oluşturur."),
                B("**Antijeni yakalayıp folikül merkez B hücrelerine sunar** → B hücrelerinin proliferasyonu."),
            ]),
            C("Parakorteks", [
                B("**Timusa bağımlı zon** ya da **T hücre zonu**: nükleer sınırları düzensiz, kondanse kromatinli **küçük T hücreleri**."),
                B("**Hücresel immün cevabın en önemli yeri**."),
                B("**Postkapiller (yüksek endotelli) venüller** burada: küboid/silindirik endotel; kandan gelen, daha çok **T tipi lenfositler** parakortekse bu damarlarla ulaşır."),
                B("**İnterdigitating retikulum (dendritik) hücreleri**: **T lenfositlere antijen sunar**, immün cevabın başlatılmasında önemli; **kemik iliği** kökenli, derinin **Langerhans hücreleriyle** ilişkili."),
            ]),
            C("Sinüsler", [
                B("**Endotel** ile döşeli; **hilusa yaklaştıkça** endotel ortadan kalkar, yerini **histiyositler** alır."),
                B("Fagositer hücreler lenfteki **antijenik olmayan partikülleri** ve **antijenleri** temizler."),
            ]),
        ],
        # ------------------------------------------------ PDF 1 · reaktif lenfadenitler
        [
            C("Reaktif lenfadenitler — genel", [
                B("Birçok farklı antijene cevap → **B ve T lenfositleri, sinüs histiyositleri** ve bazen özelleşmiş aksesuar hücrelerin çoğalması."),
                B("Proliferasyon kişinin **yaşına, immünolojik durumuna**, antijenle **daha önce karşılaşmış olmasına** ve **proliferasyonun süresine** göre değişir."),
            ]),
            C("Sınıflama", [
                B("1- **Akut non-spesifik** lenfadenit"),
                B("2- **Kronik non-spesifik** lenfadenit: **foliküler, interfoliküler, mikst** (foliküler + interfoliküler), **diffüz, sinüs (sinüzoidal)** patern"),
                B("3- **Spesifik** lenfadenitler: **tüberküloz, sarkoidoz, lepra** vb."),
            ]),
            C("Akut non-spesifik lenfadenit", [
                B("**Lokal enfeksiyon** ya da **sistemik bakteriyel/viral enfeksiyona** bağlı; lenf bezi büyümesi ve **ağrı**."),
                B("Mikroskopi: akut iltihabi değişiklikler (**polimorf nükleer lökosit** infiltrasyonu); bazen **apse**; enfeksiyonun deriye açılmasıyla **drenaj sinüsleri**."),
                B("Morfoloji (s.21): nodlar şişmiş, **gri-kırmızı**, dolgun; çok sayıda mitotik figür içeren **büyük germinal merkezler**."),
                B("Neden **pyojenik** organizma ise folliküller çevresinde ve lenfoid sinüslerde **nötrofilik infiltrat**; ağır enfeksiyonda folikül merkezleri **nekroz**a gidebilir, **apse** oluşabilir."),
                B("Nodlar ağrılı; geniş apsede **fluktuasyon**; üstteki deri sıklıkla **kızarık**; akıntılı sinüsler oluşabilir."),
                B("Enfeksiyon kontrol altına alınınca nod normal inaktif görünümüne döner ya da hasar görmüşse **skar (nedbe)** oluşur."),
            ]),
        ],
        [
            C("Kronik non-spesifik lenfadenit — foliküler patern", [
                B("**B hücrelerini aktive eden** enfeksiyon ve inflamatuar olaylarda; foliküler-germinal merkez reaksiyonu → **nonspesifik foliküler hiperplazi**."),
                B("Reaktif folikül: çok sayıda **aktive B hücresi**, arada dağınık T hücresi, nükleer debri içeren **tingible body** makrofajlar, antijen sunan **dendritik ağ**."),
                B("Örnekler: **romatoid artrit / Sjögren**, **anjiyofoliküler hiperplazi (Castleman)**, **HIV** ile ilişkili, **germinal merkezlerin progresif transformasyonu**."),
            ]),
            C("Foliküler hiperplazi", [
                B("Foliküllerin **sayı ve büyüklüğünde artış**; genişlemiş germinal merkezler çevresinde **mantle zon** bulunur."),
                B("Hiperplastik GM'de **mitoz sık**; yüksek proliferatif hızı gösteren **“yıldızlı gök”** manzarası karakteristik."),
                B("Benign folikülün göstergesi: **germinal merkez polaritesi** (★)."),
                B("**En önemli ayırıcı tanısı: foliküler lenfoma** (!!! ★)."),
            ]),
            C("Foliküler lenfoma lehine bulgular ★★★★", [
                B("1- **Tingible body makrofajların bulunmaması**"),
                B("2- **Mitoz oranının düşük** oluşu"),
                B("3- **Mantle zonların tamamen kaybolması** ya da basıklığı"),
                B("4- **bcl-2 pozitifliği**: neoplastik folikül merkez hücreleri bcl-2 ile boyanır, **benign folikül merkez hücreleri boyanmaz**."),
                B("Ayrıca foliküler lenfomaların **%85-90**'ında yapısal sitogenetik **t(14;18)** translokasyonu."),
            ]),
        ],
        [
            C("İnterfoliküler patern", [
                B("Lenf nodunun **T hücrelerindeki immün reaksiyon** sonucu; **hücresel immün yanıtı** tetikleyen uyarılar neden olur."),
                B("**Parakorteks genişler**, folikülleri birbirinden ayırır veya iter; hücresel yapı uyarının cinsi ve süresine göre değişir."),
                B("Örnekler: **nonspesifik interfoliküler (parakortikal) hiperplazi**, **dermatopatik lenfadenit**, **viral enfeksiyonlar (EBV)**, **SLE**, **granülomatöz lenfadenit**."),
            ]),
            C("Mikst (foliküler + interfoliküler) patern", [
                B("**Toksoplazma** lenfadeniti, **kedi tırmığı** hastalığı, **lenfogranuloma venereum**, **mezenterik** lenfadenit."),
            ]),
            C("Diffüz patern", [
                B("Örnekler: **enfeksiyöz mononükleoz** ve diğer viral lenfadenopatiler, anormal immün cevap / **anjiyoimmünoblastik** lenfadenopati, **ilaca bağlı hipersensitivite**, **SLE**, mukokutanöz lenf düğümü sendromu (**Kawasaki**)."),
                B("Lenf düğümünün **çatısı kısmen veya tümüyle silinir**."),
                B("Lenfosit, immünoblast, plazma hücresi, eozinofil ve histiyositten oluşan **polimorfik** populasyon; endotelleri belirgin **postkapiller venül proliferasyonu** eşlik eder."),
            ]),
            C("Sinüs paterni", [
                B("**Lenfatik sinüslerin genişlemesi**: sinüsleri döşeyen **endotel hücrelerinin hipertrofisi** ve **makrofaj infiltrasyonu**."),
                B("Örnekler: **sinüs histiyositozis**, **hemofagositik sendrom**, **yaygın lenfadenopatili sinüs histiyositozis**, **lenfanjiyografi etkisi**, **Whipple** hastalığı."),
            ]),
        ],
        [
            C("Sifiliz", [
                B("**Foliküler hiperplazi** ve **interfoliküler plazmasitozis** ile karakterize (★)."),
                B("**Kapsül ve trabeküller kalınlaşmış**, plazma hücreleriyle infiltre; **perivenüler plazmasitozis**, epiteloid histiyosit kümeleri, **multinükleer dev hücreli epiteloid granülomlar**."),
                B("**Spiroketler** çoğunlukla **postkapiller ven duvarları** çevresinde, bazen germinal merkezler içinde."),
            ]),
            C("Castleman hastalığı", [
                B("Diğer adları: **anjiyofoliküler** lenf düğümü hiperplazisi, **dev lenf düğümü** hiperplazisi."),
                B("En sık yer **mediasten**; ikincil olarak abdominal kavite, akciğer parankimi, aksiller ve servikal bölge."),
                B("Klinik 2 form: en sık **lokalize** tip ve **multisentrik (generalize)** form. Lokalize tipin histolojik 2 major şekli: daha sık **hyalin vasküler**, az görülen **plazma hücreli** tip."),
                B("Hyalin vasküler tip: **1.5-16 cm**, tek ve yuvarlak kitle. Mikroskopi: 1- çevresinde mantle zonlar olan, sıklıkla **“soğan zarı”** şeklinde konsantrik dizilimli, **involüsyona gitmiş / atrofik germinal merkezler**; 2- insizyonda **şiddetli kanama** yapan belirgin **interfoliküler damarlanma** ve **sinüslerin görülmemesi**."),
            ]),
            C("Germinal merkezlerin progresif transformasyonu (GMPT)", [
                B("Germinal merkezlerin **3-4 katına** ulaşan çok büyük oval yapılar / nodüller; transforme GM: küçük lenfositler, rezidü GM hücreleri ve dendritik retikulum hücreleri."),
                B("**Lenfositten zengin Hodgkin** ile sık karıştırılır; Hodgkin'de **LH tipi Reed-Sternberg** hücrelerinin görülmesi tanı koydurucu."),
            ]),
            C("Dermatopatik lenfadenit", [
                B("Çeşitli **benign deri hastalıklarına** ve **mikozis fungoides / Sézary** sendromuna eşlik eder."),
                B("Parakorteks geniş, **soluk sitoplazmalı** hücrelerle genişler: çoğu **histiyosit**, az kısmında **melanin**; aralarında **Langerhans hücreleri**. Parakorteks genişlemesi yüzünden foliküller **atrofik** olabilir."),
            ]),
        ],
        [
            C("Toksoplazma lenfadeniti", [
                B("Özellikle **arka servikal** bölgede, tek veya birden fazla lenf düğümü büyümesi."),
                B("Histoloji: **foliküler hiperplazi**; **interfoliküler bölgelerde epiteloid histiyositler**; **sinüslerin monositoid B hücreleriyle** dolu olması."),
                B("Nadiren **parazitik kistler**; meduller kordonlarda çok sayıda **plazma hücresi**."),
                B("Tanı **serolojik** çalışmalarla doğrulanmalıdır."),
            ]),
            C("Kedi tırmığı hastalığı ve lenfogranuloma venereum", [
                B("Kedi tırmığı etkeni **Bartonella henselae**: **gram negatif**, **Warthin-Starry** boyasında pozitif."),
                B("Doku kesitlerinde benzer görüntü veren **lenfogranuloma venereum**'dan ayırt edilmelidir."),
                B("LGV: **klamidyaların** oluşturduğu, **cinsel yolla** bulaşan hastalık; en sık **inguinal** lenf bezleri."),
                B("İkisinin granülomu belirgin: merkezdeki **süpüratif nekroz** sahasını **çit tarzında** çevreleyen **histiyosit ve fibroblastlar**.", y="21-22"),
                B("Kedi tırmığında küçük nekroz sahaları ve **nötrofil kümelerini** çevreleyen histiyositler bulunabilir."),
            ]),
        ],
        [
            C("Enfeksiyöz mononükleozis — genel ve tanı", [
                B("**Herpesvirus** ailesi üyesi (**EBV**); **adolesan ve genç erişkin**; akut hastalık; **oral temas**."),
                B("**Ateş, boğaz ağrısı** ve yaygın lenfadenit; **aktive CD8+ T lenfositlerin** oluşturduğu lenfositoz."),
                B("**Transforme edici virüs**: monoklonal B hücreli lenfomaya transformasyon."),
                B("Tanı: 1- periferik kanda **atipik lenfositler**; 2- pozitif **heterofil reaksiyonu (Monospot)**; 3- **EBV'ye karşı spesifik antikor** titrelerinde artış."),
            ]),
            C("Patogenez", [
                B("Önce **orofarengeal epitel** hücreleri, sonra lenfoid dokuya yayılarak **B hücreleri** enfekte olur; virüs **latent** kalır."),
                B("EBV ile enfekte B hücreleri EBV proteinleriyle **aktive olur, prolifere** olur; **konak T hücre yanıtı** proliferasyonu ve virüs yayılımını kontrol eder."),
                B("Erken dönemde **viral kapsid antijenine karşı IgM**, sonra **ömür boyu IgG**."),
                B("EBV+ B hücrelerinin kontrolünde **CD8+ sitotoksik T** önemli; dolaşımdaki **atipik lenfositler** = virüse spesifik **CD8+ sitotoksik T (Downey hücreleri)** — karakteristik bulgu."),
            ]),
            C("Morfoloji", [
                B("Kan, lenf nodu, dalak, karaciğerde değişiklikler; **lökositoz**; **atipik lenfositler (CD8+ T)** (★)."),
                B("Lenfadenopati en sık **posterior servikal**, aksiller, inguinal."),
                B("**Splenomegali** (dalakta atipik lenfositler), **rüptüre eğilim**; karaciğerde **portal alan** ve **sinüzoidleri** infiltre eden atipik lenfositler."),
            ]),
            C("Lenf nodu ve Hodgkin ayırıcı tanısı", [
                B("Nonspesifik **foliküler ve/veya parakortikal hiperplazi**; bazen **Hodgkin** ve Hodgkin dışı lenfomayı **taklit eder**, ayrımı zor olabilir.", y="23-24"),
                B("**En karakteristik bulgu** (! ★★): daha çok T hücrelerinden oluşan küçük lenfositler arasında dağılmış **büyük transforme B lenfositlerin** proliferasyonuna bağlı **parakortikal genişleme**."),
                B("Parakortekste atipik T hücreleri; **RS hücrelerinden kolayca ayrılamayan iki çekirdekli** hücreler (enfekte reaktif **B immünoblastlar**) → Hodgkin şüphesi.", y="23-24"),
                B("Hodgkin'deki RS hücreleri **CD15+, CD30+**; EMN'deki taklitçi hücreler **CD15−**."),
            ]),
        ],
        [
            C("SLE'de lenf nodu", [
                B("Hastaların **%30-60**'ında, başta **servikal**, lenf düğümleri büyüyebilir; başta **plazmasitozla** birlikte **foliküler hiperplazi** ve çeşitli spesifik olmayan hiperplaziler."),
                B("Karakteristik: **karyorektik debris içeren nekroz** alanları; burada genellikle **nötrofil yok**, plazmasitoz var."),
                B("Nekroz yaygın, **koagülatif** tipte olabilir; kan damarları nekrotik ve tromboze olabilir."),
                B("**Hematoksilen cisimcikler**: nekroz kenarlarında, sinüslerde, damar duvarında ve çevresinde; **değişikliğe uğramış DNA**'dan oluşan amorf, hematoksifilik yapılar."),
                B("Histolojik SLE yorumu mutlaka **klinik ve serolojik** çalışmalarla doğrulanmalıdır."),
            ]),
            C("Sinüs histiyositozis", [
                B("Lenfatik **sinüslerin genişlemesi**, sinüsleri döşeyen **endotelde proliferasyon**, sinüslerde **histiyosit infiltrasyonu**."),
                B("Sıklıkla **kanserlere komşu** lenf bezlerinde görülen reaksiyon."),
            ]),
            C("Rosai-Dorfman = yaygın (masif) lenfadenopatili sinüs histiyositozis", [
                B("Vakaların çoğu **ilk iki dekatta**; makroskopide fibröz bantlarla ayrılmış **multinodüler** kitleler."),
                B("**Kapsül belirgin kalınlaşmış**; fibrozis kapsül dışındaki dokulara ilerler."),
                B("**Sinüsler bariz genişler**: büyük, şeffaf/köpüklü sitoplazmalı, belirgin nükleoluslu veziküler çekirdekli **çok sayıda histiyositle** dolu.", y="25-26"),
                B("Karakteristik: histiyosit sitoplazmasında çok sayıda **lenfosit**, daha az **plazma hücresi, nötrofil**, hatta **eritrosit**; **fagosite edilmemiş gibi, canlı** görünürler = **EMPERİPOLEZİS**.",
                  y="22-23 24-25 25-26", tuzak="“Richter transformasyonu / Reed-Sternberg hücresi / hematoksilen cisimciği” → YANLIŞ"),
                B("**Meduller kordonların** yoğun **plazma hücresi** infiltrasyonu da karakteristik."),
                B("Görsel (s.69): sinüs histiyositleri **S-100** ile güçlü pozitif; Oil red O ile sitoplazmada bol **nötral lipid**."),
            ]),
        ],
        [
            C("Whipple hastalığı", [
                B("**Abdominal** lenf düğümleri sıklıkla etkilenir; hastaların **%50**'sinde periferik lenfadenopati."),
                B("Sinüsler genişlemiş; doku takibinde **eriyen lipide** bağlı büyük vakuoller; sinüslerde geniş vakuollü sitoplazmalı büyük histiyositler ve **nekrotize olmayan granülomlar**."),
                B("Karakteristik: histiyosit sitoplazmasında **PAS pozitif, orak benzeri** partiküller → elektron mikroskopide **mikroorganizmalara** karşılık gelir."),
            ]),
            C("Spesifik lenfadenitler", [
                B("**Tüberküloz**: **kazeifikasyon nekrozu** gösteren granülomlar."),
                B("**Lepra**."),
                B("**Sarkoidoz**: **iyi sınırlı nonnekrotizan** granülom."),
            ]),
            C("Reaktif ve klonal proliferasyonların ayırıcı tanısı", [
                B("Sitoloji: reaktif **normal** ↔ neoplastik **atipik hücreler**"),
                B("Yapı: reaktif **yapısal değişiklik** ↔ neoplastik **yapısal destrüksiyon**"),
                B("Neden: reaktifte **sıklıkla saptanabilir** ↔ neoplastikte genellikle **bilinen neden yok**"),
                B("Seyir: reaktif **kendini sınırlar / tedaviyle düzelir** ↔ neoplastik **tedavisiz ilerler**"),
                B("Klonalite: **poliklonal** ↔ **monoklonal**"),
                B("Karyotip: **normal** ↔ **kromozomal anormallikler**"),
            ]),
        ],
        # ------------------------------------------------ PDF 2 · beyaz kan hücresi neoplazileri
        [
            C("Beyaz kan hücrelerinin neoplastik proliferasyonları", [
                B("1- **Malign lenfomalar** · 2- **Myeloid neoplaziler** (akut myeloid lösemiler, myelodisplastik sendromlar, kronik myeloproliferatif hastalıklar) · 3- **Plazma hücre diskrazileri** · 4- **Histiyositozlar**"),
            ]),
            C("Etiyoloji ve patogenez", [
                B("1- **Kromozomal translokasyonlar ve onkogenler**: onkogenik rearanjman — **antijen reseptör gen** ekspresyonu sürecindeki hatalardan kaynaklanır."),
                B("2- **Kalıtsal**: **Bloom** sendromu, **Fanconi** anemisi, **ataksi telenjiektazi** → akut lösemi riski artmış; **Down** sendromu ve **nörofibromatozis tip I** → çocukluk çağı lösemileri artmış."),
                B("3- **Virüsler** (★):"),
                B("**HTLV-1** → erişkin T hücreli lösemi/lenfoma", lvl=1),
                B("**EBV** → **Burkitt lenfoma**, **Hodgkin lenfoma**, NK/T hücreli lenfoma", y="23-24 24-25 25-26", lvl=1),
                B("**KSHV / HHV-8** → plevral efüzyon lenfoması", lvl=1),
                B("4- **Çevresel**: **Helikobakter pilori** → gastrik **MALT** lenfoma; **glutene duyarlı enteropati** → intestinal T hücreli lenfoma."),
                B("5- **İatrojenik**: radyoterapi ve kemoterapi (**mutajenik** etki)."),
            ]),
            C("Lösemi – lenfoma", [
                B("**Lösemi**: kemik iliğinin **yaygın tutulumu** ile ortaya çıkan, genellikle **periferik kanda çok sayıda tümör hücresi** bulunan lenfoid neoplazm."),
                B("**Lenfoma**: **belirgin doku kitleleri** ile ortaya çıkan proliferasyon: 1. **Hodgkin** lenfoma, 2. **Hodgkin dışı (non-Hodgkin)** lenfoma."),
                B("Terimler klinik olarak ortaya çıkış anındaki **alışılmış doku dağılımını** tanımlar; **kesin sınırla ayrılamaz**."),
            ]),
        ],
        [
            C("Sınıflama sistemleri", [
                B("**Rappaport (1966)** · Lukes-Collins (1974) · Kiel-Lennert (1974) · WHO (1976) · Working Formulation (1982) · **REAL (1994)** · WHO (1998) · **WHO 2016**"),
            ]),
            C("Tüm sınıflamaların ortak özellikleri", [
                B("Histopatolojik sınıf prognozu belirleyen **tek faktör değildir**."),
                B("**Nodüler / foliküler patern** → yavaş gelişen hastalık, düşük proliferasyon hızı, **uzun yaşam**."),
                B("**Küçük lenfoid hücreler** veya **plazmositik farklılaşma** → **düşük tümör derecesi**."),
                B("**Blastik** veya **büyük hücreler** → **kötü prognoz**.", y="21-22"),
                B("**Tutulum yerleri, büyük tümör kitlesi, serum LDH** düzeyi prognoz için önemli."),
            ]),
            C("WHO sınıflaması", [
                B("**Morfoloji, kaynak hücre-immünfenotip, klinik özellikler ve genotip** temelinde; diğer sınıflamalar yalnız NHL'yi kapsarken **WHO Hodgkin'i de kapsar**."),
                B("3'e ayrılır: **B hücre** tümörleri · **T ve NK hücre** tümörleri · **Hodgkin** lenfoma."),
                B("Lenfoid neoplaziler: 1. **prekürsör B** · 2. **matür B** · 3. **prekürsör T** · 4. **matür T ve NK** · 5. **Hodgkin** lenfoma."),
            ]),
            C("Monoklonalite ve hücre kökeni", [
                B("Malign prekürsörden gelen hücreler **aynı antijen reseptör gen konfigürasyonu ve sekansını** paylaşır, aynı reseptör proteinini (Ig ya da TCR) sentezler = **MONOKLONALİTE**; normal immün yanıt **poliklonal**."),
                B("Lenfoid neoplazilerin **%80-85**'i **germinal merkez / postgerminal merkez B** kökenli; geri kalanın çoğu **T**; **NK kökenli çok nadir**."),
                B("Tümör hücreleri T/B gelişiminin **herhangi bir aşamasının** özelliklerini gösterebilir. **CD (cluster differentiation)**: lenfomaları ayırt etmede kullanılan, hücre serisine spesifik antijenler."),
                B("Özet (s.69): sınıflama **hücre kökeni ve diferansiasyon evresine** göre; **çocukta en sık** öncül B/T kökenli **akut lenfoblastik lösemi/lenfoma**, **erişkinde en sık germinal merkez B** kökenli NHL."),
            ]),
        ],
        [
            C("T hücre antikorları", [
                B("**CD1**: kortikal timositler ve **Langerhans histiyositleri**"),
                B("**CD3**: timositler ve periferik T · **CD4**: T helper"),
                B("**CD5**: T hücreleri ve **B hücrelerinin küçük bir kısmı**"),
                B("**CD8**: sitotoksik T ve bazı NK hücreleri"),
            ]),
            C("B hücre antikorları", [
                B("**CD10**: kemik iliği pre-B ve **germinal merkez B**; **CALLA**"),
                B("**CD19**: kemik iliği pre-B ve matür B (plazma hücresi −)"),
                B("**CD20**: CD19'dan sonraki kemik iliği pre-B ve matür B (plazma hücresi −)"),
                B("**CD21**: **EBV reseptörü**; matür B ve foliküler dendritik hücreler"),
                B("**CD23**: aktive matür B · **CD79a**: kemik iliği pre-B ve matür B"),
            ]),
            C("Monosit / makrofaj antikorları", [
                B("**CD11c**: granülosit, monosit, makrofaj; **tüylü hücreli lösemide de +**"),
                B("**CD13**: immatür ve matür monosit, granülosit · **CD14**: monositler"),
                B("**CD15**: granülositler; **Reed-Sternberg hücreleri**"),
                B("**CD33**: myeloid progenitörler, monositler · **CD64**: matür myeloid hücreler"),
            ]),
            C("NK, kök hücre, aktivasyon", [
                B("**CD16**: NK ve granülositler · **CD56**: NK ve T hücrelerinin az bir kısmı"),
                B("**CD34**: pluripotent hematopoetik kök hücreler ve progenitörler"),
                B("Aktivasyon: **CD30**: aktive B, T hücreleri ve monositler; **Reed-Sternberg hücreleri**"),
            ]),
        ],
        [
            C("WHO — B hücreli neoplazmlar", [
                B("**I. Prekürsör B**: prekürsör B-lenfoblastik lösemi/lenfoma"),
                B("**II. Periferal (matür) B**: 1- B-KLL / küçük lenfositik lenfoma · 2- B-prolenfositik lösemi · 3- lenfoplazmasitik lenfoma · 4- splenik ve nodal marjinal zon · 5- ekstranodal marjinal zon · 6- mantle hücreli · 7- foliküler · 8- tüylü hücreli lösemi · 9- plazmasitoma / plazma hücreli myeloma · 10- diffüz büyük B · 11- Burkitt"),
            ]),
            C("WHO — T / NK hücreli neoplazmlar ve Hodgkin", [
                B("**III. Prekürsör T**: prekürsör T-lenfoblastik lösemi/lenfoma"),
                B("**IV. Periferik (matür) T ve NK**: 1- T-prolenfositik lösemi · 2- büyük granüler lenfositik lösemi (LGL) · 3- **mikozis fungoides / Sézary** · 4- periferik T-hücreli lenfomalar"),
                B("5- **Anaplastik büyük hücreli lenfoma** → **T hücre kökenli** (periferik T grubu)", y="22-23 23-24",
                  tuzak="mantle, foliküler, küçük lenfositik, marjinal zon, Burkitt “T hücreli” → YANLIŞ (hepsi B)"),
                B("6- anjiyoimmünoblastik T · 7- enteropati ilişkili T · 8- pannikülit benzeri T · 9- hepatosplenik γδ T · 10- adult T-hücreli lenfoma/lösemi · 11- NK/T hücreli lenfoma, nazal tip · 12- NK hücreli lösemi"),
                B("**V. Hodgkin lenfoma**"),
            ]),
            C("B hücreli neoplazmlar — genel", [
                B("B kökenli NHL'ler İHK ile, kaynaklandıkları **immatür / matür** lenfositlere göre **prekürsör** ve **periferik** B hücreli olarak ikiye ayrılır."),
                B("Doku kesitlerinin **İHK boyanması lenfoma tanısı için gereklidir** → B ve T-NK kökenli ayrımı."),
                B("Parafin kesitlerde B hücreli lenfomaların tespitinde **CD20 ve CD79**."),
            ]),
        ],
        [
            C("B hücreli lenfoblastik lösemi / lenfoma (B-ALL) ★★", [
                B("**Çocukluk ve ergenlik** yaşları ve **erkeklerde** daha sık."),
                B("KI'de biriken blastlar normal hematopoezi baskılar; genellikle KI ve periferik kan tutulumuyla **akut lösemi** tablosu."),
                B("**İmmatür lenfositlerden (lenfoblast)** → **agresif** tümörler."),
                B("Solid tümörleri sık olarak LN, KI, dalak, karaciğer, **Waldeyer halkası**; seyrek **deri ve testis**; **mediastinal** tutulum da var."),
                B("Histolojik olarak **T-hücreli lenfoblastik lenfomadan ayrılamaz**."),
            ]),
            C("Patogenez", [
                B("Başlıca defekt **diferansiyasyonda duraklama**: diferansiyasyonu düzenleyen **transkripsiyon faktörlerinde edinsel mutasyonlar**."),
                B("En sık mutasyona uğrayan TF genleri: **TEL1, AML1, E2A, PAX5, EBF**."),
                B("Ek olarak en sık mutasyon: **t(9;22)** ile oluşan **BCR-ABL** füzyon geni (**Philadelphia kromozomu**)."),
            ]),
            C("Klinik, morfoloji, prognoz", [
                B("**Ani ve şiddetli** başlangıç; anemiye bağlı halsizlik, nötropeniye bağlı ateş, trombositopeniye bağlı kanama; **kemik ağrısı** ve hassasiyeti; yaygın LAP, splenomegali, hepatomegali; sinir felçleri gibi **SSS** bulguları."),
                B("Lenf nodu **diffüz** infiltre; immünofenotip: **TdT** ve **CD10 (CALLA)** pozitif."),
                B("**2-10 yaş iyi prognozlu**; yoğun kemoterapiyle **%80'den fazlasında** tam tedavi."),
                B("Kötü prognoz: **erkek** cinsiyet, **2 yaştan küçük**, **10 yaştan büyük**, tanıda **lökosit sayısının yüksek** olması."),
                B("Özet (s.69): son derece agresif; **KI yetmezliği** bulguları ya da **hızlı büyüyen kitle** ile; diferansiasyonu durduran genetik lezyonlar → **immatür nonfonksiyonel blast** birikimi."),
            ]),
        ],
        [
            C("Kronik lenfositik lösemi / küçük lenfositik lenfoma ★★", [
                B("Küçük lenfositlerden oluşan **monoklonal B hücreli** neoplazm; **NHL'lerin %5**'i."),
                B("**Yavaş büyüyen, yavaş ilerleyen** tümör: tümör hücresinin **hayatta kalma süresinin uzaması** proliferasyondan daha önemli."),
                B("Kemik iliği ve lenf nodlarından kaynaklanır; **ileri yaş**, **kadınlarda** daha sık."),
                B("En sık **servikal, aksiller, inguinal** LN; çoğu vakada karakteristik **periferik kan tutulumu**; hepatosplenomegali ve trombositopeni görülebilir."),
            ]),
            C("Patogenez", [
                B("Apoptozisi engelleyen **Bcl-2 seviyesi çok yüksek**; Bcl-2'nin negatif düzenleyicisi **mikroRNA**'ları kodlayan genlerde **delesyonlar**."),
                B("**İmmündisregülasyon**: KLL hücre birikimi normal B fonksiyonunu baskılar → **hipogammaglobulinemi**."),
                B("Paradoksal olarak hastaların **%15**'inde kendi **eritrosit ve trombositlerine karşı otoantikor**."),
            ]),
            C("Histoloji, genetik, immünfenotip", [
                B("Normalden hafifçe büyük, **kaba kromatinli yuvarlak** nükleuslu, **dar sitoplazmalı**, monomorfik lenfositlerden **diffüz** infiltrasyon."),
                B("**Mitoz az**, daha çok **proliferasyon merkezlerinde**; tedavi edilemeyen **düşük gradeli** neoplazm."),
                B("En sık genetik değişiklik: **trizomi 12** ve **11, 13, 17**. kromozom delesyonları; kötü prognoz işareti **Notch1** aktive edici mutasyonu."),
                B("**%3-10**'unda prolenfositik / büyük hücreli lenfomaya transformasyon = **Richter sendromu** ★★★★"),
                B("**CD5+, CD20+, CD23+, CD43+, CD79+**"),
            ]),
        ],
        [
            C("KLL/SLL — morfoloji (s.24)", [
                B("Tutulan LN: **küçük lenfosit tabakaları** + aktif bölünen büyük hücrelerin seyrek, sınırları belirsiz odakları; baskın hücre küçük inaktif lenfosit."),
                B("Mitotik aktif hücre odakları = **proliferasyon merkezleri** → **KLL/SLL için patognomonik**."),
                B("LN'e ek olarak **KI, dalak ve karaciğer** hemen hemen tüm olgularda tutulmuş; çoğu hastada **mutlak lenfositoz**."),
                B("Dolaşımdaki tümör hücreleri **frajil**: yaymada parçalanarak karakteristik **smudge hücreleri**; kanda daha büyük aktive lenfositler de bulunur."),
            ]),
            C("KLL/SLL — klinik", [
                B("Genellikle **asemptomatik**; en sık bulgu **kolay yorulma, kilo kaybı, iştahsızlık**; LAP, splenomegali."),
                B("Geç dönemde **hipogammaglobulinemi** → **bakteriyel enfeksiyonlara** eğilim; daha az sıklıkla **otoimmün hemolitik anemi** ve trombositopeni."),
                B("**Medyan sağkalım 4-6 yıl**; zamanla daha agresif tümöre (**prolenfositik lösemi** ya da **diffüz büyük B hücreli lenfoma**) dönüşüm = **Richter transformasyonu** (SLL → büyük hücreli lenfoma)."),
                B("Özet (s.69): genellikle **KI ve LN** tutulumu; enfeksiyon ve otoimmün hastalığa eğilim gibi **immün sistem anormallikleriyle** ilişkili, yavaş seyirli."),
            ]),
            C("B hücreli prolenfositik lösemi", [
                B("**Olgunlaşmamış büyük lenfositlerden** (prolenfosit, paraimmünoblast) oluşur."),
                B("LN'de sınırları belirgin, yer yer foliküle benzer proliferasyon (**psödofolikül**) odakları."),
                B("Hücreler normalden büyük; kaba kromatinli yuvarlak nükleus, **belirsiz nükleolus**, **geniş sitoplazma**."),
            ]),
        ],
        [
            C("Lenfoplazmasitik lenfoma (immünositoma)", [
                B("Sıklıkla **lösemik**; çoğu vaka **serum IgM yüksekliği** ile karakterize **hiperviskozite** semptomları (**Waldenström makroglobulinemisi**) ile birlikte."),
                B("**İleri yaş**, **kadınlarda** daha sık."),
                B("LN'de küçük yuvarlak dar sitoplazmalı lenfositler, **plazmasitoid lenfositler** (sıklıkla eksantrik nükleuslu, geniş sitoplazmalı) ve plazmositlerden diffüz infiltrasyon."),
                B("Sitoplazmada **Russell**, nükleusta **Dutcher cisimciği**: **PAS (+)** inklüzyon cisimcikleri (★)."),
                B("Mitoz nadir; **düşük gradeli** lenfoma."),
            ]),
            C("Dalak marjinal zon lenfoması", [
                B("Dalakta **beyaz pulpanın marjinal ve mantle zonundan** çıkar; **kırmızı pulpa** infiltrasyonu sık; dalak **masif** büyümüş."),
                B("Tipik olarak **KI ve periferik kan** tutulumu; genellikle **periferik LAP yok**; immünofenotipi nodal ve ekstranodal MZL'ye benzer."),
            ]),
            C("Nodal marjinal zon lenfoması", [
                B("Çoğunluğu **Sjögren** sendromlu veya diğer ekstranodal **MALT** tip lenfomalı hastalarda."),
                B("Lenfoid foliküllerin **mantle zon dışındaki marjinal zondan** kaynaklanan **monositoid ve MALT tip düşük grade B** hücreli lenfomalar ★★★★★★"),
                B("Dalak, KI ve periferik kan tutulumu sık; **ileri yaş**, **kadınlarda** sık."),
                B("LN'de **subkapsüler ve parankimal sinüsler** ile **parafoliküler** bölgelerde **monositoid B lenfosit** infiltrasyonu."),
            ]),
        ],
        [
            C("Ekstranodal marjinal zon lenfoması (MALT) ★★", [
                B("**Yetişkin** ve **kadınlarda** sık; çoğu hastada **Sjögren, Hashimoto** gibi otoimmün hastalık ya da **H. pylori gastriti** → MALT'tan lenfoma gelişimi."),
                B("Sıklıkla **GİS mukozası**, **parotis**, akciğer, lakrimal gland, konjonktiva, oküler kanaliküli."),
                B("Mukozalardaki lenfoid foliküllerin **marjinal zonundan** kaynaklanan küçük lenfositik lenfoma: düzensiz kaba kromatinli nükleuslu, geniş sitoplazmalı küçük lenfositler."),
                B("Mukozal epitelin infiltrasyonu = **lenfoepitelyal lezyon (LEL)** ★★"),
                B("GİS'te **kenarları kalkık ülserler** ve kaba infiltrasyonlar; mideden gelişenler genellikle **H. pylori** ile birlikte."),
            ]),
            C("Seyir ve prognoz", [
                B("Tanıda sıklıkla **lokalize (evre I, II)**."),
                B("**Midedekiler bağırsaktakilerden daha iyi** prognozlu; **beyin, böbrek** gibi organlardan çıkanlarda prognoz çok daha kötü."),
                B("Midede **reaktif, poliklonal** bir enfeksiyon olarak başlar, zamanla **monoklonal** B hücre tümörüne dönüşür; **antibiyotik tedavisi sonrası regresyon** bildirilmiş."),
                B("Zamanla uzak yayılım ve **diffüz büyük B hücreli lenfomaya** dönüşüm olabilir."),
            ]),
            C("Tablo (s.37): MALT tipi marjinal zon B hücreli lenfoma", [
                B("Morfoloji: küçük **sentrosit benzeri** hücreler, **“monositoid B hücreleri”**, lenfositler, plazma hücreleri."),
                B("İmmünoloji: yüzey Ig **+**; **CD5 −, CD10 −**; CD19, 20, 22, 79a **+**; **CD23 −**."),
                B("Genetik: birçok olguda **t(11;18)**; bazılarında **trizomi 3**."),
                B("Klinik: **indolent**, sıklıkla lokalize; büyük hücreli lenfomaya dönüşebilir. REAL şeması nodal MZL'yi (“monositoid B hücreli lenfoma”) provizyonel antite olarak alır."),
            ]),
        ],
        [
            C("Mantle hücreli lenfoma", [
                B("Sekonder foliküllerin **mantle zonundaki naif B** hücrelerine benzeyen hücreler."),
                B("**Orta-ileri yaş**, **erkeklerde** daha sık."),
                B("Jeneralize LAP, KI, dalak, **Waldeyer** halkası, periferik kan ve özellikle **lenfomatöz polipozis** olarak GİS tutulumu."),
                B("LN'de diffüz, foliküler ya da mantle zon proliferasyonu: normalden hafifçe büyük, **yuvarlak düzensiz kenarlı, çentikli** nükleuslu, dar sitoplazmalı lenfositler."),
                B("Tanıda genellikle **yayılmış**; periferik kan tutulumu sık."),
                B("İmmünofenotip **Cyclin D1+**; genotip **t(11;14)**: 11. kromozomda cyclin D1'i kodlayan **BCL-1 (PRAD-1)** + 14. kromozomdaki **Ig ağır zinciri**."),
                B("**Orta derecede agresif** tümör."),
            ]),
            C("Morfoloji (s.40) ve özet (s.69)", [
                B("LN'leri **diffüz** ya da belli belirsiz **nodüler** patern şeklinde tutar; düzensiz nükleus, **belirgin olmayan nükleolus**, dar sitoplazma; daha nadiren hücreler büyük ve **lenfoblastlara** benzer."),
                B("Olguların çoğunda **KI** tutulumu, yaklaşık **%20**'sinde **periferik kan** tutulumu."),
                B("Bazen **GİS**'ten kaynaklanır: makroskopik olarak polibe benzeyen submukozal nodüller (**lenfomatoid polipozis**)."),
                B("Özet: LN, KI ve GİS gibi ekstranodal bölgelerin tutulumuyla giden **ileri evre** hastalık; hücre siklusunda düzenleyici **siklin D1 overekspresyonu** ile sonuçlanan **t(11;14)**."),
            ]),
        ],
        [
            C("Foliküler lenfoma — genel", [
                B("**Batıda sık**; genellikle **ağrısız yaygın LAP**; yetişkinlerde sık; **E/K eşit**; tanıda genellikle **yayılmış**."),
            ]),
            C("Morfoloji", [
                B("Genellikle **nodüler** proliferasyon; normal **germinal merkez B** hücrelerine benzer: **sentrosit ve sentroblast**."),
                B("**Sentrosit** (en sık): inaktif lenfositten biraz büyük, **belirgin girintili, çentikli** nükleus; kromatin kaba ve yoğun, nükleol belirgin değil."),
                B("**Sentroblast**: daha büyük; **veziküler kromatinli**, birkaç nükleollü, dar sitoplazmalı."),
                B("**Mitoz az**, **apoptoz yok**."),
            ]),
            C("Grade (büyük hücre oranı)", [
                B("**Grade I**: büyük hücreler **%25'ten az** veya her büyük büyütme sahasında **5'ten az**"),
                B("**Grade II**: **%25-50** veya her büyük büyütme sahasında **5-15**"),
                B("**Grade III**: **%50'den fazla** veya her büyük büyütme sahasında **15'ten fazla**"),
            ]),
            C("Klinik", [
                B("Tanı anında **kemik iliği tutulumu %85**; genellikle **50 yaş üstü**; cinsiyet farkı yok; **ağrısız LAP**."),
                B("Dalakta **beyaz pulpa**, karaciğerde **portal aralık** tutulumu sık; **ekstranodal tutulum sık değil**."),
                B("Vakaların **%10**'unda periferik kanda lenfositoz (**20.000'den fazla**)."),
                B("Yavaş ilerleme, uzun yaşam (**ort. 7-9 yıl**); **tam tedavi edilebilir değil**; bazı vakalarda **diffüz büyük B hücreli lenfomaya** transformasyon."),
            ]),
        ],
        [
            C("Foliküler lenfoma — immünfenotip, genetik, patogenez", [
                B("**CD10 (CALLA) +/−, CD20+, CD79+**; **CD5−, CD23−, CD43−, Cyclin D1−**."),
                B("Birçok folikül merkez hücreli lenfomada antiapoptotik **Bcl-2+**; bu protein **normal germinal merkez B hücrelerinde bulunmaz** (KLL/SLL'deki gibi BCL2 eksprese eder)."),
                B("Folikül merkez hücreli lenfomaların **%85**'inde (s.42: **%85'inden fazlasında**), **küçük hücreli tipin %100**'ünde **t(14;18)**: kromozom 18'deki **BCL2** + kromozom 14'teki **IgH** lokusu füzyonu → **BCL2 overekspresyonu**; tümör hücresi sağkalımına etkili."),
                B("Olguların **üçte birinde** histon asetil transferazları kodlayan genlerde fonksiyon kaybı mutasyonları → **epigenetik** değişimler."),
                B("Özet (s.69): tümör normal **germinal merkez B** hücrelerinin büyüme paternini taklit eder."),
            ]),
            C("Tüylü hücreli lösemi (hairy cell)", [
                B("Diğer adı **lösemik retiküloendoteliyozis**; **kronik B hücreli** lösemi."),
                B("**Orta yaş** grubu **kadınlarda** sık."),
                B("KI, periferik kan tutulumu ve **masif splenomegali**; **LN tutulumu nadir**."),
                B("Sitoplazması **soluk** boyanan, **ince uzantıları** olan büyük hücreler; nükleus yuvarlak/oval, kimi vakada kıvrık veya serebriform, kiminde daha büyük ve bir bölgesi çöküntülü."),
                B("Tümör hücrelerinde **tartarata dirençli asit fosfataz (TRAP)**; CD tablosunda **CD11c** tüylü hücreli lösemide de +."),
            ]),
        ],
        [
            C("Plazmasitoma (soliter myeloma)", [
                B("Plazma hücreli neoplazmların **%3-5**'i; yumuşak doku veya kemikte **soliter** lezyon."),
                B("Kemik dışı lezyonlar en sık **sinüsler, nazofarenks, larinks**."),
                B("Hastaların yaklaşık **%25**'inde M protein düzeyinde orta derecede yükselme."),
                B("Nadiren yayılır; sınırlı, **lokal rezeksiyonla** tedavi edilebilir; **5-10 yılda MM'a** progrese olur."),
            ]),
            C("Multipl myelom ★★★", [
                B("**En sık görülen malign plazma hücre diskrazisi**; iskelette **multifokal litik lezyonlar** ve kemik iliğinde neoplastik **plazma hücresi** proliferasyonu ile karakterize.", y="24-25 25-26"),
                B("**Erkeklerde** ve **ileri yaşlarda** sık.", y="24-25 25-26"),
                B("En sık **vertebra, kosta, kafatası, pelvis, femur, skapula**; lezyonlar **medulladan** başlar, kortikal kemiği yıkar → **patolojik fraktürler**.", y="24-25"),
                B("Atipik plazmositlerde **üzüm salkımına benzeyen, Ig içeren vakuoller**; nükleus kaba kromatinli, etrafında **halo**, hücrenin bir kenarında; nükleol belirgin (**plazmablast**); çift nükleuslu ve multinükleer hücreler."),
            ]),
            C("MM — yayılım, böbrek, laboratuvar", [
                B("Ekstramedüller infiltrasyon genellikle **abdominal LN**; ileri dönemde dalak, karaciğer, böbrek, akciğer."),
                B("Böbrek tutulumu → **myeloma nefrozu**: interstisyumda anormal plazma hücreleri, tübüllerde **Bence-Jones proteininden** (idrarla atılan düşük molekül ağırlıklı **hafif zincirler**) silendirler; silendirler genellikle **multinükleer dev hücrelerle** sarılı."),
                B("Olguların **%99**'unda serum, idrar ya da her ikisinde Ig veya Ig hafif zincirinde **monoklonal artış**."),
                B("Myeloma proteinlerinin aşırı yapımı ve kümelenmesi → **hiperviskozite sendromu**."),
                B("İmmünofenotip: **CD38+**.", y="25-26"),
                B("Özet (s.69): multipl litik kemik lezyonları → patolojik fraktür ve **hiperkalsemi**; neoplastik plazma hücreleri **normal humoral bağışıklığı baskılar**, **nefrotoksik parsiyel immünglobulinler** salgılar."),
            ]),
        ],
        [
            C("Diffüz büyük B hücreli lenfoma (DBBHL) ★★★", [
                B("**Erişkinde en sık görülen lenfoma** tipi; medyan yaş **60**, her yaşta görülebilir; ileri yaş ve **erkeklerde** sık."),
                B("**Agresif** lenfoid neoplazmların **%60-70**'i, **NHL'lerin %30-40**'ı."),
                B("**Ekstranodal** yerleşim sık (**GİS, deri, kemik, beyin, tiroid**); sıklıkla tek bir nodal / ekstranodal bölgede **hızlı büyüyen kitle**."),
                B("Cilt, GİS, kemik, beyin, **Waldeyer halkası**, orofarengeal lenfoid dokular sık tutulur; dalak ve karaciğerde **büyük destrüktif kitleler**; agresif, **hızlı öldürür**."),
            ]),
            C("Histoloji", [
                B("**Diffüz büyüme paterni**; veziküler kromatinli, belirgin konturlu yuvarlak/oval nükleuslu **büyük lenfositler** (lenfositten **4-5 kat**; s.61 kitap kutusu: inaktif lenfositin **en az 3-4 katı**)."),
                B("Bir kısmı nükleer membrana bitişik **2-3 nükleollü (sentroblast)**, bir kısmı merkezde **tek nükleollü (immünoblast)**; bazı vakalarda immünoblastlar **plazmasitoid** diferansiasyon gösterir."),
                B("Hücre tipleri: **sentroblastik, immünoblastik, anaplastik**. Sentroblastik → **germinal merkez** kökenli (“sentroblastik-sentrositik spektrum”un bir ucu); immünoblastik → **plazma hücresi** yapımına giden B olgunlaşma yolu (LN'nin **ekstrafoliküler** alanları)."),
                B("Bazen ileri derecede **anaplastik**: Hodgkin lenfomanın **Reed-Sternberg** hücrelerine benzeyen dev tümör hücreleri."),
            ]),
        ],
        [
            C("DBBHL — immünfenotip, genetik, patogenez", [
                B("İmmünofenotip: **CD20+, CD22+, CD79+**, CD45+/−, CD5−/+, CD10−/+."),
                B("Genotip: **%20-30 Bcl-2+**, **%20-40 Bcl-6+**; **t(8;14)** bulunur."),
                B("Patogenez (s.60): yaklaşık **üçte birinde 3q27**'deki **BCL6** geninde yeniden düzenlenme; daha yüksek oranda **BCL6 promoter** bölgesinde aktive edici nokta mutasyonu → germinal merkez B hücrelerinde önemli transkripsiyon düzenleyicisi **BCL6 proteini yüksek**."),
                B("Bir diğer **%30**'unda **BCL2** overekspresyonuna yol açan **t(14;18)** → bazıları **“transforme” foliküler lenfoma** olabilir; yaklaşık üçte birinde histon asetil transferaz genlerinde fonksiyon kaybı (**epigenetik**)."),
                B("Özet (s.69): matür B tümörlerinin **heterojen**, büyük hücreli, **agresif** grubu; **en sık görülen lenfoma tipi**; üçte biri foliküler lenfomadan kaynaklanır."),
            ]),
            C("Burkitt lenfoma ★★★★★", [
                B("**Orta boyutlu çentiksiz** lenfositlerin hakim olduğu **periferik B** hücreli neoplazm."),
                B("**Afrika'da 5-15 yaş** arasında **en sık görülen tümör**; **erkek çocuklarda** daha sık."),
                B("**EBV** ile ilgili: tümör hücrelerinde **virüs DNA genomu** bulunmuş.", y="24-25 25-26"),
                B("Afrika'da primer lezyon **%60 maksilla / mandibula**, **%25 abdominal** (retroperitoneal LN, karaciğer, böbrek, bağırsak, over)."),
                B("Endemik olmayan bölgelerde **abdominal** primer sık; **ülkemizde çene dışı** lokalizasyon daha sık."),
            ]),
        ],
        [
            C("Burkitt — morfoloji ve genetik", [
                B("**Monoton** hücreler; **vakuollü (nötral yağ) bazofilik** sitoplazma; yuvarlak nükleus, **2-5 santral bazofilik nükleol**."),
                B("Orta büyüklükte hücreler (**histiyosit nükleusu kadar ya da daha küçük**); diffüz monoton patern; koheziv ama köşelenmeler oluşturan hücreler; kaba kromatinli nükleus, **multipl bazofilik nükleol**."),
                B("**Mitoz sık**; metabolik aktivite çok yüksek → **nekrotik hücreler** sık; yüksek proliferasyon ve apoptoz."),
                B("Tümöre saçılmış **saydam sitoplazmalı histiyositler** → **“yıldızlı gök” (starry-sky)**: **karakteristik ama patognomonik değil**."),
                B("Genotip: **t(8;14)** sık — kromozom 8'deki **MYC** genini ilgilendiren translokasyonlar."),
            ]),
            C("Klinik tipler", [
                B("**Endemik**: Afrika, Papua Yeni Gine; çocuklar, E:K = 2/1; **EBV ilişkili**; **çene** ve diğer yüz kemikleri, ileum, çekum, gonadlar, böbrek, meme."),
                B("**Sporadik**: çocuklar ve genç erişkinler, E:K = 2/1 – 3/1; **tüm çocukluk çağı lenfomalarının %30-50**'si; **EBV %30**; **abdominal (ileoçekal)**, gonadlar, böbrek, meme."),
                B("**İmmün yetmezlik ilişkili**: **HIV**; **EBV %25-40**; nodal ve kemik iliği."),
                B("Özet (s.69): son derece agresif matür B tümörü; genellikle **ekstranodal** bölgelerden; **MYC** translokasyonları; hücreler sıklıkla EBV ile **latent** enfekte."),
            ]),
        ],
    ],
    sorular=[
        Q("25-26", 74, "Lenf nodunda büyüme; mikroskopide sinüslerde çok sayıda histiyositle genişleme ve emperipolezis ile karakterize lenfadenit?",
          "Rosai-Dorfman hastalığı", "Castleman, sifiliz, kedi tırmığı, EMN değil"),
        Q("25-26", 75, "İleri yaş, kemikte litik lezyonlar, CD38 + malign plazma hücre diskrazisi?",
          "Multipl myelom", "Mantle hücreli, ALCL, Hodgkin, mikozis fungoides değil"),
        Q("25-26", 76, "Burkitt lenfoma ve nazofaringeal karsinomun etyopatogenezinde önemli rol oynayan? (Karsinojen Ajanlar'da sayıldı)",
          "Epstein-Barr virüsü", "HPV, HBV, şistozomiyazis, H. pylori değil · bu derste: EBV → Burkitt, Hodgkin, NK/T", ref=True),
        Q("24-25", 78, "Burkitt lenfoma gelişiminde rolü olan enfeksiyon? (Karsinojen Ajanlar'da sayıldı)",
          "Epstein-Barr virüsü", "H. pylori, HPV, HBV, şistozomiyazis değil", ref=True),
        Q("24-25", 79, "Yaygın LAP'li sinüs histiyositoziste histiyosit sitoplazmasında nötrofil, lenfosit, plazma hücrelerinin fagosite edilmemiş gibi bulunması?",
          "Emperipolezis", "Richter transformasyonu, RS hücresi, hematoksilen cisimciği, mantle zon değil"),
        Q("24-25", 80, "Erkek, ileri yaş; multifokal litik kemik lezyonları, patolojik fraktür; en sık malign plazma hücre diskrazisi?",
          "Multipl myelom", "Foliküler, lenfoplazmasitik lenfoma, hairy cell, Hodgkin değil"),
        Q("23-24", 71, "Hodgkin lenfoma ile ayırıcı tanısı yapılması gereken ve HL patogenezinde rolü olan reaktif lenfadenit?",
          "Enfeksiyöz mononükleozis", "Sifiliz, Castleman, dermatopatik, LGV değil · PDF: EMN Hodgkin'i taklit eder (RS benzeri hücreler CD15−); EBV → Hodgkin"),
        Q("23-24", 72, "T hücre kökenli malign lenfoma?",
          "Anaplastik büyük hücreli lenfoma", "Mantle, foliküler, küçük hücreli, Burkitt = B"),
        Q("22-23", 71, "Periferik T hücreli lenfoma grubunda yer alan?",
          "Anaplastik büyük hücreli lenfoma", "Foliküler, mantle, marjinal zon, Burkitt = B"),
        Q("22-23", 72, "Yaygın LAP'li sinüs histiyositoziste histiyosit sitoplazmasında lenfosit, nötrofil, plazma hücrelerinin canlı durması?",
          "Emperipolezis", "Richter sendromu, RS hücresi, granülom, atipik hücre değil"),
        Q("21-22", None, "Popcorn görünümü, CD15 −, CD30 − ?",
          "Nodüler lenfosit predominant Hodgkin lenfoma",
          "Hatırlanan soru · PDF'te yalnız klasik RS CD15+, CD30+ ve GMPT ayırıcı tanısında “LH tipi RS hücresi” · (PDF'te geçmiyor)"),
        Q("21-22", None, "“Çit tarzı görünüm” (lenf nodu patolojisi)",
          "PDF'e göre: kedi tırmığı / LGV granülomu (hatırlanan cevap “Castleman?”)",
          "PDF: süpüratif nekrozu çit tarzında çevreleyen histiyosit + fibroblast; Castleman'da “soğan zarı” konsantrik dizilim"),
        Q("21-22", None, "Lenfoma sınıflamalarının ortak bulguları: blast hücre … ?",
          "Blastik veya büyük hücreler kötü prognozu gösterir",
          "Hatırlanan soru (H4) — önce sınıflanmamıştı; PDF2 s.9 ile birebir"),
    ],
)
