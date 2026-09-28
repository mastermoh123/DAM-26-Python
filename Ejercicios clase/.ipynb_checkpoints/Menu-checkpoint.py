import os
import runpy

dir_actual = os.path.dirname(os.path.abspath(__file__))

archivos = os.listdir(dir_actual)
for f in archivos:
    if 'ejercicio' in f.lower():
        print(f)

num = -1

while num != 0:
    try:
        num = int(input("Introduce el número de ejercicio (0 para salir): "))
    except ValueError:
        print("El ejercicio no existe o no es un número válido.")
        continue

    if num == 0:
        print("Adios")
        break

    archivo_a_ejecutar = os.path.join(dir_actual, f"Ejercicio{num}.py")

    try:
        runpy.run_path(archivo_a_ejecutar, run_name="__main__")
    except FileNotFoundError:
        print(f"El archivo Ejercicio{num}.py no existe en la carpeta.")