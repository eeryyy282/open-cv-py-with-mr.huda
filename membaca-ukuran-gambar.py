import cv2 as cv
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()
lokasi_gambar = filedialog.askopenfilename(title="Pilih Gambar", filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])

gambar = cv.imread(lokasi_gambar)

def baca_ukuran_gambar(gambar):
    print("Lebar = ", gambar.shape[1])
    print("Tinggi = ", gambar.shape[0])
    print("Ukuran = ", gambar.shape)

baca_ukuran_gambar(gambar)

cv.waitKey(0)
cv.destroyAllWindows()
