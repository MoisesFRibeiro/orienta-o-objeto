# Crie um programa que realiza a contagem de 1 até 100, usando apenas de números ímpares,
# ao final do processo exiba na tela quantos números ímpares foram encontrados nesse intervalo,
# assim como a soma dos mesmos.

import os 


os.system('cls')

print('-'*70)
print('contando numeros impares')
print('='*70)

# variaveis
contador = 0
soma = 0

# realizando a contagem
for var_iteradora in range(1, 100, 2):
   contador = contador+ 1
   soma += var_iteradora

print(f'de 1 a 100 foram encontrados {contador} numeros impares')
print (f'e a soma dos numeros impares é: {soma}')

