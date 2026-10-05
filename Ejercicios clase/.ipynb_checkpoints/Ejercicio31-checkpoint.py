def mostrar_menu():
    print("\n--- MENÚ DE OPCIONES ---")
    print("1. Contar")
    print("2. Modificar")
    print("3. Eliminar")
    print("4. Terminar")


def main():
    palabras = []
    print("Introduce las palabras iniciales para la lista (escribe 'fin' para terminar la introducción):")
    while True:
        palabra = input("Palabra: ").strip()
        if palabra.lower() == 'fin':
            break
        if palabra:
            palabras.append(palabra)

    if not palabras:
        print("La lista está vacía. Empezamos con una lista vacía.")

    while True:
        print(f"\n[Estado actual de la lista]: {palabras}")
        mostrar_menu()
        
        opcion = input("Selecciona una opción (1-4): ").strip()

        if opcion == "1":
            cadena = input("Introduce la cadena que deseas contar: ").strip()
            contador = palabras.count(cadena)
            print(f"La cadena '{cadena}' aparece {contador} veces en la lista.")

        elif opcion == "2":
            cadena_buscar = input("Introduce la cadena a buscar: ").strip()
            cadena_nueva = input("Introduce la nueva cadena de reemplazo: ").strip()
            
            modificaciones = 0
            for i in range(len(palabras)):
                if palabras[i] == cadena_buscar:
                    palabras[i] = cadena_nueva
                    modificaciones += 1
            
            print(f"Se han modificado {modificaciones} apariciones.")

        elif opcion == "3":
            cadena_eliminar = input("Introduce la cadena que deseas eliminar: ").strip()
            
            if cadena_eliminar in palabras:
                while cadena_eliminar in palabras:
                    palabras.remove(cadena_eliminar)
                print(f"Se han eliminado todas las apariciones de '{cadena_eliminar}'.")
            else:
                print(f"La cadena '{cadena_eliminar}' no se encuentra en la lista.")

        elif opcion == "4":
            print("¡Programa finalizado! Lista final:", palabras)
            break
        else:
            print("Opción no válida. Por favor, introduce un número del 1 al 4.")


if __name__ == "__main__":
    main()