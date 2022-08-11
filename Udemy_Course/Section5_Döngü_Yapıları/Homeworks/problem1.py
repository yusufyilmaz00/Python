# mükemmel sayıyı kontrol ederken bölen sayıların listesini
# görmek istiyorsanız '#' yorum satılarını kaldırın.

num = int(input("Bir sayı giriniz: "))

#bölen_liste=[]
bölen_toplam=0
for i in range(1,num): # sayının kendisine kadar
    if num % i==0: # kalansız bölüyorsa
        #bölen_liste.append(i)
        bölen_toplam += i
if bölen_toplam==num:
    print("Bu sayı mükemmel sayıdır...")
else:
    print("Bu sayı mükemmel sayı değildir.")
#print(bölen_liste)