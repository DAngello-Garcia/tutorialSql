import conexion

class Conductor:
    conexion.checkDB()
    cnx = conexion.getConnection()
    cursor = conexion.getCursor()

    def __init(self, id, nombres, apellidos, celu, fecha, correo, licencia, categoria, turno, ciudad, direccion, barrio, cod_vehi):
        self.Identificacion = id
        self.Nombres = nombres
        self.Apellidos = apellidos
        self.Celular = celu
        self.Fecha_Nacimiento = fecha
        self.Correo = correo
        self.Numero_Licencia = licencia
        self.Categoria_Licencia = categoria
        self.Turno = turno
        self.Ciudad = ciudad
        self.Direccion = direccion
        self.Barrio = barrio
        self.Codigo_Vehiculo = cod_vehi

    def createTable():
        query = '''CREATE TABLE Conductor (
            Id_Conductor INT AUTO_INCREMENT,
            Identificacion BIGINT NOT NULL,
            Nombres VARCHAR(150),
            Apellidos VARCHAR(150),
            Celular CHAR(15),
            Fecha_Nacimiento DATE,
            Correo VARCHAR(150),
            Numero_Licencia CHAR(50),
            Categoria_Licencia CHAR(5),
            Turno CHAR(15),
            Ciudad VARCHAR(150),
            Direccion VARCHAR(150),
            Barrio VARCHAR(150),
            Codigo_Vehiculo INT,
            PRIMARY KEY (Id_Conductor),
            FOREIGN KEY (Codigo_Vehiculo) REFERENCES Vehiculo(Id_Vehiculo)
        );'''
        cursor.execute(query)
        cnx.commit()
        cursor.close()
        cnx.close()

    def createEntities(**kwargs):
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
        except mysql.connector.Error as err:
            print(err)

    def readEntities(id):
        try:
            query = "SELECT * FROM Conductor WHERE Identificacion = {};".format(id)
            cursor.execute(query)
            result = cursor.fetchall()
            for i in result:
                print(i)
            cursor.close()
        except mysql.connector.Error as err:
            print(err)

    def updateTable(self, **kwargs):
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
            query += " WHERE Identificacion = {};".format(self.Codigo)
            cursor.execute(query)
            cnx.commit()
            cursor.close()
            cnx.close()
        except mysql.connector.Error as err:
            print(err)

    def deleteEntities(id):
        try:
            query = '''DELETE FROM Conductor WHERE (Identificacion = {});'''.format(id)
            cursor.execute(query)
            cnx.commit()
            cursor.close()
            cnx.close()
        except mysql.connector.Error as err:
            print(err)
