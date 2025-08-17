from mongodb_connections import mycollection
from bson.objectid import ObjectId

#*****delete_one()*****
# for i in mycollection.find():
#     print(i)

# print("*"*50)

# mycollection.delete_one({"name":"Samsung S6"})

# for i in mycollection.find():
#     print(i)


#*****delete_many()*****
for i in mycollection.find():
    print(i)

print("*"*50)

result = mycollection.delete_many({"name":{"$regex":"I"} })
print(f"{result.deleted_count} tane kayıt silindi")

for i in mycollection.find():
    print(i)

#*****bütün kayıtları silme*****
# mycollection.delete_many({})

# for i in mycollection.find():
#     print(i)