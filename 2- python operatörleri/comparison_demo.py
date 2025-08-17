# 1- girilen 2 sayıdan hangisi büyüktür
inputs=[]
for i in range(2):
    inpute=int(input(f"{i+1}. değeri girin: "))
    inputs.append(inpute)
result = (inputs[0]>=inputs[1])
print(inputs)
print(result)

# 2- kullanıcıdan vize(%40) ve final(½60) alıp ortalama hesaplayın
#    eğer ortalama 50 ve üzeriyse geçti değilse kaldı yazın
vize  = int(input("vize notunu girin: "))
final = int(input("final notunu girin: "))
ortalama = ((vize*0.4)+(final*0.6))
print(ortalama)
durum = ortalama>=50
print(durum)

# 3- girilen bir sayının tek mi çift mi olduğunu bulun
number1 = int(input("bir sayı girin: "))
result1 = (number1%2==0)
print(result1)

# 4- girilen bir sayının negatif pozitif durumunu yazın
number2 = int(input("bir sayı girin: "))
result2 = (number2<0)
print(result2)

# 5- parola ve kullanıcıadı bilgisini isteyip doğruluğunu kontrol edin
#    kullanıcıadı= IndigoApatosarus : parola: 123456
username = input("kullanıcı adı girin: ")
password = input("şifre girin: ")
result = username=="IndigoApatosarus" and password == "123456"
print(result)