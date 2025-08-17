
"""
ogrenciler = {
        "120": {
            "ad" : "ali",
            "soyad" : "yılmaz",
            "telefon" : "532 000 00 01"
        },
        "125": {
            "ad" : "can",
            "soyad" : "korkmaz",
            "telefon" : "532 000 00 02"
        },
        "128": {
            "ad" : "volkan",
            "soyad" : "yükselen",
            "telefon" : "532 000 00 03"
        },
    }
    1-Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle 
    dictionaary içinde saklayın

    2-öğrenci numarasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin
"""
ogrenciler = {}

# number = input("öğrenci no: ")
# name = input("öğrenci adı: ")
# surname = input("öğrenci soyadı: ")
# phone = input("öğrenci telefonu: ")

# ogrenciler[number] = {            #bu daha iyi döngüde öyle karar kıldm
#     "ad" : name,
#     "soyad" : surname,
#     "telefon" : phone
# }

# ogrenciler.update({
#     number: {
#         "ad" : name,
#         "soyad" : surname,
#         "telefon" : phone
#     }
# })

for i in range(2):
    number = input(f"{i+1}. öğrenci no: ")
    name = input(f"{i+1}. öğrenci adı: ")
    surname = input(f"{i+1}. öğrenci soyadı: ")
    phone = input(f"{i+1}. öğrenci telefonu: ")
    ogrenciler[number] = {
        "ad" : name,
        "soyad" : surname,
        "telefon" : phone
    }

print(ogrenciler)

ogrNo = input("öğrenci no: ")
ogrenci = ogrenciler[ogrNo]
print(ogrenci)

