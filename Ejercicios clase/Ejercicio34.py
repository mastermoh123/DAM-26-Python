dias_validos = ("lunes", "martes", "miércoles", "jueves", "viernes")
guardias = {}

while len(guardias) < 4:

    nom = input("Introduce el nombre de la persona: ").lower()

    while nom in guardias.values():
        nom = input("El nombre ya existe. Introduce otro: ")
    
    dia = input("Introduce el día de la guardia: ").lower()

    while dia not in dias_validos or dia in guardias:

        if(dia not in dias_validos):
            dia = input("Ese día no es valido. Introduce otro: ")
        if(dia in guardias):
            dia = input("Ese día está en uso. Introduce otro: ")

    guardias[dia] = nom

print(guardias)