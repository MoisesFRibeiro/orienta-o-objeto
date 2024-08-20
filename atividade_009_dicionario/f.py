# Faça um programa que cadastra 5 tipos de vinho.
#  Para os campos deste cadastro tome como referência
#  nome do vinho, tipo, teor alcoólico e safra.

import os


os.system('cls')

# criando uma biblioteca
vinhos = [ ]
vinho = {}

# solicitando cadastro de referências
nome_do_vinho = str('entre com o nome do vinho:')
tipo = str('entre com o tipo do vinho: ')
teor_alcóolico = str('entre com o teor alcóolico: ')
safra = str('entre com a safra do vinho: ')

# adicionnado elementos a essa biblioteca
vinhos[1] = input('digite aqui o nome do vinho: ')  
if vinho == vinhos:
    for vinhos in vinho.items():
        print(f'{vinhos.capitalize()}:{vinho}')

vinhos[2] = input('digite aqui o nome do vinho: ')
if vinho == vinhos:
    for vinhos in vinho.items():
        print(f'{vinhos.capitalize()}: {vinho}')

vinhos[3] = input('digite aqui o nome do vinho: ')
if vinho == vinhos:
    for vinhos in vinho.items():
        print(f'{vinhos.capitalize()}: {vinho}')

vinhos[4] = input('digite aqui o nome do vinho: ')
if vinho == vinhos:
    for vinhos in vinho.items():
        print(f'{vinhos.capitalize()}: {vinho}')

vinhos[5] = input('digite aqui o nome do vinho: ')
if vinho == vinhos:
    for vinhos in vinho.items():
        print(f'{vinhos.capitalize()}: {vinho}')

