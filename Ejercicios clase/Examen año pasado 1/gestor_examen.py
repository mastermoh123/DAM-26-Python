import csv
import pymysql


def conectar_bbdd(
    host="db",
    user="root",
    password="test",
    database="examen",
    port=3306,
    dict_cursor=False,
):
    """Conecta a MySQL/MariaDB usando pymysql con los parámetros del entorno."""
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


# -------------------------------------------------------------------------
# LECTURA Y ESCRITURA EN .TXT (TABLA 2D: LISTA DE LISTAS)
# -------------------------------------------------------------------------
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


# -------------------------------------------------------------------------
# LECTURA Y ESCRITURA EN .CSV
# -------------------------------------------------------------------------
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


def cargar_reservas_desde_csv(ruta_csv="reservas.csv", sep=","):
    """Devuelve {id_int: {'nombre': ..., 'telefono': ..., 'fecha': ..., 'personas': int, 'mesa': int}}."""
    reservas = {}
    with open(ruta_csv, "r", newline="", encoding="utf-8") as f:
        lector = csv.DictReader(f, delimiter=sep)
        for fila in lector:
            if not fila or not fila.get("id"):
                continue
            id_reserva = int(fila["id"].strip())
            reservas[id_reserva] = {
                "nombre": fila["nombre"].strip(),
                "telefono": fila["telefono"].strip(),
                "fecha": fila["fecha"].strip(),
                "personas": int(fila["personas"].strip()),
                "mesa": int(fila["mesa"].strip()),
            }
    return reservas


# -------------------------------------------------------------------------
# FUNCIONES CON LAMBDA (FILTRAR, ORDENAR, TRANSFORMAR)
# -------------------------------------------------------------------------
def filtrar_tabla(tabla, condicion_lambda):
    return list(filter(condicion_lambda, tabla))


def ordenar_tabla(tabla, clave_lambda, descendente=False):
    return sorted(tabla, key=clave_lambda, reverse=descendente)


def transformar_tabla(tabla, transform_lambda):
    return list(map(transform_lambda, tabla))


# -------------------------------------------------------------------------
# OPERACIONES MYSQL CON PYMYSQL (%S)
# -------------------------------------------------------------------------
def insertar_reservas_bbdd(reservas, host="db", user="root", password="test", database="examen", port=3306):
    registros = list(
        map(
            lambda item: (
                int(item[0]),
                item[1]["nombre"],
                item[1]["telefono"],
                item[1]["fecha"],
                int(item[1]["personas"]),
                int(item[1]["mesa"]),
            ),
            reservas.items(),
        )
    )

    conn = conectar_bbdd(host=host, user=user, password=password, database=database, port=port)
    try:
        with conn.cursor() as cursor:
            sql = """
                INSERT INTO reserva (
                    id, nombre_cliente, telefono, fecha_reserva, numero_personas, numero_mesa
                ) VALUES (%s, %s, %s, %s, %s, %s)
                ON DUPLICATE KEY UPDATE
                    nombre_cliente = VALUES(nombre_cliente),
                    telefono = VALUES(telefono),
                    fecha_reserva = VALUES(fecha_reserva),
                    numero_personas = VALUES(numero_personas),
                    numero_mesa = VALUES(numero_mesa)
            """
            cursor.executemany(sql, registros)
        conn.commit()
    finally:
        conn.close()


def consultar_reservas_fecha(fecha, host="db", user="root", password="test", database="examen", port=3306):
    conn = conectar_bbdd(host=host, user=user, password=password, database=database, port=port)
    try:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                SELECT nombre_cliente, telefono, numero_personas, numero_mesa
                FROM reserva
                WHERE fecha_reserva = %s
                ORDER BY numero_mesa ASC, id ASC
                """,
                (fecha,),
            )
            return cursor.fetchall()
    finally:
        conn.close()