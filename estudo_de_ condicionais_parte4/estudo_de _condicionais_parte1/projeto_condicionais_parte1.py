# estudo de condicionais parte1

# curso de desenvolvimento de sistemas 
# turma 0152(braba)
# autor: moises de souza ribeiro
# data: 24/04/2024
# estudo de condicionais parte 1
# objetivo: verificando um valor decimal

import os
 
 
os.system('cls')
 
print('_'*70) 
print('estudo de condicional: parte 1')
print('='*70)
 
# Entrada
valor = float(input('digite o numero decimal: 10  '))
resposta =  ''
 
# condicional
if valor % 2 == 0:
      resposta = f'entrada incorreta,valor {valor: .0f} e um inteiro!'
else:
      resposta = f'entrada correta, o valor{valor} e um decimal!'
# Saida   
print('='*70)
print(resposta)

print('fim do programa!\n')   #  \n salta uma linha     