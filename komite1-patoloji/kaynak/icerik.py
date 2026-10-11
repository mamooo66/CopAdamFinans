# -*- coding: utf-8 -*-
"""Komite 1 Patoloji hap bilgi slaytlarının içeriği (Bölüm 1-10).

Yazım kuralları
  B(metin, y="23-24 25-26", tuzak="...", g="İÇ HAST. 23-24", lvl=1)
      y     : patoloji sorusu olarak çıktığı yıllar (kırmızı ÇIKMIŞ etiketi)
      tuzak : sınavda bu bilgi yanlış ifade (çeldirici) olarak sorulduysa o ifade
      g     : başka bir ders (İç Hast., Pediatri, Biyokimya, Enfeksiyon) sorusunda geçmişse gri etiket
  C(başlık, [B...])          bir kart
  Q(yıl, soru_no, kök, cevap, not)   çıkmış soru özeti
Metin içinde **kalın** kullanılabilir.
"""

YILLAR = ["21-22", "22-23", "23-24", "24-25", "25-26"]


def B(t, y=None, tuzak=None, g=None, lvl=0):
    return dict(t=t, y=(y.split() if y else []), tuzak=tuzak, g=g, lvl=lvl)


def C(baslik, maddeler, ikon=None):
    return dict(baslik=baslik, maddeler=maddeler, ikon=ikon)


def Q(y, no, kok, cevap, not_=None, n=1, ref=False):
    """n: kaç soruyu temsil ettiği (hatırlanan birleşik maddeler için); ref: sayıma girmeyen çapraz atıf"""
    return dict(y=y, no=no, kok=kok, cevap=cevap, not_=not_, n=n, ref=ref)


BOLUMLER = []

# ---------------------------------------------------------------- 1
BOLUMLER.append(dict(
    no=1, key="giris", baslik="Patolojiye Giriş", yeni=True,
    hoca="Doç. Dr. Selma Erdoğan Düzcü", tarih="21 Eylül (ilk ders)", saat="—",
    kaynak="2026-27 YENİ klasör: 1-PATOLOJİYE GİRİŞ (S. E. Düzcü)",
    ozet=["Son 5 yılda bu başlıktan doğrudan soru yok — ama boya/IHK bilgisi diğer konularda karşına çıkıyor (Kongo red ×5, CD38, CD30).",
          "Yeni (2026-27) klasördeki tek PDF bu ders: sayısal bilgileri (süreler, yüzdeler) ezberle."],
    slaytlar=[
        [
            C("Tanım ve kapsam", [
                B("Patoloji = **hastalık bilimi**; kapsamı: **tanı, etiyoloji, patogenez**."),
                B("İki kol: **genel patoloji** ve **sistemik (özel) patoloji**; temel bilimlerle klinik arasında köprü."),
            ]),
            C("Patoloji laboratuvarına gelen 4 materyal", [
                B("**Biyopsi** (eksizyonel / insizyonel)"),
                B("**Cerrahi girişimle** çıkarılan doku ve organlar"),
                B("**Otopsi** doku örnekleri"),
                B("**Yayma (sitolojik) preparatlar**"),
            ]),
            C("Fiksasyon ve saklama süreleri", [
                B("Doku → **%10'luk formalin**; sitolojik materyal → **%96'lık alkol**."),
                B("Fiksasyon süresi **en az 4 saat**; doku takibi normalde **12-14 saat**."),
                B("Saklama: **bloklar ≥20 yıl**, **lamlar ≥10 yıl**, **raporlar süresiz**."),
            ]),
            C("Doku takibi (sıra)", [
                B("**Fiksasyon** (formalin) → **dehidratasyon** (en sık **alkol**) → **şeffaflandırma** (alkolü temizler; en sık **ksilen**) → **infiltrasyon/sertleştirme** (**parafin**)"),
                B("→ **blok hazırlama (gömme)** → **kesit** (mikrotom) → **deparafinizasyon** → **boyama** (rutin boya **H&E**)."),
            ]),
        ],
        [
            C("Boyalar", [
                B("Rutin: **Hematoksilen-Eozin (H&E)**, **May-Grünwald Giemsa**, **Papanicolaou** (sitoloji)."),
                B("Histokimyasal (özel) boyalar: glikojen-musin → **PAS, Alcian blue**; kollajen → **Masson trikrom**; **retikülin**, **elastin**, **yağ**, **pigment-mineral** boyaları."),
                B("**Giemsa** → midede **Helicobacter pylori** gösterilir."),
                B("Amiloid → **Kongo red** (polarize ışıkta elma yeşili) — bkz. Amiloidoz", y="21-22 22-23 23-24 24-25 25-26"),
            ]),
            C("İmmünohistokimya (IHK)", [
                B("Dokuda **spesifik antijen** gösterilerek **tümörün kökeni** saptanır; **parafin bloklarda** çalışılabilir."),
                B("Epitel: **keratin, EMA** · Mezenkim: **vimentin** · Kas: **desmin, aktin, miyoglobin**"),
                B("Damar: **faktör VIII-Ag, CD31** · Nöral: **S-100, NSE, GFAP** · Histiosit: **CD68**, S-100"),
                B("Lökosit: **LCA (CD45)**, T ve B lenfosit antijenleri (CD3, CD20…)."),
            ]),
            C("İmmünofloresan ve enzim histokimya", [
                B("**İmmünofloresan**: **taze-dondurulmuş doku**, morfolojik detay yok → **deri ve böbreğin immünolojik hastalıklarının** ayırıcı tanısı."),
                B("**Enzim histokimya**: taze-dondurulmuş dokuda oksidatif/hidrolitik enzimler → **kas biyopsileri** ve **lösemilerin sınıflandırılması**."),
            ]),
        ],
        [
            C("Sitoloji", [
                B("**Eksfoliyatif**: boşluklu organlara dökülen hücreler — idrar, BOS, periton sıvısı (**parasentez**), vajinal yayma, balgam."),
                B("**Abraziv**: abeslang/fırça ile alınan hücreler; **yıkama örnekleri de abraziv** gruptadır."),
                B("**Aspirasyon**: solid organ/lezyonlardan **ince iğne aspirasyon (İİAB)** sitolojisi."),
                B("Fiksasyon: lama yayılmışsa **%96 etil alkol** veya sprey; gecikecek sıvıya **eşit hacim %50 alkol** (daha derişik alkol hücreyi büzer); İİAB yaymaları **havada kurutularak** da fikse edilir."),
            ]),
            C("Frozen (dondurma kesit) tanı", [
                B("Taze doku kriyostatta dondurulup kesilir, hızlı boyanır; tanı **ortalama 20-30 dk**."),
                B("**Ameliyat sırasında**, tanısı bilinmeyen lezyonda **ameliyatın şeklini belirler**; **cerrahi sınır** kontrolü."),
                B("**Kesin tanı parafin kesitlerde** verilir."),
            ]),
            C("Moleküler patoloji", [
                B("**Hibridizasyon** (FISH, CISH, SISH) · **Amplifikasyon** (PCR) · **Elektroforez**"),
                B("**Sekanslama** (NGS – yeni nesil, Sanger, pyrosekanslama) · **Likit biyopsi**"),
            ]),
            C("Patoloji istem formu", [
                B("Materyalin alınma tarihi, gönderen hekim, hasta adı-adresi-yaşı-cinsi, materyalin alındığı yer ve teknik, **klinik ön tanı**, yakınma/bulgular, tedavi, önceki tanılar."),
                B("Jinekolojik örneklerde ek olarak **son adet tarihi**, adet düzeni, kontraseptif ve gebelik öyküsü."),
            ]),
        ],
    ],
    sorular=[],
))

# ---------------------------------------------------------------- 2
BOLUMLER.append(dict(
    no=2, key="hasar", baslik="Hücre Hasarı ve Hücre Ölümü",
    hoca="Doç. Dr. Selma Erdoğan Düzcü", tarih="21 Eylül", saat="2 saat",
    kaynak="2025-26 ders notları (S. E. Düzcü) + Robbins Temel Patoloji",
    ozet=["Her yıl 1 soru: “doğru olan hangisi?” tipinde nekroz–apoptoz–mekanizma karışımı.",
          "Çeldiriciler hep aynı: apoptoz reversibl/yalnız patolojik, nekrozda membran intakt, ATP↑/Ca↓, böbrekte likefaksiyon."],
    slaytlar=[
        [
            C("Nedenler", [
                B("**Hipoksi** (O₂ yetersizliği) — **en sık nedeni iskemi** (kan akımı kaybı)."),
                B("Hipokside **HIF-1α** aktive olur (glikoliz ve VEGF genleri ↑).", y="21-22"),
                B("Fiziksel ajanlar, kimyasal ajan/ilaçlar, enfeksiyonlar, **immünolojik reaksiyonlar** (otoimmünite, anafilaksi), genetik bozukluklar, beslenme dengesizlikleri, **yaşlanma** (serbest radikal ↑)."),
                B("Hasara yanıt; hasarın tipi-süresi-şiddeti ile hücrenin tipi, durumu ve genetik yapısına bağlıdır → **kişiden kişiye farklıdır**.", y="24-25",
                  tuzak="“Hücre hasarı kişiler arasında farklılık göstermez” → YANLIŞ"),
            ]),
            C("ATP azalmasının sonuçları", [
                B("**Na⁺-K⁺ pompası** bozulur → hücreye Na⁺ ve su girer → **akut hücresel şişme**, ER genişler."),
                B("**Anaerobik glikoliz ↑** → **glikojen depoları AZALIR**, laktik asit ↑ → pH ↓ → **kromatin kümelenmesi**.", y="24-25",
                  tuzak="“Hücre içi glikojen depoları artar” → YANLIŞ"),
                B("**ATP bağımlı Ca²⁺ pompaları** yetersiz → **hücre içi Ca²⁺ ARTAR**.", y="24-25 25-26",
                  tuzak="“Hücre hasarında ATP artar, hücre içi Ca azalır” → YANLIŞ"),
                B("Ribozomlar ayrılır → protein sentezi ↓; yanlış katlanmış protein → **UPR/ER stresi** → apoptoz."),
            ]),
            C("Mitokondri hasarı ve serbest radikaller", [
                B("**Mitokondri hasarı → ATP ↓ ve reaktif oksijen türevleri (ROS) ↑**; mitokondriyal geçirgenlik ↑ → **sitokrom c** salınımı → apoptoz.", y="24-25"),
                B("Hücre içi Ca²⁺ ↑ → fosfolipaz, proteaz, endonükleaz, ATPaz ve **kaspazlar** aktive olur."),
                B("Serbest radikal: dış orbitalde **eşleşmemiş tek elektron**. Hasar: **membran lipid peroksidasyonu**, protein çapraz bağlanması (disülfid), **DNA tek zincir kırıkları**.",
                  g="BİYOKİMYA 22-23 · 23-24 · 25-26"),
                B("Uzaklaştırma: **SOD, katalaz, glutatyon peroksidaz**; antioksidanlar (vit. E, A, C, β-karoten)."),
                B("**İskemi-reperfüzyon hasarı**: kan akımı geri gelince ROS ↑, Ca²⁺ yüklenmesi, inflamasyon, kompleman aktivasyonu."),
            ]),
        ],
        [
            C("Reversibl ↔ İrreversibl hasar", [
                B("Reversibl: **hücresel şişme** (hidropik/vakuoler dejenerasyon — **en erken ve en sık**) ve **yağlı değişiklik** (karaciğer, kalp).", y="23-24",
                  tuzak="“Hücresel şişme ve yağlı değişiklik irreversibl hasardır” → YANLIŞ"),
                B("Reversibl ultrastrüktür: ER genişlemesi, ribozom ayrılması, mitokondri şişmesi, membran blebleri, miyelin figürleri."),
                B("İrreversibilitenin 2 göstergesi: **mitokondri fonksiyonunun geri dönmemesi** (ATP üretilemez) + **plazma ve lizozom membranlarında ciddi hasar**."),
                B("Değişiklik sırası: **biyokimyasal → ultrastrüktürel → ışık mikroskobik → EN SON makroskopik** (ölümden saatler sonra).", y="24-25",
                  tuzak="“İrreversibl zedelenmede ilk olarak makroskopik değişiklikler görülür” → YANLIŞ"),
            ]),
            C("Nekroz", [
                B("**Membran bütünlüğü bozulur** → hücre içeriği/enzimler sızar → **inflamasyon** gelişir.", y="22-23 25-26",
                  tuzak="“Nekrozda membran intakt kaldığından inflamasyon gelişmez” → YANLIŞ"),
                B("Her zaman **patolojiktir** (programlanmış/fizyolojik DEĞİL).", y="22-23 23-24",
                  tuzak="“Nekroz programlanmış hücre ölümüdür, fizyolojik olabilir” → YANLIŞ"),
                B("Sitoplazma: **eozinofili ↑**; nükleus: **piknoz** (büzülme-koyulaşma) → **karyoreksis** (parçalanma) → **karyolizis** (silinme).", y="21-22"),
            ]),
            C("Nekroz paternleri", [
                B("**Koagülasyon**: doku iskeleti korunur — **beyin hariç solid organ iskemisi** (**böbrek**, kalp, dalak).", y="25-26 23-24",
                  tuzak="“Böbrekte iskemi sonrası nekroz likefaksiyon tipindedir” → YANLIŞ"),
                B("**Likefaksiyon**: **beyinde iskemi**, bakteriyel/fungal enfeksiyon (abse, pü)."),
                B("**Kazeifikasyon**: peynirimsi — **tüberküloz** (granülom merkezi)."),
                B("**Yağ nekrozu**: **akut pankreatit** (lipaz) → yağ asidi + Ca = sabunlaşma, **tebeşir beyazı** odaklar."),
                B("**Fibrinoid**: antijen-antikor kompleksi + fibrin **arter duvarında** (vaskülit)."),
                B("**Gangrenöz**: klinik terim; ekstremite (kuru = koagülasyon, ıslak = + enfeksiyon/likefaksiyon)."),
            ]),
        ],
        [
            C("Apoptoz", [
                B("**Programlanmış** hücre ölümü; **fizyolojik VEYA patolojik** olabilir.", y="22-23 25-26",
                  tuzak="“Apoptozis yalnızca patolojik olaylarda meydana gelir” → YANLIŞ"),
                B("**Membran intakt**, hücre küçülür, kromatin yoğunlaşır, **apoptotik cisimler** fagosite edilir → **iltihabi reaksiyon YOK**.", y="23-24 22-23",
                  tuzak="“Apoptozda membran bozulur / yoğun inflamasyon / enzimler hücre dışına çıkar” → YANLIŞ"),
                B("Apoptoz **irreversibl** hücre ölümüdür (reversibl hasar değil).", y="25-26",
                  tuzak="“Apoptozis reversibl hücre hasarıdır” → YANLIŞ"),
                B("Fizyolojik: embriyogenez, hormon çekilmesi (endometrium), timusta otoreaktif T hücre delesyonu, inflamasyon sonrası nötrofil. Patolojik: DNA hasarı, yanlış katlanmış protein, viral enfeksiyon, kanal tıkanması."),
            ]),
            C("Apoptoz yolları", [
                B("**İntrinsik (mitokondriyal)**: BCL-2 ailesi dengesi — **BAX/BAK** (pro) ↔ **BCL-2/BCL-XL** (anti); BH3-only proteinler (BAD, BID, PUMA) → sitokrom c → **APAF-1** → **kaspaz-9**."),
                B("**Ekstrinsik (ölüm reseptörü)**: **Fas–FasL**, TNF reseptörü → FADD → **kaspaz-8**."),
                B("Ortak son yol: yürütücü **kaspaz-3** (DNA fragmantasyonu, sitoskeleton yıkımı)."),
            ]),
            C("Diğer ölüm yolları / otofaji", [
                B("**Nekroptoz** (RIPK1/RIPK3), **piroptoz** (inflammazom–kaspaz-1–IL-1), **ferroptoz** (demir bağımlı lipid peroksidasyonu)."),
                B("**Otofaji**: hücrenin kendi içeriğini lizozoma taşıyıp yıkması — açlık, atrofi."),
                B("Hücresel stres yanıtları: **entegre stres yanıtı (ISR)**, **katlanmamış protein yanıtı (UPR)**."),
            ]),
        ],
    ],
    sorular=[
        Q("25-26", 67, "Hücre hasarıyla ilgili doğru olan?",
          "Böbrekte kan akımının ani kesilmesi → koagülasyon nekrozu",
          "Çeldiriciler: ATP↑/Ca↓ · apoptoz reversibl · apoptoz yalnız patolojik · nekrozda membran intakt"),
        Q("24-25", 69, "Hücre hasarlanma mekanizmalarıyla ilgili doğru olan?",
          "Mitokondri hasarıyla reaktif oksijen türevleri artar",
          "Çeldiriciler: kişiler arası farklılık yok · ilk makroskopik değişiklik · glikojen artar · hücre içi Ca azalır"),
        Q("23-24", 61, "Hücre hasarı mekanizmalarıyla ilgili doğru olan?",
          "Apoptozda hücre membranı intakt kalır ve iltihabi reaksiyon gelişmez",
          "Çeldiriciler: yalnızca enfeksiyon · şişme/yağlı değişiklik irreversibl · nekroz programlı · böbrekte likefaksiyon"),
        Q("22-23", 60, "Nekroz ve apoptozla ilgili doğru olan?",
          "Nekrozda hücre membran bütünlüğü bozulmuştur",
          "Çeldiriciler: nekroz fizyolojik olabilir · apoptozda membran bozuk · apoptozda yoğun inflamasyon · apoptozda enzimler dışarı çıkar"),
        Q("21-22", None, "Nekroz–apoptoz karşılaştırması (nükleer değişiklikler)",
          "Piknoz → karyoreksis → karyolizis (nekroz)", "Öğrenci hatırlamasından derlenmiş soru"),
    ],
))

# ---------------------------------------------------------------- 3
BOLUMLER.append(dict(
    no=3, key="adaptasyon", baslik="Hücresel Adaptasyon ve Hücre İçi Birikimler",
    hoca="Dr. Öğr. Üyesi Nur Tunç Karabekiroğlu", tarih="22 Eylül", saat="1 saat",
    kaynak="2025-26 ders notları + Robbins Temel Patoloji",
    ozet=["4 yıl üst üste soru: hipertrofi / hiperplazi / metaplazi örnekleri ve “prekanseröz mü?”",
          "Barrett = metaplazi · HT'de kalp = hipertrofi (prekanseröz DEĞİL) · östrojen → endometrial hiperplazi (prekanseröz)."],
    slaytlar=[
        [
            C("Hipertrofi — hücre BOYUTU ↑", [
                B("Hücre boyutu artar → organ büyür; **bölünemeyen** hücrelerde (kalp, iskelet kası) tek başına görülür."),
                B("Fizyolojik: **gebe uterus** (hipertrofi + hiperplazi; östrojen), **sporcuda çizgili kas**.", y="24-25",
                  tuzak="Gebe uterus / sporcu kası hipertrofisi prekanseröz DEĞİLDİR"),
                B("Patolojik: **hipertansiyon / aort stenozunda kalp kası (sol ventrikül) hipertrofisi**.", y="22-23 23-24",
                  tuzak="“HT sonucu kalp hipertrofisi prekanserözdür” → YANLIŞ"),
            ]),
            C("Hiperplazi — hücre SAYISI ↑", [
                B("**Bölünebilen** hücrelerde; fizyolojik veya patolojik."),
                B("Fizyolojik hormonal: puberte/gebelikte meme, gebe uterus. Fizyolojik kompansatuvar: **parsiyel hepatektomi sonrası karaciğer**.", y="24-25"),
                B("Patolojik: **yüksek östrojene bağlı endometrium hiperplazisi** → endometrium karsinomu zemini (**prekanseröz**).", y="24-25 23-24"),
                B("Diğer: **BPH** (prostat, androjen), HPV ile deri siğilleri. Uyarı kalkınca hiperplazi geriler ama patolojik hiperplazi kanser için verimli zemindir."),
            ]),
            C("Atrofi — hücre boyutu (± sayısı) ↓", [
                B("Protein sentezi ↓, yıkım ↑ (ubikitin-proteazom); **otofaji ↑** (otofajik vakuoller, **lipofuksin**)."),
                B("Nedenler: kullanılmama, denervasyon, **kan akımı ↓** (en temel), beslenme yetersizliği, endokrin uyarı kaybı (menopoz), basınç, yaşlanma (senil)."),
                B("Fizyolojik: **pubertede timus atrofisi**, doğum sonrası uterus.", y="24-25"),
            ]),
        ],
        [
            C("Metaplazi — bir erişkin hücre tipi yerine başka bir erişkin hücre tipi", [
                B("**Reversibldir**; farklılaşmış hücre dönüşmez → **kök hücreler yeniden programlanır**."),
                B("**Barrett özofagus**: GÖRH → çok katlı yassı epitel yerine **intestinal tip kolumnar epitel** (goblet hücreli) → adenokarsinom riski.", y="25-26 23-24"),
                B("**Sigara**: bronş/**larinks** silyalı epitelinde **yassı (skuamöz) metaplazi** → SCC zemini.", y="23-24"),
                B("**Kronik gastritte intestinal metaplazi** → mide adenokarsinomu zemini.", y="23-24"),
                B("Vit. A eksikliği, taş (safra/tükürük kanalı) → yassı metaplazi. Mezenkimal: en sık **kemik metaplazisi** (myositis ossificans)."),
                B("Etken sürerse: **metaplazi → displazi → karsinom**."),
            ]),
            C("Hücre içi birikimler", [
                B("**Yağlı değişiklik (steatoz)**: en sık **karaciğer** (alkol, obezite/DM, toksin, protein malnütrisyonu); kalp, kas."),
                B("**Kolesterol**: aterosklerotik plak (köpük hücresi), **ksantoma**, **safra kesesi kolesterolozisi**, Niemann-Pick C."),
                B("**Protein**: **Russell cisimleri** (plazma hücresi, Ig), **Mallory-Denk cisimleri** (alkolik karaciğer; keratin ara filamanları), proteinüride tübül damlacıkları."),
                B("**Hiyalin değişiklik** (homojen pembe), **glikojen** (DM, glikojen depo hastalıkları)."),
                B("Pigment: en sık ekzojen **karbon (antrakoz)**; endojen **lipofuksin** (“yıpranma-aşınma”, serbest radikal hasarının izi; yaşlanma/atrofi), **melanin**, **hemosiderin** (Hb türevi, altın sarısı-kahverengi; Prusya mavisi)."),
            ]),
            C("Patolojik kalsifikasyon", [
                B("**Distrofik**: serum Ca **normal**; **ölü/hasarlı dokuda** (nekroz, aterom, hasarlı kapak); **psammom cisimcikleri** (papiller tiroid ca, seröz over ca, meningiom)."),
                B("**Metastatik**: **hiperkalsemi** → **normal dokuda** (böbrek, akciğer, mide, damar). Nedenler: **PTH ↑**, kemik yıkımı (metastaz, MM), **vit. D fazlalığı**, **sarkoidoz**, **KBY** (sekonder hiperparatiroidi)."),
            ]),
        ],
    ],
    sorular=[
        Q("25-26", 61, "GÖRH'de alt özofagustaki çok katlı yassı epitelin intestinal tip kolumnar epitele dönüşmesi?",
          "Metaplazi", "Barrett özofagus"),
        Q("24-25", 70, "Hangi adaptasyon prekanseröz bir durumdur?",
          "Yüksek östrojen düzeyine bağlı endometrium hiperplazisi",
          "Çeldiriciler: gebe uterus hipertrofisi · hepatektomi sonrası hiperplazi · sporcu kas hipertrofisi · pubertede timus atrofisi"),
        Q("23-24", 62, "Hangisi prekanseröz DEĞİLDİR?",
          "Hipertansiyon sonucu gelişen kalp hipertrofisi",
          "Prekanserözler: endometrial hiperplazi · kronik gastritte intestinal metaplazi · sigarada larinks yassı metaplazisi · Barrett"),
        Q("22-23", 61, "Hipertansiyonda artan iş yükünü karşılamak için kalp kasındaki adaptasyon?",
          "Hipertrofi", None),
    ],
))

# ---------------------------------------------------------------- 4
BOLUMLER.append(dict(
    no=4, key="akut", baslik="İnflamasyon: Tanım, Patogenez ve Akut İnflamasyon",
    hoca="Doç. Dr. Selma Erdoğan Düzcü", tarih="22-23 Eylül", saat="3 saat",
    kaynak="2025-26 ders notları + Robbins Temel Patoloji",
    ozet=["5 yılda 7 soru — patolojinin en verimli başlıklarından.",
          "TNF + IL-1 = akut faz (2 kez) · selektin = yuvarlanma · ROS/NO = hücre içi öldürme · inflammazom = sitozolik DAMP sensörü."],
    slaytlar=[
        [
            C("Genel", [
                B("Hasar veya enfeksiyona karşı **koruyucu** yanıt: zararlı ajanı uzaklaştırır, onarımı başlatır; kontrolsüzse doku hasarı."),
                B("Kardinal bulgular: **rubor** (kızarıklık), **calor** (ısı), **tumor** (şişlik), **dolor** (ağrı), **functio laesa** (fonksiyon kaybı)."),
                B("Nedenler: enfeksiyon, **doku nekrozu**, yabancı cisim, immün reaksiyonlar (alerji, otoimmünite), travma."),
                B("Akut: kısa süreli, **nötrofil (PNL)** baskın, eksüda. Kronik: uzun, mononükleer hücre + doku yıkımı + onarım (fibrozis, anjiogenez)."),
            ]),
            C("İlk adım: tanıma", [
                B("**Toll-benzeri reseptörler (TLR)**: plazma membranı ve endozomlarda; mikrobiyal ürünleri (PAMP) tanır → **tanıma aşaması**.", y="21-22"),
                B("**İnflammazom**: **sitozolik** multiprotein kompleks (NLRP3); **DAMP**'ları tanır — ürik asit, **ATP**, ↓ hücre içi K⁺, sitoplazmaya sızan DNA → **kaspaz-1** → **IL-1β**.", y="22-23",
                  tuzak="DAMP'ı tanıyan SİTOZOLİK reseptör TLR değil → inflammazom"),
                B("İnflammazom aşırı aktivitesi: **gut** (ürat kristali), otoinflamatuvar sendromlar (FMF)."),
                B("Diğer sensörler: NOD-like, **RIG-like** (viral RNA), **C-tipi lektin** (fungal glikan), N-formil peptid reseptörü; dolaşan proteinler: **kompleman, MBL, kollektinler**."),
            ]),
            C("Vasküler olaylar", [
                B("Geçici vazokonstriksiyon → **arteriol vazodilatasyonu** (histamin, NO) → akım ↑ (eritem, ısı) → **geçirgenlik ↑** → **eksüda** → staz."),
                B("Geçirgenlik artışında en sık mekanizma: **postkapiller venüllerde endotel kontraksiyonu** (histamin, bradikinin, lökotrienler; hızlı, kısa)."),
                B("Diğer: direkt endotel hasarı (yanık, toksin), lökosit aracılı hasar, **transsitoz** (VEGF), yeni damarlardan sızıntı. Lenf akımı ↑."),
                B("**Transüda** (protein ↓, <1.012) · **Eksüda** (protein ↑, >1.020) · **Pü** (nötrofil + debri).",
                  g="BİYOKİMYA 22-23 · 23-24"),
            ]),
        ],
        [
            C("Hücresel olaylar — lökositin damar dışına çıkışı", [
                B("1) **Marjinasyon**: staz ile lökositler **damar DUVARINA (perifere)** yaklaşır.", y="24-25",
                  tuzak="“Marjinasyonda nötrofiller damarın santraline yakınlaşır” → YANLIŞ"),
                B("2) **Yuvarlanma (rolling) = gevşek adezyon**: **SELEKTİNLER** (E-, P-, L-selektin).", y="24-25"),
                B("3) **Sıkı adezyon**: **İNTEGRİNLER** (LFA-1, Mac-1, VLA-4) ↔ ICAM-1, VCAM-1 (TNF/IL-1 endoteli aktive eder)."),
                B("4) **Transmigrasyon (diapedez)**: **PECAM-1 (CD31)**; postkapiller venüllerden.", y="24-25",
                  tuzak="“CD31 kemotaksisi gerçekleştirir” → YANLIŞ (CD31 = transmigrasyon)"),
                B("5) **Kemotaksis**: N-formil peptidler, **C5a**, **LTB4**, **IL-8 (CXCL8)**."),
                B("6) **Fagositoz**: tanıma-bağlanma (opsoninler: **IgG, C3b**) → yutma → öldürme. Fagositoz İLK olay değildir.", y="24-25",
                  tuzak="“Hücre olaylarından ilk olarak fagositoz gerçekleşir” → YANLIŞ"),
                B("Nötrofil ilk 6-24 saatte, monosit/makrofaj 24-48 saatte baskın."),
            ]),
            C("Öldürme ve yıkım", [
                B("**ROS** (NADPH oksidaz — oksidatif patlama; MPO → HOCl), **NO** (iNOS) ve **lizozomal granül enzimleri** → **mikroorganizmaların hücre içinde (fagolizozomda) yok edilmesi**.", y="25-26 24-25",
                  tuzak="“ROS nötrofilin damar dışına çıkışını sağlar” → YANLIŞ"),
                B("**NET** (nötrofil ekstrasellüler tuzakları); lökosit ürünleri doku hasarı da yapar."),
                B("Defektler: **LAD-1** (CD18 β2-integrin), **LAD-2** (selektin ligandı), **Chediak-Higashi**, **kronik granülomatöz hastalık** (NADPH oksidaz)."),
            ]),
        ],
        [
            C("Kimyasal mediatörler", [
                B("**Histamin**: mast hücresi (en zengin kaynak), bazofil, trombosit — **HÜCRE kökenli, önceden yapılmış**; **arteriol DİLATASYONU** + venül geçirgenliği ↑.", y="25-26",
                  tuzak="“Histamin plazma kökenli mediatördür, arteriollerde vazokonstriksiyon yapar” → YANLIŞ"),
                B("**Araşidonik asit** (fosfolipaz A₂): **COX yolu** → PGE₂ (ağrı, ateş), **PGI₂** (vazodilatasyon, agregasyon inhibisyonu — endotel), **TXA₂** (trombosit agregasyonu + **VAZOKONSTRİKSİYON** — trombosit).", y="25-26",
                  tuzak="“Tromboksan A₂ damarlarda vazodilatasyon yapar” → YANLIŞ"),
                B("**Lipoksijenaz yolu**: **LTB₄** (kemotaksis), LTC₄/D₄/E₄ (vazokonstriksiyon, bronkospazm, geçirgenlik ↑); **lipoksinler** inflamasyonu baskılar. NSAİİ/aspirin COX'u inhibe eder."),
                B("**Kompleman**: C3a, C5a (anafilatoksin), **C5a kemotaksis**, **C3b opsonizasyon**, MAC (C5b-9) lizis. **Bradikinin**: geçirgenlik ↑, vazodilatasyon, **ağrı**. **NO**: vazodilatasyon, mikrop öldürme."),
            ]),
            C("Sitokinler ve sistemik etkiler (akut faz yanıtı)", [
                B("**TNF ve IL-1**: endotel aktivasyonu + **sistemik akut faz reaksiyonları** (ateş, akut faz proteinleri, lökositoz) — en önemli iki sitokin.", y="23-24 25-26"),
                B("**IL-6** → karaciğerden **CRP, fibrinojen (sedimantasyon ↑), SAA**, hepsidin; ateş: PGE₂ (IL-1/TNF pirojen)."),
                B("Lökositoz (bakteri: nötrofili; virüs: lenfositoz; parazit/alerji: eozinofili); ağır durumda **sepsis/septik şok**."),
            ]),
            C("Akut inflamasyonun morfolojik paternleri", [
                B("**Seröz** (yanık kabarcığı, efüzyon) · **Fibrinöz** (perikardit — “ekmek-tereyağı”) · **Süpüratif/pürülan** (**abse**; stafilokok) · **Ülser** (akut peptik ülser).", y="22-23 24-25 25-26"),
                B("**Granülomatöz inflamasyon AKUT değil, KRONİK inflamasyon paternidir.**", y="22-23 25-26",
                  tuzak="“Granülomatöz inflamasyon akut paterndir” / “Süpüratif iltihap kroniktir” → YANLIŞ"),
                B("Sonuç: tam düzelme (rezolüsyon) · skar/fibrozis · kronik inflamasyona ilerleme."),
            ]),
        ],
    ],
    sorular=[
        Q("25-26", 68, "Akut inflamasyonda ROS, nitrik oksit ve granül enzimleri hangi hücresel olayda etkin?",
          "Mikroorganizmaların hücre içinde yok edilmesi", "Adezyon (integrin), marjinasyon, kemotaksis, yuvarlanma (selektin) değil"),
        Q("25-26", 69, "Akut ve kronik inflamasyon reaksiyonlarıyla ilgili doğru olan?",
          "IL-1 ve TNF sistemik akut faz reaksiyonlarını uyarır",
          "Çeldiriciler: granülomatöz akut patern · histamin plazma kökenli/vazokonstriktör · TXA₂ vazodilatatör · süpüratif kronik"),
        Q("24-25", 71, "Akut inflamasyonun hücresel olaylarıyla ilgili doğru olan?",
          "Gevşek adezyon ve yuvarlanma selektin ailesi tarafından gerçekleştirilir",
          "Çeldiriciler: ilk olay fagositoz · marjinasyonda santrale · CD31 kemotaksis · ROS damar dışına çıkış"),
        Q("23-24", 63, "Akut faz reaksiyonlarını uyaran en önemli iki sitokin?",
          "TNF-α ve IL-1", "Histamin-serotonin, NO-ROS, C3-C5, fibrinojen-plazmin değil"),
        Q("22-23", 62, "DAMP'ları tanıyan sitozolik reseptör?",
          "İnflammazom", "TLR, integrin, marjinasyon, bradikinin değil"),
        Q("22-23", 63, "Akut inflamasyonun morfolojik paternleri arasında yer ALMAYAN?",
          "Granülomatöz inflamasyon", "Ülserasyon, pürülan, seröz, fibrinöz = akut"),
        Q("21-22", None, "TLR reseptörleri inflamasyonun hangi aşamasında kullanılır?",
          "Yabancı maddelerin (mikropların) tanınması", "Öğrenci hatırlamasından derlenmiş soru"),
    ],
))

# ---------------------------------------------------------------- 5
BOLUMLER.append(dict(
    no=5, key="kronik", baslik="Kronik İnflamasyon",
    hoca="Doç. Dr. Selma Erdoğan Düzcü", tarih="24 Eylül", saat="2 saat",
    kaynak="2025-26 ders notları + Robbins Temel Patoloji",
    ozet=["4 yıl üst üste soru: granülom ve dev hücre kökeni, kronik iltihapta hangi hücre YOK.",
          "Dev hücre ← epiteloid histiosit / makrofaj (2 kez) · TB'de granülomatöz = kronik · kronik kolitte nötrofil beklenmez."],
    slaytlar=[
        [
            C("Tanım ve nedenler", [
                B("Uzun süreli (haftalar-aylar); **inflamasyon + doku hasarı + onarım (anjiogenez, fibrozis)** eş zamanlı."),
                B("Nedenler: persistan enfeksiyonlar (**tüberküloz**, T. pallidum, virüs, mantar, parazit), **hipersensitivite** (otoimmünite, alerji), uzun süreli toksik maruziyet (**silika**, ateroskleroz)."),
                B("Uzun süren kronik inflamasyon → **AA amiloidoz** zemini (RA, TB, FMF…)."),
            ]),
            C("Hücreler (mononükleer infiltrat)", [
                B("**Makrofaj** (baskın hücre; monosit kökenli): **M1** — klasik, IFN-γ/mikrop ürünleri → ROS, NO, mikrop öldürme; **M2** — alternatif, IL-4/IL-13 → onarım, fibrozis (TGF-β)."),
                B("**Lenfosit**: Th1 (IFN-γ → makrofaj aktivasyonu), Th2 (IL-4, IL-5, IL-13 → eozinofil), Th17 (IL-17 → nötrofil-monosit toplanması); makrofaj ↔ lenfosit karşılıklı uyarı."),
                B("**Plazma hücresi** (antikor), **eozinofil** (parazit, IgE alerji; MBP), **mast hücresi** (akut + kronik; IgE)."),
                B("Kronik nonspesifik kolitte lamina propriada lenfosit, plazma hücresi, makrofaj, eozinofil görülür — **NÖTROFİL (akut iltihap hücresi) beklenmez**.", y="23-24"),
            ]),
        ],
        [
            C("Granülomatöz inflamasyon", [
                B("Kronik inflamasyonun özel paterni — örnek: **tüberkülozda granülomatöz inflamasyon**.", y="24-25 22-23"),
                B("Granülom: **epiteloid histiositler** (aktive makrofaj; geniş pembe sitoplazma) + çevrede lenfosit kuşağı (± plazma hücresi, fibroblast)."),
                B("**Multinükleer dev hücreler = epiteloid histiosit/makrofajların füzyonu**: **Langhans tipi** (çekirdekler periferde at nalı; TB) · **yabancı cisim tipi** (çekirdekler dağınık).", y="25-26 22-23"),
                B("**İmmün granülom** (Th1, IFN-γ): **TB** (merkezde **kazeifikasyon nekrozu**), lepra, sifiliz (gom), kedi tırmığı (yıldızsı mikroabse), **sarkoidoz (nekrozsuz)**, Crohn, mantar enfeksiyonları."),
                B("**Yabancı cisim granülomu**: sütür, talk, **kıl (pilonidal sinüs)**; polarize ışıkta yabancı cisim görülebilir.", y="22-23"),
            ]),
            C("Hatırlatma", [
                B("Akut: nötrofil · Kronik: makrofaj + lenfosit + plazma hücresi · Alerji/parazit: eozinofil."),
                B("Granülomatöz inflamasyon + **kazeifikasyon** = TB'yi düşündür; nekrozsuz = sarkoidoz."),
            ]),
        ],
    ],
    sorular=[
        Q("25-26", 78, "Akciğerde kazeifikasyon nekrozlu TB granülomundaki multinükleer dev hücreler hangi hücrelerden oluşur?",
          "Epiteloid histiositler", "Lenfosit, mast hücresi, fibroblast, atipik tümör hücresi değil"),
        Q("24-25", 72, "Hangi hastalıktaki morfolojik patern kronik inflamasyona örnektir?",
          "Tüberkülozda görülen granülomatöz inflamasyon",
          "Seröz (yanık), süpüratif (stafilokok), abse, akut peptik ülser = akut"),
        Q("23-24", 64, "Kronik nonspesifik kolit biyopsisinde lamina propriada hangi hücre GÖRÜLMEZ?",
          "Nötrofil", "Eozinofil, lenfosit, makrofaj, plazma hücresi görülür"),
        Q("22-23", 74, "Pilonidal sinüste kıl kesitlerini çevreleyen multinükleer hücrelerin kökeni?",
          "Makrofaj", "Yabancı cisim tipi dev hücre"),
    ],
))

# ---------------------------------------------------------------- 6
BOLUMLER.append(dict(
    no=6, key="iyilesme", baslik="İyileşme ve Tamir, Onarım Kusurları",
    hoca="Doç. Dr. Selma Erdoğan Düzcü", tarih="29 Eylül", saat="2 saat",
    kaynak="2025-26 ders notları + Robbins Temel Patoloji",
    ozet=["5 yılın 5'inde de soru: granülasyon dokusu, primer/sekonder iyileşme, hücre tipleri (labil-stabil-permanent).",
          "Sıra: inflamasyon → granülasyon dokusu → fibrozis (önce fibrozis DEĞİL) · yara kontraksiyonu = sekonder iyileşme."],
    slaytlar=[
        [
            C("Rejenerasyon kapasitesi", [
                B("**Labil** (sürekli bölünen): deri/**ağız çok katlı yassı epiteli**, GİS epiteli, **ürotelyum (transisyonel epitel)**, kemik iliği & **lenfoid hücreler**.", y="23-24"),
                B("**Stabil** (G0'da; hücre kaybında **G1'e geçer**, düşük çoğalma): **karaciğer parankim hücresi (hepatosit)**, böbrek, pankreas, endotel, fibroblast, düz kas.", y="23-24"),
                B("**Permanent** (bölünmeyen): **nöron**, **kalp kası** (iskelet kası çok sınırlı — satellit hücre).", y="23-24"),
                B("Siklus: G0 → G1 → S (DNA sentezi) → G2 → M; siklin–CDK kompleksleri; G1/S ve G2/M kontrol noktaları."),
                B("Karaciğer: **parsiyel hepatektomi sonrası** kompansatuvar hiperplazi (HGF, IL-6); ağır hasarda progenitör hücreler."),
            ]),
            C("Büyüme faktörleri", [
                B("**EGF / TGF-α**: epitel ve fibroblast mitojeni (EGFR). **HGF**: hepatosit-epitel."),
                B("**PDGF**: trombosit (+ makrofaj, endotel) → fibroblast, düz kas, monosit göçü ve çoğalması."),
                B("**VEGF**: **anjiogenezin ana uyaranı** + damar geçirgenliği ↑ (reseptörü yalnız endotelde). **FGF-2 (bFGF)**: anjiogenez, fibroblast.", y="22-23"),
                B("**TGF-β**: **en önemli fibrojenik faktör** (kollajen/fibronektin ↑, MMP ↓; anti-inflamatuvar)."),
            ]),
        ],
        [
            C("Skar ile onarım — basamaklar", [
                B("1) **Hemostaz/pıhtı** → 2) **inflamasyon** (nötrofil ~24 s, makrofaj 2-3. gün) → 3) **granülasyon dokusu + anjiogenez** (3-5. gün) → 4) **fibrozis/skar** (kollajen birikimi; tip III → tip I) → 5) **remodeling** (MMP'ler; haftalar-aylar).", y="22-23",
                  tuzak="“Yara iyileşmesinde önce fibrozis gelişir, sonra granülasyon dokusu oluşur” → YANLIŞ"),
                B("**Granülasyon dokusu**: makroskopide **yumuşak, pembe, granüler**; mikroskopide **yeni kapillerler + prolifere fibroblastlar + iltihabi hücreler + gevşek ödemli ECM**.", y="25-26 21-22"),
                B("Onarım alanında **anjiogenez** (VEGF, FGF-2), fibroblast göçü ve **ECM** (kollajen, elastin, fibronektin, laminin, proteoglikan) kritik rol oynar.", y="22-23"),
                B("Yara gerilme gücü: 1. hafta ~%10 → 3. ay ~%70-80 (asla %100 olmaz)."),
            ]),
            C("Deri yarası: primer ↔ sekonder iyileşme", [
                B("**Primer (birincil)**: temiz, kenarları yaklaştırılmış cerrahi insizyon → **az iltihap, az granülasyon, az skar**.", y="24-25",
                  tuzak="“Primer iyileşmede daha fazla skar / daha yoğun iltihabi reaksiyon” → YANLIŞ"),
                B("**Sekonder (ikincil)**: geniş doku kaybı (ülser, infarkt, abse) → **yoğun inflamasyon, bol granülasyon dokusu, fazla skar** + **YARA KONTRAKSİYONU (miyofibroblast)**.", y="24-25"),
                B("Her ikisinde de ilk aşamada **akut inflamasyon** gelişir; **granülasyon dokusu oluşmadan skar gelişmez**.", y="24-25",
                  tuzak="“Granülasyon dokusu gelişmeden skarlaşma olur” / “İlk aşamada akut iltihap gelişmez” → YANLIŞ"),
            ]),
            C("Onarım kusurları", [
                B("Yetersiz: **yara ayrılması (dehisens)**, ülserasyon (DM, vasküler yetmezlik)."),
                B("Aşırı: **hipertrofik skar** (yara sınırında, gerileyebilir) ↔ **keloid** (sınırları aşar, gerilemez; genetik yatkınlık); **ekzuberan granülasyon** (“proud flesh”); **kontraktür** (yanık)."),
                B("İyileşmeyi bozanlar: **enfeksiyon (en önemli)**, diyabet, malnütrisyon (protein, **vit. C** – kollajen hidroksilasyonu, çinko), **glukokortikoidler**, kötü perfüzyon, yabancı cisim, mekanik stres."),
            ]),
        ],
    ],
    sorular=[
        Q("25-26", 70, "Yara iyileşmesinde 3-5. günde yara kabuğu altında yumuşak, pembe, granüler; mikroskopide fibroblast + iltihap hücresi + gevşek ECM?",
          "Granülasyon dokusu", "Rejenerasyon, anjiogenez, nedbe, fibroplazi değil"),
        Q("24-25", 73, "Deri yaralarının iyileşmesiyle ilgili doğru olan?",
          "Yara büzüşmesi (kontraksiyon) sekonder yara iyileşmesinde görülür",
          "Çeldiriciler: granülasyonsuz skar · primer'de daha fazla skar · primer'de yoğun iltihap · ilk aşamada akut iltihap yok"),
        Q("23-24", 65, "G0'da olup hücre kaybında G1'e geçen düşük çoğalma kapasiteli stabil hücre?",
          "Karaciğer parankim hücresi", "Ağız yassı epiteli, ürotelyum, lenfoid hücre = labil · kalp kası = permanent"),
        Q("22-23", 64, "Yara iyileşme süreçleriyle ilgili doğru OLMAYAN?",
          "“Yara iyileşmesi sırasında önce fibrozis gelişir sonra granülasyon dokusu oluşur”",
          "Doğrular: anjiogenez · VEGF ve FGF-2 · fibroblast göçü · ECM rolü"),
        Q("21-22", None, "İyileşme evreleri sorusu", "Granülasyon dokusu", "Öğrenci hatırlamasından derlenmiş soru"),
    ],
))

# ---------------------------------------------------------------- 7
BOLUMLER.append(dict(
    no=7, key="odem", baslik="Ödem, Hiperemi, Konjesyon ve Kanama",
    hoca="Doç. Dr. Selma Erdoğan Düzcü", tarih="25 Eylül", saat="1 saat",
    kaynak="2025-26 ders notları + Robbins Temel Patoloji",
    ozet=["Ödemin mekanizması 2 kez soruldu: KKY = hidrostatik basınç ↑; nefrotik/siroz/malnütrisyon = onkotik basınç ↓.",
          "Tanım tuzakları (25-26): hiperemi ≠ hemoraji · peteşi ≠ ekimoz."],
    slaytlar=[
        [
            C("Ödem ve efüzyon", [
                B("İnterstisyumda sıvı birikimi = **ödem**; vücut boşluklarında = **efüzyon** (hidrotoraks, hidroperikard, hidroperitoneum = **asit**); yaygın ağır ödem = **anazarka**."),
                B("**Transüda**: proteinden fakir, dansite düşük (<1.012) — hidrostatik ↑ veya onkotik ↓. **Eksüda**: proteinden zengin — inflamasyon/geçirgenlik ↑.", y="22-23",
                  tuzak="“Transüda vasfında ödem proteinden zengin olup dansitesi yüksektir” → YANLIŞ", g="BİYOKİMYA 22-23 · 23-24"),
                B("Ödem **azalmış plazma onkotik (ozmotik) basıncında** VEYA **artmış hidrostatik basınçta** gelişebilir.", y="22-23"),
            ]),
            C("Ödem nedenleri", [
                B("**Hidrostatik basınç ↑** (venöz dönüş bozukluğu): **konjestif kalp yetmezliği**, **DVT** (tek bacakta ödem), konstriktif perikardit, portal HT/siroz (asit), venöz obstrüksiyon.", y="23-24"),
                B("**Onkotik basınç ↓** (albümin ↓): **nefrotik sendrom**, **siroz**, **malnütrisyon**, **protein kaybettiren gastroenteropati**. Albümin ARTIŞI ödem yapmaz.", y="23-24 22-23",
                  tuzak="“Plazma albümin seviyesinin artışı ödeme neden olur” → YANLIŞ"),
                B("**Lenfatik obstrüksiyon (lenfödem)**: filariazis (elefantiazis), tümör, **cerrahi/radyasyon** (meme ca aksiller diseksiyonu); memede **peau d'orange**.", y="22-23",
                  tuzak="“Lenfatiklerin obstrüksiyonu ödeme neden olmaz” → YANLIŞ"),
                B("**Na⁺ ve su retansiyonu**: böbrek yetmezliği, **RAAS** aktivasyonu (KKY'de renal hipoperfüzyon); inflamasyon (eksüda)."),
            ]),
            C("Ödem morfolojisi", [
                B("Subkutan ödem **yerçekimine bağımlı** bölgelerde değerlendirilir: ayakta **bacak/ayak bileği**, yatanda sakrum — **gode (pitting)**; kardiyak ödem bacakta, renal (nefrotik) ödem **periorbital**.", y="22-23",
                  tuzak="“Subkutan ödemin klinik değerlendirilmesi koldan yapılır” → YANLIŞ"),
                B("**Akciğer ödemi**: en sık sol kalp yetmezliği; ağır, ıslak; köpüklü-kanlı sıvı. **Beyin ödemi**: giruslar düzleşir, sulkuslar daralır → herniasyon."),
            ]),
        ],
        [
            C("Hiperemi ↔ Konjesyon", [
                B("**Hiperemi**: **AKTİF**; **arteriol dilatasyonu ile artmış kan akımı** (egzersiz, inflamasyon) → **kırmızı** (oksijenlenmiş).", y="25-26",
                  tuzak="“Hemoraji: arteriol dilatasyonu ile artmış kan akımı” → YANLIŞ (bu tanım hiperemi)"),
                B("**Konjesyon**: **PASİF**; venöz dönüş bozukluğu → deoksi-Hb birikimi → **mavi-mor (siyanoz)**; genellikle ödemle birlikte."),
                B("**Akciğerin kronik pasif konjesyonu** (sol KY): septal kalınlaşma/fibrozis + hemosiderin yüklü makrofajlar = **“kalp yetmezliği hücreleri”** → **kahverengi endurasyon**."),
                B("**Karaciğerin kronik pasif konjesyonu** (sağ KY): sentrolobüler konjesyon/nekroz + periportal yağlanma → **“muskat karaciğer”** (nutmeg)."),
            ]),
            C("Kanama (hemoraji) — damar dışına kan çıkışı", [
                B("**Peteşi**: 1-2 mm **noktasal** kanama (deri, mukoza, seroza) — trombositopeni/trombosit fonksiyon bozukluğu.", y="25-26",
                  tuzak="“Ekimoz: deri ve mukozalarda çok küçük noktasal kanama” → YANLIŞ (bu peteşi)"),
                B("**Purpura**: ≥3 mm · **Ekimoz**: 1-2 cm subkutan kanama (**çürük**; renk: kırmızı-mavi → yeşil-mavi → altın-kahverengi)."),
                B("**Hematom**: doku içinde kan birikimi; boşlukta: hemotoraks, hemoperikard, hemoperitoneum, hemartroz."),
                B("Total kan hacminin **%20'sinden azı** kaybı tolere edilir; fazlası **hipovolemik şok**; kronik kayıp → **demir eksikliği anemisi**."),
            ]),
        ],
    ],
    sorular=[
        Q("23-24", 66, "Ödem oluşumunda hidrostatik basınç artışının ön planda olduğu durum?",
          "Konjestif kalp yetmezliği",
          "Nefrotik sendrom, malnütrisyon, protein kaybettiren enteropati = onkotik ↓ · lenfatik tıkanıklık = lenfödem"),
        Q("22-23", 65, "Ödem morfolojisiyle ilgili doğru olan?",
          "Ödem azalmış ozmotik basınçta ya da artmış hidrostatik basınçta gelişebilir",
          "Çeldiriciler: koldan değerlendirilir · lenfatik obstrüksiyon ödem yapmaz · albümin artışı ödem yapar · transüda proteinden zengin"),
        Q("25-26", 71, "(Hemodinamik soru — tanım çeldiricileri, bkz. Bölüm 8)",
          "Doğru: DIC tanımı", "Hemoraji ≠ arteriol dilatasyonu (hiperemi) · Ekimoz ≠ noktasal kanama (peteşi)", ref=True),
    ],
))

# ---------------------------------------------------------------- 8
BOLUMLER.append(dict(
    no=8, key="tromboz", baslik="Trombüs, Emboli, İnfarktüs ve Şok",
    hoca="Doç. Dr. Selma Erdoğan Düzcü", tarih="28 Eylül", saat="2 saat",
    kaynak="2025-26 ders notları + Robbins Temel Patoloji",
    ozet=["Hemostaz molekülleri (vWF, trombomodulin), soluk/kırmızı infarkt ve terim tanımları (DIC, emboli, Zahn) soruluyor.",
          "Ders notu: “Şokun evreleri ve bulguları önemli — sınavda sorulabilir.”"],
    slaytlar=[
        [
            C("Normal hemostaz", [
                B("1) Arteriyel **vazokonstriksiyon** (refleks + **endotelin**)."),
                B("2) **Primer hemostaz (trombosit tıkacı)** — **adezyon**: subendotelyal kollajene **vWF köprüsüyle** trombosit **GpIb** bağlanır.", y="22-23"),
                B("Trombosit **aktivasyonu/sekresyonu** (ADP, Ca²⁺, **TXA₂** sentezi) → **agregasyon**: **GpIIb/IIIa + fibrinojen** köprüsü. (ADP, TXA₂, vWF, fibrin = protrombotik)", y="24-25"),
                B("3) **Sekonder hemostaz**: **doku faktörü (faktör III)** ile koagülasyon kaskadı → **trombin** → fibrinojen → **fibrin** (tıkacı sağlamlaştırır)."),
                B("4) Pıhtı stabilizasyonu ve rezorpsiyon: **t-PA** ile fibrinoliz."),
            ]),
            C("Endotel: antitrombotik ↔ protrombotik", [
                B("Trombosit inhibisyonu: **PGI₂ (prostasiklin)**, **NO**, ADPaz (CD39)."),
                B("Antikoagülan: **heparin-benzeri moleküller** (antitrombin III), **TROMBOMODULİN** (trombine bağlanır → **protein C** aktivasyonu → faktör Va/VIIIa yıkımı → **pıhtılaşma zincirini bloke eder**), endotelyal protein C reseptörü, **TFPI**.", y="24-25"),
                B("Fibrinolitik: **t-PA**. Hasar/aktivasyonda protrombotik: **vWF**, **doku faktörü**, **PAI** (plazminojen aktivatör inhibitörü)."),
            ]),
            C("Tromboz — Virchow triadı", [
                B("**Endotel hasarı** (kalp/arter: MI, ülsere aterom, vaskülit) · **anormal akım** (türbülans → arter/kalp; **staz → ven**) · **hiperkoagülabilite**."),
                B("Kalıtsal: **faktör V Leiden (en sık)**, protrombin mutasyonu, antitrombin III / protein C / protein S eksikliği. Edinsel: immobilizasyon, cerrahi, kanser (Trousseau), gebelik, OKS, sigara, **antifosfolipid sendromu**, HIT, nefrotik sendrom."),
            ]),
        ],
        [
            C("Trombüsün özellikleri", [
                B("**Zahn çizgileri**: soluk trombosit-fibrin ve koyu eritrosit tabakalarının laminasyonu; trombüsün **akan kanda (kalp, aort, arter)** oluştuğunu gösterir → **antemortem trombüsü postmortem pıhtıdan ayırır**.", y="25-26",
                  tuzak="“Zahn çizgisi: tromboze vende görülen makroskobik çizgilenme” → eksik/yanlış tanım"),
                B("Venöz trombüs (flebotromboz): **%90 bacak derin venleri**; staz → **kırmızı (staz) trombüs**, eritrositten zengin. Postmortem pıhtı: jelatinöz, duvara yapışık değil (“tavuk yağı” + “frenk üzümü jölesi”)."),
                B("Trombüsün kaderi: yayılma, **embolizasyon**, çözünme, **organizasyon ve rekanalizasyon**; enfekte → mikotik anevrizma."),
                B("**DIC**: mikrosirkülasyonda **yaygın fibrin trombüsleri** + faktör/trombosit tüketimine bağlı **kanamalar** = **tüketim koagülopatisi**. Nedenler: obstetrik (amniyon sıvısı embolisi, ablasyo), **sepsis**, malignite (APL, müsinöz adenoca), ağır travma/yanık.", y="25-26"),
            ]),
            C("Emboli", [
                B("**Damar içinde kan akımıyla uzak bir yere taşınan katı, sıvı veya gaz kitle**; %99'u tromboemboli.", y="25-26",
                  tuzak="Bu tanım soruda “İnfarktüs” diye verildi → YANLIŞ (tanım emboliye ait)"),
                B("**Pulmoner tromboemboli**: **%95 bacak DVT** kaynaklı; çoğu sessiz; **eyer (saddle) emboli** → ani ölüm; çoklu küçük → pulmoner HT; çift dolaşım → infarkt seyrek."),
                B("**Sistemik tromboemboli**: **%80 kalp içi mural trombüs** (sol ventrikül MI, **AF**'de sol atriyum); en sık hedef **alt ekstremite**, sonra beyin. **Paradoks emboli**: ASD/VSD/PFO."),
                B("**Yağ embolisi**: uzun kemik kırığı, yanık; 1-3 gün sonra pulmoner yetmezlik, nörolojik bulgu, anemi, trombositopeni, **peteşiyal döküntü**."),
                B("**Hava**: >100 mL; **vurgun (dekompresyon)** – azot kabarcıkları (kronik: kaisson, femur başı nekrozu). **Amniyon sıvısı**: doğumda ani dispne, şok, **DIC**; pulmoner damarlarda fetal skuamöz hücre, lanugo, müsin."),
            ]),
        ],
        [
            C("İnfarktüs", [
                B("Arteriyel (nadiren venöz) oklüzyona bağlı **iskemik nekroz** alanı; **koagülasyon nekrozu** (beyinde likefaksiyon); **kama şeklinde**, tepesi tıkalı damara bakar."),
                B("**Beyaz (soluk/anemik) infarkt**: **solid organ + uç (end) arter dolaşımı + arteriyel oklüzyon** → **kalp, dalak, BÖBREK**.", y="24-25"),
                B("**Kırmızı (hemorajik) infarkt**: **venöz oklüzyon** (**over/testis torsiyonu**), **gevşek dokular**, **çift dolaşımlı** dokular (**akciğer, ince barsak**), önceden konjesyon, reperfüzyon.", y="24-25"),
                B("**Septik infarkt**: enfekte vejetasyon embolisi → abse. Etkileyen faktörler: kollateral/çift dolaşım, oklüzyon hızı, hipoksiye duyarlılık (**nöron 3-4 dk**, miyokard 20-30 dk), kanın O₂ içeriği."),
            ]),
            C("Şok — sistemik hipoperfüzyon", [
                B("**Kardiyojenik** (MI, aritmi, tamponad, **pulmoner emboli**), **hipovolemik** (kanama, yanık, kusma-ishal), **septik** (en sık ölüm nedeni yoğun bakımda), **nörojenik** (spinal kord hasarı), **anafilaktik** (Tip I)."),
                B("**Septik şok**: PAMP/DAMP → TNF, IL-1, IL-6 → **yaygın vazodilatasyon + kapiller geçirgenlik ↑** (hipotansiyon), endotel aktivasyonu, DIC, metabolik bozukluk (hiperglisemi, laktik asidoz); erken dönemde cilt **sıcak-kızarık**.", g="PEDİATRİ 25-26"),
                B("**Evreler**: 1) **Nonprogresif (kompanse)**: baroreseptör, katekolamin, RAAS, ADH → **taşikardi, periferik vazokonstriksiyon (soğuk-soluk cilt)**, renal sıvı tutulumu · 2) **Progresif**: doku hipoksisi, anaerobik glikoliz → **laktik asidoz**, arteriol dilatasyonu, kan göllenmesi, oligüri · 3) **İrreversibl**: lizozomal enzim sızıntısı, miyokard kontraktilitesi ↓, **akut tübüler nekroz** → ölüm."),
                B("Morfoloji: beyin, kalp, böbrek (**ATN**), adrenal (lipid kaybı; meningokoksemide **Waterhouse-Friderichsen**), akciğer (**DAH/ARDS**), GİS."),
            ]),
        ],
    ],
    sorular=[
        Q("25-26", 71, "Hemodinamik bozukluklarla ilgili doğru olan?",
          "DIC: mikrosirkülasyonda yaygın trombüsler ve kanamalarla giden tüketim koagülopatisi",
          "Çeldiriciler: hemoraji = arteriol dilatasyonu (hiperemi) · Zahn = tromboze vende çizgilenme · ekimoz = noktasal kanama (peteşi) · infarktüs = taşınan kitle (emboli)"),
        Q("24-25", 74, "Hangi organda soluk (beyaz) infarkt görülür?",
          "Böbrek", "Akciğer, over, testis, barsak → kırmızı infarkt"),
        Q("24-25", 75, "Hemostazda salınımı pıhtılaşma zincirini bloke ederek antitrombotik etki gösteren?",
          "Trombomodulin", "vWF, ADP, TXA₂, fibrin = protrombotik"),
        Q("22-23", 66, "Primer hemostazda trombosit adezyonunda GpIb ile kollajen arasında köprü?",
          "von Willebrand faktör (vWF)", "Trombin, ADP, TXA₂, pıhtılaşma zinciri değil"),
    ],
))

# ---------------------------------------------------------------- 9
BOLUMLER.append(dict(
    no=9, key="amiloid", baslik="Amiloidoz",
    hoca="Doç. Dr. Selma Erdoğan Düzcü", tarih="25 Eylül", saat="1 saat",
    kaynak="2025-26 ders notları + Robbins Temel Patoloji",
    ozet=["★ 5 yılın 5'inde de soru! Kongo red → polarize ışıkta elma yeşili çift kırma.",
          "Ayrıca: FMF → AA amiloid · MM → AL · ekstrasellüler birikim · tiplendirme HE ile YAPILAMAZ · tanı: rektum/abdominal yağ biyopsisi."],
    slaytlar=[
        [
            C("Tanım", [
                B("Yanlış katlanmış proteinlerin **EKSTRASELLÜLER** alanda **β-kırmalı tabaka** yapısında, çözünmeyen **fibriller** halinde birikmesi.", y="24-25"),
                B("EM: dallanmayan 7.5-10 nm fibriller; + **amiloid P komponenti (SAP)** ve proteoglikanlar."),
                B("HE'de **eozinofilik (pembe), amorf, hiyalin** ekstrasellüler materyal; damar duvarı ve bazal membranlar çevresinde.", y="25-26"),
            ]),
            C("★ Boyalar (5/5 yıl)", [
                B("**KONGO RED**: ışık mikroskobunda **pembe-kırmızı**; **polarize ışıkta “ELMA YEŞİLİ” çift kırıcılık (birefringence)** → tanı koydurucu.", y="21-22 22-23 23-24 24-25 25-26"),
                B("**Kristal viyole** (metakromazi) ve tiyoflavin T (floresan) ile de gösterilir.", y="25-26 21-22"),
                B("**Tiplendirme HE ile yapılamaz** → immünohistokimya / kütle spektrometrisi.", y="24-25",
                  tuzak="“AA, AL, ATTR amiloid tipleri H&E boyamada tespit edilir” → YANLIŞ"),
                B("Çeldirici boyalar: Giemsa (H. pylori), Alcian blue (müsin), CD3/CD20 (IHK – lenfosit)."),
            ]),
            C("Tanı biyopsisi", [
                B("**Rektum biyopsisi**, **abdominal yağ aspirasyonu**, dişeti; böbrek biyopsisi.", y="23-24 24-25"),
            ]),
        ],
        [
            C("Amiloid proteinleri ve hastalıklar", [
                B("**AL** (Ig **hafif zinciri**, λ > κ): **plazma hücre diskrazisi / MULTİPL MİYELOM** (primer amiloidoz).", y="24-25"),
                B("**AA** (karaciğerde sentezlenen **SAA**, IL-1/IL-6): **reaktif sistemik (sekonder) amiloidoz** — **kronik inflamasyon** (RA, ankilozan spondilit, IBD, TB, bronşektazi, osteomiyelit) ve **ailesel Akdeniz ateşi (FMF)**.", y="25-26"),
                B("**ATTR** (transtiretin): mutant → **ailesel amiloid polinöropati**; normal → **senil sistemik amiloidoz (kalp)**."),
                B("**Aβ2m** (β2-mikroglobulin): **uzun süreli hemodiyaliz** (karpal tünel, eklem). **Aβ**: **Alzheimer** plakları."),
                B("Lokal/endokrin: **kalsitonin → medüller tiroid karsinomu**; **amilin (IAPP) → tip 2 DM'de Langerhans adacıkları**; ANF → izole atriyal."),
            ]),
            C("Organ tutulumu", [
                B("**Böbrek**: en sık ve en ağır → **nefrotik sendrom** → böbrek yetmezliği (büyük, soluk, sert)."),
                B("**Dalak**: **sago dalak** (foliküllerde) ↔ **lardaseöz dalak** (kırmızı pulpa sinüs duvarları)."),
                B("Karaciğer (Disse aralığı, hepatomegali), **kalp** (restriktif kardiyomiyopati, aritmi), **dil (makroglossi – AL)**, GİS, adrenal, sinir."),
                B("Prognoz: sistemik amiloidozda kötü (AL en kötü); ölüm genellikle böbrek yetmezliği veya kardiyak aritmi."),
            ]),
        ],
    ],
    sorular=[
        Q("25-26", 72, "FMF tanılı hastada barsak perforasyonu; vasküler ve subserozal eozinofilik materyal; Kongo red ve kristal viyole pozitif?",
          "Amiloidoz (AA tipi)", "Paradoks emboli, amniyon sıvısı embolisi, mikotik anevrizma, hidroperitoneum değil"),
        Q("24-25", 76, "Amiloidozla ilgili doğru OLMAYAN?",
          "“AA, AL, ATTR amiloid tipleri H&E boyamada tespit edilir”",
          "Doğrular: Kongo red ile polarize ışıkta çift kırma · ekstrasellüler birikim · rektal biyopsi · MM'de AL"),
        Q("23-24", 67, "Rektum biyopsisinde amiloid: ışık mikroskobunda pembe-kırmızı, polarize ışıkta elma yeşili veren boya?",
          "Kongo red", "Giemsa, kristal viyole, H&E, Alcian blue değil"),
        Q("22-23", 67, "Amiloidi gösteren, polarize ışıkta elma yeşili çift kırma gösteren boya?",
          "Kongo red", "CD3, CD20 (IHK), kristal viyole, Giemsa değil"),
        Q("21-22", None, "Amiloid birikimi hangi boyayla görüntülenir?",
          "Kongo red (kristal viyole)", "Öğrenci hatırlamasından derlenmiş soru"),
    ],
))

# ---------------------------------------------------------------- 10
BOLUMLER.append(dict(
    no=10, key="cevre", baslik="Çevresel Patojenler ve Hastalıklar (Beslenme Dahil)",
    hoca="Doç. Dr. Selma Erdoğan Düzcü", tarih="1 Ekim", saat="2 saat",
    kaynak="2025-26 ders notları + Robbins Temel Patoloji",
    ozet=["4 yıl üst üste soru: ASBEST (2 kez: mezotelyoma + akciğer/larinks ca), sigaranın etkileri, anoreksiya nervoza.",
          "Sigara mukus üretimini ARTIRIR (azaltır değil)."],
    slaytlar=[
        [
            C("Tütün (sigara) — önlenebilir en önemli ölüm nedeni", [
                B("Kanser: **akciğer** (+ **larinks**, ağız, özefagus, **mesane**, böbrek, pankreas, serviks, AML). Karsinojenler: **polisiklik aromatik hidrokarbonlar (benzo[a]piren)**, **nitrozaminler**; nikotin bağımlılık yapar.", y="23-24"),
                B("Solunum yolu: **mukus bezi hiperplazisi → mukus HİPERSEKRESYONU**, silya hasarı, **skuamöz metaplazi**, KOAH (kronik bronşit, amfizem).", y="23-24",
                  tuzak="“Sigara mukozada direkt etki ile mukus üretimini azaltır” → YANLIŞ"),
                B("Kardiyovasküler: ateroskleroz, MI; **trombosit agregasyonu ↑**, **miyokard oksijenlenmesi ↓** (CO → karboksi-Hb, taşikardi).", y="23-24"),
                B("Gebelik: **erken doğum**, düşük doğum ağırlığı, abortus; pasif içicilik. Alkolle sinerji (ağız, larinks, özefagus ca).", y="23-24"),
            ]),
            C("Mesleki/çevresel karsinojen ve toksinler", [
                B("**ASBEST** → **akciğer karsinomu** (sigarayla sinerji), **malign mezotelyoma** (plevra, periton), **LARİNKS kanseri**, over/kolon; asbestozis (interstisyel fibrozis), **plevral plaklar**, ferruginöz cisimcik.", y="22-23 24-25"),
                B("**Vinil klorür → karaciğer anjiyosarkomu** · **benzen → AML** · **aflatoksin B1 → HCC** · **arsenik** → deri SCC, akciğer · **krom/nikel/berilyum** → akciğer ca · **β-naftilamin** → **mesane** ca · **radon** → akciğer."),
                B("**Bisfenol A**, **organoklorinler (DDT)** → endokrin bozucular. (Çeldirici olarak sık kullanılır.)"),
                B("Silika (silikozis, TB riski ↑), kömür tozu (antrakoz → pnömokonyoz), CO (kiraz kırmızısı), **kurşun** (mikrositer anemi + bazofilik noktalanma, diş eti kurşun hattı, nöropati), cıva (Minamata)."),
            ]),
        ],
        [
            C("Alkol, ilaç ve fiziksel ajanlar", [
                B("**Alkol**: karaciğer (yağlanma → alkolik hepatit, Mallory-Denk → siroz), pankreatit, kardiyomiyopati, **Wernicke-Korsakoff** (B1), fetal alkol sendromu; kanser (ağız, larinks, özefagus, karaciğer, meme)."),
                B("İlaçlar: östrojen/HRT (endometrium-meme ca, tromboemboli), **OKS** (tromboz, hepatik adenom), **asetaminofen** (sentrilobüler karaciğer nekrozu)."),
                B("Fiziksel: termal yanık, hipertermi, hipotermi, elektrik, **iyonizan radyasyon** (en duyarlı: lenfoid doku, kemik iliği, gonad, GİS epiteli)."),
            ]),
            C("Beslenme hastalıkları", [
                B("**Marasmus**: çocuğun ağırlığı normalin **<%60**'ı; **somatik protein (iskelet kası) + yağ kaybı**; **ödem YOK**, albümin normal/hafif ↓; büyüme geriliği."),
                B("**Kwashiorkor**: **protein yetersizliği > kalori**; **visseral protein kaybı → hipoalbüminemi → jeneralize ödem**, karaciğer yağlanması, “pul pul boya” deri, saçta renk bantları, apati."),
                B("**Kaşeksi**: kanser/kronik hastalıkta yağ + kas kaybı (TNF, IL-6, PIF)."),
                B("**ANOREKSİYA NERVOZA**: kişinin **isteyerek kendini aç bırakması** → belirgin kilo kaybı; şiddetli PEM benzeri bulgular + **endokrin bozukluklar: AMENORE** (GnRH ↓), hipotiroidi benzeri bulgular, **KONSTİPASYON**, kemik dansitesi ↓; **aritmi/ani ölüm** (hipokalemi).", y="25-26"),
                B("**Bulimia**: tıkınırcasına yeme + kusma → **hipokalemi → aritmi**, aspirasyon, özefagus/mide yırtılması; amenore daha az."),
                B("Vitaminler: **A** (gece körlüğü, kseroftalmi, **skuamöz metaplazi**), **D** (raşitizm/osteomalazi), **C** (skorbüt — kollajen hidroksilasyonu ↓, kanama, yara iyileşmesi bozuk), **B1** (beriberi, Wernicke), **B12/folat** (megaloblastik anemi), **K** (kanama)."),
                B("**Obezite**: metabolik sendrom, tip 2 DM, HT; **kanser** (endometrium, meme, kolon, böbrek); kolelitiyaz, OSA, osteoartrit, NAFLD."),
            ]),
        ],
    ],
    sorular=[
        Q("25-26", 73, "Endokrin bozukluk, amenore, konstipasyon; şiddetli PEM benzeri bulgular; kişinin isteyerek kendini aç bırakması?",
          "Anoreksiya nervoza", "Kwashiorkor, bulimia, marasmus, kaşeksi değil"),
        Q("24-25", 77, "Larinks kanseri ve mezotelyomanın etyopatogenezinde rol alan endüstriyel ajan?",
          "Asbest", "Bisfenol A, vinil klorür, polisiklik hidrokarbon, organoklorin değil"),
        Q("23-24", 68, "Sigarayla ilişkili hastalıkların mekanizmalarıyla ilgili doğru OLMAYAN?",
          "“Mukozada direkt etki ile mukus üretimini azaltır” (aslında ARTIRIR)",
          "Doğrular: erken doğum riski ↑ · akciğer ca ↑ · myokard oksijenlenmesi ↓ · trombosit agregasyonu ↑"),
        Q("22-23", 68, "Uzun süreli maruziyeti akciğer karsinomu ve mezotelyomaya neden olan?",
          "Asbest", "Benzen, vinil klorür, bisfenol A, DDT değil"),
    ],
))
