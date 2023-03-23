import tkinter as tk

class LoginWindow:
    def __init__(self, master):
        self.master = master
        master.title("Login")

        self.username_label = tk.Label(master, text="Username:")
        self.username_label.pack()

        self.username_entry = tk.Entry(master)
        self.username_entry.pack()

        self.password_label = tk.Label(master, text="Password:")
        self.password_label.pack()

        self.password_entry = tk.Entry(master, show="*")
        self.password_entry.pack()

        self.login_button = tk.Button(master, text="Login", command=self.login)
        self.login_button.pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # TODO: Add your own authentication logic here
        print("Username: " + username)
        print("Password: " + password)

root = tk.Tk()
login_window = LoginWindow(root)
root.mainloop()