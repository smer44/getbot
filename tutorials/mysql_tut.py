'''
Mysql connector for python

https://www.w3schools.com/python/python_mysql_create_db.asp

installing the module: 

I had the same problem and passing auth_plugin='mysql_native_password' did not work, because I accidentally installed mysql-connector instead of mysql-connector-python


pip3 install mysql-connector-python

or else pip3 install mysql.connector will need microsoft visual tools


installng mysql server :

https://dev.mysql.com/get/Downloads/MySQLInstaller/mysql-installer-community-8.0.19.0.msi



'''

db_user = "root"

db_pw = "root"

database="tutorials"

import mysql.connector # needs mucrosoft visual tools

print(mysql.connector)

mydb = mysql.connector.connect(
  host="localhost",
  user=db_user,
  password=db_pw,
  database="tutorials", # also it is called schema in mysql programs
  auth_plugin='mysql_native_password'
)

mycursor = mydb.cursor()

#mycursor.execute("CREATE DATABASE tutorials")

mycursor.execute("SHOW DATABASES")# returns none

for x in mycursor:
    print(x)

#mycursor.execute("CREATE TABLE cats (id INT,  uri VARCHAR(255))")
mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)  

#inserting an entry: 





sql = "INSERT INTO cats (id , uri) VALUES (%s, %s)"

val = (42, 'test_string')
mycursor.execute(sql, val)

#Important!: Notice the statement: mydb.commit(). It is required to make the changes, otherwise no changes are made to the table.
mydb.commit()

print(mycursor.rowcount, "record inserted.")

# wohoo, it is working !!!


# read from database: 

mycursor.execute("SELECT * FROM cats")

#Note: We use the fetchall() method, which fetches all rows from the last executed statement.
myresult = mycursor.fetchall()

for x in myresult:
    print(x)


#delete entries 

sql = "DELETE FROM cats WHERE id = 42"

mycursor.execute(sql)

#Important!: Notice the statement: mydb.commit(). It is required to make the changes, otherwise no changes are made to the table.
mydb.commit()

print(mycursor.rowcount, "record(s) deleted")

"""
sql = "DROP TABLE customers"

mycursor.execute(sql)

"""

