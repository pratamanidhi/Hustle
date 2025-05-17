import cv2
import threading
import numpy as np

class Camera:
    def __init__(self):
        self.cap = None
        self.running = False
        self.thread = None

    def StartCamera(self):
        if self.running:
            print("Camera is already running.")

            return

        print("Opening camera...")
        self.running = True
        self.thread = threading.Thread(target=self._run_camera)
        self.thread.start()
        return True

    def _run_camera(self):
        imageOverlay = cv2.imread('HustleAssets/logo.png', cv2.IMREAD_UNCHANGED)

        self.cap = cv2.VideoCapture(1)

        if not self.cap.isOpened():
            print("Cannot open camera")
            self.running = False
            return

        ret, frame = self.cap.read()
        if not ret:
            print("Can't read initial frame.")
            self.running = False
            return

        rows, cols, _ = frame.shape
        overlay_width = cols
        aspect_ratio = imageOverlay.shape[0] / imageOverlay.shape[1]
        overlay_height = int(overlay_width * aspect_ratio)
        imageOverlay = cv2.resize(imageOverlay, (overlay_width, overlay_height))
        cv2.namedWindow('Webcam', cv2.WND_PROP_FULLSCREEN)
        cv2.setWindowProperty('Webcam', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

        while self.running:
            ret, frame = self.cap.read()
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break

            height, width, _ = imageOverlay.shape
            rows, cols, _ = frame.shape

            xPos, yPos = 0, 0

            if xPos + width > cols or yPos + height > rows:
                continue

            overlayImages = imageOverlay[:, :, :3]
            mask = imageOverlay[:, :, 3:] / 255.0

            roi = frame[yPos:yPos + height, xPos:xPos + width]
            blended = (1.0 - mask) * roi + mask * overlayImages
            frame[yPos:yPos + height, xPos:xPos + width] = blended.astype(np.uint8)

            cv2.imshow('Webcam', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.StopCamera()

    def StopCamera(self):
        self.running = False
        if self.cap:
            self.cap.release()
        cv2.destroyAllWindows()
        if self.thread and self.thread.is_alive():
            self.thread.join()
        print("Camera stopped.")
        return True

