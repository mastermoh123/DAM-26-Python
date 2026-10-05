def multiplicar_matrices(A, B):
  """Función para multiplicar dos matrices 3x3 usando listas."""
  resultado = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
  for i in range(3):
    for j in range(3):
      for k in range(3):
        resultado[i][j] += A[i][k] * B[k][j]
  return resultado


def main():
  print("--- CREACIÓN DE MATRIZ 3X3 ---")
  print("Por favor, introduce 9 números uno a uno:")

  numeros = []
  for i in range(9):
    while True:
      try:
        num = float(input(f"Número {i+1}/9: "))
        numeros.append(num)
        break
      except ValueError:
        print("Error: Introduce un valor numérico válido.")

  matriz = []
  for i in range(3):
    fila = numeros[i * 3 : (i + 1) * 3]
    matriz.append(fila)

  print("\n--- MATRIZ INTRODUCIDA ---")
  for fila in matriz:
    print([int(x) if x.is_integer() else x for x in fila])

  matriz_cuadrada = multiplicar_matrices(matriz, matriz)

  print("\n--- MATRIZ AL CUDRADO (A x A) ---")
  for fila in matriz_cuadrada:
    print([int(x) if x.is_integer() else x for x in fila])


if __name__ == "__main__":
  main()