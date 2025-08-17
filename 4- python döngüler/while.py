# 1-100 e kadar
x = 0
while x <= 100:
    if x % 2==0:
        print(x)
    x += 1
print("bitti")

name = "" # False                         ismi boş bırakmamanı sağlıyo faydalı
while not name: #True
    name = input("isminizi girin: ").strip()

print(f"isminiz : {name}")

