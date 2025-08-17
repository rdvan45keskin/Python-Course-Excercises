import pyodbc
from connection import conn,cursor

def getProducts():
    sql = "select * from products"
    sql = "select * from categories"
    sql = "select * from products p inner join categories c on p.categoryid=c.id"
    sql = "select p.name,p.price,c.name from products p inner join categories c on p.categoryid=c.id where c.name='bilgisayar'"

    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        for i in result:
            print(i)
    except Exception as ex:
        print("hata: ",ex)
    finally:
        conn.close()

getProducts()