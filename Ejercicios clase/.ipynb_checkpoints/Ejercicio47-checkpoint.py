f_texto = input("Fichero de texto original: ")
f_sust = input("Fichero de sustituciones: ")
f_salida = input("Fichero de salida: ")

sustituciones = {}
with open(f_sust, "r", encoding="utf-8") as f:
    for linea in f:
        if ";" in linea:
            origen, destino = linea.strip().split(";")
            sustituciones[origen] = destino

with open(f_texto, "r", encoding="utf-8") as f:
    contenido = f.read()

# Se aplica carácter a carácter para evitar sustituciones encadenadas (ej. a->o y luego o->x)
nuevo_texto = "".join(sustituciones.get(c, c) for c in contenido)

with open(f_salida, "w", encoding="utf-8") as f:
    f.write(nuevo_texto)