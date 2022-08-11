toplam=0
print("Promram siz 'q' veya 'Q' yazana kadar çalışacaktır.\n")
while True:
    x=(input("Bir sayı giriniz: "))
    if x=="q" or x=="Q":
        break
    toplam+=int(x)

print("Toplam: ",toplam,"\n-------------------------\nProgram sonlandırılıyor...")