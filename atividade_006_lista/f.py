# Faça um programa que leia 5 nomes, depois imprima estes nomes com seus respectivos índices.
import os 


os.system.('cls')

soma = 0

nomes = ['joão, maria, thiago, olga, dayse']

for indice, nomes in enumerate(nomes):
    soma += nomes
    print(F'indice: {indice} = nomes: {nomes}')
    