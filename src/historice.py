import cv2
import numpy as np


def syImHisto_Show(title: str, img: np.ndarray):
    """Muestra el histograma acumulado (CDF) de una imagen en escala de grises."""
    if img is None:
        print(f"{title}: imagen None")
        return
    # Asegurar imagen en gris
    if img.ndim == 3:
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    else:
        img_gray = img

    hist, bins = np.histogram(img_gray.flatten(), 256, [0, 256])
    cdf = hist.cumsum()
    # Normalizar para visualizar
    cdf_normalized = (cdf - cdf.min()) / (cdf.max() - cdf.min() + 1e-9) * 299
    hist_img = np.zeros((300, 256), dtype=np.uint8)
    for x, y in enumerate(cdf_normalized):
        cv2.line(hist_img, (x, 299), (x, 299 - int(y)), 255)
    cv2.imshow(title + " Histograma", hist_img)


def syImSkin_Mask_Slow(src_bgr: np.ndarray) -> np.ndarray:
    """Detección lenta de piel (píxel a píxel) en espacio HLS.

    Criterio usado:
      - s >= 51
      - 0.5 < l/s < 3.0
      - h <= 14 or h >= 165
    """
    if src_bgr is None or src_bgr.ndim != 3 or src_bgr.shape[2] != 3:
        print("La imagen de entrada debe tener 3 canales (BGR).")
        return None

    src_hls = cv2.cvtColor(src_bgr, cv2.COLOR_BGR2HLS)
    ren, col = src_bgr.shape[:2]
    mask = np.zeros((ren, col), dtype=np.uint8)

    for i in range(ren):
        for j in range(col):
            h, l, s = src_hls[i, j]
            if s == 0:
                ls_ratio = 1.0
            else:
                ls_ratio = float(l) / float(s)

            if (s >= 51) and (0.5 < ls_ratio < 3.0) and (h <= 14 or h >= 165):
                mask[i, j] = 255
            else:
                mask[i, j] = 0

    return mask


def main():
    filename = './Imagenes/jugadoras.jpg'
    src = cv2.imread(filename)
    if src is None or src.size == 0:
        print("Error en el nombre o la carpeta de la imagen:", filename)
        return -1

    # Mostrar entrada
    cv2.imshow("Imagen Original", src)

    # Histograma de entrada (gris)
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    syImHisto_Show("Para la Entrada", gray)

    # Ecualización global
    Equ = cv2.equalizeHist(gray)
    cv2.imshow("Para la Salida", Equ)
    syImHisto_Show("Para la Salida", Equ)

    # Ecualización sólo en región enmascarada (threshold simple como ejemplo)
    ret, mask = cv2.threshold(gray, 32, 255, cv2.THRESH_BINARY)
    cv2.imshow("Mask", mask)
    masked_region = cv2.bitwise_and(gray, gray, mask=mask)
    equalized_masked_region = cv2.equalizeHist(masked_region)
    Equ_Masked = gray.copy()
    Equ_Masked[mask != 0] = equalized_masked_region[mask != 0]
    cv2.imshow("Ecualizacion con mascara", Equ_Masked)
    syImHisto_Show("Para la Equ Masked", Equ_Masked)

    # Detección de piel (lenta)
    mask_skin = syImSkin_Mask_Slow(src)
    if mask_skin is None:
        print("Error al generar la máscara de piel.")
    else:
        cv2.imshow("Máscara Piel", mask_skin)
        dst = cv2.bitwise_and(src, src, mask=mask_skin)
        cv2.imshow("Imagen de piel", dst)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()