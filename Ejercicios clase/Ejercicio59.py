from functools import reduce

# a)
def medicamentosFinanciados(diccionario):
    financiados = filter(lambda item: item[1][0] == "SI", diccionario.items())
    return tuple(map(lambda item: item[0][0], financiados))

# b)
def mayorVolumenNoFinanciado(diccionario):
    jarabes_no = list(filter(lambda item: item[0][1] == "jarabe" and item[1][0] == "NO", diccionario.items()))
    mayor = reduce(lambda a, b: a if a[1][1] > b[1][1] else b, jarabes_no)
    return [mayor[0][0]]