from importlib.metadata import entry_points
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from backend import *


class WelcomeWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Wallet")
        self.root.geometry('600x500')
        title = tk.Label(root)
        title["justify"] = "center"
        title["text"] = "Password Wallet"
        title["font"] = tkFont.Font(family='Calibri', size=25, weight='bold')
        title.place(x=100, y=5, width=400, height=40)

        info = tk.Label(root)
        info["justify"] = "center"
        info["text"] = "Please log in to see your passwords. If its your first log in, click register"
        info.place(x=100, y=100, width=400, height=50)

        loginButton = tk.Button(root, command=self.log_in, text='Log In', font=(
            "Calibri", 12), bd=3, activeforeground='white', activebackground='gray', justify='center')
        loginButton.place(x=360, y=220, width=70, height=25)

        registerButton = tk.Button(root, command=self.register, text='Register', font=(
            "Calibri", 10), bd=3, activeforeground='white', activebackground='gray', justify='center')
        registerButton.place(x=160, y=220, width=70, height=25)

        if(plogin()):
            registerButton['state'] = 'disabled'

    def register(self):
        print("command")

    def log_in(self):
        self.root.destroy()  # close the current window
        self.app = LoginWindow(self.root)  # create Demo2 window
        self.root.mainloop()


class LoginWindow:

    def __init__(self, root):
        self.root = tk.Tk()
        self.app = (self.root)
        self.root.title("Password Wallet")
        self.root.geometry('600x500')
        title = tk.Label(self.root)
        title["justify"] = "center"
        title["text"] = "Password Wallet"
        title["font"] = tkFont.Font(family='Calibri', size=25, weight='bold')
        title.place(x=100, y=5, width=400, height=40)

        text = tk.Label(self.root)
        text["justify"] = "center"
        text["text"] = "Password:"
        text["font"] = tkFont.Font(family='Calibri', size=10)
        text.place(x=60, y=220, width=80, height=40)

        info = tk.Label(self.root)
        info["justify"] = "center"
        info["text"] = "Please enter your password:"
        info.place(x=110, y=100, width=400, height=50)

        self.name_entry = tk.Entry(self.root,
                                   font=('calibri', 10, 'normal'), show='*')
        self.name_entry.place(x=140, y=220, width=200, height=30)
        commitButton = tk.Button(self.root, command=self.password_process, text='Log In', font=(
            "Calibri", 10), bd=3, activeforeground='white', activebackground='gray', justify='center').place(x=350, y=220, width=70, height=25)

    def password_process(self):
        password = self.name_entry.get()
        if check_password(password):
            window = tk.Toplevel()
            label = tk.Label(window, text="Correct password!")
            label.pack(fill='x', padx=50, pady=5)
            button_close = tk.Button(
                window, text="Close", command=window.destroy)
            button_close.pack(fill='x')
            self.new_window()
        else:
            window = tk.Toplevel()
            label = tk.Label(window, text="Password Incorrect!")
            label.pack(fill='x', padx=50, pady=5)
            button_close = tk.Button(
                window, text="Close", command=window.destroy)
            button_close.pack(fill='x')

    def new_window(self):
        self.root.destroy()  # close the current window
        self.app = AccountWindow(self.root)  # create Demo2 window
        self.root.mainloop()


class AccountWindow:
    def __init__(self, root):
        self.root = tk.Tk()
        self.app = (self.root)
        self.root.title("Password Wallet")
        self.root.geometry('600x500')
        title = tk.Label(self.root)
        title["justify"] = "center"
        title["text"] = "Password Wallet"
        title["font"] = tkFont.Font(family='Calibri', size=25, weight='bold')
        title.place(x=100, y=5, width=400, height=40)
        output = show_passwords()
        for i in range(len(output)):
            for j in range(len(output)[0]):
                print(i)
                if i == 0:
                    entry = tk.Entry(self.root, width=20, bg='LightSteelBlue', fg='Black',
                                     font=('Arial', 16, 'bold'))
                else:
                    entry = tk.Entry(self.root, width=20, fg='blue',
                                     font=('Arial', 16, ''))

                entry.grid(row=i, column=j)
                entry.insert('END', output[i][j])


def main():
    root = tk.Tk()
    app = WelcomeWindow(root)
    root.mainloop()


if __name__ == "__main__":
    main()
