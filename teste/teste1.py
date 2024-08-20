import os


os.system('cls')

print('-'*70)
print('entrada de dados')

# entrada 
nome = str(input('entre com o nome:    '))
altura = int(input('entre com sua altura:    '))
nascimento = int(input('entre com nascimento:   '))

# saida 
print('-'*70)
print(f'olá nome:{nome}')
print(f'sua altura é:{altura}')
print(f'seu nascimento é{nascimento}')
print('='*70)