# Faça um programa para criar um dicionário com 5  cores. Depois,  imprima as chaves e os valores deste dicionário.

import os 


os.system('cls')

print('-'*70)
print('imprimindo chaves e valores')
print('='*70)

cores = {}

# atribuindo valores
cores['pink'] = 'rosa'
cores['black'] = 'preto'
cores['orange'] = 'laranja'
cores['green'] = 'verde'
cores['blue'] = 'azul'

# saida da chaves com valores
valor = cores.get('cores não encontrada')
print(f'cor RGB: {cores}')