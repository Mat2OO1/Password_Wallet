from setuptools import setup
from controller import generate_password
import random

f = open('key.txt', 'r')
f.write(generate_password(random.random(8, 20), True, True, True, True))
f.close()

setup(
    name='PasswordWallet',
    version='1.0',
    packages='PasswordWallet'
)
