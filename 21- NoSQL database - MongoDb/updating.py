from mongodb_connections import mycollection
from bson.objectid import ObjectId

# *****update_one*****

# for i in mycollection.find():
#     print(i)

# mycollection.update_one(
#     {"name": "Samsung S6"},
#     {"$set": {
#         "name": "Iphone 7",
#         "price": 5000
#     }}
# )

# for i in mycollection.find():
#     print(i)


# *****update_many*****

for i in mycollection.find():
    print(i)

result = mycollection.update_many(
    {"name": "Samsung S7"},
    {"$set": {
        "name": "Iphone 8",
        "price": 7000
    }}
)

print(f"{result.modified_count} adet kayıt güncellendi.")

for i in mycollection.find():
    print(i)