# -*- coding: utf-8 -*-
"""Kapsam kontrolü: PDF'in hangi sayfaları modülde karşılık bulmamış? (kırpılan/atlanan sayfaları bulur)

Kullanım (kaynak/ klasöründen): python3 araclar/kapsam.py <modul> <metin.txt> [metin2.txt ...] [--esik 0.4]
metin.txt = araclar/pdf_metin.py çıktısı ("=== s.N ===" işaretli). Her içerik sayfasının anlamlı sözcüklerinin
ne kadarının modülde geçtiğini ölçer; eşiğin altındaki sayfaları listeler. Listedeki her sayfa ya modüle eklenmeli
ya da gerçekten içeriksiz olmalı (başlık, amaçlar, teşekkür, kaynakça, yalnız fotoğraf).
"""
import importlib
import os
import re
import sys
import unicodedata

K = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, K)
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

DURAK = set("""olarak ancak kadar sonra daha gibi ile için olan veya ayrıca genellikle özellikle arasında nedeniyle
şeklinde sonucu olabilir bulunur yapılır edilir olur olması olduğu olduğunu ettiği eden etmek etkiler ilgili göre
yani hangi bunlar bunun şöyle ise ki her hem bazı birçok diğer diye kendi içinde üzerinde tarafından sırasında
yüksek düşük önemli fazla az""".split())


def norm(s):
    s = s.replace("İ", "i").replace("I", "ı").lower().replace("\\#", "i")
    s = unicodedata.normalize("NFC", s)
    return re.sub(r"[^0-9a-zçğıöşüâîû]+", " ", s)


def sozcukler(s):
    return {w for w in norm(s).split() if len(w) >= 5 and w not in DURAK and not w.isdigit()}


def main():
    args = sys.argv[1:]
    esik = 0.4
    if "--esik" in args:
        i = args.index("--esik")
        esik = float(args[i + 1])
        del args[i:i + 2]
    modul, dosyalar = args[0], args[1:]
    B = importlib.import_module("bolumler." + modul).BOLUM
    parca = [B.get("baslik", "")] + list(B.get("ozet", []))
    for kartlar in B["slaytlar"]:
        for c in kartlar:
            parca.append(c["baslik"])
            for m in c["maddeler"]:
                parca += [m["t"], m["tuzak"] or ""]
    for q in B["sorular"]:
        parca += [q["kok"], q["cevap"], q["not_"] or ""]
    mod = sozcukler(" ".join(parca).replace("**", ""))
    kok = {w[:5] for w in mod}
    dusuk, olcum = [], []
    for d in dosyalar:
        metin = open(d, encoding="utf-8", errors="replace").read()
        for m in re.finditer(r"=== s\.(\d+) ===\n(.*?)(?=\n=== s\.|\Z)", metin, re.S):
            n, t = int(m.group(1)), m.group(2)
            ws = sozcukler(t)
            if len(ws) < 6:
                continue
            oran = sum(1 for w in ws if w in mod or w[:5] in kok) / len(ws)
            olcum.append(oran)
            if oran < esik:
                eksik = sorted(w for w in ws if not (w in mod or w[:5] in kok))
                dusuk.append((oran, os.path.basename(d), n, " ".join(t.split())[:110], eksik[:10]))
    if not olcum:
        sys.exit("ölçülecek sayfa yok (metin dosyası '=== s.N ===' işaretli mi?)")
    olcum.sort()
    print(f"{modul}: {len(olcum)} içerik sayfası · ortanca kapsam {olcum[len(olcum) // 2]:.0%} · "
          f"eşik {esik:.0%} altı: {len(dusuk)} sayfa")
    for oran, d, n, bas, eksik in sorted(dusuk, key=lambda x: (x[1], x[2])):
        print(f"  [{oran:.0%}] {d} s.{n}: {bas}  ← eksik: {', '.join(eksik)}")


if __name__ == "__main__":
    main()
