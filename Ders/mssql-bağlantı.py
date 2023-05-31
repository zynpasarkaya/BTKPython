
import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "mysql123"
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE mydatabase") #database oluşturma

'''mycursor.execute("SHOW DATABASES") #dtagösterme
for x in mycursor:
     print(x)'''



mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "mysql123"
    database = "mydb"
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")