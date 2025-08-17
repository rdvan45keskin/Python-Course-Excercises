# 1- kullanıcıdan isim, yaş ve eğitim bilgilerini kontrol eden bir uygulama. ehliyet alma koşulu
# en az 18 yaş ve eğitim durumu lise ya da üniversite olmalıdır

# name = input("isminizi girin : ")
# age = int(input("yaşınızı girin : "))
# edu = input("eğitim durumunuzu girin : ").lower()

# if(edu=="ilkokul")or(edu=="ortaokul")or(edu=="lise")or(edu=="üniversite"):
#     if(age>=18):
#         if(edu=="lise")or(edu=="üniversite"):
#             print(f"Sayın {name} ehliyet alabilirsiniz")
#         else:
#             print(f"Sayın {name} eğitim durumunuz lise ya da üniversite olmalıdır")
#     else:
#         print(f"Sayın {name} en az 18 yaşında olmalısınız")
# else:
#     print("geçerli bir eğitim durumu girin \nilkokul,ortaokul,lise,üniversite")



# 2- bir öğrencinin 2 yazılı bir sözlü notunu alıp hesaplanan not ortalamasına göre aralığa karşılık
# gelen not bilgisini yazın
# 0-24 => 0
# 25-44 => 1
# 45-54 => 2
# 55-69 => 3
# 70-84 => 4
# 85-100 => 5

# yazili1 = int(input("1. yazılıyı girin: "))
# yazili2 = int(input("2. yazılıyı girin: "))
# sozlu1 = int(input("sözlüyü girin: "))

# ortalama = (yazili1+yazili2+sozlu1)/3
# if (0<ortalama<=24):
#     print("0")
# elif (25<=ortalama<=44):
#     print("1")
# elif (45<=ortalama<=54):
#     print("2")
# elif (55<=ortalama<=69):
#     print("3")
# elif (70<=ortalama<=84):
#     print("4")
# elif (85<=ortalama<=100):
#     print("5")
# else:
#     print("hesaplanamadı")


# 3- trafige çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere göre hesaplayın
# 1.bakım => 1.yıl
# 2.bakım => 2.yıl
# 3.bakım => 3.yıl
# **süre hesabını alınan gün,ay,yıl bilgisine göre gün bazlı hesaplayın
# **datetime modülünü kullanmanız gerekiyor
# (simdi) - (2024/8/11) = gün

from datetime import datetime
trafige_cikis_tarhihi = input("trafiğe çıkış tarihini giriniz (gg/aa/yyyy): ")
trafige_cikis = datetime.strptime(trafige_cikis_tarhihi,"%d/%m/%Y")
gunumuz = datetime.now()
gecen_gun_sayisi = (gunumuz-trafige_cikis).days
if (0<gecen_gun_sayisi<365):
    print(f"aracınız {gecen_gun_sayisi} gündür trafikte ve 1. bakımını yaptırmalısınız.")
elif (365<=gecen_gun_sayisi<730):
    print(f"aracınız {gecen_gun_sayisi} gündür trafikte ve 2. bakımını yaptırmalısınız.")
elif (730<=gecen_gun_sayisi<1095):
    print(f"aracınız {gecen_gun_sayisi} gündür trafikte ve 3. bakımını yaptırmalısınız.")
elif (1095<=gecen_gun_sayisi<1460):
    print(f"aracınız {gecen_gun_sayisi} gündür trafikte ve 4. bakımını yaptırmalısınız.")
else:
    print(f"aracınız {gecen_gun_sayisi} gündür trafikte ve genel bakım yaptırın.")
