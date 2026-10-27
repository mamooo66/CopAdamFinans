#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Farmakoloji konu haritası: her dersin üst başlık → alt başlık tablosu (A4 PDF).

Veri: harita/<KOD>.json (ders PDF'lerinin kendi başlıklarından çıkarıldı).
Kullanım (kaynak/ klasöründen): python3 harita.py  → ../Komite1_AI_Notlari_Farmakoloji_Konu_Haritasi.pdf
"""
import glob
import html
import json
import os
import pathlib
import subprocess
import sys

BURASI = os.path.dirname(os.path.abspath(__file__))

# (grup, [(kod, ders adı — yalnız PDF'i olmayanlar için)])
GRUPLAR = [
    ("Genel Farmakoloji", ["F01", "F02", "F03", "F04", "F05", "F06", "F07", "F08", "F09", "F10", "F14"]),
    ("Kan ve Pıhtılaşma İlaçları", ["F12", "F13", ("—", "Antianemik İlaçlar", "Doç. Dr. Oruç Yunusoğlu · 9 Ekim")]),
    ("Antineoplastik ve İmmünmodülatör İlaçlar", ["F11", ("—", "İmmünmodülatörler", "Prof. Dr. Akif Hakan Kurt · 14 Ekim")]),
    ("Kemoterapötikler (Antibakteriyel İlaçlar)", [
        "F15", "F16", "F17", "F26",
        ("—", "Makrolidler, Linkozamidler ve Amfenikoller", "Prof. Dr. Akif Hakan Kurt · 19 Ekim"),
        ("—", "Beta Laktam Antibiyotikler", "Prof. Dr. Akif Hakan Kurt · 20 Ekim"),
        ("—", "Kinolonlar", "Prof. Dr. Akif Hakan Kurt · 26 Ekim"),
        ("—", "Aminoglikozidler", "Prof. Dr. Akif Hakan Kurt · 26 Ekim"),
        ("—", "Tüberküloz ve Lepra Tedavisinde Kullanılan İlaçlar", "Doç. Dr. Oruç Yunusoğlu · 23 Ekim")]),
    ("Antifungal, Antiviral ve Antiparaziter İlaçlar · Antiseptikler", [
        ("—", "Antifungal İlaçlar", "Prof. Dr. Akif Hakan Kurt · 27 Ekim"),
        ("—", "Antiviral İlaçlar", "Doç. Dr. Oruç Yunusoğlu · 21 Ekim"),
        "F25", "F19", "F18"]),
]

CSS = """
@font-face{font-family:I;src:url("@@F@@/InterPDF-400.ttf");font-weight:400}
@font-face{font-family:I;src:url("@@F@@/InterPDF-600.ttf");font-weight:600}
@font-face{font-family:I;src:url("@@F@@/InterPDF-700.ttf");font-weight:700}
@font-face{font-family:I;src:url("@@F@@/InterPDF-800.ttf");font-weight:800}
@page{size:A4;margin:14mm 12mm 14mm 12mm}
*{box-sizing:border-box}
body{font-family:I,sans-serif;color:#13232A;font-size:10.2pt;line-height:1.35;margin:0}
h1{font-size:22pt;margin:0 0 2mm;color:#0B4552;font-weight:800;letter-spacing:-.01em}
.ust{font-size:9pt;color:#4B6B73;margin-bottom:5mm}
.ust b{color:#0B4552}
h2{font-size:13.5pt;color:#fff;background:#0B4552;border-radius:6px;padding:2.2mm 4mm;margin:7mm 0 3mm;
   page-break-after:avoid;break-after:avoid}
h3{font-size:11.5pt;margin:5mm 0 1.6mm;color:#0B4552;page-break-after:avoid;break-after:avoid}
h3 .kod{display:inline-block;background:#13A3B8;color:#fff;border-radius:4px;padding:0 1.8mm;margin-right:2mm;font-size:9.5pt}
h3 .hoca{font-weight:400;color:#4B6B73;font-size:9pt;margin-left:2mm}
table{width:100%;border-collapse:collapse;margin-bottom:2mm}
td,th{border:1px solid #CFE3E7;vertical-align:top;padding:1.6mm 2.4mm}
th{background:#E6F4F6;color:#0B4552;text-align:left;font-size:9pt}
td.ub{width:34%;font-weight:700;color:#0B3B45;background:#F5FBFC}
td.ub .s{display:block;font-weight:400;color:#6B8A91;font-size:8.3pt}
td ul{margin:0;padding-left:4.5mm}
td li{margin:.4mm 0}
td li ul{padding-left:4mm;color:#36535A}
tr{page-break-inside:avoid;break-inside:avoid}
.ozet td{font-size:9.4pt}
.ozet td.k{width:13mm;text-align:center;font-weight:800;color:#0B4552}
.yok{color:#9A6B10;font-style:italic}
.not{font-size:8.6pt;color:#4B6B73;margin-top:5mm}
"""


def e(s):
    return html.escape(str(s))


def alt_html(alt):
    li = []
    for a in alt or []:
        if isinstance(a, dict):
            ic = f"<ul>{''.join(f'<li>{e(x)}</li>' for x in a.get('alt', []))}</ul>" if a.get("alt") else ""
            li.append(f"<li>{e(a.get('t', ''))}{ic}</li>")
        else:
            li.append(f"<li>{e(a)}</li>")
    return f"<ul>{''.join(li)}</ul>" if li else ""


def main():
    veri = {}
    for yol in glob.glob(os.path.join(BURASI, "harita", "*.json")):
        d = json.load(open(yol, encoding="utf-8"))
        veri[d["kod"]] = d
    ozet, govde = [], []
    for grup, dersler in GRUPLAR:
        govde.append(f"<h2>{e(grup)}</h2>")
        for x in dersler:
            if isinstance(x, tuple) or x not in veri:
                ad, bilgi = (x[1], x[2]) if isinstance(x, tuple) else (x, "")
                ozet.append(f'<tr><td>{e(grup)}</td><td class="k">—</td><td>{e(ad)}</td>'
                            f'<td class="yok">2026-27 PDF\'i Drive\'da yok · {e(bilgi)}</td></tr>')
                govde.append(f'<h3><span class="kod">—</span>{e(ad)}<span class="hoca">{e(bilgi)}</span></h3>'
                             f'<p class="yok">Bu dersin 2026-27 PDF\'i Drive\'da yok; PDF gelince haritası eklenecek.</p>')
                continue
            d = veri[x]
            ozet.append(f'<tr><td>{e(grup)}</td><td class="k">{e(x)}</td><td>{e(d["ders"])}</td>'
                        f'<td>{", ".join(e(b["baslik"]) for b in d["basliklar"])}</td></tr>')
            satir = "".join(
                f'<tr><td class="ub">{e(b["baslik"])}'
                + (f'<span class="s">slayt {e(b["sayfa"])}</span>' if b.get("sayfa") else "")
                + f'</td><td>{alt_html(b.get("alt"))}</td></tr>' for b in d["basliklar"])
            govde.append(f'<h3><span class="kod">{e(x)}</span>{e(d["ders"])}<span class="hoca">{e(d.get("hoca", ""))}'
                         f' · PDF: {e(d.get("pdf", ""))}</span></h3>'
                         f'<table><tr><th>Üst başlık</th><th>Alt başlıklar</th></tr>{satir}</table>')
    fontlar = pathlib.Path(BURASI, "fontlar").as_uri()
    sayfa = (f'<!doctype html><html lang="tr"><head><meta charset="utf-8"><title>Farmakoloji Konu Haritası</title>'
             f'<style>{CSS.replace("@@F@@", fontlar)}</style></head><body>'
             f'<h1>Farmakoloji · Konu Haritası</h1>'
             f'<div class="ust"><b>Komite 1 AI Notları</b> · Dönem III · 2026-27 · Her dersin üst ve alt başlıkları '
             f'o dersin 2026-27 PDF\'indeki başlıklardan, PDF\'teki sırayla alındı. Kodlar Farmakoloji notlarındaki '
             f'bölüm kodlarıdır (F12 → notlarda F12).</div>'
             f'<h2>Özet: hangi ders hangi grupta</h2><table class="ozet"><tr><th>Grup</th><th>Kod</th><th>Ders</th>'
             f'<th>Üst başlıklar</th></tr>{"".join(ozet)}</table>'
             f'{"".join(govde)}'
             f'<p class="not">Gruplar (Genel Farmakoloji, Kemoterapötikler …) dersleri bir arada görmek için '
             f'eklendi; ders içi başlıklar yalnız PDF\'lerden.</p></body></html>')
    calisma = os.path.join(BURASI, "..", "calisma")
    os.makedirs(calisma, exist_ok=True)
    htm = os.path.join(calisma, "harita_farmakoloji.html")
    open(htm, "w", encoding="utf-8").write(sayfa)
    pdf = os.path.normpath(os.path.join(BURASI, "..", "Komite1_AI_Notlari_Farmakoloji_Konu_Haritasi.pdf"))
    js = ("const {chromium}=require('playwright');const {pathToFileURL}=require('url');(async()=>{"
          "const b=await chromium.launch();const p=await b.newPage();"
          f"await p.goto(pathToFileURL({json.dumps(htm)}).href,{{waitUntil:'load'}});"
          "await p.evaluate(()=>document.fonts.ready);"
          f"await p.pdf({{path:{json.dumps(pdf)},format:'A4',printBackground:true,"
          "displayHeaderFooter:true,headerTemplate:'<span></span>',"
          "footerTemplate:'<div style=\"font-size:7pt;color:#6B8A91;width:100%;text-align:center\">"
          "Komite 1 AI Notları · Farmakoloji Konu Haritası · <span class=\"pageNumber\"></span>/<span class=\"totalPages\"></span></div>',"
          "margin:{top:'14mm',bottom:'14mm',left:'12mm',right:'12mm'}});await b.close();})();")
    subprocess.run(["node", "-e", js], check=True)
    print(pdf, f"({len(veri)} dersin haritası)")


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    main()
