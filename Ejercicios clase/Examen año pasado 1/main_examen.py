from gestor_examen import (
    cargar_reservas_desde_csv,
    consultar_reservas_fecha,
    escribir_csv,
    escribir_txt,
    insertar_reservas_bbdd,
    ordenar_tabla,
)


def mostrar_reservas_fecha(fecha):
    filas = consultar_reservas_fecha(fecha)
    print(f"\nRESERVAS PARA {fecha}:")
    if not filas:
        print("No hay reservas para esta fecha.")
        print("Total: 0 reservas, 0 personas")
        return

    total_personas = 0
    for nombre_cliente, telefono, num_personas, num_mesa in filas:
        total_personas += int(num_personas)
        print(f"Mesa {num_mesa}: {nombre_cliente} ({num_personas} personas) - Tel: {telefono}")

    print(f"Total: {len(filas)} reservas, {total_personas} personas")


def main():
    # 1. Cargar reservas desde CSV y mostrarlas
    reservas = cargar_reservas_desde_csv("reservas.csv")
    print("=== RESERVAS CARGADAS DESDE CSV ===")
    for id_res, datos in reservas.items():
        print(f"{id_res}: {datos}")

    # 2. Insertar en MySQL ('examen' -> tabla 'reserva')
    insertar_reservas_bbdd(reservas)
    print("\nReservas insertadas en 'examen.reserva'.")

    # 3. Consultar y mostrar reservas para las fechas solicitadas
    mostrar_reservas_fecha("2025-03-15")
    mostrar_reservas_fecha("2025-11-14")

    # 4. Ejemplo extra: convertir reservas a tabla 2D, ordenar con lambda y exportar a .txt y .csv
    tabla_2d = [
        [id_res, d["nombre"], d["telefono"], d["fecha"], d["personas"], d["mesa"]]
        for id_res, d in reservas.items()
    ]
    ordenada_por_personas = ordenar_tabla(tabla_2d, lambda fila: int(fila[4]), descendente=True)
    escribir_txt(ordenada_por_personas, "reservas_ordenadas.txt", sep=";")
    escribir_csv(
        ordenada_por_personas,
        "reservas_ordenadas.csv",
        cabecera=["id", "nombre", "telefono", "fecha", "personas", "mesa"],
        sep=",",
    )


if __name__ == "__main__":
    main()