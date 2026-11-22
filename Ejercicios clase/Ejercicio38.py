contabilidad = {}
    
print("--- Sistema de Contabilidad Empresarial ---")
print("Escribe 'x' como nombre de cuenta para finalizar la entrada de datos.\n")
    
while True:
    cuenta = input("Nombre de cuenta: ").strip()
        
    if cuenta.lower() == 'x':
        break
            
    try:
        importe = float(input(f"Importe del movimiento para '{cuenta}': "))
    except ValueError:
        print("Error: El importe debe ser un número válido. Inténtalo de nuevo.\n")
        continue
            
    if cuenta in contabilidad:
        contabilidad[cuenta] += (importe,)
    else:
        contabilidad[cuenta] = (importe,)
            
    print() 
        
if not contabilidad:
    print("\nNo se han registrado movimientos.")
    break

print("\n" + str(contabilidad))
    
saldos = {cuenta: sum(movimientos) for cuenta, movimientos in contabilidad.items()}
    
cuenta_mayor = max(saldos, key=saldos.get)
cuenta_menor = min(saldos, key=saldos.get)
    
print(f"Cuenta con el saldo mayor: ('{cuenta_mayor}', {int(saldos[cuenta_mayor]) if saldos[cuenta_mayor].is_integer() else saldos[cuenta_mayor]})")
print(f"Cuenta con el saldo menor: ('{cuenta_menor}', {int(saldos[cuenta_menor]) if saldos[cuenta_menor].is_integer() else saldos[cuenta_menor]})")
