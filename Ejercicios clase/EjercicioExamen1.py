def leer_tapas():
    lista = []
    for _in range(4):
        nombre_tapa = input("Nombre de la tapa.")
        precio = float(input("Precio de la tapa."))
        unidades = int(input("Unidades de la tapa."))

        tupla = (nombre_tapa, precio, unidades)
        lista.append(tupla)

    return lista

def calcular_estadisticas_tapas(lista_ventas):
    d = ()

    for tapa in lista_tapas:
        if tapa[2] > 25:
            popularidad = "Alta"
        else if tapa[2] > 15
            popularidad = "Media"
        else
            popularidad = "Baja"

    d[tapa[0]] = (tapa[1] * tapa[2], tapa[1] * 0.1, popularidad)

def analizar_rendimiento_tapas(dicc_tapas):

    tapas_popularidad_alta = filter (lambda tapa: tapa[1][2] == 'Alta', dicc_tapas.items() )

    lista_iva = map(lambda tapa: tapa[1][1] , dicc_tapas.items())

    promedio_iva = sum(map (lambda tapa: tapa[1][1], dicc_tapas.items() )) / len(dicc_tapas)
    