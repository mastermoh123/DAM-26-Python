numeros = []

print("Por favor, introduce 6 números en total:")
for i in range(6):
    num = float(input(f"Número {i + 1}: "))
    numeros.append(num)

lista1 = sorted(numeros[:3])
lista2 = sorted(numeros[3:])

tupla_resultado = tuple(lista1 + lista2)

print("\n--- RESULTADOS ---")
print(f"Contenido de la primera lista: {lista1}")
print(f"Contenido de la segunda lista: {lista2}")
print(f"Tupla concatenada: {tupla_resultado}")