import cv2

# Buka webcam
cam = cv2.VideoCapture(0)
ret, frame1 = cam.read()
ret, frame2 = cam.read()

while cam.isOpened():
    # Hitung selisih antara dua frame
    diff = cv2.absdiff(frame1, frame2)
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh, None, iterations=3)
    
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:
        if cv2.contourArea(c) < 500:
            continue
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Gerakan Terdeteksi", frame1)

    # Update frame
    frame1 = frame2
    ret, frame2 = cam.read()

    # Tekan 'q' untuk keluar
    if cv2.waitKey(10) == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
