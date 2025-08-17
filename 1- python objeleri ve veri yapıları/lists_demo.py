# 1-  "bmw, mercedes, opel, mazda " elemanlarına sahip bir liste oluşturun
my_list = ["bmw","mercedes","opel","mazda"]
print(my_list)

# 2-  liste kaç elemanlıdır
print(len(my_list))

# 3-  listenin ilk ve son elemanı nedir
print(my_list[0]+" "+my_list[-1])

# 4-  mazda değerini toyota ile değiştirin
my_list[3] = "toyota"
print(my_list)

# 5-  mercedes listenin bir elemanı mıdır
is_member = "mercedes" in my_list
print(is_member)

# 6-  listenin -2 indeksindeki değer nedir
print(my_list[-2])

# 7-  listenin ilk 3 elemnanını alın
print(my_list[:3])

# 8-  listenin son 2 elemanı yerine "toyota" ve "renault" değerlerini ekkleyin
my_list[-2:]=["toyota","renault"]
print(my_list)

# 9-  listenin üzerine "audi" ve "nissan" değerlerini ekleyin
my_list.extend(["audi","nissan"])
print(my_list)

# 10- listenin son elemanını silin
my_list.pop(-1)
del my_list[-1]
# my_list.remove("nissan")
# 11- liste elemanlarını tersten yazdırırn
my_list.sort()
my_list.reverse()
print(my_list)
# 12- aşağıdaki verileri bir liste içined saklayınız
#         studentA: Yiğit Bilgi 2010, (70,60,70)
#         studentB: Sena Turan  1999, (80,80,70)
#         studentC: Ahmet Turan 1998, (80,70,90)
studentA = ["yiğit","bilgi",2010,[70,60,70]]
studentB = ["sena","turan",1999,[80,80,70]]
studentC = ["ahmet","turan",1998,[80,70,90]]
# 13- liste elemanlarını ekrana yazdırın
print(f"{studentA[0]} {studentA[1]} {2024-studentA[2]} yaşında ve not ortalaması {(studentA[3][0]+studentA[3][1]+studentA[3][2])/3:1.4}")