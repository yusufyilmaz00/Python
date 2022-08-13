import random

import time

print("""***************************
Sayı Tahmin Oyunu

1 ile 50 arasında bir sayı tahmin edin

***************************
""")


rastgele_sayı = (random.randint(1,50))
tahmin_hak= 7
while True:
    tahmin= int(input("Tahmininizi giriniz: "))
    if tahmin<rastgele_sayı:
        print("Bilgiler sorgulanıyor...")
        time.sleep(1)
        print("Daha büyük bir sayı seç !")
        tahmin_hak -= 1
    elif tahmin>rastgele_sayı:
        print("Bilgiler sorgulanıyor...")
        time.sleep(1)
        print("Daha küçük bir sayı seç !")
        tahmin_hak -= 1
    elif tahmin==rastgele_sayı:
        print("Bilgiler sorgulanıyor...")
        time.sleep(1)
        print("Aferin, doğru tahmin !")
        break

    if tahmin_hak==0:
        print("-----------------------------\n"
              "Cevap hakkınız bitmiştir\n"
              "Doğru cevap {} olacaktı.".format(rastgele_sayı))
        break