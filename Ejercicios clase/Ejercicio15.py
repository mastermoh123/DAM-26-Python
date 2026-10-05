try:
    numero = int(input("Introduce un número entero para descomponer: "))
    
    if numero <= 1:
        print("Por favor, introduce un número entero mayor que 1.")
    else:
        print(f"Descomposición en factores primos de {numero}:")
        n = numero
        factor = 2
        factores = []
        
        while n > 1:
            if n % factor == 0:
                factores.append(factor)
                n //= factor            
            else:
                factor += 1             

        resultado_visual = " x ".join(str(f) for f in factores)
        print(f"{numero} = {resultado_visual}")

except Exception as e:
    print(f"Ocurrió un error: {e}")
