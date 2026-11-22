from Pieza import Pieza

class PiezaPlastico(Pieza):
    def __init__(self, id_pieza: str, peso: int, precio: float, url_fabricante: str, resistencia: int):
        super().__init__(id_pieza, peso, precio, url_fabricante)
        self.__resistencia = resistencia

    @property
    def resistencia(self):
        return self.__resistencia

    def __str__(self):
        return f"{super().__str__()}, Tipo: Plástico (Resistencia: {self.__resistencia})"