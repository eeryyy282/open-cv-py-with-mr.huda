import cv2 as cv
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

lokasi_gambar = filedialog.askopenfilename(title="Pilih Gambar", filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])

gambar = cv.imread(lokasi_gambar)

size_y, size_x = gambar.shape[:2]

sizex, sizey = size_x * 2, size_y * 2
ukuran_baru = cv.resize(gambar, (sizex, sizey))

cv.imshow("Foto Asli", gambar)
cv.imshow("Foto Baru", ukuran_baru)

cv.waitKey(0)
cv.destroyAllWindows()
