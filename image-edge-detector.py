import cv2 as cv
gambar = cv.imread('D:\python\grafika-komputer\eka2.png')
tinggi, lebar = gambar.shape[:2]
gambarBaru = cv.resize(gambar, (lebar//3, tinggi//3), interpolation=cv.INTER_AREA)
edge = cv.Canny(gambarBaru, 70, 70)
cv.imshow('Deteksi Edge', edge)
cv.imshow('Gambar Original', gambarBaru)
cv.waitKey(0)
cv.destroyAllWindows()