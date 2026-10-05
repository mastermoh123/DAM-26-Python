try:
    n = int(input("Introduce el número de términos (n) para calcular pi: "))
    
    if n <= 0:
        print("Por favor, introduce un número entero mayor que 0.")
    else:
        producto = 1.0
        
        for i in range(1, n + 1):
            numerador = 2 * i
            den1 = numerador / (numerador - 1)
            den2 = numerador / (numerador + 1)
            producto *= den1 * den2
        
        pi_calculado = 2 * producto
        print(f"\nValor aproximado de pi con n={n}: {pi_calculado}")
        
except Exception as e:
    print(f"Ocurrió un error inesperado al procesar los datos: {e}")
