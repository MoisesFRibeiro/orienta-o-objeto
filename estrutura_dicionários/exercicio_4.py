# metodos fromKeys(), get()

import os 


os.system('cls')

meu_dicionário = None

# loop principal do programa
while True:
    print('-'*70)
    print("\n menu de opções:")
    print("1. criar o dicionário fromkeys()")
    print("2. buscar valor de uma chave get()")
    print("3. sair ")
    print('-'*70)

    opção = input("escolha uma opção (1-3): ")

    if opção == '1':
        # criação do meu dicionário usando fromkeys()
        chaves = input("digite as chaves separadas por virgula: ").split(',')
        valor_padrão = input("digite o valor padrão paras as chaves: ")
        meu_dicionário = dict.fromkeys(chaves, valor_padrão)
        print("dicionário criado:", meu_dicionário)

    elif opção == '2':
        # verifica se o dicionário foi criado antes de acessá-lo
        if meu_dicionário is not None:
            chaves = input("digite a chave que deseja buscar: ")
            valor = meu_dicionário.get(chaves, "Chave não encontrada")
            print(f"valor para a chave '{chaves}' : '{valor}'")
        else:
            print("erro! crie um dicionário.")
    elif opção == '3':
        print("saindo do programa.")
        break

    else:
        print("opção invalida. tente novamente.")

