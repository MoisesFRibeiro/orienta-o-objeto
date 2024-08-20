# Faça um programa que procure na lista numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] e produza:
# O intervalo de 1 até 9
# O intervalo de 8 até 13
# Os números pares
# Os números impares
# Os múltiplos de 2, 3 e 4
# Lista reversa
# O produto dos intervalos 5-6 por 11-12

# curso de desenvolvimento de sistemas
# Turma 0152 ( Braba)
# Autor: Moises de Souza Ribeiro
# Data 19/06/2024
# listas

import os


os.system('cls')
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15] 

for indice in enumerate(lista):

    if 1 <= indice and 9 <= len(lista):
        print(f'o intervalo de 1 a 9 é: ')lista.extend()
if 8 <= indice and 13 <= len(lista):
        print(f'o intervalo de 8 a 13 é: ')lista.extend()
soma = 0
for var_iteradora in range(1, 15):
     numero = int(input(f'{var_iteradora + 1}º numero'))
     if (numero % 2 == 0):
        print(f'o numero {numero} é par')
else:
        print(f'o numero {numero} é impar')
for lista in numero:
     if(numero % 2 == 0):
       mutiplos2 = lista.append(lista)
for lista in numero:
     if(numero % 3 == 0):
       mutiplos3 = lista.append(lista) 
for lista in numero:
     if(numero % 4 == 0):
       mutiplos4 = lista.append(lista)
if lista == lista:
        lista.reverse()
        print('lista invertida:', lista) 
for indice in enumerate(lista):
     if 5-6 <= indice and 11-12 <= len(lista):
          print(f'o produto dos intervalos entre 5-6 por 11-12 são: ')        




