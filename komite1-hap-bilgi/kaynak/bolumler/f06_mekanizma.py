# -*- coding: utf-8 -*-
"""Kaynak: Drive › Komite-1 › PDF › Farmakoloji › 2026-2027(yeni) › Oruç Yunusoğlu › 2-İlaçların Etkimekanizmaları (66 slayt)"""

from yardim import B, C, Q  # noqa: F401

BOLUM = dict(
    key="mekanizma", baslik="İlaçların Etki Mekanizmaları",
    hoca="Doç. Dr. Oruç Yunusoğlu", tarih="24 Eylül", saat="2 saat",
    kaynak="2-İlaçların Etkimekanizmaları · O. Yunusoğlu · 2026",
    ozet=["Son 5 yılda bu dersten **5 soru** çıktı: **G proteini–reseptör eşleşmesi** (Gq), **ikinci haberciler** (cAMP, DAG; 2 kez), **iyon kanalı** etkili ilaçlar (Ca²⁺ kanal blokerleri, lokal anestezikler → Na⁺ kanalı).",
          "Tuzaklar: **G proteini ikinci haberci değil**, transdüserdir; **insülin, histamin, anjiyotensin** ligandtır, ikinci haberci değildir.",
          "Gq = **α₁, M₁/M₃/M₅, H₁, V₁, AT₁**; Gs = β₁/β₂/β₃, D₁, H₂; Gi = α₂, M₂, D₂, opioid."],
    slaytlar=[
        # 1
        [
            C("Etki mekanizmaları — iki ana grup", [
                B("**Reseptör aracılı** mekanizmalar · **Non-reseptör aracılı** mekanizmalar."),
                B("İlaç hedefleri: **reseptör, enzim, iyon kanalı, transporter/ATPaz ve DNA**."),
            ]),
            C("Reseptör", [
                B("İlaçları ve endojen ligandları **seçici olarak tanıyan** ve bunlara bağlanarak **hücresel yanıtın oluşmasını sağlayan makromoleküler yapılar**."),
                B("Reseptör + ilaç → **reseptör–ilaç kompleksi** → **hücresel yanıt**; model: **“kilit & anahtar”**."),
            ]),
            C("Reseptörlerin 4 ana ailesi", [
                B("1. **Ligand kapılı iyon kanalları** · 2. **G proteinine bağlı reseptörler (GPCR)**"),
                B("3. **Enzimle ilişkili reseptörler** · 4. **Hücre içi / nükleer reseptörler**"),
            ]),
            C("Ailelere göre sinyal ve yanıt başlangıcı", [
                B("**Ligand kapılı iyon kanalı**: iyon akışı · **ms** · örn. GABA-A"),
                B("**GPCR**: G proteinleri / 2. haberciler · **sn–dk** · örn. β₂-AR"),
                B("**Enzimle ilişkili**: kinaz / JAK-STAT · **dk–saat** · örn. insülin reseptörü"),
                B("**Hücre içi/nükleer**: gen transkripsiyonu · **saat–gün** · örn. glukokortikoid reseptörü"),
            ]),
        ],
        # 2
        [
            C("Membran reseptörleri (slayt sınıflaması)", [
                B("**GPCR**: β-adrenerjik reseptörler, muskarinik asetilkolin reseptörleri."),
                B("**Ligand kapılı iyon kanalları**: nikotinik ACh reseptörü, GABA-A reseptörü."),
                B("**Enzimle ilişkili**: reseptör tirozin kinazlar (insülin reseptörü, EGFR); reseptör serin/treonin kinazlar (TGF-β reseptörü); sitokin reseptörleri (JAK/STAT)."),
                B("**Diğer**: Toll-benzeri reseptörler (TLR)."),
            ]),
            C("Doğrudan iyon kanalına bağlı reseptörler", [
                B("**Nikotinik ACh reseptörü** → Na⁺/K⁺ geçişi → **depolarizasyon**."),
                B("**GABA-A reseptörü** → **Cl⁻ kanalı** → **hiperpolarizasyon** → inhibisyon."),
                B("**Glutamat reseptörleri** (AMPA, NMDA, kainat) → Na⁺/Ca²⁺ geçişi → **eksitatör** etki."),
                B("**5-HT₃ reseptörü** → katyon kanalı → depolarizasyon → eksitatör etki."),
                B("**Glisin reseptörü** → Cl⁻ kanalı → inhibisyon."),
            ]),
            C("İyon konsantrasyonu değişimine bağlı etkiler", [
                B("**Na⁺ ve Ca²⁺**: seviye artışı → **uyarıcı**; azalması → baskılayıcı."),
                B("**K⁺**: seviye artışı → **baskılayıcı**; azalması → uyarıcı."),
                B("**Cl⁻**: seviye artışı → **baskılayıcı**; azalması → uyarıcı."),
            ]),
        ],
        # 3
        [
            C("G proteinine bağlı reseptörler (GPCR) — G proteini tipleri", [
                B("**Gs** → adenilat siklaz ↑ → **cAMP ↑**: **β₁, β₂, β₃-adrenerjik; D₁; H₂; glukagon**.", y="25-26", tuzak="“β₂-adrenerjik ve D₁ reseptörü Gq ile kenetlidir” → YANLIŞ"),
                B("**Gi** → adenilat siklaz ↓ → **cAMP ↓**: **α₂-adrenerjik; M₂; D₂; 5-HT₁; opioid μ/κ/δ**.", y="25-26", tuzak="“M₂ ve α₂-adrenerjik reseptör Gq ile kenetlidir” → YANLIŞ"),
                B("**Gq** → **fosfolipaz C ↑** → **IP₃ + DAG ↑** → **Ca²⁺ ↑**: **α₁-adrenerjik; M₁/M₃/M₅; H₁; V₁; AT₁** (tabloda 5-HT₂ de).", y="25-26"),
                B("**G12/13** → Rho/Rac yolakları → hücre iskeleti ve hücresel hareketin düzenlenmesi."),
            ]),
            C("GPCR sinyal sistemi — 3 temel bileşen", [
                B("1. **Reseptör**: ligandı tanır ve bağlanır."),
                B("2. **Transdüser (G proteini)**: reseptörden gelen sinyali hücre içine iletir.", y="24-25 23-24", tuzak="“G-proteini ikinci habercidir” → YANLIŞ"),
                B("3. **Efektör**: adenilat siklaz, fosfolipaz C veya iyon kanalları gibi hedefleri düzenler."),
                B("**Reseptör, G proteini ve efektör birbirinden ayrı moleküler bileşenlerdir.**"),
            ]),
        ],
        # 4
        [
            C("Enzimle ilişkili reseptörler", [
                B("**Reseptör tirozin kinazlar (RTK)**: ligand bağlanması → **dimerizasyon → otofosforilasyon**; MAPK ve PI3K/Akt yollarını aktive eder. Örn. insülin reseptörü, EGFR, PDGFR, VEGFR, FGFR."),
                B("**Reseptör tirozin fosfatazlar (RPTP)**: tirozin kalıntılarındaki fosfatları uzaklaştırır. Örn. CD45, RPTPα, RPTPβ."),
                B("**Sitokin reseptörleri**: **intrinsik kinaz aktivitesi yoktur**; JAK aktivasyonu → STAT fosforilasyonu → gen ekspresyonu. Örn. interlökin ve interferon reseptörleri."),
                B("**Non-reseptör tirozin kinazlar**: sitoplazmik veya membrana bağlı; Src ailesi, JAK, Abl."),
            ]),
            C("İkinci haberciler (enzim → haberci → temel etki)", [
                B("**Adenilat siklaz → cAMP** → **protein kinaz A (PKA)** aktivasyonu.", y="24-25", tuzak="“İnsülin, histamin veya anjiyotensin ikinci habercidir” → YANLIŞ"),
                B("**Fosfolipaz C → IP₃** → hücre içi **Ca²⁺ salınımı**."),
                B("**Fosfolipaz C → DAG** → **protein kinaz C (PKC)** aktivasyonu.", y="23-24", tuzak="“İnsülin, histamin veya anjiyotensin ikinci habercidir” → YANLIŞ"),
                B("**Guanilat siklaz → cGMP** → **protein kinaz G (PKG)** aktivasyonu."),
                B("**Ca²⁺** → kalmodulin üzerinden çeşitli protein/enzimlerin aktivasyonu."),
            ]),
        ],
        # 5
        [
            C("Reseptör sonrası basamakları hedefleyen ajanlar", [
                B("**Pertussis toksini**: **Gi** tipi G proteinlerini inaktive eder."),
                B("**Kolera toksini**: **Gs**'nin sürekli aktif kalmasını sağlar."),
                B("**Lityum**: inozitol monofosfatazı inhibe ederek inozitol fosfat döngüsünü azaltır."),
                B("**Kafein**: endoplazmik retikulumdan Ca²⁺ salınımını artırabilir."),
                B("**Tapsigargin**: **SERCA** pompasını inhibe eder → hücre içi Ca²⁺ artar."),
                B("**Forskolin**: adenilat siklazı reseptör ve G proteinlerinden bağımsız **doğrudan** uyarır."),
                B("**Fasudil**: **Rho-kinaz (ROCK)** inhibitörü; vasküler düz kas gevşemesi, vazodilatasyon."),
            ]),
            C("İlaçların agonistik etkileri", [
                B("**Sinerjizm**: iki ilacın etkisi, her birinin tek başına etkisinin cebirsel toplamından büyüktür (**1 + 1 > 2**). Örn. ampisilin + sulbaktam; trimetoprim + sülfametoksazol."),
                B("**Potansiyalizasyon (supra-aditif)**: tek başına belirgin etkisi olmayan ilacın diğerinin etkisini artırması (**0 + 1 > 1**). Örn. kokainin katekolaminlerin etkisini artırması."),
                B("**Reseptör düzeyinde potansiyalizasyon**: bir ilacın diğerinin reseptör sayısını veya duyarlılığını artırması. Örn. tiroit hormonlarının β-adrenerjik reseptör ekspresyonunu artırması."),
            ]),
        ],
        # 6
        [
            C("Non-reseptör aracılı mekanizmalar (slayt ağacı)", [
                B("Fiziksel / kimyasal nonspesifik etki · enzim inhibisyonu / aktivasyonu · transporter / ATPaz etkisi"),
                B("İyon kanallarının açılması / blokajı · antimetabolit etki · yerine koyma (replasman)"),
                B("Endojen maddelerin salıverilmesini değiştirme · şelasyon · maddeyi bağlama / nötralizasyon"),
                B("Gen transkripsiyonu / mRNA ekspresyonu"),
            ]),
            C("Fiziksel / kimyasal nonspesifik etki", [
                B("İlaç spesifik reseptöre bağlanmadan **fiziksel veya kimyasal özelliğiyle** etki eder."),
                B("**Genel anestezikler** → nöronal iyon kanallarını ve membran fonksiyonlarını etkileyerek nöronal aktiviteyi baskılar."),
                B("**Antiasitler** → HCl'yi nötralize eder."),
                B("**MgSO₄** → ozmotik etkiyle laksatif etki."),
            ]),
            C("Reseptör aktivasyonu / inhibisyonu", [
                B("**Agonist**: reseptöre bağlanır → aktive eder → yanıt oluşturur."),
                B("**Antagonist**: reseptöre bağlanır → aktive etmez → agonistin etkisini engeller."),
                B("Örn. **β₂ agonisti** → β₂ aktivasyonu → cAMP ↑ → **bronkodilatasyon**."),
            ]),
            C("Enzim aktivasyonu / inhibisyonu", [
                B("**Aspirin** → COX inhibisyonu → prostaglandin sentezi ↓."),
                B("**ACE inhibitörleri** → anjiyotensin II ↓ → vazodilatasyon."),
                B("**Statinler** → HMG-CoA redüktaz inhibisyonu → kolesterol sentezi ↓."),
                B("**Neostigmin** → AChE inhibisyonu → ACh ↑."),
            ]),
        ],
        # 7
        [
            C("Antimetabolit olarak etki", [
                B("Doğal metabolitlere benzerlik gösterip **enzimleri veya metabolik yolları inhibe eder**, hücresel işlevleri bozar."),
                B("**Metotreksat** → folat metabolizması ↓ → DNA sentezi ↓ (kanser, otoimmün hastalıklar)."),
                B("**Sülfonamidler** → **PABA ile yarışır** → folat sentezi ↓ (bakteriyel enfeksiyonlar)."),
            ]),
            C("Transporterlar ve ATPazlar", [
                B("**Omeprazol** → H⁺/K⁺-ATPaz inhibisyonu → mide asidi ↓."),
                B("**Digoksin** → Na⁺/K⁺-ATPaz inhibisyonu → hücre içi Ca²⁺ ↑ → kontraktilite ↑."),
                B("**SSRI'lar** → SERT inhibisyonu → sinaptik 5-HT ↑."),
                B("**SGLT2 inhibitörleri** → glukoz geri emilimi ↓ → glukozüri ↑."),
            ]),
            C("İyon kanallarının açılması / kapatılması", [
                B("**Lokal anestezikler** → **Na⁺ kanallarını bloke eder** → sinir iletimi ↓.", y="23-24", tuzak="“Mg⁺ / Ca⁺ kanallarını aktive eder, dopamin reseptörlerini veya ATP duyarlı K⁺ kanallarını bloke eder” → YANLIŞ"),
                B("**Kalsiyum kanal blokerleri** → **Ca²⁺ kanallarını bloke eder** → damar düz kası gevşer.", y="25-26", tuzak="“β-blokerler, kolinesteraz inhibitörleri, D₂ antagonistleri veya antimetabolitler iyon kanallarını açıp kapatır” → YANLIŞ"),
                B("Bazı **antiaritmikler** → Na⁺, K⁺ veya Ca²⁺ kanallarını etkiler → kardiyak iletim/uyarılabilirlik değişir."),
                B("**Kanal açıcı ilaçlar** → belirli iyon kanallarını aktive eder → membran potansiyeli değişir."),
            ]),
        ],
        # 8
        [
            C("Yerine koyma (replasman) tedavisi", [
                B("Eksik endojen madde/metabolitin yerine konulması."),
                B("**L-DOPA** → dopamin öncülü → Parkinson · **insülin** → diabetes mellitus"),
                B("**Levotiroksin** → hipotiroidi · **vitaminler** → vitamin eksiklikleri"),
            ]),
            C("Endojen maddelerin salıverilmesini değiştirme", [
                B("**Efedrin** → noradrenalin salıverilmesi ↑ → sempatik etki ↑."),
                B("**Amfetamin** → monoaminlerin salıverilmesi ↑ → santral/periferik sempatik etkiler ↑."),
                B("**Kromolin** → mast hücrelerinden mediyatör salıverilmesi ↓ → antialerjik etki."),
            ]),
            C("Şelasyon yoluyla etki", [
                B("Metal iyonlarına bağlanıp **kompleks** hâline getirerek vücuttan uzaklaştırır."),
                B("**Kalsiyum disodyum EDTA** → **kurşun (Pb)** · **dimerkaprol (BAL)** → **arsenik, cıva**"),
                B("**Deferoksamin** → **demir (Fe)** · **penisilamin** → **bakır (Cu)**"),
            ]),
            C("Maddeyi bağlayarak etkisizleştirme", [
                B("Bağlanan madde hedef dokuda etkisini gösteremez; klasik reseptör–agonist etkileşiminden farklıdır; **antidotlar ve biyolojik ilaçlar** örnektir."),
                B("**İnfliksimab** → TNF-α'yı bağlar · **omalizumab** → IgE'yi bağlar · **trastuzumab** → HER2'yi hedefler · **şelatörler** → ağır metalleri bağlar."),
            ]),
            C("Gen transkripsiyonu ve mRNA ekspresyonunu değiştirme", [
                B("**Glukokortikoidler**, **tiroid hormonları**, **retinoidler** → **nükleer reseptör** → gen transkripsiyonu / protein sentezi / hücresel farklılaşma değişir."),
                B("**HDAC inhibitörleri** → kromatin yapısı / gen ekspresyonu değişir; **uzun süreli etki**."),
            ]),
        ],
        # 9
        [
            C("Biyolojik / biyobenzer ilaçlar (1)", [
                B("**Anti-TNF-α**: infliksimab, adalimumab → TNF-α nötralizasyonu; romatoid artrit, Crohn, ülseratif kolit."),
                B("**Anti-IL-6**: tocilizumab → IL-6 reseptör blokajı; romatoid artrit, dev hücreli arterit."),
                B("**Anti-IL-17**: secukinumab → IL-17A nötralizasyonu; psöriyazis, psöriyatik artrit."),
                B("**Anti-IL-12/23**: ustekinumab → IL-12/23 sinyal inhibisyonu; psöriyazis, Crohn, ülseratif kolit."),
                B("**Anti-CD20**: rituksimab → B hücrelerine bağlanma, **B hücre deplesyonu**; lenfoma, lösemi, romatoid artrit."),
                B("**Anti-HER2**: trastuzumab → HER2 sinyal inhibisyonu; HER2-pozitif meme/gastrik kanser."),
                B("**Anti-VEGF**: bevacizumab → VEGF nötralizasyonu, anjiyogenez ↓; kolorektal, akciğer, over ve diğer kanserler."),
            ]),
        ],
        [
            C("Biyolojik / biyobenzer ilaçlar (2)", [
                B("**Anti-EGFR**: cetuximab → EGFR blokajı, proliferasyon ↓; kolorektal kanser, baş-boyun kanserleri."),
                B("**Anti-RANKL**: denosumab → RANKL inhibisyonu, osteoklast aktivitesi ↓; osteoporoz, kemik metastazları."),
                B("**Anti-IgE**: omalizumab → serbest IgE bağlanması; alerjik astım, kronik spontan ürtiker."),
                B("**Anti-C5**: eculizumab → C5 inhibisyonu, kompleman aktivitesi ↓; PNH, aHUS, miyastenia gravis."),
                B("**Anti-integrin**: natalizumab → lökositlerin dokuya geçişi ↓; multipl skleroz, Crohn hastalığı."),
                B("**İnsülin analogları**: glargin, lispro → insülin reseptörü aktivasyonu, glukoz kullanımı ↑; diabetes mellitus."),
                B("**Eritropoietinler**: epoetin alfa → EPO reseptörü aktivasyonu, eritropoez ↑; kronik böbrek hastalığına bağlı anemi."),
            ]),
        ],
        # 11
        [
            C("Terminoloji", [
                B("**Reseptör bölgesi**: reseptörde ilacın bağlandığı spesifik bölge."),
                B("**Agonist**: reseptöre bağlanır ve aktive eder."),
                B("**Parsiyel agonist**: reseptörü aktive eder; **tam agonistten daha düşük maksimum yanıt** oluşturur."),
                B("**İnvers agonist**: reseptörün **konstitütif (bazal) aktivitesini azaltır**."),
                B("**Antagonist**: reseptöre bağlanır ama aktive etmez; agonistin etkisini engeller."),
                B("Slaytta anılan kavramlar: afinite, Kd; potens ve etkinlik (EC50, Emax); **potens ≠ etkinlik**."),
            ]),
            C("Kompetitif antagonist", [
                B("Agonistle **aynı bağlanma bölgesi için yarışır**; etkisi **agonist konsantrasyonu artırılarak aşılabilir**."),
                B("Doz-cevap eğrisi **sağa kayar**; **EC50 ↑**; **Emax değişmez**."),
                B("Örn. **atropin** (muskarinik antagonist) → asetilkolinin etkisini bloke eder."),
            ]),
            C("İrreversibl / nonkompetitif antagonizma", [
                B("Antagonist reseptöre **kalıcı bağlanır** veya işlevini geri dönüşsüz engeller."),
                B("Agonist artırılsa da **aşılamaz**; **Emax ↓**; doz-cevap eğrisinin şekli değişebilir."),
                B("Örn. **fenoksibenzamin** → α-adrenerjik reseptörleri irreversibl bloke eder."),
            ]),
        ],
        # 12
        [
            C("Fizyolojik ve kimyasal antagonizma", [
                B("**Fizyolojik antagonist**: **farklı reseptörlere** bağlanarak **zıt fizyolojik etkiler**. Örn. adrenalin → β₂ → bronkodilatasyon; asetilkolin → M₃ → bronkokonstriksiyon."),
                B("**Kimyasal antagonist**: başka ilaç/maddeyle **doğrudan etkileşip** etkisini nötralize eder. Örn. **protamin → heparini nötralize eder**; EDTA → metal iyonlarını bağlar; dimerkaprol → ağır metalleri bağlar."),
            ]),
            C("İlaç etkileşimleri — sınıflama", [
                B("**Farmakodinamik**: sinerjizma, antagonizma."),
                B("**Farmakokinetik (ADME)**: emilim, dağılım, metabolizma, atılım."),
                B("**Farmasötik** etkileşimler (geçimsizlik)."),
            ]),
            C("Antagonizma türleri", [
                B("**Kimyasal**: ilaç/madde doğrudan kimyasal olarak nötralize edilir."),
                B("**Fizyolojik**: farklı reseptörler üzerinden zıt fizyolojik etkiler."),
                B("**Farmakolojik**: aynı reseptör/hedef üzerinden agonistin etkisi engellenir → **kompetitif** (EC50 ↑, Emax ↔) ya da **nonkompetitif** (Emax ↓)."),
            ]),
        ],
        # 13
        [
            C("Doz–yanıt eğrileri", [
                B("**Kademeli (graded)**: **tek bir biyolojik sistemde** doz arttıkça yanıtın büyüklüğü; **Emax ve EC50** değerlendirilir."),
                B("**Kuantal (quantal)**: **popülasyonda** belirli dozda önceden tanımlı **“var/yok”** yanıtı gösterenlerin oranı; **ED50, TD50, LD50** değerlendirilir."),
            ]),
            C("Tolerans ve ilişkili kavramlar", [
                B("**Tolerans**: tekrarlayan/uzun süreli kullanımda aynı etki için **daha yüksek doz** gereksinimi veya etkinin azalması."),
                B("**Taşifilaksi**: toleransın **çok kısa sürede (dakikalar–saatler)** gelişmesi."),
                B("**Desensitizasyon**: **reseptör sayısı değişmeden** reseptör/hücre yanıtının azalması (fosforilasyon → β-arrestin → internalizasyon → yanıt azalması)."),
                B("**Down-regulation**: uzun süreli **agonist** → reseptör sayısı ↓ → yanıt ↓."),
                B("**Up-regulation**: uzun süreli **antagonist** → reseptör sayısı ↑ → yanıt ↑."),
                B("Tolerans ve adaptasyon yalnızca ilaçlarla değil, **endojen ligandların** uzun süreli etkisiyle de gelişebilir."),
            ]),
            C("Terapötik indeks", [
                B("**TI = TD50 / ED50** veya **LD50 / ED50**; **ED50** istenen etki, **TD50** toksik etki, **LD50** ölüm — popülasyonun %50'sinde."),
                B("TI ↑ → güvenlik aralığı ↑; TI ↓ → ↓. **Dar TI**'li ilaçlarda doz ayarlaması ve ilaç düzeyi izlemi daha önemlidir."),
            ]),
        ],
        # 14
        [
            C("Klinik örnek ve slayt sonu soruları", [
                B("**β₂ agonisti → Gs → adenilat siklaz ↑ → cAMP ↑ → bronkodilatasyon** (terapötik etki/yan etki)."),
                B("Desensitizasyon = **reseptör sayısı değişmeden yanıtın azalması**."),
                B("Uzun süreli β-agonist sonrası reseptör sayısı azalması → **down-regulation**."),
                B("**Taşifilaksi** = ilaca saatler içinde gelişen hızlı tolerans."),
                B("Halotan gibi lipofilik genel anestezikler → **lipid membran akışkanlığını değiştirip Na⁺ kanallarının açılmasını engelleyerek** nöronları deprese eder."),
                B("Gen transkripsiyonu/mRNA ekspresyonunu değiştiren grup → **glukokortikoidler**."),
                B("**Yanlış eşleştirme**: Ca²⁺ → doğrudan DNA'ya bağlanıp gen transkripsiyonunu başlatır (Ca²⁺ kalmodulin üzerinden etki eder)."),
                B("Gq aktivasyonu → **fosfolipaz C ↑ → IP₃ ve DAG ↑ → Ca²⁺ ↑**; Gs reseptörü örn. **β₂**."),
            ]),
        ],
    ],
    sorular=[
        Q("25-26", 40, "Aşağıdaki reseptörlerden hangisi Gq proteini ile kenetlidir?", "α₁-adrenerjik reseptör",
          "β₂ ve D₁ → Gs; M₂ ve α₂ → Gi. Gq: α₁, M₁/M₃/M₅, H₁, V₁, AT₁"),
        Q("25-26", 41, "Eksitabl hücrelerde transmembranal iyon kanallarını açıp kapatarak etki gösteren hangisidir?", "Kalsiyum kanal blokörleri",
          "β-bloker ve D₂ antagonisti = reseptör; kolinesteraz inh. = enzim; antimetabolit = metabolik yol"),
        Q("24-25", 43, "Aşağıdakilerden hangisi ikinci habercidir?", "Siklik AMP (cAMP)",
          "İnsülin, histamin, anjiyotensin = ligand; G-proteini = transdüser. İkinci haberciler: cAMP, IP₃, DAG, cGMP, Ca²⁺"),
        Q("23-24", 28, "Aşağıdakilerden hangisi ikinci habercidir?", "Diaçilgliserol (DAG)",
          "İnsülin, histamin, anjiyotensin = ligand; G-proteini = transdüser. Fosfolipaz C → IP₃ + DAG"),
        Q("23-24", 29, "Lokal anesteziklerin etki mekanizması hangisidir?", "Voltaja bağımlı Na⁺ kanallarını bloke ederler",
          "Mg⁺/Ca⁺ kanallarını aktive etme, dopamin reseptörü veya ATP duyarlı K⁺ kanalı blokajı yanlış"),
    ],
)
