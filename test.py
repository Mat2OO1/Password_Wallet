from models import Model

m = Model()
m.create_db()
m.add_password('ja', 'da', 'rfs')
print(m.show_passwords[0])
