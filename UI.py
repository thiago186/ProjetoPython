import tkinter as tk
from tkinter import ttk

class LoginWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Login")

        self.username_label = ttk.Label(self.master, text="Username")
        self.username_label.grid(row=0, column=0, padx=5, pady=5)

        self.username_entry = ttk.Entry(self.master)
        self.username_entry.grid(row=0, column=1, padx=5, pady=5)

        self.password_label = ttk.Label(self.master, text="Password")
        self.password_label.grid(row=1, column=0, padx=5, pady=5)

        self.password_entry = ttk.Entry(self.master, show="*")
        self.password_entry.grid(row=1, column=1, padx=5, pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    LoginWindow(root)
    root.mainloop()