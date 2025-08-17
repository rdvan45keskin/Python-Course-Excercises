names = ["ali","yağmur","hakan","deniz"]
years = [1998,2000,1998,1987]

# 1- "cenk" ismini listenin sonuna ekleyin
names.append("cenk")
print("1:",names)

# 2- "sena" ismini listenin başına ekleyin
names.insert(0,"sena")
print("2:",names)

# 3- "deniz" isminin indeksi nedir
index_of_deniz = names.index("deniz")
print("3:",index_of_deniz) 

# 4- "deniz" ismini listeden silim
new_names = names.remove("deniz")
print("4:",new_names)

# 5- "ali" listenin bir elemanı mdır
is_member = "ali" in names
print("5:",is_member)

# 6- liste elemanlarını ters çevirin
print(years[::-1])
print("6:",years)

# 7- liste elemanlarını alfabetik olarak sıralayın
names.sort()
print("7:",names)

# 8- years listesini rakamsal büyüklüğe göre sıralayın
years.sort()
print("8:",years)

# 9- str = "chevrolet,dacia" karakter dizisini listeye çevirin
str = "chevrolet,dacia"
result = str.split(",")
print(result)

# 10- years dizisinin en büyük ve en küçük elemanlarını yazın
maxY = max(years)
minY = min(years)
print(f"max year : {maxY} and min years : {minY}")

# 11- years dizisinde kaç tane 1998 değeri vardır
count_1998 = years.count(1998)
print("11:",count_1998)
# 12- years dizisinin tüm elemanlarını silin
years.clear()
# 13- kullanıcıdan alacağınız 3 tane marka bilgisini bir listedee saklayın
 
# markalar = []
# for i in range(3):
#     marka = input(f"{i+1}. markayı girin: ")
#     markalar.append(marka)
# print(markalar)