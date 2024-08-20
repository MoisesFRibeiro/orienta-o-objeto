# curso de desnenvolvimento de sistemas
# turma 0152(braba)
# autor: moises de souza ribeiro
# data: 25/04/2024
# estudo de condicionais parte 2
# obejtivo: praticas com condicionais simples e aninhadas

import os


os.system('cls')

# declarações
a = 10
b = 5
resposta = ''

print('_'*70)
print('estudo de condicional(simples)')
print("_"*70)

# condicionais
if a > b:
        resposta = f'{a} e maior que {b}' 
else:
    resposta = f'{a} não e maior que {b}'
# saida
print('_'*70)
print(resposta)

# declarações
a = 5 
b = 5

print('_'*70)
print('estudo de condicional(aninhada)')
print("_"*70)

if a > b:
        resposta = F'{a} e maior que {b}'
elif a < b:
          resposta = f'{a} e menor que {b}'
else: 
    resposta = f' os valores são iguais a: {a} = {b}'
# saida
print('_'*70)              