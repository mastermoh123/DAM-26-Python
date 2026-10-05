cont = 0
sumPos = 0
sumNeg = 0
media = 0

for i in range(0, 10):
    num = int(input("Introduce un número: "))
    
    if num < 0:
        cont += 1
        sumNeg = sumNeg + num
        media = sumNeg / cont

    else:
        sumPos = sumPos + num

if sumPos == 0:
    print("No se ha introducido ningún numero positivo.")
else:
    print(f"La suma total es: {sumPos}")
    
if sumNeg == 0:
    print("No se ha introducido ningún numero negativo.")
else:
    print(f"La media es: {media}")