# Crie uma função que verifica se um aluno está cadastrado ou não em um dicionário.
# Se estiver cadastrado, imprima o nome desse aluno e o resto dos seus dados. 
# O dicionário deverá conter nome, matrícula e a data de nascimento do aluno.

import os


os.system('cls')
cadastro = {}

# definindo a função
def cadastrar_aluno(aluno):

    nome = input('nome: ')
    matricula =  input('matricula:')
    data_nascimento =  input('data_ nascimento: ')
    cadastro['nome'] = nome
    cadastro['matricula'] = matricula
    cadastro['data nascimento'] = data_nascimento
  
    print('cadastro de alunos: ')
    print()
    for chave, valor in cadastro.items():
        print(f'{chave}: {valor}')
    return aluno    