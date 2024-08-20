# G) Você está desenvolvendo um programa para determinar se três segmentos podem formar um triângulo.
# Para isso, o programa precisa receber as medidas dos três segmentos e compará-las entre si.
# A resposta resultante dessa comparação deve indicar se os segmentos fornecidos podem formar um triângulo ou não.

# curso de desenvolvimento de sistemas 
# turma 0152(braba)
# autor: moises de souza ribeiro
# data: 29/04/2024
# forma de um triangulo
# descobrir a forma de um triangulo

# importando a biblioteca
import os


# limpando a biblioteca
os.system('cls')

print('-'*70)
print('forma de um triangulo')
print('='*70)

# entrada 
a = float(input('entre a'))
b = float(input('entre b'))
c = float(input('entre c'))

# maior que >

if a + b > c and a + c > b and b + c > a:
    print(f'os valores podem formar um triangulo')
else:
    print(f'os valores nao podem formar um triangulo')    
    
    
