class Mascota:
    def __init__(self, id_mascota: int, peso: int):
        self.__id_mascota = id_mascota
        self.__peso = peso

    @property
    def id_mascota(self):
        return self.__id_mascota

    @property
    def peso(self):
        return self.__peso

    def __str__(self):
        return f"Mascota ID: {self.__id_mascota}, Peso: {self.__peso}g"