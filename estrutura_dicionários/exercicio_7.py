# metodos setdefaul() e update()

import os 


os.system('cls')

meu_dicionário = {}

while True:
    print('-'*70)
    print("\nmenu de opções:")
    print("1. adicionar um par chave valor")
    print("2. definir valor padrão para uam chave usando setdefault()")
    print("3. atualiza o dicionário usando update()")
    print("4. mostrar o dicionário atual")
    print("5. sair")
    print('_'*70)
    opção = input("escolha uma opção (1- 5): ")

    if opção == '1':
        # adiciona um par chave valor ao dicionário
        chave = input("digite a chave: ")
        valor = input("digite o valor: ")
        meu_dicionário[chave] = valor
        print(f"par {chave} : {valor} adicionado.")

    elif opção == '2': 
        # definir valor padrão para uma chave usando setdefault()
        chave = input("digite a chave para definir um valor padrão: ")
        valor_padrão = input("digite o valor padrão: ")
        valor_existente = meu_dicionário.setdefault(chave, valor_padrão)
        print(f"valor para a chave '{chave}' : {valor_existente}")

    elif opção == '3':
        # atualiza o dicionário usando update() 
        novos_pares = input("digite os novos pares chave-valor: ")
        novos_pares_lista = novos_pares.split(',')
        novos_dados = {}
        for par in novos_pares_lista:
            chave, valor = par.split(':')
            novos_dados[chave] = valor
        meu_dicionário.update(novos_dados)
        print("dicionário atualizado:", meu_dicionário) 

    elif opção == '4':
        # mostra o dicionário atual 
        if meu_dicionário:
            print("dicionário atual:", meu_dicionário)
        else:
            print("o dicionário está vazio")

    elif opção == '5':
        # sai do programa
        print("saindo do programa.")
        break

    else:
        #mensagem para opção invalida
        print("opção invalida. tente novamente")