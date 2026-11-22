from functools import reduce

# a)
def obtenerPasajeros(diccionario):
    ferries = filter(lambda item: item[0][0] == "ferry", diccionario.items())
    return tuple(map(lambda item: item[1][1], ferries))

# b)
def mayorCarga(diccionario):
    mercantes = list(filter(lambda item: item[0][0] == "mercante", diccionario.items()))
    mayor = reduce(lambda a, b: a if a[1][0] > b[1][0] else b, mercantes)
    return [mayor[0][1]]