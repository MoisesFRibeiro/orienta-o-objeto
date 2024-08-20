# Faça um programa que imprima os valores no intervalo definidos pelo usuário. 
# Defina 3 números que deverão ser ignorados, ou seja, que não serão impressos na tela.

# curso de desenvolvimento de sistemas 
# turma 0152(braba)
# autor: moises de souza ribeiro
# data: 03/06/2024
# valores no intervalo
# numeros ignorados

import os


os.system('cls')

print('_'*70)
print('imprimindo intervalo ignorando numeros')
print('='*70)

# variaveis
inicio = int(input('entre com o inicio: '))
final = int(input('entre com o final: '))

for c in range(inicio,final):
    if c == 1:
     continue
    elif c == 3:
       continue
    elif c == 5:
       continue
    print(f'{c}')
    
       