# 1- girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz

# sayi1 = int(input("bir sayı girin: "))
# result1 = sayi1>=0 and sayi1<=100
# print(f"sayının 0 ile 100 arasında olma durumu: {result1}")

# 2- girilen bir sayının pozitif çift sayı olup olmadığını kontrol Ediniz

# sayi2 = int(input("bir sayı girin: "))
# result2 = sayi2>=0 and sayi2%2 == 0
# print(f"sayının pozitif ve çift olma durumu: {result2}")

# 3- kullaniciadi ve parola bilgileri ile giriş kontrolü yapın

# username,password = "Indigo513","123456"
# kullaniciadi = input("kullanici adi girin: ")
# parola = input("parola girin: ")
# isUsername = (username==kullaniciadi.strip())
# isPassword = (password==parola.strip())
# print(f"kullanıcı adı doğru mu : {isUsername} ve parola doğru mu : {isPassword}")

# 4- girilen 3 sayıyıyı büyüklük olarak karşılaştırın

# sayiA = int(input("1. sayıyı girin: "))
# sayiB = int(input("2. sayıyı girin: "))
# sayiC = int(input("3. sayıyı girin: "))
# resultA = sayiA>sayiB and sayiA>sayiC
# resultB = sayiB>sayiA and sayiB>sayiC
# resultC = sayiC>sayiA and sayiC>sayiB
# print(f"1. max mı : {resultA}, 2. max mı : {resultB}, 3. max mı: {resultC}")

# 5- kullanıcıdan 2 tane vize(%60) ve final(%40) notunu alıp ortalama hesapla
#     eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdır
#     a-) ortalama 50 olsa bile final notu en az 50 olmalıdır
#     b-) finalden 70 alındığında ortalamanın önemi olmasın

# vize1  = int(input("1. vize notu girin: "))
# vize2 = int(input("2. vize notu girin: "))
# final = int(input("final notu girin: "))
# ortalama = (((vize1+vize2)*0.6)/2) + (final*0.4)
# result = ortalama >= 50 and final>=50 or final>=70
# print(f"ortalamanız: {ortalama} ve geçme durumunuz : {result}")

# 6- kişinin ad,kilo ve boy bilgilerini alıp kilo indeksini hesaplayın
#     formül: (kilo / boyun karesi)
#     aşağıdaki tabloya göre kişi hangi gruba girer
#     0-18.4 zayıf
#     18.5-24.4 normal
#     25.0-29.9 fazla kilolu
#     30-34.9 ak şişkosu

name  = input("adınızı yazın: ")
weigh = float(input("kilonuzu yazın: "))
heigh = int(input("boyunuzu girin(cm cinsinden): "))
heigh = heigh / 100
index = (weigh) / (heigh ** 2)
A = (index>=0) and  (index<=18.4)
B = (index>18.4) and (index<=24.9)
C = (index>24.9) and (index<=29.9)
D = (index>=29.9) and (index<=34.9)

print(f"Adınız : {name} \nKilo index Durumunuz : {index} \nZayıf : {A} \nNormal : {B} \nFazla kilolu : {C} \nAk şişkosu : {D}")