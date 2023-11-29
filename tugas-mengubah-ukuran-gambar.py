import cv2
from tkinter import filedialog
import tkinter as tk

def ubah_ukuran(lokasiGambar, target_width, target_height):
    # Membaca gambar
    imgrgb = cv2.imread(lokasiGambar)
    
    # Mengubah ukuran ke dimensi gambar asli
    height, width = imgrgb.shape[:2]

    # Memnentukan skala berdasarkan ukuran target dari width dan height
    skala_width = target_width / width
    skala_height = target_height / height

    # Menentukan faktor skala yang lebih kecil agar tidak ada distorsi atau blur pada gambar yang digunakan
    scale_factor = min(skala_width, skala_height)

    # Menghitung ukuran baru berdasarkan skala yang digunakan
    new_width = int(width * scale_factor)
    new_height = int(height * scale_factor)

    # Mengubah ukuran gambar
    imgrgb_resized = cv2.resize(imgrgb, (new_width, new_height))

    # Menampilkan gambar
    cv2.imshow('Gambar RGB', imgrgb_resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Membuat jendela tkinter
root = tk.Tk()
root.withdraw()  # Menyembunyikan jendela utama

# Meminta pengguna memilih lokasi gambar
lokasi_gambar = filedialog.askopenfilename(title="Pilih Gambar", filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])

# Memilih ukuran gambar yang diinginkan
ukuran_valid = False

while not ukuran_valid:
    ukuran = input("Ukuran yang ingin diubah (A4/F4) = ")
    
    if ukuran == "A4":
        target_width, target_height = 248, 350
        ukuran_valid = True
    elif ukuran == "F4":
        target_width, target_height = 255, 385
        ukuran_valid = True
    else:
        print("Maaf, ukuran yang Anda masukkan salah. Hanya menerima ukuran A4 atau F4. Silakan coba lagi.")

# Mengubah ukuran gambar
ubah_ukuran(lokasi_gambar, target_width, target_height)
