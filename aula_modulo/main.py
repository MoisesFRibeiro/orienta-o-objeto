import os

from pacote.modulo_somar import somar 
from pacote.subpacote.modulo_multiplicar import multiplicar as multi
from pacote.modulo_divisao import dividir

while True:
    os.system('cls')

    a = input('entre com o valor de A: ')
    b = input('entre com o valor de B: ')

    if not a.replace('-', '' , 1).isdigit() or not b.replace('-', '', 1).isdigit():
        print("por favor , entre com um numero válido.")
        continue

    a = float(a)
    b = float(b)

    resultado_soma = somar(a, b)
    resultado_produto = multi(a, b) # variavel recebendo 2 argumentos posicionais
    resultado_divisão, erro = dividir(a, b) # desenpacotamento

    print('-'*70)
    print('caluculos matematicos')
    print('='*70)
    print(f'calculo da soma: {resultado_soma}')
    print(f'calculo do produto: {resultado_produto}')
    print(f'calculo da divisão: {resultado_divisão}, {erro}') # validação
    print('-'*70)

    sair = input("deseja sair do programa? (s/n): ").strip().lower()
    if sair == 's':
        print("saindo do programa...")
        break
