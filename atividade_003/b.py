# Faça um programa que receba 2 valores, faça a divisão entre eles. 
# Se a divisão não for inteira, o programa deverá arredondar o resultado para cima e para baixo.
# Faça a validação para divisão por 0.

import os
import math


os.system('cls')

# entrada de dados
dividendo = int(input('entre com dividendo: '))
divisor = int(input('entre com divisor: '))


if divisor == 0:
    print(f'{divisor} == 0 o numero é valido')
else:
    quociente = dividendo / divisor 
    print(f' a divisão de {dividendo} / {divisor} é: {quociente} ')
    arrendondar_para_cima = math.ceil(quociente)
    arrendondar_para_baixo = math.floor(quociente)
    print(f'o numero{quociente} arredondado para cima é: {arrendondar_para_cima}')
    print(f'o numero{quociente} arredondado para baixo é: {arrendondar_para_baixo}')