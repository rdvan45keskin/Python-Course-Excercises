name = "Rıdvan"
surname = "Keskin"
age = 21
greeting = "My name is "+ name + " "+ surname + " and \nI am "+ str(age) + " years old."
length = len(greeting)

# stringler harflerin bir dizide birleşmesi olduğu için her harfi diziyle çağırabiliyoz

# print(greeting)
# print(greeting[0]) 
# print(greeting[3])
# print(greeting[-1])
# print(greeting[length-1]) === print(greeting[-1])
print(greeting[3:7]) # 3 ten başlayıp 7 ye kadar 7 dahil değil
print(greeting[3:])  # 3 ten sonuna kadar git
print(greeting[:7])  # en baştan 7 ye kadar git 7 dahil değil
print(greeting[2:40:2]) # 2 den başlayıp 40 a kadar 2 şer 2 şer git 
