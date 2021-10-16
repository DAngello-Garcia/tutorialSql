c = {'Identificacion':'', 'Nombres':'', 'Apellidos':'', 'Celular':'', 'Fecha_Nacimiento':'', 'Turno':'', 'Codigo_Vehiculo':''}

def verificarExistencia(id):
        try:
            query = "SELECT * FROM Vehiculo WHERE Codigo = {};".format(id)
            return True
        except:
            print("El vehículo no existe. Error: ")
            return False
c['Codigo_Vehiculo'] = int(input("Ingrese el código del vehículo asignado: "))
if verificarExistencia(c['Codigo_Vehiculo']):
    print("hola")
query = '''SELECT * FROM Vehiculo WHERE Codigo = {};'''.format(c['Codigo_Vehiculo'])
print(query)