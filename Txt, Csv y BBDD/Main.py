"""
===============================================================================
GUÍA COMPLETA Y SCRIPT PARA EL EXAMEN: .TXT (TABLA 2D) -> LAMBDA -> .CSV -> MYSQL (PYMYSQL)
===============================================================================

Este archivo reúne en un solo lugar:
1. Conexión a MySQL/MariaDB con pymysql (host="db", puerto 3306, user="root",
   password="test", database="libreria") y ejemplos de qué cambiar.
2. Lectura de un .txt como tabla de 2 dimensiones (lista de listas) y ejemplos
   de qué cambiar (separador, cabecera, líneas vacías).
3. Filtrado y ordenación con funciones lambda (filter, sorted, map) y ejemplos
   de qué cambiar (texto, int, float, decimales con coma, dos columnas, descendente).
4. Exportación a .csv con el módulo csv y ejemplos de qué cambiar (delimitador,
   columnas seleccionadas, con o sin cabecera).
5. Creación de tabla, inserción por lotes con '%s' y consulta con pymysql,
   más ejemplos de adaptación (por ejemplo, cambiar de tabla 'personas' a 'libros').
6. Ejecución principal lista para probar y adaptar en el examen.

NOTA SOBRE PYMYSQL VS SQLITE3:
- En pymysql se conecta con pymysql.connect(...) y los parámetros SQL usan '%s' (no '?').
- En MySQL/MariaDB el autoincremento suele ser INT AUTO_INCREMENT PRIMARY KEY.
- Recuerda hacer connection.commit() tras INSERT / DELETE / UPDATE y cerrar con
  connection.close() (idealmente dentro de un bloque try ... finally).
===============================================================================
"""

import csv
import pymysql


# -----------------------------------------------------------------------------
# 1. CONEXIÓN A LA BASE DE DATOS CON PYMYSQL
# -----------------------------------------------------------------------------
# Qué hace:
# Abre la conexión contra el host/contenedor 'db' en el puerto 3306, usando las
# credenciales y la base de datos 'libreria' exigidas en clase.
# charset="utf8mb4" evita problemas con tildes, 'ñ' y caracteres especiales.
#
# Ejemplos de qué cambiar aquí:
# - Si en tu máquina local no existe el host Docker 'db':
#     host="localhost"
# - Si el examen pide otra base de datos (ej. "tienda" o "biblioteca"):
#     database="tienda"
# - Si cambian usuario, contraseña o puerto:
#     user="alumno", password="123", port=3307
def conectar_bbdd():
    return pymysql.connect(
        host="db",
        user="root",
        password="test",
        database="libreria",
        port=3306,
        charset="utf8mb4",
    )


# -----------------------------------------------------------------------------
# 2. LEER EL .TXT COMO TABLA DE 2 DIMENSIONES (FILAS Y COLUMNAS)
# -----------------------------------------------------------------------------
# Qué hace:
# - Cada línea no vacía del .txt se limpia con .strip() y se parte por 'sep_txt'
#   (por defecto ';') con .split(sep_txt).
# - Cada elemento se limpia con .strip() para quitar espacios extra.
# - El resultado 'tabla' es una lista de listas (2D): tabla[fila][columna].
#
# Ejemplos de qué cambiar aquí:
# - Si el archivo está separado por comas ',' o pipes '|':
#     sep_txt = ","   # o sep_txt = "|"
# - Si el .txt tiene una primera línea de cabecera que NO quieres incluir en 'tabla':
#     lineas = [l.strip() for l in f if l.strip()]
#     tabla = [extraer_fila(l) for l in lineas[1:]]
def leer_txt_como_tabla(ruta_txt, sep_txt=";"):
    extraer_fila = lambda linea: [campo.strip() for campo in linea.strip().split(sep_txt)]
    with open(ruta_txt, "r", encoding="utf-8") as f:
        return [extraer_fila(linea) for linea in f if linea.strip()]


# -----------------------------------------------------------------------------
# 3. FILTRAR Y ORDENAR CON FUNCIONES LAMBDA (EJEMPLOS DE ADAPTACIÓN)
# -----------------------------------------------------------------------------
# Qué hace:
# - filter(lambda fila: ..., tabla) filtra filas según una condición booleana.
# - sorted(tabla, key=lambda fila: ..., reverse=...) ordena filas completas
#   según una clave calculada con lambda (sin separar los datos de cada fila).
# - map(lambda fila: ..., tabla) transforma cada fila (por ejemplo, para elegir
#   columnas o convertir tipos).
#
# Ejemplos de qué cambiar según lo que pida el enunciado:
# A) Ordenar por texto (ej. columna 0 = nombre, ignorando mayúsculas/minúsculas):
#    tabla_ord = sorted(tabla, key=lambda f: f[0].lower(), reverse=False)
#
# B) Ordenar por entero (ej. columna 3 = edad, de menor a mayor; reverse=True para mayor a menor):
#    tabla_ord = sorted(tabla, key=lambda f: int(f[3]), reverse=False)
#
# C) Ordenar por decimal (ej. columna 2 = precio, soportando coma o punto decimal):
#    tabla_ord = sorted(tabla, key=lambda f: float(f[2].replace(",", ".")), reverse=True)
#
# D) Ordenar por DOS criterios (ej. ciudad [col 2] A-Z y, si empatan, edad [col 3] ascendente):
#    tabla_ord = sorted(tabla, key=lambda f: (f[2].lower(), int(f[3])))
#
# E) Ordenar por DOS criterios con el segundo DESCENDENTE (ej. ciudad A-Z y edad mayor a menor):
#    tabla_ord = sorted(tabla, key=lambda f: (f[2].lower(), -int(f[3])))
#
# F) Filtrar por número (ej. edad [col 3] mayor o igual a 18):
#    filtrada = list(filter(lambda f: int(f[3]) >= 18, tabla))
#
# G) Filtrar por texto contenido (ej. apellido [col 1] que contenga "martín"):
#    filtrada = list(filter(lambda f: "martín" in f[1].lower(), tabla))
def filtrar_y_ordenar(tabla, col_orden=3, numerico=True, descendente=False, ciudad_filtro=None):
    resultado = tabla

    if ciudad_filtro:
        es_ciudad = lambda fila: fila[2].lower() == ciudad_filtro.strip().lower()
        resultado = list(filter(es_ciudad, resultado))

    clave_orden = lambda fila: (
        int(fila[col_orden]) if numerico else fila[col_orden].lower()
    )
    return sorted(resultado, key=clave_orden, reverse=descendente)


# -----------------------------------------------------------------------------
# 4. EXPORTAR LA TABLA A ARCHIVO .CSV
# -----------------------------------------------------------------------------
# Qué hace:
# - Abre el archivo CSV con newline="" para evitar líneas en blanco sobrantes.
# - Escribe la cabecera con writerow(...) y las filas con writerows(...).
#
# Ejemplos de qué cambiar aquí:
# - Si piden CSV separado por punto y coma ';':
#     escritor = csv.writer(f_csv, delimiter=";")
# - Si piden CSV SIN cabecera:
#     borra o comenta la línea escritor.writerow(...)
# - Si solo quieres exportar ciertas columnas (ej. col 0 y col 3):
#     filas_csv = list(map(lambda f: [f[0], f[3]], tabla))
#     escritor.writerows(filas_csv)
def exportar_a_csv(tabla, ruta_csv, cabecera=None, sep_csv=","):
    with open(ruta_csv, "w", newline="", encoding="utf-8") as f_csv:
        escritor = csv.writer(f_csv, delimiter=sep_csv)
        if cabecera is not None:
            escritor.writerow(cabecera)
        escritor.writerows(tabla)


# -----------------------------------------------------------------------------
# 5. GUARDAR Y CONSULTAR EN MYSQL CON PYMYSQL
# -----------------------------------------------------------------------------
# Qué hace:
# - Conecta a 'libreria', crea la tabla si no existe, limpia duplicados de prueba,
#   transforma cada fila en tupla con los tipos correctos usando map + lambda,
#   inserta con executemany(..., '%s') y hace commit().
#
# Ejemplo de qué cambiar si el enunciado es de 'libros' (titulo;autor;precio;stock):
# - Tabla:
#     CREATE TABLE IF NOT EXISTS libros (
#         id INT AUTO_INCREMENT PRIMARY KEY,
#         titulo VARCHAR(150) NOT NULL,
#         autor VARCHAR(120) NOT NULL,
#         precio DECIMAL(10, 2) NOT NULL,
#         stock INT NOT NULL
#     )
# - Preparación con lambda:
#     preparar = lambda f: (f[0], f[1], float(f[2].replace(",", ".")), int(f[3]))
# - Inserción:
#     INSERT INTO libros (titulo, autor, precio, stock) VALUES (%s, %s, %s, %s)
def guardar_y_consultar_mysql(tabla):
    connection = conectar_bbdd()
    try:
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

            # Limpia registros anteriores para que reejecutar el script no duplique filas
            cursor.execute("DELETE FROM personas")

            # Convierte cada fila (lista de str) a tupla con los tipos de cada columna
            preparar_registro = lambda fila: (
                fila[0],
                fila[1],
                fila[2],
                int(fila[3]),
            )
            registros = list(map(preparar_registro, tabla))

            cursor.executemany(
                """
                INSERT INTO personas (nombre, apellidos, ciudad, edad)
                VALUES (%s, %s, %s, %s)
                """,
                registros,
            )

        connection.commit()

        with connection.cursor() as cursor:
            cursor.execute("SELECT id, nombre, apellidos, ciudad, edad FROM personas")
            return cursor.fetchall()
    finally:
        connection.close()


# -----------------------------------------------------------------------------
# 6. EJECUCIÓN COMPLETA DE PRUEBA
# -----------------------------------------------------------------------------
def main():
    ruta_txt = "personas.txt"
    ruta_csv = "personas_ordenadas.csv"

    # Crea un archivo de ejemplo si aún no existe para poder probarlo directamente
    try:
        with open(ruta_txt, "x", encoding="utf-8") as f_demo:
            f_demo.write(
                "Carlos;Gómez Pérez;Sevilla;31\n"
                "Elena;Martínez Ruiz;Madrid;19\n"
                "Lucía;Navarro Gil;Sevilla;9\n"
                "David;Sánchez López;Valencia;25\n"
            )
    except FileExistsError:
        pass

    tabla = leer_txt_como_tabla(ruta_txt, sep_txt=";")
    tabla_ordenada = filtrar_y_ordenar(
        tabla,
        col_orden=3,
        numerico=True,
        descendente=False,
        ciudad_filtro=None,  # Pon ej. "Sevilla" si quieres filtrar por ciudad
    )

    exportar_a_csv(
        tabla_ordenada,
        ruta_csv,
        cabecera=["nombre", "apellidos", "ciudad", "edad"],
        sep_csv=",",
    )

    filas_bd = guardar_y_consultar_mysql(tabla_ordenada)

    print("=== TABLA ORDENADA (DESDE .TXT) ===")
    for fila in tabla_ordenada:
        print(fila)

    print("\n=== REGISTROS EN MYSQL (libreria) ===")
    for registro in filas_bd:
        print(registro)


if __name__ == "__main__":
    main()