import pyodbc
from connection import conn,cursor


def updateProduct(id, name, price):
    sql = "Update products Set name= ? , Price = ? where id= ?"
    values = (name,price,id)

    try:
        cursor.execute(sql,values)
        conn.commit()
        cursor.execute("SELECT @@ROWCOUNT")
        rowcount = cursor.fetchone()[0]
        print(f"{rowcount} tane kayıt güncellendi")
    except Exception as ex:
        print("hata: ",ex)
    finally:
        conn.close()
        print("bağlantı kapandı")

def getProducts():
    sql = "select * from products"

    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        for i in result:
            print(i)
    except Exception as ex:
        print("hata: ",ex)
    finally:
        conn.close()

ID = input("Hangi ID ile işlem yapılsın: ")
Name = input("Yeni isim ne olsun: ")
Price = input("Yeni fiyat ne olsun: ")

updateProduct(ID,Name,Price)
getProducts()