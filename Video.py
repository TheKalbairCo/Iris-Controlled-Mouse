import cv2

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()

    cv2.imshow('Webcam', img)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()