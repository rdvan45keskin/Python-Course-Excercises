import pymongo

# bilgisayardaki swye bağlanma
# myclient = pymongo.MongoClient("mongodb://localhost:27017")

# bulut swye bağlanma
myclient = pymongo.MongoClient("mongodb+srv://IndigoApatosarus:1QAZxsw2Ed@cluster0.olkul.mongodb.net/node-app?retryWrites=true&w=majority&appName=Cluster0")
mydb = myclient["node-app"]
mycollection = mydb["products"]

#------ tek kayıt seçme   find_ome()--------
# result = mycollection.find_one()
# print(result)

# ------birden fazla kayıt seçme find()-------- select * from
for i in mycollection.find({},{"_id":0,"name":1}):      # getirmek istediğimiz kolonlara 1 istenmeyenlere 0  {"_id":0,"name":1,"price":1}
    print(i)

