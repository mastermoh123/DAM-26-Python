class Pieza:
    def __init__(self, id_pieza: str, peso: int, precio: float, url_fabricante: str):
        self.__id_pieza = id_pieza
        self.__peso = peso
        self.__precio = precio
        self.__url_fabricante = url_fabricante

    @property
    def id_pieza(self):
        return self.__id_pieza

    @property
    def peso(self):
        return self.__peso

    @property
    def precio(self):
        return self.__precio

    @property
    def url_fabricante(self):
        return self.__url_fabricante

    def __str__(self):
        return f"Pieza {self.__id_pieza}: peso={self.__peso}g, precio={self.__precio}€, fabricante={self.__url_fabricante}"