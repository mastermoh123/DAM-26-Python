import os
import runpy

dir_actual = os.path.dirname(os.path.abspath(__file__))

archivos_ejercicio = sorted([f for f in os.listdir(dir_actual) if 'ejercicio' in f.lower()])

COLUMNAS = 3

print("=================================== EJERCICIOS DISPONIBLES ===================================")
for i in range(0, len(archivos_ejercicio), COLUMNAS):
    fila = archivos_ejercicio[i:i + COLUMNAS]
    print(*(f"{arch:30}" for arch in fila))
print("==============================================================================================\n")

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
        print(f"\n--- Ejecutando Ejercicio{num}.py ---\n")
        runpy.run_path(archivo_a_ejecutar, run_name="__main__")
        print("\n-----------------------------------\n")
    except FileNotFoundError:
        print(f"El archivo Ejercicio{num}.py no existe en la carpeta.")
