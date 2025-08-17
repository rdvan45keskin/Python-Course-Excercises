import sqlite3

connection = sqlite3.connect("chinook.db")

cursor = connection.cursor()

sql = "select * from customers"

cursor.execute(sql)
results = cursor.fetchall()

for i in results:
    print(i)




connection.close()