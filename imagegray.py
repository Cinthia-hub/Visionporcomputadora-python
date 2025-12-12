# Autora : Cinthia Camila Bravo Marmolejo

import cv2
import numpy as np

print("ACCESO A LOS PIXELES")
Gray = np.zeros((128,256), dtype=np.uint8)
# 128, 200, 60
Gray[:] = 230
cv2.imshow("Imagen Gris", Gray)

imChafa = np.zeros((128,256), dtype=np.uint8)
for r in range(imChafa.shape[0]):
    for c in range(imChafa.shape[1]):
        imChafa[r,c] = c
cv2.imshow("Imagen Chafa", imChafa)

imBuena = np.zeros((128,256), dtype=np.uint8)
imBuena[:] = np.arange(256, dtype=np.uint8)
cv2.imshow("Imagen Buena", imBuena)

imNeg = 255 - imBuena
cv2.imshow("Imagen Negativo", imNeg)

cv2.waitKey(0)
cv2.destroyAllWindows()