#error handling => hata yönetimi

# try:
#     x = int(input("x: "))
#     y = int(input("y: "))
#     print(x/y)
# except ZeroDivisionError:
#     print("y değeri 0 olamaz")
# except ValueError:
#     print("sadece sayısal veri girin")

# try:
#     x = int(input("x: "))
#     y = int(input("y: "))
#     print(x/y)
# except (ZeroDivisionError,ValueError) as e:
#     print("yanlış bilgi girdiniz")
#     print(e)

# try:
#     x = int(input("x: "))
#     y = int(input("y: "))
#     print(x/y)
# except:
#     print("yanlış bilgi girdiniz")

while True:
    try:
        x = int(input("x: "))
        y = int(input("y: "))
        print(x/y)
    except Exception as ex:
        print("yanlış bilgi girdiniz",ex)
    else:
        print("her şey yolunda")
        break
    finally:
        print("try except sonlandı.")
