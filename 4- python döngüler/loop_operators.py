# Range                   ---

# for i in range(50,100,10): #başlangıç,bitiş,kaçar artacağı
#     print(i)
# print(list(range(50,100,10)))

# enumerate               ---karakterlerin indeksini yazıyo

# index = 0
# greeting = "hello there"
# for letter in greeting:
#     print(f"index: {index} letter: {letter}")
#     index += 1

# greeting = "hello"
# for index,letter in enumerate(greeting):
#     print(f"index: {index} letter: {letter}")

# zip                     ---listeleri birleştiriyomuş

list1 = [1,2,3,4,5]
list2 = ["a","b","c","d","e"]
list3 = [100,200,300,400,500]

print(list(zip(list1,list2,list3)))

for item in (zip(list1,list2,list3)):
    print(item)

for a,b,c in (zip(list1,list2,list3)):
    print(a,b,c)