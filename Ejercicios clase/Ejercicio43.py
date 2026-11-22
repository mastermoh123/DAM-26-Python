fichero_entrada = input("Fichero de entrada a ordenar: ")
columna = int(input("Número de columna (empezando en 1): ")) - 1
fichero_salida = input("Fichero de salida ordenada: ")

with open(fichero_entrada, "r", encoding="utf-8") as f:
    lineas = f.readlines()

# Ordena tomando la subcadena desde la columna indicada hasta el final
lineas_ordenadas = sorted(lineas, key=lambda linea: linea[columna:])

with open(fichero_salida, "w", encoding="utf-8") as f:
    f.writelines(lineas_ordenadas)

print("Fichero ordenado generado.")