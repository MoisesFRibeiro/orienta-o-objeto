import os


os.system('cls')

# inicializa uma lista de exemplo
lista_numeros = [10, 20, 30, 40, 50,60, 70, 80, 90, 100]

# solicita ao usuario para inserir um indice para remover o elemento
indice = int(input('digite o indicce do elemento a ser removido (0-9): '))

# verifica  se o indice esta dentro  do intervalo valido na lista 
if 0 <= indice < len( lista_numeros):
    # remove o elemnto no indice especioficado e exibe-o 
    elemento_removido = lista_numeros.pop(indice)
    print(f'elemento removido: {elemento_removido}')
else:
    print('indice invalido!')

# exibe a lista resultante
print('lista apos a remoção:', lista_numeros)