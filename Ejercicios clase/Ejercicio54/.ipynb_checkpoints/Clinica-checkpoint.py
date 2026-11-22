from Mascota import Mascota
from Gato import Gato
from Perro import Perro

class Clinica:
    def __init__(self):
        self.__mascotas = []

    @property
    def mascotas(self):
        return self.__mascotas

    def altaMascota(self, o_mascota: Mascota) -> str:
        for mascota in self.__mascotas:
            if mascota.id_mascota == o_mascota.id_mascota:
                return "Mascota repetida"
        self.__mascotas.append(o_mascota)
        return "Alta OK"

    def bajaMascota(self, id_mascota: int) -> str:
        for mascota in self.__mascotas:
            if mascota.id_mascota == id_mascota:
                self.__mascotas.remove(mascota)
                return "Mascota dada de baja"
        return "Mascota no localizada"

    def pesoMaximoGato(self) -> int:
        gatos_peso = [m.peso for m in self.__mascotas if isinstance(m, Gato)]
        if not gatos_peso:
            return 0
        return max(gatos_peso)

    def listadoPerros(self) -> str:
        perros = [m for m in self.__mascotas if isinstance(m, Perro)]
        if not perros:
            return "No hay perros registrados en la clínica."
        
        resultado = "Listado de perros:\n"
        for perro in perros:
            resultado += f"- {str(perro)}\n"
        return resultado.strip()

    def __str__(self):
        return f"Clínica con {len(self.__mascotas)} mascotas registradas."