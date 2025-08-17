# x = 10

# if x > 5:
#     raise Exception("x 5den büyük değer alamaz")

# def check_password(psw):
#     import re
#     if len(psw) < 5:
#         raise Exception ("Parola en az 6 karakter olmalıdır")
#     elif not re.search("[a-z]",psw):
#         raise Exception("parola küçük harf içermelidir")
#     elif not re.search("[A-Z]",psw):
#         raise Exception("parola Büyük harf içermelidir")
#     elif not re.search("[0-9]",psw):
#         raise Exception("parola Rakamm içermelidir")
#     elif not re.search("[_@$]",psw):
#         raise Exception("parola alfanumerik karakter içermelidir")
#     elif re.search("\s",psw):
#         raise Exception("parola boşluk içermemelidir")
#     else:
#         print("geçerli parola def")

# password = "123456aA_"

# try:
#     check_password(password)
# except Exception as ex:
#     print(ex)
# else:
#     print("geçerli parola : else")
# finally:
#     print("validation tamamlandı.")


class Person:
    def __init__(self,name,year):
        if len(name) > 10:
            raise Exception("name alanı fazla karakter içeriyor")
        else:
            self.name = name

p = Person("Indigoooooooo",1)
print(p)