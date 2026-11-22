def CalcularSegundos(horas, minutos, segundos):
    return horas * 3600 + minutos * 60 + segundos

def CalcularTiempo(segundos_totales):
    horas = segundos_totales // 3600
    resto = segundos_totales % 3600
    minutos = resto // 60
    segundos = resto % 60
    return (horas, minutos, segundos)

while True:
    print("\n--- MENÚ DE CONVERSIÓN ---")
    print("1. Convertir a segundos")
    print("2. Convertir a horas, minutos y segundos")
    print("3. Salir")
    opcion = input("Elige una opción: ")

    if opcion == "1":
        h = int(input("Horas: "))
        m = int(input("Minutos: "))
        s = int(input("Segundos: "))
        print(f"Total: {CalcularSegundos(h, m, s)} segundos.")
    elif opcion == "2":
        s_tot = int(input("Cantidad de segundos: "))
        h, m, s = CalcularTiempo(s_tot)
        print(f"Equivalente a: {h}h {m}m {s}s.")
    elif opcion == "3":
        print("Saliendo del programa...")
        break
    else:
        print("Opción incorrecta.")