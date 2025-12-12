import cv2

def main():
    print("Video Streaming")

    cam = cv2.VideoCapture(0)  # Capture video from the default camera
    if not cam.isOpened():
        print("No se encontro la fuente de video.")
        return False

    cv2.namedWindow("Video", cv2.WINDOW_NORMAL)
    cv2.namedWindow("Gris", cv2.WINDOW_NORMAL)

    while True:
        success, frame = cam.read()
        if not success:
            break

        cv2.imshow("Video", frame)

        gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow("Gris", gris)
        
        if cv2.waitKey(30) >= 0:  # Exit on any key press
            break

    cv2.destroyAllWindows()
    cam.release()

if __name__ == "__main__":
    main()