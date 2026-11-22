from Zoologico import Zoologico
from Herbivoro import Herbivoro
from Carnivoro import Carnivoro

print("=== DEMOSTRACIÓN DEL ZOOLÓGICO ==-\n")
    
zoo = Zoologico()

h1 = Herbivoro(1, "Elefante", 150)
h2 = Herbivoro(2, "Cebra", 35)
c1 = Carnivoro(3, "León", True)
c2 = Carnivoro(4, "Lince Ibérico", False)

print("--- Altas de Animales ---")
print("Alta h1:", zoo.altaAnimal(h1))
print("Alta h2:", zoo.altaAnimal(h2))
print("Alta c1:", zoo.altaAnimal(c1))
print("Alta c2:", zoo.altaAnimal(c2))
print("Alta h1 repetido:", zoo.altaAnimal(h1))  # Debe retornar "Animal repetido"

print("\n--- Consultas ---")
print(f"Kilos de pasto necesarios al día: {zoo.numKilosPasto()} kg")

print("\n--- Listado de Carnívoros Peligrosos ---")
print(zoo.listadoPeligrosos())

print("\n--- Bajas de Animales ---")
print("Baja c1 (ID 3):", zoo.bajaAnimal(3))
print("Baja animal inexistente (ID 999):", zoo.bajaAnimal(999))  # Debe retornar "Animal no localizado"

print("\n--- Listado de Carnívoros Peligrosos tras la baja ---")
print(zoo.listadoPeligrosos())
