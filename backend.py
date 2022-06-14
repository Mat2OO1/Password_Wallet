import os
from numpy import delete, true_divide
import rncryptor
import sqlite3
import string
import secrets
import re
import random


class PasswordProcess:
    def __init__(self):
        self.first = True
        self.output = []

    def plogin(self):
        if 'db.sqlite' in os.listdir('.'):
            self.output = self.show_passwords()
            return True
        else:
            return False

    def check_password(self, password):
        f = open('secrets.bin', 'rb')
        secret = f.read()
        f.close()
        if self.decrypt_password(secret) == password:
            return True
        else:
            return False

    def first_login(self, password):
        with open('secrets.bin', 'wb') as f:
            f.write(self.encrypt_password(password))
        f.close()
        self.create_db()
        return True

    def add_password(self, name, email, password):
        if len(password) == 0 or (len(name) == 0 or len(email) == 0):
            return False
        else:
            enc = self.encrypt_password(password)
            self.save_to_db(name, email, enc, password)
            return True

    def edit_password(self, name, email, password, id):
        if len(password) == 0 or (len(name) == 0 or len(email) == 0):
            return False
        else:
            enc = self.encrypt_password(password)
            self.edit_db(name, email, password, id, enc)
            return True

    def generate_password(self, length, num_of_special, capital, num_of_numbers):
        if not (length.isnumeric() or num_of_special.isnumeric() or capital.isnumeric() or num_of_numbers.isnumeric()):
            return False, ''
        else:
            num_of_special = int(num_of_special)
            length = int(length)
            capital = int(capital)
            num_of_numbers = int(num_of_numbers)
            if(length < num_of_special + capital + num_of_numbers):
                return False, ''
            else:
                upper = string.ascii_uppercase
                numbers = string.digits
                alphabet = string.ascii_letters + string.digits
                special = '!@#$%^&*()-_'

                password = ''.join(secrets.choice(upper)
                                   for i in range(capital))
                password += ''.join(secrets.choice(numbers)
                                    for i in range(num_of_numbers))
                password += ''.join(secrets.choice(special)
                                    for i in range(num_of_special))
                password += ''.join(secrets.choice(alphabet) for i in range(
                    num_of_special + capital + num_of_numbers, length))
                password = ''.join(random.sample(password, len(password)))
                return True, password

    def show_passwords(self):
        if self.first and 'db.sqlite' in os.listdir('.'):
            conn = sqlite3.connect('db.sqlite')
            c = conn.cursor()
            tab = []
            j = 0
            for row in c.execute('SELECT * FROM PASSWORD_WALLET'):
                tab = list(row)
                tab[3] = self.decrypt_password(tab[3])
                self.output.append(tab)
            c.close()
            self.first = False
            return self.output
        else:
            return self.output

    def encrypt_password(self, password):
        key = os.getenv('PASSWORD_WALLET')
        cryptor = rncryptor.RNCryptor()
        encrypted_password = cryptor.encrypt(password, key)
        return encrypted_password

    def decrypt_password(self, password):
        key = os.getenv('PASSWORD_WALLET')
        cryptor = rncryptor.RNCryptor()
        decrypted_password = cryptor.decrypt(password, key)
        return decrypted_password

    def save_to_db(self, name, email, encpassword, password):
        conn = sqlite3.connect('db.sqlite')
        c = conn.cursor()
        c.execute("INSERT INTO Password_wallet(name,email,password) values (?,?,?)",
                  (name, email, encpassword))
        conn.commit()
        conn.close()
        self.updateOutput(len(self.output), name, email, password, 'add')

    def create_db(self):
        conn = sqlite3.connect('db.sqlite')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS Password_wallet
                    (id INTEGER PRIMARY KEY, name TEXT, email TEXT, password TEXT)''')
        conn.commit()
        conn.close()

    def edit_db(self, name, email, password, id, enc):
        conn = sqlite3.connect('db.sqlite')
        c = conn.cursor()
        c.execute("UPDATE Password_wallet SET password =?, name=?, email=? WHERE id =?",
                  (enc, name, email, id))
        conn.commit()
        conn.close()
        self.updateOutput(id, name, email, password, 'edit')

    def delete_password(self, id):
        conn = sqlite3.connect('db.sqlite')
        c = conn.cursor()
        c.execute("DELETE FROM Password_wallet WHERE id =? ", (id,))
        conn.commit()
        conn.close()
        for elem in self.output:
            if int(elem[0]) == int(id):
                i = 0
                for elem in self.output:
                    if int(elem[0]) == int(id):
                        self.output.pop(i)
                        return True
                i += 1
        return False

    def updateOutput(self, id, name, email, password, command):
        if command == 'add':
            self.output.append([id, name, email, password])
        elif command == 'edit':
            i = 0
            for elem in self.output:
                if elem[0] == id:
                    self.output[i] = [id, name, email, password]
                    return True
                i += 1

    def reset(self):
        os.remove('secrets.bin')
        os.remove('db.sqlite')
