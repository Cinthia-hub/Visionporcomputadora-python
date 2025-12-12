import cv2
import numpy as np

def main():
    print("Tema")

    filename = './caption.jpg'
    #Color input (BGR) - leer en color porque luego convertimos a gris
    src = cv2.imread(filename)
    if src is None or src.size == 0:
        print("Error en el nombre o la carpeta de la imagen")
        return -1
    cv2.imshow("Imagen Original", src)

    # .. (INI) Codigo a probar
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    cv2.imshow("Niveles de gris", gray)

    colorGray = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)
    cv2.imshow("Color gris", colorGray)

    cv2.line(colorGray,
             (0,0), #Punto de inicio
             (colorGray.shape[1], colorGray.shape[0]), #Punto inicio
             (0,0,255), #Color rojo
             3, #Grosor
             cv2.LINE_8 #Tipo de linea
            )
    
    cv2.circle(colorGray, 
               (colorGray.shape[1]//2, colorGray.shape[0]//2), #Centro
               20, #Radio
               (0,255,255), #Amarillo
               5, #Grosor
               cv2.LINE_8
               )
    
    cv2.namedWindow("Color gris", cv2.WINDOW_NORMAL)
    cv2.imshow("Color gris", colorGray)
    # .. (FIN) Codigo a probar
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()