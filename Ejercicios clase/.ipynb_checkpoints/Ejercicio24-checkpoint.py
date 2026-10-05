try:
    n = int(input("Introduce el número de filas para la matriz cuadrada: "))
    
    if n <= 0:
        print("Por favor, introduce un número entero mayor que 0.")
    else:
        print(f"\nMatriz cuadrada de {n}x{n}:")
        
        for i in range(1, n + 1):
            fila = []
            for j in range(1, n + 1):
                valor = i + j
                fila.append(valor)
            print("  ".join(f"{val:2d}" for val in fila))
            
except ValueError:
    print("Error: Debes introducir un número entero válido.")