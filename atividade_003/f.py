
# curso de desenvolvimento de sistemas
# Turma 0152 ( Braba)
# Autor: Moises de Souza Ribeiro
# Data 17/05/2024
# advinhar numeros

# Faça um programa onde o usuário tenta adivinhar o número que o computador está ‘pensando’.

# importando a biblioteca os
import os
# importando a biblioteca random
import random


# limpando o terminal
os.system('cls')

print('-'*70)
print(' adivinhação')
print('='*70)

print('numero aleatorio inteiro')

# entrada
numero = int(input('entre com o numero '))
aleatorio_inteiro = random.randint(1,5)

# saida
if aleatorio_inteiro == numero:
    print(f'parabens {numero} é igual a {aleatorio_inteiro}')

else:
    print(f'errou o numero digitado foi {numero} o numero pensado foi {aleatorio_inteiro}')    