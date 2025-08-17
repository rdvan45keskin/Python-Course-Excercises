# 1- Gonderilen bir kelimeyi belirtilen kez ekranda göstereren foknsiyonu yazın

# kelime = input("kelimeyi yazın: ")
# adet = int(input("kaç adet yazılacak: "))

# def loopWord(kelime,adet):
#     for i in range(adet):
#         print(kelime)
# loopWord(kelime,adet)


# 2- Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyonu yazın
# ****************************************************
# def liste(*parametre):
#     myList = []
#     for param in parametre:
#         myList.append(parametre)
#     return  myList
# giris = [10,20,30,"hello"]
# print(liste(giris))


# 3- Gönderilen 2 sayı arasındaki tüm asal sayıları bulun
# ****************************************************
# baslangic = int(input("başlangıç: "))
# bitis = int(input("bitis: "))
# def asal(baslangic,bitis):
#     asallar = []
#     for sayi in range(baslangic,bitis+1):
#         if sayi > 1:
#             for i in range(2,sayi):
#                 if (sayi % i ==0):
#                     break
#             else:
#                 asallar.append(sayi)
#     print(asallar)

# asal(baslangic,bitis)

        
# 4- kendisine gönderilen bir sayının tam bölenlerini liste şeklinde verin
# ****************************************************
# def tamBolen(sayi):
#     tambolenler = []
#     for i in range(2,sayi+1):
#         if sayi % i == 0:
#             tambolenler.append(i)
#     return tambolenler
# print(tamBolen(20))