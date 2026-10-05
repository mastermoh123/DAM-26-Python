try:
    n = int(input("Introduce un número entero: "))
    
    if n <= 1:
        print(f"El número {n} NO es primo (los primos son mayores que 1).")
    else:
        es_primo = True
        
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                es_primo = False
                break 
                
        if es_primo:
            print(f"¡El número {n} ES primo!")
        else:
            print(f"El número {n} NO es primo.")
            
except ValueError:
    print("Error: Debes introducir un número entero válido.")