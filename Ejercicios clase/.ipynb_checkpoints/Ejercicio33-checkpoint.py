def main():
    print("--- ASIGNACIÓN DE GUARDIAS ---")
    print("Introduce los datos para 5 trabajadores (días de lunes a viernes).\n")
    
    dias_validos = ("lunes", "martes", "miércoles", "jueves", "viernes")
    
    guardias = []
    
    while len(guardias) < 5:
        print(f"\n--- Registro {len(guardias) + 1} de 5 ---")
        nombre = input("Nombre del trabajador: ").strip()
        
        nombres_registrados = [t[0] for t in guardias]
        if nombre in nombres_registrados:
            print("Este trabajador ya está registrado. Inténtalo de nuevo.")
            continue
            
        dia = input("Día de la guardia (lunes a viernes): ").strip().lower()
        
        if dia not in dias_validos:
            print("Día no válido. Debe ser un día laborable de lunes a viernes.")
            continue
            
        dias_ocupados = [t[1] for t in guardias]
        if dia in dias_ocupados:
            print("Este día ya está asignado a otro trabajador. Elige otro.")
            continue
            
        guardias.append((nombre, dia))
        print(f"Asignado correctamente: ({nombre}, {dia})")

    print("\n" + "="*50)
    print("LISTA FINAL DE GUARDIAS")
    print("="*50)
    print(guardias)


if __name__ == "__main__":
    main()