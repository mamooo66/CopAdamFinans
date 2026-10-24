#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Komite 1 AI Notları: her ders için ayrı PDF basar.

Kullanım (kaynak/ klasöründen):
  python3 bas.py patoloji          → ../Komite1_AI_Notlari_Patoloji.pdf
  python3 bas.py p c a             → birden çok ders (harf ya da ad)
  python3 bas.py                   → modülü olan bütün dersler
  python3 bas.py pediatri --olc    → PDF basmadan yalnız sığma raporu
Ara HTML: ../calisma/<Ders>.html
"""
import os
import subprocess
import sys

BURASI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, BURASI)
import icerik  # noqa: E402
import olustur  # noqa: E402


def bas(k, olc=False):
    ad = icerik.DOSYA[k]
    calisma = os.path.join(BURASI, "..", "calisma")
    os.makedirs(calisma, exist_ok=True)
    htm = os.path.join(calisma, ad + ".html")
    if not icerik.yukle(ders=k):
        print(f"{icerik.AD[k]}: modül yok, atlandı")
        return
    olustur.olustur(None, htm, k)
    pdf = os.path.normpath(os.path.join(BURASI, "..", f"Komite1_AI_Notlari_{ad}.pdf"))
    komut = ["node", os.path.join(BURASI, "pdf.cjs"), "--html", htm] + (["--olc"] if olc else ["--pdf", pdf])
    r = subprocess.run(komut, capture_output=True, text=True, encoding="utf-8")
    satirlar = r.stdout.strip().splitlines()
    for x in satirlar:
        if "<<<" in x:
            print("   ", x)
    print("   ", satirlar[-1] if satirlar else r.stderr[-800:])
    if r.returncode:
        sys.exit(r.returncode)


if __name__ == "__main__":
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    olc = "--olc" in sys.argv
    secim = [a for a in sys.argv[1:] if a != "--olc"]
    for k in ([icerik.ders_kodu(a) for a in secim] or [k for k, _ in icerik.DERSLER]):
        bas(k, olc)
