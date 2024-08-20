# método del() e os operadores in not in

import os 


os.system('cls')

# inicialização do dicionário de contatos
agenda = {
    'jojo': '99196-3030',
    'Dio' : '99196-5050',
    'jolyne': '99196-6060',
    'lisa-lisa' : '99196-7070',
    'speedwagon' : '99196-8080',
    'zeppeli' : '99196-9090',
    'suzie Q' : '99196-0000',
}

while True:
    os.system('cls')

    print('-'*70)
    print("\nagenda de contatos")
    for nome, telefone in agenda.items():
        print(f'{nome} : {telefone}')
        print('='*70)

# verificar se 'jojo' está no dicionário
    if 'jojo' in agenda:
    print('primeiro teste: verificando se jojo está no dicionário')
    print('VERDADEIRO! jojo está no dicionário')

    else:
    print('FALSO! jojonão está no dicionário')

    print()

# segundo teste: verificar se 'Jhon' não está no dicionário
    if 'jhon' not in agenda:
        print('segundo teste: verificando se jhon não está no dicionário')
        print('VERDADEIRO! jhon não está no dicionário')
    else:
        print('FALSO! jhon está no dicionário')

    print('-'*70)
    print("menu de opções")
    print("1. adicionar um contato")
    print("2. remover um contato")
    print("3. verificar um contato especifico")
    print("4. mostrar agenda")
    print("5. sair")
    print('-'*70)

    opção = input("escolha uma opção de (1-5):")

    if opção == '1':
        # adicionar um contato
        nome = input("digite o nome do contato: ")
        telefone = input("digite o telefone do contato: ")
        agenda[nome] = telefone
        print(f"contato {nome}: {telefone} adicionado.")

    elif opção == '2':
        # remover um contato
        nome = input("digite o nome do contato que deseja remover: ")
        if nome in agenda:
            del agenda[nome] 
            print(f"contato {nome} removido.")
        else:
            print(f"contato {nome} não encontrado na agenda.")

    elif opção == '3': 
        # verificar contato especifico
        nome = input("digite o nome que deseja verificar: ")
        if nome in agenda:
            print(f"contato encontrado - {nome}: {agenda[nome]}")
        else:
            print(f"contato {nome} não encontrado na agenda.")

    elif opção == '4':
        # mostrar a agenda atual
        print("\nagenda de contatos:")
        print(agenda)

    elif opção == '5': 
        print("saindo do programa")
        break
    else:
        print("opção ")                             