import logica.conexion as conexion
import mysql.connector
from mysql.connector import errorcode

class Conductor:

    def __init__(self, id, nombres, apellidos, celu, fecha, turno, cod_vehi):
        self.Identificacion = id
        self.Nombres = nombres
        self.Apellidos = apellidos
        self.Celular = celu
        self.Fecha_Nacimiento = fecha
        self.Turno = turno
        self.Codigo_Vehiculo = cod_vehi
    
    def getIdentificacion(self):
        return self.Identificacion

    def createTable(self):
        cnx = conexion.getConnection()
        cursor = cnx.cursor(buffered=True)
        cursor.execute("CALL sys.table_exists('prueba', 'Conductor', @exists);")
        verificar = cursor.execute("SELECT @exists;")
        if verificar == '':
            query = '''CREATE TABLE Conductor (
                Identificacion BIGINT NOT NULL,
                Nombres VARCHAR(150),
                Apellidos VARCHAR(150),
                Celular VARCHAR(15),
                Fecha_Nacimiento DATE,
                Turno VARCHAR(15),
                Codigo_Vehiculo VARCHAR(50),
                PRIMARY KEY (Identificacion),
                FOREIGN KEY (Codigo_Vehiculo) REFERENCES Vehiculo(Codigo)
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
            query = "INSERT INTO Conductor (Identificacion, Nombres, Apellidos, Celular, Fecha_Nacimiento, Turno, Codigo_Vehiculo) VALUES {};".format(args)
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
            query = "SELECT * FROM Conductor WHERE Identificacion = {};".format(id)
            cursor.execute(query)
            result = cursor.fetchall()
            for i in result:
                print(i)
            cursor.close()
        except mysql.connector.Error as err:
            print("Error: ",err)

    def updateTable(self, id, **kwargs):
        try:
            cnx = conexion.getConnection()
            cursor = cnx.cursor(buffered=True)
            query = "UPDATE Conductor"
            i = 0
            for key, value in kwargs.items():
                if i == 0:
                    query += " SET "
                else:
                    query += ", "
                query += "{}='{}'".format(key, value)
                i += 1
            query += " WHERE Identificacion = {};".format(id)
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
            query = '''DELETE FROM Conductor WHERE (Identificacion = {});'''.format(id)
            cursor.execute(query)
            cnx.commit()
            cursor.close()
            cnx.close()
        except mysql.connector.Error as err:
            print("Error: ",err)
