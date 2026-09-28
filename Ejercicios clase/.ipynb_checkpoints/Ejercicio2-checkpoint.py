print("Introduce el primer número: ")
num1 = int(input())

print("Introduce el segundo número: ")
num2 = int(input())

print("")

print("1) Sumar")
print("2) Restar")
print("3) Multiplicar")
print("0) Salir")
print("Selecciona una de las opciones: ")
opcion = int(input())

while opcion != 0:
    
    match opcion:
        case 0:
            print("Adios")
            break
        case 1:
            print(f"Resultado: {num1 + num2}")
        case 2:
            print(f"Resultado: {num1 - num2}")
        case 3:
            print(f"Resultado: {num1 * num2}")
        case _:
            print("Esa opción no existe")

    print("1) Sumar")
    print("2) Restar")
    print("3) Multiplicar")
    print("0) Salir")
    print("Selecciona una de las opciones: ")
    opcion = int(input())