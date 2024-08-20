# Faça um programa que calcule os números primos em um intervalo pré-determinado pelo usuário

# curso de desenvolvimento de sistemas 
# turma 0152(braba)
# autor: moises de souza ribeiro
# data: 03/06/2024
# números primos
# intervalo pré determinado


import os


os.system('cls')

print('_'*70)
print('numeros primos')
print('-'*70)

# variaveis
numero_incial = 0
numero_final = 0

# entrada 
numero_incial = int(input('informe o primeiro numero do intervalo: ')) + 1
numero_final = int(input('informe o numero final do intervalo: ')) + 1

# calculando os numeros primos
if numero_incial < 2: # nao existe numero primo menor que 2
   numero_incial = 2

# verificndo se é divisivelpor outro numero
for i in range(numero_incial, numero_final):
      for i2 in range(numero_incial, i):
       if i % i2 != 0:
        break
else:
    print(i)
print('-'*70)
print('fim do programa')