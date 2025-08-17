import numpy as np
# 1- (10,15,30,45,60) değerlerine sahip numpy dizisi oluşturun
result = np.array([10,15,30,45,60])

# 2- (5-15) arasındaki sayılarla numpy dizisi oluşturun
result = np.arange(5,15)

# 3- (50-100) arasında 5 er 5 er artarak numpy dizisi oluşturun
result = np.arange(50,100,5)

# 4- 10 elemanlı 0 lardan oluşan bir dizi oluşturun
result = np.zeros(10)

# 5- 10 elemanlı birlerden oluşan bir dizi oluşturun
result = np.ones(10)

# 6- (0-100) arasında eşit aralıklı 5 sayı üretin
result = np.linspace(0,100,5)

# 7- (10-30) arasında 5 tane tam sayı üretin
result = np.random.randint(10,30,5)

# 8- [-1 ile 1 ] arasında 10 adet rastgele sayı üretin
result = np.random.randn(10)

# 9- (3x5) boyutlarında (10-50) arasında rastgele bir matris oluşturun
result = np.random.randint(10,50,15).reshape(3,5)

# 10- üretilen matrisin satır ve sütun sayıları toplamını hesaplayın
result= np.random.randint(10,50,15).reshape(3,5)
resultx = result.sum(axis=0)
resulty = result.sum(axis=1)
print(resultx,resulty)

# 11- üretilen matrisin en büyük,en küçük ve ortalamasını hesaplayın
max = result.max()
min = result.min()
avr = result.mean()
print(f"max: {max}\nmin: {min}\navr: {avr}")

# 12- üretilen matrisin en büyük değerinin indeksi kaçtır
maxI = result.argmax()
print(f"max Index: {maxI}")

# 13- (10-20) arasındaki dizinin ilk 3 elemanını seçin
array = np.arange(10,20)
result = array[:3]

# 14- üretilen dizinin elemanlarını tersten yazdırın
result = array[::-1]

# 15- üretilen matrisin ilk satırını seçin
matris = np.random.randint(10,50,15).reshape(3,5)
print(matris)
result = matris[0]

# 16- üretilen matrisin 2.satır 3.sütundaki eleman nedir
result = matris[1,2]

# 17- üretilen matrisin tüm satırlardaki ilk elemanını seçim
result = matris[:,0]

# 18- üretilen matrisin her bir elemanının karesini alın
result = matris**2

# 19- üretilen matris elemanlarının hangisi pozitif çift sayıdır
#     aralığı (-50,+50) arasında yapın
matris2 = np.random.randint(-50,50,15).reshape(3,5)
print(matris2)
cift = matris2[matris2%2==0]
result = cift[cift>0]

print(result)