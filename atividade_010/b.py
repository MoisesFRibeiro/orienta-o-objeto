# Crie uma função que cadastre o nome de uma aluno, a matrícula e a data de nascimento.
# Depois imprima os resultados cadastrados utilizando uma estrutura de repetição for. 

import os 


os.system('cls')

aluno = []
matricula = []
data_nascimento = []

# definindo a funçaõ cadastrar aluno
def cadastrar_aluno(aluno, matricula, Dt_nascimento):

aluno = input()('entre com o nome do aluno')
matricula = input('entre com a matricula do aluno: ')
data_nascimento = input('entre com o nascimento do aluno: ')


print(f'o nome do aluno cadastrado é: {aluno}')
print(f'a matricula do aluno é: {matricula}')
print(f'o nascimento do aluno é: {data_nascimento}')