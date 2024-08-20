import os


os.system('cls')

print('-'*70)
print('ESTRUTURA DE DADOS: DICIONARIO ') # dict => {}
print('='*70)

# indices iguais: só ira exebir um intem
dicionário1 = {'nome': 'john' , 'nome' : 'jane'}

# posso ter uma tupla com indice e uma lista como valor
dicionário2 = {(1, 2) : [1, 2]}

# mas não posso ter uma lista como indice e uma tupla com valor
dicionário3 = {[1, 2] : (1, 2)}

# saida 
print('-'*80)
print(dicionário1)
print(dicionário2)

print()