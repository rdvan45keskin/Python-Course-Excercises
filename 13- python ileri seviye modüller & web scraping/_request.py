import requests
import json

result = requests.get("https://jsonplaceholder.typicode.com/todos")
result = json.loads(result.text)   # json.load ile string bilgiyi listeye çevvirip işlem yapabilmeyi sağlıyo

# print(result[0]["title"])

for i in result:
    if i["userId"] == 1: 
        print(i["title"])

