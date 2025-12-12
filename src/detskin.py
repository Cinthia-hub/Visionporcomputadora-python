import cv2
import numpy as np

def syImSkin_Pixel(pix_hls):
    h,l,s = pix_hls
    if s == 0:
        ls_ratio = 1.0
    else:
        ls_ratio = float(l) / float(s)
    if(s >= 51 and 0.5 < ls_ratio < 3.0 and (h <= 14 or h >= 165)):
        return True
    return False

def syImSkin_Mask_Slow(src_BGR: np.ndarray) -> np.ndarray:
    if src_BGR.shape[2] != 3:
        print("Error: La imagen de entrada debe tener 3 canales (BGR).")
        return None
    src_hls = cv2.cvtColor(src_BGR, cv2.COLOR_BGR2HLS)
    ren, col, _ = src_BGR.shape
    # Crear una máscara vacía
    mask = np.zeros((ren, col), dtype=np.uint8)
    for i in range(ren):
        for j in range(col):
            if syImSkin_Pixel(src_hls[i, j]):
                mask[i, j] = 255
            else:
                mask[i, j] = 0
    return mask

def main():
    filename = './Imagenes/jugadoras.jpg'
    #Gray-level input
    src = cv2.imread(filename)
    if src is None or src.size == 0:
        print("Error en el nombre o la carpeta de la imagen")
        return -1
    cv2.imshow("Imagen Original", src)

    # .. (INI) Codigo a probar
    mask = syImSkin_Mask_Slow(src)
    if mask is None:
        print("Error al generar la máscara.")
        return False
    cv2.imshow("Máscara de piel", mask)

    dst = cv2.bitwise_and(src, src, mask=mask)
    cv2.imshow("Imagen de piel", dst)
    # .. (FIN) Codigo a probar
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()