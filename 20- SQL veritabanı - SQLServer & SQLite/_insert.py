import pyodbc

def insertProduct(name, price, imageURL, description):
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


list = []
while True:
    name = input("ürün adı: ")
    price = input("ürün fiyatı: ")
    imageURL = input("ürün resim adı: ")
    description = input("ürün açıklaması: ")

    # insertProduct(name, price, imageURL, description)
    list.append((name, price, imageURL, description))

    result = input("devam etmek istiyor musunuz? (y,n)\n").lower()
    if result == "n":
        print("kayıtlar veritabanına aktarılıyor...")
        print(list)
        insertProducts(list)



