import pyodbc

# SQL Server bağlantı bilgileri
server = 'RIDVANKESKIN\SQLEXPRESS09'   # Sunucu adı, yerel bilgisayar için 'localhost' veya '.' kullanılabilir
database = 'pythonCourse'  # Veritabanı adı

# Bağlantı dizesini oluşturma
connection_string = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'

# Ya da

# connection_string = f"""
#     DRIVER={{SQL Server}};
#     SERVER={server};
#     DATABASE={database};
#     Trusted_Connection=yes;'
# """

try:
    conn = pyodbc.connect(connection_string)
    print("Bağlantı başarılı!")
except Exception as e:
    print("Bağlantı hatası:", e)



# Bir cursor oluşturma
mycursor = conn.cursor()

# Tüm databaseleri görüntüleme
# mycursor.execute("SELECT name FROM sys.databases")
# for x in mycursor:
#     print(x[0])

# Bir sorgu çalıştırma örneği
mycursor.execute("SELECT * FROM products")

# Sonuçları çekme
rows = mycursor.fetchall()

# Sonuçları yazdırma
for row in rows:
    print(row)

# Bağlantıyı kapatma
mycursor.close()
conn.close()
