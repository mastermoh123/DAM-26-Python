fichero_entrada = input("Fichero de entrada: ")
fichero_salida = input("Fichero de salida: ")

puntuacion = ".,:;!¡?¿"
frecuencias = {}

with open(fichero_entrada, "r", encoding="utf-8") as f:
    texto = f.read().upper()

for signo in puntuacion:
    texto = texto.replace(signo, "")

for palabra in texto.split():
    frecuencias[palabra] = frecuencias.get(palabra, 0) + 1

with open(fichero_salida, "w", encoding="utf-8") as f:
    for palabra, conteo in frecuencias.items():
        f.write(f"{palabra}, {conteo}\n")