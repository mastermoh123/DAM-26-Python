class Vehiculo:
    def __init__(self, matricula: str, precio_venta: float):
        self.__matricula = matricula
        self.__vendido = False  # Por enunciado, al crearse NO puede estar vendido
        self.__precio_venta = precio_venta

    @property
    def matricula(self): return self.__matricula
    @matricula.setter
    def matricula(self, valor): self.__matricula = valor

    @property
    def vendido(self): return self.__vendido
    @vendido.setter
    def vendido(self, valor): self.__vendido = valor

    @property
    def precio_venta(self): return self.__precio_venta
    @precio_venta.setter
    def precio_venta(self, valor): self.__precio_venta = valor

    def __str__(self):
        estado = "Vendido" if self.__vendido else "Disponible"
        return f"Matrícula: {self.__matricula} | Precio: {self.__precio_venta}€ | Estado: {estado}"