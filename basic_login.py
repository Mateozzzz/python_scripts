#Gobla Functions
user = input('Ingrese su nombre de usuario: ')
password = input('Ingrese su contraseña: ')

#Login User
def login():
    print (f'Hola {user}')
    if password == '123456':
        print('Acceso Concedido :)')
    else:
        print('Acceso Denegado..')
#Call Function     
login()
    
