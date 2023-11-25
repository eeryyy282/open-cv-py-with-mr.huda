import cv2

def resize_image(image_path, target_width, target_height):
    # Membaca gambar
    imgrgb = cv2.imread(image_path)
    
    # Mendapatkan dimensi gambar asli
    height, width = imgrgb.shape[:2]

    # Mengubah ukuran gambar
    imgrgb_resized = cv2.resize(imgrgb, (target_width, target_height))

    # Menampilkan gambar
    cv2.imshow('Gambar RGB', imgrgb_resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Lokasi gambar
lokasi_gambar = input("Masukkan path gambar = ")

# Memilih ukuran gambar yang diinginkan
ukuran = input("Ukuran yang ingin diubah (A4/F4) = ")
if ukuran == "A4":
    target_width, target_height = 248, 350
    # Mengubah ukuran gambar
    resize_image(lokasi_gambar, target_width, target_height)
elif ukuran == "F4":
    target_width, target_height = 255, 385
    # Mengubah ukuran gambar
    resize_image(lokasi_gambar, target_width, target_height)
else:
    print("Maaf, ukuran yang Anda masukkan salah")

