# Faça um programa que receba um número inteiro e mostre na tela:
# • A quantidade de unidades, a quantidade de dezenas, a quantidade de centenas e a quantidade de milhares.

# curso de desenvolvimento de sistemas 
# turma 0152(braba)
# autor: moises de souza ribeiro
# data: 27/05/2024
# número inteiro
# mostrar a quantidade

import os


os.system('cls')

# entrada
numero = int(input('entre com o numero inteiro'))

# processamento
unidades = numero % 10
dezenas = (numero //10) % 10
centenas = (numero //100) % 10
milhares = (numero//1000) % 10

# saida
print(f'quantidade de unidades: {unidades}')
print(f'quantidade de dezenas: {dezenas}')
print(f'quantidade de centenas: {centenas}')
print(f'quantidade de milhares: {milhares}')
print('_'*70)

