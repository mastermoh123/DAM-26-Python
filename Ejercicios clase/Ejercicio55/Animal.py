class Animal:
    def __init__(self, id_animal: int, especie: str):
        self.__id_animal = id_animal
        self.__especie = especie

    @property
    def id_animal(self):
        return self.__id_animal

    @property
    def especie(self):
        return self.__especie

    def __str__(self):
        return f"Animal ID: {self.__id_animal}, Especie: {self.__especie}"