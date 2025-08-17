# 1- Liste elemanları içindeki sayısal değerleri bulunuz
# **************************************************
# liste = ["1","2","5a","10b","abc","10","50"]
# sayilar = []
# gecersizler = []
# for i in liste:
#     try:
#         sayilar.append(int(i))
#     except ValueError:
#         print("değer sayı olmalıdır.",i)
#         gecersizler.append(i)
# print(sayilar)
# print(gecersizler)



# 2- Kullanıcı "q" değerini girmedikce aldığınız her inputun sayı
# olduğundan emin olun aksi taktirde hata mesajı verin
# **************************************************
# degerler = []
# while True:
#     x = (input("sayi girin: "))
#     if x == "q":
#         break
#     try:
#         result = float(x)
#         degerler.append(result)
#     except ValueError:
#         print("değer sayı olmalıdır.")
   
# print(degerler)



# 3- girilen parola içinde türkçe karakter var mı kontrol EncodingWarning
# **************************************************
# parola = "123456aQç"
# def control(chk):
#     import re
#     if re.search("[çşğüöıİ]",chk):
#         raise Exception("parola türkçe karakter içermemeli")
#     else:
#         print("parola geçerli")

# try:
#     control(parola)
# except Exception as ex:
#     print(ex)
# **************************************************
# ***OR***
# def checkPassword(parola):
#     turkce_karakterler = "çşğüöıİ"

#     for i in parola:
#         if i in turkce_karakterler:
#             raise TypeError("Parola türkçe karakter içermemelidir")
#         else:
#             pass
#     print("geçerli parola")
# parola = input("parola girin: ")

# try:
#     checkPassword(parola)
# except TypeError as err:
#     print(err)



# 4- faktoriyel fonksiyonu oluşturup fonksiyona gelen değerler için
# hata mesajları verin negatif veya harf gelmesi durumu
# **************************************************
# def fact(x):
#     if  type(x) == str:
#         raise Exception("girilen değer sayı olmalıdır")
    
#     elif x < 0:
#         raise Exception("girilen sayi negatif olmamalı")
    
#     fac = 1
#     for i in range(1,x+1):
#         fac *= i
#     print(f"{x}! = {fac}")
# sayi = 6
# try:
#     fact(sayi)
# except Exception as ex:
#     print(ex)
# **************************************************
# ***OR***
liste = ["1","2","5a","10b","abc","10","50"]

def fact(x):
    if x < 0:
        raise Exception("girilen sayi negatif olmamalı")
    
    fac = 1
    for i in range(1,x+1):
        fac *= i
    return fac

for x in liste:
    try:
        K = fact(int(x))
    except ValueError:
        print(f"'{x}' sayı değildir.")
        continue
    except Exception as ex:
        print(ex)
        continue
    print(f"{x}! = {K}")
