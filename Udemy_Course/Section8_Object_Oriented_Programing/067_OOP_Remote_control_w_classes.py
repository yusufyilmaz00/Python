import time

import random

class Kumanda():

    def __init__(self,tv_durum= "Kapalı",tv_ses =0,kanal_listesi= ["TRT"],kanal ="TRT",kanal_türü="TV"):
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_listesi = kanal_listesi
        self.kanal = kanal
        self.kanal_türü = kanal_türü

    def tv_aç(self):
        if (self.tv_durum == "Açık"):
            print("Tevevizyon zaten açık !")
        else:
            time.sleep(1)
            print("Televizyon açılıyor...")
            self.tv_durum = "Açık"

    def tv_kapat(self):
        if (self.tv_durum=="Kapalı"):
            print("Televizyon zaten kapalı !")
        else:
            time.sleep(1)
            print("Televizyon kapatılıyor...")
            self.tv_durum = "Kapalı"

    #finish
    def ses_ayarları(self):
        while True:
            cevap = input("Sesi 1 azaltmak için '<' , çoklu azaltmak için '<<<'\n"
                          "Sesi 1 arttırmak için '>' , çoklu arttırmak için '>>>'\n"
                          "Tuşlarına basınız : ")

            if (cevap =="<"):
                if (self.tv_ses >0):
                    self.tv_ses -=1
                    print("Ses: ",self.tv_ses)

            elif (cevap ==">"):
                if (self.tv_ses <100):
                    self.tv_ses +=1
                    print("Ses: ",self.tv_ses)

            elif (cevap == "<<<"):
                if (self.tv_ses >= 10):
                    self.tv_ses -= 10
                    print("Ses: ", self.tv_ses)

            elif (cevap == ">>>"):
                if (self.tv_ses <= 90):
                    self.tv_ses += 10
                    print("Ses: ", self.tv_ses)

            else:
                print("\n          Hata: Geçersiz format\n"
                      "Lütfen sizden istenilen formatta giriş yapınız.")
                print("          Güncel ses: ",self.tv_ses)
                break

    # finish
    def kanal_ekle(self,kanal_ismi):
        print("Kanal ekleniyor...")
        time.sleep(1)
        self.kanal_listesi.append(kanal_ismi)
        print("Kanal eklendi")

    # finish
    def rastgele(self):
        rastgele = random.randint(0,len(self.kanal_listesi)-1)
        self.kanal = self.kanal_listesi[rastgele]
        print("Bulunduğunuz kanal: ",self.kanal)

    #finish
    def __len__(self):
        return len(self.kanal_listesi)

    #finish
    def __str__(self):
        return "TV durumu: {}\nTV ses: {}\nKanal listesi: {}\nŞuanki kanal: {}\n".format(self.tv_durum,self.tv_ses,self.kanal_listesi,self.kanal)

    def tür(self):
        while True:
            seçim = input("Kanal türünü güncelleyiniz --> 'TV' ya da 'Radyo' : ")
            if seçim =="TV":
                print("TV moduna geçildi.")
                break
            elif seçim=="Radyo":
                print("Radyo moduna geçildi.")
                break
            else:
                print("Geçersiz kelime girildi")

kumanda = Kumanda()

print(""""
Kumanda Uygulaması

1. TV aç

2. TV kapat

3. Ses ayarları

4. Kanal ekle

5. Kanal sayısını öğrenme

6. Rastgele kanala geçme

7. Televizyon bilgileri

8. Cihaz modunu değiştirin

çıkmak için q'ya basınız.
""")

while True:
    işlem = input("İşlemi seçiniz: ")

    if işlem =="q" or işlem=="Q":
        print("Program kapatılıyor...")
        break

    elif işlem =="1":
        kumanda.tv_aç()

    elif işlem=="2":
        kumanda.tv_kapat()

    elif işlem=="3":
        kumanda.ses_ayarları()

    elif işlem=="4":
        kanal_isimleri = input("Kanal isimlerini ',' ile ayırarak girin: ")
        kanal_listesi= kanal_isimleri.split(",")
        for eklenecekler in kanal_listesi:
            kumanda.kanal_ekle(eklenecekler)

    elif işlem=="5":
        print(kumanda.__len__())

    elif işlem == "6":
        kumanda.rastgele()

    elif işlem =="7":
        print(kumanda.__str__())

    elif işlem =="8":
        kumanda.tür()

    else:
        print("Geçersiz işlem...")