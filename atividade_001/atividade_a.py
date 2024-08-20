# imports
import os


os.system('cls')

print('-'*70)
print('soma e multiplicar dos valores')
print('-'*70)

# Entrada
nota1 = float(input('1ª nota: '))
nota2 = float(input('2ª nota: '))
nota3 = float(input('3ª nota: '))

# Processamento
soma = nota1 + nota2 + nota3
multiplicar = nota1 * nota2 * nota3

# saida
print (f'a soma dos números é : {soma}')
print (f'a multiplicacao dos numeros é :{multiplicar} ')
