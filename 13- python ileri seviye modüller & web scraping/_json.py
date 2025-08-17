import json

person_string = '{"name":"Rıdvan","languages":["Python","C#"]}'     #json
person_dict   =  {"name":"Rıdvan","languages":["Python","C#"]}      #dict
# result = person["name"]
# result = person["languages"][0]

#----Json string to dict----
result = json.loads(person_string)      # jsonu dicte çevirio
# result = result["name"]

# with open("person.json",encoding="utf-8") as f:
#     data = json.load(f)
#     print(data["name"])

#----Dict to Json----

# result = json.dumps(person_dict, ensure_ascii=False)        # dict bilgiyi jsona çeviriyo ve türkçe karakterlere ellemiyo string bilgi diye geçiyo

# with open("person.json","w",encoding="utf-8") as f:         #dosyaya yazma
#     json.dump(person_dict,f,ensure_ascii=False)

person_dict = json.loads(person_string)
result = json.dumps(person_dict, indent=4, sort_keys=True,ensure_ascii=False)
print(result)


# JSON Verisini Bir Dosyadan Okumak (json.load):
# JSON Verisini Pytyon veri yapısına dönüştürmek (json.loads):
# Python Veri Yapısını JSON Dosyasına Yazmak (json.dump):
# Python Veri Yapısını JSON Formatına Dönüştürmek (json.dumps):