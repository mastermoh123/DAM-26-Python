mes = int(input("Introduzca el número del mes (1 al 12): "))

meses_31 = [1, 3, 5, 7, 8, 10, 12]  
meses_30 = [4, 6, 9, 11]            

if mes in meses_31:
    dias = 31
elif mes in meses_30:
    dias = 30
elif mes == 2:
    dias = 28
else:
    dias = None

if dias is not None:
    print(f"El mes {mes} tiene {dias} días.")
else:
    print("Número de mes no válido. Debe introducir un número del 1 al 12.")
