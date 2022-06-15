from tkinter import CENTER, END, W
import customtkinter
from models import Model
from views import WelcomeView, RegisterView, LoginView, AccountView
import tkinter as tk


class Controller:
    def __init__(self):
        self.model = Model()
        self.root = customtkinter.CTk()
        self.ActiveView = WelcomeView(self.root, self)

    def run(self):
        self.app = self.ActiveView
        self.root.mainloop()

    def login(self):
        return self.model.login()

    def first_login(self):
        return self.model.first_login()

    def add_password(self, name, email, password):
        return self.model.add_password(name, email, password)

    def edit_password(self, name, email, password, id):
        return self.model.edit_password(name, email, password, id)

    def delete_password(self, id):
        return self.model.delete_password(id)

    def generate_password(self, length, ifspecial, ifupper, ifnumbers, iflower):
        return self.model.generate_password(length, ifspecial, ifupper, ifnumbers, iflower)

    def check_password(self, password):
        return self.model.check_password(password)

    def show_passwords(self):
        return self.model.show_passwords()

    def reset(self):
        self.model.reset()

    def get_passwords(self):
        return self.model.get_passwords()

    def updateOutput(self, id, name, email, password, command):
        self.model.updateOutput(id, name, email, password, command)

    # methods for WelcomeView
    def log_in(self):
        self.root.withdraw()
        toplevel = customtkinter.CTkToplevel(self.root)
        toplevel.geometry("350x350")
        self.app = LoginView(toplevel, self)
        self.ActiveView = self.app

    def register(self):
        self.root.withdraw()
        toplevel = customtkinter.CTkToplevel(self.root)
        toplevel.geometry("350x350")
        self.app = RegisterView(toplevel, self)
        self.ActiveView = self.app

    # methods for RegisterView
    def registerProcessed(self):
        password = self.ActiveView.password_entry.get()
        self.model.first_login(password)
        self.root.withdraw()
        self.ActiveView.root.destroy()
        self.log_in()

    # methods for LoginView

    def password_process(self):
        password = self.ActiveView.name_entry.get()
        if self.model.check_password(password):
            self.window = customtkinter.CTkToplevel()
            self.window.title = "Login successfull"
            label = customtkinter.CTkLabel(
                self.window, text="Correct password!")
            label.pack(fill='x', padx=50, pady=5)
            button_close = customtkinter.CTkButton(
                self.window, text="Close", command=self.new_window)
            button_close.pack(fill='x')
        else:
            self.window = customtkinter.CTkToplevel()
            label = customtkinter.CTkLabel(
                self.window, text="Password Incorrect!")
            label.pack(fill='x', padx=50, pady=5)
            button_close = customtkinter.CTkButton(
                self.window, text="Close", command=self.window.destroy)
            button_close.pack(fill='x')

    def reset(self):
        self.window = customtkinter.CTkToplevel()
        self.window.title("Forgot Password")
        self.window.geometry('400x300')
        self.frame = customtkinter.CTkFrame(master=self.window,
                                            width=500,
                                            height=450,
                                            corner_radius=10)
        self.frame.pack(padx=20, pady=20)

        info = customtkinter.CTkLabel(master=self.frame,
                                      justify='center',
                                      text='Are you sure? \n All data will be lost')
        info.place(relx=0.5, rely=0.3, anchor=CENTER)

        confirmButton = customtkinter.CTkButton(self.frame,
                                                command=self.confirm,
                                                text='Confirm')
        confirmButton.place(relx=0.7, rely=0.7, anchor=CENTER)

    def confirm(self):
        self.model.reset()
        self.ActiveView.root.destroy()
        self.window.destroy()
        self.root.withdraw()
        toplevel = customtkinter.CTkToplevel(self.root)
        self.app = WelcomeView(toplevel, self)
        self.ActiveView = self.app

    def new_window(self):
        self.root.withdraw()
        self.window.destroy()
        toplevel = customtkinter.CTkToplevel(self.root)
        toplevel.geometry("350x350")
        self.ActiveView.root.destroy()
        self.app = AccountView(toplevel, self)
        self.ActiveView = self.app

    def exit(self):
        self.root.destroy()

    # methods for AccountView

    def showPassword(self, event):
        password = self.ActiveView.table.item(
            self.ActiveView.table.focus())['values'][3]
        self.ActiveView.root.clipboard_clear()
        self.ActiveView.root.clipboard_append(password)
        window = customtkinter.CTkToplevel(self.root)
        window.title = "Password"
        label = customtkinter.CTkLabel(
            window, text="Password copied to clipboard")
        label.pack(fill='x', padx=50, pady=5)
        button_close = customtkinter.CTkButton(
            window, text="Close", command=window.destroy)
        button_close.pack(fill='x')

    def add(self):
        self.win = customtkinter.CTkToplevel(master=self.root)
        self.win.title("Add Password")
        self.win.geometry('400x300')
        self.frame = customtkinter.CTkFrame(master=self.win,
                                            width=500,
                                            height=450,
                                            corner_radius=10)
        self.frame.pack(padx=20, pady=20)

        name = customtkinter.CTkLabel(master=self.frame,
                                      justify='center',
                                      text='name')
        name.place(relx=0.3, rely=0.2, anchor=CENTER)

        email = customtkinter.CTkLabel(master=self.frame,
                                       justify="center",
                                       text="e-mail")
        email.place(relx=0.3, rely=0.4, anchor=CENTER)

        password = customtkinter.CTkLabel(master=self.frame,
                                          justify="center",
                                          text="password")
        password.place(relx=0.3, rely=0.6, anchor=CENTER)

        self.name_entry = customtkinter.CTkEntry(self.frame)
        self.name_entry.place(relx=0.6, rely=0.2, anchor=CENTER)

        self.email_entry = customtkinter.CTkEntry(self.frame)
        self.email_entry.place(relx=0.6, rely=0.4, anchor=CENTER)

        self.password_entry = customtkinter.CTkEntry(self.frame,
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
        if self.model.add_password(name, email, password):
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
            window.title = "Add password"
            label = customtkinter.CTkLabel(window, text="Incorrect data!")
            label.pack(fill='x', padx=50, pady=5)
            button_close = customtkinter.CTkButton(
                window, text="Close", command=window)
            button_close.pack(fill='x')

    def edit(self):
        choice = self.ActiveView.table.focus()
        values = password = self.ActiveView.table.item(choice)['values']
        if(len(choice) != 0):
            self.win = customtkinter.CTkToplevel(master=self.root)
            self.win.title("Edit")
            self.win.geometry('400x300')
            self.frame = customtkinter.CTkFrame(master=self.win,
                                                width=500,
                                                height=450,
                                                corner_radius=10)
            self.frame.pack(padx=20, pady=20)
            param = self.ActiveView.table.item(choice)
            name = customtkinter.CTkLabel(master=self.frame,
                                          justify='center',
                                          text='name')
            name.place(relx=0.3, rely=0.2, anchor=CENTER)

            email = customtkinter.CTkLabel(master=self.frame,
                                           justify="center",
                                           text="e-mail")
            email.place(relx=0.3, rely=0.4, anchor=CENTER)

            password = customtkinter.CTkLabel(master=self.frame,
                                              justify="center",
                                              text="password")
            password.place(relx=0.3, rely=0.6, anchor=CENTER)

            self.name_entry = customtkinter.CTkEntry(
                self.frame)
            self.name_entry.insert(END, values[1])
            self.name_entry.place(relx=0.6, rely=0.2, anchor=CENTER)

            self.email_entry = customtkinter.CTkEntry(self.frame)
            self.email_entry.insert(END, values[2])
            self.email_entry.place(relx=0.6, rely=0.4, anchor=CENTER)

            self.password_entry = customtkinter.CTkEntry(self.frame)
            self.password_entry.insert(END, values[3])
            self.password_entry.place(relx=0.6, rely=0.6, anchor=CENTER)

            commitButton = customtkinter.CTkButton(self.win,
                                                   command=self.editPassword,
                                                   text='Edit')
            commitButton.place(relx=0.8, rely=0.8, anchor=CENTER)

    def editPassword(self):
        name = self.name_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        id = self.ActiveView.table.item(
            self.ActiveView.table.focus())['values'][0]
        if self.model.edit_password(name, email, password, id):
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
            window.title("Edit Password")
            label = customtkinter.CTkLabel(window, text="Incorrect data!")
            label.pack(fill='x', padx=50, pady=5)
            button_close = customtkinter.CTkButton(
                window, text="Close", command=window.destroy)
            button_close.pack(fill='x')

    def newWindow(self):
        self.win.destroy()
        self.window.destroy()
        self.root.withdraw()
        self.ActiveView.root.destroy()
        toplevel = customtkinter.CTkToplevel(self.root)
        self.app = AccountView(toplevel, self)
        self.ActiveView = self.app

    def delete(self):
        choice = self.ActiveView.table.focus()
        if(len(choice) != 0):
            self.win = customtkinter.CTkToplevel(self.root)
            self.win.geometry('400x400')
            self.win.title = "Delete Password"
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
        id = str(self.ActiveView.table.item(
            self.ActiveView.table.focus())['values'][0])
        if self.model.delete_password(id):
            self.window = customtkinter.CTkToplevel(self.root)
            self.window.title("Delete Password")
            label = customtkinter.CTkLabel(
                self.window, text="Password successfully deleted.")
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
        length["text"] = "Length"
        length.place(relx=0.2, rely=0.1, anchor=CENTER)

        self.generator = customtkinter.CTkLabel(self.win)
        self.generator["justify"] = "center"
        self.generator["text"] = ""
        self.generator.place(relx=0.5, rely=0.8, anchor=CENTER)

        self.combobox = customtkinter.CTkComboBox(master=self.win,
                                                  values=[
                                                      8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
        self.combobox.place(relx=0.5, rely=0.1, anchor=CENTER)

        self.checkbox_special = customtkinter.CTkCheckBox(
            master=self.win, text="Special")
        self.checkbox_special.place(relx=0.5, rely=0.25, anchor=W)

        self.checkbox_upper = customtkinter.CTkCheckBox(
            master=self.win, text="Upper  ")
        self.checkbox_upper.place(relx=0.5, rely=0.4, anchor=W)

        self.checkbox_lower = customtkinter.CTkCheckBox(
            master=self.win, text="Lower  ")
        self.checkbox_lower.place(relx=0.5, rely=0.55, anchor=W)

        self.checkbox_numbers = customtkinter.CTkCheckBox(
            master=self.win, text="Numbers ")
        self.checkbox_numbers.place(relx=0.5, rely=0.7, anchor=W)

        generateButton = customtkinter.CTkButton(
            self.win, command=self.generateProcessed, text='Generate')
        generateButton.place(relx=0.7, rely=0.9, anchor=CENTER)

        BackButton = customtkinter.CTkButton(
            self.win, command=self.win.destroy, text='Back')
        BackButton.place(relx=0.3, rely=0.9, anchor=CENTER)

    def generateProcessed(self):
        length = self.combobox.get()
        special = self.checkbox_special.get()
        upper = self.checkbox_upper.get()
        lower = self.checkbox_lower.get()
        numbers = self.checkbox_numbers.get()
        password, test = self.model.generate_password(
            length, special, upper, numbers, lower)
        if test:
            self.root.clipboard_append(password)
            self.generator['text'] = password
            window = customtkinter.CTkToplevel(self.root)
            window.title = "Generate Password"
            label = customtkinter.CTkLabel(
                window, text="Password generated. Copied to clipboard")
            label.pack(fill='x', padx=50, pady=5)
            button_close = customtkinter.CTkButton(
                window, text="Close", command=window.destroy)
            button_close.pack(fill='x')
        else:
            window = customtkinter.CTkToplevel()
            window.title("Generate Password")
            label = customtkinter.CTkLabel(window, text="Incorrect data!")
            label.pack(fill='x', padx=50, pady=5)
            button_close = customtkinter.CTkButton(
                window, text="Close", command=window.destroy)
            button_close.pack(fill='x')


if __name__ == '__main__':
    c = Controller()
    c.run()
