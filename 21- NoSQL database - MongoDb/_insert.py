import pymongo

# bilgisayardaki swye bağlanma
# myclient = pymongo.MongoClient("mongodb://localhost:27017")

# bulut swye bağlanma
myclient = pymongo.MongoClient("mongodb+srv://IndigoApatosarus:1QAZxsw2Ed@cluster0.olkul.mongodb.net/node-app?retryWrites=true&w=majority&appName=Cluster0")
mydb = myclient["node-app"]
# print(myclient.list_database_names())

mycollection = mydb["products"]
# print(mydb.list_collection_names())

# -------bir kayıt ekleme---------
# product = {"name":"Samsung S5", "price": 2000}

# result = mycollection.insert_one(product)

# print(result)
# print(type(result))
# print(result.inserted_id)

# -------birden fazla kayıt ekleme---------
productList = [
    {"_id":1,"name":"Samsung S6", "price": 3000, "description":"iyi telefon"},
    {"name":"Samsung S7", "price": 4000, "categories":["telefon","elektronik"]},
]

result = mycollection.insert_many(productList)
print(result.inserted_ids)