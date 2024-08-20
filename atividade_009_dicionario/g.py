# Faça um programa para cadastrar os alunos de uma escola.
# Para os campos, tome como referência o nome do aluno,
# data de nascimento e matrícula.
import os


os.sytem('cls')


print('-'*70)
print('Cadastro de alunos')
print('='*70)

# cadastrando alunos
Nome_do_aluno = input('digite o nome do aluno: ')
data_de_nascimento = input('digite a sua data de nascimento: ')
matricula = input('entre com a matricula do aluno: ')

# cadastro final do aluno
print(f'o cadastro final é nome {Nome_do_aluno}: data de nascimento {data_de_nascimento}: matricula {matricula}')