a,b = 1,1
x = int((int(input("/Girdi formatı çift sayı olmalıdır/\n"
              "Kaç elemanlı dizi oluşturmak istersin : "))) / 2)
fibo=[]

for i in range(x):
    fibo.append(b)
    fibo.append(a)
    b= a+b          # b=2 oldu
    a += b          # a=3

print(fibo)
