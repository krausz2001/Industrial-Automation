import mysql.connector
db_connection = mysql.connector.connect(host='localhost', user='root', password='', database='automacao')
cursor = db_connection.cursor()

sql = "DELETE FROM tf WHERE 1;"
cursor.execute(sql)

for i in range (1,6):
    sql = "INSERT INTO tf (Silo, Produto, Quantidade) VALUES ({}, '', '0');".format(i)
    cursor.execute(sql)
    
cursor.close()
db_connection.commit()
db_connection.close()