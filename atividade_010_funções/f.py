# Crie uma função que receba 2 listas: 
# - lista 1: nome, peso, idade
# - lista 2: John, 40, 1.8
# - Sua função deverá criar um dicionário contendo chave e valor utilizando como base essas duas listas.
# Depois, seu programa deverá imprimir esse dicionário utilizando uma estrutura de repetição for.

# curso de desenvolvimento de sistemas
# Turma 0152 ( Braba)
# Autor: Moises de Souza Ribeiro
# Data 05/08/2024
# estrutura em for

import os


os.system('cls')

print('-'*70)
print('estrutura em for')
print('='*70)

lista_1 = ['nome', 'peso', 'idade']
lista_2 = ['whyllian', 65, 3.5]


def receber_listas():

    dicionario = dict(zip(lista_1, lista_2))

    for chave, valor in dicionario.items():
        print(f'{chave}: {valor}')

receber_listas()
print()