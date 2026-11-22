from Animal import Animal

class Carnivoro(Animal):
    def __init__(self, id_animal: int, especie: str, peligroso: bool):
        super().__init__(id_animal, especie)
        self.__peligroso = peligroso

    @property
    def peligroso(self):
        return self.__peligroso

    def __str__(self):
        estado_peligro = "Sí" if self.__peligroso else "No"
        return f"{super().__str__()}, Tipo: Carnívoro, Peligroso: {estado_peligro}"