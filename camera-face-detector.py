import cv2 as cv

kamera = cv.VideoCapture(0)
face = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
eye = cv.CascadeClassifier('haarcascade_eye.xml')

while True:
    cond, frame = kamera.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    muka = face.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in muka:
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 5)
        warna_roi = frame[y:y+h, x:x+w]
        gray_roi = gray[y:y+h, x:x+w]
        mata = eye.detectMultiScale(gray_roi)

        for (mx, my, mw, mh) in mata:
            cv.rectangle(warna_roi, (mx, my), (mx+mw, my+mh), (255, 255, 0), 2)

    cv.imshow('Deteksi Wajah dan Mata', frame)
    k = cv.waitKey(1) & 0xff

    if k == ord('q'):
        break

kamera.release()
cv.destroyAllWindows()
