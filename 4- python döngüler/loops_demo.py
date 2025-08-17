"""
    1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile 
    buldurmaya çalışın
    *** "random modülü" için "python random" şeklinde arama yapın
    *** 100 üzerinden puanlama yapın.her soru 20 puan
    *** hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı
        üzerinden hesaplansın
"""

import random
rastgele_sayi = random.randint(1, 10)
print(rastgele_sayi)
hak = int(input("hak sayısı girin: "))
sayac = 0
puan = 100
puan_kaybi = 100/hak
print(puan_kaybi)
print(f"Deneme Hakkınız : {hak}")
while hak > 0:
    tahmin=int(input("sayiyi tahmin edin: "))
    hak -= 1
    sayac += 1
    if(rastgele_sayi==tahmin):
        print(f"Tebrikler {sayac}. defada bildiniz ve puanınız: {puan}")
        break
    elif(rastgele_sayi>tahmin):
        print(f"Yukarı \nKalan Hak : {hak}")
    elif(rastgele_sayi<tahmin):
        print(f"Aşağı \nKalan Hak : {hak}")
    if(hak>0):
        puan-=puan_kaybi
    if(hak==0):
        print(f"hakkınız bitti. Tutulan sayı : {rastgele_sayi}")











