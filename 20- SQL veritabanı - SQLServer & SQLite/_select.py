import pyodbc
from connection import conn,cursor

def insertProduct(name, price, imageURL, description):
    sql = "INSERT INTO products(name,price,imageURL,description) OUTPUT INSERTED.id VALUES (?,?,?,?)"
    values = (name, price, imageURL, description)

    try:
        cursor.execute(sql, values)
        print(f"{cursor.rowcount+2} tane kayıt eklendi")
        last_id = cursor.fetchone()[0]  # OUTPUT INSERTED.ID ile dönen son eklenen ID'yi alır
        print(f"Son eklenen kaydın ID numarası: {last_id}")
    except Exception as e:
        print("Hata:", e)
    finally:
        conn.close()
        print("Database bağlantısı kapandı")



def insertProducts(list):
    server = 'RIDVANKESKIN\SQLEXPRESS09'   # Sunucu adı, yerel bilgisayar için 'localhost' veya '.' kullanılabilir
    database = 'pythonCourse'  # Veritabanı adı
    
    connection_string = f"""
        DRIVER={{SQL Server}};
        SERVER={server};
        DATABASE={database};
        Trusted_Connection=yes;'
    """
    try:
        conn = pyodbc.connect(connection_string)
        conn.autocommit = True
        print("Bağlantı başarılı!")
    except Exception as e:
        print("Bağlantı hatası:", e)

    cursor = conn.cursor()

    sql = "INSERT INTO products(name,price,imageURL,description) OUTPUT INSERTED.id VALUES (?,?,?,?)"
    values = list

    try:
        cursor.executemany(sql, values)
        print(f"{cursor.rowcount+1+len(list)} tane kayıt eklendi")
        last_id = cursor.fetchone()[0]  # OUTPUT INSERTED.ID ile dönen son eklenen ID'yi alır
        print(f"Son eklenen kaydın ID numarası: {last_id}")
    except Exception as e:
        print("Hata:", e)
    finally:
        conn.close()
        print("Database bağlantısı kapandı")


def getProducts():
    cursor.execute("SELECT * FROM products order by price desc")
    # cursor.execute("SELECT * FROM products order by price desc")                              # order by
    # cursor.execute("SELECT * FROM products  Where name like '%Samsung%' and price='3000'")    # like
    # cursor.execute("SELECT name,price FROM products")

    try:
        result = cursor.fetchall()      # for döngüsü oluşturulur
        # result = cursor.fetchone()    # for döngüsü oluşturulamaz tek bir bilgiyi seçer

        for i in result:
            print(f"id: {i[0]} name: {i[1]} price: {i[2]}")
            # print(f"name: {i[0]} price: {i[1]}")
    except Exception as ex:
        print("hata: ",ex)
    finally:
        conn.close()
        print("bağlantı kapandı")

def getProductById(id):
    sql = "SELECT * FROM products  Where id=?"
    params = (id,)

    cursor.execute(sql,params)

    result = cursor.fetchone()

    print(f"id: {result[0]} name: {result[1]} price: {result[2]}")

getProducts()
# getProductById(3)

# list = []
# while True:
    # name = input("ürün adı: ")
    # price = input("ürün fiyatı: ")
    # imageURL = input("ürün resim adı: ")
    # description = input("ürün açıklaması: ")

    # # insertProduct(name, price, imageURL, description)
    # list.append((name, price, imageURL, description))

    # result = input("devam etmek istiyor musunuz? (y,n)\n").lower()
    # if result == "n":
    #     print("kayıtlar veritabanına aktarılıyor...")
    #     print(list)
    #     insertProducts(list)

