import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/toptv/?ref_=nv_tvv_250"

headers = { # chromeda f12 bastıktan sonra networke tıklayıp yukardaki urlye tıkladıktan sonra "User-Agent"te yazan şeyi buraya kopyalıyoz safari yazan yere kadar
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0"
}

html = requests.get(url, headers=headers).content
soup = BeautifulSoup(html,"html.parser")

liste = soup.find("ul",{"class":"ipc-metadata-list"}).find_all("li",limit=10)    # belirtilen classtaki ul nin limitte belirtilen kadar li elemanını listele

for item in liste:
    filmadi = item.find("h3",{"class":"ipc-title__text"}).text      #yukarda bulunan li elemanlarının her birinde belirtilen classtaki h3 elemanını arar ve text ile içindeki metni seçer
    puan = item.find("span",{"class":"ipc-rating-star"}).text
    print(f"{filmadi} // Puan: {puan}")
    

