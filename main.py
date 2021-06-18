import cv2

cap = cv2.VideoCapture('video.mp4')

while True:
    ret, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # ----------------Grayscale Video--------------
    cv2.imshow('Grayscale', gray)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()