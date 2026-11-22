from Mascota import Mascota

class Gato(Mascota):
    def __init__(self, id_mascota: int, peso: int, raza: str):
        super().__init__(id_mascota, peso)
        self.__raza = raza

    @property
    def raza(self):
        return self.__raza

    def __str__(self):
        return f"{super().__str__()}, Tipo: Gato, Raza: {self.__raza}"