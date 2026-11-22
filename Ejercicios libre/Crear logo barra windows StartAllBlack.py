import os
import cv2
import numpy as np

def generar_tira_openshell(ruta_imagen="1f.png", salida="star_force_3_estados.png"):
    if not os.path.exists(ruta_imagen):
        print(f"Error: No se encontró el archivo '{ruta_imagen}' en esta carpeta.")
        return

    # 1. Leer imagen original (manteniendo canales de color)
    img = cv2.imread(ruta_imagen, cv2.IMREAD_UNCHANGED)
    
    # 2. Eliminar el fondo blanco/grisáceo y volverlo transparente
    if img.shape[2] == 3:  # Si no tiene canal Alfa (transparencia), se lo creamos
        b, g, r = cv2.split(img)
        # Crear una máscara: todo lo que sea muy claro (fondo blanco de internet) se vuelve transparente
        gris = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        _, alpha = cv2.threshold(gris, 240, 255, cv2.THRESH_BINARY_INV)
        img = cv2.merge([b, g, r, alpha])

    # 3. Redimensionar el icono a un tamaño óptimo cuadrado (ej. 64x64 píxeles)
    tamano_celda = 64
    icono_limpio = cv2.resize(img, (tamano_celda, tamano_celda), interpolation=cv2.INTER_AREA)

    # 4. Crear el lienzo vertical de 3 estados (Ancho: 64px, Alto: 192px)
    tira_vertical = np.zeros((tamano_celda * 3, tamano_celda, 4), dtype=np.uint8)

    # 5. Clonar el emblema de Star Force en las 3 posiciones (Normal, Hover, Click)
    tira_vertical[0:tamano_celda, 0:tamano_celda] = icono_limpio                # Estado 1: Normal
    tira_vertical[tamano_celda:tamano_celda*2, 0:tamano_celda] = icono_limpio     # Estado 2: Sobre el botón
    tira_vertical[tamano_celda*2:tamano_celda*3, 0:tamano_celda] = icono_limpio   # Estado 3: Presionado

    # 6. Guardar el archivo definitivo
    cv2.imwrite(salida, tira_vertical)
    print(f"¡Éxito! Tu imagen limpia y adaptada se guardó como: {salida}")

if __name__ == "__main__":
    generar_tira_openshell()
    input()
