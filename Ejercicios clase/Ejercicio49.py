import sqlite3

def peso_medio():
    with sqlite3.connect("equipo.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT AVG(peso) FROM jugadores WHERE fecha_baja IS NOT NULL")
        return cursor.fetchone()[0]

def jugadores_retirados_delgados():
    media = peso_medio()
    with sqlite3.connect("equipo.db") as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT dni FROM jugadores WHERE fecha_baja IS NOT NULL AND peso < ?", (media,))
        dnis = cursor.fetchall()
    
    with open("jugadores.txt", "w", encoding="utf-8") as f:
        for (dni,) in dnis:
            f.write(f"{dni}\n")

if __name__ == "__main__":
    print(f"Peso medio retirados: {peso_medio():.2f} kg")
    jugadores_retirados_delgados()
    print("Fichero jugadores.txt generado.")