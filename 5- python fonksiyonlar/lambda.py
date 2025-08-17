# def square(num):
#     return num **2
# numbers = [1,3,5,9]

# result = list(map(square,numbers))   #listenin içindeki her değeri fonksiyonda işleme sokar

# for item in map(square,numbers):
#     print(item)

# print(result)

# numbers = [1,3,5,9]

# result = list(map(lambda num: num ** 2,numbers))

# print(result)

# numbers = [1,3,5,9]

# square = lambda num: num ** 2

# result = list(map(square,numbers))
# print(result)
# result = square(3)
# print(result)

numbers = [1,3,5,9,10]

# def check_even(num):
#     return num%2==0
# result = list(filter(check_even,numbers))
# print(result)

result = list(filter(lambda num: num%2==1,numbers))
print(result)