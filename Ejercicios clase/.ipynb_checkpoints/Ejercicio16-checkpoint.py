try:
    n = int(input("Introduce el valor de n (entero positivo): "))
    
    if n <= 0:
        print("Por favor, introduce un número mayor que 0.")
    else:
        suma_serie = 0.0
        
        for i in range(1, n + 1):
            suma_serie += 1 / i
            
        print(f"\nLa suma de la serie hasta 1/{n} es: {suma_serie}")
        
except ValueError:
    print("Error: Debes introducir un número entero válido.")