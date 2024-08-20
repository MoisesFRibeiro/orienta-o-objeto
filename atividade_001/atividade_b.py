# imports
import os
import datetime


os.system('cls')

print('_'*70)
print('Data de Nascimento versus Calculo de Idade')
print('_'*70)

# Entradas
nascimento = int(input('data de nascimento'))

# Processamento
ano_atual = datetime.datetime.now().year
idade = ano_atual - nascimento

# saida
print 
print (f'o calculo da idade é :{idade}')
