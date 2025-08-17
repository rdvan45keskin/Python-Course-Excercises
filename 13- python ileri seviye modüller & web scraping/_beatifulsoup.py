html_doc = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>index</title>
</head>
<body>
    
    <h1 id="header">
        Python kursu
    </h1>
    <div class="grup1">
        <h2>
            Programlama
        </h2>
        <ul>
            <li>Menü1</li>
            <li>Menü2</li>
            <li>Menü3</li>
        </ul>
    </div>
    <div class="grup2">
        <h2>
            Modüller
        </h2>
        <ul>
            <li>Menü1</li>
            <li>Menü2</li>
            <li>Menü3</li>
        </ul>
    </div>
    <img src="yakuza.jpg" alt="">
    <a href="https://www.leagueoflegends.com/tr-tr/">League of Legends</a>
</body>
</html>
"""
from bs4 import BeautifulSoup

soup = BeautifulSoup(html_doc,"html.parser")
result = soup.prettify()        # boşlukları karıştırılmış olan dosyayı düzenler
result = soup.title             # title bilgisini alır
result = soup.head              # head bilgisini alır
result = soup.body              # body bilgisini alır


result = soup.title.name        # sadece etiket ismini veriyo
result = soup.title.string      # içindeki ifadeyi veriyo

result = soup.h2                # ilk bulduğu h2yi getiriyo

result = soup.find_all("h2")    # tüm h2 leri getiriyo

result = soup.find_all("div")[1]# 1. indexteki divi getiriyo

result = soup.find_all("div")[1].ul.find_all("li")

result = soup.div.findChildren()# bütün alt elemanları getir

result = soup.div.findNextSibling().findNextSibling().findPreviousSibling()   # konumdan bir sondakine geçip bir öncekine geri döndük

result = soup.find_all("a")
for link in result:
    print(link.get("href"))



print(result)