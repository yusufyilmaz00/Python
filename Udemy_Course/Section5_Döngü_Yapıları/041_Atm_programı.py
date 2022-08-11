print("""***********************************
ATM Makinesine Hoşgeldiniz.

işlemler;
1.Bakiye Sorgulama
2.Para Yatırma
3.Para Çekme

q --> çıkış
***********************************
""")
user_bakiye = 0
while True:
    islem=(input("Yapmak istediğiniz işlem numarasını giriniz: "))

    if islem=="1":
        print("Güncel bakiyeniz '{}' TL'dir...".format(user_bakiye))

    try:
        if islem=="2":
            yatır=int(input("Yatırmak istediğiniz tutarı giriniz: "))
            user_bakiye += yatır
            print("Güncel bakiyeniz '{}' olmuştur...".format(user_bakiye))
    except:
        # if user enter any string
        print("\nGeçersiz format. Lütfen sadece sayı giriniz.\n")

    try:
        if islem=="3":
            çek = int(input("Çekmek istediğiniz tutarı giriniz: "))

            if (user_bakiye - çek) < 0:
                print("Hesabınızda yeterli miktarda para bulunmakmaktadır...")
                continue
            user_bakiye -= çek
            print("Güncel bakiyeniz '{}' olmuştur...".format(user_bakiye))
    except:
    # if user enter any string
        print("\nGeçersiz format. Lütfen sadece sayı giriniz.\n")

    if islem=="q" or islem == "Q":
        print("Program kapatılıyor...")
        break