from Clinica import Clinica
from Gato import Gato
from Perro import Perro

print("=== DEMOSTRACIÓN DE LA CLÍNICA VETERINARIA ==-\n")
    
clinica = Clinica()

gato1 = Gato(101, 4000, "Siamés")
gato2 = Gato(102, 5500, "Persa")
perro1 = Perro(201, 15000, 50)
perro2 = Perro(202, 8000, 30)

print("--- Altas de Mascotas ---")
print("Alta gato1:", clinica.altaMascota(gato1))
print("Alta gato2:", clinica.altaMascota(gato2))
print("Alta perro1:", clinica.altaMascota(perro1))
print("Alta perro2:", clinica.altaMascota(perro2))
print("Alta gato1 repetido:", clinica.altaMascota(gato1))  # Debe retornar "Mascota repetida"

print("\n--- Consultas ---")
print(f"Peso máximo de gato: {clinica.pesoMaximoGato()} g")

print("\n--- Listado de Perros ---")
print(clinica.listadoPerros())

print("\n--- Bajas de Mascotas ---")
print("Baja perro1 (ID 201):", clinica.bajaMascota(201))
print("Baja mascota inexistente (ID 999):", clinica.bajaMascota(999))  # Debe retornar "Mascota no localizada"

print("\n--- Listado de Perros tras la baja ---")
print(clinica.listadoPerros())