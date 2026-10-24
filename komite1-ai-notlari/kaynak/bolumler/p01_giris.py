# -*- coding: utf-8 -*-
"""Kaynak: Drive › Komite-1 › PDF › Patoloji › 2026-2027(yeni) › Selma Erdoğan Düzcü › 1-PATOLOJİYE GİRİŞ (34 slayt)"""

from yardim import B, C, Q  # noqa: F401

BOLUM = dict(
    key="giris", baslik="Patolojiye Giriş",
    hoca="Doç. Dr. Selma Erdoğan Düzcü", tarih="21 Eylül", saat="—",
    kaynak="1-PATOLOJİYE GİRİŞ · Doç. Dr. S. E. Düzcü · 2026",
    ozet=["Son 5 yılda bu dersten **doğrudan soru çıkmadı**.",
          "Bu dersteki **Giemsa, Alcian blue, H&E** amiloid boyası sorularında (22-23, 23-24) **çeldirici şık** olarak geçti — doğru cevap Kongo red (Amiloidoz dersi).",
          "Sayısal bilgiler kolay soru malzemesi: %10 formalin, %96 alkol, ≥4 saat, 12-14 saat, 20 / 10 yıl, 20-30 dk."],
    slaytlar=[
        [
            C("Tanım ve kapsam", [
                B("Patoloji = **hastalık bilimi**. Kapsamı: **tanı, etiyoloji ve patogenez**."),
                B("İki kolu: **1- Genel patoloji**, **2- Sistemik (özel) patoloji**."),
                B("**Temel bilimler ile klinik uygulamalar arasında köprü** görevi gören bilim dalı."),
            ]),
            C("Patoloji laboratuvarına gelen 4 tür materyal", [
                B("1- **Biyopsi** (eksizyonel ve insizyonel)"),
                B("2- **Cerrahi girişim** ile alınan doku ve organlar"),
                B("3- **Otopsiden** alınan doku örnekleri"),
                B("4- **Yayma preparatlar**"),
            ]),
            C("Gönderim, süreler ve saklama", [
                B("**Dokular** fiksatif içinde gönderilir: **%10'luk formalin**."),
                B("**Sitolojik materyaller** **%96'lık alkol** içinde gönderilir."),
                B("Fiksasyon süresi **en az 4 saat**; takip işlemi normal şartlarda **12-14 saat** sürer."),
                B("Saklama: **bloklar en az 20 yıl**, **lamlar en az 10 yıl**, **raporlar süresiz**."),
            ]),
            C("Doku takibi — 8 basamak (slayttaki sırayla)", [
                B("1- **Fiksasyon (tesbit)**: %10'luk formalin"),
                B("2- **Dehidratasyon** (sertleştirme – suyunu alma): en sık **alkol**"),
                B("3- **Şeffaflandırma**: alkolü temizler; en sık kullanılan ajan **ksilen**"),
                B("4- **Sertleştirme (infiltrasyon)**: **parafin**"),
                B("5- **Deparafinizasyon** · 6- **Blok hazırlama (gömme)** · 7- **Kesit hazırlama**"),
                B("8- **Boyama** işlemleri — rutin boya **HE (hematoksilen eozin)**"),
            ]),
        ],
        [
            C("Tanı yöntemleri", [
                B("**Rutin boyalar**: **Hematoksilen & Eozin**, **May-Grünwald Giemsa**, **Papanicolaou**."),
                B("**Özel yöntemler**: enzim histokimya, immünofloresan boyama, histokimyasal boyalar (özel boyalar), immünohistokimya."),
            ]),
            C("Histokimyasal boyalar (özel boyalar)", [
                B("1- **Glikojen ve musin** boyaları: **PAS**, **Alcian blue**"),
                B("2- **Trikrom** boyama yöntemleri: **Masson trikrom**"),
                B("3- **Retikülin** · 4- **Elastin** · 5- **Yağ** · 6- **Pigment ve mineral** boyaları"),
                B("Slayt örnekleri: **Giemsa** ile midede **Helicobacter pylori**; **Alcian blue** boyası."),
            ]),
            C("İmmünohistokimya (İHK)", [
                B("Dokuya **spesifik antijenler** gösterilerek **doku veya tümörün kökeni** hakkında bilgi edinilir."),
                B("**Parafin bloklardan** alınan kesitlerde çalışılabilir."),
            ]),
            C("İHK'da marker olarak kullanılan başlıca antijenler", [
                B("1- **Epitelyal**: keratin, EMA · 2- **Vimentin**"),
                B("3- **Kas**: desmin, aktin, miyoglobin"),
                B("4- **Vasküler**: faktör VIII-AG, CD31"),
                B("5- **Nöral**: S-100 protein, NSE, GFAP"),
                B("6- **Histiyositik**: CD68, S-100"),
                B("7- **Lökosit**: LCA, T ve B lenfosit antijenleri"),
            ]),
        ],
        [
            C("İmmünofloresan boyama", [
                B("Dokuda aranan antijene, **floresans özelliği olan bir madde** antijen-antikor reaksiyonu ile bağlanır; floresan mikroskobunda çeşitli renklerde parlak görüntü elde edilir."),
                B("**Taze, dondurulmuş dokuda** çalışılır ve görüntüde **morfolojik detay yoktur** → kullanım alanı sınırlı."),
                B("Kullanım: **deri ve böbreğin immünolojik hastalıklarının** ayırıcı tanısı."),
            ]),
            C("Enzim histokimya", [
                B("Dokudaki çeşitli **oksidatif ve hidrolitik enzimlerin** gösterilme yöntemi."),
                B("**Taze, dondurulmuş dokuda** çalışılır."),
                B("Kullanım: **kas biyopsilerinin** değerlendirilmesi ve **lösemilerin sınıflandırılması**."),
            ]),
            C("Frozen ile tanı", [
                B("Taze gelen doku, içinde **mikrotom bulunan dondurucu bir cihazda** dondurularak kesilir, hızlıca boyanır ve tanı verilir."),
                B("Tanı **ortalama 20-30 dakika** sürer."),
                B("**Operasyon esnasında**, önceden tanısı bilinmeyen lezyonun tanısı için → **ameliyatın şeklini tayin eder**."),
                B("**Cerrahi sınırlarda tümör kalıp kalmadığını** anlamak için de başvurulur."),
                B("**Kesin tanı yine parafin kesitlerde** verilir."),
            ]),
            C("Moleküler patoloji", [
                B("1- **Hibridizasyon**: FISH, CISH, SISH · 2- **Amplifikasyon**: PCR · 3- **Elektroforez**"),
                B("4- **Sekanslama**: NGS (yeni nesil sekanslama), Sanger dizi analizi, pyrosekanslama · 5- **Likit biyopsi**"),
            ]),
        ],
        [
            C("Sitoloji — 3 tip", [
                B("1- **Eksfoliyatif**: kavitesi olan organların iç yüzeyine **dökülen hücreler** — idrar, BOS, periton sıvısı (parasentez), vajinal yaymalar, balgam. Lama yayılarak ya da sıvı olarak direkt gönderilir."),
                B("2- **Abraziv**: materyal **abeslang veya fırça** ile alınır, fırçadaki hücreler lama yayılır. **Yıkama ile alınan örnekler de abraziv** gruptadır."),
                B("3- **Aspirasyon**: solid organ ve lezyonlar **ince iğne aspirasyon sitolojisi** ile incelenir; kitleye enjektörle girilip çekilen materyal lama yayılır."),
            ]),
            C("Sitolojide fiksasyon", [
                B("Lama yayılmışsa **%96 etil alkol** içinde gönderilir ya da **sprey fiksatif** uygulanır."),
                B("Sıvı örnekte ulaşmada zaman kaybı varsa **örnek miktarı kadar %50 alkol** eklenir (**daha derişik alkol hücreleri büzüştürür**)."),
                B("Aspirasyon sitolojisi preparatları **havada kurutma** yöntemiyle de fikse edilebilir."),
            ]),
            C("Sitolojide inceleme", [
                B("Rutin boyalar · histokimyasal boyama · immünohistokimyasal boyama · immünofloresan boyalar."),
            ]),
            C("Patoloji-sitoloji istem formunda bulunması gerekenler", [
                B("Materyalin **alınma tarihi**, **gönderen doktorun** ismi, hastanın **ismi, adresi, yaşı, cinsi**."),
                B("Materyalin **vücudun neresinden**, hangi sitoloji veya biyopsi **tekniği** ile alındığı."),
                B("**Klinik ön tanı**, şu anki yakınma ve bulgular, varsa uygulanan **tedavi**, **önceki sitolojik ve histolojik tanılar**."),
                B("**Jinekolojik spesmenlerde** ek olarak: **son adet tarihi**, adet düzeni, kontraseptif ilaç alım öyküsü, gebelik öyküsü."),
            ]),
        ],
    ],
    sorular=[],
)
