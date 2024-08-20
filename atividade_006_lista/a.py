# Crie a lista [1, 2, 3, 5, 6] e depois insira o valor que está faltando na posição correta.
import os


os.system('cls')

<<<<<<< HEAD
lista_numeros = [1, 2, 3, 5, 6]
posição = int(input('posição onde deseja o elemento: '))
elemento = input('elemento a ser inserido: ')

if posição >= 0 and posição <= len(lista_numeros):
    lista_numeros.insert(posição, elemento)
    print('lista após inserção', lista_numeros)
else:
    print((f'a posição fora do intervalo 0,{len(lista_numeros)} '))    
=======
print('-'*70)
print('criando lista')
print("-"*70)

lista_numeros = [1, 2, 3, 5, 6]
lista_numeros.insert()
for i in range(1):
    numero = int(input('digite o numero: ')) 

numero_verfificar = int(input('digite o numero: '))

if numero_verfificar in lista_numeros:
    print(f'o numero {numero_verfificar} esta na lista')
else:
    print(f'o numero {numero_verfificar} não esta na lista')    
>>>>>>> d1f4d1a1432730ab8797bf9e197d721f6d54e303
