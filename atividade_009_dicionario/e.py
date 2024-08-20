# Faça um programa para criar um dicionário com 5  ferramentas.
#  Depois,  imprima os valores e a quantidade de elementos do dicionário.

import os


os.system('cls')

print('-'*70)
print('imprimindo valores e quantidade de elementos')
print('='*70)

# criando um dicionário para receber ferramentas
ferramentas = {}

# atribuindo as ferramentas 
ferramentas[1] = 'martelo'
ferramentas[2] = 'cerrote'
ferramentas[3] = 'serrinha'
ferramentas[4] = 'martelete'
ferramentas[5] = 'facão'

# saida com valores e quantidade
print("\nferramentas:")
for valor, quantidade in ferramentas.items():
    print(f'{valor}: {quantidade}')
    print('-'*70)
    print