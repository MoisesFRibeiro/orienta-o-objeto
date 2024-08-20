# Faça um programa que receba um valor e mostre sua raiz quadrada. Para raízes que não são exatas, arredonde para cima ou para baixo.
# Faça a validação para números negativos, avisando ao usuário que o resultado será um número complexo.

import os
import math


os.system('cls')

# entrada
numero = int(input('entre_com_Numero'))

# processamento
raizquadrada = math.sqrt('radicando')
arredondar_para_cima = math.ceil('raiz_quadrada')
arredondar_para_baixo = math.floor('raiz_quadrada')
if numero != 0:
    resposta:f'raiz quadrada != 0 {raizquadrada} é um numero complexo'
elif numero < 0:    
    resposta:f'raiz quadrada < 0 {raizquadrada} não é um numero complexo'
else:
    resposta:f'raiz quadrada == 0 {raizquadrada} é um numero positivo'       
# saida
print('-'*70)
print(f'o numero {raizquadrada} arredondado para cima é: {arredondar_para_cima}')
print(f'o numero {raizquadrada} arredondado para baixo é: {arredondar_para_baixo}')
print('-'*70)
