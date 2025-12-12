import cv2
import numpy as np
import matplotlib.pyplot as plt

def syImHisto_Show(title, src):
    hist = cv2.calcHist([src], [0], None, [256], [0,256])
    hist = hist / np.sum(hist)

    plt.figure()
    plt.title(title)
    plt.xlabel("Nivel de gris")
    plt.ylabel("Probabilidad")
    plt.plot(hist)
    plt.xlim([0, 256])
    plt.show()

def main():
    print("Ajuste de Histograma por Normalización, por Sanchez")

    filename = './caption.jpg'
    #Gray-level input
    src = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    if src is None or src.size == 0:
        print("Error en el nombre o la carpeta de la imagen")
        return -1
    cv2.imshow("Imagen Original", src)

    # .. (INI) Codigo a probar
    syImHisto_Show("Histograma de entrada", src)

    img_equ = cv2.equalizeHist(src, None)
    cv2.imshow("Ecualizada", img_equ)
    syImHisto_Show("Histograma de Equ", img_equ)
    # .. (FIN) Codigo a probar
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()