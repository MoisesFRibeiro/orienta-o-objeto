# Utilizando o exercício anterior , retire um elemento do dicionário.

import os 


os.system('cls')

print('-'*70)
print('retirando um elemento do dicionário')
print('='*70)

# criando um dicionário
carros = {}

# atribuindo elementos
carros[1] = 'ford ka'
carros[2] = 'celta'
carros[3] = 'gol'
carros[4] = 'uno'

# removendo um intem  
print('remover um intem usando pop(). ')
if carros:
    carros = input('digite o carro que deseja excluir: ')
    valor_removido = carros.pop(carros, 'carros não encontrado')
    print(f'item removido: {carros}: {valor_removido}')