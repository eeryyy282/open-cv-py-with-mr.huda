import cv2 as cv
gambar = cv.imread('D:\python\grafika-komputer\eka2.png')
tinggi, lebar = gambar.shape[:2]
gambarBaru = cv.resize(gambar, (lebar//3, tinggi//3), interpolation=cv.INTER_AREA)
eye = cv.CascadeClassifier('haarcascade_eye.xml')
face = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
gray = cv.cvtColor(gambarBaru, cv.COLOR_BGR2GRAY)
muka = face.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in muka:
    cv.rectangle(gambarBaru, (x,y), (x+w, y+h), (0,255,0),2)
    warna_roi = gambarBaru[y:y+h, x:x+2]
    gray_roi = gray[y:y+h, x:x+w]
    mata = eye.detectMultiScale(gray_roi, 1.5,3)
    for (mx, my, mw, mh) in mata:
        cv.rectangle(warna_roi, (my, mx), (mx+mw, my+mh), (255,255,0),1)
cv.imshow('Foto Normal', gambarBaru)
cv.waitKey(0)
cv.destroyAllWindows()