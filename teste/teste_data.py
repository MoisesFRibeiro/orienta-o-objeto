import os
from datetime import datetime 
from datetime import date


os.system('cls')

# declarando uma variavel para data
data = datetime.now()
data_atual = input('data_atual').strip()
nascimento = input('nascimento').strip()

# variavel data formatada
data_formatada = data.strftime('%d/%m/%y')


aniversario = data.strftime('%y')
idade = aniversario.year - nascimento
print(data_formatada, aniversario)