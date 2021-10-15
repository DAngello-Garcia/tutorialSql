import mysql.connector
from mysql.connector import errorcode
import os

dbUser = os.environ.get('DB_USER')
dbPass = os.environ.get('DB_PASS')
dbHost = 'localhost'
dbName = 'Empresa_Teleco'


cnx = mysql.connector.connect(user=dbUser, password=dbPass, host=dbHost)
cursor = cnx.cursor()

def createDB():
    try:
        cursor.execute("CREATE DATABASE {}".format(dbName))
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)
    
def checkDB():
    try:
        cursor.execute("USE {}".format(dbName))
    except mysql.connector.Error as err:
        print("Database {} does not exists".format(dbName))
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            createDB()
            print("Database {} created successfully.".format(dbName))
        else:
            print(err)
            exit(1)

def getCursor():
    return cursor

def getConnection():
    return cnx
