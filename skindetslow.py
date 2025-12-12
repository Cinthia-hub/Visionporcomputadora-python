import cv2
import numpy as np

def syImSkin_Pixel(pix_hls):
    h,l,s = pix_hls
    ls_ratio = 0
    if s == 0:
        ls_ratio = 1.0
    else:
        ls_ratio = float(l) / float(s)
    return (s >= 51 and 0.5 < ls_ratio < 3.0 and (h <= 14 or h >= 165))

def syImSkin_Mask_Slow(src_bgr: np.ndarray) -> np.ndarray:
    if src_bgr.shape[2] != 3:
        print("La imagen de entrada debe tener 3 canales (BGR).")
        return None
    #Convertir a espacio HLS
    src_hls = cv2.cvtColor(src_bgr, cv2.COLOR_BGR2HLS)
    #Crear una máscara
    ren, col, _ = src_bgr.shape
    mask = np.zeros((ren, col), dtype=np.uint8)
    #Detección de pixeles que son piel
    #return mask
    for r in range(ren):
        for c in range(col):
            if syImSkin_Pixel(src_hls[r,c]):
                mask[r,c] = 255
    return mask

def main():
    print("Skin Detection Slow")

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
    cv2.imshow("Máscara Detectora de Piel", mask)
    # .. (FIN) Codigo a probar
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()   