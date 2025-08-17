message = "Hello There. My name is Rıdvan Keskin"

# message = message.upper()                     #tüm harfleri büyük harf yapar
# message = message.lower()                     #tüm harfleri küçük harf yapar
# message = message.title()                     #kelimelerin baş harflerini büyük yapar
# message = message.capitalize()                #cümledeki ilk harfi büyük yapar

# message = message.strip()                     #başta veya sonraki boşlukları siler
# message = message.split()                     #boşluklara göre kelimeleri dizi elemanları olarak böler
# message = message.split(".")                  #girilen parametreye göre ayırır
# message = "---".join(message)                 #parçalanan kelimeleri birleştirir ve önüne yazılan şeyleri aralara ekler

# index = message.find("Rıdvan")                #cümlenin içinde bu kelimenin kaçıncı indexte olduğunu yazar yoksa -1 yazar
# isFound = message.startswith("H")             #değerin verilen parametle ile başlayıp başlamadığını sorgular
# isFound = message.endswith("n")               #değerin verilen parametle ile bitip bitmediğini sorgular

# message = message.replace("Rıdvan","Indigo")  #birinci parametreyi bulup ikinci parametre ile değiştir

# message = message.center(50,"*")              #50 karakter içine sığdırır ve tam ortalar

print(message)