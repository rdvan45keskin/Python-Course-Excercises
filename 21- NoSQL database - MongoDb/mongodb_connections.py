import pymongo

# bilgisayardaki swye bağlanma
# myclient = pymongo.MongoClient("mongodb://localhost:27017")

# bulut swye bağlanma
myclient = pymongo.MongoClient("mongodb+srv://IndigoApatosarus:1QAZxsw2Ed@cluster0.olkul.mongodb.net/node-app?retryWrites=true&w=majority&appName=Cluster0")
mydb = myclient["node-app"]
# print(myclient.list_database_names())

mycollection = mydb["products"]
# print(mydb.list_collection_names())







