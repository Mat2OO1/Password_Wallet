import os
from numpy import delete, true_divide
import rncryptor
import sqlite3
import string
import secrets
import re
import random


def plogin():
    if 'db.sqlite' in os.listdir('.'):
        return True
    else:
        return False


def check_password(password):
    f = open('secrets.bin', 'rb')
    secret = f.read()
    f.close()
    if decrypt_password(secret) == password:
        return True
    else:
        return False


def first_login():
    with open('secrets.bin', 'wb') as f:
        f.write(encrypt_password(get_password()))
    f.close()


def get_password():
    password = 'lubiekoty'
    return password


def add_password(name, email, password):
    if len(password) == 0 or (len(name) == 0 or len(email) == 0):
        return False
    else:
        enc = encrypt_password(password)
        save_to_db(name, email, enc)
        return True


def edit_password(name, email, password, id):
    if len(password) == 0 or (len(name) == 0 or len(email) == 0):
        return False
    else:
        enc = encrypt_password(password)
        edit_db(name, email, enc, id)
        return True


def delete_password(id):
    return delete_from_db(id)


def generate_password(length, num_of_special, capital, num_of_numbers):
    if not (length.isnumeric() or num_of_special.isnumeric() or password.isnumeric() or num_of_numbers.isnumeric()):
        return False, None
    else:
        num_of_special = int(num_of_special)
        length = int(length)
        capital = int(capital)
        num_of_numbers = int(num_of_numbers)
        if(length < num_of_special + capital + num_of_numbers):
            return False, None
        else:
            upper = string.ascii_uppercase
            numbers = string.digits
            alphabet = string.ascii_letters + string.digits
            special = '!@#$%^&*()-_'

            password = ''.join(secrets.choice(upper) for i in range(capital))
            password += ''.join(secrets.choice(numbers)
                                for i in range(num_of_numbers))
            password += ''.join(secrets.choice(special)
                                for i in range(num_of_special))
            password += ''.join(secrets.choice(alphabet) for i in range(
                num_of_special + capital + num_of_numbers, length))
            password = ''.join(random.sample(password, len(password)))
            return True, password


def show_passwords():
    output = []
    conn = sqlite3.connect('db.sqlite')
    c = conn.cursor()
    tab = []
    j = 0
    for row in c.execute('SELECT * FROM PASSWORD_WALLET'):
        tab = list(row)
        tab[3] = decrypt_password(tab[3])
        output.append(tab)
    c.close()
    return output


def encrypt_password(password):
    key = os.getenv('PASSWORD_WALLET')
    cryptor = rncryptor.RNCryptor()
    encrypted_password = cryptor.encrypt(password, key)
    return encrypted_password


def decrypt_password(password):
    key = os.getenv('PASSWORD_WALLET')
    cryptor = rncryptor.RNCryptor()
    decrypted_password = cryptor.decrypt(password, key)
    return decrypted_password


def save_to_db(name, email, password):
    conn = sqlite3.connect('db.sqlite')
    c = conn.cursor()
    c.execute("INSERT INTO Password_wallet(name,email,password) values (?,?,?)",
              (name, email, password))
    conn.commit()
    conn.close()


def create_db():
    conn = sqlite3.connect('db.sqlite')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS Password_wallet
                (id INTEGER PRIMARY KEY, name TEXT, email TEXT, password TEXT)''')
    conn.commit()
    conn.close()


def edit_db(name, email, password, id):
    conn = sqlite3.connect('db.sqlite')
    c = conn.cursor()
    c.execute("UPDATE Password_wallet SET password =?, name=?, email=? WHERE id =?",
              (password, name, email, id))
    conn.commit()
    conn.close()


def delete_from_db(id):
    conn = sqlite3.connect('db.sqlite')
    c = conn.cursor()
    c.execute("DELETE FROM Password_wallet WHERE id =? ", id)
    conn.commit()
    conn.close()
    return True
