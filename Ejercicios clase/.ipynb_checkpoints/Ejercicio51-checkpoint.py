import sqlite3

def filtrar_peso(peso_min, peso_max):
    with sqlite3.connect("equipo.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT dni FROM jugadores WHERE peso BETWEEN ? AND ?", (peso_min, peso_max))
        return [fila[0] for fila in cursor.fetchall()]

def lista_to_fichero(lista_dnis):
    with sqlite3.connect("equipo.db") as conn, open("jugadores.txt", "w", encoding="utf-8") as f:
        cursor = conn.cursor()
        for dni in lista_dnis:
            cursor.execute("SELECT dni, fecha_baja, peso, altura FROM jugadores WHERE dni = ?", (dni,))
            fila = cursor.fetchone()
            if fila:
                f.write(f"{fila[0]}, {fila[1]}, {fila[2]}, {fila[3]}\n")

if __name__ == "__main__":
    dnis = filtrar_peso(70, 85)
    lista_to_fichero(dnis)
    print("Fichero generado con los jugadores filtrados por peso.")