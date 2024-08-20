import os 


os.system('cls')

# lista original
lista = [1, 2, 3, 4]

# pedindo ao usuario parta fornecer a
# posição e o elemento a ser inserido
posição = int(input('posição onde deseja enserir o elemento: '))
elemento = input('elemento a ser inserido: ')

# verificando se a posição inserida pelo usuario e valida
if posição>= 0 and posição <=len(lista):
    # inserindo o elemenmto na lista na posição especificada pelo usuario
    lista.insert(posição, elemento)
    print('lista apos inserção:', lista)
else:
    print(f'posição fora do invtervalo0, {len(lista)}')    