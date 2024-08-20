# Crie uma função que verifica se um aluno(a) está cadastrado ou não em um dicionário.
# Se estiver cadastrado, imprima o nome desse aluno e o resto dos seus dados. 
# O dicionário deverá conter nome, matrícula e a data de nascimento do aluno.

# curso de desenvolvimento de sistemas
# Turma 0152 ( Braba)
# Autor: Moises de Souza Ribeiro
# Data 05/08/2024
# verificando cadastro de aluno

import os


os.system('cls')

print('-'*70)
print('verificando cadastro de aluno')
print('='*70)

dicionario_aluno = {'nome': 'wilson',
                    'matricula': '4211','nascimento': '15/07/2001'}


def verificar_aluno():
    if dicionario_aluno['nome'] == 'wilson':
        for chave, valor in dicionario_aluno.items():
            print(f'{chave}: {valor}')
    else:
        print(f'Nome não encontrado no dicionário {dicionario_aluno['nome']}')

verificar_aluno()