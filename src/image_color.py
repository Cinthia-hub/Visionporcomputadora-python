# Autora : Cinthia Camila Bravo Marmolejo

import cv2
import numpy as np

print("IMÁGENES A COLOR")

Colored = np.zeros((128,256,3), dtype=np.uint8)
Colored[:] = (0, 255, 255) #Amarillo en formato BGR
'''
Colored[:,:,0] = 77 #Canal Azul
Colored[:,:,1] = 44   #Canal Verde
Colored[:,:,2] = 100   #Canal Rojo
'''
cv2.imshow("Imagen Color", Colored)

RandColored = np.random.randint(0,256,(256,256,3), dtype=np.uint8)
cv2.imshow("Imagen Color Aleatoria", RandColored)

plane = np.zeros((256,256,3), dtype=np.uint8)
blue = 100
plane[:,:,0] = blue #Canal Azul
plane[:,:,1] = np.arange(256) #Canal Verde
plane[:,:,2] = np.arange(256) #Canal Rojo
cv2.namedWindow("Plano", cv2.WINDOW_NORMAL)
cv2.imshow("Plano", plane)

cv2.waitKey(0)
cv2.destroyAllWindows()