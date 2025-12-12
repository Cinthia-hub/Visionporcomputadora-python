import cv2
import numpy as np
import matplotlib.pyplot as plt

def main():
    print("Tema")

    filename = './caption.jpg'
    #Gray-level input
    src = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    if src is None or src.size == 0:
        print("Error en el nombre o la carpeta de la imagen")
        return -1

    # .. (INI) Codigo a probar
    # Histograma
    hist = cv2.calcHist([src], [0], None, [256], [0,256])
    hist = hist / np.sum(hist)  # Histogram normalization
    
    #Histograma acumulado
    histCum = np.cumsum(hist)

    fig, axes = plt.subplots(1, 2, figsize=(10, 4))

    axes[0].plot(hist, color='blue')
    axes[0].set_title("Histograma normalizado")
    axes[0].set_xlabel("Intensidad")
    axes[0].set_ylabel("Probabilidad")

    axes[1].plot(histCum, color='red')
    axes[1].set_title("Histograma Acumulado")
    axes[1].set_xlabel("Intensidad")
    axes[1].set_ylabel("Probabilidad")

    plt.tight_layout()
    plt.show()
    # .. (FIN) Codigo a probar
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()