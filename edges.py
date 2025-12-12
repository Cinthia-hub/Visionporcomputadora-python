import cv2
import numpy as np

def main():
    print("Kanny Edge Detector")

    filename = './Imagenes/shapes.png'
    #Gray-level input
    src = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    if src is None or src.size == 0:
        print("Error en el nombre o la carpeta de la imagen")
        return -1
    cv2.imshow("Imagen Original", src)

    # .. (INI) Codigo a probar

    blurred = cv2.GaussianBlur(src, (11, 11), 0)
    cv2.imshow("Blurred", blurred)

    edges = cv2.Canny(blurred, 30, 100)
    cv2.imshow("Canny Edges", edges)

    # .. (FIN) Codigo a probar
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()