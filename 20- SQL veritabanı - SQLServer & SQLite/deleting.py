from datetime import datetime
from connection import conn,cursor

def deleteProduct(id):
    sql = "delete from products where id= ?"
    # sql = "delete from products where name like '%?%'"
    values = (id,)

    try:
        cursor.execute(sql,values)
        conn.commit()
        cursor.execute("SELECT @@ROWCOUNT")
        rowcount = cursor.fetchone()[0]
        print(f"{rowcount} tane kayıt silindi")
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

# ID = input("hangi Id silinsin: ")
# deleteProduct(ID)
# getProducts()