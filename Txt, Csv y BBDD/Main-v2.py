"""
===============================================================================
PLANTILLA COMPLETA DE EXAMEN: LECTURA Y ESCRITURA EN .TXT, .CSV Y MYSQL (PYMYSQL)
===============================================================================
Este script cubre los 6 pasos bidireccionales (leer y escribir en cada formato):
  1. LEER desde .txt (como tabla 2D: lista de listas)
  2. PROCESAR / FILTRAR / ORDENAR con funciones lambda
  3. ESCRIBIR en .txt (nuevo archivo ordenado)
  4. ESCRIBIR en .csv y LEER desde .csv
  5. ESCRIBIR en MySQL ('libreria' con pymysql) y LEER desde MySQL
  6. Sincronizar de vuelta: guardar lo leído de MySQL en .txt y .csv de respaldo

Conexión exigida:
  host="db", user="root", password="test", database="libreria", port=3306
===============================================================================
"""

import csv
import pymysql


# -----------------------------------------------------------------------------
# CONEXIÓN A MYSQL CON PYMYSQL
# -----------------------------------------------------------------------------
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
# 1. LECTURA Y ESCRITURA EN ARCHIVOS .TXT (TABLA 2D)
# -----------------------------------------------------------------------------
def leer_txt(ruta_txt, sep=";"):
    """Lee un .txt y lo devuelve como tabla 2D (lista de listas limpias)."""
    extraer_fila = lambda linea: [campo.strip() for campo in linea.strip().split(sep)]
    with open(ruta_txt, "r", encoding="utf-8") as f:
        return [extraer_fila(linea) for linea in f if linea.strip()]


def escribir_txt(tabla, ruta_txt, sep=";"):
    """Escribe una tabla 2D en un archivo .txt uniendo cada fila con 'sep'."""
    formatear_fila = lambda fila: sep.join(str(campo) for campo in fila)
    lineas = list(map(formatear_fila, tabla))
    with open(ruta_txt, "w", encoding="utf-8") as f:
        if lineas:
            f.write("\n".join(lineas) + "\n")


# -----------------------------------------------------------------------------
# 2. LECTURA Y ESCRITURA EN ARCHIVOS .CSV
# -----------------------------------------------------------------------------
def escribir_csv(tabla, ruta_csv, cabecera=None, sep=","):
    """Escribe una tabla 2D en un .csv (con cabecera opcional)."""
    with open(ruta_csv, "w", newline="", encoding="utf-8") as f:
        escritor = csv.writer(f, delimiter=sep)
        if cabecera is not None:
            escritor.writerow(cabecera)
        escritor.writerows(tabla)


def leer_csv(ruta_csv, sep=",", tiene_cabecera=True):
    """Lee un .csv y devuelve (cabecera, tabla_2d)."""
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


# -----------------------------------------------------------------------------
# 3. ESCRITURA Y LECTURA EN BASE DE DATOS MYSQL (PYMYSQL)
# -----------------------------------------------------------------------------
def escribir_bbdd(tabla):
    """Crea la tabla 'personas' si no existe, limpia duplicados e inserta filas."""
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

            cursor.execute("DELETE FROM personas")

            # Lambda para convertir cada fila a tupla con los tipos SQL adecuados
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
    finally:
        connection.close()


def leer_bbdd():
    """Lee todos los registros de la tabla 'personas' ordenados por edad."""
    connection = conectar_bbdd()
    try:
        with connection.cursor() as cursor:
            cursor.execute(
                "SELECT id, nombre, apellidos, ciudad, edad FROM personas ORDER BY edad ASC"
            )
            return cursor.fetchall()
    finally:
        connection.close()


# -----------------------------------------------------------------------------
# 4. PROCESAMIENTO CON LAMBDA (FILTRAR Y ORDENAR)
# -----------------------------------------------------------------------------
def procesar_con_lambda(tabla, col_orden=3, numerico=True, descendente=False, ciudad_filtro=None):
    resultado = tabla

    if ciudad_filtro:
        resultado = list(
            filter(lambda f: f[2].lower() == ciudad_filtro.strip().lower(), resultado)
        )

    clave = lambda f: int(f[col_orden]) if numerico else f[col_orden].lower()
    return sorted(resultado, key=clave, reverse=descendente)


# -----------------------------------------------------------------------------
# 5. FLUJO COMPLETO: LEER Y ESCRIBIR EN TXT, CSV Y BBDD
# -----------------------------------------------------------------------------
def main():
    txt_entrada = "personas.txt"
    txt_salida = "personas_ordenadas.txt"
    csv_salida = "personas_ordenadas.csv"
    txt_desde_bd = "personas_desde_bbdd.txt"
    csv_desde_bd = "personas_desde_bbdd.csv"

    # Crear archivo inicial de prueba si no existe
    try:
        with open(txt_entrada, "x", encoding="utf-8") as f_demo:
            f_demo.write(
                "Carlos;Gómez Pérez;Sevilla;31\n"
                "Elena;Martínez Ruiz;Madrid;19\n"
                "Lucía;Navarro Gil;Sevilla;9\n"
                "David;Sánchez López;Valencia;25\n"
            )
    except FileExistsError:
        pass

    # PASO A: Leer de .txt -> ordenar con lambda -> escribir en nuevo .txt
    tabla_txt = leer_txt(txt_entrada, sep=";")
    tabla_ordenada = procesar_con_lambda(tabla_txt, col_orden=3, numerico=True, descendente=False)
    escribir_txt(tabla_ordenada, txt_salida, sep=";")
    print("1) Leído de .txt y escrito en:", txt_salida)

    # PASO B: Escribir en .csv -> volver a leer desde .csv
    cabecera = ["nombre", "apellidos", "ciudad", "edad"]
    escribir_csv(tabla_ordenada, csv_salida, cabecera=cabecera, sep=",")
    cabecera_leida, tabla_desde_csv = leer_csv(csv_salida, sep=",", tiene_cabecera=True)
    print(f"2) Escrito y leído desde .csv ({len(tabla_desde_csv)} filas), cabecera: {cabecera_leida}")

    # PASO C: Escribir en MySQL (desde lo leído del CSV) -> volver a leer desde MySQL
    escribir_bbdd(tabla_desde_csv)
    filas_bd = leer_bbdd()
    print("3) Registros leídos desde MySQL (libreria):")
    for reg in filas_bd:
        print("  ", reg)

    # PASO D: Exportar lo leído de la BBDD tanto a .txt como a .csv (incluyendo el id)
    tabla_bd_listas = [list(fila) for fila in filas_bd]
    escribir_txt(tabla_bd_listas, txt_desde_bd, sep=";")
    escribir_csv(
        tabla_bd_listas,
        csv_desde_bd,
        cabecera=["id", "nombre", "apellidos", "ciudad", "edad"],
        sep=",",
    )
    print(f"4) Datos de MySQL volcados de vuelta a {txt_desde_bd} y {csv_desde_bd}")


if __name__ == "__main__":
    main()