from Concesionario.vehiculo import Vehiculo

class Turismo(Vehiculo):
    def __init__(self, matricula: str, precio_venta: float, num_plazas: int):
        super().__init__(matricula, precio_venta)
        self.__num_plazas = num_plazas

    @property
    def num_plazas(self): return self.__num_plazas
    @num_plazas.setter
    def num_plazas(self, valor): self.__num_plazas = valor

    def __str__(self):
        return f"[Turismo] {super().__str__()} | Plazas: {self.__num_plazas}"