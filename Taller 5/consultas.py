from logica.vehiculo import Vehiculo
from logica.conductor import Conductor
from logica.conexion import checkDB


def ingresarVehiculo():
    v = []
    v.append(input("Ingrese el código del vehículo: "))
    v.append(input("Ingrese la placa del vehículo: "))
    v.append(input("Ingrese el tipo del vehículo (bus/camión): "))
    v.append(input("Ingrese la marca del vehículo: "))
    v.append(input("Ingrese el modelo del vehículo: "))
    v.append(input("Ingrese la fecha de inicio de operación del vehículo (YYYY-MM-DD): "))
    est = input("Ingrese el estado del vehículo (uso/no uso): ")
    if est=="uso":
        v.append(True)
    else:
        v.append(False)
    ObjVehiculo = Vehiculo(*v)
    ObjVehiculo.createTable()
    ObjVehiculo.createEntities(*v)
    return ObjVehiculo

def ingresarConductor():
    c = []
    c.append(int(input("Ingrese la identificación del conductor: ")))
    c.append(input("Ingrese los nombres del conductor: "))
    c.append(input("Ingrese los apellidos del conductor: "))
    c.append(input("Ingrese el celular del conductor: "))
    c.append(input("Ingrese la fecha de nacimiento del conductor (YYYY-MM-DD): "))
    c.append(input("Ingrese el turno del conductor (día/noche): "))
    c.append(input("Ingrese el código del vehículo asignado: "))
    if Vehiculo.verificarExistencia(c[0]):
        ObjConductor = Conductor(*c)
        ObjConductor.createTable()
        ObjConductor.createEntities(*c)
        return ObjConductor
    else:
        print("Error al ingresar un conductor.")

def modificarVehiculo(ObjVehiculo):
    codConsulta = input("Ingrese el código del vehículo que desea modificar: ")
    if ObjVehiculo.verificarExistencia(codConsulta):
        print("Esta es la información del vehículo: ")
        ObjVehiculo.readEntities(codConsulta)
        v = {'Placa':'', 'Modelo':''}
        v['Placa'] = input("Ingrese la nueva placa del vehículo: ")
        v['Modelo'] = input("Ingrese el nuevo modelo del vehículo: ")
        ObjVehiculo.updateTable(**v)
        print("La nueva información del vehículo: ")
        ObjVehiculo.readEntities(codConsulta)

checkDB()
nuevoVehiculo = ingresarVehiculo()
nuevoConductor = ingresarConductor()
id = nuevoConductor.getIdentificacion()
nuevoConductor.readEntities(id)