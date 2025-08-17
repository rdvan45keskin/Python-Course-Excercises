# def greeting(name):
#     print("hello",name)

# print(greeting("ali"))
# print(greeting)

# sayHello = greeting         # datanın adresini eşliyo
# print(sayHello)
# print(greeting)

# print(greeting("ali"))
# print(sayHello("ali"))

# del sayHello
# print(greeting)

# encaapsulation
# def outer(num1):
#     print("outer:",num1)
#     def inner_increment(num1):
#         print("outer:",num1)
#         return num1 + 1
#     num2 = inner_increment(num1)
#     print(num1,num2)

# outer(10)

def factorial(number):
    if not isinstance(number,int):
        raise TypeError("gönderilen bilgi sayı olmalı")
    
    if not number >=0:
        raise ValueError("sayı 0 veya 0 dan büyük olmalı")

    def inner_factorial(number):
        if number <=1:
            return 1
        
        return number * inner_factorial(number-1)
    
    return inner_factorial(number)
try:
    print(factorial(8))
except Exception as ex:
    print(ex)