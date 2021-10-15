import conexion

conexion.checkDB()
cnx = conexion.getConnection()
cursor = conexion.getCursor() 

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

