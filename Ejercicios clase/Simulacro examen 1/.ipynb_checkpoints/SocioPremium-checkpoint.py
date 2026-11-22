from Socio import Socio

class SocioPremium(Socio):
    def __init__(self, nombre: str, cuota_mensual: float, servicios_extra: list[float]):
        super().__init__(nombre, cuota_mensual)
        self.__servicios_extra = list(servicios_extra)

    @property
    def servicios_extra(self) -> list[float]:
        # Devuelve una copia para proteger la lista interna de modificaciones externas directas
        return list(self.__servicios_extra)

    def calcular_cuota(self, descuento: float) -> float:
        # El descuento solo afecta a la cuota base; los servicios extra se suman íntegros
        cuota_base_con_descuento = super().calcular_cuota(descuento)
        return cuota_base_con_descuento + sum(self.__servicios_extra)

    def contratar_servicio(self, precio: float) -> None:
        self.__servicios_extra.append(precio)

    def __str__(self) -> str:
        ct = self.calcular_cuota(0)  # Cuota total sin descuento
        return f"Nombre: {self.nombre} - Cuota mensual: {self.cuota_mensual} - Servicios extra: {self.__servicios_extra} - Cuota total: {ct}"