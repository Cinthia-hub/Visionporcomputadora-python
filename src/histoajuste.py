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

    # Recibe la imagen que vamos a ajustar (normalizar)
    # img_norm = cv2.normalize(src, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
    img_norm = cv2.normalize(src, None, 0, 255, cv2.NORM_MINMAX)
    cv2.imshow("Imagen Ajustada", img_norm)
    syImHisto_Show("Histograma de Ajustada", img_norm)
    
    img_aqua = cv2.normalize(src, None, 200, 255, cv2.NORM_MINMAX)
    cv2.imshow("Marca de agua", img_aqua)
    syImHisto_Show("Histograma de Aqua", img_aqua)
    # .. (FIN) Codigo a probar
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()