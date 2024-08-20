# Crie uma função que cadastre o nome de um aluno(a), a matrícula e a data de nascimento.
# Depois imprima os resultados cadastrados utilizando uma estrutura de repetição for.

# curso de desenvolvimento de sistemas
# Turma 0152 ( Braba)
# Autor: Moises de Souza Ribeiro
# Data 05/08/2024
# cadastro de alunos

import os 


os.system('cls')

print('-'*70)
print('cadastro de aluno')
print('='*70)

cadastro = []
alunos = {}

def cadastrar(aluno):
    alunos = aluno
    cadastro.append(alunos.copy())
    
    def mostrar():
        for item in cadastro:
            for b, w  in item.items():
                print(f'{b}:'{w}', end= |')
                print()
while True:
    menu = input('1 -cadastrar | 2 -esibir | 0 -sair ')
    if menu == '1':
        while True:
            nome = input('insira aqui o nome do aluno: ').title().strip()
            matricula = input('insira aqui o numero de matricula: ')
            data_nascimento = input('insira aqui sua data de nascimento: dd/mm/aaaa')
            cadastrar(nome = nome, matricula = matricula, data_nascimento = data_nascimento)
            break

    elif menu == '2':
        esibir()
        input('pressione enter')
    elif menu == '0':
        print('fim')
        break    