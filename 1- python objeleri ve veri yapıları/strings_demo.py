website = "http://www.leagueoflegends.com"
course  = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 Saat)"

# 1- "course" karakter dizisinde kaç karakter bulunmaktadır
result1=len(course)
print(result1)

# 2- "website" içinden www karakterlerini alın.
print(website[7:10])

# 3- "website" içinden com karakterlerini alın.
print(website[-3:])

# 4- "course" içinden ilk 15 ve son 15 karakterlerini alın
print(course[:15])
print(course[-15:])

# 5- "course" ifadesindei karakterleri tersten yazdırın
print(course[::-1])

name, surname ,age ,job = "Bora","Yılmaz", 32, "mühendis"

# 6- yukarıda verilen değişkenler ile ekrana aşağıdaki cümleyi yazdırın
#     "benim adım bora yılmaz, yaşım 32 ve mesleğim mühendis
print(f"benim adım {name} {surname}, yaşım {age} ve mesleğim {job}")

# 7- "hello world" ifadesindeki w harfini "W" ile değiştirin
s = "hello world"
s = s[0:6] + "W" +s[-4:]
s.replace("w","W")
print(s)

# 8- "abc" ifadesini yan yana 3 defa yazdırın
word="abc"
print(word*3)