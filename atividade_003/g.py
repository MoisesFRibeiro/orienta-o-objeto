# curso de desenvolvimento de sistemas
# Turma 0152 ( Braba)
# Autor: Moises de Souza Ribeiro
# Data 17/05/2024
# Raiz quadrada

# Faça um programa que peça os valores de a, b e c de uma equação do 2º grau.
# Calcule as raízes da equação do 2º grau seguindo a fórmula: Δ = b² - 4ac, x = (-b ± raiz(Δ)) / (2a).

# importando biblioteca
import os 
#importando bibliotca math
import math


# limpando o terminal
os.system('cls')

print('-'*70)
print('raiz quadrada')
print('-'*70)

# entrada
a =int(input('entre com a '))
b =int(input('entre com b '))
c =int(input('entre com c '))

# processamento
# Δ = b² - 4ac,
# x = (-b ± raiz(Δ)) / (2a).
b2 = math.pow(b, 2)
delta = b2 - (4*a*c )
raizdelta = math.sqrt (delta)
x1 = (-b + raizdelta ) / (2* a )
x2 = (-b - raizdelta ) / (2* a )

# saida 
print(f' a raiz quadrada de  é: {raizdelta}')
print(f'o resultado de x1 é : {x1 }')
print(f'o rwsultado de x2 é : {x2 }')
