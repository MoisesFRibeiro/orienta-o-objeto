# Crie uma função que receba uma lista de números. 
# Depois retorne duas listas com os números pares, os números ímpares,
# a quantidade de números pares e a quantidade de números ímpares.

import os


os.system('cls')

# definindo uma função 
def pegar_par_impar(lista):
    pares = []
    impares = []

# fazendo uma varredura para verificar par impar
    print(f'lista: {lista}')
    for i in lista:
        if (i % 2 == 0):
            pares.append(i)

        else:
            impares.append(i)

# exibindo pares e impares e fazendo a contagem
    print(f'a lista possui: {len(pares)} numeros pares')
    print(f' lista pares: {pares}')
    print()
    print(f'lista possui: {len(impares)} numeros impares')
    print(f'lista impares: {impares}')

# retornando os pares, impares e mostrando a quantidade
    return pares + impares 
print(f'quantidade de pares: pares')
print(f'quantidade de impares: impares')

# lista de numeros
lista = [1, 2, 3, 4, 5, 6,]

# chamando os numeros da lista
pegar_par_impar(lista)

print('fim do programa')