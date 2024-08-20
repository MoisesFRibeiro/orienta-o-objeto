# outros exemplos

import os


os.system('cls')

print('-'*70)
print('---------tabela periodica---------')
print('='*70)

# inicialização do dicionário e da lista 
elementos = {} # dicionário 
periodica = [] # lista

while True:
    os.system('cls')

    # cabeçalho do menu
    print('-'*70)
    print('MENU DE OPÇÕES')
    print('='*70)
    print("1. adicionar um elemento")
    print("2. visualizar todos os elementos ")
    print("3. atualizar um elemento")
    print("4. remover um elemento")
    print("5. sair")
    print('-'*70)

    # solicitação da escolha do usuário
    opção = input("escolha uma opção (1-5): ")
     
    if opção == '1':
        # adicionar um elemento
        simbolo = str(input("simbolo do elemento: "))
        nome = str(input("nome do elemento: "))
        elementos['simbolo'] = simbolo
        elementos[nome] = nome
        periodica.append(elementos.copy())
        input("\nelemento adicionado. pressione enter para continuar...")

    elif opção == '2':
        # visualizar todos os elementos 
        print("\nelementos da tabela periodica:")
        print('-'*70)
        for elemento in periodica:
            for chave, valor in elemento.items():
                print(f'{chave.capitalize()}: {valor}')
            print('-'*70)
        input("\npressione enter para continuar...")

    elif opção == '3':
        # atualizar um elemento
        simbolo = str(input('digite o simbolo do elemento pra atualizar: '))
        # inicializa a flag como false
        encontrado = False
        for elemento in periodica:
            if elemento['simbolo'] == simbolo:
                novo_simbolo = str(input(f'digite o novo simbolo para'
                f'{simbolo} ( ou deixe em branco para menter o atual): '))
                novo_nome = str(input(f'digite o novo nome para'
                f' {simbolo} (ou deixe em branco para manter o atual): '))

                # atualiza o simbolo e o nome for fornecidos
                if novo_simbolo:
                    elemento['simbolo'] = novo_simbolo
                    if novo_nome:
                        elemento['nome'] = novo_nome
                        # define a flag como true quando o elemento é encontrado
                        encontrado = True
                        break
                    if encontrado:
                        input("\nelemento atualizado. enter para continuar....")
                    else:
                        input("\nelemento não encontrado. enter para continuar....")

    elif opção == '4':
      # remover um elemento                              
      simbolo = str(
          input('digite o simbolo do elemento que deseja remover: '))
    encontrado = False # inicializa a flag como false
    for elemento in periodica:
        if elemento['simbolo'] == simbolo:
            periodica.remove(elemento)
            # define a flag como true  quando o elemento é encontrado
            encontrado = True
            break
        if encontrado:
            input("\nelemento removido. enter para continuar.....")
        else:
            input("\nelemento não encontrado. enter para continuar....")

        elif opção == '5':
        print("saindo do programa.")
        break

        else:
        input("opção invalida. enter para tentar novamente....")
    
            
                 