import time

class Hayvan():

    def __init__(self,nefes,renk="Bilgi yok."):
        self.nefes = nefes
        self.renk = renk

    def animal_add():
        command= input("Kaydedeceğiniz hayvan türünü seçin: "
                       "\n    - bird"
                       "\n    - dog"
                       "\n    - horse"
                       "\n: ")
        if command== "bird":
            bird.kayıt()
            bird.göster()
            bird.nefes_al()
            bird.nefes_ver()

        elif command== "dog":
            dog.kayıt()
            dog.göster()
            dog.nefes_al()
            dog.nefes_ver()

        elif command== "horse":
            horse.kayıt()
            horse.göster()
            horse.nefes_al()
            horse.nefes_ver()

        else:
            print("Hata: Geçersiz işlem !")

    def nefes_al(self):
        print("Nefes alınıyor...")
        time.sleep(1)
        print("Nefes alındı.")
        self.nefes = "Nefes Tutuluyor."

    def nefes_ver(self):
        print("Nefes veriliyor...")
        time.sleep(1)
        print("Nefes verildi.")
        self.nefes = "Nefes salınıyor."

class Köpek(Hayvan):
    def __init__(self,tüy="Var",tırnak = "Uzun"):
        self.tüy = tüy
        self.tırnak = tırnak
    def kayıt(self):
        self.tüy = input("Tüy 'VAR' or 'YOK' : ")
        self.tırnak = input("Tırnak 'Kısa' or 'Uzun' : ")
        self.renk = input("Renk bilgisini giriniz: ")
    def göster(self):
        print("""
        Tüy : {}
        Tırnak : {}
        Renk : {}
        """.format(self.tüy,self.tırnak,self.renk))

class Kuş(Hayvan):
    def __init__(self,tüy="Var",kanat_uzunluğu="0"):
        self.tüy= tüy
        self.kanat_uzunluğu = kanat_uzunluğu
    def kayıt(self):
        self.tüy = input("Tüy 'VAR' or 'YOK' : ")
        self.kanat_uzunluğu = input(" Kanat uzunluğunu gir: ")
        self.renk = input("Renk bilgisini giriniz: ")

    def göster(self):
        print("""
        Tüy : {}
        Kanat uzunluğu : {}
        Renk : {}
        """.format(self.tüy,self.kanat_uzunluğu,self.renk))

class At(Hayvan):
    def __init__(self, yele="Var", ağırlık="0"):
        self.yele = yele
        self.ağırlık = ağırlık

    def kayıt(self):
        self.yele = input("Yele'VAR' or 'YOK' : ")
        self.ağırlık = input("Atın ağırlığını giriniz: ")
        self.renk = input("Renk bilgisini giriniz: ")

    def göster(self):
        print("""
         Yele : {}
         Ağırlık : {}
         Renk : {}
         """.format(self.yele, self.ağırlık, self.renk))

bird = Kuş()
dog = Köpek()
horse = At()

Hayvan.animal_add()




