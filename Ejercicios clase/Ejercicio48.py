import sqlite3

def altura_media():
    with sqlite3.connect("equipo.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT AVG(altura) FROM jugadores WHERE fecha_baja IS NULL")
        return cursor.fetchone()[0]

def jugadores_altos():
    media = altura_media()
    with sqlite3.connect("equipo.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT dni FROM jugadores WHERE fecha_baja IS NULL AND altura > ?", (media,))
        dnis = cursor.fetchall()
    
    with open("jugadores.txt", "w", encoding="utf-8") as f:
        for (dni,) in dnis:
            f.write(f"{dni}\n")

if __name__ == "__main__":
    print(f"Altura media en activo: {altura_media():.2f} m")
    jugadores_altos()
    print("Fichero jugadores.txt generado.")