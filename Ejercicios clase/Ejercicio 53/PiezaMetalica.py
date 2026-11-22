from Pieza import Pieza

class PiezaMetalica(Pieza):
    def __init__(self, id_pieza: str, peso: int, precio: float, url_fabricante: str, metal: str):
        super().__init__(id_pieza, peso, precio, url_fabricante)
        self.__metal = metal

    @property
    def metal(self):
        return self.__metal

    def __str__(self):
        return f"{super().__str__()}, Tipo: Metálica (Metal: {self.__metal})"