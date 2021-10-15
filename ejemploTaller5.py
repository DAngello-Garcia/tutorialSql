import os
import mysql.connector

dbHost = "localhost"
dbUser = os.environ.get('DB_USER')
dbPass = os.environ.get('DB_PASS')
dbName = "Directorio"
# mydb = mysql.connector.connect(host=dbHost, user=dbUser, password=dbPass)
# mycursor = mydb.cursor()
# sql = "CREATE DATABASE Directorio"
# mycursor.execute(sql)
# mydb.commit()

# mydb = mysql.connector.connect(host=dbHost, user=dbUser, password=dbPass, database=dbName)
# mycursor = mydb.cursor()

# sql = '''CREATE TABLE clientes (
#     Id_Cliente INT AUTO_INCREMENT,
#     Identificacion BIGINT NOT NULL,
#     Nombre VARCHAR(150),
#     Apellido VARCHAR(150),
#     Celular CHAR(15),
#     PRIMARY KEY (Id_Cliente)
# );'''
# mycursor.execute(sql)
# mydb.commit()

# mydb = mysql.connector.connect(host=dbHost, user=dbUser, password=dbPass, database=dbName)
# mycursor = mydb.cursor()

# sql = '''ALTER TABLE clientes
#     ADD COLUMN Ciudad CHAR(35),
#     ADD COLUMN Telefono CHAR(15);'''
# mycursor.execute(sql)
# mydb.commit()

# mydb = mysql.connector.connect(host=dbHost, user=dbUser, password=dbPass, database=dbName)
# mycursor = mydb.cursor()

# sql = '''ALTER TABLE clientes
# #     MODIFY Telefono DEFAULT '00000';
#     '''
# mycursor.execute(sql)
# mydb.commit()

mydb = mysql.connector.connect(host=dbHost, user=dbUser, password=dbPass, database=dbName)
mycursor = mydb.cursor()

# sql = '''INSERT INTO clientes (
#     Identificacion, Nombre, Apellido, Celular, Ciudad, Telefono)
#     VALUES (%(Identificacion)s, %(Nombre)s, %(Apellido)s, %(Celular)s, %(Ciudad)s, %(Telefono)s);'''
# sql1 = '''INSERT INTO clientes (
#     Identificacion, Nombre, Apellido, Celular, Ciudad, Telefono)
#     VALUES (%s, %s, %s, %s, %s, %s);'''
# values = {
#     'Identificacion': 12345,
#     'Nombre': 'Pepe',
#     'Apellido': 'Pérez',
#     'Celular': 3001234567,
#     'Ciudad': 'Bogotá',
#     'Telefono': 7234567,
# }
# initialValues = (9765, 'Sed', 'last name', 3012345678, 'Armenia', 87624)

# mycursor.execute("SELECT * FROM clientes;")
# #mydb.commit()

# for x in mycursor:
#       print(x)

mycursor.close()
mydb.close()
