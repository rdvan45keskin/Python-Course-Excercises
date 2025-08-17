import requests
from bs4 import BeautifulSoup
url = "https://www.trendyol.com/sr?q=playstation%205&qt=playstation%205&st=playstation%205&os=1"

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0"
}

html = requests.get(url,headers=headers).content
soup = BeautifulSoup(html,"html.parser")

liste = soup.find("div",{"class":"prdct-cntnr-wrppr"}).find_all("div",{"class":"p-card-wrppr with-campaign-view"},limit = 10)
i=1
for item in liste:
    fiyat = item.find("div",{"class":"prc-box-dscntd"}).text
    urunAdi = item.find("div",{"class":"prdct-desc-cntnr"}).text
    print(f"{i}.ürün ismi :  {urunAdi} // Fiyat: {fiyat}")
    i+=1



#----------------------Fiyatları sıralama-------------------
# import requests
# from bs4 import BeautifulSoup

# url = "https://www.trendyol.com/sr?q=playstation%205&qt=playstation%205&st=playstation%205&os=1"

# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0"
# }

# html = requests.get(url, headers=headers).content
# soup = BeautifulSoup(html, "html.parser")

# liste = soup.find("div", {"class": "prdct-cntnr-wrppr"}).find_all("div", {"class": "p-card-wrppr with-campaign-view"}, limit=10)

# urunler = []

# for item in liste:
#     fiyat = item.find("div", {"class": "prc-box-dscntd"}).text
#     urunAdi = item.find("div", {"class": "prdct-desc-cntnr"}).text
    
#     # Fiyatı sayısal değere dönüştür
#     fiyat_sayisal = float(fiyat.replace(" TL", "").replace(".", "").replace(",", "."))
    
#     urunler.append((urunAdi.strip(), fiyat_sayisal))

# # Fiyatına göre sıralama
# urunler_sirali = sorted(urunler, key=lambda x: x[1])

# # Sıralanmış ürünleri yazdırma
# for i, (urunAdi, fiyat) in enumerate(urunler_sirali, 1):
#     print(f"{i}-) {urunAdi} // Fiyat: {fiyat:.2f} TL")
