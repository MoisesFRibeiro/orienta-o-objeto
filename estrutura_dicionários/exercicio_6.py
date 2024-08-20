# metodos pop() e popitem()

import os


os.system('cls')

meu_dicionário = {}

while True:
    print('-'*70)
    print("\nmenu de opções:")
    print("1. adcicionar um par chave-valor")
    print("2. remover um intem usando pop()")
    print("3. remover o ultimo item usando popitem()")
    print("4. mostrar o dicionário atual")
    print("5. sair")
    print('-'*70)

    opção = input("escolha uma opção (1- 5): ")

    if opção  == '1':
        # adicionar um par chave valor ao dicionário
        chave = input("digite a chave: ")
        valor = input("digite o valor: ")
        meu_dicionário[chave] = valor
        print(f"par {chave} : {valor} adicionado.")

    elif opção == '2':
        # remover um item especifico usando pop()
        if meu_dicionário:
            chave = input("digite a chave do item que deseja remover: ")
            valor_removido = meu_dicionário.pop(chave, "chave não encontrada")
            print(f"item removido: {chave} : {valor_removido}")
        else:
            print("o dicionário está vazio. adicione itens primeiro.")

    elif opção == '3': 
        # remover o ultimo item usando popitem()
        if meu_dicionário:
            chave, valor = meu_dicionário.popitem() 
            print(f"ultimo item removido: {chave} : {valor}")
        else:
            print("o dicionário está vazio. adicione items primeiro.")

    elif opção == '4':
        # mostrar o dicionário atual
        if meu_dicionário:
            print("dicionario atual:", meu_dicionário) 
        else:
            print("o dicionário esta vazio.")

    elif opção == '5':
        print("saindo do programa.")
        break 

    else:
        print("opção invalida. tente novamente.")                                   