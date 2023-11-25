#library openCV
import cv2 as cv

imgrgb = cv.imread('eka-ori.jpg')

#transformasi gambar rgp menjadi grayscalse
imggray = cv.imread('eka-grayscale.jpg', cv.IMREAD_GRAYSCALE)

#menampilkangambar
cv.imshow('Gambar RGB', imgrgb)

#menampilkan gambar grayscale
cv.imshow('Gambar Grayscale', imggray)

#menunggu input key
cv.waitKey(0)
