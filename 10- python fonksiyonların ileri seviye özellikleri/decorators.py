# def myDecorator(func):            #buraya sayHello değerini gönderdik 12.satırda
#     def wrapper(name):
#         print("fonksiyondan önceki işlemler")
#         func(name)                #func yerine sayHello yazdı ve içindeki name yerine 13.satırdaki işlem uygulandı
#         print("fonksiyondan sonraki işlemler")
#     return wrapper

# @myDecorator
# def sayHello(name):
#     print("hello",name)

# # sayHello = myDecorator(sayHello)
# sayHello("Rıdvan")

import math
import time

# def usAlma(a,b):
#     start = time.time()
#     time.sleep(1)
#     print(math.pow(a,b))
#     finish = time.time()
#     print("fonksiyon "+ str(finish-start)+ "saniye sürdü")

# def faktoriyel(number):
#     start = time.time()
#     time.sleep(1)
#     print(math.factorial(number))
#     finish = time.time()
#     print("fonksiyon "+ str(finish-start)+ "saniye sürdü")

# usAlma(2,3)
# faktoriyel(4)

def calculateTime(func):   
    def inner(*arg,**kwargs):
        start = time.time()
        time.sleep(1)
        func(*arg,**kwargs)
        finish = time.time()
        print("fonksiyon "+func.__name__+ str(finish-start)+ "saniye sürdü")
    return inner
@calculateTime
def usAlma(a,b):
    print(math.pow(a,b))
@calculateTime
def faktoriyel(number):
    print(math.factorial(number))
@calculateTime
def toplama(a,b):
    print(a+b)
usAlma(2,3)
faktoriyel(4)
toplama(10,20)

    