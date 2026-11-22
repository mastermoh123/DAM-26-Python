from Producto import Producto
from PiezaMetalica import PiezaMetalica
from PiezaPlastico import PiezaPlastico

print("=== DEMOSTRACIÓN DEL SISTEMA DE FÁBRICA ==-\n")

producto1 = Producto("PRD-001", "Bicicleta de Montaña")

pm1 = PiezaMetalica("M01", 1200, 45.50, "http://metalparts.com", "Acero")
pm2 = PiezaMetalica("M02", 300, 15.00, "http://metalparts.com", metal="Aluminio")

pm2 = PiezaMetalica("M02", 300, 15.00, "http://metalparts.com", "Aluminio")
    
pp1 = PiezaPlastico("P01", 150, 8.20, "http://plasticos.es", 85)
pp2 = PiezaPlastico("P02", 50, 3.50, "http://plasticos.es", 60)

print("--- Agregando Piezas ---")
print("Añadiendo pm1:", producto1.agregarPieza(pm1))
print("Añadiendo pm2:", producto1.agregarPieza(pm2))
print("Añadiendo pp1:", producto1.agregarPieza(pp1)) 
print("Añadiendo pp1 repetida:", producto1.agregarPieza(pp1))

print("\n--- Información del Producto ---")
print(producto1)

print("\n--- Cálculo de Precio y Peso Totales ---")
print(f"Precio Total del Producto: {producto1.precioProducto():.2f} €")
print(f"Peso Total del Producto: {producto1.pesoProducto()} g")

print("\n--- Listado de Piezas ---")
print(producto1.listadoPiezas())