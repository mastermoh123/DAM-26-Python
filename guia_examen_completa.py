"""
===============================================================================
GUÍA MAESTRA Y PLANTILLA COMPLETA PARA EXAMEN:
TABLAS 2D + FUNCIONES LAMBDA + LECTURA/ESCRITURA EN .TXT, .CSV Y MYSQL (PYMYSQL)
===============================================================================

¿QUÉ CONTIENE ESTE ARCHIVO ÚNICO?
1. Conexión a MySQL / MariaDB con pymysql (host="db", port=3306, user="root",
   password="test", database="libreria") y variaciones habituales.
2. Estructura en 2 dimensiones (lista de listas: tabla[fila][columna]) y
   lectura / escritura en archivos .txt.
3. Lectura / escritura en archivos .csv con módulo `csv` (newline="",
   delimitadores, cabeceras, DictReader, etc.).
4. Catálogo completo de funciones `lambda` con `sorted`, `filter`, `map`,
   `min` y `max` (texto A-Z / Z-A, int, float, decimales con coma, múltiples
   criterios, desempates, números negativos en tupla, filtros compuestos).
5. Operaciones completas con `pymysql` usando marcadores `%s` (nunca `?`):
   CREATE TABLE, INSERT / executemany, SELECT (fetchall / fetchone),
   UPDATE y DELETE con try / finally y commit().
6. Flujo bidireccional completo (.txt <-> lambda <-> .csv <-> MySQL) y
   variaciones listas para adaptar en el examen.

===============================================================================
CHULETA RÁPIDA DE ADAPTACIÓN EN EL EXAMEN
===============================================================================
- Separador en .txt: cambiar sep=";" por sep="," o sep="|" o sep="\t".
- Índice de columna: empieza siempre en 0 (col 0, col 1, col 2, col 3...).
- Número entero: int(campo.strip())
- Número decimal (admite coma o punto): float(campo.strip().replace(",", "."))
- Orden ascendente / descendente: reverse=False (asc) / reverse=True (desc)
- Desempate en ordenación: key=lambda f: (clave1(f), clave2(f))
- Segundo criterio descendente numérico: key=lambda f: (clave1(f), -int(f[col]))
- Marcadores SQL en pymysql: SIEMPRE %s (nunca ?).
- Escritura / borrado en MySQL: SIEMPRE connection.commit() y cerrar conexión.
===============================================================================
"""

import csv
import pymysql


# =============================================================================
# 1. CONEXIÓN A MYSQL / MARIA DB CON PYMYSQL
# =============================================================================
# Configuración estándar exigida en clase:
#   host="db", user="root", password="test", database="libreria", port=3306
#
# Variaciones habituales en examen:
# - Conexión local fuera de Docker: host="localhost"
# - Otra base de datos: database="tienda" o database="biblioteca"
# - Filas como diccionario en vez de tupla: cursorclass=pymysql.cursors.DictCursor
def conectar_bbdd(
    host="db",
    user="root",
    password="test",
    database="libreria",
    port=3306,
    dict_cursor=False,
):
    cursor_cls = pymysql.cursors.DictCursor if dict_cursor else pymysql.cursors.Cursor
    return pymysql.connect(
        host=host,
        user=user,
        password=password,
        database=database,
        port=port,
        charset="utf8mb4",
        cursorclass=cursor_cls,
    )


# =============================================================================
# 2. ARCHIVOS .TXT COMO TABLA 2D (LECTURA Y ESCRITURA)
# =============================================================================
# Una tabla 2D es una lista de listas: tabla[fila][columna].
# Cada línea no vacía es una fila; cada campo separado por `sep` es una columna.
#
# Variaciones habituales en examen:
# - Separador distinto: sep="," / sep="|" / sep="\t"
# - El .txt trae cabecera en la primera línea: saltar_cabecera=True
# - Añadir al final sin borrar lo existente: escribir_txt(..., modo="a")
def leer_txt(ruta_txt, sep=";", saltar_cabecera=False):
    extraer_fila = lambda linea: [campo.strip() for campo in linea.strip().split(sep)]
    with open(ruta_txt, "r", encoding="utf-8") as f:
        lineas = [linea.strip() for linea in f if linea.strip()]
    if saltar_cabecera and lineas:
        lineas = lineas[1:]
    return [extraer_fila(linea) for linea in lineas]


def escribir_txt(tabla, ruta_txt, sep=";", cabecera=None, modo="w"):
    formatear_fila = lambda fila: sep.join(str(campo) for campo in fila)
    lineas = list(map(formatear_fila, tabla))
    with open(ruta_txt, modo, encoding="utf-8") as f:
        if cabecera is not None and modo == "w":
            f.write(formatear_fila(cabecera) + "\n")
        if lineas:
            f.write("\n".join(lineas) + "\n")


# =============================================================================
# 3. ARCHIVOS .CSV (ESCRITURA Y LECTURA)
# =============================================================================
# Siempre usar newline="" al abrir con el módulo `csv` para evitar líneas vacías
# extra.
#
# Variaciones habituales en examen:
# - CSV con punto y coma: sep=";"
# - CSV sin cabecera: cabecera=None al escribir, tiene_cabecera=False al leer
# - Leer como lista de diccionarios: leer_csv_dict(ruta_csv, sep=",")
def escribir_csv(tabla, ruta_csv, cabecera=None, sep=",", modo="w"):
    with open(ruta_csv, modo, newline="", encoding="utf-8") as f:
        escritor = csv.writer(f, delimiter=sep)
        if cabecera is not None and modo == "w":
            escritor.writerow(cabecera)
        escritor.writerows(tabla)


def leer_csv(ruta_csv, sep=",", tiene_cabecera=True):
    with open(ruta_csv, "r", newline="", encoding="utf-8") as f:
        lector = csv.reader(f, delimiter=sep)
        filas = [
            [campo.strip() for campo in fila]
            for fila in lector
            if any(campo.strip() for campo in fila)
        ]
    if tiene_cabecera and filas:
        return filas[0], filas[1:]
    return None, filas


def leer_csv_dict(ruta_csv, sep=","):
    with open(ruta_csv, "r", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter=sep))


# =============================================================================
# 4. CATÁLOGO DE FUNCIONES LAMBDA SOBRE TABLAS 2D
# =============================================================================
# En todos los ejemplos siguientes, `fila` es una lista de columnas, por ejemplo:
#   ["Carlos", "Gómez Pérez", "Sevilla", "31"]
#   col 0 -> nombre | col 1 -> apellidos | col 2 -> ciudad | col 3 -> edad/número


def ejemplos_lambda(tabla):
    # --- A) ORDENACIÓN CON sorted(..., key=lambda fila: ..., reverse=...) ---

    # 1. Por texto (col 0) alfabéticamente A-Z sin importar mayúsculas/minúsculas
    ord_texto_asc = sorted(tabla, key=lambda f: f[0].strip().lower())

    # 2. Por texto (col 0) alfabéticamente Z-A
    ord_texto_desc = sorted(tabla, key=lambda f: f[0].strip().lower(), reverse=True)

    # 3. Por número entero (col 3) de menor a mayor
    ord_int_asc = sorted(tabla, key=lambda f: int(f[3].strip()))

    # 4. Por número entero (col 3) de mayor a menor
    ord_int_desc = sorted(tabla, key=lambda f: int(f[3].strip()), reverse=True)

    # 5. Por número decimal (col 3) admitiendo coma o punto decimal
    ord_float_asc = sorted(
        tabla, key=lambda f: float(f[3].strip().replace(",", "."))
    )

    # 6. Por DOS criterios: primero ciudad (col 2) A-Z y, si empatan, edad (col 3) asc
    ord_dos_criterios = sorted(
        tabla, key=lambda f: (f[2].strip().lower(), int(f[3].strip()))
    )

    # 7. Por DOS criterios con el segundo DESCENDENTE (ciudad A-Z, edad mayor a menor)
    ord_dos_criterios_desc_num = sorted(
        tabla, key=lambda f: (f[2].strip().lower(), -int(f[3].strip()))
    )

    # 8. Por longitud de un campo de texto (ej. longitud del nombre en col 0)
    ord_longitud = sorted(tabla, key=lambda f: len(f[0].strip()))

    # --- B) FILTRADO CON list(filter(lambda fila: ..., tabla)) ---

    # 9. Igualdad exacta de texto (ej. ciudad == "sevilla")
    fil_ciudad = list(
        filter(lambda f: f[2].strip().lower() == "sevilla", tabla)
    )

    # 10. Subcadena contenida en un campo (ej. apellidos contienen "ruiz")
    fil_contiene = list(
        filter(lambda f: "ruiz" in f[1].strip().lower(), tabla)
    )

    # 11. Condición numérica (ej. edad >= 18)
    fil_mayores = list(filter(lambda f: int(f[3].strip()) >= 18, tabla))

    # 12. Condición compuesta con AND / OR (ej. de Sevilla Y mayor o igual a 18)
    fil_compuesto = list(
        filter(
            lambda f: f[2].strip().lower() == "sevilla" and int(f[3].strip()) >= 18,
            tabla,
        )
    )

    # --- C) TRANSFORMACIÓN CON list(map(lambda fila: ..., tabla)) Y EXTREMOS ---

    # 13. Transformar / seleccionar / reordenar columnas (ej. [CIUDAD, nombre, edad_int])
    transf_columnas = list(
        map(
            lambda f: [f[2].strip().upper(), f[0].strip(), int(f[3].strip())],
            tabla,
        )
    )

    # 14. Filtrar Y ordenar en cadena
    fil_y_ord = sorted(
        filter(lambda f: int(f[3].strip()) >= 18, tabla),
        key=lambda f: int(f[3].strip()),
        reverse=True,
    )

    # 15. Máximo y mínimo según una columna sin ordenar toda la tabla
    max_fila = max(tabla, key=lambda f: int(f[3].strip())) if tabla else None
    min_fila = min(tabla, key=lambda f: int(f[3].strip())) if tabla else None

    return {
        "ord_texto_asc": ord_texto_asc,
        "ord_texto_desc": ord_texto_desc,
        "ord_int_asc": ord_int_asc,
        "ord_int_desc": ord_int_desc,
        "ord_float_asc": ord_float_asc,
        "ord_dos_criterios": ord_dos_criterios,
        "ord_dos_criterios_desc_num": ord_dos_criterios_desc_num,
        "ord_longitud": ord_longitud,
        "fil_ciudad": fil_ciudad,
        "fil_contiene": fil_contiene,
        "fil_mayores": fil_mayores,
        "fil_compuesto": fil_compuesto,
        "transf_columnas": transf_columnas,
        "fil_y_ord": fil_y_ord,
        "max_fila": max_fila,
        "min_fila": min_fila,
    }


# =============================================================================
# 5. OPERACIONES COMPLETAS EN MYSQL CON PYMYSQL (CREAR, INSERTAR, LEER, UPDATE, DELETE)
# =============================================================================
# Regla de oro en pymysql:
# - Usa %s como marcador de parámetros en SQL (NUNCA ? ni f-strings con datos de usuario).
# - Llama a connection.commit() tras CREATE / INSERT / UPDATE / DELETE.
# - Cierra siempre la conexión en un bloque `finally: connection.close()`.


def crear_tabla_personas(connection):
    with connection.cursor() as cursor:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS personas (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(100) NOT NULL,
                apellidos VARCHAR(150) NOT NULL,
                ciudad VARCHAR(100) NOT NULL,
                edad INT NOT NULL
            )
        """)
    connection.commit()


def insertar_personas(connection, tabla, limpiar_antes=True):
    # Convierte cada fila (lista de str) a tupla con los tipos esperados por MySQL
    preparar = lambda f: (
        f[0].strip(),
        f[1].strip(),
        f[2].strip(),
        int(f[3].strip()),
    )
    registros = list(map(preparar, tabla))

    with connection.cursor() as cursor:
        if limpiar_antes:
            cursor.execute("DELETE FROM personas")
        cursor.executemany(
            """
            INSERT INTO personas (nombre, apellidos, ciudad, edad)
            VALUES (%s, %s, %s, %s)
            """,
            registros,
        )
    connection.commit()


def consultar_personas(connection, ciudad=None, edad_min=None, order_by="edad ASC"):
    sql = "SELECT id, nombre, apellidos, ciudad, edad FROM personas WHERE 1=1"
    params = []

    if ciudad is not None:
        sql += " AND LOWER(ciudad) = LOWER(%s)"
        params.append(ciudad.strip())

    if edad_min is not None:
        sql += " AND edad >= %s"
        params.append(int(edad_min))

    sql += f" ORDER BY {order_by}"

    with connection.cursor() as cursor:
        cursor.execute(sql, params)
        return cursor.fetchall()


def actualizar_ciudad_persona(connection, persona_id, nueva_ciudad):
    with connection.cursor() as cursor:
        cursor.execute(
            "UPDATE personas SET ciudad = %s WHERE id = %s",
            (nueva_ciudad.strip(), int(persona_id)),
        )
    connection.commit()


def eliminar_persona_por_id(connection, persona_id):
    with connection.cursor() as cursor:
        cursor.execute(
            "DELETE FROM personas WHERE id = %s",
            (int(persona_id),),
        )
    connection.commit()


# --- EJEMPLO DE CÓMO ADAPTAR A OTRA TABLA (ej. `libros`: titulo;autor;precio;stock) ---
# CREATE TABLE IF NOT EXISTS libros (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     titulo VARCHAR(150) NOT NULL,
#     autor VARCHAR(120) NOT NULL,
#     precio DECIMAL(10, 2) NOT NULL,
#     stock INT NOT NULL
# );
# preparar_libro = lambda f: (
#     f[0].strip(),
#     f[1].strip(),
#     float(f[2].strip().replace(",", ".")),
#     int(f[3].strip()),
# )
# cursor.executemany(
#     "INSERT INTO libros (titulo, autor, precio, stock) VALUES (%s, %s, %s, %s)",
#     list(map(preparar_libro, tabla)),
# )


# =============================================================================
# 6. FLUJO BIDIRECCIONAL COMPLETO (.TXT <-> LAMBDA <-> .CSV <-> MYSQL)
# =============================================================================
def main():
    txt_entrada = "personas.txt"
    txt_ordenado = "personas_ordenadas.txt"
    csv_ordenado = "personas_ordenadas.csv"
    txt_desde_bd = "personas_desde_bbdd.txt"
    csv_desde_bd = "personas_desde_bbdd.csv"

    # Crea personas.txt de ejemplo si no existe para poder probar sin preparativos
    try:
        with open(txt_entrada, "x", encoding="utf-8") as f:
            f.write(
                "Carlos;Gómez Pérez;Sevilla;31\n"
                "Elena;Martínez Ruiz;Madrid;19\n"
                "Lucía;Navarro Gil;Sevilla;9\n"
                "David;Sánchez López;Valencia;25\n"
            )
    except FileExistsError:
        pass

    # 1. Leer .txt como tabla 2D -> ordenar con lambda -> escribir .txt
    tabla_2d = leer_txt(txt_entrada, sep=";", saltar_cabecera=False)
    tabla_ordenada = sorted(tabla_2d, key=lambda f: int(f[3].strip()))
    escribir_txt(tabla_ordenada, txt_ordenado, sep=";")

    # 2. Escribir .csv y volver a leer desde .csv
    cabecera_personas = ["nombre", "apellidos", "ciudad", "edad"]
    escribir_csv(tabla_ordenada, csv_ordenado, cabecera=cabecera_personas, sep=",")
    _, tabla_leida_csv = leer_csv(csv_ordenado, sep=",", tiene_cabecera=True)

    # 3. Guardar en MySQL ('libreria') -> consultar -> exportar de vuelta a .txt y .csv
    conn = conectar_bbdd()
    try:
        crear_tabla_personas(conn)
        insertar_personas(conn, tabla_leida_csv, limpiar_antes=True)
        filas_bd = consultar_personas(conn, order_by="edad ASC")
    finally:
        conn.close()

    tabla_bd = list(map(lambda fila: list(fila), filas_bd))
    escribir_txt(tabla_bd, txt_desde_bd, sep=";")
    escribir_csv(
        tabla_bd,
        csv_desde_bd,
        cabecera=["id", "nombre", "apellidos", "ciudad", "edad"],
        sep=",",
    )

    print("Flujo completado.")
    print("Filas ordenadas (2D):", tabla_ordenada)
    print("Registros en MySQL:", filas_bd)


if __name__ == "__main__":
    main()
