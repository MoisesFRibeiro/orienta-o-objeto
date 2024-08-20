# F) A empresa "LeapYearCheck" está desenvolvendo um software de verificação de anos bissextos para auxiliar usuários na identificação desses anos de forma rápida e precisa.
# Eles precisam de um programa que permita aos usuários inserir um ano e, em seguida, determine se esse ano é bissexto ou não, de acordo com as regras
# estabelecidas pelo calendário gregoriano. Além disso, é necessário realizar a validação de entrada de dados para garantir que o ano inserido pelo usuário
# seja um valor válido, ou seja, um número inteiro positivo.

# curso de desenvolvimento de sistemas 
# turma 0152
# autor: moises de souza ribiero
# data 29/04/2024
# atividade de condicionais: F

# importando a biblioteca 
import os


# limpando a biblioteca
os.system("cls")

print('_'*70)
print('atividade: f')
print('='*70)

# entrada
ano = int(input('entre com o ano '))
if ano % 100 !=0 and ano % 4 == 0:
    print(f'(ano) é bisexto')
    
else: 
    print(f'(ano) não é bisexto')
    
print('_'*70)
 
     