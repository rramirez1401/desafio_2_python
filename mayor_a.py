import sys
import os

ventas = {
"Enero": 15000,
"Febrero": 22000,
"Marzo": 12000,
"Abril": 17000,
"Mayo": 81000,
"Junio": 13000,
"Julio": 21000,
"Agosto": 41200,
"Septiembre": 25000,
"Octubre": 21500,
"Noviembre": 91000,
"Diciembre": 21000,
}

try:
    mayor = {mes: monto for mes, monto in ventas.items() if int(monto) > int(sys.argv[1])}
    os.system('clear')
    print(f'{mayor}\n')


except (ValueError, IndexError) as e:
    os.system('clear')
    print('Argumento no válido, intenta de nuevo (ejemplo: python nombre_archivo.py valor_a_filtrar)\n')
    exit()
