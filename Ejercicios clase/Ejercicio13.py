altura = int(input("Introduce la altura: "))

for i in range(altura):
    espacios = " " * (altura - i - 1)
    asteriscos = "*" * (2 * i + 1)
    print(espacios + asteriscos)
