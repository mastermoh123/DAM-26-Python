from Socio import Socio
from SocioPremium import SocioPremium

if __name__ == '__main__':
    # 1. Crear dos objetos de cada clase
    s1 = Socio("Alejandro Pérez", 40.0)
    s2 = Socio("María Gómez", 35.0)
    sp1 = SocioPremium("Carlos Ruiz", 50.0, [10.0, 15.0])
    sp2 = SocioPremium("Laura Torres", 50.0, [20.0])

    print("--- INFORMACIÓN INICIAL ---")
    print(s1)
    print(s2)
    print(sp1)
    print(sp2)

    print("\n--- CUOTAS CON 20% DE DESCUENTO ---")
    print(f"{s1.nombre}: {s1.calcular_cuota(20)}€")
    print(f"{s2.nombre}: {s2.calcular_cuota(20)}€")
    print(f"{sp1.nombre}: {sp1.calcular_cuota(20)}€")
    print(f"{sp2.nombre}: {sp2.calcular_cuota(20)}€")

    print("\n--- MODIFICACIONES Y CONTRATACIÓN DE SERVICIOS ---")
    s1.cuota_mensual = 45.0
    sp1.contratar_servicio(12.0)
    sp1.contratar_servicio(8.0)

    print("\n--- INFORMACIÓN ACTUALIZADA ---")
    print(s1)
    print(sp1)