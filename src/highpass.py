import cv2
import numpy as np

def main():
    print("Tema")

    filename = './Imagenes/retine.jpg'
    #Gray-level input
    src = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    if src is None or src.size == 0:
        print("Error en el nombre o la carpeta de la imagen")
        return -1
    #cv2.imshow("Imagen a nivel de grises", src)

    # .. (INI) Codigo a probar

    #src = cv2.resize(src, (200, 100), cv2.INTER_LINEAR)
    src = cv2.resize(src, (0, 0), fx=1.5, fy=1.5)
    cv2.imshow("Entrada", src)

    src_f = src.astype(np.float32)

    kernel4 = np.array([[-1, -1, -1],
                        [-1,  9, -1],
                        [-1, -1, -1]], dtype=np.float32)

    kernel5 = np.array([[0, -1, 0],
                        [-1,  5, -1],
                        [0, -1, 0]], dtype=np.float32)

    dst4 = cv2.filter2D(src_f, -1, kernel4, anchor=(-1, -1), delta=0, borderType=cv2.BORDER_DEFAULT)
    #dst4 = cv2.normalize(dst4, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)
    dst4 = cv2.normalize(dst4, None, 0.0, 1.0, cv2.NORM_MINMAX)
    cv2.imshow("HP1", dst4)

    dst5 = cv2.filter2D(src_f, -1, kernel5, anchor=(-1, -1), delta=0, borderType=cv2.BORDER_DEFAULT)
    dst5 = cv2.normalize(dst5, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)
    dst5 = cv2.equalizeHist(dst5)
    cv2.imshow("HP2", dst5)
    # .. (FIN) Codigo a probar
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    return 0


if __name__ == "__main__":
    main()