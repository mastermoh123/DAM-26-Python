from Concesionario.vehiculo import Vehiculo

class Camion(Vehiculo):
    def __init__(self, matricula: str, precio_venta: float, masa_maxima: str):
        super().__init__(matricula, precio_venta)
        self.__masa_maxima = masa_maxima

    @property
    def masa_maxima(self): return self.__masa_maxima
    @masa_maxima.setter
    def masa_maxima(self, valor): self.__masa_maxima = valor

    def __str__(self):
        return f"[Camión] {super().__str__()} | MMA: {self.__masa_maxima}"