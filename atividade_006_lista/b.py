# Crie uma lista com 5 números inteiros. Depois imprima a soma desses valores.
import os


os.system('cls')

lista = [2, 6, 7, 3, 8]

soma = 0

for var_iteradora in range (2, 8):
    numero =int(input(f'{var_iteradora + 1} soma é: '))
soma += numero

print('_'*70)
print('a soma dos numeros é: {soma} ')
print('fim do programa')
print('='*70)