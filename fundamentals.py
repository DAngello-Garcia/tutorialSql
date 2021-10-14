dbPass = "1q2w3e4r" #https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/removing-sensitive-data-from-a-repository
                    #https://stackoverflow.com/questions/2397822/what-is-the-best-practice-for-dealing-with-passwords-in-git-repositories
'''
# #Structured Query Language

Data Definition Language
CREATE, ALTER, DROP, TRUNCATE

Data Manipulation Language
 SELECT, INSERT, UPDATE, DELETE
Data Control Language
 GRANT, REVOKE

Transaction Control Language
 COMMIT, ROLLBACK, SAVEPOINT

 Cláusulas
 FROM, WHERE, GROUP BY, HAVING, ORDER BY

'''
import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="admin", password=dbPass, database="firstdb")
mycursor = mydb.cursor()
#mycursor.execute("CREATE DATABASE mydatabase")

#mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

#mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# mycursor.execute(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "record inserted.")

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = [
#   ('Peter', 'Lowstreet 4'),
#   ('Amy', 'Apple st 652'),
#   ('Hannah', 'Mountain 21'),
#   ('Michael', 'Valley 345'),
#   ('Sandy', 'Ocean blvd 2'),
#   ('Betty', 'Green Grass 1'),
#   ('Richard', 'Sky st 331'),
#   ('Susan', 'One way 98'),
#   ('Vicky', 'Yellow Garden 2'),
#   ('Ben', 'Park Lane 38'),
#   ('William', 'Central st 954'),
#   ('Chuck', 'Main Road 989'),
#   ('Viola', 'Sideway 1633')
# ]

# mycursor.executemany(sql, val)

# mydb.commit()


# mycursor.execute("SELECT * FROM customers")

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)

# mycursor.execute("SELECT name, address FROM customers")

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x) 

# sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"

# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)


# sql = "SELECT * FROM customers ORDER BY name"

# mycursor.execute(sql)

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)


# sql = "DELETE FROM customers WHERE address = 'Mountain 21'"

# mycursor.execute(sql)

# mydb.commit()

# # sql = "DROP TABLE IF EXISTS customers"

# # mycursor.execute(sql) 

# sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"

# mycursor.execute(sql)

# mydb.commit()

