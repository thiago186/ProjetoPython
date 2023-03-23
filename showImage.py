import tkinter as tk
from PIL import Image, ImageTk

class App:
    def __init__(self, window, window_title, image_path):
        self.window = window
        self.window.title(window_title)

        self.image = Image.open(image_path)
        self.photo = ImageTk.PhotoImage(self.image)
        self.label = tk.Label(window, image = self.photo)
        self.label.pack()

        self.window.mainloop()

App(tk.Tk(), "Tkinter and Image", "image.png")