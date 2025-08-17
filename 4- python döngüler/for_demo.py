sayilar = [1,3,5,7,9,12,19,21]
# 1- Sayılar listesindeki hangi sayılar 3ün katıdır
for i in sayilar:
    if i%3==0:
        print(i)

# 2- Sayılar listesinde sayıların toplamı kaçtır
toplam = 0
for j in sayilar:
    toplam += j
print(toplam)

# 3- Sayılar listesindeki tek sayıların karesini alın
for i in sayilar:
    if not i%2==0:
        print(i**2)
    
sehirler = ["manisa", "istanbul", "ankara" ,"izmir","antalya"]
# 4- şehirlerden hangileri en fazla 5 karakterlidir
for i in sehirler:
    if len(i) <=5:
        print(i)
urunler = [
    {"name":"samsung S6","price": 3000},
    {"name":"samsung S7","price": 4000},
    {"name":"samsung S8","price": 5000},
    {"name":"samsung S9","price": 6000},
    {"name":"samsung S10","price": 7000}
]
# 5- ürünlerin fiyat toplamı nedir
toplam_fiyat = 0
for urun in urunler:
    toplam_fiyat += urun["price"]

print(f"Ürünlerin toplam fiyatı: {toplam_fiyat} TL")
# 6- ürünlerin fiyatı en fazla 5000 olan ürünleri gösterin
for urun in urunler:
    if urun["price"]<=5000:
        print(urun["name"])