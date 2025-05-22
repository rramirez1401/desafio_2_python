from string import ascii_lowercase
from getpass import *
import os

os.system('clear')

abc = ascii_lowercase

password = getpass("Ingresa la contraseña: ")

counter = 0

forced_pass = []

for let1 in password:
    for let2 in abc:
        counter += 1
        if let1 == let2:
            forced_pass.append(let2)
            break


print(f'Contraseña descubierta\nLa contraseña es: {(''.join(forced_pass))}')
print(f'La contraseña fué forzada en {counter} intentos')

    