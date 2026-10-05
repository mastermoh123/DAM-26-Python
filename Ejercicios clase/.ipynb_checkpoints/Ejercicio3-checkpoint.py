print("Introduce la temperatura actual: ")
tempAct = int(input())

print("Introduce la temperatura deseada: ")
tempDes = int(input())

if(tempAct < tempDes):
    tempAct = tempDes
    print(f"Iniciando calentador. Temperatura actual: {tempAct}")
else:
    tempAct = tempDes
    print(f"Iniciando sistema de refrigeración. Temperatura actual: {tempAct}")