import cv2

#lokasi gambar 
lokasi_gambar = input("Masukkan path gambar = ")
imgrgb = cv2.imread(lokasi_gambar)

#mengatur ukuran gambar
height, width = imgrgb.shape[:2]

#menginput ukuran gambar yang diinginkan
max_height = int(input("Masukkan ukuran yang diinginkan = "))
if height > max_height:
    scale = max_height / height  
    new_width = int(width * scale)
    new_height = int(height * scale)
    imgrgb = cv2.resize(imgrgb, (new_width, new_height))

#grayscale gambar
imggray = cv2.cvtColor(imgrgb, cv2.COLOR_BGR2GRAY)

#menampilkan gambar
cv2.imshow('Gambar RGB', imgrgb)

#menampilkan gambar yang telah di grayscale
cv2.imshow('Gambar Grayscale', imggray)
cv2.waitKey(0)
cv2.destroyAllWindows()
