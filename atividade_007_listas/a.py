# Faça um programa que leia um número indeterminado de notas (pressione ‘s’ ou ‘0’ para sair). 
# Após esta entrada de dados, faça o seguinte:
# Mostre a quantidade de notas que foram lidas.
# Exiba todas as notas na ordem em que foram informadas.
# Exiba todas as notas na ordem inversa à que foram informadas, uma abaixo da outra.
# Calcule e mostre a soma das notas.
# Calcule e mostre a média das notas.

# curso de desenvolvimento de sistemas
# Turma 0152 ( Braba)
# Autor: Moises de Souza Ribeiro
# Data 19/06/2024
# listas

import os


os.system('cls')
soma = 0
contador = 1
notas = []
medias = notas

notas = int(input('digite aqui suas notas:' ))  
while_true:
            
if notas == 's' or notas == '0':
    print(f'leitura interrompida no {'s'} or {'0'}')
notas_para_contar = int(input('digite notas para contar:' ))
contagem_notas = notas.count(notas)    
if notas == 'asc':
    notas.sort()
    print(f'lista de notas ordem ascendente:' )
elif notas == 'desc':
    notas.sort(reverse = True) 
    print(f'lista de notas ordem descendente:' )

for indice, notas in enumerate (notas):
   soma += notas
print(f' indice: {soma} = notas {notas}')

media = soma * notas
print(f'media: {media}')

notas = []
for i in range(0,5):
    valor = int(input('digite a nota: '))
    if (valor < 0):
        print('fim')
