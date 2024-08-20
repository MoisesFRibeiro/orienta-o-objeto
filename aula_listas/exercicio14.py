import os


os.system('cls')

print('-'*70)
print('saida com for...enumerate()')
print('='*70)

soma = 0

# criando uma lista 
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# percorrendo a lista com enumerate()
# o comando enumerate adiciona um indice
# para cada valor da nossa lista 
# start opcional, para não começar no indice 0
# enumarete(listanumeros, start = 1)

# para cada numero dentro  da lista  de numeros, enumere com um indice 
for indice, numero in  enumerate(lista_numeros):
    soma += numero # soma os numeros 
    print(f'indice: {indice} = numero: {numero}')

print('-'*70)
print(f'a soma de ')  