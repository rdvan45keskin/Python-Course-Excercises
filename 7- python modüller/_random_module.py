import random
# result = dir(random)
# result = help(random)

result = random.random() # 0.0 - 1.0 sayı üretcek
result = random.random()*100
result = random.uniform(1,10)
result = random.randint(1,100)

greeting = "hello there"
names = ["ali","yağmur","deniz","cenk","ahmet","efe"]
# result = names[random.randint(0,len(names)-1)]

result = random.choice(names)   # listeden rastgele bir elemanı seçip getiriyo
result = random.choice(greeting)

liste = list(range(10))
random.shuffle(liste)           # listedeki elemanları karıştırıyo
result = liste

liste = range(100)
result = random.sample(liste,3) # listeden rastgele belirlenen kadar eleman çekiyo
result = random.sample(names,3)
print(result)