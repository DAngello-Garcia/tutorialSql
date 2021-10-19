import mysql.connector
from mysql.connector import errorcode
import os

dbUser = os.environ.get('DB_USER')
dbPass = os.environ.get('DB_PASS')
dbHost = 'localhost'
dbName = 'prueba'

def createDB():
    try:
        cnx = mysql.connector.connect(host=dbHost, user=dbUser, password=dbPass)
        cursor = cnx.cursor()
        cursor.execute("CREATE DATABASE {}".format(dbName))
        cursor.close()
        cnx.close()
    except mysql.connector.Error as err:
        print("Failed creating database: {}".format(err))
        exit(1)
    
def checkDB():
    try:
        cnx = mysql.connector.connect(host=dbHost, user=dbUser, password=dbPass, database=dbName)
        cursor = cnx.cursor()
        cursor.execute("USE {}".format(dbName))
        cursor.close()
        cnx.close()
    except mysql.connector.Error as err:
        print("Database {} does not exists".format(dbName))
        if err.errno == errorcode.ER_BAD_DB_ERROR:
            createDB()
            print("Database {} created successfully.".format(dbName))
        else:
            print(err)
            exit(1)

def getConnection():
    return mysql.connector.connect(host=dbHost, user=dbUser, password=dbPass, database=dbName)