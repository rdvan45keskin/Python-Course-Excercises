sayilar = [1,3,5,7,9,12,19,21]

# 1- sayilar listesini while ile ekrana yazdırın
#********************************************************
# uzunluk = 0
# while uzunluk < len(sayilar):
#     print(sayilar[uzunluk])
#     uzunluk+=1


# 2- başlangıç ve bitiş değerlerini kullanıcıdan alarak aradaki
#     tek sayıları ekrana yazdırın
#********************************************************
# baslangic = int(input("başlangıç değeri girin: "))
# bitis = int(input("bitis değeri girin: "))
# while baslangic<=bitis:
#     if(baslangic%2==1):
#         print(baslangic)
#     baslangic+=1 


# 3- 1-100 arasındaki sayıları azalan şekilde yazdırın
#********************************************************
# x=100
# while x >= 1:
#     print(x)
#     x-=1


# 4- kullanıcıdan alacağınız 5 sayıyı ekranda sıralı bir şekilde yazdırın
#********************************************************
# x=0
# sayilar = []
# while x<5:
#     sayi = int(input(f"{x+1}. sayıyı girin: "))
#     sayilar.append(sayi)
#     x += 1
# sayilar.sort()
# print("sıralı sayılar: ",sayilar)


# 5- kullanıcıdan alacağınız sınırsız ürün bilgisini ürünler listesinde saklayın
#     **ürün sayısını kullanıcıya sorun
#     **dictionary listesi yapısı (name,price) şeklinde olsun
#     **ürün ekleme işlemi bittiğinde ürünleri ekranda while ile listeleyin
#********************************************************
urun_sayisi=int(input("kaç ürün girilecek: "))
urunler = []
while urun_sayisi>0:
    name=input(f"{len(urunler)+1}.ürün adını girin: ")
    price=int(input(f"{len(urunler)+1}.ürün fiyatını girin: "))
    urunler.append({"name":name,"price":price})
    urun_sayisi-=1

index = 0
while index < len(urunler):
    urun = urunler[index]
    print(f"Ürün adı: {urun['name']}, Ürün fiyatı: {urun['price']} TL")
    index += 1