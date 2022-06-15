import tkinter as tk
from tkinter import CENTER, END, LEFT, W, ttk
import customtkinter

# Modes: system (default), light, dark
customtkinter.set_appearance_mode("dark")
# Themes: blue (default), dark-blue, green
customtkinter.set_default_color_theme("dark-blue")


class WelcomeView:
    def __init__(self, root, controller):
        self.root = root
        self.root.title("Password Wallet")
        self.root.geometry('600x500')
        self.frame = customtkinter.CTkFrame(master=self.root,
                                            width=500,
                                            height=450,
                                            corner_radius=10)
        self.frame.pack(padx=20, pady=20)
        title = customtkinter.CTkLabel(
            master=self.frame, width=120, height=25, corner_radius=8, justify='center', text="Password Wallet")
        title.place(relx=0.5, rely=0.2, anchor=CENTER)

        info = customtkinter.CTkLabel(
            master=self.frame,
            width=400,
            height=40,
            corner_radius=8,
            justify='center',
            text="Please log in to see your passwords. \n If its your first log in, click register")
        info.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.loginButton = customtkinter.CTkButton(
            master=self.frame,
            command=controller.log_in,
            width=120,
            height=32,
            border_width=0,
            corner_radius=8,
            text='Log In')
        self.loginButton.place(relx=0.65, rely=0.7, anchor=CENTER)

        self.registerButton = customtkinter.CTkButton(master=self.frame,
                                                      command=controller.register,
                                                      width=120,
                                                      height=32,
                                                      border_width=0,
                                                      corner_radius=8,
                                                      text='Register')
        self.registerButton.place(relx=0.35, rely=0.7, anchor=CENTER)

        if controller.login():
            self.registerButton.configure(state=tk.DISABLED)
        else:
            self.loginButton.configure(state=tk.DISABLED)


class RegisterView:
    def __init__(self, root, controller):
        self.root = root
        self.root.title("Register")
        self.root.geometry('400x300')
        self.frame = customtkinter.CTkFrame(master=self.root,
                                            width=500,
                                            height=450,
                                            corner_radius=10)
        self.frame.pack(padx=20, pady=20)
        name = customtkinter.CTkLabel(
            self.frame,
            justify="center",
            text="Password:")
        name.place(relx=0.2, rely=0.5, anchor=CENTER)
        self.password_entry = customtkinter.CTkEntry(master=self.frame,
                                                     show='*')
        self.password_entry.place(relx=0.5, rely=0.5, anchor=CENTER)

        self.commitButton = customtkinter.CTkButton(
            master=self.frame,
            command=controller.registerProcessed,
            width=120,
            height=32,
            border_width=0,
            corner_radius=8,
            text='Add')
        self.commitButton.place(relx=0.8, rely=0.8, anchor=CENTER)


class LoginView:
    def __init__(self, root, controller):
        self.root = root
        self.root.title("Password Wallet")
        self.root.geometry('600x500')
        self.root.protocol('WM_DELETE_WINDOW', exit)
        self.frame = customtkinter.CTkFrame(master=self.root,
                                            width=500,
                                            height=450,
                                            corner_radius=10)
        self.frame.pack(padx=20, pady=20)

        text = customtkinter.CTkLabel(master=self.frame,
                                      justify="center",
                                      width=140,
                                      height=25,
                                      corner_radius=8,
                                      text="Password:")
        text.place(relx=0.2, rely=0.5, anchor=CENTER)

        info = customtkinter.CTkLabel(master=self.frame,
                                      justify="center",
                                      width=120,
                                      height=25,
                                      corner_radius=8,
                                      text="Please enter your password:")
        info.place(relx=0.5, rely=0.2, anchor=CENTER)

        self.name_entry = customtkinter.CTkEntry(master=self.frame,
                                                 show='*')
        self.name_entry.place(relx=0.5, rely=0.5, anchor=CENTER)

        commitButton = customtkinter.CTkButton(master=self.frame,
                                               command=controller.password_process,
                                               width=120,
                                               height=32,
                                               border_width=0,
                                               corner_radius=8,
                                               text='Log In')
        commitButton.place(relx=0.8, rely=0.8, anchor=CENTER)

        resetButton = customtkinter.CTkButton(master=self.frame,
                                              command=controller.reset,
                                              width=120,
                                              height=32,
                                              border_width=0,
                                              corner_radius=8,
                                              text='Forgot Password')
        resetButton.place(relx=0.2, rely=0.8, anchor=CENTER)


class AccountView:
    def __init__(self, root, controller):
        self.root = root
        self.root.title("Password Wallet")
        self.root.geometry('800x600')
        self.root.protocol('WM_DELETE_WINDOW', exit)
        self.frame = customtkinter.CTkFrame(master=self.root,
                                            width=700,
                                            height=400,
                                            corner_radius=10)
        self.frame.pack(padx=40, pady=40)
        text = customtkinter.CTkLabel(
            self.frame,
            justify="center",
            text="In order to get your password, double-click on it")
        text.place(relx=0.5, rely=0.1, anchor=CENTER)
        style = ttk.Style()
        style.configure("Treeview",
                        highlightthickness=0,
                        bd=0,
                        font=(
                            'Calibri', 11))
        style.configure("Treeview.Heading", font=(
            'Calibri', 13, 'bold'))
        style.layout("Treeview", [('mystyle.Treeview.treearea', {
            'sticky': 'nswe'})])
        style.configure('Treeview',
                        rowheight=30,
                        background='#2E2E2C',
                        foreground='white',
                        fieldbackground='#3c78a3')

        style.map('Treeview',
                  background=[['selected', '#3c78a3']],
                  foreground=[['selected', 'white']])
        self.table = ttk.Treeview(
            self.frame, style="mystyle.Treeview")
        self.table['show'] = 'headings'
        self.table['columns'] = ('id', 'name', 'email', 'password')
        self.table["displaycolumns"] = ("name", "email")
        self.table.column("id", width=10, stretch=0, anchor=W)
        self.table.column("name", width=180, stretch=0, anchor=W)
        self.table.column("email", width=180, anchor=W)
        self.table.column("password", width=180, anchor=W)
        self.table.heading("id", text="Id", anchor=CENTER)
        self.table.heading("name", text="Name", anchor=CENTER)
        self.table.heading("email", text="E-mail/Login", anchor=CENTER)
        self.table.heading("password", text="Password", anchor=CENTER)
        self.table.bind("<Double-1>", controller.showPassword)
        i = 0
        for row in controller.model.output:
            self.table.insert(parent='', index='end', iid=i, text='',
                              values=(row[0], row[1], row[2], row[3]))
            i += 1
        self.table.pack()
        self.table.place(relx=0.35, rely=0.5, anchor=CENTER)
        addButton = customtkinter.CTkButton(master=self.frame,
                                            command=controller.add,
                                            text='Add Password',
                                            width=120,
                                            height=32,
                                            border_width=0,
                                            corner_radius=8)
        addButton.place(relx=0.8, rely=0.2, anchor=CENTER)

        editButton = customtkinter.CTkButton(master=self.frame,
                                             command=controller.edit,
                                             text='Edit Password',
                                             width=120,
                                             height=32,
                                             border_width=0,
                                             corner_radius=8)
        editButton.place(relx=0.8, rely=0.35, anchor=CENTER)

        deleteButton = customtkinter.CTkButton(master=self.frame,
                                               command=controller.delete,
                                               text='Delete Password',
                                               width=120,
                                               height=32,
                                               border_width=0,
                                               corner_radius=8)
        deleteButton.place(relx=0.8, rely=0.5, anchor=CENTER)

        generateButton = customtkinter.CTkButton(master=self.frame,
                                                 command=controller.generate,
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
