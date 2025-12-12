# Autora : Cinthia Camila Bravo Marmolejo

import numpy as np

'''
print("CREACIÓN DE MATRICES")
#Son arreglos (imagenes)

mZ = np.zeros((2,3), dtype = np.float32) #Matriz de ceros
print(mZ)

mO = np.ones((5,5), np.uint8) #Matriz de unos
print(mO)

mE = np.eye(4, dtype = np.float32) #Matriz de identidad
print(mE)

#mR = np.random.randint(0,256,(3,2)).astype(np.uint8) #Matriz con valores aleatorios
mR = np.random.randint(0,256,(3,2), np.uint8)
print(mR)
'''

print("OPERACIONES BÁSICAS CON MATRICES")

A = np.eye(3, 2,dtype = np.float32)
B = np.ones((3,2), dtype = np.float32)  

Add = A + B
print(Add)

C = (A+1) - B
print(C)

#Resta elemento a elemento usando el operador -
Res = A - B
print(Res)

#Multiplicación elemento a elemento usando el operador *
Mul = A * B
print(Mul)

#Multiplicación de matrices usando la función dot
Dot = np.dot(A.T, B)
print(Dot)
# Y con el operador @
Dot2 = A.T @ B
print(Dot2)

#Transpuesta usando C.T 
print(C.T)

#Inversa usando la función inv
D = np.array([[1, 2],
              [3, 4]])

# Inversa
Inv = np.linalg.inv(D)
print("Inversa de D:\n", Inv)

