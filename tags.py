from importlib.metadata import entry_points
import tkinter as tk
from tkinter import CENTER, ttk
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
        self.table = ttk.Treeview(self.root)
        self.table['columns'] = ('id', 'nazwa', 'email', 'haslo')
        self.table.column("#0", width=0, anchor=CENTER)
        self.table.column("id", width=10, anchor=CENTER)
        self.table.column("nazwa", width=80, anchor=CENTER)
        self.table.column("email", width=140, anchor=CENTER)
        self.table.column("haslo", width=80, anchor=CENTER)
        self.table.heading("#0", text="", anchor=CENTER)
        self.table.heading("id", text="Id", anchor=CENTER)
        self.table.heading("nazwa", text="Nazwa", anchor=CENTER)
        self.table.heading("email", text="E-mail", anchor=CENTER)
        self.table.heading("haslo", text="Haslo", anchor=CENTER)
        i = 0
        for row in output:
            self.table.insert(parent='', index='end', iid=i, text='',
                              values=(row[0], row[1], row[2], row[3]))
            i += 1
        self.table.pack()
        self.table.place(x=50, y=100, width=400, height=300)
        addButton = tk.Button(self.root, command=self.add, text='Add Password', font=(
            "Calibri", 10), bd=3, activeforeground='white', activebackground='gray', justify='center').place(x=485, y=105, width=110, height=40)
        editButton = tk.Button(self.root, command=self.edit, text='Edit Password', font=(
            "Calibri", 10), bd=3, activeforeground='white', activebackground='gray', justify='center').place(x=485, y=155, width=110, height=40)
        deleteButton = tk.Button(self.root, command=self.delete, text='Delete Password', font=(
            "Calibri", 10), bd=3, activeforeground='white', activebackground='gray', justify='center').place(x=485, y=205, width=110, height=40)
        generateButton = tk.Button(self.root, command=self.generate, text='Generate Password', font=(
            "Calibri", 10), bd=3, activeforeground='white', activebackground='gray', justify='center').place(x=485, y=255, width=110, height=40)

    def add(self):
        self.win = tk.Toplevel(self.root)
        self.win.title("Add New Password")
        self.win.geometry('400x300')
        name = tk.Label(self.win)
        name["justify"] = "center"
        name["text"] = "name"
        name.place(x=20, y=20, width=100, height=20)

        email = tk.Label(self.win)
        email["justify"] = "center"
        email["text"] = "e-mail"
        email.place(x=20, y=70, width=100, height=20)

        password = tk.Label(self.win)
        password["justify"] = "center"
        password["text"] = "password"
        password.place(x=20, y=120, width=100, height=20)
        self.name_entry = tk.Entry(self.win,
                                   font=('calibri', 10, 'normal'))
        self.name_entry.place(x=130, y=20, width=200, height=20)

        self.email_entry = tk.Entry(self.win,
                                    font=('calibri', 10, 'normal'))
        self.email_entry.place(x=130, y=70, width=200, height=20)

        self.password_entry = tk.Entry(self.win,
                                       font=('calibri', 10, 'normal'), show='*')
        self.password_entry.place(x=130, y=120, width=200, height=20)

        commitButton = tk.Button(self.win, command=self.commit, text='Add', font=(
            "Calibri", 10), bd=3, activeforeground='white', activebackground='gray', justify='center').place(x=280, y=160, width=70, height=25)

    def commit(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        if add_password(name, email, password):
            self.win.destroy()
            window = tk.Toplevel()
            label = tk.Label(window, text="Password successfully added.")
            label.pack(fill='x', padx=50, pady=5)
            button_close = tk.Button(
                window, text="Close", command=window.destroy)
            button_close.pack(fill='x')
            self.root.destroy()
            self.__init__(self.root)
        else:
            window = tk.Toplevel()
            label = tk.Label(window, text="Incorrect data!")
            label.pack(fill='x', padx=50, pady=5)
            button_close = tk.Button(
                window, text="Close", command=window.destroy)
            button_close.pack(fill='x')

    def edit(self):
        choice = self.table.focus()
        if(len(choice) != 0):
            param = self.table.item(choice)
            self.win = tk.Toplevel(self.root)
            self.win.title("Edit Password")
            self.win.geometry('400x300')
            name = tk.Label(self.win)
            name["justify"] = "center"
            name["text"] = "name"
            name.place(x=20, y=20, width=100, height=20)

            email = tk.Label(self.win)
            email["justify"] = "center"
            email["text"] = "e-mail"
            email.place(x=20, y=70, width=100, height=20)

            password = tk.Label(self.win)
            password["justify"] = "center"
            password["text"] = "password"
            password.place(x=20, y=120, width=100, height=20)
            self.name_entry = tk.Entry(self.win,
                                       font=('calibri', 10, 'normal'))
            self.name_entry.insert(0, param['values'][1])
            self.name_entry.place(x=130, y=20, width=200, height=20)

            self.email_entry = tk.Entry(self.win,
                                        font=('calibri', 10, 'normal'))
            self.email_entry.place(x=130, y=70, width=200, height=20)
            self.email_entry.insert(0, param['values'][2])
            self.password_entry = tk.Entry(self.win,
                                           font=('calibri', 10, 'normal'), text=param['values'][3])
            self.password_entry.place(x=130, y=120, width=200, height=20)
            self.password_entry.insert(0, param['values'][3])
            commitButton = tk.Button(self.win, command=self.editPassword, text='Edit', font=(
                "Calibri", 10), bd=3, activeforeground='white', activebackground='gray', justify='center').place(x=280, y=160, width=70, height=25)

    def editPassword(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        id = self.table.item(self.table.focus()[0])
        print(id)
        if edit_password(name, email, password, id):
            self.win.destroy()
            window = tk.Toplevel()
            label = tk.Label(window, text="Password successfully edited.")
            label.pack(fill='x', padx=50, pady=5)
            button_close = tk.Button(
                window, text="Close", command=window.destroy)
            button_close.pack(fill='x')
            self.root.destroy()
            self.__init__(self.root)
        else:
            window = tk.Toplevel()
            label = tk.Label(window, text="Incorrect data!")
            label.pack(fill='x', padx=50, pady=5)
            button_close = tk.Button(
                window, text="Close", command=window.destroy)
            button_close.pack(fill='x')

    def delete(self):
        window = tk.Toplevel()
        window.geometry('300x300')
        label = tk.Label(
            window, text="Press Delete if you want to delete your password")
        label.place(x=10, y=20, width=300, height=50)
        button_close = tk.Button(
            window, text="Back", command=window.destroy)
        button_close.place(x=80, y=120, width=50, height=30)
        button_delete = tk.Button(
            window, text="Delete", command=self.deleteConfirmed)
        button_delete.place(x=160, y=120, width=50, height=30)

    def deleteConfirmed(self):
        id = str(self.table.item(self.table.focus())['values'][0])
        if delete_password(id):
            window = tk.Toplevel()
            label = tk.Label(window, text="Password successfully deleted.")
            label.pack(fill='x', padx=50, pady=5)
            button_close = tk.Button(
                window, text="Close", command=window.destroy)
            button_close.pack(fill='x')
            self.root.destroy()
            self.__init__(self.root)

    def generate(self):
        # num_of_special, length, num_of_capital, num_of_numbers#
        self.win = tk.Toplevel(self.root)
        self.win.title("Generate Password")
        self.win.geometry('400x350')
        length = tk.Label(self.win)
        length["justify"] = "center"
        length["text"] = "Length of password"
        length.place(x=40, y=20, width=150, height=20)

        special = tk.Label(self.win)
        special["justify"] = "center"
        special["text"] = "Num of special characters"
        special.place(x=40, y=70, width=150, height=20)

        capital = tk.Label(self.win)
        capital["justify"] = "center"
        capital["text"] = "Num of capital characters"
        capital.place(x=40, y=120, width=150, height=20)

        numbers = tk.Label(self.win)
        numbers["justify"] = "center"
        numbers["text"] = "Num of numbers"
        numbers.place(x=40, y=170, width=150, height=20)

        self.generator = tk.Label(self.win)
        self.generator["justify"] = "center"
        self.generator["text"] = "Length of password"
        self.generator.place(x=50, y=250, width=300, height=20)

        self.length_entry = tk.Entry(self.win,
                                     font=('calibri', 10, 'normal'))
        self.length_entry.place(x=230, y=20, width=30, height=20)

        self.special_entry = tk.Entry(self.win,
                                      font=('calibri', 10, 'normal'))
        self.special_entry.place(x=230, y=70, width=30, height=20)

        self.capital_entry = tk.Entry(self.win,
                                      font=('calibri', 10, 'normal'))
        self.capital_entry.place(x=230, y=120, width=30, height=20)

        self.numbers_entry = tk.Entry(self.win,
                                      font=('calibri', 10, 'normal'))
        self.numbers_entry.place(x=230, y=170, width=30, height=20)

        generateButton = tk.Button(self.win, command=self.generateProcessed, text='Generate', font=(
            "Calibri", 10), bd=3, activeforeground='white', activebackground='gray', justify='center').place(x=280, y=290, width=70, height=25)

        BackButton = tk.Button(self.win, command=self.win.destroy, text='Back', font=(
            "Calibri", 10), bd=3, activeforeground='white', activebackground='gray', justify='center').place(x=180, y=290, width=70, height=25)

    def generateProcessed(self):
        length = self.length_entry.get()
        special = self.special_entry.get()
        capital = self.capital_entry.get()
        numbers = self.numbers_entry.get()
        test, password = generate_password(length, special, capital, numbers)
        if test:
            self.root.clipboard_append(password)
            self.generator['text'] = password
            window = tk.Toplevel()
            label = tk.Label(
                window, text="Password generated. Copied to clipboard")
            label.pack(fill='x', padx=50, pady=5)
            button_close = tk.Button(
                window, text="Close", command=window.destroy)
            button_close.pack(fill='x')
        else:
            window = tk.Toplevel()
            label = tk.Label(window, text="Incorrect data!")
            label.pack(fill='x', padx=50, pady=5)
            button_close = tk.Button(
                window, text="Close", command=window.destroy)
            button_close.pack(fill='x')


def main():
    root = tk.Tk()
    app = WelcomeWindow(root)
    root.mainloop()


if __name__ == "__main__":
    main()
