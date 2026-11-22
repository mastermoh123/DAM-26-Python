from functools import reduce

# c)
def totalCarga(diccionario):
    cargas = map(lambda v: v[0], diccionario.values())
    return [reduce(lambda acc, x: acc + x, cargas, 0)]

# d)
def obtenerCarga(diccionario):
    mercantes = filter(lambda item: item[0][0] == "mercante", diccionario.items())
    return tuple(map(lambda item: item[1][0], mercantes))