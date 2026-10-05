vocales = ["a", "e", "i", "o", "u"]

letra = input("Introduce una letra: ")

if letra.lower() in vocales:
    print("Es vocal.")
else:
    print("Es consonante.")