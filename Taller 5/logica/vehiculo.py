import logica.conexion as conexion
import mysql.connector
from mysql.connector import errorcode

class Vehiculo:

    def __init__(self, Codigo, Placa, Tipo, Marca, Modelo, Fecha_inicio, Estado):
        self.Codigo = Codigo
        self.Placa = Placa
        self.Tipo = Tipo
        self.Marca = Marca
        self.Modelo = Modelo
        self.Fecha_inicio = Fecha_inicio
        self.Estado = Estado

    def createTable(self):
        cnx = conexion.getConnection()
        cursor = cnx.cursor(buffered=True)
        cursor.execute("CALL sys.table_exists('prueba', 'Vehiculo', @exists);")
        verificar = cursor.execute("SELECT @exists;")
        if verificar == '':
            query = '''CREATE TABLE Vehiculo (
                Codigo VARCHAR(50) NOT NULL,
                Placa VARCHAR(10),
                Tipo VARCHAR(50),
                Marca VARCHAR(100),
                Modelo VARCHAR(50),
                Fecha_inicio DATE,
                Estado BOOLEAN,
                PRIMARY KEY (Codigo)
            );'''
            cursor.execute(query)
            cursor.close()
            cnx.close()
        else:
            cursor.close()
            cnx.close()
    
    def createEntities(self, *args):
        try:
            cnx = conexion.getConnection()
            cursor = cnx.cursor(buffered=True)
            query = "INSERT INTO Vehiculo (Codigo, Placa, Tipo, Marca, Modelo, Fecha_inicio, Estado) VALUES {};".format(args)
            cursor.execute(query)
            cnx.commit()
            cursor.close()
            cnx.close()
        except mysql.connector.Error as err:
            print("Error: ",err)

    def readEntities(self, id):
        try:
            cnx = conexion.getConnection()
            cursor = cnx.cursor(buffered=True)
            query = "SELECT * FROM Vehiculo WHERE Codigo = {};".format(id)
            cursor.execute(query)
            result = cursor.fetchall()
            for i in result:
                print(i)
            cursor.close()
            cnx.close()
        except mysql.connector.Error as err:
            print("Error: ",err)

    def updateTable(self, id, **kwargs):
        try:
            cnx = conexion.getConnection()
            cursor = cnx.cursor(buffered=True)
            query = "UPDATE Vehiculo"
            i = 0
            for key, value in kwargs.items():
                if i == 0:
                    query += " SET "
                else:
                    query += ", "
                query += "{}='{}'".format(key, value)
                i += 1
            query += " WHERE Codigo = {};".format(id)
            cursor.execute(query)
            cnx.commit()
            cursor.close()
            cnx.close()
        except mysql.connector.Error as err:
            print("Error: ",err)

    def deleteEntities(self, id):
        try:
            cnx = conexion.getConnection()
            cursor = cnx.cursor(buffered=True)
            query = "DELETE FROM Vehiculo WHERE (Codigo = {});".format(id)
            cursor.execute(query)
            cnx.commit()
            cursor.close()
            cnx.close()
        except mysql.connector.Error as err:
            print("Error: ",err)

    @staticmethod
    def verificarExistencia(id):
        try:
            cnx = conexion.getConnection()
            cursor = cnx.cursor(buffered=True)
            conexion.checkDB()
            query = "SELECT * FROM Vehiculo WHERE Codigo = {};".format(id)
            cursor.execute(query)
            cursor.close()
            cnx.close()
            return True
        except mysql.connector.Error as err:
            print("Error: ",err)
            return False