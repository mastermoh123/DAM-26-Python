def main():
    print("--- CONTROL DE MOVIMIENTOS BANCARIOS ---")
    print("Introduce los movimientos. Escribe 'fin' en el concepto para terminar.\n")
    
    lista_ingresos = []
    lista_gastos = []
    
    while True:
        concepto = input("Concepto del movimiento (o 'fin' para terminar): ").strip()
        if concepto.lower() == 'fin':
            break
        
        if not concepto:
            print("El concepto no puede estar vacío. Inténtalo de nuevo.")
            continue
            
        try:
            cantidad = float(input(f"Cantidad para '{concepto}' (positivo = ingreso, negativo = gasto): "))
        except ValueError:
            print("Error: Introduce un valor numérico válido para la cantidad.")
            continue
            
        movimiento = (concepto, cantidad)
        
        if cantidad > 0:
            lista_ingresos.append(movimiento)
        elif cantidad < 0:
            lista_gastos.append(movimiento)
        else:
            print("El importe es 0, no se clasifica como ingreso ni como gasto.")
            
        print() # Línea en blanco para separar iteraciones

    total_ingresos = sum(cantidad for _, cantidad in lista_ingresos)
    total_gastos = sum(cantidad for _, cantidad in lista_gastos)

    print("\n" + "="*50)
    print("RESUMEN DE LA CUENTA BANCARIA")
    print("="*50)
    print(f"Lista de Ingresos: {lista_ingresos}")
    print(f"Total de Ingresos: {total_ingresos:.2f} €")
    print("-" * 50)
    print(f"Lista de Gastos: {lista_gastos}")
    print(f"Total de Gastos: {total_gastos:.2f} €")
    print("="*50)

if __name__ == "__main__":
    main()