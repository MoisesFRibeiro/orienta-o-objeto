#Faça um programa que receba um número inteiro e mostre o sucessor e antecessor.
# imports
import os


# Limpando a Biblioteca
os.system('cls')

# Entrada

print('_'*70)
valor1 = int(input('entre com seu valor'))

# Processamento
sucessor = valor1 + 1
antecessor = valor1 -1

# Saida
print(f'o numero digitado foi  {valor1} antecessor {antecessor} e sucessor {sucessor}')