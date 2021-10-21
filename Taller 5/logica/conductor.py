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

    def createEntities(self, *args):
        try:
            cnx = conexion.getConnection()
            cursor = cnx.cursor(buffered=True)
            query = "INSERT INTO Conductor (Identificacion, Nombres, Apellidos, Celular, Fecha_Nacimiento, Turno, Codigo_Vehiculo) VALUES {};".format(
                args)
            cursor.execute(query)
            cnx.commit()
            cursor.close()
            cnx.close()
        except mysql.connector.Error as err:
            print("Error: ", err)

    def readEntities(self, id):
        try:
            cnx = conexion.getConnection()
            cursor = cnx.cursor(buffered=True)
            query = "SELECT * FROM Conductor WHERE Identificacion = {};".format(
                id)
            cursor.execute(query)
            result = cursor.fetchall()
            for i in result:
                print("Identificación: ", i[0])
                print("Nombres: ", i[1])
                print("Apellidos: ", i[2])
                print("Celular: ", i[3])
                print("Fecha de nacimiento: ", i[4])
                print("Turno: ", i[5])
                print("Código vehículo asignado: ", i[6])
            cursor.close()
        except mysql.connector.Error as err:
            print("Error: ", err)

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
            print("Error: ", err)

    def deleteEntities(self, id):
        try:
            cnx = conexion.getConnection()
            cursor = cnx.cursor(buffered=True)
            query = '''DELETE FROM Conductor WHERE (Identificacion = {});'''.format(
                id)
            cursor.execute(query)
            cnx.commit()
            cursor.close()
            cnx.close()
        except mysql.connector.Error as err:
            print("Error: ", err)
