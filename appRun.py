import mysql.connector
mydb = mysql.connector.connect(
    host="localhost",
    database="klambi_db",
    user="root",
    passwd="root"
)

print(mydb)

sql_select_Query = "select * from user"
cursor = mydb.cursor()
cursor.execute(sql_select_Query)
records = cursor.fetchall()

for row in records:
    print(row)