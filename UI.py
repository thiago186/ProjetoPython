import tkinter as tk
from tkinter import ttk

class Window():
    def __init__(self):
        self.master = tk.Tk()
        self.canvas = tk.Canvas(self.master)
        self.canvas.create_image(0, 0, 'image.png')

if __name__ == '__main':
    app = Window()