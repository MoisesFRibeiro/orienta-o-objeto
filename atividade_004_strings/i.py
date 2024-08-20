# Faça um programa que receba o nome completo de uma pessoa e, em seguida, mostre o primeiro e o último nome.

# curso de desenvolvimento de sistemas 
# turma 0152(braba)
# autor: moises de souza ribeiro
# data: 27/05/2024
# nome completo
# mostrar primeiro e ultimo nome

import os


os.system('cls')

# entrada
nome_completo = input('digite o nome completo')

# processamento
# dividindo o nome completo em uma lista de nomes
lista = nome_completo.split(' ')
primeiro_nome = lista[0]
ultimo_nome = lista[-1]

# saida 
print(f'primeiro nome: {primeiro_nome}')
print(f'ultimo nome: {ultimo_nome}')
print('_'*70)