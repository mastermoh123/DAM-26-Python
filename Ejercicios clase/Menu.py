import os
import re
import runpy

dir_actual = os.path.dirname(os.path.abspath(__file__))

dic_ejercicios = {}
for f in os.listdir(dir_actual):
    if 'ejercicio' in f.lower():
        numeros = re.findall(r'\d+', f)
        if numeros:
            num = int(numeros[0])
            dic_ejercicios[num] = f

if not dic_ejercicios:
    print("No se encontraron archivos de ejercicio en la carpeta.")
    exit()

numeros_ordenados = sorted(dic_ejercicios.keys())
min_num = numeros_ordenados[0]
max_num = numeros_ordenados[-1]

rangos = []
r_inicio = 1
while r_inicio <= max_num:
    r_fin = r_inicio + 9
    rangos.append((r_inicio, r_fin))
    r_inicio += 10

COLUMNAS = 3

while True:
    print("\n=================================== BLOQUES DE EJERCICIOS ===================================")
    for i, (r_ini, r_fin) in enumerate(rangos, 1):
        ejercicios_en_rango = [n for n in numeros_ordenados if r_ini <= n <= r_fin]
        estado = f"({len(ejercicios_en_rango)} disponibles)" if ejercicios_en_rango else "(vacío)"
        print(f"[{i}] Del {r_ini} al {r_fin} {estado}")
    print("[0] Salir")
    print("==============================================================================================")
    
    try:
        opcion_bloque = int(input("Selecciona el número de bloque (0 para salir): "))
    except ValueError:
        print("Por favor, introduce un número válido.")
        continue
        
    if opcion_bloque == 0:
        print("¡Adiós!")
        break
        
    if 1 <= opcion_bloque <= len(rangos):
        r_ini, r_fin = rangos[opcion_bloque - 1]
        ejercicios_bloque = [n for n in numeros_ordenados if r_ini <= n <= r_fin]
        
        if not ejercicios_bloque:
            print(f"\nNo hay ejercicios en el rango del {r_ini} al {r_fin}.")
            continue

        while True:
            print(f"\n================================== EJERCICIOS ({r_ini} - {r_fin}) ==================================")
            for i in range(0, len(ejercicios_bloque), COLUMNAS):
                fila = ejercicios_bloque[i:i + COLUMNAS]
                print(*(f"Ejercicio {num:2}" for num in fila))
            print("[0] Volver al menú de bloques")
            print("==============================================================================================\n")
            
            try:
                num_ej = int(input("Introduce el número de ejercicio a ejecutar (0 para volver): "))
            except ValueError:
                print("Número no válido.")
                continue
                
            if num_ej == 0:
                break
                
            if num_ej in ejercicios_bloque:
                archivo_a_ejecutar = os.path.join(dir_actual, dic_ejercicios[num_ej])
                try:
                    print(f"\n--- Ejecutando Ejercicio{num_ej} ({dic_ejercicios[num_ej]}) ---\n")
                    runpy.run_path(archivo_a_ejecutar, run_name="__main__")
                    print("\n------------------------------------------------------------------------------\n")
                except Exception as e:
                    print(f"Error al ejecutar el archivo: {e}")
            else:
                print("El ejercicio no existe en este rango o no es válido.")
    else:
        print("Bloque no válido. Inténtalo de nuevo.")