#set metodu küme oluşturmayı sağlıyor.

def ebob(num1, num2):
    böl1 = set()
    böl2 = set()

    for a in range (1,num1+1):
        if num1 % a ==0:
            a = int(a)
            böl1.add(a)
# 'add' komutu kümeye eleman eklemeyi sağlar.

    for b in range (1,num2+1):
        if num2 % b ==0:
            b = int(b)
            böl2.add(b)

    ortak = (böl1.intersection(böl2))
    if len(ortak)>0:
        print("\nSayıların ebobu : ",max(ortak))
# intersection kümelerin kesişimini bulmamızı sağlar.
    print("[",ortak,"]\n")
while True:
    num1 = int(input("Birinci sayı: "))
    num2 = int(input("İkinci sayı: "))
    ebob(num1,num2)
