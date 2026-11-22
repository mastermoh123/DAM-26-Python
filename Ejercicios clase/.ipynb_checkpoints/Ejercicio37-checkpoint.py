contabilidad = {}
    
print("--- GESTIÓN CONTABLE DE LA EMPRESA ---")
print("Introduce los datos. Escribe 'x' en el nombre de la cuenta para finalizar.\n")
    
while True:
    cuenta = input("Nombre de cuenta: ").strip()
        
    if cuenta.lower() == 'x':
        break
            
    try:
        importe = float(input("Importe del movimiento: "))
    except ValueError:
        print("Por favor, introduce un número válido para el importe.\n")
        continue
            
    if cuenta in contabilidad:
        contabilidad[cuenta] += (importe,)
    else:
        contabilidad[cuenta] = (importe,)
            
    print("-" * 40)

if not contabilidad:
    print("\nNo se han registrado movimientos.")

contabilidad_limpia = {}
saldos = {}
    
for cuenta, movimientos in contabilidad.items():
    movs_limpios = tuple(int(m) if m.is_integer() else m for m in movimientos)
    contabilidad_limpia[cuenta] = movs_limpios
    saldos[cuenta] = sum(movs_limpios)

cuenta_mayor = max(saldos, key=saldos.get)
cuenta_menor = min(saldos, key=saldos.get)

print("\n")
print(contabilidad_limpia)
print(f"Cuenta con el saldo mayor: ('{cuenta_mayor}', {saldos[cuenta_mayor]})")
print(f"Cuenta con el saldo menor: ('{cuenta_menor}', {saldos[cuenta_menor]})")