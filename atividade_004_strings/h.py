# Faça um programa que leia o nome de um aluno e mostre quantas vezes a letra 'o'
# aparece e em que posição ela aparece pela primeira e última vez.

# curso de desenvolvimento de sistemas 
# turma 0152(braba)
# autor: moises de souza ribeiro
# data: 27/05/2024
# quantas vezes aparece a letra "o"
# posição que aparece

import os


os.system('cls')

# entrada
nome_aluno = input('digite o nome do aluno: ')
letra = 'o'
contador = 'o'
primeira_posicao = -1
ultima_posicao = -1

# processamento
for i in range(len(nome_aluno)):
    if nome_aluno [i] == 'o' or nome_aluno[i] == 'o':
        contador += 1
    if primeira_posicao == -1:    
        primeira_posicao = i
    ultima_posicao = i

# saida
print(f"quantidade de vezesque a letra 'o' aparece: {contador}")
print(f'posicao da primeira ocorrencia: {primeira_posicao}')
print(f'posicao da ultima ocorrencia: {ultima_posicao}')
print('='*80)
print()