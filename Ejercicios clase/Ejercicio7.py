nota = int(input("Introduzca la nota (de 0 a 10): "))

if nota < 0 or nota > 10:
    print("Nota no válida. Debe estar entre 0 y 10.")
elif nota < 5.0:
    print("Calificación: Suspenso")
elif nota < 7.0:
    print("Calificación: Aprobado")
elif nota < 9.0:
    print("Calificación: Notable")
elif nota < 10.0:
    print("Calificación: Sobresaliente")
else:
    print("Calificación: Matrícula de honor")
