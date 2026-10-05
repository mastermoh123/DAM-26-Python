p1 = int(input("Introduzca la primera puntuación (0-100): "))
p2 = int(input("Introduzca la segunda puntuación (0-100): "))
p3 = int(input("Introduzca la tercera puntuación (0-100): "))
p4 = int(input("Introduzca la cuarta puntuación (0-100): "))

media = (p1 + p2 + p3 + p4) / 4
print(f"\nLa media obtenida es: {media:.2f}")

if 90 <= media <= 100:
    calificacion = "A"
elif 80 <= media < 90:
    calificacion = "B"
elif 70 <= media < 80:
    calificacion = "C"
elif 60 <= media < 70:
    calificacion = "D"
elif 0 <= media < 60:
    calificacion = "E"
else:
    calificacion = "Puntuación fuera de rango válido"

print(f"La calificación correspondiente es: {calificacion}")
