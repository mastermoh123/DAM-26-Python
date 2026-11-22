def LeerFecha():
    dia = int(input("Introduce el día: "))
    mes = int(input("Introduce el mes: "))
    anio = int(input("Introduce el año: "))
    return (dia, mes, anio)

def es_bisiesto(anio):
    return (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0)

def DiaJuliano(dia, mes, anio):
    dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if es_bisiesto(anio):
        dias_mes[1] = 29
    return sum(dias_mes[:mes - 1]) + dia

d, m, a = LeerFecha()
print(f"El día juliano correspondiente es: {DiaJuliano(d, m, a)}")