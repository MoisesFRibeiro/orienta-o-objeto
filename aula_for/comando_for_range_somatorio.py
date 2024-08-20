import os


os.system('cls')

print('_'*50)
print('estrutura de controle somatorio')
print('_'*50)

print()

soma = 0

for var_iteradora in range(0, 4):
    numero = int(input(f'digite o {var_iteradora+ 1}º numero: '))

    # calculo
    soma += numero # mesma coisa: soma = soma + numero

print('_'*50)
print(f'a somados numeros é: {soma}')
print('-'*50)
print()