# key => value
# bir yerdeki değeri görmek için o değeri belirten anahtar gerekiyo
sehirler = ["manisa","izmir"]
plakalar = [45,35]

print(sehirler[plakalar.index(45)])

# print(plakalar["manisa"]) => 45

# plakalar = {"key" : "value"}

# plakalar = {45 : "manisa", 35 : "izmir"}
# print(plakalar[45])

# plakalar[34] = "istanbul"                     #yeni değer ekleme
# plakalar[45] = "memleket"                     #var olan değeri güncelleme

# print(plakalar)

users = {
    "IndigoApatosarus" : {
        "rank"   : "silver",
        "mains"   : ["akali","irelia","tristana"],
        "lane"   : "mid",
        "server" : "tr"
    },
    "Indigo513" : {
        "rank"   : "gold",
        "mains"   : ["irelia","akali","katarina"],
        "lane"   : "mid",
        "server" : "euw"
    }
}
print(users["IndigoApatosarus"]["mains"][1])
print(users["Indigo513"]["mains"][2])
print(users["Indigo513"]["server"])