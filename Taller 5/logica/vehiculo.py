import conexion

class Vehiculo:
    conexion.checkDB()
    cnx = conexion.getConnection()
    cursor = conexion.getCursor()

    def __init__(self, Codigo, Placa, Tipo, Marca, Modelo, Descripcion, Fecha_inicio, Estado):
        self.Codigo = Codigo
        self.Placa = Placa
        self.Tipo = Tipo
        self.Marca = Marca
        self.Modelo = Modelo
        self.Descripcion = Descripcion
        self.Fecha_inicio = Fecha_inicio
        self.Estado = Estado

    def createTable():
        query = '''CREATE TABLE Vehiculo (
            Id_Vehiculo INT AUTO_INCREMENT,
            Codigo VARCHAR(50) NOT NULL,
            Placa CHAR(10) NOT NULL,
            Tipo VARCHAR(50),
            Marca VARCHAR(100),
            Modelo VARCHAR(50),
            Descripcion VARCHAR(150),
            Fecha_inicio DATE,
            Estado BOOLEAN,
            PRIMARY KEY (Id_Vehiculo)
        );'''
        cursor.execute(query)
        cnx.commit()
        cursor.close()
        cnx.close()
    
    def createEntities(**kwargs):
        try:
            query = "INSERT INTO Vehiculo ("
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
            query = "SELECT * FROM Vehiculo WHERE Codigo = {};".format(id)
            cursor.execute(query)
            result = cursor.fetchall()
            for i in result:
                print(i)
            cursor.close()
        except mysql.connector.Error as err:
            print(err)

    def updateTable(self, **kwargs):
        try:
            query = "UPDATE Vehiculo"
            i = 0
            for key, value in kwargs.items():
                if i == 0:
                    query += " SET "
                else:
                    query += ", "
                query += "{}='{}'".format(key, value)
                i += 1
            query += " WHERE Codigo = {};".format(self.Codigo)
            cursor.execute(query)
            cnx.commit()
            cursor.close()
            cnx.close()
        except mysql.connector.Error as err:
            print(err)

    def deleteEntities(id):
        try:
            query = '''DELETE FROM Vehiculo WHERE (Codigo = {});'''.format(id)
            cursor.execute(query)
            cnx.commit()
            cursor.close()
            cnx.close()
        except mysql.connector.Error as err:
            print(err)
