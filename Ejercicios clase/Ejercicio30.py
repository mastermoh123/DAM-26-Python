equipos_datos = []

print("Introducción de datos del torneo:")
for i in range(3):
    nombre = input(f"\nNombre del equipo {i+1}: ")
    ganados = int(input("Partidos ganados: "))
    perdidos = int(input("Partidos perdidos: "))
    empatados = int(input("Partidos empatados: "))
    
    equipos_datos.append((nombre, ganados, perdidos, empatados))

print("\nLista de equipos introducidos:")
print(equipos_datos)

equipos_puntos = []
for equipo in equipos_datos:
    nombre, ganados, perdidos, empatados = equipo
    puntos = (ganados * 3) + (empatados * 1)
    equipos_puntos.append((nombre, puntos))

equipos_puntos.sort(key=lambda x: x[1], reverse=True)

print("\nClasificación final (orden descendente por puntos):")
print(equipos_puntos)
