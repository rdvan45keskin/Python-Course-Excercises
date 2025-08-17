# 1- Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz
#*******************************************************************
# sayi1 = int(input("bir sayı girin: "))
# if (0<=sayi1<=100):
#     print("sayi 0 ile 100 arasındadır")
# else:
#     print("değildir")





# 2- Girilen bir sayının pozitif çift sayı olup olmadığını kontrol ediniz
#*******************************************************************
# sayi2 = int(input("bir sayı girin: "))
# if (sayi2>0 and sayi2%2==0):
#     print("sayi pozitif çifttir")
# else:
#     print("değildir")





# 3- kullanıcıadi ve parola bilgileri ile giriş kontrolü yapın
#*******************************************************************
# kullaniciadi = "Indigo513"
# parola = "1234"
# username = input("kullanıcı adı girin: ").strip()
# password = input("parola girin: ").strip()
# if (username==kullaniciadi):
#     if (password==parola):
#         print("giriş başarılı")
#     else:
#         print("parola hatalı")
# else:
#     print("kullanıcı adı hatalı")





# 4- girilen 3 sayıyı büyüklük olarak sıralayın
#*******************************************************************
# sayi1 = int(input("1. sayıyı girin: "))
# sayi2 = int(input("2. sayıyı girin: "))
# sayi3 = int(input("3. sayıyı girin: "))
# sayilar = [sayi1, sayi2, sayi3]
# sayilar.sort()

# if(sayi1 > max(sayi2,sayi3)):
#     print("en büyük sayı 1.sayı")
# elif(sayi2 > max(sayi1,sayi3)):
#     print("en büyük sayı 2.sayı")
# else:
#     print("en büyük sayı 3.sayı")

# print(f"sıralama : {sayilar[2]}, {sayilar[1]}, {sayilar[0]} (büyükten küçüğe)")





# 5- kullanıcıdan 2 vize 60 ve final 40 notunu alıp ortalama hesaplayın
# eğer ortalama 50 ve üstündeyse geçti değilse kaldı yazdırın
# a- ortalama 50 olsa bile final notu en az 50 olmalıdır
# b- finalden 70 alındığında ortalamanın önemi yoktur
#*******************************************************************
# vize1  = int(input("1. vize notu girin: "))
# vize2 = int(input("2. vize notu girin: "))
# final = int(input("final notu girin: "))
# ortalama = (((vize1+vize2)*0.6)/2) + (final*0.4)
# if(ortalama >= 50):
#     if(final > 50):
#         print(f"ortalamanız : {ortalama} ve geçtiniz")
#     else:
#         print(f"ortalamanız : {ortalama} ama final notunuz 50'nin altında ({final}) olduğu için kaldınız")
# elif(final>70):
#     print(f"ortalamanız : {ortalama} ve geçtiniz")
# else:
#     print(f"ortalamanız : {ortalama} ve kaldınız")





# 6- kişinin ad,kilo ve boy bilgilerini alıp kilo indeksini hesaplayın
# formül: (kilo / boyun karesi) 
# aşağıdaki tabloya göre kişi hangi gruba girer
# 0-18.4 zayıf 
# 18.5-24.4 normal
# 25.0-29.9 fazla kilolu
# 30-34.9 ak şişkosu
#*******************************************************************
# name  = input("adınızı yazın: ")
# weigh = float(input("kilonuzu yazın: "))
# heigh = int(input("boyunuzu girin(cm cinsinden): "))
# heigh = heigh / 100
# index = (weigh) / (heigh ** 2)
# if(0<=index<=18.4):
#     print(f"Sayın {name} kilo indeksin: {index} ve kilo değerlendirmen zayıf")
# elif(18.4<index<=24.9):
#     print(f"Sayın {name} kilo indeksin: {index} ve kilo değerlendirmen normal")
# elif(24.9<index<=29.9):
#     print(f"Sayın {name} kilo indeksin: {index} ve kilo değerlendirmen kilolu")
# elif(29.9<index<=34.9):
#     print(f"Sayın {name} kilo indeksin: {index} ve kilo değerlendirmen obez")
# else:
#     print(f"Sayın {name} kilo indeksin: {index} yuh amk obezi az ye az")