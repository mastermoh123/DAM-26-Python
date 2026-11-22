class Socio:
    def __init__(self, __nombre: str, __cuota_mensual: float):
        self.__nombre = __nombre
        self.__cuota_mensual = __cuota_mensual
        
    @property
    def nombre(self) -> str:
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre: str):
        self.__nombre = nuevo_nombre

    @property
    def cuota_mensual(self) -> float:
        return self.__cuota_mensual

    @cuota_mensual.setter
    def cuota_mensual(self, nueva_cuota: float):
        self.__cuota_mensual = nueva_cuota

    def calcular_cuota(self, descuento: float) -> float:
        # Aplica el descuento porcentual a la cuota mensual
        return self.__cuota_mensual * (1 - descuento / 100)

    def __str__(self) -> str:
        return f"Nombre: {self.__nombre} - Cuota mensual: {self.__cuota_mensual}"
    