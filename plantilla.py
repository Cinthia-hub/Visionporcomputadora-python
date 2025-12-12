import cv2
import numpy as np

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