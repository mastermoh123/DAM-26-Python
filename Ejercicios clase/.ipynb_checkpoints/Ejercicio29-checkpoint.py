nPar = []
nImpar = []

print("Por favor, introduce 5 números en total:")
for i in range(5):
    num = int(input(f"Número {i + 1}: "))
    if(num % 2 == 0):
        nPar.append(num)
    else:
        nImpar.append(num)

print("\n--- RESULTADOS ---")
print(f"Contenido de pares: {nPar}")
print(f"Contenido de impares: {nImpar}")