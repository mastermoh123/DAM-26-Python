pVocal = []
pConso = []

vocales = ["a", "e", "i", "o", "u"]

print("Por favor, introduce 6 palabras en total:")

for i in range(6):
    palabra = input(f"Palabra {i + 1}: ")

    if(palabra[0].lower() in vocales):
        pVocal.append(palabra)
    else:
        pConso.append(palabra)

tuplaConso = tuple(pConso)

print("\n--- RESULTADOS ---")
print(f"Contenido de vocales: {pVocal}")
print(f"Contenido de consonantes: {tuplaConso}")