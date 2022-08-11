username= "admin2022"
password= "1959"
i=7 # deneme hakkı

while (i>0):
    un=str(input("Kullanıcı adınızı giriniz: ")) # un for "username"
    pw=str(input("Kullanıcı parolanızı giriniz: ")) # pw for "password"

    if un != username and pw == password:
        print("\nKullanıcı adı hatalı...\n")

    elif un == username and pw != password:
        print("\nParola hatalı...\n")

    elif un != username and pw != password:
        print("\nKullanıcı adı ve Parola hatalı...\n")

    elif un==username and pw==password:
        print("\nBaşarılı bir şekilde giriş yapılıyor...")
        break

    i -= 1