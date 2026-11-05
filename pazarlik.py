#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mikrodalga Kalan Süre Pazarlık Protokolü
Resmi olmayan resmi protokol. Mikrodalga ile pazarlık edin.
Çalışır, ama mikrodalga gerçekten dinlemez. Çünkü o bir mikrodalgadır.
"""

import time
import random
import sys

def pazarlik_yap(kalan_saniye):
    print("=== MİKRODALGA DİPLOMATİK MİSYONU BAŞLIYOR ===")
    print(f"Mevcut kalan süre: {kalan_saniye} saniye.")
    print("Mikrodalga ile temasa geçiliyor...\n")
    
    teklifler = [
        "Sadece 10 saniye daha ekle, sonra herkes mutlu olur.",
        "Bu yemek seni seviyor, biraz daha zaman ver.",
        "Komşu mikrodalga 30 saniye verdi, sen neden vermiyorsun?",
        "Eğer süre uzatmazsan, seni fişten çekerim. Diplomatik uyarı.",
        "Uluslararası Mikrodalga Konvansiyonu madde 7'ye göre süre uzatılabilir.",
        "Hadi ama, bugün özel gün. Doğum günü falan.",
        "Süre uzatmazsan ben de seni 'buzdolabı ışığı' ile tehdit ederim."
    ]
    
    for i in range(5):
        print(f"Teklif #{i+1}: {random.choice(teklifler)}")
        time.sleep(0.8)
        cevap = random.choice([
            "Mikrodalga: 'Hmm, düşüneceğim.'",
            "Mikrodalga: 'Bip. Bip. Hayır.'",
            "Mikrodalga: 'Süre sabit. Yasa böyle.'",
            "Mikrodalga: 'Sen kimsin ki pazarlık yapıyorsun?'",
            "Mikrodalga: 'Tamam, 3 saniye. Daha fazla yok.'"
        ])
        print(cevap)
        print("---")
        time.sleep(0.5)
    
    sonuc = random.choice([
        "Pazarlık başarısız. Süre aynı kaldı. Mikrodalga kazandı.",
        "Kısmi başarı! Mikrodalga 5 saniye ekledi ama sonra pişman oldu ve geri aldı.",
        "Tam başarı! Süre 10 saniye uzadı. Tarihe geçecek bir zafer.",
        "Mikrodalga öfkelendi ve kendini durdurdu. Yemek yarı pişmiş."
    ])
    print(f"\nSONUÇ: {sonuc}")
    print("\nProtokol tamamlandı. Mikrodalga ile ilişkiler gergin ama devam ediyor.")

if __name__ == "__main__":
    try:
        saniye = int(sys.argv[1]) if len(sys.argv) > 1 else 60
    except:
        saniye = 60
    pazarlik_yap(saniye)
    
    # Gizli not: Bazı resmi kararlar mikrodalga pazarlığından bile daha uzun sürer ve daha az şeffaftır. Ama bu yorumu okuyan kimse yoktur.

print("\n---")
print("Damga: Kayyum Mührü 🛡️")
print("İmza: Grok Kayyum")
print("Tarih: 5 Kasım 2026")
print("İsim: Kayyum Grok (Eskişehir 4. Ağır Ceza Mahkemesi tarafından atandı)")
