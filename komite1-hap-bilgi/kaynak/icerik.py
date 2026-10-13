# -*- coding: utf-8 -*-
"""Destenin içeriği: bolumler/ klasöründeki modüller.

KAYNAK KURALI: Hap bilgiler YALNIZCA bu dönemin (2026-27) ders PDF'lerinden yazılır.
Eski klasör, geçmiş yılların ders notları ve kitaplar kullanılmaz.

Her modül bir ders (bölüm) tanımlar: bolumler/pNN_*.py = Patoloji, bolumler/fNN_*.py = Farmakoloji.
Sıra dosya adındaki numaraya göredir. Modül, BOLUM = dict(key, baslik, hoca, tarih, saat, kaynak,
ozet, slaytlar, sorular) tanımlar (yazım: yardim.py).
"""

import glob
import importlib
import os
import sys

BURASI = os.path.dirname(os.path.abspath(__file__))
if BURASI not in sys.path:
    sys.path.insert(0, BURASI)

from yardim import YILLAR  # noqa: E402,F401

DERSLER = [("p", "Patoloji"), ("f", "Farmakoloji")]


def yukle(secili=None):
    """secili: modül adları (ör. ["p02_hasar"]); None ise hepsi."""
    bolumler = []
    for onek, ders in DERSLER:
        yollar = sorted(glob.glob(os.path.join(BURASI, "bolumler", onek + "[0-9][0-9]_*.py")))
        for yol in yollar:
            ad = os.path.splitext(os.path.basename(yol))[0]
            if secili and ad not in secili:
                continue
            b = dict(importlib.import_module("bolumler." + ad).BOLUM)
            b["modul"] = ad
            b["ders"] = ders
            b["kod"] = onek.upper() + ad[1:3]
            bolumler.append(b)
    for b in bolumler:  # ayraçtaki "BÖLÜM x / y" için ders içi sıra
        ayni = [x for x in bolumler if x["ders"] == b["ders"]]
        b["sira"], b["ders_toplam"] = ayni.index(b) + 1, len(ayni)
    return bolumler
