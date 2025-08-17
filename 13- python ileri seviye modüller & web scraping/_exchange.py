import requests
import json

apiUrl = "https://v6.exchangerate-api.com/v6/73923c57c297e3030cc4ad20/latest/"#bozulan döviz girio buraya

bozulan_doviz = input("bozulan döviz türü: ") #usd
alinan_doviz = input("alınan döviz türü: ") #try
miktar = int(input(f"ne kadar {bozulan_doviz} bozdurmak istiyorsunuz: "))

sonuc = requests.get(apiUrl + bozulan_doviz)            #urlnin sonuna bozulacak dövizi getirip görüntüleme
sonuc_json = json.loads(sonuc.text)                     #jsonu pythonda kullanmak için dönüştürme

doviz_kuru = sonuc_json["conversion_rates"][alinan_doviz]       #gelen bilgilerden "conversion_rates" bölümünden alınmak istenen dövizin bilgileri seçiliyor
# print(sonuc_json["conversion_rates"][alinan_doviz])       

print(f"1 {bozulan_doviz} = {doviz_kuru} {alinan_doviz}")
print(f"{miktar} {bozulan_doviz} = {miktar *doviz_kuru:.4f} {alinan_doviz}")