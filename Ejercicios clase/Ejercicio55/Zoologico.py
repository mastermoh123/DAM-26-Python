from Animal import Animal
from Herbivoro import Herbivoro
from Carnivoro import Carnivoro

class Zoologico:
    def __init__(self):
        self.__animales = []

    @property
    def animales(self):
        return self.__animales

    def altaAnimal(self, o_animal: Animal) -> str:
        for animal in self.__animales:
            if animal.id_animal == o_animal.id_animal:
                return "Animal repetido"
        self.__animales.append(o_animal)
        return "Alta OK"

    def bajaAnimal(self, id_animal: int) -> str:
        for animal in self.__animales:
            if animal.id_animal == id_animal:
                self.__animales.remove(animal)
                return "Animal dado de baja"
        return "Animal no localizado"

    def numKilosPasto(self) -> int:
        return sum(a.kg_dia for a in self.__animales if isinstance(a, Herbivoro))

    def listadoPeligrosos(self) -> str:
        peligrosos = [a for a in self.__animales if isinstance(a, Carnivoro) and a.peligroso]
        if not peligrosos:
            return "No hay animales carnívoros peligrosos registrados."
        
        resultado = "Listado de animales carnívoros peligrosos:\n"
        for animal in peligrosos:
            resultado += f"- {str(animal)}\n"
        return resultado.strip()

    def __str__(self):
        return f"Zoológico con {len(self.__animales)} animales registrados."