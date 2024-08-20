# curso de desenvolvimento de dados
# turma 0152(Braba)
# autor: moises de souza ribeiro
# data: 26/04/2024
# atividade de condicionais: A

# importando as bibliotecas
import os


# limpando o terminal
os.system('cls')

print('_'*70)
print('atividade de condicional: A')
print('='*70)

# entrada
numero = float(input('digite seu numero: '))
resposta = ''

# condicional
if numero % 2 == 0:
    resposta = f'o numero {numero} é par'
else:
    resposta = f'o numero {numero} é impar'
    
# saida 
print('='*70)
print(resposta)

print('fim do programa!')