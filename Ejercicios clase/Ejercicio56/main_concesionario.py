from Concesionario.concesionario import Concesionario
from Concesionario.turismo import Turismo
from Concesionario.camion import Camion

conc = Concesionario()
print(conc.altaVehiculo(Turismo("1234ABC", 15000.0, 5)))
print(conc.altaVehiculo(Camion("5678DEF", 45000.0, "3500kg")))
print(conc.ventaVehiculo("5678DEF"))
print(conc.ventaVehiculo("5678DEF"))
print(f"Importe ventas: {conc.importeVentas()}€")
print("Turismos:\n" + conc.listadoTurismo())
print("Camiones vendidos:\n" + conc.listadoCamionVendido())