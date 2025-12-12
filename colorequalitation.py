import cv2
import numpy as np

def main():
    filename = './caption.jpg'
    #Gray-level input
    src = cv2.imread(filename)
    if src is None or src.size == 0:
        print("Error en el nombre o la carpeta de la imagen")
        return -1
    cv2.imshow("Imagen Original", src)

    # .. (INI) Codigo a probar
    #Es  un macro
    cielab = cv2.cvtColor(src, cv2.COLOR_BGR2LAB)
    # L, a, b 
    #L es el canal de luminancia 
    # a, b son los canales de crominancia  
    channel= cv2.split(cielab)

    equ = cv2.equalizeHist(channel[0])
    cv2.imshow("Canal L", channel[0])
    cv2.imshow("Canal L ecualizado", equ)

    Out = cv2.merge((equ, channel[1], channel[2]))
    #La television usa YUV
    Out = cv2.cvtColor(Out, cv2.COLOR_YCrCb2BGR)
    cv2.imshow("Imagen ecualizada", Out)

    # .. (FIN) Codigo a probar
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()