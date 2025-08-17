fruits = {"orange", "apple", "banana"}

# print(fruits[0])   indexlenemez

for i in fruits:
    print(i)

fruits.add("cherry")
fruits.update(["mango","grape","apple"])
fruits.remove("mango")
fruits.discard("apple")

print(fruits)

fruits.pop()

fruits.clear()

print(fruits)

myList = [1,2,5,4,4,2,1]
print(myList)
print(set(myList))    #tekrarlayan elemanları 1 kere yazar