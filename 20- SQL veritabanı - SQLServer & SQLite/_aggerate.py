import pyodbc
from connection import conn,cursor

def getProductInfo():
    # sql = "SELECT count(id) FROM products where price>=2000"
    # sql = "SELECT avg(price) FROM products"
    # sql = "SELECT sum(price) FROM products"
    # sql = "SELECT min(price) FROM products"
    # sql = "SELECT max(price) FROM products"
    sql = "SELECT name,price FROM products where Price = (SELECT max(price) FROM products)" # en pahalı ürünün adı
    cursor.execute(sql)

    result = cursor.fetchone()

    print(f"result: {result[0]}   {result[1]}")
    # print(f"id: {result[0]} name: {result[1]} price: {result[2]}")

getProductInfo()