import cv2
import numpy as np

def syImCanny( src: np.ndarray) -> np.ndarray:
    blurred = cv2.GaussianBlur(src, (7, 7), 0)
    edges = cv2.Canny(blurred, 20, 60)    
    return edges

def main():
    print("Kanny Edge Detector")

    filename = './Imagenes/butterfly.bmp'
    #Gray-level input
    src = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    if src is None or src.size == 0:
        print("Error en el nombre o la carpeta de la imagen")
        return -1
    cv2.imshow("Imagen Original", src)

    # .. (INI) Codigo a probar
    edges = syImCanny(src)
    cv2.imshow("Canny Edges", edges)

    # .. (FIN) Codigo a probar
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()