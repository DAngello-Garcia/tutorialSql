from logica.vehiculo import Vehiculo
from logica.conductor import Conductor


def ingresarVehiculo():
    v = {'Codigo':'', 'Placa':'', 'Tipo':'', 'Marca':'', 'Modelo':'', 'Fecha_inicio':'', 'Estado':''}
    v['Codigo'] = input("Ingrese el código del vehículo: ")
    v['Placa'] = input("Ingrese la placa del vehículo: ")
    v['Tipo'] = input("Ingrese el tipo del vehículo (bus/camión): ")
    v['Marca'] = input("Ingrese la marca del vehículo: ")
    v['Modelo'] = input("Ingrese el modelo del vehículo: ")
    v['Fecha_inicio'] = input("Ingrese la fecha de inicio de operación del vehículo (YYYY-MM-DD): ")
    est = input("Ingrese el estado del vehículo (uso/no uso): ")
    if est=="uso":
        v['Estado'] = True
    else:
        v['Estado'] = False
    ObjVehiculo = Vehiculo(v['Codigo'], v['Placa'], v['Tipo'], v['Marca'], v['Modelo'], v['Fecha_inicio'], v['Estado'])
    ObjVehiculo.createEntities(**v)
    return ObjVehiculo

def ingresarConductor(v):
    c = {'Identificacion':'', 'Nombres':'', 'Apellidos':'', 'Celular':'', 'Fecha_Nacimiento':'', 'Turno':'', 'Codigo_Vehiculo':''}
    c['Identificacion'] = int(input("Ingrese la identificación del conductor: "))
    c['Nombres'] = input("Ingrese los nombres del conductor: ")
    c['Apellidos'] = input("Ingrese los apellidos del conductor: ")
    c['Celular'] = input("Ingrese el celular del conductor: ")
    c['Fecha_Nacimiento'] = input("Ingrese la fecha de nacimiento del conductor (YYYY-MM-DD): ")
    c['Turno'] = input("Ingrese el turno del conductor (día/noche): ")
    c['Codigo_Vehiculo'] = input("Ingrese el código del vehículo asignado: ")
    if v.verificarExistencia(c['Codigo_Vehiculo']):
        ObjConductor = Conductor(c['Identificacion'], c['Nombres'], c['Apellidos'], c['Celular'], c['Fecha_Nacimiento'], c['Turno'], c['Codigo_Vehiculo'])
        ObjConductor.createEntities(**c)
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

nuevoVehiculo = ingresarVehiculo()
nuevoConductor = ingresarConductor(nuevoVehiculo)
#modificarVehiculo(nuevoVehiculo)