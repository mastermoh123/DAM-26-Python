from Mascota import Mascota

class Perro(Mascota):
    def __init__(self, id_mascota: int, peso: int, altura: int):
        super().__init__(id_mascota, peso)
        self.__altura = altura

    @property
    def altura(self):
        return self.__altura

    def __str__(self):
        return f"{super().__str__()}, Tipo: Perro, Altura: {self.__altura}cm"