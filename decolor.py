import cv2
import numpy as np

def main():
    print("Tema")

    filename = './caption.jpg'
    #Gray-level input
    src = cv2.imread(filename)
    if src is None or src.size == 0:
        print("Error en el nombre o la carpeta de la imagen")
        return -1
    cv2.imshow("Imagen Original", src)

    # .. (INI) Codigo a probar
    #cv2.split(src, channels := cv2.split(src))
    blue, green, red = cv2.split(src)
    cv2.imshow("Canal Azul", blue)
    cv2.imshow("Canal Verde", green)
    cv2.imshow("Canal Rojo", red)

    Azul=src.copy()
    Azul[:,:,1]=0
    Azul[:,:,2]=0
    cv2.imshow("Imagen Azul", Azul)

    Amarillo=src.copy()
    Amarillo[:,:,0]=0
    cv2.imshow("Imagen Amarilla", Amarillo)
    # .. (FIN) Codigo a probar
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()