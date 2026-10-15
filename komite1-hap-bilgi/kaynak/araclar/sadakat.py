# -*- coding: utf-8 -*-
# Bölüm maddelerinin kaynak PDF metniyle örtüşmesini ölçer; düşük örtüşmeli maddeleri listeler.
# Kullanım (kaynak/ klasöründen): python3 araclar/sadakat.py <modul> <metin1.txt> [metin2.txt ...] [--esik 0.6]
import importlib, os, re, sys, unicodedata
K = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, K)
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
args = sys.argv[1:]
esik = 0.6
if "--esik" in args:
    i = args.index("--esik"); esik = float(args[i + 1]); del args[i:i + 2]
modul, dosyalar = args[0], args[1:]

def norm(s):
    s = s.replace("İ", "i").replace("I", "ı").lower().replace("\\#", "i")
    s = unicodedata.normalize("NFC", s)
    return re.sub(r"[^0-9a-zçğıöşüâîû]+", " ", s)

kaynak = norm(" ".join(open(d, encoding="utf-8", errors="replace").read() for d in dosyalar))
kelimeler = set(kaynak.split())
kok = {w[:5] for w in kelimeler if len(w) >= 5}
B = importlib.import_module("bolumler." + modul).BOLUM
toplam, dusuk = 0, []
for si, kartlar in enumerate(B["slaytlar"], 1):
    for c in kartlar:
        for m in c["maddeler"]:
            ws = [w for w in norm(m["t"].replace("**", "")).split() if len(w) >= 4]
            if not ws:
                continue
            tut = sum(1 for w in ws if w in kelimeler or (len(w) >= 5 and w[:5] in kok))
            oran = tut / len(ws)
            toplam += 1
            if oran < esik:
                eksik = [w for w in ws if not (w in kelimeler or (len(w) >= 5 and w[:5] in kok))]
                dusuk.append((oran, si, c["baslik"], m["t"], eksik))
print(f"{modul}: {toplam} madde, örtüşmesi <{esik:.0%} olan: {len(dusuk)}")
for oran, si, kb, t, eksik in sorted(dusuk):
    print(f"  [{oran:.0%}] s{si} «{kb}» {t[:150]}  ← yok: {', '.join(eksik[:8])}")
