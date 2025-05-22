import os
os.system('clear')

r0 = input('Programa de primeros auxilios iniciada\nResponde a las preguntas con "si" o "no"\nIngresa "q" ' \
'para salir en cualquier momento\nPresiona enter para continuar ')

fin = 'Programa finalizado\n'
enter = '\nPresiona enter para continuar\n'

if r0.lower() == 'q':
    os.system('clear')
    print(fin)
    exit()

while True:
    os.system('clear')
    r1 = input('¿La persona responde a estímulos? ')
    if r1.lower() == 'si':
        print('\nValorar la necesidad de llevarlo al hospital más cercano.\n\nPrograma finalizado\n')
        exit()
    elif r1.lower() == 'no':
        print('\nAbrir vía aérea')
        break
    elif r1.lower() == 'q':
        os.system('clear')
        print(fin)
        exit()
if input(enter) == 'q':
    os.system('clear')
    print(fin)
    exit()

while True:
    os.system('clear')
    r2 = input('¿La persona respira? ')
    if r2.lower() == 'si':
        print('\nPermitirle posición de suficiente ventilación\n\nPrograma finalizado\n')
        exit()
    elif r2.lower() == 'no':
        print('\nAdministrar 5 ventilaciones y llamar a la ambulancia.')
        break
    elif r2.lower() == 'q':
        os.system('clear')
        print(fin)
        exit()

if input(enter) == 'q':
    os.system('clear')
    print(fin)
    exit()
cont = 0
while True:
    if cont != 0:
        while True:
            os.system('clear')
            r3 = input('¿Llegó la ambulancia? ')
            if r3.lower() == 'si':
                print(fin)
                exit()
            elif r3.lower() == 'no':
                break
            elif r3.lower() == 'q':
                os.system('clear')
                print(fin)
                exit()

    while True:   
        os.system('clear')
        r4 = input('¿La persona tiene signos de vida? ')

        if r4.lower() == 'si':
            print('\nReevaluar a la espera de la ambulancia.')
            if cont == 0:
                cont += 1
            break
        elif r4.lower() == 'no':
            print('\nAdministrar compresiones torácicas hasta que llegue la ambulancia.')
            if cont == 0:
                cont += 1
            break
        elif r4.lower() == 'q':
            os.system('clear')
            print(fin)
            exit()
    if input(enter) == 'q':
        os.system('clear')
        print(fin)
        exit()