# importando as bibliotecas
import os
import math


# limpando o terminal
os.system('cls')

print('_'*70)
print('estudo da biblioteca matemática math')
print('='*70)
print()

# declarações
base = 2
expoente = 3
angulo = 30
radicando = 81
co = 5 # cateto oposto
ca = 10 # cateto adjacente

# processamento
potencia = math.pow(base, expoente)
raizquadrada = math.sqrt(radicando)
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
hipotenusa = math.hypot(co, ca)

# saida
print(f'{base} elevado a {expoente} é igual a: {potencia}')
print(f' a raiz quadrada de {radicando} é: {raizquadrada}')
print(f'o seno de {angulo} é: {seno: .2f}')
print(f'o cosseno de {angulo} é: {cosseno: .2f}')
print(f' a tangente de {angulo} é {tangente: .2f}')
print(f'o valor da hipotenusa é: {hipotenusa: .2f}')
print('-'*70)