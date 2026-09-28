##Ejercicio 1
import random

numRand = random.randint(1, 10)
intento = 3

while intento > 0:
    numUsu = int(input("Introduce un número: ")) 
    
    if numUsu != numRand:
        intento -= 1
        print("No has acertado")
    else:
        print("ENHORABUENA")
        break
else:
    print("No te quedan intentos, el número era: ", numRand)