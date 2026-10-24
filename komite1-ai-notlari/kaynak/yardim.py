# -*- coding: utf-8 -*-
"""Bölüm modüllerinin kullandığı yazım yardımcıları.

  B(metin, y="23-24 25-26", tuzak="...", g="İÇ HAST. 23-24", lvl=1)   bir madde
      y     : bu bilginin AYNI dersin sorusu olarak çıktığı yıllar (kırmızı ÇIKMIŞ etiketi)
      tuzak : sınavda bu bilgi yanlış ifade (çeldirici) olarak sorulduysa o yanlış ifade
      g     : başka bir dersin sorusunda geçtiyse gri etiket metni (ör. "İÇ HAST. 23-24")
      lvl   : 1 = alt madde (girintili)
  C(başlık, [B, ...])                                                 bir kart
  Q(yıl, soru_no, kök, cevap, not, n=1, ref=False)                    çıkmış soru özeti
      n   : hatırlanan birleşik maddelerde kaç soruyu temsil ettiği
      ref : başka bölümde sayılan sorunun çapraz atfı (sayıma girmez)
Metin içinde **kalın** kullanılabilir.
"""

YILLAR = ["21-22", "22-23", "23-24", "24-25", "25-26"]


def B(t, y=None, tuzak=None, g=None, lvl=0):
    return dict(t=t, y=(y.split() if y else []), tuzak=tuzak, g=g, lvl=lvl)


def C(baslik, maddeler, ikon=None):
    return dict(baslik=baslik, maddeler=maddeler, ikon=ikon)


def Q(y, no, kok, cevap, not_=None, n=1, ref=False):
    return dict(y=y, no=no, kok=kok, cevap=cevap, not_=not_, n=n, ref=ref)
