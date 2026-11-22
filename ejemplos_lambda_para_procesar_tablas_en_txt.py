# ==============================================================================
# GUÍA RÁPIDA DE EXAMEN: PROCESAR ARCHIVOS TIPO TABLA (SEPARADOS POR ';')
# CON FUNCIONES LAMBDA EN PYTHON
# ==============================================================================
# Supongamos un archivo de texto (por ejemplo 'personas.txt') donde cada línea
# representa una fila y los campos van separados por ';' (como una tabla 2D):
#
#   Nombre  ; Apellidos     ; Ciudad   ; Edad
#   Carlos  ; Gómez Pérez   ; Sevilla  ; 31
#   Elena   ; Martínez Ruiz ; Madrid   ; 19
#   Lucía   ; Navarro Gil   ; Valencia ; 9
#
# Índices de columna en este ejemplo:
#   col 0 -> Nombre
#   col 1 -> Apellidos
#   col 2 -> Ciudad
#   col 3 -> Edad
# ==============================================================================


def cargar_filas(ruta_archivo, sep=";"):
    """
    Lee un archivo de texto, elimina espacios/saltos de línea (\n) con strip(),
    ignora líneas vacías y devuelve la lista de filas limpias.
    """
    with open(ruta_archivo, "r", encoding="utf-8") as f:
        return [linea.strip() for linea in f if linea.strip()]


def guardar_filas(ruta_archivo, filas):
    """
    Guarda una lista de filas de texto en un archivo de salida, una por línea.
    """
    with open(ruta_archivo, "w", encoding="utf-8") as f:
        if filas:
            f.write("\n".join(filas) + "\n")
        else:
            f.write("")


# ------------------------------------------------------------------------------
# POSIBILIDAD 1: Ordenar por texto (A-Z o Z-A) ignorando mayúsculas/minúsculas
# ------------------------------------------------------------------------------
def posibilidad_1_ordenar_texto(filas, col=0, sep=";", descendente=False):
    # Usamos .lower() en la lambda para que 'ana' y 'Carlos' se ordenen sin que
    # las mayúsculas alteren el orden alfabético.
    return sorted(
        filas,
        key=lambda fila: fila.split(sep)[col].strip().lower(),
        reverse=descendente
    )


# ------------------------------------------------------------------------------
# POSIBILIDAD 2: Ordenar por números enteros (menor a mayor o mayor a menor)
# ------------------------------------------------------------------------------
def posibilidad_2_ordenar_enteros(filas, col=3, sep=";", descendente=False):
    # Convertimos a int() para que 9 vaya antes que 19 (como texto iría después).
    return sorted(
        filas,
        key=lambda fila: int(fila.split(sep)[col].strip()),
        reverse=descendente
    )


# ------------------------------------------------------------------------------
# POSIBILIDAD 3: Ordenar por dos criterios (ej. Ciudad A-Z y luego Edad)
# ------------------------------------------------------------------------------
def posibilidad_3_ordenar_dos_criterios(filas, col_1=2, col_2=3, sep=";", desc_col_2=False):
    # Devolver una tupla en la lambda ordena primero por col_1 y, ante empate,
    # desempata por col_2. Si desc_col_2=True, negamos el número (-int(...)).
    return sorted(
        filas,
        key=lambda fila: (
            fila.split(sep)[col_1].strip().lower(),
            -int(fila.split(sep)[col_2].strip()) if desc_col_2 else int(fila.split(sep)[col_2].strip())
        )
    )


# ------------------------------------------------------------------------------
# POSIBILIDAD 4: Ordenar por números decimales (con punto o con coma)
# ------------------------------------------------------------------------------
def posibilidad_4_ordenar_decimales(filas, col=3, sep=";", descendente=False):
    # Reemplazamos ',' por '.' por si el archivo trae decimales en formato español.
    return sorted(
        filas,
        key=lambda fila: float(fila.split(sep)[col].strip().replace(",", ".")),
        reverse=descendente
    )


# ------------------------------------------------------------------------------
# POSIBILIDAD 5: Ordenar por longitud de un campo de texto (ej. nombre más corto)
# ------------------------------------------------------------------------------
def posibilidad_5_ordenar_por_longitud(filas, col=0, sep=";", descendente=False):
    # len() mide cuántos caracteres tiene el texto de esa columna.
    return sorted(
        filas,
        key=lambda fila: len(fila.split(sep)[col].strip()),
        reverse=descendente
    )


# ------------------------------------------------------------------------------
# POSIBILIDAD 6: Filtrar filas por condición numérica (ej. edad >= 18)
# ------------------------------------------------------------------------------
def posibilidad_6_filtrar_numero(filas, minimo, col=3, sep=";"):
    # filter() + lambda conserva solo las filas que cumplen la condición.
    return list(
        filter(
            lambda fila: int(fila.split(sep)[col].strip()) >= minimo,
            filas
        )
    )


# ------------------------------------------------------------------------------
# POSIBILIDAD 7: Filtrar filas por coincidencia de texto (ej. ciudad o subcadena)
# ------------------------------------------------------------------------------
def posibilidad_7_filtrar_texto(filas, texto_buscado, col=2, sep=";", solo_igual=True):
    # Si solo_igual=True busca coincidencia exacta (sin mayúsculas);
    # si solo_igual=False busca si el texto aparece dentro del campo.
    objetivo = texto_buscado.strip().lower()
    if solo_igual:
        return list(
            filter(
                lambda fila: fila.split(sep)[col].strip().lower() == objetivo,
                filas
            )
        )
    return list(
        filter(
            lambda fila: objetivo in fila.split(sep)[col].strip().lower(),
            filas
        )
    )


# ------------------------------------------------------------------------------
# POSIBILIDAD 8: Transformar una columna manteniendo el resto de la fila
# ------------------------------------------------------------------------------
def posibilidad_8_transformar_columna(filas, col=0, sep=";"):
    # map() + lambda modifica solo la columna indicada (ej. pasar a MAYÚSCULAS)
    # y vuelve a unir la fila con el separador.
    return list(
        map(
            lambda fila: sep.join(
                [
                    c.strip().upper() if idx == col else c.strip()
                    for idx, c in enumerate(fila.split(sep))
                ]
            ),
            filas
        )
    )


# ------------------------------------------------------------------------------
# POSIBILIDAD 9: Seleccionar o reordenar columnas (ej. "Ciudad;Nombre")
# ------------------------------------------------------------------------------
def posibilidad_9_reordenar_columnas(filas, indices_columnas=(2, 0), sep=";"):
    # Construye una nueva fila tomando únicamente las columnas indicadas en orden.
    return list(
        map(
            lambda fila: sep.join(
                [fila.split(sep)[i].strip() for i in indices_columnas]
            ),
            filas
        )
    )


# ------------------------------------------------------------------------------
# POSIBILIDAD 10: Combinar filtrado + ordenación en una sola operación
# ------------------------------------------------------------------------------
def posibilidad_10_filtrar_y_ordenar(filas, ciudad, col_filtro=2, col_orden=3, sep=";", descendente=False):
    # Primero filtramos por ciudad con filter + lambda y sobre el resultado
    # aplicamos sorted() con otra lambda para ordenar por número.
    filtradas = filter(
        lambda fila: fila.split(sep)[col_filtro].strip().lower() == ciudad.strip().lower(),
        filas
    )
    return sorted(
        filtradas,
        key=lambda fila: int(fila.split(sep)[col_orden].strip()),
        reverse=descendente
    )


# ------------------------------------------------------------------------------
# POSIBILIDAD 11: Obtener el máximo o mínimo según una columna sin ordenar todo
# ------------------------------------------------------------------------------
def posibilidad_11_max_y_min(filas, col=3, sep=";"):
    # max() y min() aceptan 'key=lambda ...' igual que sorted().
    fila_max = max(filas, key=lambda fila: int(fila.split(sep)[col].strip()))
    fila_min = min(filas, key=lambda fila: int(fila.split(sep)[col].strip()))
    return fila_max, fila_min


# ==============================================================================
# BLOQUE DE PRUEBA (CON DATOS DE EJEMPLO EN MEMORIA PARA PROBAR RÁPIDO)
# ==============================================================================
if __name__ == "__main__":
    datos_ejemplo = [
        "Carlos;Gómez Pérez;Sevilla;31",
        "Elena;Martínez Ruiz;Madrid;19",
        "Lucía;Navarro Gil;Valencia;9",
        "David;Martín López;Madrid;25",
        "Ana;Sánchez Ruiz;Sevilla;19",
    ]

    # Si quieres leer desde un archivo real en vez de 'datos_ejemplo':
    # datos_ejemplo = cargar_filas("personas.txt", sep=";")

    print("--- 1. Ordenar por nombre (col 0, texto) ---")
    print(posibilidad_1_ordenar_texto(datos_ejemplo, col=0))

    print("\n--- 2. Ordenar por edad (col 3, entero ascendente) ---")
    print(posibilidad_2_ordenar_enteros(datos_ejemplo, col=3, descendente=False))

    print("\n--- 3. Ordenar por ciudad (col 2) y desempatar por edad descendente (col 3) ---")
    print(posibilidad_3_ordenar_dos_criterios(datos_ejemplo, col_1=2, col_2=3, desc_col_2=True))

    print("\n--- 4. Ordenar por decimales (ejemplo con notas/precios) ---")
    datos_decimales = ["ProdA;Cat1;12,5", "ProdB;Cat1;3,25", "ProdC;Cat2;12.1"]
    print(posibilidad_4_ordenar_decimales(datos_decimales, col=2, sep=";"))

    print("\n--- 5. Ordenar por longitud del nombre (col 0) ---")
    print(posibilidad_5_ordenar_por_longitud(datos_ejemplo, col=0))

    print("\n--- 6. Filtrar mayores o iguales de 18 años (col 3) ---")
    print(posibilidad_6_filtrar_numero(datos_ejemplo, minimo=18, col=3))

    print("\n--- 7. Filtrar apellidos que contengan 'martín' (col 1) ---")
    print(posibilidad_7_filtrar_texto(datos_ejemplo, "martín", col=1, solo_igual=False))

    print("\n--- 8. Transformar nombre (col 0) a MAYÚSCULAS ---")
    print(posibilidad_8_transformar_columna(datos_ejemplo, col=0))

    print("\n--- 9. Reordenar columnas a 'Ciudad;Nombre' (cols 2 y 0) ---")
    print(posibilidad_9_reordenar_columnas(datos_ejemplo, indices_columnas=(2, 0)))

    print("\n--- 10. Filtrar 'Madrid' y ordenar por edad ascendente ---")
    print(posibilidad_10_filtrar_y_ordenar(datos_ejemplo, ciudad="Madrid", col_filtro=2, col_orden=3))

    print("\n--- 11. Máximo y mínimo por edad (col 3) ---")
    mayor, menor = posibilidad_11_max_y_min(datos_ejemplo, col=3)
    print("Mayor edad:", mayor)
    print("Menor edad:", menor)

    # Ejemplo de cómo guardar cualquiera de los resultados en un archivo:
    # guardar_filas("salida_examen.txt", posibilidad_2_ordenar_enteros(datos_ejemplo, col=3))