fichero_entrada = input("Fichero de entrada: ")
fichero_salida = input("Fichero de salida: ")
desplazamiento = int(input("Desplazamiento (< 26): "))

with open(fichero_entrada, "r", encoding="utf-8") as f:
    texto = f.read()

resultado = []
for char in texto:
    if 'A' <= char <= 'Z':
        nuevo = chr((ord(char) - ord('A') + desplazamiento) % 26 + ord('A'))
        resultado.append(nuevo)
    elif 'a' <= char <= 'z':
        nuevo = chr((ord(char) - ord('a') + desplazamiento) % 26 + ord('a'))
        resultado.append(nuevo)
    else:
        resultado.append(char)

with open(fichero_salida, "w", encoding="utf-8") as f:
    f.write("".join(resultado))