import cv2
import numpy as np

def main():
    print("Tema")

    filename = './Imagenes/jugadoras.jpg'
    #Gray-level input
    src = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    if src is None or src.size == 0:
        print("Error en el nombre o la carpeta de la imagen")
        return -1
    cv2.imshow("Imagen Original", src)

    # .. (INI) Codigo a probar

    #src = cv2.resize(src, (200, 100), cv2.INTER_LINEAR)
    src = cv2.resize(src, (0, 0), fx=0.5, fy=0.5)
    cv2.imshow("Entrada", src)

    print("Suavizado de imagenes monocromáticas")
    
    kernel_size = 5

    dst1 = cv2.blur(src, (kernel_size, kernel_size), cv2.BORDER_DEFAULT)
    cv2.imshow("Blur", dst1)

    dst2 = cv2.medianBlur(src, kernel_size)
    cv2.imshow("Median Blur", dst2)

    dst3 = cv2.GaussianBlur(src, (kernel_size, kernel_size), kernel_size/6.0, cv2.BORDER_DEFAULT)
    cv2.imshow("Gaussian Blur", dst3)
    # .. (FIN) Codigo a probar
    # keep windows open until a key is pressed
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return 0


if __name__ == "__main__":
    main()