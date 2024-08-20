import os 


os.system('cls')

print('-'*70)
print('saida com in e not in')
print('='*70)

# exemplo com in
lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

if (3 in lista_numeros):
    print(lista_numeros)
    posição = lista_numeros.index(3)
    print(f'o numero 3 esta na posição {posição}')
else:
    print('o elemento não consta na listagem')

print()

# exemplo com not in 
lista_nomes = ['john', 'jane', 'carol']

if ('maria' not in lista_nomes):
    # antes
    print(lista_nomes)

    # não esta na lista, acrescentar 
    lista_nomes.append('maria')

    print('\no nome maria foi acrescentado')
    print(lista_nomes)

    print()
    print('-'*70)
    print('fim do programa!')
    print('-'*70)
    