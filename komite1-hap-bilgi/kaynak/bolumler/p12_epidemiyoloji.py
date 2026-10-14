# -*- coding: utf-8 -*-
"""Kaynak: Drive › Komite-1 › PDF › Patoloji › 2026-2027(yeni) › Selma Erdoğan Düzcü › 10-NEOPLAZİDE EPİDEMİYOLOJİ
(58 slayt; slayt başlığı "Kanser Epidemiyolojisi"; s.14-29 metinsiz grafik/tablo sayfaları — s.14-15 görselden okundu)"""

from yardim import B, C, Q  # noqa: F401

BOLUM = dict(
    key="epidem", baslik="Neoplazide Epidemiyoloji",
    hoca="Doç. Dr. Selma Erdoğan Düzcü", tarih="8 Ekim", saat="1 saat",
    kaynak="10-NEOPLAZİDE EPİDEMİYOLOJİ · Doç. Dr. S. E. Düzcü · 2026",
    ozet=["**23-24**: Türkiye verilerine göre en sık kanserler → **erkekte akciğer, kadında meme**. Çeldiriciler: erkekte prostat/mide, "
          "kadında over/tiroid/kolorektal (hepsi 2. sıra ve altı).",
          "**22-23**: ağız boşluğunda **yassı hücreli ca**'ya zemin hazırlayan bozukluk → **lökoplaki** (s.55); çeldiriciler başka kanserlerin zemini.",
          "Bu dersten çıkmış **2 soru** var: biri **s.14-15 grafiklerinden**, diğeri **s.55 preneoplastik bozukluk listesinden**."],
    slaytlar=[
        [
            C("Epidemiyoloji — tanım (s.2)", [
                B("**Epidemiyoloji** = tıp ve sağlık bilimlerinde **araştırma yöntem bilimi**."),
                B("Sağlık olaylarının **kişi, yer ve zaman** özelliklerini (**epidemiyolojik 3'lü**) irdeleyerek **“topluma tanı koymayı”** amaçlar."),
                B("**Kanser epidemiyolojisi**: toplumda ve riskli bireylerde kanserin **kimde-nerede-ne zaman** görüldüğünü belirleyerek topluma tanı koyar."),
                B("**Özneleri tekil bireyler değil, riskli toplum kümeleridir.**"),
            ]),
            C("Kanser kayıtçılığı ve kanserin doğası (s.3)", [
                B("Ülkenin kanser epidemiyolojisini yansıtmak için ülkeyi temsil edecek **toplam ülke nüfusunun %20'sinin** kanser verilerini toplamak yeterlidir."),
                B("**Kanser = hücre büyüme ve davranış bozukluğu** → nedenleri **hücresel ve moleküler düzeyde** tanımlanmalıdır."),
            ]),
            C("Kanser sıklığı (s.4)", [
                B("Kanser sıklığı **problemin büyüklüğünü** anlamada önemlidir."),
                B("Günümüzde kanser, **erken tanı** konulduğunda tedavi olabilen, en azından bir grup hasta için **kronik hastalıktır**."),
                B("**En çok ölüme neden olan kanser: akciğer kanseri.**"),
            ]),
            C("Olgu sayısı ve risk altındaki nüfus (s.6)", [
                B("**Belirli bir süre içindeki yeni kanser olgu sayısı**: belirli yıla ait, belirli coğrafik alanda ikamet eden **yeni kanser tanısı almış vakaların toplam sayısı**."),
                B("**Belirli bir süre içinde izlenen risk altındaki nüfus**: belirli yıla ait, belirli coğrafik alandaki **kanser geliştirme olasılığı olan toplam nüfus**."),
            ]),
        ],
        [
            C("Kanser insidansı — Türkiye 2022 (s.10)", [
                B("2022'de **yaşa standardize kanser hızı**: **erkeklerde yüz binde 258,4**, **kadınlarda yüz binde 197,4**."),
                B("**Toplam kanser insidansı yüz binde 227,9**; bu yılda toplam **239.997 kişiye** yeni kanser teşhisi konulmuştur."),
                B("**COVID-19** salgını nedeniyle **2020-2021** yıllarında genel kanser insidansları önceki yıllara göre **daha düşük**."),
                B("Tanıların büyük ölçüde **sağlık hizmetlerine başvurmama** nedeniyle düştüğü düşünülmektedir.", lvl=1),
                B("**Çocukluk çağı kanserlerinde** COVID döneminde **düşüş görülmemiştir**."),
            ]),
            C("Türkiye ve dünya karşılaştırması (s.11)", [
                B("Türkiye'de kanser görülme sıklığı hem erkeklerde hem kadınlarda **Avrupa, Kanada, Amerika ve Avustralya**'ya göre **daha düşüktür**."),
                B("Dünyada **kadınlarda** (158 ülke genelinde) **meme kanseri birinci sırada**; **Afrika'nın bazı bölgelerinde serviks kanseri** ilk sıraya geçer."),
                B("**Erkeklerde** Kuzey-Güney Amerika, Batı Avrupa ve Avustralya'da **prostat kanseri** birinci; **Türkiye'nin de yer aldığı Asya ve Doğu Avrupa**'da "
                  "**akciğer kanseri** ilk sırada.", y="23-24"),
            ]),
            C("Akciğer kanseri — Türkiye (s.12)", [
                B("Başta **akciğer kanseri** olmak üzere **sigara ile ilişkili kanser insidansları özellikle erkeklerde yüksek** düzeyde devam etmektedir."),
                B("**Kadınlarda akciğer kanseri insidansında artış** gözlenmektedir."),
                B("2022'de **34.610 kişiye** akciğer kanseri tanısı; tanı sırasında **%51,7'si uzak metastaz** yapmış."),
                B("Tanı alma **medyan yaşı 66**."),
            ]),
            C("Meme kanseri — Türkiye (s.13)", [
                B("**Meme kanseri, kadınlarda en sık görülen kanser türüdür**; tanı konulan **yaklaşık her üç kadın kanserinden biri** meme kanseridir.", y="23-24"),
                B("Bir yılda **32.021 kadına** meme kanseri tanısı; vakaların **%45,9'u lokalize evrede** tanı almıştır."),
                B("Tanı alma **medyan yaşı 54**."),
            ]),
            C("Kolorektal kanser — Türkiye (s.13)", [
                B("**Kolorektal kanserler hem kadınlarda hem erkeklerde üçüncü sıradaki** önemini korumaktadır."),
                B("Sıklık: **erkeklerde yüz binde 25,7**, **kadınlarda yüz binde 15,1**."),
                B("Bir yılda **21.902 kişiye** kolorektal kanser teşhisi; tanı alma **medyan yaşı 65**."),
            ]),
        ],
        [
            C("Erkek — en sık 10 kanser, 2022 (s.14; yaşa standardize hız /100.000)", [
                B("1- **Trakea-bronş-akciğer 53,4** · 2- **Prostat 39,2** · 3- **Kolorektal 25,7** · 4- **Mesane 21,2** · 5- **Mide 12,9**",
                  y="23-24", tuzak="“Erkekte en sık görülen kanser prostat / mide” → YANLIŞ"),
                B("6- Böbrek 7,3 · 7- Tiroid 6,3 · 8- Non-Hodgkin lenfoma 6,3 · 9- Pankreas 6,2 · 10- Beyin-sinir sistemi 5,7", lvl=1),
            ]),
            C("Kadın — en sık 10 kanser, 2022 (s.14; yaşa standardize hız /100.000)", [
                B("1- **Meme 57,5** · 2- **Tiroid 20,1** · 3- **Kolorektal 15,1** · 4- **Trakea-bronş-akciğer 12,4** · 5- **Uterus korpusu 10,4**",
                  y="23-24", tuzak="“Kadında en sık görülen kanser over / tiroid / kolorektal” → YANLIŞ"),
                B("6- Over 6,8 · 7- Mide 6,4 · 8- Beyin-sinir sistemi 4,5 · 9- Non-Hodgkin lenfoma 4,5 · 10- Uterus serviksi 4,2", lvl=1),
            ]),
            C("Tüm yaş grupları — yüzde dağılım (s.15; T.C. Sağlık Bakanlığı veri tabanı, 2022)", [
                B("**İlk 5 sıra hız (s.14) ve yüzde (s.15) grafiklerinde aynıdır**; kolorektal her iki cinste 3. sırada."),
                B("**Erkek**: **Akciğer %22,7** · **Prostat %16,5** · **Kolorektal %11,0** · **Mesane %9,1** · **Mide %5,5** · Böbrek 3,2 · Tiroid 2,8 · "
                  "Pankreas 2,6 · Non-Hodgkin lenfoma 2,6 · Larinks 2,3"),
                B("**Kadın**: **Meme %31,4** · **Tiroid %10,4** · **Kolorektal %8,7** · **Akciğer %7,0** · **Uterus korpusu %5,7** · Mide 3,7 · Over 3,6 · "
                  "Pankreas 2,4 · Non-Hodgkin lenfoma 2,4 · Uterus serviksi 2,3"),
            ]),
        ],
        [
            C("HPV ile ilişkili kanserler (s.30)", [
                B("Başlıca etkeni **HPV** olan **uterus serviks kanseri** ülkemizde **düşük sıklıkta** görülür."),
                B("Uluslararası Kanser Ajansı analizi: **HPV'ye bağlı kanserler erkek kanserlerinin %1'inden, kadın kanserlerinin %5-10'undan** sorumludur."),
                B("Ülkemizde HPV ilişkili kanserler **kadınları daha çok** etkiler; kadınlarda **erkeklerin yaklaşık 5 katı** HPV ilişkili kanser olduğu tahmin edilir."),
            ]),
            C("Obezite ile ilişkili kanserler (s.31)", [
                B("**Meme, uterus korpusu ve over** gibi kadın kanserlerinde en önemli risk faktörlerinden biri **obezite**dir."),
                B("Obezitenin etken olduğu kanserler **daha çok kadınları** etkiler → obezite ilişkili kanserlerde **hız kadınlarda erkeklere göre yüksek**."),
            ]),
            C("Metinsiz grafik/tablo slaytları (s.16-29)", [
                B("**s.16** çocukluk çağı (0-14 yaş) kanserleri, yüzde · **s.17-22** yaş gruplarına göre en sık kanserler (0-19, 15-19, 15-24, 25-49, 50-69, 70+ yaş)."),
                B("**s.23-24** meme ve toraks kanserlerinin **histolojik tip dağılımı** · **s.25** bazı kanserlerin **evre dağılımı**."),
                B("**s.26-27** erkek/kadında en sık kanser türlerinin **dünya haritası** · **s.28-29** Türkiye ve bölgelere göre **ilk beş kanser** tabloları."),
                B("Sayılar yalnız grafikte; bu modülde sadece s.14-15 verileri yazıldı."),
            ]),
        ],
        [
            C("Kanserin epidemiyolojik özellikleri — 12 başlık (s.32)", [
                B("Kanserler epidemiyolojik açıdan **coğrafi dağılım, cinsiyet, yaş, sosyoekonomik durum ve meslek** özellikleri gösterir."),
                B("Slayt sırasıyla: 1- **Coğrafi ve çevresel faktörler** · 2- **Cinsiyet** · 3- **Yaş** · 4- **Sosyoekonomik durum** · 5- **Meslek** · 6- **Sigara**"),
                B("7- **Beslenme alışkanlıkları ve şişmanlık** · 8- **Enfeksiyonlar** · 9- **İyonize radyasyon** · 10- **UV ışınlar** · "
                  "11- **Cinsel ve üreme sağlığı etmenleri** · 12- **Herediter**", lvl=1),
            ]),
            C("1- Coğrafi ve çevresel faktörler (s.32-33)", [
                B("Kanser sıklığı **bölgelere, ülkelere, hatta aynı ülkenin farklı yerleşim yerlerine** göre değişir; kanser türleri de farklı sıklıkta görülür."),
                B("Nedeninin **kalıtım ya da çevresel risk etmenleri** olabileceği düşünülmektedir.", lvl=1),
                B("**Burkitt lenfoma → Afrika** · **ağız boşluğu kanserleri → Hindistan** · **mide kanseri → Japonya**"),
                B("**Kolon kanseri → Kuzey Avrupa ülkeleri** · **meme kanseri → genel olarak gelişmiş ülkeler** · **serviks kanseri → gelişmekte olan ülkeler**"),
            ]),
            C("2- Cinsiyet (s.34)", [
                B("**Kanser sıklığı ve türleri cinsiyete göre farklılıklar** gösterir."),
            ]),
            C("3- Yaş (s.35)", [
                B("**Ortalama yaşın 50 üzerinde** olduğu toplumlarda kanser daha sık görülür; gençlerde de kanser görülür."),
                B("Türkiye'de tüm kanserlerde yaş dağılımı **gelişmekte olan ülkelerdeki dağılıma** uymaktadır."),
                B("Yaşla artan sıklık **somatik mutasyon birikimi** ile olur; **yaşlanmayla azalan immünite** de etkilidir."),
                B("**Mortalitenin çoğu 55-75 yaşları** arasında olur."),
                B("**15 yaş altı çocuklardaki ölümlerin %10'undan fazlasının** nedeni kanserdir."),
            ]),
        ],
        [
            C("Yaşlara göre kanserlerin dağılımı (s.36)", [
                B("**0-5 yaş** sık malign tümörler: **akut lenfoblastik lösemi, Wilms tümörü, retinoblastom, nöroblastom, testisin yolk sak tümörü, rabdomyosarkom**."),
                B("**6-15 yaş** sık tümörler: **osteosarkom, Ewing sarkomu, PNET, medulloblastom**."),
                B("**25-40 yaş** sık tümörler: **testis tümörleri** (seminom, teratokarsinom)."),
                B("**Bifazik yaş dağılımı** gösteren tümörler: **Hodgkin hastalığı ve nazofarinks tümörleri**."),
            ]),
            C("4- Sosyoekonomik durum (s.37)", [
                B("Sosyoekonomik durumu düşük kişilerde **kanserin temel riskleri daha fazla**; bu kişiler **sağlık hizmetlerine en az ulaşan grup**."),
                B("Bu kişilerde daha fazla: **sigara, alkol kullanımı, yağlı beslenme, mesleksel karsinojenlere maruziyet, cinsel yolla bulaşan hastalıklar ve enfeksiyonlar**."),
                B("**Koruma, erken tanı ve tedavi** hizmetlerine daha az ulaşırlar → **yaşam süresi az, yaşam kalitesi düşük**."),
            ]),
            C("5- Meslek (s.38)", [
                B("Mesleğin etkisi ilk kez **1775'te Sir Percivall Pott** tarafından **baca temizleyiciliği - skrotum kanseri** ilişkisinden ortaya atıldı."),
                B("150 yıl sonra bu kansere yol açan kimyasal etmen **katran; 1-2 dibenz antrasen** **ilk kimyasal karsinojen** olarak tanımlandı."),
                B("**Radyoaktif maddelerin** kanser yapıcı özelliği ilk kez **radyumla saat boyayan işçilerde kemik kanserinin** sık görülmesiyle ortaya kondu."),
                B("**Maden işçilerinde akciğer kanseri** → maden ocaklarındaki **radyoaktif madde** ile ilişkili."),
                B("**Benzen lösemiye neden olur.**"),
            ]),
        ],
        [
            C("6- Sigara (s.40)", [
                B("Sigaranın neden olduğu başlıca kanserler: **akciğer, oral kavite, larinks, özefagus ve mide**."),
                B("Gelişmiş ülkelerde sigara **tüm kanserlerde %30 ölüm nedeni**; **akciğer kanseri ölümlerinin %80-90'ı** sigaraya bağlı."),
                B("Sigara içenlerde kanserden ölüm oranı içmeyenlere göre **15-25 kat fazla**."),
                B("**İçilen sigara yılı** ve **günlük içilen sigara miktarı** arttıkça kanser riski artar."),
                B("**Sigarayı bırakma yaşı ne kadar erkense** ileri yaşta akciğer kanseri riski o kadar azalır."),
            ]),
            C("7- Beslenme alışkanlıkları ve şişmanlık (s.41)", [
                B("Beslenme alışkanlıkları ve şişmanlık tüm kanserlerin **gelişmiş ülkelerde %30'unun, gelişmekte olan ülkelerde %20'sinin** nedeni."),
                B("**Şişmanlık**: özefagus, kolorektum, meme, endometrium, böbrek kanserlerinde."),
                B("**Alkol**: oral kavite, farinks, larinks, özefagus, karaciğer, meme kanserlerinde."),
                B("**Aflatoksin** gibi bazı mikotoksinler: **karaciğer kanserinde kesin riski artıran** etmen."),
            ]),
            C("8- Enfeksiyonlar (s.42)", [
                B("Enfeksiyonlar **dünyadaki kanserlerin %15'inden** sorumludur."),
                B("**Hepatit B, C** → karaciğer kanseri · **HPV** → serviks kanseri · **H. pylori** → mide kanseri"),
                B("**Epstein-Barr virüsü** → Burkitt lenfoma, nazofaringeal karsinom"),
                B("**HIV** → Kaposi sarkomu, non-Hodgkin lenfoma · **Şistozomiyazis** → kolanjiokarsinom, mesane kanseri"),
            ]),
        ],
        [
            C("9- İyonize radyasyon (s.43)", [
                B("Başlıca kaynaklar: **elektrik üretimine yönelik nükleer güç santralleri**; **radyografi ve radyoskopi cihazları**; "
                  "**radyoaktif madde ihtiva eden analiz cihazları**."),
                B("Eğitim-araştırma laboratuvarlarında kullanılan **açık ve kapalı radyoizotoplar**.", lvl=1),
                B("Tıpta teşhis ve tedavi amaçlı **radyoloji ve radyoterapi cihazları**.", lvl=1),
                B("**Nükleer tıp ve radyoimmünoassay** laboratuvarlarında kullanılan açık ve kapalı radyoaktif maddeler.", lvl=1),
                B("İyonize radyasyonla ortaya çıkan maligniteler **en sık: lösemi, tiroid kanseri, meme, kolon ve karaciğer kanseri**."),
            ]),
            C("10- UV ışınlar (s.44)", [
                B("**UVB ve UVC**: DNA yapısında **mutasyon, hücre yıkımı ve transformasyon**; tümör baskılayıcı gen **p53** mutasyonu."),
                B("UV ışınları **Langerhans hücre işlevlerini bozarak** bağışıklık sistemini baskılar."),
                B("Güneş ışınlarının çok yoğun olduğu bölgelerde yaşayanlarda **bazal ve skuamöz hücreli karsinom** daha fazla."),
            ]),
            C("11- Cinsel ve üreme sağlığı etmenleri (s.45)", [
                B("Üreme sağlığına ilişkin bazı özellikler kanser için önemli risk etmenidir."),
                B("**Hiç doğum yapmamış kadınlarda meme, endometrium ve over kanseri sık**; bu türler **doğurganlığın düşük olduğu Avrupa ülkelerinde** daha fazla."),
                B("**Erken cinsel ilişki ve çok sayıda cinsel eş** → **serviks kanseri** risk etmeni."),
            ]),
        ],
        [
            C("12- Herediter kanserler — 3 kategori (s.46)", [
                B("Herediter kanserler **soya geçiş tipine göre üç kategoriye** ayrılır."),
                B("**A- OD kanser sendromları**: **tek mutant genle** nakledilen tümörler; **retinoblastomların %40'ı aileseldir** (tümör supresör gen mutasyonu)."),
                B("**B- OR geçen kusurlu onarım sendromları**: **Xeroderma pigmentosum**."),
                B("**C- Kalıtım şekli bilinmeyen ailesel kanserler** (slayttaki örnek: **ailesel kolon kanseri**)."),
                B("Özellikleri: **genç yaşta çıkması** · **indeks vakaların en az iki yakın akrabada görülmesi** · bazen tümörün **çok sayıda veya iki taraflı** olması.", lvl=1),
            ]),
            C("Malignite oluşumu ile ilgili genler — 4 grup (s.48)", [
                B("1- **Protoonkogenler** (büyümeyi düzenler) · 2- **Tümör supresör genler** (antionkogen genler)"),
                B("3- **Apoptozisi regüle eden genler** · 4- **DNA tamirinden sorumlu genler**"),
            ]),
            C("1- Protoonkogenlerin yapı ve regülasyonunda bozukluklar (s.49)", [
                B("**A- Nokta mutasyonlar**: özellikle **Ras geninde**."),
                B("**B- Kromozomal translokasyonlar**: **c-myc geni t(8;14) → Burkitt lenfoma** · **Bcl-2 gen ekspresyonu t(14;18) → foliküler B hücreli lenfoma**."),
            ]),
            C("2- Tümör supresör genler (s.50)", [
                B("Normalde **hücre büyümesinde görev** alırlar; **mutasyonlarında tümör oluşur**."),
                B("**En sık rastlanan tümör supresör gen: p53**."),
                B("**p53**: hücre büyümesini durdurma · DNA onarımı · apoptozis · tümör anjiogenezis inhibisyonu."),
            ]),
            C("3- Apoptozla ilgili genler (s.52)", [
                B("Bu genlerin **inhibisyonu malignite oluşumuna** neden olur."),
                B("**BAX, BAK, BAD, BID, BIM** apoptozisi **artırır**; **BCL-2 antiapoptotik** özellik gösterir."),
            ]),
        ],
        [
            C("4- DNA onarım genleri (s.53)", [
                B("**A- Herediter nonpolipozis kolon karsinomu sendromu**: **OD**; **daha erken yaşta** ortaya çıkar, **sağ kolon yerleşimli**; "
                  "DNA onarım genleri **MLH1, MSH2, MSH6, PMS2**."),
                B("**Mide, beyin, ince bağırsak, pankreas ve deri kanserleri** eşlik eder.", lvl=1),
                B("**B- Xeroderma pigmentosum**: **OR** → **deri kanserleri**"),
                B("**C- Bloom sendromu** · **D- Ataksi telenjiektazi** · **E- Fanconi anemisi**: üçü de **OR** → **lösemi, lenfoma**"),
            ]),
            C("Edinsel preneoplastik bozukluklar (s.54)", [
                B("Malign neoplazi gelişiminde **genetik etkilere ek olarak predispoze ve preneoplastik bozukluklar** da etkilidir."),
                B("**Persistan rejeneratif hücre replikasyonu**:"),
                B("Kronik deri fistülü kenarı, uzun süre iyileşmeyen deri yaraları → **yassı hücreli ca**", lvl=1),
                B("Karaciğer sirozu → **hepatoselüler ca**", lvl=1),
                B("**Hiperplastik ve displastik proliferasyonlar**:"),
                B("Atipik endometrial hiperplazi → **endometrial ca**", lvl=1),
                B("Sigara içenlerin displazik bronş mukozası → **akciğer adenoca**", lvl=1),
            ]),
            C("Preneoplastik bozukluk → artmış kanser riski (s.55)", [
                B("**Kronik atrofik gastrit**, **pernisiyöz anemi** → **mide ca**"),
                B("**Kronik ülseratif kolit** → **kolorektal karsinomlar**"),
                B("**Lökoplaki** (ağız boşluğu, vulva veya penis) → **yassı hücreli ca** riskinde artma", y="22-23",
                  tuzak="“Ağız boşluğunda yassı hücreli ca zemini: Hashimoto / endometrial hiperplazi / karaciğer sirozu / Graves” → YANLIŞ"),
                B("**Kolonda villöz adenom** → **kolorektal ca**"),
                B("**Solar keratoz** → **yassı hücreli karsinom**"),
                B("**Kemiğin Paget hastalığı** → **osteosarkom**"),
                B("**Hashimoto, Graves hastalığı** → **papiller tiroid karsinomu**"),
                B("**Gonadal disgenezis** → **germ hücreli tümörler**"),
            ]),
        ],
        [
            C("Kanserden koruma — 3 düzey (s.56-57)", [
                B("**Birincil koruma**: hastalığın ortaya çıkışını önlemek için **risklerden kaçınma**; etkenle ilgili önlemlere ek olarak **kişilerin sağlık bilincinin geliştirilmesi** gerekir."),
                B("**İkincil koruma**: kanserin **erken teşhisi ve etkili tedavisi**; erken tanı-tedavi olanaklarının geliştirilmesi ile birlikte **sağlık kurumlarının ulaşılabilirliği** önemli."),
                B("**Üçüncül koruma**: **tedavi sonrası komplikasyonların azaltılması**, **tıbbi ve sosyal rehabilitasyon**."),
            ]),
            C("Erken tanı ve tarama (s.57)", [
                B("**Prekanseröz/premalign dönemin bulunması** ve erken (lokalize) dönemde **%75'inin kolaylıkla tanınabilir** olması kanserin erken tanınmasına olanak sağlar."),
                B("**Erken tanı alan kanserin prognozu daha iyi**, tedavi şansı daha yüksektir."),
                B("**Asemptomatik kişilerde taranması önerilen kanserler**: **meme, serviks, kolon-rektum, prostat, deri**."),
                B("Uygulamada **en çok meme ve serviks** kanserine ilişkin taramalar yapılır."),
                B("**Yüksek riskli kişilerde** **over, endometrium, akciğer** kanseri taramaları önerilir."),
            ]),
        ],
    ],
    sorular=[
        Q("23-24", 69, "Türkiye birleşik veri tabanına göre erkek ve kadınlarda en sık görülen kanserler?",
          "Erkekte akciğer, kadında meme kanseri",
          "Çeldiriciler: erkekte prostat (2.) / mide (5.) · kadında over (6.) / tiroid (2.) / kolorektal (3.) — ilk sırada değil"),
        Q("22-23", 69, "Preneoplastik bozukluklardan hangisi ağız boşluğunda yassı hücreli karsinom gelişiminde rol oynar?",
          "Lökoplaki",
          "Çeldiriciler başka kanserin zemini: Hashimoto/Graves → papiller tiroid ca · endometrial hiperplazi → endometrial ca · siroz → hepatoselüler ca"),
    ],
)
