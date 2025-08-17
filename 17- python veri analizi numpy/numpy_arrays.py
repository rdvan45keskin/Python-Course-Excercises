import numpy as np

# result = np.array([1,3,5,7,9])
# result = np.arange(1,10)            # 1 den 10a kadar 10 dahil değil aradaki tüm sayılarla dizi oluştur
# result = np.arange(10,100,5)
# result = np.zeros(10)               # belirtilen sayı kadar 0 lardan oluşan dizi
# result = np.ones(10)                # belirtilen sayı kadar 1 lerden oluşan dizi
# result = np.linspace(0,100,5)       # belirtilen 2 sayı arasını 3. belirtilen sayıya ayır
# result = np.random.randint(0,10)    # belirtilen değerler arasında sayı üret
# result = np.random.randint(20)      # 0 dan belirtilen değere kadar random sayı üret
# result = np.random.randint(1,10,3)  # rastgele 3 sayı getir
# result = np.random.rand(5)          # 0 ve 1 arasında belirtilen değer kadar sayı üret
# result = np.random.rand(5)          # eksili sayılar işe girer
# np_array = np.arange(50)
# np_multi = np_array.reshape(5,10)     # 5 - 10 luk matris oluştur
# print(np_multi.sum(axis=1))         # satırların toplamı
# print(np_multi.sum(axis=0))         # sütunların toplamı

rnd_number = np.random.randint(1,100,10)
print(rnd_number)
# result = rnd_number.max()           # max sayı
# result = rnd_number.min()           # min sayı
# result = rnd_number.mean()          # sayıların ortalaması
# result = rnd_number.argmax()        # en büyük sayının indexsini verir
# result = rnd_number.argmin()        # en küçük sayının indexsini verir

# print(result)
