import cv2
from tkinter import Tk as tk
from tkinter import filedialog
from PIL import Image, ImageTk

def browse_image():
    file_path = filedialog.askopenfilename()
    entry_path.delete(0, 'end')
    entry_path.insert(0, file_path)
    show_image(file_path)

def show_image(file_path):
    imgrgb = cv2.imread(file_path)
    if imgrgb is not None:
        height, width = imgrgb.shape[:2]
        max_height = 400
        if height > max_height:
            scale = max_height / height
            new_width = int(width * scale)
            new_height = int(height * scale)
            imgrgb = cv2.resize(imgrgb, (new_width, new_height))

        img = Image.fromarray(cv2.cvtColor(imgrgb, cv2.COLOR_BGR2RGB))
        img.thumbnail((400, 400))
        img = ImageTk.PhotoImage(img)
        label_image.config(image=img)
        label_image.image = img
    else:
        label_image.config(image=None)

# Membuat jendela GUI sederhana
root = Tk()
root.title("Pilih Gambar")

# Menambahkan elemen-elemen GUI
label_path = tk.Label(root, text="Lokasi Gambar:")
label_path.pack()

entry_path = tk.Entry(root, width=50)
entry_path.pack()

button_browse = tk.Button(root, text="Pilih Gambar", command=browse_image)
button_browse.pack()

label_image = tk.Label(root)
label_image.pack()

# Menunggu hingga gambar dipilih
root.mainloop()

# Mengambil lokasi gambar setelah dipilih
lokasi_gambar = entry_path.get()

# Melanjutkan skrip seperti biasa
imgrgb = cv2.imread(lokasi_gambar)