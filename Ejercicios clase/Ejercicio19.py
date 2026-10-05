numPer = int(input("Introduzca el número de personas: "))

mayorEdad = []
menorEdad = []

for i in range(0, numPer):
    edad = int(input(f"Introduzca la edad de la persona {i}: "))
    if(edad < 18):
        menorEdad.append(f"Persona {i} es menor de edad")
    else:
        mayorEdad.append(f"Persona {i} es mayor de edad")

for persona in menorEdad:
    print(persona)

for persona in mayorEdad:
    print(persona)