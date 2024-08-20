# metodos clear(), copy(), len(),

import os 


os.system('cls')

# criação do dicionário vazio
meu_dicionário = {}

while True:
    print('-'*70)
    # exibição do menu de opções 
    print("\nmenu de opções:")
    print("1. adicionar um par chave-valor")
    print("2. mostrar o dicionário")
    print("3. mostrar o tamanho do dicionário")
    print("4. fazer uma cópia do dicionário")
    print("5. limpar o dicionário")
    print("6. sair")
    print('-'*70)

    # solicitação da escolha do usuario
    opção = input("escolha uma opção (1-6): ")

    if opção == '1':
        # adciona um novo par chave-valor ao dicionário
        chave = input("digite a chave: ")
        valor = input("digite o valor: ")
        meu_dicionário[chave] = valor
        print(f"par {chave}: {valor} adicionado.")

    elif opção == '2':
        # exbe o meu dicionário atual
        print("dicionario atual: ", meu_dicionário)

    elif opção == '3':
        # mostra o tamanho do dicionário usando len()
        tamanho = len(meu_dicionário)
        print(f'o dicionário tem {tamanho} elementos.')

    elif opção == '4':
        # cria uma lista do dicionário usando copy() e exibe a cópia
        copia_dicionário = meu_dicionário.copy()
        print("copia do dicionário: ", copia_dicionário)

    elif opção == '5':
        # limpa o dicionário usando clear()
        meu_dicionário.clear()
        print("dicionário limpo")

    elif opção == '6':
        # sai do programa
        print('saindo do programa!.')
        break

    else:
        # mensagem para opção invalida
        print("opção invalida. tente novamente.")