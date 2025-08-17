import os
import datetime
from datetime import datetime

# print(dir(os))
# result = os.name

#*** dizin değiştirme ***  
# os.chdir("C:\\Users\\Rıdvan Keskin\\Desktop")   # dosya yolu belirtir
# os.chdir("..")                                  # bir üst klasöre geçer



#*** klasör oluşturma ***
# os.mkdir("yeniDosya")                           # dosya oluşturur
# os.makedirs("newdirectory/yeni klasör")         # iç içe dosya oluşturur
# os.rename("newdirectory/yeniklasör")            # dosyanın adını yeniklasör olarak değiştirir
# os.rmdir("yeniklasör")                          # belirtilen dosyayı siler alt klasör yoksa
# os.removedirs("yeniklasör/yeniklasör")          # alt klasörü siler



#*** listeleme ***
# result = os.listdir()                           # dosyanın içindeki her şeyi gösterir
# result = os.listdir("D:\\")
# for dosya in os.listdir():                      # dosyanın içinden belli şeyleri seçme
#     if dosya.endswith(".py"):
#         print(dosya)



#*** etkin dizin öğrenme ***
# result = os.getcwd()                            # dosyanın yolunu veriyor

# result = os.stat("_datetime.py")
# result = result.st_size/1024                    # dosyanın kb cinsinden boyutu
# result = datetime.fromtimestamp(result.st_ctime)# dosyanın oluşturulma zamanı
# result = datetime.fromtimestamp(result.st_atime)# son erişilme tarihi
# result = datetime.fromtimestamp(result.st_mtime)# son değiştirilme tarihi

# os.system("notepad.exe")                        # uygulama çalıştırma

# ***path***
result = os.path.abspath("_os.py")              # belirtilen şeyin konumunu verir
result = os.path.dirname("C:/Users/Rıdvan Keskin/Documents/dersler/btk/python/13- python ileri seviye modüller & web scraping/_os.py")
result = os.path.dirname(os.path.abspath("_os.py")) # dosyayı bulup ona giden yolu veriyo
result = os.path.exists("_os.py")               # böyle bir şey var mı yokmu true false
result = os.path.isdir("")                      # klasör müdür diye soruyor
result = os.path.isfile("_os.py")               # dosya mıdır diye sorar

result = os.path.join("C:\\","deneme","deneme1")# yol oluşturma ama bulunamıyo
result = os.path.split("C:\\deneme")            # yolu bölüyo
result = os.path.splitext("_os.py")             # uzantısını ayırıyo
# result = result[0]
result = result[1]
print(result)