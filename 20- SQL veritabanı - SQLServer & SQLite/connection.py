import pyodbc

server = 'RIDVANKESKIN\SQLEXPRESS09'
database = 'schooldb'
database = 'pythonCourse'


connection_string = f"""
    DRIVER={{SQL Server}};
    SERVER={server};
    DATABASE={database};
    Trusted_Connection=yes;
"""

try:
    conn = pyodbc.connect(connection_string)
    conn.autocommit = True      # yönetici mod açmak gibi bişey her şeyi yaptırıyo
    cursor = conn.cursor()
    print("Bağlantı başarılı!")
except Exception as e:
    print("Bağlantı hatası:", e)