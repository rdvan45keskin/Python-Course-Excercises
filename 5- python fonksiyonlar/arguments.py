# def changeName(n):
#     n = "Indigo"

# name = "Wixen"

# changeName(name)
# print(name)

# def change(n):
#     n[0] = "istanbul"

# sehirler = ["ankara", "izmir"]
# n = sehirler[:]         #diziyi n ye kopyalama
# n[0]= "istanbul"
# print(sehirler)
# print(n)

# def change(n):
#     n[0] = "istanbul"

# sehirler = ["ankara", "izmir"]
# n = sehirler[:]         #diziyi n ye kopyalama
# change(sehirler[:])
# print(sehirler)
# print(n)

# def add(*params):
#     print(params)
#     return sum((params))
# print(add(10,20))
# print(add(10,20,30))
# print(add(10,20,30,40,50,60,70,80,90,100))

# def add(*params):
#     sum = 0
#     for i in params:
#         sum = sum + i
#     return sum

# print(add(10,20))

def displayUser(**veri):
    print(type(veri))
    for key , value in veri.items():
        print(f"{key} is {value}")



displayUser(name = "Rıdvan", age = 21, city = "manisa")
displayUser(name = "Indigo", age = 30, city = "London",phone = "123456")
displayUser(name = "Wixen", age = 24, city = "Tokyo",phone = "453158",gender = "female")

def myFunc(a,b,*args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
myFunc(10,20,30,40,50, key1 = "value" ,key2 = "value2")

