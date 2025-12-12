import cv2
import numpy as np

def main():
    print("Umbralización de imágenes monocromáticas, por Sanchez")

    filename = './caption.jpg'
    #Gray-level input
    src = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    if src is None or src.size == 0:
        print("Error en el nombre o la carpeta de la imagen")
        return -1
    # .. (INI) Codigo a probar
    thresh_type = cv2.THRESH_BINARY
    thresh_value = 200
    ret, dst = cv2.threshold(src, thresh_value, 255, thresh_type)
    cv2.imshow("Umbralizada", dst)

    #thresh_type = cv2.THRESH_BINARY
    thresh_type = cv2.THRESH_OTSU
    thresh_value = np.mean(src)
    ret2, dst2 = cv2.threshold(src, thresh_value, 255, thresh_type)
    print(f"\nEl umbral de Otsu es {ret2}")
    cv2.imshow("Umbralizada Otsu", dst2)
    # .. (FIN) Codigo a probar
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()