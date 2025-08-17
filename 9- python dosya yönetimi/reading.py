# try:
#     file = open("newfile.txt","r")
#     print(file)
# except FileNotFoundError:
#     print("belirtilen dosya bulunamadı")
# finally:
#     print("dosya kapandı")
#     file.close

file = open("newfile.txt","r",encoding="utf-8")

# for döngüsü
# for i in file:
#     print(i,end = "")

# ************read fonksiyonu
# content = file.read()
# print("içerik 1")
# print(content)

# content2 = file.read()      # 1. komut çalışınca dosya kapanmadığı için
# print("içerik2")            # imleç en sonda kalır ve boşluğu okur
# print(content2)
# file.close()

# content = file.read(6)
# content = file.read(3)
# content = file.read(4)
# print(content)
# file.close()

# ************readline() fonksiyonu komple satırı okur


# print(file.readline(),end="")
# print(file.readline(),end="")

# ************readlines() fonksiyonu
# liste = file.readlines()
# print(liste[1])




file.close()