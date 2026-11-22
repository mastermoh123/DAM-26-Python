import csv
import mysql.connector

def conectar_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # Modifica este campo con tu contraseña de MySQL si la tienes configurada
        database="examen"
    )


def cargar_reservas_desde_csv():
    reservas = {}
    with open('reservas.csv', mode='r', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            id_reserva = int(fila['id'].strip())
            reservas[id_reserva] = {
                'nombre': fila['nombre'].strip(),
                'telefono': fila['telefono'].strip(),
                'fecha': fila['fecha'].strip(),
                'clase': fila['clase'].strip(),
                'duracion': int(fila['duracion'].strip())
            }
    return reservas


def insertar_reservas_bbdd(reservas):
    conexion = conectar_db()
    cursor = conexion.cursor()
    
    # Sentencia SQL con protección contra inyección y duplicados (UPSERT básico)
    sql = """
        INSERT INTO reserva (id, nombre, telefono, fecha, clase, duracion)
        VALUES (%s, %s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE 
        nombre=VALUES(nombre), telefono=VALUES(telefono), fecha=VALUES(fecha), clase=VALUES(clase), duracion=VALUES(duracion)
    """
    
    for id_res, datos in reservas.items():
        valores = (
            id_res,
            datos['nombre'],
            datos['telefono'],
            datos['fecha'],
            datos['clase'],
            datos['duracion']
        )
        cursor.execute(sql, valores)
        
    conexion.commit()
    cursor.close()
    conexion.close()


def mostrar_reservas_fecha(fecha):
    conexion = conectar_db()
    # Usamos dictionary=True para recuperar los registros como diccionarios de Python
    cursor = conexion.cursor(dictionary=True)
    
    sql = "SELECT * FROM reserva WHERE fecha = %s ORDER BY id"
    cursor.execute(sql, (fecha,))
    resultados = cursor.fetchall()
    
    cursor.close()
    conexion.close()
    
    if not resultados:
        print(f"No hay reservas para esa fecha.")
        return
        
    print(f"RESERVAS PARA {fecha}:")
    print("=========================")
    
    total_minutos = 0
    total_reservas = len(resultados)
    
    for r in resultados:
        print(f"{r['clase']} ({r['duracion']} min): {r['nombre']}     Tel: {r['telefono']}")
        total_minutos += r['duracion']
        
    print(f"Total: {total_reservas} reservas, {total_minutos} minutos\n")


def main():
    # 1. Cargar datos del CSV y mostrarlos
    print("Cargando reservas desde CSV...")
    reservas = cargar_reservas_desde_csv()
    print("Diccionario cargado correctamente:")
    print(reservas)
    
    # 2. Insertar los datos en la base de datos
    print("\nInsertando reservas en la base de datos MySQL...")
    insertar_reservas_bbdd(reservas)
    print("Inserción completada con éxito.")
    
    # 3. Mostrar reservas de las fechas indicadas
    print("\n--- CONSULTAS DE CALENDARIO ---")
    mostrar_reservas_fecha('2026-11-20')
    mostrar_reservas_fecha('2026-11-21')


if __name__ == '__main__':
    main()