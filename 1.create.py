import mysql.connector
db_connection = mysql.connector.connect(host='localhost', user='root', password='')
cursor = db_connection.cursor()

sql = "CREATE DATABASE automacao"
cursor.execute(sql)

sql = "USE automacao"
cursor.execute(sql)

table = "CREATE table tf(Silo int(5) not null,Produto varchar(30),Quantidade int(11),primary key(Silo))"
cursor.execute(table)
for i in range (1,6):
           sql = "INSERT INTO tf (Silo, Produto, Quantidade) VALUES ({}, '', '0');".format(i)
           cursor.execute(sql)

cursor.close()
db_connection.commit()
db_connection.close()
