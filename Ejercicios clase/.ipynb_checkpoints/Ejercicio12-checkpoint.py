a = int(input("Introduzca el primer número: "))
b = int(input("Introduzca el segundo número: "))
c = int(input("Introduzca el tercero número: "))

try:
    x = -c / (2*a +b)
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")

print(f"La solución es: {x}")