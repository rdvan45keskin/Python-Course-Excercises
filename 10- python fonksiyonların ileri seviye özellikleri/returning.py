# def usAlma(number):
#     def inner(power):
#         return number ** power
#     return inner

# two = usAlma(2)
# print(two(3))
# # three = usalma(3)
# print((usAlma(3))(4))   

# def yetkiSorgu(page):
#     def inner(role):
#         if role == "Admin":
#             return "{0} rolü {1} sayfasına ulaşabilir".format(role,page)
#         else:
#             return "{0} rolü {1} sayfasına ulaşamaz".format(role,page)
#     return inner

# User1 = yetkiSorgu("asad")
# print(User1("Admin"))
# print(User1("User"))

def islem(islemAdi):
    def toplam(*args):
        toplam = 0
        for i in args:
            toplam+=i
        return toplam
    
    def carpma(*args):
        carpim = 1
        for i in args:
            carpim *=i
        return carpim
    
    def cikarma(*args):
        if len(args) == 0:
            return 0
        cikarma = args[0]
        for i in args[1:]:
            cikarma-=i
        return cikarma
    
    def bolme(*args):
        if len(args) == 0:
            return 0
        bolum = args[0]
        try:
            for i in args[1:]:
                bolum /= i
        except ZeroDivisionError:
            return "Hata: Sıfıra bölme işlemi yapılamaz."
        return bolum
    
    if islemAdi == "toplama":
        return toplam
    elif islemAdi == "carpma":
        return carpma
    elif islemAdi == "cikarma":
        return cikarma
    elif islemAdi == "bolme":
        return bolme
    else:
        return lambda *args: "Geçersiz işlem"
    
# Örnek kullanım:
toplama = islem("toplama")
print(toplama(1, 2, 3))  # 6

carpma = islem("carpma")
print(carpma(2, 3, 4))  # 24

cikarma = islem("cikarma")
print(cikarma(10, 5, 2))  # 3

bolme = islem("bolme")
print(bolme(20, 5, 2))  # 2.0
print(bolme(20, 0))     # Hata: Sıfıra bölme işlemi yapılamaz.