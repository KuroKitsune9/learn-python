import cv2 # type: ignore
import cvlib as cv # type: ignore
from cvlib.object_detection import draw_bbox # type: ignore

# Buka webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Deteksi objek
    bbox, label, conf = cv.detect_common_objects(frame)

    # Gambar kotak dan label
    output = draw_bbox(frame, bbox, label, conf)

    # Tampilkan hasil
    cv2.imshow("Deteksi Objek (cvlib)", output)

    # Tekan 'q' untuk keluar
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
