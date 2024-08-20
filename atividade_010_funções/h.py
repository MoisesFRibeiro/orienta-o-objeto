# Uma Academia deseja fazer uma pesquisa entre seus clientes para descobrir a média de altura
# e peso de seus clientes. Faça um programa que pergunte a cada um dos clientes da academia seu código,
# nome, altura e peso. Após esse cadastramento, seu programa deverá listar os dados dos clientes e a média.
# Para sair do programa o usuário deverá digitar o valor zero(0). O número de clientes é indefinido.
# Veja a saída no próximo slide.

# curso de desenvolvimento de sistemas
# Turma 0152 ( Braba)
# Autor: Moises de Souza Ribeiro
# Data 05/08/2024
# academia

import os


os.system('cls')

print('_'*70)
print('academia')
print('='*70)

def media_altura_peso():
    soma_peso = 0
    soma_altura = 0
    for aluno in clientes:
        soma_altura += aluno['altura']
        soma_peso += aluno['peso']
    media_altura = soma_altura / len(clientes) if clientes else 0 
    media_peso = soma_peso / len(clientes) if clientes else 0
    return media_altura, media_peso
    
clientes = []

while True:
    media_altura, media_peso  = media_altura_peso()
    codigo = int(input("Digite o código do cliente (ou '0' para terminar): "))
    if codigo == 0:
        break
    
    nome = input("Digite o nome do cliente: ")
    altura = float(input("Digite a altura do cliente: "))
    peso = float(input("Digite o peso do cliente: "))
    # print('Cliente cadastrado com sucesso')
    os.system('cls')
    cliente = {'codigo': codigo,'nome': nome,'altura': altura,'peso': peso}
    clientes.append(cliente)
    
print("\nLista de Clientes:")
# for cliente in clientes:
#     print(f"Código: {cliente['codigo']}")
#     print(f"Nome: {cliente['nome']}")
#     print(f"Altura: {cliente['altura']} metros")
#     print(f"Peso: {cliente['peso']} kg")
print("\nLista de Clientes:")
for cliente in clientes:
    for chave, valor in cliente.items():
        print(f'{chave}: {valor}', end= ' | ')
    print()
print()
print(f'A média de altura dos alunos cadastrados é de {media_altura:.2f}m')
print(f'A média de peso dos alunos cadastrados é de {media_peso:.3f}kg')