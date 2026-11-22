fichero = input("Nombre del fichero de números: ")
numeros = []

with open(fichero, "r", encoding="utf-8") as f:
    for linea in f:
        linea = linea.strip()
        if linea:
            numeros.extend([float(x) for x in linea.split(";")])

print(f"Valor máximo: {max(numeros)}")
print(f"Valor mínimo: {min(numeros)}")
print(f"Suma de todos los valores: {sum(numeros)}")
print(f"Media de todos los valores: {sum(numeros) / len(numeros)}")