# Crie uma função que receba uma lista de números. Depois retorne duas listas com os números pares,
# os números ímpares, a quantidade de números pares e a quantidade de números ímpares.

# curso de desenvolvimento de sistemas
# Turma 0152 ( Braba)
# Autor: Moises de Souza Ribeiro
# Data 05/08/2024
# lista de numeros

import os 


os.system('cls')

print('_'*70)
print('lista de numeros')
print('='*70)

# criando uma lista de numeros 
lista_numeros = []
pares = []
impares = []

# separando pares de impares e contando a quantidade
def lista(lista_numeos):
    par = 0
    impar = 0
    for i in lista_numeros:
        i = int(i)
        if i % 2 == 0:
            pares.append(i)
            par += 1
        else:
            impares.append(i)
            impar += 1
            return par,impar

def adicionando_valores():
    while True:
        valor = input('adicione um valor: ').strip()
        lista_numeros.append(valor)
        continuar = input(
            'deseja inserir valores(s - sim)? ').lower().strip()
        if continuar == 's'or (valor == '' and not valor.isnumeric()):
            break

    while True:
        adicionando_valores()
        par ,impar = lista

        print(f'esiste {par} os numeros pares são: {pares}')
        print(f'esiste {impar} os numeros impares são: {impares} ')