import mysql.connector
db_connection = mysql.connector.connect(host='localhost', user='root', password='')
cursor = db_connection.cursor()

sql = "DROP database automacao"
cursor.execute(sql)

cursor.close()
db_connection.commit()
db_connection.close()
