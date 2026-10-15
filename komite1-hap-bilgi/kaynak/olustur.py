#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""İçerik modüllerinden 1280x720 slayt HTML'i üretir (pdf.cjs ile PDF'e basılır).

Desteye yalnızca bolumler/ klasöründeki modüller (2026-27 PDF'lerinden yazılmış dersler) girer.
Kullanım: python3 olustur.py [--sadece p02_hasar,f01_giris] [--cikti yol/slaytlar.html]

Sıra: kapak · kullanım · içindekiler ·
      her ders için: ders ayracı · soru dağılımı · en çok çıkanlar · bölümler (ayraç, hap bilgi, çıkmış sorular)
Dağılım ve en çok çıkanlar sayfaları ancak gösterecek veri varsa eklenir.
"""

import html
import math
import os
import pathlib
import re
import sys

BURASI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BURASI)

import icerik  # noqa: E402
from yardim import YILLAR  # noqa: E402
from cikmis_patoloji import BEKLEYEN as BEKLEYEN_P  # noqa: E402

try:
    from cikmis_farmakoloji import BEKLEYEN as BEKLEYEN_F  # noqa: E402
except ImportError:
    BEKLEYEN_F = {}

BEKLEYEN = {"Patoloji": BEKLEYEN_P, "Farmakoloji": BEKLEYEN_F}
SINIF = {"Patoloji": "p", "Farmakoloji": "f"}
YILLIK = {"Patoloji": "her yıl 22-24 patoloji sorusu", "Farmakoloji": "her yıl 28-30 farmakoloji sorusu"}
KITAPCIK = [  # (yıl, kaynak, patoloji aralığı, farmakoloji aralığı)
    ("2025-26", "d3k1 soru kitapçığı A", "S61-82", "S13-42"),
    ("2024-25", "2024-2025 kitapçığı", "S69-90", "S27-56"),
    ("2023-24", "“2023 K1 SON” kitapçığı A", "S61-82", "S13-40"),
    ("2022-23", "Toplu Çıkmışlar › Komite 1", "S60-83", "S11-39"),
    ("2021-22*", "Toplu Çıkmışlar › Komite 1 (kitapçık yok, hatırlanan sorular)", "hatırlanan", "hatırlanan"),
]
TAM_YIL = {"21-22": "2021-22", "22-23": "2022-23", "23-24": "2023-24", "24-25": "2024-25", "25-26": "2025-26"}

BOLUMLER = []  # olustur() doldurur


# ------------------------------------------------------------------ yardımcılar
def md(s):
    s = html.escape(s or "", quote=False)
    return re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)


def duz(s):
    return re.sub(r"\*\*", "", s or "")


def buyuk(s):
    """Türkçe büyük harf (i → İ, ı → I)."""
    return s.replace("i", "İ").replace("ı", "I").upper()


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
    return h.replace("Dr. Öğr. Üyesi ", "Dr. ")


def sayim(b):
    c = {y: 0 for y in YILLAR}
    for q in b["sorular"]:
        if q["ref"] or q["y"] not in YILLAR:
            continue
        c[q["y"]] += q["n"]
    return c


def toplam_soru(b):
    return sum(sayim(b).values())


def dersler():
    return [d for _, d in icerik.DERSLER if any(b["ders"] == d for b in BOLUMLER)]


def ders_bolumleri(d):
    return [b for b in BOLUMLER if b["ders"] == d]


def bekleyen(d):
    """PDF'i henüz gelmemiş derslerin (başlık, soru sayısı) listesi."""
    out = []
    for v in BEKLEYEN[d].values():
        n = sum(q["n"] for q in v["sorular"] if not q["ref"])
        out.append((v["baslik"], n))
    return out


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
    t = toplam_soru(b)
    sag = (f'<span class="hdr-ck">{t} çıkmış soru</span>' if t
           else '<span class="hdr-ck sifir">5 yılda soru yok</span>')
    return (f'<header class="hdr"><span class="no">{b["kod"]}</span>'
            f'<span class="ttl">{md(b["baslik"])}</span>{ek}<span class="sp"></span>'
            f'<span class="meta">{html.escape(kisa_hoca(b["hoca"]))}</span>{sag}</header>')


def alt_bant(sayfa, kaynak="", ders=None):
    ad = ders or " + ".join(dersler()) or "Hap Bilgi"
    return (f'<footer class="ftr"><span>Komite 1 Hap Bilgi · {html.escape(ad)} · Dönem III · 2026-27</span>'
            f'<span class="src">{html.escape(kaynak)}</span>'
            f'<span class="pg">{sayfa} / @@TOPLAM@@</span></footer>')


def slayt(ic, sinif="", sid=None):
    idattr = f' id="{sid}"' if sid else ""
    return f'<section class="slide {sinif}"{idattr}>{ic}</section>'


def yil_cipleri(c):
    return "".join(f'<div class="yc{" bos" if c[y] == 0 else ""}"><span>{yil_etiketi(y)}</span><b>{c[y]}</b></div>'
                   for y in YILLAR)


# ------------------------------------------------------------------ ön sayfalar
def kapak():
    ds = dersler()
    adlar = '<span class="ayir"> + </span>'.join(f'<span class="{SINIF[d]}">{buyuk(d)}</span>' for d in ds)
    kutular = "".join(
        f'<div><b>{len(ders_bolumleri(d))}</b><span>{d.lower()} dersi<br>bu dönemin PDF\'inden</span></div>' for d in ds)
    taranan = sum(toplam_soru(b) for b in BOLUMLER) + sum(n for d in ds for _, n in bekleyen(d))
    ic = f'''
    <div class="kp-desen"></div>
    <div class="kp-ust">BAİBÜ Tıp Fakültesi · Dönem III · Hastalıkların Biyolojik Temeli Kurulu (I. Kurul)</div>
    <h1 class="kp-baslik">KOMİTE 1<span class="kp-dersler">{adlar}</span></h1>
    <div class="kp-alt">Hap Bilgi Slaytları <b>·</b> yalnızca 2026-27 dönemi PDF'lerinden</div>
    <div class="kp-kutular">
      {kutular}
      <div><b>{taranan}</b><span>çıkmış soru tarandı<br>2021-22 → 2025-26</span></div>
    </div>
    <div class="kp-lejant">
      <span class="ck">ÇIKMIŞ<span class="y">24-25</span></span> sınavda çıkmış bilgi
      <span class="ck sicak">★ ÇIKMIŞ<span class="x">×3</span><span class="y">…</span></span> 3+ yıl çıkmış
      <span class="tuzak-ornek">⚠ Tuzak</span> çeldirici olarak sorulmuş yanlış ifade
    </div>
    <div class="kp-alt2">Yeni PDF geldikçe ilgili ders çıkmışlarıyla birlikte eklenir · Kurul sınavı: <b>30 Ekim 2026 Cuma</b></div>
    '''
    return slayt(ic, "kapak")


def kullanim(sayfa):
    ds = dersler()
    ders_li = "".join(
        f"<li><b>{d}</b>: {len(ders_bolumleri(d))} ders — Drive › Komite-1 › PDF › {d} › 2026-2027(yeni)</li>" for d in ds)
    bekleyen_n = sum(n for d in ds for _, n in bekleyen(d))
    eksikler = [b for b in BOLUMLER if b.get("eksik")]
    eksik_li = (f"<li>⚠ PDF'i kısmen okunabilen dersler: {', '.join(b['kod'] for b in eksikler)} — eksik kısım ayraç slaytında yazıyor.</li>"
                if eksikler else "")
    kaynak_li = "".join(
        f"<li><b>{y}</b> {html.escape(k)} — "
        + " · ".join(f"{d.lower()} {p if d == 'Patoloji' else f}" for d in ds) + "</li>"
        for y, k, p, f in KITAPCIK)
    ic = f'''
    <header class="hdr"><span class="no">i</span><span class="ttl">Nasıl kullanılır? · Kaynaklar</span><span class="sp"></span></header>
    <div class="govde iki" data-max="16">
      <div class="sut">
        <div class="kart"><h3>Kaynak kuralı</h3><ul>
          <li>Hap bilgiler <b>yalnızca bu dönemin (2026-27) ders PDF'lerinden</b> yazıldı. Eski klasör, geçmiş yılların notları ve kitaplar <b>kullanılmadı</b>.</li>
          {ders_li}
          <li>Çıkmış sorunun cevabı 2026-27 PDF'inde yoksa soru yine gösterilir ve <b>“(PDF'te geçmiyor)”</b> diye işaretlenir.</li>
          <li>PDF'i henüz yüklenmemiş dersler desteye konmadı; çıkmışları hazır bekliyor ({bekleyen_n} soru).</li>
          {eksik_li}
        </ul></div>
        <div class="kart"><h3>Slayt düzeni</h3><ul>
          <li>Her ders kendi bölümünde: <b>ders ayracı</b> → <b>soru dağılımı</b> → <b>en çok çıkanlar</b> → dersler.</li>
          <li>Her ders bir <b>ayraç slaytı</b> ile başlar (hoca, 2026 ders tarihi, 5 yıllık soru sayısı); sonra <b>hap bilgi</b>, en sonda o dersin <b>çıkmış soruları</b> (✔ doğru cevap + çeldiriciler).</li>
          <li>İçindekiler, dağılım tablosu ve “→ P05” bağlantıları tıklanabilir.</li>
        </ul></div>
      </div>
      <div class="sut">
        <div class="kart"><h3>Etiketler</h3><ul>
          <li class="c">Aynı dersin sorusunda doğrudan çıkmış bilgi {ck_rozet(["24-25"])}</li>
          <li class="c">Birden çok yıl çıkmış bilgi (×yıl sayısı) {ck_rozet(["22-23", "25-26"])}</li>
          <li class="c">3 veya daha fazla yıl çıkmış {ck_rozet(["22-23", "24-25", "25-26"])}</li>
          <li class="c">Sınavda yanlış ifade (çeldirici) olarak sorulmuş bilgi {ck_rozet(["24-25"])}<span class="tuzak">⚠ Tuzak: sınavdaki yanlış ifade</span></li>
          <li>Başka bir dersin sorusunda geçen ilgili bilgi {gri_rozet("İÇ HAST. 23-24")}</li>
        </ul></div>
        <div class="kart"><h3>Çıkmış soru kaynakları (Drive › Çıkmışlar)</h3><ul>{kaynak_li}</ul></div>
      </div>
    </div>
    {alt_bant(sayfa)}'''
    return slayt(ic, "", "kullanim")


def icindekiler(sayfa, baslangic, ders_bas):
    sutunlar = []
    for d in dersler():
        bs = ders_bolumleri(d)
        sat = [f'<a class="toc-bas {SINIF[d]}" href="#ders-{SINIF[d]}">{buyuk(d)} · {len(bs)} ders · '
               f'{sum(toplam_soru(b) for b in bs)} çıkmış soru<span>s. {ders_bas[d]}</span></a>']
        for b in bs:
            t = toplam_soru(b)
            bar = f'<span class="bar"><i style="width:{min(100, t * 6.5):.0f}%"></i></span>'
            sat.append(f'<a class="toc {SINIF[d]}" href="#{b["kod"]}"><span class="tn">{b["kod"]}</span>'
                       f'<span class="tt">{md(b["baslik"])}</span>{bar}'
                       f'<span class="tc">{t if t else "–"}</span><span class="tp">{baslangic[b["kod"]]}</span></a>')
        sutunlar.append(sat)
    if len(sutunlar) == 1:  # tek ders: iki sütuna böl
        s = sutunlar[0]
        yari = (len(s) + 1) // 2
        sutunlar = [s[:yari], s[yari:]]
    govde = "".join(f'<div class="sut">{"".join(s)}</div>' for s in sutunlar)
    ic = f'''
    <header class="hdr"><span class="no">≡</span><span class="ttl">İçindekiler</span><span class="sp"></span>
      <span class="meta">sütunlar: çıkmış soru sayısı (5 yıl) · sayfa</span></header>
    <div class="govde iki toc-govde" data-max="15">{govde}</div>
    {alt_bant(sayfa)}'''
    return slayt(ic, "", "icindekiler")


# ------------------------------------------------------------------ ders sayfaları
def ders_ayrac(d, sayfa, baslangic):
    bs = ders_bolumleri(d)
    c = {y: sum(sayim(b)[y] for b in bs) for y in YILLAR}
    t = sum(c.values())
    sirali = sorted(bs, key=lambda b: -toplam_soru(b))
    verimli = ", ".join(f"<b>{md(b['baslik'])}</b> ({toplam_soru(b)})" for b in sirali[:4] if toplam_soru(b))
    bek = bekleyen(d)
    ozet = [f"Kurul sınavında {YILLIK[d]} çıkıyor; bu destedeki derslerden 5 yılda <b>{t}</b> soru."]
    if verimli:
        ozet.append(f"En çok soru gelen dersler: {verimli}.")
    if bek:
        ozet.append("PDF'i henüz yüklenmemiş: " + ", ".join(f"{html.escape(a)} ({n})" for a, n in bek)
                    + f" — {sum(n for _, n in bek)} çıkmış soru PDF gelince eklenecek.")
    hocalar = []
    for b in bs:
        if b["hoca"] not in hocalar:
            hocalar.append(b["hoca"])
    cipler = "".join(f'<a class="dv-cip" href="#{b["kod"]}"><b>{b["kod"]}</b> {md(b["baslik"])} · s.{baslangic[b["kod"]]}</a>'
                     for b in bs)
    ic = f'''
    <div class="dv-bg">{SINIF[d].upper()}</div>
    <div class="dv-ust">KOMİTE 1 · DERS</div>
    <h1 class="dv-baslik dv-ders">{buyuk(d)}</h1>
    <div class="dv-meta">{len(bs)} ders · 2026-27 PDF'lerinden · {html.escape(", ".join(kisa_hoca(h) for h in hocalar))}</div>
    <div class="dv-istat"><div class="dv-n"><b>{t}</b><span>çıkmış soru<br>son 5 yılda</span></div><div class="dv-yillar">{yil_cipleri(c)}</div></div>
    <div class="dv-ozet"><h4>Bu derste</h4><ul>{"".join(f"<li>{o}</li>" for o in ozet)}</ul></div>
    <div class="dv-icerik"><h4>Dersler</h4><div class="dv-cipler">{cipler}</div></div>
    <div class="dv-kaynak">2021-22* sütunu hatırlanan sorulardan derlendi (kitapçık yok).<span class="pg">{sayfa} / @@TOPLAM@@</span></div>'''
    return slayt(ic, f"ayrac ders-ayrac {SINIF[d]}", f"ders-{SINIF[d]}")


def dagilim(d, sayfa):
    def isi(n):
        return "h0" if n == 0 else "h1" if n == 1 else "h2" if n == 2 else "h3"
    bs = ders_bolumleri(d)
    satir = []
    ytop = {y: 0 for y in YILLAR}
    for b in bs:
        c = sayim(b)
        for y in YILLAR:
            ytop[y] += c[y]
        hucre = "".join(f'<td class="{isi(c[y])}">{c[y] or ""}</td>' for y in YILLAR)
        satir.append(f'<tr><td class="dn">{b["kod"]}</td><td class="db"><a href="#{b["kod"]}">{md(b["baslik"])}</a></td>'
                     f'{hucre}<td class="dt">{sum(c.values())}</td></tr>')
    bas = "".join(f"<th>{yil_etiketi(y)}</th>" for y in YILLAR)
    alt = "".join(f"<td>{ytop[y]}</td>" for y in YILLAR)
    hoca = {}
    for b in bs:
        hoca[b["hoca"]] = hoca.get(b["hoca"], 0) + toplam_soru(b)
    hoca_li = "".join(f"<li><b>{v}</b> soru — {html.escape(kisa_hoca(k))}</li>"
                      for k, v in sorted(hoca.items(), key=lambda kv: -kv[1]))
    sirali = sorted(bs, key=lambda b: -toplam_soru(b))
    verimli = ", ".join(f"<b>{md(b['baslik'])} ({toplam_soru(b)})</b>" for b in sirali[:5] if toplam_soru(b))
    tam = [md(b["baslik"]) for b in bs if all(sayim(b)[y] for y in YILLAR)]
    her_yil = f"<li><b>5/5 yıl</b> soru gelenler: {', '.join(tam)}.</li>" if tam else ""
    bek = bekleyen(d)
    bek_li = (f"<li>PDF'i henüz olmayan derslerden bekleyen: <b>{sum(n for _, n in bek)}</b> soru.</li>" if bek else "")
    ic = f'''
    <header class="hdr"><span class="no">%</span><span class="ttl">{d} · 5 Yılın Soru Dağılımı</span><span class="sp"></span>
      <span class="meta">her hücre = o yıl o dersten çıkan soru</span></header>
    <div class="govde dg" data-max="15">
      <table class="dtab"><colgroup><col class="c-dn"><col class="c-db">{'<col class="c-y">' * len(YILLAR)}<col class="c-t"></colgroup>
        <thead><tr><th></th><th class="db">Ders</th>{bas}<th>Top.</th></tr></thead>
        <tbody>{"".join(satir)}</tbody>
        <tfoot><tr><td></td><td class="db">Toplam</td>{alt}<td class="dt">{sum(ytop.values())}</td></tr></tfoot></table>
      <div class="dg-yan">
        <div class="kart"><h3>Ne anlama geliyor?</h3><ul>
          <li>Kurul sınavında {YILLIK[d]}.</li>
          {f"<li>En verimli dersler: {verimli}.</li>" if verimli else ""}
          {her_yil}
          {bek_li}
        </ul></div>
        <div class="kart"><h3>Hoca bazında (5 yıl)</h3><ul>{hoca_li}</ul></div>
        <div class="not">21-22* sütunu hatırlanan sorulardan derlendi (resmi kitapçık yok).</div>
      </div>
    </div>
    {alt_bant(sayfa, ders=d)}'''
    return slayt(ic, SINIF[d], f"dagilim-{SINIF[d]}")


def en_cok_listesi(d, en_fazla=16):
    """İki veya daha çok yıl çıkmış maddeler (yıl sayısına göre)."""
    liste = []
    for b in ders_bolumleri(d):
        for kartlar in b["slaytlar"]:
            for c in kartlar:
                for m in c["maddeler"]:
                    if len(m["y"]) >= 2:
                        liste.append((m["t"], m["y"], b["kod"]))
    liste.sort(key=lambda x: -len(x[1]))
    return liste[:en_fazla]


def en_cok(d, sayfa, liste):
    li = []
    for i, (t, ys, kod) in enumerate(liste, 1):
        li.append(f'<li><span class="rk">{i}</span><span class="ec-t">{md(t)} {ck_rozet(ys)}'
                  f'<a class="ec-git" href="#{kod}">→ {kod}</a></span></li>')
    yari = (len(li) + 1) // 2
    ic = f'''
    <header class="hdr"><span class="no">★</span><span class="ttl">{d} · En Çok Çıkan Bilgiler</span><span class="sp"></span>
      <span class="meta">2 ve daha fazla yıl sorulanlar · yıl sayısına göre</span></header>
    <div class="govde iki" data-max="16.5"><ol class="ec sut">{"".join(li[:yari])}</ol><ol class="ec sut" start="{yari + 1}">{"".join(li[yari:])}</ol></div>
    {alt_bant(sayfa, ders=d)}'''
    return slayt(ic, SINIF[d], f"encok-{SINIF[d]}")


# ------------------------------------------------------------------ bölüm slaytları
def ayrac(b, sayfa):
    c = sayim(b)
    t = sum(c.values())
    ozet = "".join(f"<li>{md(o)}</li>" for o in b.get("ozet", []))
    saat = f' · {html.escape(b["saat"])}' if b.get("saat") and b["saat"] != "—" else ""
    basliklar = [k["baslik"] for kartlar in b["slaytlar"] for k in kartlar]
    if b["sorular"]:
        basliklar.append("Çıkmış sorular")
    cipler = "".join(f'<span class="dv-cip">{md(x)}</span>' for x in basliklar)
    sayi = (f'<div class="dv-n"><b>{t}</b><span>çıkmış soru<br>son 5 yılda</span></div>' if t
            else '<div class="dv-n sifir"><b>0</b><span>son 5 yılda<br>doğrudan soru yok</span></div>')
    eksik = f'<div class="dv-eksik">⚠ {md(b["eksik"])}</div>' if b.get("eksik") else ""
    ic = f'''
    <div class="dv-bg">{b["kod"][1:]}</div>
    <div class="dv-ust">{buyuk(b["ders"])} · BÖLÜM {b["sira"]} / {b["ders_toplam"]} <span class="yeni">2026-27 PDF</span></div>
    <h1 class="dv-baslik">{md(b["baslik"])}</h1>
    <div class="dv-meta">{html.escape(b["hoca"])} · 2026: {html.escape(b["tarih"])}{saat}</div>
    <div class="dv-istat">{sayi}<div class="dv-yillar">{yil_cipleri(c)}</div></div>
    <div class="dv-ozet"><h4>Bu başlıkta öne çıkanlar</h4><ul>{ozet}</ul></div>
    {eksik}
    <div class="dv-icerik"><h4>Bu bölümde</h4><div class="dv-cipler">{cipler}</div></div>
    <div class="dv-kaynak">Kaynak: {html.escape(b["kaynak"])}<span class="pg">{sayfa} / @@TOPLAM@@</span></div>'''
    return slayt(ic, f"ayrac {SINIF[b['ders']]}", b["kod"])


def icerik_slayti(b, kartlar, sayfa, sira, adet):
    ek = f'<span class="parca">{sira}/{adet}</span>' if adet > 1 else ""
    sutunlar = ikiye_bol(kartlar)
    sinif = "govde iki" if len(sutunlar) == 2 else "govde tek"
    gov = "".join(f'<div class="sut">{"".join(kart_html(c) for c in s)}</div>' for s in sutunlar)
    ic = f'{ust_bant(b, ek)}<div class="{sinif}" data-max="18">{gov}</div>{alt_bant(sayfa, b["kaynak"], b["ders"])}'
    return slayt(ic, f"icerik {SINIF[b['ders']]}")


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
          f'{alt_bant(sayfa, "Resmi cevap anahtarı yok · cevabı 2026-27 PDF’inde olmayanlar “(PDF’te geçmiyor)” notlu", b["ders"])}')
    return slayt(ic, f"soru-slayt {SINIF[b['ders']]}")


# ------------------------------------------------------------------ montaj
def olustur(secili=None, hedef=None):
    global BOLUMLER
    BOLUMLER = icerik.yukle(secili)

    # 1. geçiş: sayfa planı
    on = ["kapak", "kullanim"] + (["icindekiler"] if len(BOLUMLER) >= 2 else [])
    plan = []
    for d in dersler():
        bs = ders_bolumleri(d)
        plan.append(("ders", d))
        if len(bs) >= 2 and sum(toplam_soru(b) for b in bs):
            plan.append(("dagilim", d))
        ec = en_cok_listesi(d)
        if ec:
            plan.append(("encok", (d, ec)))
        for b in bs:
            plan.append(("ayrac", b))
            for i, kartlar in enumerate(b["slaytlar"], 1):
                plan.append(("icerik", (b, kartlar, i, len(b["slaytlar"]))))
            ss = sorulari_sayfala(b["sorular"]) if b["sorular"] else []
            for i, qs in enumerate(ss, 1):
                plan.append(("soru", (b, qs, i, len(ss))))
    baslangic, ders_bas = {}, {}
    for i, (tip, veri) in enumerate(plan, len(on) + 1):
        if tip == "ayrac":
            baslangic[veri["kod"]] = i
        elif tip == "ders":
            ders_bas[veri] = i
    toplam = len(on) + len(plan)

    # 2. geçiş: render
    s = []
    for i, ad in enumerate(on, 1):
        if ad == "kapak":
            s.append(kapak())
        elif ad == "kullanim":
            s.append(kullanim(i))
        else:
            s.append(icindekiler(i, baslangic, ders_bas))
    for i, (tip, veri) in enumerate(plan, len(on) + 1):
        if tip == "ders":
            s.append(ders_ayrac(veri, i, baslangic))
        elif tip == "dagilim":
            s.append(dagilim(veri, i))
        elif tip == "encok":
            s.append(en_cok(veri[0], i, veri[1]))
        elif tip == "ayrac":
            s.append(ayrac(veri, i))
        elif tip == "icerik":
            b, kartlar, sira, adet = veri
            s.append(icerik_slayti(b, kartlar, i, sira, adet))
        else:
            b, qs, sira, adet = veri
            s.append(soru_slayti(b, qs, i, sira, adet))
    assert len(s) == toplam, (len(s), toplam)

    with open(os.path.join(BURASI, "stil.css"), encoding="utf-8") as f:
        css = f.read()
    # Yazı tipleri mutlak adresle: --cikti başka klasöre yazsa da Inter yüklenir ve sığma ölçümü aynı kalır.
    css = css.replace('url("fontlar/', 'url("' + pathlib.Path(BURASI, "fontlar").as_uri() + "/")
    with open(os.path.join(BURASI, "sigdir.js"), encoding="utf-8") as f:
        js = f.read()
    sayfa_html = (f'<!doctype html><html lang="tr"><head><meta charset="utf-8">'
                  f'<title>Komite 1 Hap Bilgi</title><style>{css}</style></head>'
                  f'<body>{"".join(s)}<script>{js}</script></body></html>')
    sayfa_html = sayfa_html.replace("@@TOPLAM@@", str(toplam))
    hedef = hedef or os.path.join(BURASI, "slaytlar.html")
    with open(hedef, "w", encoding="utf-8") as f:
        f.write(sayfa_html)
    print(f"{hedef}: {toplam} slayt")


if __name__ == "__main__":
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("--sadece", help="virgülle modül adları (ör. p02_hasar,f01_giris)")
    ap.add_argument("--cikti", help="HTML çıktı yolu (varsayılan kaynak/slaytlar.html)")
    a = ap.parse_args()
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    secili = a.sadece.split(",") if a.sadece else None
    bilinmeyen = [m for m in secili or [] if not os.path.exists(os.path.join(BURASI, "bolumler", m + ".py"))]
    if bilinmeyen:
        sys.exit(f"bolumler/ altında yok: {', '.join(bilinmeyen)} (modülün DOSYA adını ver, ör. p04_inflamasyon)")
    olustur(secili, a.cikti)
