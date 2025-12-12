# Autora : Cinthia Camila Bravo Marmolejo

import cv2
import numpy as np

print("CREACIÓN DE IMÁGENES USANDO NUMPY")
im0 = np.zeros((128,256), dtype=np.uint8)
cv2.imshow("Imagen de Ceros", im0)

im1 = np.ones((256,256), dtype=np.uint8)
cv2.imshow("Imagen de Unos", im1*255)

imE = np.eye(256, dtype=np.uint8)
imE *= 255
cv2.imshow("Imagen de Identidad", imE)

imSub = im1*255 - imE
cv2.imshow("Resta", imSub)

cv2.waitKey(0)
cv2.destroyAllWindows()