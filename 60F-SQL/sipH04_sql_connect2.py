# -*- coding: utf-8 -*-
#https://www.w3schools.com/python/python_mysql_create_db.asp
import mysql.connector
mydb = mysql.connector.connect( host="localhost", user="root",  passwd="mysql123")
print(mydb)

#create db
mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE dulms")

mycursor.execute("SHOW DATABASES")

for x in mycursor:  print(x)

#create table
import mysql.connector
mydb = mysql.connector.connect(  host="localhost",  user="du",  passwd="mysql123",  database="dulms")
#create user
#create user 'du'@'localhost' identified by 'mysql123'
#grant all privileges on dulms.* to 'du'@'localhost'
mycursor = mydb.cursor()

#create table
mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
#insert data into table
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("John", "Highway 21")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")

val = ("Dhiraj", "Noida")
mycursor.execute(sql, val)
mydb.commit()
print(mycursor.rowcount, "record inserted.")



#read data
mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()
for x in myresult:  print(x)

#selected columns
mycursor.execute("SELECT name, address FROM customers")
myresult = mycursor.fetchall()
for x in myresult:  print(x)
#one row
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchone()
print(myresult)

#where clause
sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:  print(x)

#sort
sql = "SELECT * FROM customers ORDER BY name"
#sql = "SELECT * FROM customers ORDER BY name DESC"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:  print(x)

#delete
sql = "DELETE FROM customers WHERE address = 'Mountain 21'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted")

#drop table
sql = "DROP TABLE customers"
mycursor.execute(sql)

#update
sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")

#limited rows
mycursor.execute("SELECT * FROM customers LIMIT 5")
myresult = mycursor.fetchall()
for x in myresult:  print(x)

#joins
sql = "SELECT   users.name AS user, products.name AS favorite  FROM users INNER JOIN products ON users.fav = products.id"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:  print(x)
#https://www.w3schools.com/python/python_mysql_join.asp


#store data from excel to mysql

sql = "SELECT * FROM pd8"
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:  print(x)


#mysql to pandas
import mysql.connector as sql
import pandas as pd

db_connection = sql.connect(host='localhost', database='dulms', user='du', password='mysql123')
df = pd.read_sql('SELECT * FROM pd8', con=db_connection)
df

#good
