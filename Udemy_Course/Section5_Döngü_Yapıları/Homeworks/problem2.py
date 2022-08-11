num = int(input("Bir sayı giriniz: "))

kuvvet = 0
total = 0
num_copy = num

while num_copy != 0:
    num_copy = num_copy // 10
    kuvvet +=1

for i in str(num):
    total += int(i) ** kuvvet

if total==num:
    print(f"Girdiğiniz sayı armstrong sayıdır. {total}")
else:
    print(f"Girdiğiniz sayı armstrong sayısı değildir. {total}")