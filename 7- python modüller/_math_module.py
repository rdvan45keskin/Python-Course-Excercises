# *************Yöntem 1**************
# import math
# import math as islem

# # value = dir(math)
# # value = help(math)
# # value = help(math.factorial)
# # value = math.factorial(5)
# # value = math.ceil(5.9)

# value = islem.factorial(5)

# *************Yöntem 2**************
# from math import *
def sqrt(x):                                #hangisi en son tanımlanırsa o fonksiyonu önce kullanır
    print("x: "+str(x))

from math import factorial,sqrt
value = factorial(5)
value = sqrt(9)
print(value)