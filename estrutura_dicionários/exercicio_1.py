import os


os.system('cls')

print('_'*70)
print('ESTRUTURA DE DADOS: DICIONÁRIO ') # dict => {}
print('='*70)

compras = {}
pessoas = {}
cores = {}
elementos = dict()
numeros = dict()

# atribuindo valores 
compras['id'] = 1
compras['item'] = 'caderno'
compras['valor'] = 10.80

pessoas['id'] = '0010'
pessoas['nome'] = 'sherlock holmes'
pessoas['endereço'] = 'baker street'
pessoas['numero'] = '221B'
pessoas['cidade'] = 'londres'
pessoas['pais'] = 'londres'

cores['red'] = 'vermelho'
cores['green'] = 'verde'
cores['blue'] = 'azul'

elementos['pb'] = 'chumbo'
elementos['au'] = 'ouro'
elementos['n'] = 'nitrogenio'

numeros[1] = 100
numeros[2] = 200
numeros[3] = 300

# saida simples 
print(f'minhas compras: {compras}')
print(f'detetives: {pessoas}')
print(f'cor rgb: {cores}')
print(f'tabela periodica: {elementos}')
print(f'listagen de numeros: {numeros}')
print()
print('-'*100)