# imports
import os


os.system('cls')

print('_'*70)
print('Media das Notas')
print('_'*70)

# Entrada de Dados
nota1 = float(input('entre com a 1ª nota : '))
nota2 = float(input('entre com a 2ª nota : '))
nota3 = float(input('entre com a 3ª nota : '))
nota4 = float(input('entre com a 4ª nota : '))

# processamento
media = (nota1 + nota2 + nota3 + nota4) / 4

# saida

print('_'*70)
print (f'media : {media}')
print('_'*70)
