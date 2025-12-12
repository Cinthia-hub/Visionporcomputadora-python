import cv2

# --- Cargar la imagen ---
# Cambia "imagen.jpg" por el nombre de tu archivo en la misma carpeta
imagen = cv2.imread("./caption.jpg")

if imagen is None:
    print("No se pudo cargar la imagen, revisa la ruta.")
    exit()

# --- Mostrar la imagen original ---
cv2.imshow("Original", imagen)

# --- Convertir a escala de grises ---
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
cv2.imshow("Escala de grises", gris)

# --- Aplicar un desenfoque (GaussianBlur) ---
desenfoque = cv2.GaussianBlur(gris, (5, 5), 0)
cv2.imshow("Desenfoque", desenfoque)

# --- Detectar bordes con Canny ---
bordes = cv2.Canny(desenfoque, 50, 150)
cv2.imshow("Bordes Canny", bordes)

# --- Detección de contornos ---
contornos, _ = cv2.findContours(bordes, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
imagen_contornos = imagen.copy()
cv2.drawContours(imagen_contornos, contornos, -1, (0, 255, 0), 2)
cv2.imshow("Contornos", imagen_contornos)

# --- Esperar a que se presione una tecla y luego cerrar ---
cv2.waitKey(0)
cv2.destroyAllWindows()
import cv2

# --- Cargar la imagen ---
# Cambia "imagen.jpg" por el nombre de tu archivo en la misma carpeta
imagen = cv2.imread("piel-de-carnero.png")

if imagen is None:
    print("No se pudo cargar la imagen, revisa la ruta.")
    exit()

# --- Mostrar la imagen original ---
cv2.imshow("Original", imagen)

# --- Convertir a escala de grises ---
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
cv2.imshow("Escala de grises", gris)

# --- Aplicar un desenfoque (GaussianBlur) ---
desenfoque = cv2.GaussianBlur(gris, (5, 5), 0)
cv2.imshow("Desenfoque", desenfoque)

# --- Detectar bordes con Canny ---
bordes = cv2.Canny(desenfoque, 50, 150)
cv2.imshow("Bordes Canny", bordes)

# --- Detección de contornos ---
contornos, _ = cv2.findContours(bordes, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
imagen_contornos = imagen.copy()
cv2.drawContours(imagen_contornos, contornos, -1, (0, 255, 0), 2)
cv2.imshow("Contornos", imagen_contornos)

# --- Esperar a que se presione una tecla y luego cerrar ---
cv2.waitKey(0)
cv2.destroyAllWindows()
