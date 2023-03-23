import tkinter as tk
from tkinter import ttk

class LoginWindow:
    def __init__(self, master):
        self.username, self.password = '', ''
        self.master = master
        self.master.title("Janela Inicial do Projeto Python")

        self.username_label = ttk.Label(self.master, text="Usuário:")
        self.username_label.grid(row=0, column=0)

        self.username_entry = ttk.Entry(self.master)
        self.username_entry.grid(row=0, column=1)

        self.password_label = ttk.Label(self.master, text="Senha:")
        self.password_label.grid(row=1, column=0)

        self.password_entry = ttk.Entry(self.master, show="*")
        self.password_entry.grid(row=1, column=1)

        self.login_button = ttk.Button(master, text = "Fazer Login", command = self.login)
        self.login_button.grid(row=2, column=1)

        self.login_status_label = ttk.Label(self.master, text = '')
        self.login_status_label.grid(row=3, column=0)

    def login(self):
        self.username = self.username_entry.get()
        self.password = self.password_entry.get()
        self.login_status = self.auth()
        self.login_status_label.config(text=self.login_status)

    def auth(self):
        from passwords import logins
        if (self.username, self.password) in logins:
            return 'Usuário Autorizado'
        else:
            return 'Usuário não autorizado! Tente novamente ou Registre o Usuário'

if __name__ == "__main__":
    root = tk.Tk()
    LoginWindow(root)
    root.mainloop()