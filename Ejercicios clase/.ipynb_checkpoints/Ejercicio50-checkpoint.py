import sqlite3

def bd_to_diccionario():
    dicc = {}
    with sqlite3.connect("equipo.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT dni, fecha_baja, peso, altura FROM jugadores")
        for dni, fecha_baja, peso, altura in cursor.fetchall():
            dicc[dni] = (fecha_baja, peso, altura)
    return dicc

def diccionario_to_fichero(dicc):
    with open("jugadores.txt", "w", encoding="utf-8") as f:
        for dni, (fecha_baja, peso, altura) in dicc.items():
            f.write(f"{dni}, {fecha_baja}, {peso}, {altura}\n")

if __name__ == "__main__":
    datos = bd_to_diccionario()
    diccionario_to_fichero(datos)
    print(f"Exportados {len(datos)} registros a jugadores.txt")