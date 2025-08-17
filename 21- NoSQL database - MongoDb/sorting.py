from mongodb_connections import mycollection

# result = mycollection.find().sort("name" ,-1)    # 1: artan -1: azalan
# result = mycollection.find().sort("price" ,1)    # 1: artan -1: azalan
result = mycollection.find().sort([("price" ,1),("price",-1)])    # 1: artan -1: azalan


for i in result:
    print(i)