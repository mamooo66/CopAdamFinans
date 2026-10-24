# -*- coding: utf-8 -*-
"""Notların içeriği: bolumler/ klasöründeki modüller.

KAYNAK KURALI: Notlar YALNIZCA bu dönemin (2026-27) ders PDF'lerinden yazılır.
Eski klasör, geçmiş yılların ders notları ve kitaplar kullanılmaz.

Her modül bir ders saati/konusu (bölüm) tanımlar; dosya adının ilk harfi dersi gösterir:
p Patoloji · c Pediatri · a Aile Hekimliği · e Enfeksiyon Hastalıkları · f Farmakoloji · d Dahiliye · n Nükleer Tıp.
Sıra dosya adındaki numaraya göredir (p05_iyilesme.py → P05). Her ders ayrı PDF olarak basılır.
Modül, BOLUM = dict(key, baslik, hoca, tarih, saat, kaynak, ozet, slaytlar, sorular) tanımlar (yazım: yardim.py).
"""

import glob
import importlib
import os
import sys

BURASI = os.path.dirname(os.path.abspath(__file__))
if BURASI not in sys.path:
    sys.path.insert(0, BURASI)

from yardim import YILLAR  # noqa: E402,F401

DERSLER = [("p", "Patoloji"), ("c", "Pediatri"), ("a", "Aile Hekimliği"), ("e", "Enfeksiyon Hastalıkları"),
           ("f", "Farmakoloji"), ("d", "Dahiliye"), ("n", "Nükleer Tıp")]
DOSYA = {"p": "Patoloji", "c": "Pediatri", "a": "Aile_Hekimligi", "e": "Enfeksiyon", "f": "Farmakoloji",
         "d": "Dahiliye", "n": "Nukleer_Tip"}
CIKMIS = {"p": "cikmis_patoloji", "c": "cikmis_pediatri", "a": "cikmis_aile", "e": "cikmis_enfeksiyon",
          "f": "cikmis_farmakoloji", "d": "cikmis_dahiliye", "n": "cikmis_nukleer"}
AD = dict(DERSLER)


def ders_kodu(s):
    """'p', 'patoloji', 'Aile Hekimliği', 'aile_hekimligi' … → ders harfi."""
    s = (s or "").strip()
    if s.lower() in AD:
        return s.lower()
    tr = str.maketrans("çğıİöşüÇĞÖŞÜ", "cgiiosucgosu")
    n = s.translate(tr).lower().replace(" ", "_")
    n = {"pediyatri": "pediatri", "cocuk": "pediatri", "ic_hastaliklari": "dahiliye", "enfeksiyon": "enfeksiyon"}.get(n, n)
    for k, ad in DERSLER:
        if n in (ad.translate(tr).lower().replace(" ", "_"), DOSYA[k].lower()) or ad.translate(tr).lower().startswith(n):
            return k
    raise SystemExit(f"bilinmeyen ders: {s} (seçenekler: {', '.join(k + '=' + a for k, a in DERSLER)})")


def yukle(secili=None, ders=None):
    """secili: modül adları (ör. ["p02_hasar"]); ders: ders harfi. İkisi de None ise hepsi."""
    bolumler = []
    for onek, ad_ in DERSLER:
        if ders and onek != ders:
            continue
        yollar = sorted(glob.glob(os.path.join(BURASI, "bolumler", onek + "[0-9][0-9]_*.py")))
        for yol in yollar:
            ad = os.path.splitext(os.path.basename(yol))[0]
            if secili and ad not in secili:
                continue
            b = dict(importlib.import_module("bolumler." + ad).BOLUM)
            b["modul"] = ad
            b["ders"] = ad_
            b["kod"] = onek.upper() + ad[1:3]
            bolumler.append(b)
    for b in bolumler:  # ayraçtaki "BÖLÜM x / y" için ders içi sıra
        ayni = [x for x in bolumler if x["ders"] == b["ders"]]
        b["sira"], b["ders_toplam"] = ayni.index(b) + 1, len(ayni)
    return bolumler
