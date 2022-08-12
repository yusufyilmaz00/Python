def tamsayı_bölen(x):
    global liste
    liste=[]
    for i in range(1,x+1):
        if x % i == 0:
            liste.append(i)
    print("{}'in tam sayı bölenleri: ".format(x),liste)

while True:
    x= int(input("Bir sayı giriniz: "))
    tamsayı_bölen(x)
    toplam = 0

    for t in liste:
        toplam += t

    print("Toplamları da : ",toplam)
    break