#!/usr/bin/env python3
"""
Combina streaming de cámara con detección de piel (HLS).
Muestra:
 - Video: imagen a color
 - Gris: imagen en escala de grises
 - Máscara: máscara binaria de piel
 - Piel: imagen con sólo las regiones detectadas como piel

Salir presionando 'q' o ESC.
"""
import cv2
import numpy as np

def syImSkin_Pixel(pix_hls):
    """Función original por píxel (se mantiene por compatibilidad)."""
    h, l, s = pix_hls
    if s == 0:
        ls_ratio = 1.0
    else:
        ls_ratio = float(l) / float(s)
    if (s >= 51 and 0.5 < ls_ratio < 3.0 and (h <= 14 or h >= 165)):
        return True
    return False

def syImSkin_Mask_Fast(src_BGR: np.ndarray) -> np.ndarray:
    """
    Versión vectorizada de la máscara de piel usando espacio HLS.
    Devuelve una máscara uint8 con valores 0 o 255.
    """
    if src_BGR is None:
        return None
    if src_BGR.ndim != 3 or src_BGR.shape[2] != 3:
        print("Error: La imagen de entrada debe tener 3 canales (BGR).")
        return None

    # Convertir a HLS
    src_hls = cv2.cvtColor(src_BGR, cv2.COLOR_BGR2HLS)
    h, l, s = cv2.split(src_hls)  # cada canal es uint8

    # Convertir a float para la división (evitar división por cero)
    # Añadimos un epsilon pequeño para las divisiones seguras
    eps = 1e-6
    l_f = l.astype(np.float32)
    s_f = s.astype(np.float32) + eps
    ls_ratio = l_f / s_f

    # Condiciones vectorizadas (igual lógica que la función por píxel)
    cond_s = s >= 51
    cond_ratio = (ls_ratio > 0.5) & (ls_ratio < 3.0)
    cond_h = (h <= 14) | (h >= 165)

    mask_bool = cond_s & cond_ratio & cond_h
    mask = (mask_bool.astype(np.uint8)) * 255
    return mask

def main(camera_index=0):
    print("Iniciando Video Streaming con detección de piel. Presiona 'q' o ESC para salir.")

    cam = cv2.VideoCapture(camera_index)
    if not cam.isOpened():
        print("No se encontró la fuente de video.")
        return False

    cv2.namedWindow("Video", cv2.WINDOW_NORMAL)
    cv2.namedWindow("Gris", cv2.WINDOW_NORMAL)
    cv2.namedWindow("Máscara de piel", cv2.WINDOW_NORMAL)
    cv2.namedWindow("Imagen de piel", cv2.WINDOW_NORMAL)

    while True:
        success, frame = cam.read()
        if not success or frame is None:
            print("No se pudo leer un frame (stream terminado?).")
            break

        # Mostrar video a color
        cv2.imshow("Video", frame)

        # Imagen en gris
        gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Gris", gris)

        # Máscara de piel (rápida, vectorizada)
        mask = syImSkin_Mask_Fast(frame)
        if mask is None:
            print("Error al generar la máscara.")
            break
        cv2.imshow("Máscara de piel", mask)

        # Imagen resultante con sólo las regiones de piel
        dst = cv2.bitwise_and(frame, frame, mask=mask)
        cv2.imshow("Imagen de piel", dst)

        # Esperar tecla corta; salir si 'q' o ESC
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q') or key == 27:
            break

    cam.release()
    cv2.destroyAllWindows()
    print("Streaming finalizado.")
    return True

if __name__ == "__main__":
    main()