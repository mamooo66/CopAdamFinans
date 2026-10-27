#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Farmakoloji ilaç zihin haritası: ilaç grubu → alt grup → daha alt grup → ilaçlar (A4 yatay PDF).

Veri: ilac/<KOD>.json (2026-27 ders PDF'lerindeki sınıflamalardan çıkarıldı; yazım: düğüm = {ad, not?, alt?, ilaclar?}).
Kullanım (kaynak/ klasöründen): python3 ilac_haritasi.py → ../Komite1_AI_Notlari_Farmakoloji_Ilac_Haritasi.pdf
"""
import glob
import html
import json
import os
import pathlib
import subprocess
import sys

BURASI = os.path.dirname(os.path.abspath(__file__))

SIRA = [  # (grup, kodlar)
    ("Kan ve pıhtılaşma", ["F12", "F13"]),
    ("Antineoplastik", ["F11"]),
    ("Antibakteriyel kemoterapötikler", ["F15", "F16", "F17", "F26"]),
    ("Antiparaziter ilaçlar · antiseptikler", ["F25", "F19", "F18"]),
    ("Genel farmakolojideki ilaç listeleri", ["F01", "F02", "F03", "F04", "F05", "F06", "F07", "F08", "F09", "F10", "F14"]),
]
YOK = ["Antianemik İlaçlar", "İmmünmodülatörler", "Makrolidler, Linkozamidler ve Amfenikoller", "Beta Laktam Antibiyotikler",
       "Kinolonlar", "Aminoglikozidler", "Tüberküloz ve Lepra İlaçları", "Antifungal İlaçlar", "Antiviral İlaçlar"]

CSS = """
@font-face{font-family:I;src:url("@@F@@/InterPDF-400.ttf");font-weight:400}
@font-face{font-family:I;src:url("@@F@@/InterPDF-600.ttf");font-weight:600}
@font-face{font-family:I;src:url("@@F@@/InterPDF-700.ttf");font-weight:700}
@font-face{font-family:I;src:url("@@F@@/InterPDF-800.ttf");font-weight:800}
*{box-sizing:border-box}
body{font-family:I,sans-serif;color:#10262C;margin:0;font-size:9pt;line-height:1.25}
.sayfa{page-break-before:always;break-before:page}
.kapak h1{font-size:30pt;color:#0B4552;margin:6mm 0 2mm;font-weight:800}
.kapak .alt{font-size:11pt;color:#36535A;margin-bottom:6mm}
.lej{display:flex;gap:4mm;align-items:center;margin:4mm 0;font-size:9.5pt}
.ozet{width:100%;border-collapse:collapse;font-size:9.5pt}
.ozet td,.ozet th{border:1px solid #CFE3E7;padding:1.4mm 2.4mm;text-align:left}
.ozet th{background:#E6F4F6;color:#0B4552}
.ozet tr.g td{background:#0B4552;color:#fff;font-weight:700}
.yok{color:#9A6B10;font-style:italic}
.bas{display:flex;align-items:baseline;gap:3mm;border-bottom:2.5px solid #0B4552;padding-bottom:1.5mm;margin-bottom:3mm}
.bas .kod{background:#0B4552;color:#fff;border-radius:4px;padding:.5mm 2.2mm;font-weight:800;font-size:12pt}
.bas .ad{font-size:15pt;font-weight:800;color:#0B4552}
.bas .pdf{margin-left:auto;font-size:8.5pt;color:#5A7A81}
.n{display:flex;align-items:center;position:relative;margin:1.1mm 0}
.c{display:flex;flex-direction:column;margin-left:5mm;padding-left:4mm;border-left:1.6px solid #7CC3CD;position:relative}
.c::before{content:"";position:absolute;left:-5mm;top:50%;width:5mm;border-top:1.6px solid #7CC3CD}
.c > .n::before,.c > .ilac::before{content:"";position:absolute;left:-4mm;top:50%;width:4mm;border-top:1.6px solid #7CC3CD}
.k{border-radius:2.2mm;padding:1.3mm 2.4mm;font-weight:700;flex:0 0 auto}
.k .not{display:block;font-weight:400;font-style:italic;font-size:7.8pt;opacity:.9;margin-top:.4mm}
.l1{background:#0B4552;color:#fff;width:50mm;font-size:10pt}
.l2{background:#13A3B8;color:#fff;width:46mm}
.l3{background:#BFE9EF;color:#0B3B45;width:42mm}
.l4{background:#E6F4F6;color:#0B3B45;width:38mm;border:1px solid #BFE9EF}
.l1-n{break-inside:avoid;page-break-inside:avoid;margin:2.2mm 0}
.ilac{display:flex;flex-wrap:wrap;gap:1mm;position:relative;max-width:150mm;margin:1mm 0}
.c > .ilac{margin-left:0}
.n > .ilac{margin-left:5mm}
.n > .ilac::before{content:"";position:absolute;left:-5mm;top:50%;width:5mm;border-top:1.6px solid #7CC3CD}
.i{background:#fff;border:1.2px solid #E0457B;color:#7A1236;border-radius:3mm;padding:.5mm 2mm;font-weight:600;font-size:8.6pt}
"""


def e(s):
    return html.escape(str(s))


def dugum(d, seviye):
    etiket = f'<div class="k l{min(seviye, 4)}">{e(d.get("ad", ""))}' + (
        f'<span class="not">{e(d["not"])}</span>' if d.get("not") else "") + "</div>"
    ilac = "".join(f'<span class="i">{e(x)}</span>' for x in d.get("ilaclar") or [])
    ilac_kutu = f'<div class="ilac">{ilac}</div>' if ilac else ""
    cocuk = [dugum(x, seviye + 1) for x in d.get("alt") or []]
    sinif = "n l1-n" if seviye == 1 else "n"
    if cocuk:
        return f'<div class="{sinif}">{etiket}<div class="c">{"".join(cocuk)}{ilac_kutu}</div></div>'
    return f'<div class="{sinif}">{etiket}{ilac_kutu}</div>'


def say(dugumler):
    g = i = 0
    for d in dugumler:
        g += 1
        i += len(d.get("ilaclar") or [])
        a, b = say(d.get("alt") or [])
        g, i = g + a, i + b
    return g, i


def main():
    veri = {}
    for yol in glob.glob(os.path.join(BURASI, "ilac", "*.json")):
        d = json.load(open(yol, encoding="utf-8"))
        veri[d["kod"]] = d
    ozet, sayfalar = [], []
    for grup, kodlar in SIRA:
        var = [k for k in kodlar if k in veri]
        if not var:
            continue
        ozet.append(f'<tr class="g"><td colspan="4">{e(grup)}</td></tr>')
        for k in var:
            d = veri[k]
            g, i = say(d["agac"])
            ozet.append(f'<tr><td>{e(k)}</td><td>{e(d["ders"])}</td><td>{g}</td><td>{i}</td></tr>')
            sayfalar.append(f'<section class="sayfa"><div class="bas"><span class="kod">{e(k)}</span>'
                            f'<span class="ad">{e(d["ders"])}</span><span class="pdf">PDF: {e(d.get("pdf", ""))} · 2026-27</span></div>'
                            f'{"".join(dugum(x, 1) for x in d["agac"])}</section>')
    ozet.append('<tr class="g"><td colspan="4">2026-27 PDF\'i Drive\'da olmayan dersler</td></tr>')
    ozet += [f'<tr><td>—</td><td class="yok">{e(x)}</td><td colspan="2" class="yok">PDF gelince eklenecek</td></tr>' for x in YOK]
    fontlar = pathlib.Path(BURASI, "fontlar").as_uri()
    lej = ('<div class="lej"><span class="k l1">İlaç grubu</span>→<span class="k l2">Alt grup</span>→'
           '<span class="k l3">Daha alt grup</span>→<span class="i">İlaç</span></div>')
    sayfa = (f'<!doctype html><html lang="tr"><head><meta charset="utf-8"><title>Farmakoloji İlaç Haritası</title>'
             f'<style>{CSS.replace("@@F@@", fontlar)}</style></head><body>'
             f'<section class="kapak"><h1>Farmakoloji · İlaç Haritası</h1>'
             f'<div class="alt"><b>Komite 1 AI Notları</b> · Dönem III · 2026-27 · İlaç grupları, alt grupları ve '
             f'ilaçları yalnızca 2026-27 ders PDF\'lerindeki sınıflamalardan, PDF\'teki sırayla alındı.</div>{lej}'
             f'<table class="ozet"><tr><th>Kod</th><th>Ders</th><th>Grup sayısı</th><th>İlaç sayısı</th></tr>'
             f'{"".join(ozet)}</table></section>{"".join(sayfalar)}</body></html>')
    calisma = os.path.join(BURASI, "..", "calisma")
    os.makedirs(calisma, exist_ok=True)
    htm = os.path.join(calisma, "ilac_haritasi.html")
    open(htm, "w", encoding="utf-8").write(sayfa)
    pdf = os.path.normpath(os.path.join(BURASI, "..", "Komite1_AI_Notlari_Farmakoloji_Ilac_Haritasi.pdf"))
    js = ("const {chromium}=require('playwright');const {pathToFileURL}=require('url');(async()=>{"
          "const b=await chromium.launch();const p=await b.newPage();"
          f"await p.goto(pathToFileURL({json.dumps(htm)}).href,{{waitUntil:'load'}});"
          "await p.evaluate(()=>document.fonts.ready);"
          f"await p.pdf({{path:{json.dumps(pdf)},format:'A4',landscape:true,printBackground:true,"
          "displayHeaderFooter:true,headerTemplate:'<span></span>',"
          "footerTemplate:'<div style=\"font-size:7pt;color:#6B8A91;width:100%;text-align:center\">"
          "Komite 1 AI Notları · Farmakoloji İlaç Haritası · <span class=\"pageNumber\"></span>/<span class=\"totalPages\"></span></div>',"
          "margin:{top:'10mm',bottom:'12mm',left:'10mm',right:'10mm'}});await b.close();})();")
    subprocess.run(["node", "-e", js], check=True)
    print(pdf, f"({len(veri)} ders)")


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    main()
