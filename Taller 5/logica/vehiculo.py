import conexion

conexion.checkDB()
cnx = conexion.getConnection()
cursor = conexion.getCursor()

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