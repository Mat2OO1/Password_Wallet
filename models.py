import sqlite3
import os
import string
import secrets
import random
import rncryptor


class Model:
    def __init__(self):
        self.create_key()
        self.first = True
        self.output = []

    def login(self):
        if 'db.sqlite' in os.listdir('.'):
            self.output = self.show_passwords()
            return True
        else:
            return False

    def first_login(self, password):
        with open('secrets.bin', 'wb') as f:
            f.write(self.encrypt_password(password))
        f.close()
        self.create_db()

    def create_db(self):
        conn = sqlite3.connect('db.sqlite')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS Password_wallet
                        (id INTEGER PRIMARY KEY, name TEXT, email TEXT, password TEXT)''')
        conn.commit()
        conn.close()

    def edit_password(self, name, email, password, id):
        if len(password) == 0 or (len(name) == 0 or len(email) == 0):
            return False
        else:
            enc = self.encrypt_password(password)
            conn = sqlite3.connect('db.sqlite')
            c = conn.cursor()
            c.execute("UPDATE Password_wallet SET password =?, name=?, email=? WHERE id =?",
                      (enc, name, email, id))
            conn.commit()
            conn.close()
            self.updateOutput(id, name, email, password, 'edit')
            return True

    def add_password(self, name, email, password):
        if len(password) == 0 or (len(name) == 0 or len(email) == 0):
            return False
        else:
            enc = self.encrypt_password(password)
            conn = sqlite3.connect('db.sqlite')
            c = conn.cursor()
            c.execute("INSERT INTO Password_wallet(name,email,password) values (?,?,?)",
                      (name, email, enc))
            conn.commit()
            conn.close()
            self.updateOutput(len(self.output), name, email, password, 'add')
            return True

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

    def check_password(self, password):
        f = open('secrets.bin', 'rb')
        secret = f.read()
        f.close()
        if self.decrypt_password(secret) == password:
            return True
        else:
            return False

    def show_passwords(self):
        if self.first and 'db.sqlite' in os.listdir('.'):
            conn = sqlite3.connect('db.sqlite')
            c = conn.cursor()
            for row in c.execute('SELECT * FROM PASSWORD_WALLET'):
                tab = list(row)
                tab[3] = self.decrypt_password(tab[3])
                self.output.append(tab)
            self.first = False
        return self.output

    def encrypt_password(self, password):
        key = self.get_key()
        cryptor = rncryptor.RNCryptor()
        encrypted_password = cryptor.encrypt(password, key)
        return encrypted_password

    def decrypt_password(self, password):
        key = self.get_key()
        cryptor = rncryptor.RNCryptor()
        decrypted_password = cryptor.decrypt(password, key)
        return decrypted_password

    def get_key(self):
        f = open('key.txt', 'r')
        key = f.read()
        f.close()
        return key

    def generate_password(self, length, ifspecial, ifupper, ifnumbers, iflower):
        if iflower or ifnumbers or ifspecial or ifupper:
            upper = string.ascii_uppercase
            numbers = string.digits
            lower = string.ascii_lowercase
            special = '!@#$%^&*()-_'
            password = ''
            alphabet = ''
            length = int(length)
            if ifspecial:
                password += ''.join(secrets.choice(special))
                alphabet += special
            if ifupper:
                password += ''.join(secrets.choice(upper))
                alphabet += upper
            if ifnumbers:
                password += ''.join(secrets.choice(numbers))
                alphabet += numbers
            if iflower:
                password += ''.join(secrets.choice(lower))
                alphabet += lower
            password += ''.join(secrets.choice(alphabet)
                                for i in range(length - len(password)))
            password = ''.join(random.sample(password, len(password)))
            return password, True
        else:
            return None, False

    def reset(self):
        os.remove('secrets.bin')
        os.remove('db.sqlite')
        self.output = []

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

    def create_key(self):
        if 'key.txt' not in os.listdir('.'):
            f = open('key.txt', 'w')
            f.write(self.generate_password(
                random.randint(8, 20), True, True, True, True)[0])
            f.close()
