from turismo import Turismo
from camion import Camion

class Concesionario:
    def __init__(self):
        self.__vehiculos = []

    def altaVehiculo(self, oVehiculo) -> str:
        if any(v.matricula == oVehiculo.matricula for v in self.__vehiculos):
            return "Vehículo repetido"
        self.__vehiculos.append(oVehiculo)
        return "Alta OK"

    def ventaVehiculo(self, sMatricula: str) -> str:
        for v in self.__vehiculos:
            if v.matricula == sMatricula:
                if v.vendido:
                    return "Vehículo vendido anteriormente"
                v.vendido = True
                return "Vehículo vendido"
        return "Matricula no localizada"

    def importeVentas(self) -> float:
        return sum(v.precio_venta for v in self.__vehiculos if v.vendido)

    def listadoTurismo(self) -> str:
        return "\n".join(str(v) for v in self.__vehiculos if isinstance(v, Turismo))

    def listadoCamionVendido(self) -> str:
        return "\n".join(str(v) for v in self.__vehiculos if isinstance(v, Camion) and v.vendido)