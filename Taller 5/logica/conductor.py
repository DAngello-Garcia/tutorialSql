import logica.conexion as conexion

class Conductor:
    cnx = conexion.getConnection()
    cursor = conexion.getCursor()

    def __init(self, id, nombres, apellidos, celu, fecha, turno, cod_vehi):
        self.Identificacion = id
        self.Nombres = nombres
        self.Apellidos = apellidos
        self.Celular = celu
        self.Fecha_Nacimiento = fecha
        self.Turno = turno
        self.Codigo_Vehiculo = cod_vehi

    def createTable():
        query = '''CREATE TABLE Conductor (
            Id_Conductor INT AUTO_INCREMENT,
            Identificacion BIGINT NOT NULL,
            Nombres VARCHAR(150),
            Apellidos VARCHAR(150),
            Celular CHAR(15),
            Fecha_Nacimiento DATE,
            Turno CHAR(15),
            Codigo_Vehiculo VARCHAR(50),
            PRIMARY KEY (Id_Conductor),
            FOREIGN KEY (Codigo_Vehiculo) REFERENCES Vehiculo(Id_Vehiculo)
        );'''
        cursor.execute(query)
        cnx.commit()
        cursor.close()
        cnx.close()

    def createEntities(self, **kwargs):
        try:
            query = "INSERT INTO Conductor ("
            i = 0
            for key in kwargs.keys():
                if i != len(kwargs) - 1:
                    i += 1
                    query += "{}, ".format(key)
                else:
                    query += "{}) VALUES (".format(key)
                    i = 0
                    for value in kwargs.values():
                        if i != len(kwargs) - 1:
                            i += 1
                            query += "{}, ".format(value)
                        else:
                            query += "{});".format(value)
            cursor.execute(query)
            cnx.commit()
            cursor.close()
            cnx.close()
        except:
            pass
        print("Conductor creado.")

    def readEntities(self, id):
        try:
            query = "SELECT * FROM Conductor WHERE Identificacion = {};".format(id)
            cursor.execute(query)
            result = cursor.fetchall()
            for i in result:
                print(i)
            cursor.close()
        except:
            pass

    def updateTable(self, id, **kwargs):
        try:
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
        except:
            pass

    def deleteEntities(self, id):
        try:
            query = '''DELETE FROM Conductor WHERE (Identificacion = {});'''.format(id)
            cursor.execute(query)
            cnx.commit()
            cursor.close()
            cnx.close()
        except:
            pass
