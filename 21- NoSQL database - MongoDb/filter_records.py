import pymongo
from bson.objectid import ObjectId

# bilgisayardaki swye bağlanma
# myclient = pymongo.MongoClient("mongodb://localhost:27017")

# bulut swye bağlanma
myclient = pymongo.MongoClient("mongodb+srv://(Linkin gerisini sildim)")
mydb = myclient["node-app"]
mycollection = mydb["products"]

# filter = {"name":"Samsung S5"}
# result = mycollection.find(filter)
# --------idye göre sorgulama--------
# result = mycollection.find_one({"_id":ObjectId("66d181f4eabdcaff554b1efb")})


# result = mycollection.find({
#     "name": {
#         "$in" :  ["Samsung S5","Samsung S6"]    # içinde ["Samsung S5","Samsung S6"] geçenleri getir
#     }
# })
# for i in result:
#     print(i)
# print(result)


# result = mycollection.find({
#     "price": {
#         "$gt" :  2000    # değerden büyük veya küçük olanları getirme (greater than) veya lt (less than)
#     }
# })
# for i in result:
#     print(i)

# print(result)

# result = mycollection.find({
#     "price": {
#         "$gte" :  2000    # değerden büyük eşit veya küçük eşit olanları getirme (greater than equeal) veya (less than equeal)
#     }
# })
# for i in result:
#     print(i)

# print(result)


# result = mycollection.find({
#     "price": {
#         "$eq" :  2000    # değere eşit olanları getirme (equeal)
#     }
# })
# for i in result:
#     print(i)

# print(result)


# $or, $and, $not, $nor 

result = mycollection.find({
    "name": { "$regex": "^S"}
})
for i in result:
    print(i)

