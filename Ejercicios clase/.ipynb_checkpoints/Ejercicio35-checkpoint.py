trabajadores = ("Pedro", "María", "Pedro", "Juan", "María", "Marta", "Pedro")
fichaje = {}
personasD = []

for i in range(len(trabajadores)):
 
    if trabajadores[i] not in fichaje:
        fichaje[trabajadores[i]] = True
    else:
        fichaje[trabajadores[i]] = not fichaje[trabajadores[i]]

print(fichaje)

for trabajador, estado in fichaje.items():
    if estado == False:
        print(f"{trabajador} ha salido y entrado.")
    else:
        personasD.append(trabajador)

print(personasD)

        