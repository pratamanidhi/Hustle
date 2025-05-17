import cv2
import numpy as np

# Load the overlay image (with alpha channel if it's PNG)
overlay = cv2.imread('HustleAssets/logo.png', cv2.IMREAD_UNCHANGED)

# Resize overlay if needed
overlay = cv2.resize(overlay, (600, 40))  # Adjust size as needed

# Open webcam
cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Get dimensions
    h, w, _ = overlay.shape
    rows, cols, _ = frame.shape

    # Choose position (top-left corner here)
    x, y = 10, 10

    # Ensure overlay fits in the frame
    if x + w > cols or y + h > rows:
        continue

    # Split overlay into RGB and alpha
    overlay_img = overlay[:, :, :3]
    mask = overlay[:, :, 3:] / 255.0  # Normalize alpha mask

    # Get region of interest on the frame
    roi = frame[y:y+h, x:x+w]

    # Blend the overlay with ROI
    blended = (1.0 - mask) * roi + mask * overlay_img
    frame[y:y+h, x:x+w] = blended.astype(np.uint8)

    # Show the result
    cv2.imshow('Webcam with Overlay', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
