# metodos items(), keys() e values()

import os


os.system('cls')

meu_dicionário = {}

while True:
    print('-'*70)
    print("\nmenu de opções")
    print("1. adicionar um par chave_valor")
    print("2. mostrar chaves do dicionário")
    print("3. mostar valores do dicionário")
    print("4. mostar intens do dicionário")
    print("5. sair")
    print("-"*70)

    opção = input("escolha uma opção (1-5): ")

    if opção == '1':
        # adicionar um par chave valor ao dicionário
        chave = input("digite a chave: ")
        valor = input("digite o valor: ")
        meu_dicionário[chave] = valor
        print(f"par {chave} : {valor} adicionado.")

    elif opção == '2':
        # mostra as chaves dodicionário usando keys()
        if meu_dicionário:
            print("chaves do dicionário:", meu_dicionário.keys())
        else:
            print("o dicionário esta vazio. adicione itens primeiro")

    elif opção == '3':
        # mostra os valores do dicionário usando values()
        if meu_dicionário:
            print("valores do dicionário:", meu_dicionário.values())
        else:
            print("o dicionário esta vazio. adicione intens primeiro.")

    elif opção == '4':
        # mostra os itens (chave-valor) do diconário usando intems()
        if meu_dicionário:
            print("intens do dicionário", meu_dicionário.items())
        else:
            print("dicionário vazio. adicione itens primeiro.")

    elif opção == '5':
        # sai do programa
        print("saindo do programa.")
        break

    else:
        #  mensagem pra opção invalida
        print("opção invalida. tente novamente")