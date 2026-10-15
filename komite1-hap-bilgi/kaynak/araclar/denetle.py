# -*- coding: utf-8 -*-
"""Bölüm modüllerini denetler: soru tekrarları, hiçbir yere konmamış sorular, rozet-soru tutarlılığı, slayt yoğunluğu.

Kullanım (kaynak/ klasöründen): python3 araclar/denetle.py
Soru listesi ../sorular/*_cikmis.md'den okunur; her numaralı soru ya bir bölümde ya da cikmis_*.py BEKLEYEN'de olmalı.
"""
import os
import re
import sys

K = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SORULAR = os.path.join(os.path.dirname(K), "sorular")
sys.path.insert(0, K)
import icerik  # noqa: E402
from cikmis_patoloji import BEKLEYEN as BP  # noqa: E402
try:
    from cikmis_farmakoloji import BEKLEYEN as BF  # noqa: E402
except ImportError:
    BF = {}

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def tum_sorular(md):
    ids = []
    for L in open(md, encoding="utf-8"):
        m = re.match(r"- \*\*20(\d\d)-(\d\d)(\*)? ([SH])(\d+)\.\*\*", L)
        if m:
            ids.append((f"{m.group(1)}-{m.group(2)}", m.group(4), int(m.group(5))))
    return ids


bolumler = icerik.yukle()
ders_ids = {"Patoloji": tum_sorular(os.path.join(SORULAR, "patoloji_cikmis.md")),
            "Farmakoloji": tum_sorular(os.path.join(SORULAR, "farmakoloji_cikmis.md"))}
for ders, bek in (("Patoloji", BP), ("Farmakoloji", BF)):
    bs = [b for b in bolumler if b["ders"] == ders]
    sahip = {}
    print(f"\n######## {ders}: {len(bs)} bölüm")
    for b in bs:
        sl = b["slaytlar"]
        madde = sum(len(c["maddeler"]) for k in sl for c in k)
        rozet = sum(1 for k in sl for c in k for m in c["maddeler"] if m["y"])
        kr = [sum(len(m["t"]) + len(m["tuzak"] or "") for c in k for m in c["maddeler"]) for k in sl]
        qs = [q for q in b["sorular"] if not q["ref"]]
        pdfte_yok = sum(1 for q in qs if q["not_"] and "PDF'te geçmiyor" in q["not_"])
        qyil = {q["y"] for q in b["sorular"]}
        rozet_yillari = {y for k in sl for c in k for m in c["maddeler"] for y in m["y"]}
        sorunsuz = rozet_yillari - qyil
        print(f"{b['kod']} {b['key']:<16} slayt={len(sl):2d} madde={madde:3d} rozet={rozet:3d} soru={len(qs):2d} "
              f"pdfte_yok={pdfte_yok:2d} kr/slayt max={max(kr) if kr else 0}"
              + (f"  ⚠ sorusuz rozet yılı: {sorted(sorunsuz)}" if sorunsuz else "")
              + ("  ⚠ eksik (yarım ders)" if b.get("eksik") else ""))
        for q in qs:
            anahtar = (q["y"], q["no"]) if q["no"] else (q["y"], "H", q["kok"][:30])
            sahip.setdefault(anahtar, []).append(b["kod"])
    tekrar = {k: v for k, v in sahip.items() if len(v) > 1}
    if tekrar:
        print("TEKRAR:", tekrar)
    numarali = {(y, n) for (y, t, n) in ders_ids[ders] if t == "S"}
    atanan = {k for k in sahip if len(k) == 2}
    bek_ids = set()
    for v in bek.values():
        for q in v["sorular"]:
            if q["no"] and not q["ref"]:
                bek_ids.add((q["y"], q["no"]))
    cift = sorted(atanan & bek_ids)
    if cift:
        print("  hem bölümde hem BEKLEYEN'de:", cift)
    eksik = sorted(numarali - atanan - bek_ids)
    print(f"numaralı soru: {len(numarali)} · bölümlerde: {len(atanan & numarali)} · bekleyen: {len(bek_ids & numarali)}"
          f" · HİÇBİR YERDE YOK: {len(eksik)}")
    if eksik:
        print("  ", eksik)
    fazla = sorted(atanan - numarali)
    if fazla:
        print("  listede olmayan numara:", fazla)
