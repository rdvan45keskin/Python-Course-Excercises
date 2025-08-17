import pandas as pd

# customers = {
#     "CustomerId" : [1,2,3,4],
#     "FirstName" : ["Ahmet","Ali","Hasan","Canan"],
#     "LastName" : ["Yılmaz","Korkmaz","Çelik","Toprak"]
# }

# orders = {
#     "OrderId" : [10,11,12,13],
#     "CustomerId" : [1,2,5,7],
#     "OrderDate" : ["2010-07-04","2010-08-04","2010-07-07","2012-07-04",]
# }

# df_customers = pd.DataFrame(customers, columns=["CustomerId","FirstName","LastName"])
# df_orders = pd.DataFrame(orders, columns=["OrderId","CustomerId","OrderDate"])

# print(df_customers)
# print(df_orders)

# result = pd.merge(df_customers,df_orders,how="inner")
# result = pd.merge(df_customers,df_orders,how="left")        #bütün müşteriler gelsin sipariş yoksa NaN gelsin
# result = pd.merge(df_customers,df_orders,how="right")       #bütün siparişleri getir müşteri yoksa NaN yaz,
# result = pd.merge(df_customers,df_orders,how="outer")       #sağ ve soldaki bütün kayıtları getirme

customersA = {
    "CustomerId" : [1,2,3,4],
    "FirstName" : ["Ahmet","Ali","Hasan","Canan"],
    "LastName" : ["Yılmaz","Korkmaz","Çelik","Toprak"]
}

customersB = {
    "CustomerId" : [4,5,6,7],
    "FirstName" : ["Yağmur","Çınar","Rıdvan","Cengiz"],
    "LastName" : ["Bilge","Turan","Keskin","Yılmaz"]
}

df_customersA = pd.DataFrame(customersA, columns=["CustomerId","FirstName","LastName"])
df_customersB = pd.DataFrame(customersB, columns=["CustomerId","FirstName","LastName"])

result = pd.concat([df_customersA,df_customersB])               # data frame birleştirme alt alta
result = pd.concat([df_customersA,df_customersB],axis=1)        # data frame birleştirme yan yana
print(result)