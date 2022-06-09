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
    enc = encrypt_password(password)
    save_to_db(name, email, enc)


def edit_password(name, email, password):
    enc = encrypt_password(password)
    edit_db(name, email, enc)
    pass


def delete_password():
    delete_from_db()


def generate_password(num_of_special, length, num_of_capital, num_of_numbers):
    upper = string.ascii_uppercase
    numbers = string.digits
    alphabet = string.ascii_letters + string.digits
    special = '!@#$%^&*()-_'

    password = ''.join(secrets.choice(upper) for i in range(num_of_capital))
    password += ''.join(secrets.choice(numbers)
                        for i in range(num_of_numbers))
    password += ''.join(secrets.choice(special)
                        for i in range(num_of_special))
    password += ''.join(secrets.choice(alphabet) for i in range(
        num_of_special + num_of_capital + num_of_numbers, length))
    password = ''.join(random.sample(password, len(password)))
    return password


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


def edit_db(name, email, password):
    conn = sqlite3.connect('db.sqlite')
    c = conn.cursor()
    c.execute("UPDATE Password_wallet SET password = ? WHERE name = ? AND email = ? ",
              (password, name, email))
    conn.commit()
    conn.close()


def delete_from_db(name, email):
    conn = sqlite3.connect('db.sqlite')
    c = conn.cursor()
    c.execute(
        "DELETE FROM Password_wallet WHERE name = ? AND email = ? ", (name, email))
    conn.commit()
    conn.close()
