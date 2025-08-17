# name = "Rıdvan Keskin"

# for letter in name:
#     if(letter) == "a":
#         break           #a görünce döngü bitiyo
#         continue        #a yı esgeçip devam ediyo
#     print(letter)

# x = 0

# while x < 5:
#     x+=1
#     if x == 2:
#         continue
#     print(x)
    
# 1-100 e kadar tek sayıların toplamı

x = 0
toplam = 0
while x <= 100:
    x+=1
    if x % 2 == 0:
        continue
    toplam+=x
    
print(toplam)