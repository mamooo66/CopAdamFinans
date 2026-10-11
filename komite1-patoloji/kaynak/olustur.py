#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""İçerik modüllerinden 1280x720 slayt HTML'i üretir (pdf.mjs ile PDF'e basılır)."""

import html
import math
import os
import re
import sys

BURASI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BURASI)

from icerik import BOLUMLER, YILLAR  # noqa: E402
import icerik2  # noqa: E402,F401  (bölüm 11-22'yi BOLUMLER'e ekler)
from icerik_ek import EN_COK, SON_BAKIS  # noqa: E402

TAM_YIL = {"21-22": "2021-22", "22-23": "2022-23", "23-24": "2023-24", "24-25": "2024-25", "25-26": "2025-26"}
ON_SAYFA = 5  # kapak, kullanım, içindekiler, dağılım, en çok çıkanlar


# ------------------------------------------------------------------ yardımcılar
def md(s):
    s = html.escape(s or "", quote=False)
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)


def duz(s):
    return re.sub(r"\*\*", "", s or "")


def yil_etiketi(y):
    return y + ("*" if y == "21-22" else "")


def ck_rozet(yillar):
    ys = [y for y in YILLAR if y in yillar]
    if not ys:
        return ""
    n = len(ys)
    sinif = "ck sicak" if n >= 3 else "ck"
    yildiz = "★ " if n >= 3 else ""
    kat = f'<span class="x">×{n}</span>' if n >= 2 else ""
    etiket = " · ".join(yil_etiketi(y) for y in ys)
    return f'<span class="{sinif}">{yildiz}ÇIKMIŞ{kat}<span class="y">{etiket}</span></span>'


def gri_rozet(g):
    return f'<span class="ck gri">{html.escape(g)}</span>' if g else ""


def kisa_hoca(h):
    return (h.replace("Dr. Öğr. Üyesi ", "Dr. ").replace("Doç. Dr. ", "Doç. Dr. ")
             .replace("Prof. Dr. ", "Prof. Dr. "))


def sayim(b):
    c = {y: 0 for y in YILLAR}
    for q in b["sorular"]:
        if q["ref"] or q["y"] not in YILLAR:
            continue
        c[q["y"]] += q["n"]
    return c


# ------------------------------------------------------------------ yükseklik tahmini
CPL = 70      # yarım genişlik kart, 15px'te satır başına karakter
CPL_Q = 128   # soru kutusu


def kart_agirlik(c, cpl=CPL):
    w = 2.0
    for b in c["maddeler"]:
        L = len(duz(b["t"])) + (24 + 8 * len(b["y"]) if b["y"] else 0) + (len(b["g"] or "") + 4 if b["g"] else 0)
        w += math.ceil(L / cpl) + 0.35
        if b["tuzak"]:
            w += math.ceil((len(b["tuzak"]) + 10) / (cpl * 1.15))
    return w + 0.8


def ikiye_bol(kartlar):
    if len(kartlar) == 1:
        return [kartlar]
    ws = [kart_agirlik(c) for c in kartlar]
    en_iyi = None
    for k in range(1, len(kartlar)):
        m = max(sum(ws[:k]), sum(ws[k:]))
        if en_iyi is None or m < en_iyi[0]:
            en_iyi = (m, k)
    k = en_iyi[1]
    return [kartlar[:k], kartlar[k:]]


def soru_agirlik(q):
    w = 1.2 + math.ceil(len(q["kok"]) / CPL_Q) + math.ceil(len(q["cevap"]) / CPL_Q)
    if q["not_"]:
        w += math.ceil(len(q["not_"]) / (CPL_Q * 1.12))
    return w


def sorulari_sayfala(sorular, butce=25.0, en_fazla=6):
    """Soruları gereken en az sayfaya, sayfalar arasında dengeli dağıtır (tek soruluk artık sayfa olmasın)."""
    ws = [soru_agirlik(q) for q in sorular]
    n = max(math.ceil(sum(ws) / butce), math.ceil(len(sorular) / en_fazla), 1)
    hedef = sum(ws) / n
    sayfalar, cur, top = [], [], 0.0
    for q, w in zip(sorular, ws):
        kalan_sayfa = n - len(sayfalar)
        if cur and kalan_sayfa > 1 and (top + w / 2 > hedef or len(cur) >= en_fazla):
            sayfalar.append(cur)
            cur, top = [], 0.0
        cur.append(q)
        top += w
    if cur:
        sayfalar.append(cur)
    return sayfalar


# ------------------------------------------------------------------ parçalar
def madde_html(b):
    sinif = []
    if b["y"]:
        sinif.append("c")
    if b["lvl"]:
        sinif.append("l1")
    rozet = ck_rozet(b["y"]) + gri_rozet(b["g"])
    tuzak = f'<span class="tuzak">⚠ Tuzak: {md(b["tuzak"])}</span>' if b["tuzak"] else ""
    return f'<li class="{" ".join(sinif)}">{md(b["t"])} {rozet}{tuzak}</li>'


def kart_html(c):
    ck_var = any(b["y"] for b in c["maddeler"])
    li = "".join(madde_html(b) for b in c["maddeler"])
    return f'<div class="kart{" ckli" if ck_var else ""}"><h3>{md(c["baslik"])}</h3><ul>{li}</ul></div>'


def ust_bant(b, ek=""):
    c = sayim(b)
    toplam = sum(c.values())
    sag = (f'<span class="hdr-ck">{toplam} çıkmış soru</span>' if toplam
           else '<span class="hdr-ck sifir">5 yılda soru yok</span>')
    return (f'<header class="hdr"><span class="no">{b["no"]:02d}</span>'
            f'<span class="ttl">{md(b["baslik"])}</span>{ek}<span class="sp"></span>'
            f'<span class="meta">{html.escape(kisa_hoca(b["hoca"]))}</span>{sag}</header>')


def alt_bant(sayfa, kaynak=""):
    return (f'<footer class="ftr"><span>Komite 1 · Patoloji Hap Bilgi · Dönem III · 2026-27</span>'
            f'<span class="src">{html.escape(kaynak)}</span>'
            f'<span class="pg">{sayfa} / @@TOPLAM@@</span></footer>')


def slayt(ic, sinif="", sid=None):
    idattr = f' id="{sid}"' if sid else ""
    return f'<section class="slide {sinif}"{idattr}>{ic}</section>'


# ------------------------------------------------------------------ ön sayfalar
def kapak():
    toplam = sum(sum(sayim(b).values()) for b in BOLUMLER)
    ic = f'''
    <div class="kp-desen"></div>
    <div class="kp-ust">BAİBÜ Tıp Fakültesi · Dönem III · Hastalıkların Biyolojik Temeli Kurulu (I. Kurul)</div>
    <h1 class="kp-baslik">KOMİTE 1<br><span>PATOLOJİ</span></h1>
    <div class="kp-alt">Hap Bilgi Slaytları <b>+</b> Son 5 Yılın Çıkmışları</div>
    <div class="kp-kutular">
      <div><b>{toplam}</b><span>çıkmış patoloji sorusu<br>konu konu işlendi</span></div>
      <div><b>22</b><span>başlık · 46 saatlik<br>patoloji dersinin tamamı</span></div>
      <div><b>5</b><span>yıl: 2021-22 → 2025-26<br>(Dönem III Kurul 1)</span></div>
    </div>
    <div class="kp-lejant">
      <span class="ck">ÇIKMIŞ<span class="y">24-25</span></span> sınavda çıkmış bilgi
      <span class="ck sicak">★ ÇIKMIŞ<span class="x">×3</span><span class="y">…</span></span> 3+ yıl çıkmış
      <span class="tuzak-ornek">⚠ Tuzak</span> çeldirici olarak sorulmuş yanlış ifade
    </div>
    <div class="kp-alt2">2026-27 Kurul Sınavı: <b>30 Ekim 2026 Cuma</b></div>
    '''
    return slayt(ic, "kapak")


def kullanim(sayfa):
    ic = f'''
    <header class="hdr"><span class="no">i</span><span class="ttl">Nasıl kullanılır? · Kaynaklar</span><span class="sp"></span></header>
    <div class="govde iki" data-max="16">
      <div class="sut">
        <div class="kart"><h3>Etiketler</h3><ul>
          <li class="c">Patoloji sorusunda doğrudan çıkmış bilgi {ck_rozet(["24-25"])}</li>
          <li class="c">Birden çok yıl çıkmış bilgi (×yıl sayısı) {ck_rozet(["22-23", "25-26"])}</li>
          <li class="c">3 veya daha fazla yıl çıkmış — “garanti” konu {ck_rozet(["22-23", "24-25", "25-26"])}</li>
          <li class="c">Sınavda yanlış ifade (çeldirici) olarak sorulmuş bilgi {ck_rozet(["24-25"])}<span class="tuzak">⚠ Tuzak: “Hücre içi glikojen depoları artar” → YANLIŞ</span></li>
          <li>Başka bir ders (İç Hast., Pediatri, Biyokimya, Enfeksiyon) sorusunda geçen ilgili bilgi {gri_rozet("İÇ HAST. 23-24")}</li>
          <li><b>21-22*</b> = 2021-22 kitapçığı yok; öğrencilerin hatırladığı sorulardan derlendi.</li>
        </ul></div>
        <div class="kart"><h3>Slayt düzeni</h3><ul>
          <li>Her başlık bir <b>ayraç slaytı</b> ile başlar: hoca, 2026 ders tarihi, 5 yıllık soru sayısı ve öne çıkanlar.</li>
          <li>Ardından <b>hap bilgi</b> slaytları, en sonda o başlığın <b>çıkmış soruları</b> (✔ doğru cevap + çeldiriciler).</li>
          <li>İçindekiler ve soru dağılımı tablosu tıklanabilir; ilgili başlığa atlar.</li>
          <li>Cevap anahtarı olmayan sorular ders slaytı + Robbins'e göre cevaplandı; şüpheli olan tek soru (25-26 S66) ⚠ ile not edildi.</li>
        </ul></div>
      </div>
      <div class="sut">
        <div class="kart"><h3>Çıkmış soru kaynakları (Drive)</h3><ul>
          <li><b>2025-26</b> d3k1 soru kitapçığı A — patoloji S61-82</li>
          <li><b>2024-25</b> kitapçık — patoloji S69-90</li>
          <li><b>2023-24</b> “2023 K1 SON” kitapçığı A — patoloji S61-82</li>
          <li><b>2022-23</b> Toplu Çıkmışlar › Komite 1 — patoloji S60-83</li>
          <li><b>2021-22</b> Toplu Çıkmışlar › Komite 1 — hatırlanan 24 patoloji sorusundan 18'i</li>
        </ul></div>
        <div class="kart"><h3>Hap bilgi kaynakları</h3><ul>
          <li><b>Patoloji › 2026-2027 (yeni)</b> klasörü: <b>1-PATOLOJİYE GİRİŞ</b> (S. E. Düzcü) — şu an klasördeki tek PDF.</li>
          <li>Yeni klasörde henüz olmayan dersler için en güncel <b>2025-26 ders slaytları</b>: Ç. Boran (neoplazi 1-6, karsinojenler), S. P. Özer (dalak, yumuşak doku, immün sistem).</li>
          <li>S. E. Düzcü ve N. T. Karabekiroğlu dersleri için 2025-26 <b>ders notları</b> (Patoloji.pdf) + Robbins Temel Patoloji.</li>
          <li>Konu sırası ve saatleri: <b>Kurul-1 Ders Programı 2026-27</b> (42 teorik + 4 pratik saat).</li>
        </ul></div>
      </div>
    </div>
    {alt_bant(sayfa)}'''
    return slayt(ic, "", "kullanim")


def icindekiler(sayfa, baslangic):
    satirlar = []
    for b in BOLUMLER:
        t = sum(sayim(b).values())
        bar = f'<span class="bar"><i style="width:{min(100, t * 6.5):.0f}%"></i></span>'
        satirlar.append(
            f'<a class="toc" href="#b{b["no"]:02d}"><span class="tn">{b["no"]:02d}</span>'
            f'<span class="tt">{md(b["baslik"])}<em>{html.escape(kisa_hoca(b["hoca"]))}</em></span>'
            f'{bar}<span class="tc">{t if t else "–"}</span><span class="tp">{baslangic[b["no"]]}</span></a>')
    yari = (len(satirlar) + 1) // 2
    ic = f'''
    <header class="hdr"><span class="no">≡</span><span class="ttl">İçindekiler</span><span class="sp"></span>
      <span class="meta">sütun: çıkmış soru sayısı (5 yıl) · sayfa</span></header>
    <div class="govde iki toc-govde" data-max="15"><div class="sut">{"".join(satirlar[:yari])}</div><div class="sut">{"".join(satirlar[yari:])}</div></div>
    {alt_bant(sayfa)}'''
    return slayt(ic, "", "icindekiler")


def dagilim(sayfa):
    def isi(n):
        return "h0" if n == 0 else "h1" if n == 1 else "h2" if n == 2 else "h3"
    satir = []
    ytop = {y: 0 for y in YILLAR}
    for b in BOLUMLER:
        c = sayim(b)
        t = sum(c.values())
        for y in YILLAR:
            ytop[y] += c[y]
        hucre = "".join(f'<td class="{isi(c[y])}">{c[y] or ""}</td>' for y in YILLAR)
        satir.append(f'<tr><td class="dn">{b["no"]:02d}</td><td class="db"><a href="#b{b["no"]:02d}">{md(b["baslik"])}</a></td>'
                     f'{hucre}<td class="dt">{t}</td></tr>')
    bas = "".join(f"<th>{yil_etiketi(y)}</th>" for y in YILLAR)
    alt = "".join(f"<td>{ytop[y]}</td>" for y in YILLAR)
    genel = sum(ytop.values())
    hoca = {}
    for b in BOLUMLER:
        hoca[b["hoca"]] = hoca.get(b["hoca"], 0) + sum(sayim(b).values())
    hoca_li = "".join(f"<li><b>{v}</b> soru — {html.escape(kisa_hoca(k))}</li>"
                      for k, v in sorted(hoca.items(), key=lambda kv: -kv[1]))
    ic = f'''
    <header class="hdr"><span class="no">%</span><span class="ttl">5 Yılın Patoloji Soru Dağılımı</span><span class="sp"></span>
      <span class="meta">her hücre = o yıl o başlıktan çıkan soru</span></header>
    <div class="govde dg" data-max="15">
      <table class="dtab"><colgroup><col class="c-dn"><col class="c-db">{'<col class="c-y">' * len(YILLAR)}<col class="c-t"></colgroup>
        <thead><tr><th></th><th class="db">Başlık</th>{bas}<th>Top.</th></tr></thead>
        <tbody>{"".join(satir)}</tbody>
        <tfoot><tr><td></td><td class="db">Toplam</td>{alt}<td class="dt">{genel}</td></tr></tfoot></table>
      <div class="dg-yan">
        <div class="kart"><h3>Ne anlama geliyor?</h3><ul>
          <li>Patoloji her yıl <b>22-24 soru</b> (95 soruluk kurul sınavının ~%24'ü).</li>
          <li>En verimli başlıklar: <b>İmmün sistem (15)</b>, <b>Moleküler temel (10)</b>, <b>Lenf nodu (10)</b>, <b>Akut inflamasyon (7)</b>, <b>Karsinojenler (7)</b>.</li>
          <li><b>5/5 yıl</b> soru gelenler: hücre hasarı, iyileşme-tamir, amiloidoz, epitelyal tümörler, lenf nodu, karsinojenler, moleküler temel.</li>
        </ul></div>
        <div class="kart"><h3>Hoca bazında (5 yıl)</h3><ul>{hoca_li}</ul></div>
        <div class="not">21-22* sütunu hatırlanan sorulardan derlendi (resmi kitapçık yok).</div>
      </div>
    </div>
    {alt_bant(sayfa)}'''
    return slayt(ic, "", "dagilim")


def en_cok(sayfa):
    li = []
    for i, (t, ys, no) in enumerate(EN_COK, 1):
        li.append(f'<li><span class="rk">{i}</span><span class="ec-t">{md(t)} {ck_rozet(ys.split())}'
                  f'<a class="ec-git" href="#b{no:02d}">→ Bölüm {no:02d}</a></span></li>')
    yari = (len(li) + 1) // 2
    ic = f'''
    <header class="hdr"><span class="no">★</span><span class="ttl">En Çok Çıkan Bilgiler — Sınava 1 Gün Kala</span><span class="sp"></span>
      <span class="meta">tekrar eden yıl sayısına göre</span></header>
    <div class="govde iki" data-max="16.5"><ol class="ec sut">{"".join(li[:yari])}</ol><ol class="ec sut" start="{yari + 1}">{"".join(li[yari:])}</ol></div>
    {alt_bant(sayfa)}'''
    return slayt(ic, "", "encok")


# ------------------------------------------------------------------ bölüm slaytları
def ayrac(b, sayfa):
    c = sayim(b)
    t = sum(c.values())
    cipler = "".join(
        f'<div class="yc{" bos" if c[y] == 0 else ""}"><span>{yil_etiketi(y)}</span><b>{c[y]}</b></div>' for y in YILLAR)
    ozet = "".join(f"<li>{md(o)}</li>" for o in b.get("ozet", []))
    yeni = '<span class="yeni">YENİ 2026-27 PDF</span>' if b.get("yeni") else ""
    saat = f' · {html.escape(b["saat"])}' if b.get("saat") and b["saat"] != "—" else ""
    basliklar = [c["baslik"] for kartlar in b["slaytlar"] for c in kartlar]
    if b["sorular"]:
        basliklar.append("Çıkmış sorular")
    icerik = "".join(f'<span class="dv-cip">{md(t)}</span>' for t in basliklar)
    sayi = (f'<div class="dv-n"><b>{t}</b><span>çıkmış soru<br>son 5 yılda</span></div>' if t
            else '<div class="dv-n sifir"><b>0</b><span>son 5 yılda<br>doğrudan soru yok</span></div>')
    ic = f'''
    <div class="dv-bg">{b["no"]:02d}</div>
    <div class="dv-ust">BÖLÜM {b["no"]:02d} / {len(BOLUMLER)} {yeni}</div>
    <h1 class="dv-baslik">{md(b["baslik"])}</h1>
    <div class="dv-meta">{html.escape(b["hoca"])} · 2026: {html.escape(b["tarih"])}{saat}</div>
    <div class="dv-istat">{sayi}<div class="dv-yillar">{cipler}</div></div>
    <div class="dv-ozet"><h4>Bu başlıkta öne çıkanlar</h4><ul>{ozet}</ul></div>
    <div class="dv-icerik"><h4>Bu bölümde</h4><div class="dv-cipler">{icerik}</div></div>
    <div class="dv-kaynak">Kaynak: {html.escape(b["kaynak"])}<span class="pg">{sayfa} / @@TOPLAM@@</span></div>'''
    return slayt(ic, "ayrac", f'b{b["no"]:02d}')


def icerik_slayti(b, kartlar, sayfa, sira, adet):
    ek = f'<span class="parca">{sira}/{adet}</span>' if adet > 1 else ""
    sutunlar = ikiye_bol(kartlar)
    sinif = "govde iki" if len(sutunlar) == 2 else "govde tek"
    gov = "".join(f'<div class="sut">{"".join(kart_html(c) for c in s)}</div>' for s in sutunlar)
    ic = f'{ust_bant(b, ek)}<div class="{sinif}" data-max="18">{gov}</div>{alt_bant(sayfa, b["kaynak"])}'
    return slayt(ic, "icerik")


def soru_html(q):
    if q["y"] in YILLAR:
        yil = TAM_YIL[q["y"]] + ("*" if q["y"] == "21-22" else "")
    else:
        yil = q["y"]
    no = f'S{q["no"]}' if q["no"] else ("hatırlanan" if q["y"] == "21-22" else "")
    sinif = "q"
    if q["ref"]:
        sinif += " ref"
        no = (no + " · atıf").strip(" ·")
    elif q["y"] == "21-22":
        sinif += " hatira"
    not_ = f'<div class="qnot">{md(q["not_"])}</div>' if q["not_"] else ""
    return (f'<div class="{sinif}"><div class="qtag"><b>{html.escape(yil)}</b><span>{html.escape(no)}</span></div>'
            f'<div class="qg"><div class="qk">{md(q["kok"])}</div><div class="qa">✔ {md(q["cevap"])}</div>{not_}</div></div>')


def soru_slayti(b, sorular, sayfa, sira, adet):
    ek = f'<span class="parca soru">ÇIKMIŞ SORULAR{f" {sira}/{adet}" if adet > 1 else ""}</span>'
    ic = (f'{ust_bant(b, ek)}<div class="govde sorular" data-max="17.5">{"".join(soru_html(q) for q in sorular)}</div>'
          f'{alt_bant(sayfa, "Cevaplar: ders slaytları + Robbins (resmi cevap anahtarı yok)")}')
    return slayt(ic, "soru-slayt")


def son_bakis(parcalar, sayfa0):
    out = []
    for i, parca in enumerate(parcalar):
        li = "".join(f'<li>{md(t)} {ck_rozet(ys.split())}</li>' for t, ys in parca)
        ic = f'''
        <header class="hdr"><span class="no">✓</span><span class="ttl">Son Bakış — Tek Satırlık Haplar</span>
          <span class="parca">{i + 1}/{len(parcalar)}</span><span class="sp"></span><span class="meta">sınav sabahı</span></header>
        <div class="govde tek" data-max="17"><ul class="sb">{li}</ul></div>
        {alt_bant(sayfa0 + i)}'''
        out.append(slayt(ic, "", "sonbakis" if i == 0 else None))
    return out


# ------------------------------------------------------------------ montaj
def olustur():
    # 1. geçiş: sayfa sayıları
    plan = []
    for b in BOLUMLER:
        soru_sayfalari = sorulari_sayfala(b["sorular"]) if b["sorular"] else []
        plan.append((b, soru_sayfalari))
    baslangic, p = {}, ON_SAYFA + 1
    for b, ss in plan:
        baslangic[b["no"]] = p
        p += 1 + len(b["slaytlar"]) + len(ss)
    son_parcalar = [SON_BAKIS[:17], SON_BAKIS[17:]]
    toplam = p - 1 + len(son_parcalar)

    # 2. geçiş: render
    s = [kapak(), kullanim(2), icindekiler(3, baslangic), dagilim(4), en_cok(5)]
    for b, ss in plan:
        sayfa = baslangic[b["no"]]
        s.append(ayrac(b, sayfa))
        sayfa += 1
        for i, kartlar in enumerate(b["slaytlar"], 1):
            s.append(icerik_slayti(b, kartlar, sayfa, i, len(b["slaytlar"])))
            sayfa += 1
        for i, qs in enumerate(ss, 1):
            s.append(soru_slayti(b, qs, sayfa, i, len(ss)))
            sayfa += 1
    s.extend(son_bakis(son_parcalar, p))
    assert len(s) == toplam, (len(s), toplam)

    with open(os.path.join(BURASI, "stil.css"), encoding="utf-8") as f:
        css = f.read()
    with open(os.path.join(BURASI, "sigdir.js"), encoding="utf-8") as f:
        js = f.read()
    sayfa_html = (f'<!doctype html><html lang="tr"><head><meta charset="utf-8">'
                  f'<title>Komite 1 Patoloji Hap Bilgi</title><style>{css}</style></head>'
                  f'<body>{"".join(s)}<script>{js}</script></body></html>')
    sayfa_html = sayfa_html.replace("@@TOPLAM@@", str(toplam))
    hedef = os.path.join(BURASI, "slaytlar.html")
    with open(hedef, "w", encoding="utf-8") as f:
        f.write(sayfa_html)
    print(f"{hedef}: {toplam} slayt")


if __name__ == "__main__":
    olustur()
