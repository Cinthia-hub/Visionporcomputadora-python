import cv2
import numpy as np

def syImSkin_Mask_Slow(src_bgr: np.ndarray) -> np.ndarray:
    if src_bgr.shape[2] != 3:
        print("La imagen de entrada debe tener 3 canales (BGR).")
        return None
    #Convertir a espacio HLS
    src_hls = cv2.cvtColor(src_bgr, cv2.COLOR_BGR2HLS)
    #Crear una máscara
    ren, col = src_bgr.shape
    mask = np.zeros((ren, col), dtype=np.uint8)

    #Detección de pixeles que son piel
    H = src_hls[:, :, 0]  # Componente Hue
    L = src_hls[:, :, 1]  # Componente Lightness
    S = src_hls[:, :, 2]  # Componente Saturation

    S_seguro = np.where(S!= 0, S, 1) # Evitar división por cero

    LSR = L / S_seguro
    LSR[ S == 0 ] = 1.0  # Si S es 0, asignar LSR a 1.0

def main():
    print("Tema")

    filename = './caption.jpg'
    #Gray-level input
    src = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    if src is None or src.size == 0:
        print("Error en el nombre o la carpeta de la imagen")
        return -1
    cv2.imshow("Imagen Original", src)

    # .. (INI) Codigo a probar

    # .. (FIN) Codigo a probar
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()   