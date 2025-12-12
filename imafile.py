# Autora : Cinthia Camila Bravo Marmolejo

import sys
import cv2
import numpy as np

print("FILES")

filename = 'caption.jpg'

#Gray = cv2.imread(filename)
Gray = cv2.imread(filename, cv2.IMREAD_COLOR)
#Gray = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
if Gray is None:
    print("Error al leer la imagen")
    sys.exit(-1)
cv2.imshow("Imagen Original", Gray)

imNeg = 255 - Gray
cv2.imshow("Imagen Negativo", imNeg)

cv2.waitKey(0)
cv2.destroyAllWindows()