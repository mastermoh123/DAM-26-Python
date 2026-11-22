from Animal import Animal

class Herbivoro(Animal):
    def __init__(self, id_animal: int, especie: str, kg_dia: int):
        super().__init__(id_animal, especie)
        self.__kg_dia = kg_dia

    @property
    def kg_dia(self):
        return self.__kg_dia

    def __str__(self):
        return f"{super().__str__()}, Tipo: Herbívoro, Kilos de pasto/día: {self.__kg_dia}kg"
        