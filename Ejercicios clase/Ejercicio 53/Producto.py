from Pieza import Pieza

class Producto:
    def __init__(self, id_producto: str, nombre: str):
        self.__id_producto = id_producto
        self.__nombre = nombre
        self.__piezas = [] 

    @property
    def id_producto(self):
        return self.__id_producto

    @property
    def nombre(self):
        return self.__nombre

    @property
    def piezas(self):
        return self.__piezas

    # Métodos requeridos
    def agregarPieza(self, o_pieza: Pieza) -> str:
        for pieza in self.__piezas:
            if pieza.id_pieza == o_pieza.id_pieza:
                return "Pieza repetida"
        
        self.__piezas.append(o_pieza)
        return "Alta OK"

    def precioProducto(self) -> float:
        return sum(pieza.precio for pieza in self.__piezas)

    def pesoProducto(self) -> int:
        return sum(pieza.peso for pieza in self.__piezas)

    def listadoPiezas(self) -> str:
        if not self.__piezas:
            return "El producto no contiene piezas."
        
        resultado = "Listado de piezas del producto:\n"
        for pieza in self.__piezas:
            resultado += f"- {str(pieza)}\n"
        return resultado.strip()

    def __str__(self):
        return f"Producto [{self.__id_producto}] {self.__nombre} - Precio: {self.precioProducto()}€ - Peso: {self.pesoProducto()}g"