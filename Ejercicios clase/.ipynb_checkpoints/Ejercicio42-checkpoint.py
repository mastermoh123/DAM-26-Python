fichero1 = input("Nombre del primer fichero (destino): ")
fichero2 = input("Nombre del segundo fichero (origen): ")

with open(fichero2, "r", encoding="utf-8") as f2:
    contenido = f2.read()

with open(fichero1, "a", encoding="utf-8") as f1:
    f1.write("\n" + contenido)

print("Contenido agregado correctamente.")