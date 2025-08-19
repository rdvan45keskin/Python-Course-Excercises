import pymongo

# bilgisayardaki swye bağlanma
# myclient = pymongo.MongoClient("mongodb://localhost:27017")

# bulut swye bağlanma
myclient = pymongo.MongoClient("mongodb+srv://(Linkin gerisini sildim)")
mydb = myclient["node-app"]
# print(myclient.list_database_names())

mycollection = mydb["products"]
# print(mydb.list_collection_names())







