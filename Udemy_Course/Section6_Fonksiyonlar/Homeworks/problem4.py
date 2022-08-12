def sayı_oku():
    num = int(input("Bir sayı giriniz: "))
    if num<10 or num >100:
        print("sadece 2 basamaklı sayılar girebilirsiniz.")
        return
    num = str(num)

    onlar_bas = ["null","On","Yirmi","Otuz","Kırk","Elli","Altmış","Yetmiş","Seksen","Doksan"]
    birler_bas = ["","bir","iki","üç","dört","beş","altı","yedi","sekiz","dokuz"]

    idx_birler = birler_bas[int(num[1])]
    idx_onlar = onlar_bas[int(num[0])]

    print(f"{num} : {idx_onlar} {idx_birler}")

sayı_oku()