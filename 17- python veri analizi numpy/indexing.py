import numpy as np


numbers = np.array([0,5,10,15,20,25,50,75])

result = numbers[5]
result = numbers[-1]
result = numbers[0:3]
result = numbers[3:]
result = numbers[::]
result = numbers[::-1]  #listeyi döndür


numbers2 = np.array([[0,5,10],[15,20,25],[50,75,85]])
result = numbers2[0]
result = numbers2[2][0]
result = numbers2[2,0]
result = numbers2[:,2]          # her satırdaki 2. indexleri seçioz
result = numbers2[:,0]
result = numbers2[:,0:2]
result = numbers2[-1,:]
result = numbers2[:2,:2]



# print(result)

arr1 = np.arange(0,10)
# arr2 = arr1 # referans adresi kopyaladık
arr2 = arr1.copy()              # farklı adreslerde olacaklar

print(arr1)
print(arr2)

arr2[0] = 20

print(arr1)
print(arr2)



