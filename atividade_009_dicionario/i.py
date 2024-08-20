# Faça um programa para criar um dicionário com 4 elementos.
# Depois imprima a lista completa, delete o último elemento e mostre uma listagem nova.

# curso de desenvolvimento de sistemas
# Turma 0152 ( Braba)
# Autor: Moises de Souza Ribeiro
# Data 04/07/2024
# dicionários

import os


os.system('cls')

print('-'*70)
print('Dicionário de 4 elementos')
print('='*70)

# criando um dicionário 
fruta = {}

# atribuindo 4 elementos ao dicionário
fruta['fruta1'] = 'maçã'
fruta['fruta2'] = 'goiaba'
fruta['fruta3'] = 'uva'
fruta['fruta4'] = 'morango'

# imprimindo a lista completa
print(f'lista completa de frutas é {fruta}')

# deletando o ultimo elemento
del fruta ['fruta4']

# mostrando a nova lista de frutas
print(f'a nova lista é: {fruta}')

print('-'*70)
print('saindo do programa')
print()
