from importlib.metadata import entry_points
import tkinter as tk
from tkinter import CENTER, ttk
import tkinter.font as tkFont
from backend import *
import customtkinter

# Modes: system (default), light, dark
customtkinter.set_appearance_mode("dark")
# Themes: blue (default), dark-blue, green
customtkinter.set_default_color_theme("dark-blue")


class WelcomeWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Wallet")
        self.root.geometry('600x500')
        frame = customtkinter.CTkFrame(master=root,
                                       width=500,
                                       height=450,
                                       corner_radius=10)
        frame.pack(padx=20, pady=20)
        title = customtkinter.CTkLabel(
            master=frame, width=120, height=25, corner_radius=8, justify='center', text="Password Wallet")
        title.place(relx=0.5, rely=0.2, anchor=CENTER)

        info = customtkinter.CTkLabel(
            master=frame,
            width=400,
            height=40,
            corner_radius=8,
            justify='center',
            text="Please log in to see your passwords. \n If its your first log in, click register")
        info.place(relx=0.5, rely=0.5, anchor=CENTER)

        loginButton = customtkinter.CTkButton(
            master=frame,
            width=120,
            height=32,
            border_width=0,
            corner_radius=8,
            command=self.log_in,
            text='Log In')
        loginButton.place(relx=0.65, rely=0.7, anchor=CENTER)

        registerButton = customtkinter.CTkButton(master=frame,
                                                 width=120,
                                                 height=32,
                                                 border_width=0,
                                                 corner_radius=8,
                                                 command=self.register,
                                                 text='Register')
        registerButton.place(relx=0.35, rely=0.7, anchor=CENTER)

        if(plogin()):
            registerButton.configure(state=tk.DISABLED)
        else:
            loginButton.configure(state=tk.DISABLED)

    def register(self):
        self.win = customtkinter.CTkToplevel(self.root)
        self.win.title("Register")
        self.win.geometry('400x300')
        frame = customtkinter.CTkFrame(master=self.win,
                                       width=500,
                                       height=450,
                                       corner_radius=10)
        frame.pack(padx=20, pady=20)
        name = customtkinter.CTkLabel(
            frame,
            justify="center",
            text="Password:")
        name.place(relx=0.2, rely=0.5, anchor=CENTER)
        self.password_entry = customtkinter.CTkEntry(master=frame,
                                                     show='*')
        self.password_entry.place(relx=0.5, rely=0.5, anchor=CENTER)

        commitButton = customtkinter.CTkButton(
            master=frame,
            command=self.registerProcessed,
            width=120,
            height=32,
            border_width=0,
            corner_radius=8,
            text='Add')
        commitButton.place(relx=0.8, rely=0.8, anchor=CENTER)

    def registerProcessed(self):
        password = self.password_entry.get()
        if first_login(password):
            self.win.destroy()
            self.root.destroy()
            self.app = LoginWindow(self.root)
            self.root.mainloop()

        else:
            window = customtkinter.CTkToplevel()
            label = customtkinter.CTkLabel(window, text="Incorrect data!")
            label.pack(fill='x', padx=50, pady=5)
            button_close = customtkinter.CTkButton(
                window, text="Close", command=window.destroy)
            button_close.pack(fill='x')

    def log_in(self):
        self.root.withdraw()
        toplevel = customtkinter.CTkToplevel(self.root)
        toplevel.geometry("350x350")
        app = LoginWindow(toplevel)


class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Wallet")
        self.root.geometry('600x500')
        frame = customtkinter.CTkFrame(master=self.root,
                                       width=500,
                                       height=450,
                                       corner_radius=10)
        frame.pack(padx=20, pady=20)

        text = customtkinter.CTkLabel(master=frame,
                                      justify="center",
                                      width=140,
                                      height=25,
                                      corner_radius=8,
                                      text="Password:")
        text.place(relx=0.2, rely=0.5, anchor=CENTER)

        info = customtkinter.CTkLabel(master=frame,
                                      justify="center",
                                      width=120,
                                      height=25,
                                      corner_radius=8,
                                      text="Please enter your password:")
        info.place(relx=0.5, rely=0.2, anchor=CENTER)

        self.name_entry = customtkinter.CTkEntry(master=frame,
                                                 show='*')
        self.name_entry.place(relx=0.5, rely=0.5, anchor=CENTER)

        commitButton = customtkinter.CTkButton(master=frame,
                                               command=self.password_process,
                                               width=120,
                                               height=32,
                                               border_width=0,
                                               corner_radius=8,
                                               text='Log In')
        commitButton.place(relx=0.8, rely=0.8, anchor=CENTER)

    def password_process(self):
        password = self.name_entry.get()
        if check_password(password):
            self.window = customtkinter.CTkToplevel()
            label = customtkinter.CTkLabel(
                self.window, text="Correct password!")
            label.pack(fill='x', padx=50, pady=5)
            button_close = customtkinter.CTkButton(
                self.window, text="Close", command=self.new_window)
            button_close.pack(fill='x')
        else:
            window = customtkinter.CTkToplevel()
            label = customtkinter.CTkLabel(window, text="Password Incorrect!")
            label.pack(fill='x', padx=50, pady=5)
            button_close = customtkinter.CTkButton(
                window, text="Close", command=window.destroy)
            button_close.pack(fill='x')

    def new_window(self):
        self.window.destroy()
        self.root.withdraw()
        toplevel = customtkinter.CTkToplevel(self.root)
        app = AccountWindow(toplevel)


class AccountWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Wallet")
        self.root.geometry('700x600')
        self.frame = customtkinter.CTkFrame(master=self.root,
                                            width=500,
                                            height=450,
                                            corner_radius=10)
        self.frame.pack(padx=20, pady=20)
        title = customtkinter.CTkLabel(master=self.frame,
                                       justify="center",
                                       width=140,
                                       height=25,
                                       corner_radius=8,
                                       text="Password Wallet"
                                       )
        title.place(x=100, y=5, width=400, height=40)
        output = show_passwords()
        style = ttk.Style(root)
        style.theme_use("clam")
        style.configure("Treeview", background="#373a45",
                        fieldbackground="#373a45", foreground="#373a45")

        self.table = ttk.Treeview(self.frame)
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
        self.table.place(relx=0.35, rely=0.5, anchor=CENTER)
        addButton = customtkinter.CTkButton(master=self.frame,
                                            command=self.add,
                                            text='Add Password',
                                            width=120,
                                            height=32,
                                            border_width=0,
                                            corner_radius=8)
        addButton.place(relx=0.8, rely=0.2, anchor=CENTER)

        editButton = customtkinter.CTkButton(master=self.frame,
                                             command=self.edit,
                                             text='Edit Password',
                                             width=120,
                                             height=32,
                                             border_width=0,
                                             corner_radius=8)
        editButton.place(relx=0.8, rely=0.35, anchor=CENTER)

        deleteButton = customtkinter.CTkButton(master=self.frame,
                                               command=self.delete,
                                               text='Delete Password',
                                               width=120,
                                               height=32,
                                               border_width=0,
                                               corner_radius=8)
        deleteButton.place(relx=0.8, rely=0.5, anchor=CENTER)

        generateButton = customtkinter.CTkButton(master=self.frame,
                                                 command=self.generate,
                                                 text='Generate Password',
                                                 width=120,
                                                 height=32,
                                                 border_width=0,
                                                 corner_radius=8)
        generateButton.place(relx=0.8, rely=0.65, anchor=CENTER)

        exitButton = customtkinter.CTkButton(master=self.frame,
                                             command=self.root.quit,
                                             text='Exit',
                                             width=120,
                                             height=32,
                                             border_width=0,
                                             corner_radius=8)
        exitButton.place(relx=0.8, rely=0.9, anchor=CENTER)

    def add(self):
        self.win = customtkinter.CTkToplevel(master=self.root)
        self.win.title("Register")
        self.win.geometry('400x300')
        frame = customtkinter.CTkFrame(master=self.win,
                                       width=500,
                                       height=450,
                                       corner_radius=10)
        frame.pack(padx=20, pady=20)

        name = customtkinter.CTkLabel(master=frame,
                                      justify='center',
                                      text='name')
        name.place(relx=0.3, rely=0.2, anchor=CENTER)

        email = customtkinter.CTkLabel(master=frame,
                                       justify="center",
                                       text="e-mail")
        email.place(relx=0.3, rely=0.4, anchor=CENTER)

        password = customtkinter.CTkLabel(master=frame,
                                          justify="center",
                                          text="password")
        password.place(relx=0.3, rely=0.6, anchor=CENTER)

        self.name_entry = customtkinter.CTkEntry(frame)
        self.name_entry.place(relx=0.6, rely=0.2, anchor=CENTER)

        self.email_entry = customtkinter.CTkEntry(frame)
        self.email_entry.place(relx=0.6, rely=0.4, anchor=CENTER)

        self.password_entry = customtkinter.CTkEntry(frame,
                                                     show='*')
        self.password_entry.place(relx=0.6, rely=0.6, anchor=CENTER)

        commitButton = customtkinter.CTkButton(self.win,
                                               command=self.commit,
                                               text='Add')
        commitButton.place(relx=0.8, rely=0.8, anchor=CENTER)

    def commit(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        if add_password(name, email, password):
            self.window = customtkinter.CTkToplevel(self.root)
            self.window.title("Add Password")
            label = customtkinter.CTkLabel(
                self.window, text="Password successfully added.")
            label.pack(fill='x', padx=50, pady=5)
            button_close = customtkinter.CTkButton(
                self.window, text="Close", command=self.newWindow)
            button_close.pack(fill='x')
        else:
            window = customtkinter.CTkToplevel()
            label = customtkinter.CTkLabel(window, text="Incorrect data!")
            label.pack(fill='x', padx=50, pady=5)
            button_close = customtkinter.CTkButton(
                window, text="Close", command=window)
            button_close.pack(fill='x')

    def edit(self):
        choice = self.table.focus()
        if(len(choice) != 0):
            self.win = customtkinter.CTkToplevel(master=self.root)
            self.win.title("Edit")
            self.win.geometry('400x300')
            frame = customtkinter.CTkFrame(master=self.win,
                                           width=500,
                                           height=450,
                                           corner_radius=10)
            frame.pack(padx=20, pady=20)
            param = self.table.item(choice)
            name = customtkinter.CTkLabel(master=frame,
                                          justify='center',
                                          text='name')
            name.place(relx=0.3, rely=0.2, anchor=CENTER)

            email = customtkinter.CTkLabel(master=frame,
                                           justify="center",
                                           text="e-mail")
            email.place(relx=0.3, rely=0.4, anchor=CENTER)

            password = customtkinter.CTkLabel(master=frame,
                                              justify="center",
                                              text="password")
            password.place(relx=0.3, rely=0.6, anchor=CENTER)

            self.name_entry = customtkinter.CTkEntry(frame)
            self.name_entry.place(relx=0.6, rely=0.2, anchor=CENTER)

            self.email_entry = customtkinter.CTkEntry(frame)
            self.email_entry.place(relx=0.6, rely=0.4, anchor=CENTER)

            self.password_entry = customtkinter.CTkEntry(frame,
                                                         show='*')
            self.password_entry.place(relx=0.6, rely=0.6, anchor=CENTER)

            commitButton = customtkinter.CTkButton(self.win,
                                                   command=self.editPassword,
                                                   text='Edit')
            commitButton.place(relx=0.8, rely=0.8, anchor=CENTER)

    def editPassword(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        id = self.table.item(self.table.focus())['values'][0]
        if edit_password(name, email, password, id):
            self.window = customtkinter.CTkToplevel(self.root)
            self.window.title("Edit Password")
            label = customtkinter.CTkLabel(
                self.window, text="Password successfully edited.")
            label.pack(fill='x', padx=50, pady=5)
            button_close = customtkinter.CTkButton(
                self.window, text="Close", command=self.newWindow)
            button_close.pack(fill='x')
        else:
            window = customtkinter.CTkToplevel()
            label = customtkinter.CTkLabel(window, text="Incorrect data!")
            label.pack(fill='x', padx=50, pady=5)
            button_close = customtkinter.CTkButton(
                window, text="Close", command=window.destroy)
            button_close.pack(fill='x')

    def newWindow(self):
        self.win.destroy()
        self.window.destroy()
        self.frame.destroy()
        self.root.withdraw()
        toplevel = customtkinter.CTkToplevel(self.root)
        app = AccountWindow(toplevel)

    def delete(self):
        choice = self.table.focus()
        if(len(choice) != 0):
            self.win = customtkinter.CTkToplevel()
            self.win.geometry('400x400')
            label = customtkinter.CTkLabel(
                self.win,
                text="Press Delete if you want to delete your password")
            label.place(relx=0.5, rely=0.2, anchor=CENTER)
            button_close = customtkinter.CTkButton(
                self.win, text="Back", command=self.win.destroy)
            button_close.place(relx=0.3, rely=0.7, anchor=CENTER)
            button_delete = customtkinter.CTkButton(
                self.win, text="Delete", command=self.deleteConfirmed)
            button_delete.place(relx=0.7, rely=0.7, anchor=CENTER)

    def deleteConfirmed(self):
        id = str(self.table.item(self.table.focus())['values'][0])
        if delete_password(id):
            self.window = customtkinter.CTkToplevel(self.root)
            self.window.title("Edit Password")
            label = customtkinter.CTkLabel(
                self.window, text="Password successfully edited.")
            label.pack(fill='x', padx=50, pady=5)
            button_close = customtkinter.CTkButton(
                self.window, text="Close", command=self.newWindow)
            button_close.pack(fill='x')

    def generate(self):
        # num_of_special, length, num_of_capital, num_of_numbers#
        self.win = customtkinter.CTkToplevel(self.root)
        self.win.title("Generate Password")
        self.win.geometry('400x350')
        length = customtkinter.CTkLabel(self.win)
        length["justify"] = "center"
        length["text"] = "Length of password"
        length.place(relx=0.2, rely=0.1, anchor=CENTER)

        special = customtkinter.CTkLabel(self.win)
        special["justify"] = "center"
        special["text"] = "Num of special characters"
        special.place(relx=0.2, rely=0.3, anchor=CENTER)

        capital = customtkinter.CTkLabel(self.win)
        capital["justify"] = "center"
        capital["text"] = "Num of capital characters"
        capital.place(relx=0.2, rely=0.5, anchor=CENTER)

        numbers = customtkinter.CTkLabel(self.win)
        numbers["justify"] = "center"
        numbers["text"] = "Num of numbers"
        numbers.place(relx=0.2, rely=0.7, anchor=CENTER)

        self.generator = customtkinter.CTkLabel(self.win)
        self.generator["justify"] = "center"
        self.generator["text"] = ""
        self.generator.place(relx=0.5, rely=0.8, anchor=CENTER)

        self.length_entry = customtkinter.CTkEntry(self.win,)
        self.length_entry.place(relx=0.6, rely=0.1, anchor=CENTER)

        self.special_entry = customtkinter.CTkEntry(self.win)
        self.special_entry.place(relx=0.6, rely=0.3, anchor=CENTER)

        self.capital_entry = customtkinter.CTkEntry(self.win)
        self.capital_entry.place(relx=0.6, rely=0.5, anchor=CENTER)

        self.numbers_entry = customtkinter.CTkEntry(self.win)
        self.numbers_entry.place(relx=0.6, rely=0.7, anchor=CENTER)

        generateButton = customtkinter.CTkButton(
            self.win, command=self.generateProcessed, text='Generate')
        generateButton.place(relx=0.7, rely=0.9, anchor=CENTER)

        BackButton = customtkinter.CTkButton(
            self.win, command=self.win.destroy, text='Back')
        BackButton.place(relx=0.3, rely=0.9, anchor=CENTER)

    def generateProcessed(self):
        length = self.length_entry.get()
        special = self.special_entry.get()
        capital = self.capital_entry.get()
        numbers = self.numbers_entry.get()
        test, password = generate_password(length, special, capital, numbers)
        if test:
            self.root.clipboard_append(password)
            self.generator['text'] = password
            window = customtkinter.CTkToplevel()
            label = customtkinter.CTkLabel(
                window, text="Password generated. Copied to clipboard")
            label.pack(fill='x', padx=50, pady=5)
            button_close = customtkinter.CTkButton(
                window, text="Close", command=window.destroy)
            button_close.pack(fill='x')
        else:
            window = customtkinter.CTkToplevel()
            label = customtkinter.CTkLabel(window, text="Incorrect data!")
            label.pack(fill='x', padx=50, pady=5)
            button_close = customtkinter.CTkButton(
                window, text="Close", command=window.destroy)
            button_close.pack(fill='x')


def main():
    root = customtkinter.CTk()
    app = WelcomeWindow(root)
    root.mainloop()


if __name__ == "__main__":
    main()
