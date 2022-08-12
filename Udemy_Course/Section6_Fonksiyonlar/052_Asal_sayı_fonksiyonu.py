def is_prime(num):
    num = int(num)

    if num == 0:
        return False
    elif num == 1:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2,int(num ** 0.5)+1):

"""
Buradaki { int(num ** 0.5) + 1 } işlemini inceleyelim.

--> ** 0.5 işlemi sayının 1/2. kuvvetini yani kökünü(√¯) almak demek.
--> kökünü aldıktan sonra int()fonksiyonu ile tam sayıya çevirdik.
    - çünkü ( √¯5 ) yaklaşık 2.2 değerindedir ve range() fonksiyonunda
    kullanabilmemiz için tam sayı olmalır.
--> sondaki +1'i de range fonksiyonu son sayıdan 1 eksik olana kadar gittiği
    için +1 ekliyoruz. 

--> Peki neden orada matematiksel ifadeyi range()'in sınırı haline getiriyoruz.

--> Bir asal sayıyı bulmaya çalışırken ondan küçük sayıların onu tam bölme durumlarına bakarız.
    - eğer sayı asal ise kendinden önceki her sayıyı programımız dener,
     tâki asal sayıya gelene kadar. Eğer asal sayımız 100.000 ise bu 100.000 deneme demektir
     ve sayı büyüdükçe bu deneme sayısı giderek artar.
     
--> gelelim oradaki sihirli ifadeye ve bunu bir örnek ile irdeleyelim;
    - sayımız 16 olsun.
    - bölenleri [ 1 2 4 4 8 16] 'dir.
        1 x 16
        2 x 8
        4 x 4 şeklinde yani.
--> 1'den 16'ya kadar olan sayıların 16'yı bölme durumunu kontrol edelim.
    2 böler, 4 böler, 8 böler.
--> sayı asal değilken bulmak kolay çünkü 2'den sonra denememize gerek kalmıyor. 
    - ayrıca 2 bölüyorsa onun çarpan eşi 8'de kesinlikle bölecektir.
    - eğer 4'te bölüyorsa onun çarpan eşi 4'te kesinlikle bölmek zorunda.        
--> peki ya 16 sayısı asal olsaydı ?
    - 2 bölmeyecekti, dolayısıyla 8 de bölmeyecekti
    - 4 bölmeyecekti, dolayısıyla diğer 4'te bölmeyecekti. 
--> yani sayıların ilk yarısını denedikten sonra diğer yarısını denememize gerek kalmıyor.
    Peki bu yarımlığı neye göre tayin edeceğiz,belirleyeceğiz ?
--> Öncelikle sayımızın ortadaki çarpanlarına göre başka bir deyişle 
    mükemmel senaryoda sayının köküne göre.
    
--> tekrardan 16'yı inceleyelim (1,2,4,4,8,16)
    - ortadaki çarpan (4 x 4)'dır. Yani 4 sayısına kadar baktıktan sonra devamına bakmamıza gerek yok.
    16 nın kökü 4'tür . Yani anlatmaya çalıştığım mükemmel senaryonun ta kendisi.
    
    peki neden int() kullanarak tam sayıya çevirdik. Çünkü her sayı 16 kadar şanslı olmayabilir.
    Örneğin 32 , yalnızca 16'nın 2 katı. ama ortadaki çarpanı (4x8) ve 
    kökünü aldığımızda 5,5 gibi bir sonuç elde ederiz. Ama daha önceden de bahsettiğimiz gibi
    range() fonksiyonu içerisinde ondalıklı sayı kullanamayız bu yuzden int() ile tam sayıya çevirdik.
    
--> bu şekilde sayıları yanlızca Ana sayımızın (16 ya da asal sayılar) kökü olan sayıya kadar incelediğimizde
    kodumuzun çalışma süresini ve deneme sayısını kısaltmış oluruz. Bu da en verimli ve hızlı şekilde asal sayıyı
    bulmamızı sağlar.
"""
            if num % i ==0:
                return False
        else:
            return True

while True:
    x = input("Bir sayı gir: ")
    if x == "q" or x == "Q":
        print("Program kapatılıyor...")
        break

    x =int(x)
    if is_prime(x):
        print(f"{x} asal bir sayıdır.")
        break
    else:
        print(f"{x} asal bir sayı değildir.")
        break

