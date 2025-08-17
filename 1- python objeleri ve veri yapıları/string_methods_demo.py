website = "http://www.leagueoflegends.com"
course  = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 Saat)"

# 1- " hello world " karakter dizisinin baş ve sondaki boşluklarını kaldırın
word1 = " hello world ".strip()
print(word1)

# 2- "www.leagueoflegends.com" içindeki leagueoflegends bilgisi hariçi her şeyi silin
word2 = "www.leagueoflegends.com".split(".")
print(word2[1])
result = "www.leagueoflegends.com".strip("w.com")
print(result)
# 3- "course" karakter dizisinin tüm karakterlerini küçük harf yapın
word3 = course.upper()
word3 = course.title()
word3 = course.lower()
print(word3)

# 4- "website" içinde kaç a karakteri vardır count("a")
count = website.count("a")
count = website.count("a",0,10)
print(count)
count2 = website.split("a")
print(len(count2)-1)

# 5- "website" www ile başlayıp com ile bityor mu
isStart = website.startswith("www")
isEnd = website.endswith("com")
print(isStart,isEnd)

# 6- "website" içinde .com ifadesi var mı
isFind = website.find(".com")
if(isFind>0):
    print("true")
else:
    print("false")

# 7- "course" içindeki karakterlerin hepsi alfabetik mi (isalpha,isdigit)
isAlpha = course.isalpha()
print(isAlpha)

# 8- "contents" ifadesini satırda 50 karakter içine yerleştirip sağına ve soluna "*" ekleyin
word8 = "contents".center(50,"*")
print(word8)

# 9- course karakter dizisindeki tüm boşluk karakterlerini "-" ile değiştirin
replacement = course.replace(" ","-")

# 10- "hello world" karakter dizisinin "world" ifadesini "there" olarak değistirin
word10 = "hello world".replace("world","There")
print(word10)
# 11- "course" karakter dizisini boşluk karakterlerine göre ayırın
spliting = course.split(" ")
print(replacement)