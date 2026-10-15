# -*- coding: utf-8 -*-
"""Ders PDF'i → sayfa işaretli düz metin ("=== s.N ==="). Metni çıkmayan (resim) sayfaları listeler;
istenirse tek tek sayfa resmi basar. PDF'i doğrudan okumak yerine bunu kullan: metin çok daha az token tutar.

Kullanım (kaynak/ klasöründen):
  python3 araclar/pdf_metin.py ../pdf/ders.pdf --cikti ../calisma/ders.txt
  python3 araclar/pdf_metin.py ../pdf/ders.pdf --sayfa 76- --cikti ../calisma/ders_son.txt   (yalnız 76. sayfadan sonrası)
  python3 araclar/pdf_metin.py ../pdf/ders.pdf --resim 12,20-22 --dpi 70 --klasor ../calisma  (sayfa PNG'leri)
Sıra: PyMuPDF (pip install pymupdf) → pypdf (pip install pypdf) → poppler (pdftotext / pdftoppm).
"""

import argparse
import os
import re
import shutil
import subprocess
import sys


def aralik(s, son):
    """'3', '76-', '5-9', '1,4,10-12' → sayfa numaraları (1'den başlar)."""
    sayfalar = []
    for parca in s.split(","):
        parca = parca.strip()
        if not parca:
            continue
        if "-" in parca:
            a, b = parca.split("-", 1)
            sayfalar += range(int(a or 1), int(b or son) + 1)
        else:
            sayfalar.append(int(parca))
    return [p for p in sayfalar if 1 <= p <= son]


def sayfa_sayisi(pdf):
    try:
        import fitz
        with fitz.open(pdf) as d:
            return d.page_count
    except ImportError:
        pass
    try:
        from pypdf import PdfReader
        return len(PdfReader(pdf).pages)
    except ImportError:
        pass
    cikti = subprocess.run(["pdfinfo", pdf], capture_output=True, text=True).stdout
    return int(re.search(r"Pages:\s+(\d+)", cikti).group(1))


def metinler(pdf, sayfalar):
    try:
        import fitz
        with fitz.open(pdf) as d:
            return {p: d[p - 1].get_text("text") for p in sayfalar}
    except ImportError:
        pass
    try:
        from pypdf import PdfReader
        r = PdfReader(pdf)
        return {p: r.pages[p - 1].extract_text() or "" for p in sayfalar}
    except ImportError:
        pass
    if not shutil.which("pdftotext"):
        sys.exit("PDF okuyucu yok: pip install pymupdf  (ya da pypdf / poppler)")
    return {p: subprocess.run(["pdftotext", "-layout", "-f", str(p), "-l", str(p), pdf, "-"],
                              capture_output=True, text=True, encoding="utf-8").stdout for p in sayfalar}


def resim_bas(pdf, sayfalar, dpi, klasor):
    os.makedirs(klasor, exist_ok=True)
    ad = os.path.splitext(os.path.basename(pdf))[0]
    yollar = []
    try:
        import fitz
        with fitz.open(pdf) as d:
            for p in sayfalar:
                yol = os.path.join(klasor, f"{ad}_s{p}.png")
                d[p - 1].get_pixmap(dpi=dpi).save(yol)
                yollar.append(yol)
        return yollar
    except ImportError:
        pass
    if not shutil.which("pdftoppm"):
        sys.exit("Resim için PyMuPDF gerekli: pip install pymupdf")
    for p in sayfalar:
        on = os.path.join(klasor, f"{ad}_s{p}")
        subprocess.run(["pdftoppm", "-f", str(p), "-l", str(p), "-r", str(dpi), "-png", "-singlefile", pdf, on], check=True)
        yollar.append(on + ".png")
    return yollar


def temizle(t):
    t = "\n".join(s.rstrip() for s in t.replace("\r", "").split("\n"))
    return re.sub(r"\n{3,}", "\n\n", t).strip()


def main():
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("pdf")
    ap.add_argument("--sayfa", default="1-", help="ör. 76-  ya da 1-40  ya da 3,5,9 (varsayılan: hepsi)")
    ap.add_argument("--cikti", help="metin dosyası (varsayılan: PDF'in yanında .txt)")
    ap.add_argument("--resim", help="PNG basılacak sayfalar (ör. 12,20-22); metin çıkarılmaz")
    ap.add_argument("--dpi", type=int, default=70)
    ap.add_argument("--klasor", help="PNG klasörü (varsayılan: PDF'in klasörü)")
    a = ap.parse_args()

    son = sayfa_sayisi(a.pdf)
    if a.resim:
        for yol in resim_bas(a.pdf, aralik(a.resim, son), a.dpi, a.klasor or os.path.dirname(os.path.abspath(a.pdf))):
            print(yol)
        return

    sayfalar = aralik(a.sayfa, son)
    if not sayfalar:
        sys.exit(f"PDF {son} sayfa; istenen aralık ({a.sayfa}) boş")
    m = metinler(a.pdf, sayfalar)
    hedef = a.cikti or os.path.splitext(a.pdf)[0] + ".txt"
    os.makedirs(os.path.dirname(os.path.abspath(hedef)), exist_ok=True)
    bos = []
    with open(hedef, "w", encoding="utf-8") as f:
        for p in sayfalar:
            t = temizle(m[p])
            if len(t) < 40:
                bos.append(p)
            f.write(f"=== s.{p} ===\n{t}\n\n")
    toplam = sum(len(temizle(v)) for v in m.values())
    print(f"{hedef}: PDF {son} sayfa · yazılan s.{sayfalar[0]}-{sayfalar[-1]} · {toplam} karakter")
    if bos:
        print(f"metni (neredeyse) olmayan sayfalar — muhtemelen resim/şema: {', '.join(map(str, bos))}")


if __name__ == "__main__":
    main()
