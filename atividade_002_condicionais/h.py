# H) A empresa "RootCalc" está desenvolvendo um software de cálculo de raízes de equações quadráticas para auxiliar engenheiros e cientistas em suas análises e projetos.
# Eles precisam de um programa que calcule as raízes da equação quadrática 𝑥²−6𝑥+5 sem depender de funções ou métodos predefinidos,
# utilizando apenas os conceitos e operações básicas aprendidos até o momento. Essas raízes são conhecidas como 𝑥’ = 5 e 𝑥’’ = 1,
# e o programa deve ser capaz de calcular essas raízes de forma precisa, seguindo os princípios matemáticos fundamentais.

# curso de desenvolvimento de sistemas 
# turma 0152(babra)
# autor: moises de souza ribeiro
# data: 29/04/2024
# atividade de condicionais: h
# equações quadradisticas

import os


os.system('cls')

print('-'*70)
print('calculo de raizes da equação quadridista')
print('='*70)

# numeros da equação
a = 1
b = -6
c = 5

# calcular delta
delta = b**2 - 4*a*c

# condição das raizes
if delta >= 0:
    x1 = (-b + delta **0.5) / (2*a)
    x2 = (-b - delta **0.5) / (2*a)
    print('raizes de equação quadratica x² -6x + 5')
    print(f' x² ={x1}')
    print(f'x" = {x2}')
else:
    print('não ha raizes para equação')
    
print('='*70)        