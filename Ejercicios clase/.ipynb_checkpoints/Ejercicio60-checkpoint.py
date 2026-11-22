from functools import reduce

# c)
def pastillasNoFinanciadas(diccionario):
    pastillas_no = filter(lambda item: item[0][1] == "pastilla" and item[1][0] == "NO", diccionario.items())
    return tuple(map(lambda item: item[0][0], pastillas_no))

# d)
def menorEnvase(diccionario):
    pastillas = list(filter(lambda item: item[0][1] == "pastilla", diccionario.items()))
    menor = reduce(lambda a, b: a if a[1][1] < b[1][1] else b, pastillas)
    return [menor[1][1]]