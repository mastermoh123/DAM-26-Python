def leer_ventas_tienda():
    ventas = []
    for i in range(4):
        print(f"\nProducto {i+1}:")
        nombre = input("Introduce el nombre del producto: ")
        precio = float(input("Introduce el precio unitario: "))
        unidades = int(input("Introduce las unidades vendidas: "))
        ventas.append((nombre, precio, unidades))
    return ventas


def calcular_estadisticas_tienda(lista_ventas):
    estadisticas = {}
    for nombre, precio, unidades in lista_ventas:
        total_ventas = precio * unidades
        iva = round(total_ventas * 0.21, 2)
        
        if unidades > 30:
            popularidad = "Alta"
        elif unidades > 10:
            popularidad = "Media"
        else:
            popularidad = "Baja"
            
        estadisticas[nombre] = (total_ventas, iva, popularidad)
    return estadisticas


def analizar_rendimiento_tienda(dic_estadisticas):
    # 1. Filtrar productos con popularidad "Alta", formando tuplas (nombre, total_ventas) y ordenadas de mayor a menor
    alta_pop = [(nombre, datos[0]) for nombre, datos in dic_estadisticas.items() if datos[2] == "Alta"]
    alta_pop_ordenada = sorted(alta_pop, key=lambda x: x[1], reverse=True)

    # 2. Calcular el promedio de IVA de todos los productos redondeado a 2 decimales
    ivas = [datos[1] for datos in dic_estadisticas.values()]
    promedio_iva = round(sum(ivas) / len(ivas), 2) if ivas else 0.0

    # 3. Encontrar el producto con mayor total_ventas utilizando max con una función lambda
    producto_top = max(dic_estadisticas.keys(), key=lambda k: dic_estadisticas[k][0])

    return (alta_pop_ordenada, promedio_iva, producto_top)


if __name__ == '__main__':
    # Datos de prueba para comprobar el funcionamiento
    ventas_ejemplo = [
        ('Batido de proteínas', 3.5, 20), 
        ('Barrita energética', 1.5, 40),
        ('Botella de agua', 1.0, 55), 
        ('Toalla', 8.0, 5)
    ]
    
    stats = calcular_estadisticas_tienda(ventas_ejemplo)
    print("Diccionario de Estadísticas:\n", stats)
    
    analisis = analizar_rendimiento_tienda(stats)
    print("\nResultado del Análisis:\n", analisis)