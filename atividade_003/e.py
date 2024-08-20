# Faça um programa para sortear um número de 1 a 20.

import os
import random


# sorteio de numeros
os.system('cls')

print('sorteio de numeros')
numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
aleatorio_inteiro = random.randint(1,20)
print(f'O numero inteiro gerado foi: {aleatorio_inteiro}')
print('_'*70)