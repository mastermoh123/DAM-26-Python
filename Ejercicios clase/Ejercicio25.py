def pedir_vector():
  n = int(input("Introduce el tamaño del vector (N): "))
  t = []
  for i in range(n):
    t.append(float(input(f"  Elemento [{i}]: ")))
  return t


def pedir_matriz(nombre="matriz"):
  n = int(
      input(
          f"Introduce el tamaño N para la matriz cuadrada {nombre} (NxN): "
      )
  )
  m = []
  print(f"Introduce los elementos de la {nombre}:")
  for i in range(n):
    fila = []
    for j in range(n):
      fila.append(float(input(f"  {nombre}[{i}][{j}]: ")))
    m.append(fila)
  return m


# 1) Sumar elementos de un vector
def ej1_suma_vector():
  print("\n--- 1) Suma de elementos de un vector ---")
  t = pedir_vector()
  suma = sum(t)  # O un bucle acumulador tradicional
  print(f"Vector: {t}")
  print(f"Suma total: {suma}")


# 2) Producto escalar de dos vectores
def ej2_producto_escalar():
  print("\n--- 2) Producto escalar de dos vectores ---")
  print("Vector 1:")
  t1 = pedir_vector()
  print("Vector 2 (debe ser del mismo tamaño):")
  t2 = pedir_vector()

  if len(t1) != len(t2):
    print("Error: Los vectores deben tener la misma longitud.")
    return

  producto = sum(a * b for a, b in zip(t1, t2))
  print(f"Producto escalar: {producto}")


# 3) Máximo y mínimo de un vector
def ej3_max_min():
  print("\n--- 3) Máximo y mínimo de un vector ---")
  t = pedir_vector()
  if not t:
    print("Vector vacío.")
    return
  maximo = max(t)
  minimo = min(t)
  print(f"Vector: {t}")
  print(f"Máximo: {maximo} | Mínimo: {minimo}")


# 4) Invertir un vector
def ej4_invertir_vector():
  print("\n--- 4) Invertir un vector ---")
  t = pedir_vector()
  invertido = t[::-1]
  print(f"Vector original: {t}")
  print(f"Vector invertido: {invertido}")


# 5) Sumar elementos de la fila k de una matriz NxN
def ej5_suma_fila_matriz():
  print("\n--- 5) Suma de la fila k de una matriz ---")
  m = pedir_matriz()
  n = len(m)
  k = int(input(f"Introduce el índice de la fila a sumar (0 a {n-1}): "))

  if 0 <= k < n:
    suma_fila = sum(m[k])
    print(f"Fila {k}: {m[k]}")
    print(f"Suma de la fila {k}: {suma_fila}")
  else:
    print("Fila fuera de rango.")


# 6) Sumar dos matrices m1 y m2
def ej6_sumar_matrices():
  print("\n--- 6) Suma de dos matrices NxN ---")
  print("Matriz 1:")
  m1 = pedir_matriz("m1")
  print("Matriz 2:")
  m2 = pedir_matriz("m2")

  n = len(m1)
  m3 = [[m1[i][j] + m2[i][j] for j in range(n)] for i in range(n)]

  print("Matriz Resultado (m3):")
  for fila in m3:
    print(fila)


# 7) Búsqueda lineal en un vector
def ej7_busqueda_vector():
  print("\n--- 7) Búsqueda lineal en un vector ---")
  t = pedir_vector()
  x = float(input("Introduce el elemento a buscar (x): "))

  exito = False
  p = -1
  for i in range(len(t)):
    if t[i] == x:
      p = i
      exito = True
      break

  print(f"¿Éxito?: {exito}")
  if exito:
    print(f"Elemento encontrado en la posición (índice) p = {p}")
  else:
    print("El elemento no se encuentra en el vector.")


# 8) Indicar si un vector de enteros está ordenado
def ej8_vector_ordenado():
  print("\n--- 8) Indicar si un vector está ordenado ---")
  n = int(input("Introduce el tamaño del vector: "))
  t = []
  for i in range(n):
    t.append(int(input(f"  Elemento entero [{i}]: ")))

  # Verificamos si está ordenado de forma ascendente o descendente
  ascendente = all(t[i] <= t[i + 1] for i in range(len(t) - 1))
  descendente = all(t[i] >= t[i + 1] for i in range(len(t) - 1))

  if ascendente or descendente:
    print(f"El vector {t} está ordenado.")
  else:
    print(f"El vector {t} NO está ordenado.")


# 9) Búsqueda lineal en una matriz
def ej9_busqueda_matriz():
  print("\n--- 9) Búsqueda lineal en una matriz ---")
  m = pedir_matriz()
  x = float(input("Introduce el elemento a buscar (x): "))

  exito = False
  p, q = -1, -1
  for i in range(len(m)):
    for j in range(len(m[i])):
      if m[i][j] == x:
        p, q = i, j
        exito = True
        break
    if exito:
      break

  print(f"¿Éxito?: {exito}")
  if exito:
    print(f"Elemento encontrado en la posición (p, q) = ({p}, {q})")
  else:
    print("El elemento no se encuentra en la matriz.")


# 10) Traspuesta de una matriz NxN
def ej10_transpuesta():
  print("\n--- 10) Traspuesta de una matriz NxN ---")
  m = pedir_matriz()
  n = len(m)
  transpuesta = [[m[j][i] for j in range(n)] for i in range(n)]

  print("Matriz Original:")
  for fila in m:
    print(fila)
  print("Matriz Traspuesta:")
  for fila in transpuesta:
    print(fila)


# 11) Suma de la diagonal secundaria
def ej11_diagonal_secundaria():
  print("\n--- 11) Suma de la diagonal secundaria ---")
  m = pedir_matriz()
  n = len(m)
  suma = 0
  for i in range(n):
    suma += m[i][n - 1 - i]

  print(f"Suma de la diagonal secundaria: {suma}")


# 12) Multiplicación de dos matrices m1(MxL) y m2(LxN)
def ej12_multiplicar_matrices():
  print("\n--- 12) Multiplicación de matrices m1(MxL) y m2(LxN) ---")
  m_filas = int(input("Introduce las filas de m1 (M): "))
  l_comun = int(input("Introduce las columnas de m1 / filas de m2 (L): "))
  n_columnas = int(input("Introduce las columnas de m2 (N): "))

  print("Introduce matriz m1 (MxL):")
  m1 = []
  for i in range(m_filas):
    fila = []
    for j in range(l_comun):
      fila.append(float(input(f"  m1[{i}][{j}]: ")))
    m1.append(fila)

  print("Introduce matriz m2 (LxN):")
  m2 = []
  for i in range(l_comun):
    fila = []
    for j in range(n_columnas):
      fila.append(float(input(f"  m2[{i}][{j}]: ")))
    m2.append(fila)

  # m3(MxN)
  m3 = [[0.0] * n_columnas for _ in range(m_filas)]
  for i in range(m_filas):
    for j in range(n_columnas):
      for k in range(l_comun):
        m3[i][j] += m1[i][k] * m2[k][j]

  print("Matriz Resultado m3 (MxN):")
  for fila in m3:
    print(fila)


# 13) Ordenar vector por selección
def ej13_seleccion_sort():
  print("\n--- 13) Ordenar vector por selección ---")
  t = pedir_vector()
  n = len(t)

  for i in range(n - 1):
    min_idx = i
    for j in range(i + 1, n):
      if t[j] < t[min_idx]:
        min_idx = j
    # Intercambiar
    t[i], t[min_idx] = t[min_idx], t[i]

  print(f"Vector ordenado: {t}")


# Menú principal
def main():
  while True:
    print("\n========================================")
    print("      MENÚ DE EJERCICIOS - ALGORITMOS   ")
    print("========================================")
    print("1. Suma elementos de un vector")
    print("2. Producto escalar de dos vectores")
    print("3. Máximo y mínimo de un vector")
    print("4. Invertir un vector")
    print("5. Sumar elementos de la fila k")
    print("6. Sumar dos matrices (m1 + m2)")
    print("7. Búsqueda lineal en un vector")
    print("8. Indicar si un vector está ordenado")
    print("9. Búsqueda lineal en una matriz")
    print("10. Traspuesta de una matriz")
    print("11. Suma de la diagonal secundaria")
    print("12. Multiplicación de dos matrices")
    print("13. Ordenar vector por selección")
    print("0. Salir")

    opcion = input("\nElige una opción (0-13): ")

    if opcion == "1":
      ej1_suma_vector()
    elif opcion == "2":
      ej2_producto_escalar()
    elif opcion == "3":
      ej3_max_min()
    elif opcion == "4":
      ej4_invertir_vector()
    elif opcion == "5":
      ej5_suma_fila_matriz()
    elif opcion == "6":
      ej6_sumar_matrices()
    elif opcion == "7":
      ej7_busqueda_vector()
    elif opcion == "8":
      ej8_vector_ordenado()
    elif opcion == "9":
      ej9_busqueda_matriz()
    elif opcion == "10":
      ej10_transpuesta()
    elif opcion == "11":
      ej11_diagonal_secundaria()
    elif opcion == "12":
      ej12_multiplicar_matrices()
    elif opcion == "13":
      ej13_seleccion_sort()
    elif opcion == "0":
      print("¡Hasta luego!")
      break
    else:
      print("Opción no válida. Por favor, elige entre 0 y 13.")


if __name__ == "__main__":
  main()