# regular expression
# arama sonucu birşeyler döndürür veya girilen şeyi kontrol eder

import re
# result = dir(re)
# print(result)

# re module

cumle = "Python Kursu: Python Programlama Rehberiniz | 40 saat"

# re.findall()      # kaç tane belirtilen şeyden var
# result = re.findall("Python",cumle)
# result = len(result)


# re.spilt()        # ifadeyi bbelirtilen şeye göre bölme
# result = re.split(" ",cumle)


# re.sub()          # 1.yi 2.deki belirtilen şeyle değiştirir
# result = re.sub(" ","*",cumle)


# re.search()       # hangi indexler arasında bulduğunu söylüyo
# result = re.search("Python",cumle)
# result = result.span()    # hangi aralıklarda olduğu
# result = result.start()   # hangi indexten başladığı
# result = result.end()     # hangi indexte bittiği
# result = result.group()   # ne bulduğu
# result = result.string    # nerede aratma yaptığımız


# ****regular expression****
"""
    [] arasına yazılan bütün karakterleri tek tek arar
    [0-39] 0 dan üçe kadar ve 9 u ara
    [^abc] a,b ve c dışındaki karakterler 

"""
# result = re.findall("[sat]",cumle)  # s,a,t karakterlerini tek tek arar
# result = re.findall("[a-e]",cumle)    # a dan e ye kadar her karakteri arar

"""
    . - her hangi tek bir karakteri belirtir iki tane nokta olursa ab birleşik arar gibi
"""

# result = re.findall("...",cumle)    #3 lü arar
# result = re.findall("Py..on",cumle) # 2 nokta yerine her hangi bir karakteri koyar

"""
    ^ - string belirtilen karakterle başlıyor mu?
"""

# result = re.findall("^",cumle)   # cümle a ile başlıyor mu

"""
    $ - string belirtilen karakterle bitiyor mu?
"""
# result = re.findall("t$",cumle) # cumle t ile bitiyor mu
"""
    * - bir karakterin 0 yada daha fazla sayıda olmasını kontrol eder
"""
result = re.findall("sa*t",cumle)
"""
    + - bir karakterin 1 yada daha fazla sayıda olmasını kontrol eder
"""
result = re.findall("sa+t",cumle)
"""
    ? - bir karakterin 0 yada 1 kez olmasını kontrol eder
"""
result = re.findall("sa?t",cumle)   #a 2 kere tekrarlıyo diye olumsuz olur
"""
    {} - karakter sayısını kontrol eder
    [0-9]{2,4} en az 2 en fazla 4 basamaklı sayılar
"""
# result = re.findall("a{2}",cumle)
# result = re.findall("[0-9]{2}",cumle)
"""
    | - alternatif seçeneklerden birinin gerçekleşmesi gerekir
    a|b a yada b olsun
"""
"""
    () - gruplamak için kullanılır
    (a|b|c)xz a,b veya c karakterinin arkasından xz gelmelidir
"""
"""
    \ - özel karakterleri aramamızı sağlar
        \$a $karakterinin arkasına a karakteri arar yani
        $ resgular exp. engine tarafından yorumlanmaz.
    
    \A - belirtilen karakter stringin başında mı
        \Athe -- the stringin başında mı
    
    \Z - belirtilen karakter stringin sonunda mı
        the\Z -- the stringin sonunda mı
    
    \b - belirtilen karakter stringin başında yada sonunda mı
        \bthe -- the kelimenin başında mı
        the\b -- the kelimenin sonunda mı

    \B - belirtilen karakter kelimenin başında veya sonunda değil mi
        \Bthe -- the kelimenin başında değil mi
        the\B -- the kelimenin sonunda değil mi

    \d - [0-9] ile aynı anlama gelir yani rakamları arar
        \d -- 12abc12
    
    \D - [^0-9] ile aynı anlama gelir yani rakam olmayanları arar
        \D -- 1ab44_50
    
    \s - boşluk karakterlerini arar
    \S - boşluk karakteri dışındakileri arar
    \W - alfabetik karakterler, rakamlar ve alt çizgi _ karakteri arar
    \w - \w nun dışındakileri arar


"""
result = re.findall("\APython",cumle)
result = re.findall("saat\Z",cumle)
print(result)
