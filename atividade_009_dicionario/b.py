# Utilizando o exercício anterior,  adicione mais 2 elementos ao dicionário.

import os


os.system('cls')

print('-'*70)
print('adicionando mais 2 elementos a lista')
print('='*70)

# criando um dicionário
carros = {}

# atribuindo elementos
carros[1] = 'ford ka'
carros[2] = 'celta'
carros[3] = 'gol'
carros[4] = 'uno'
carros[5] = {}
carros[6] = {}

# adicionado mais 2 elementos a ao dicionario
carros[5] = int(input('digite aqui seu carro a ser adicionado: '))
carros[6] = int(input('digite aqui seu carro a ser adicionado: '))
carros.items()

print('-'*70)
print(f'lista de carros atualizada: {'carros'}')