sueldo_actual = int(input("Introduzca el sueldo actual del trabajador: "))
antiguedad = int(input("Introduzca los años de antigüedad: "))

if sueldo_actual < 1500 and antiguedad >= 10:
    nuevo_sueldo = sueldo_actual * 1.20
    print(f"Le corresponde un aumento del 20%. Nuevo sueldo: {nuevo_sueldo:.2f}")

elif sueldo_actual < 1500 and antiguedad < 10:
    nuevo_sueldo = sueldo_actual * 1.05
    print(f"Le corresponde un aumento del 5%. Nuevo sueldo: {nuevo_sueldo:.2f}")

else:
    print(f"El sueldo se mantiene sin cambios: {sueldo_actual:.2f}")
