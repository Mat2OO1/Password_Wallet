from audioop import add
from venv import create

from matplotlib.pyplot import show
from backend import *
import numpy as np

pp = PasswordProcess()
# # pp.add_password('e', 'e', 'e')
# # print(pp.show_passwords())
# conn = sqlite3.connect('db.sqlite')
# c = conn.cursor()
# tab = []
# output = []
# j = 0
# for row in c.execute('SELECT * FROM PASSWORD_WALLET'):
#     print(row)
#     tab = list(row)
#     print(tab[3])
#     tab[3] = pp.decrypt_password(tab[3])
#     output.append(tab)
# c.close()
# print(output)
# print(pp.delete_password(0))
# conn = sqlite3.connect('db.sqlite')
# c = conn.cursor()
# c.execute("DELETE FROM Password_wallet WHERE id =? ", (id,))
# conn.commit()
# conn.close()
test, password = pp.generate_password(
    'dssa', '1sdaasd', 'wadscz1', 'dsaczx1')
print(test, password)
